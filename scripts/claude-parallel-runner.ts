#!/usr/bin/env bun

import { spawn } from "node:child_process";
import { promises as fs } from "node:fs";
import path from "node:path";

type SkillEntry = {
  slug: string;
  skillPath: string;
};

type Options = {
  skillsRoot: string;
  includeFile?: string;
  excludeFile?: string;
  promptFile: string;
  outputDir: string;
  command: string;
  model: string;
  maxTurns: number;
  sample?: number;
  all: boolean;
  concurrency: number;
  timeoutMs: number;
  retries: number;
  dryRun: boolean;
  seed: number;
};

type RunResult = {
  slug: string;
  skillPath: string;
  status: "success" | "failed" | "timeout" | "invalid_output";
  attempts: number;
  durationMs: number;
  exitCode: number | null;
  outputFile?: string;
  error?: string;
};

type ParsedClaudeOutput = {
  text: string;
  subtype?: string;
  payloadType?: string;
};

function printHelp(): void {
  console.log(`claude-parallel-runner

Run claude -p across many skills in parallel with include/exclude filters.

Usage:
  bun runner/claude-parallel-runner.ts [options]

Options:
  --skills-root <path>      Skills directory root (default: ./casemark-skills/skills/legal)
  --prompt-file <path>      Prompt template file (required)
  --include-file <path>     Optional newline-delimited include slug list
  --exclude-file <path>     Optional newline-delimited exclude slug list
  --output-dir <path>       Output directory root (default: ./output)
  --command <name>          CLI command to run (default: claude)
  --model <name>            Model name passed to --model (default: claude-opus-4-6)
  --max-turns <number>      Max turns for claude call (default: 8)
  --sample <number>         Run only a sampled subset
  --all                     Run all eligible skills (default when --sample is not set)
  --concurrency <number>    Parallel workers (default: 4)
  --timeout-ms <number>     Per-skill timeout in ms (default: 180000)
  --retries <number>        Retries after first attempt (default: 1)
  --seed <number>           Seed used for sampling (default: 42)
  --dry-run                 Print selected skills without executing
  --help                    Show this help

Prompt template variables:
  {{SKILL_SLUG}}
  {{SKILL_PATH}}
  {{SKILL_CONTENT}}
`);
}

function parseArgs(argv: string[]): Options {
  const options: Options = {
    skillsRoot: path.resolve(process.cwd(), "casemark-skills/skills/legal"),
    promptFile: "",
    outputDir: path.resolve(process.cwd(), "output"),
    command: "claude",
    maxTurns: 8,
    all: false,
    concurrency: 4,
    timeoutMs: 180_000,
    retries: 1,
    dryRun: false,
    seed: 42,
    model: "claude-opus-4-6",
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    const next = argv[i + 1];

    if (arg === "--help" || arg === "-h") {
      printHelp();
      process.exit(0);
    } else if (arg === "--skills-root" && next) {
      options.skillsRoot = path.resolve(process.cwd(), next);
      i += 1;
    } else if (arg === "--prompt-file" && next) {
      options.promptFile = path.resolve(process.cwd(), next);
      i += 1;
    } else if (arg === "--include-file" && next) {
      options.includeFile = path.resolve(process.cwd(), next);
      i += 1;
    } else if (arg === "--exclude-file" && next) {
      options.excludeFile = path.resolve(process.cwd(), next);
      i += 1;
    } else if (arg === "--output-dir" && next) {
      options.outputDir = path.resolve(process.cwd(), next);
      i += 1;
    } else if (arg === "--command" && next) {
      options.command = next;
      i += 1;
    } else if (arg === "--model" && next) {
      options.model = next;
      i += 1;
    } else if (arg === "--max-turns" && next) {
      options.maxTurns = Number(next);
      i += 1;
    } else if (arg === "--sample" && next) {
      options.sample = Number(next);
      i += 1;
    } else if (arg === "--all") {
      options.all = true;
    } else if (arg === "--concurrency" && next) {
      options.concurrency = Number(next);
      i += 1;
    } else if (arg === "--timeout-ms" && next) {
      options.timeoutMs = Number(next);
      i += 1;
    } else if (arg === "--retries" && next) {
      options.retries = Number(next);
      i += 1;
    } else if (arg === "--seed" && next) {
      options.seed = Number(next);
      i += 1;
    } else if (arg === "--dry-run") {
      options.dryRun = true;
    } else {
      throw new Error(`Unknown or incomplete argument: ${arg}`);
    }
  }

  if (!options.promptFile) {
    throw new Error("--prompt-file is required");
  }

  if (options.concurrency < 1) {
    throw new Error("--concurrency must be >= 1");
  }

  if (options.retries < 0) {
    throw new Error("--retries must be >= 0");
  }

  if (options.maxTurns < 1) {
    throw new Error("--max-turns must be >= 1");
  }

  return options;
}

async function pathExists(targetPath: string): Promise<boolean> {
  try {
    await fs.access(targetPath);
    return true;
  } catch {
    return false;
  }
}

async function readSlugList(filePath?: string): Promise<Set<string>> {
  if (!filePath) {
    return new Set<string>();
  }

  const content = await fs.readFile(filePath, "utf8");
  const rows = content
    .split(/\r?\n/g)
    .map((line) => line.trim())
    .filter((line) => line.length > 0 && !line.startsWith("#"));

  return new Set(rows);
}

async function findSkills(skillsRoot: string): Promise<SkillEntry[]> {
  const stack = [skillsRoot];
  const found: SkillEntry[] = [];

  while (stack.length > 0) {
    const current = stack.pop();
    if (!current) {
      continue;
    }

    const entries = await fs.readdir(current, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(current, entry.name);
      if (entry.isDirectory()) {
        stack.push(fullPath);
        continue;
      }

      if (entry.isFile() && entry.name === "SKILL.md") {
        const slug = path.basename(path.dirname(fullPath));
        found.push({
          slug,
          skillPath: fullPath,
        });
      }
    }
  }

  return found.sort((a, b) => a.slug.localeCompare(b.slug));
}

function createSeededRng(seed: number): () => number {
  let value = seed >>> 0;
  return () => {
    value = (value + 0x6d2b79f5) | 0;
    let t = Math.imul(value ^ (value >>> 15), 1 | value);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function sampleSkills(skills: SkillEntry[], count: number, seed: number): SkillEntry[] {
  if (count >= skills.length) {
    return [...skills];
  }

  const copy = [...skills];
  const random = createSeededRng(seed);
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }

  return copy.slice(0, count).sort((a, b) => a.slug.localeCompare(b.slug));
}

function stripCodeFences(value: string): string {
  let result = value.trim();
  if (result.startsWith("```")) {
    const firstBreak = result.indexOf("\n");
    if (firstBreak > -1) {
      result = result.slice(firstBreak + 1);
    }
  }
  if (result.endsWith("```")) {
    result = result.slice(0, -3);
  }
  return result.trim();
}

function isFrontmatterBlock(content: string): boolean {
  return /^name\s*:/m.test(content) && /^description\s*:/m.test(content);
}

function findPreviousNonEmptyLine(lines: string[], index: number): string | undefined {
  for (let i = index - 1; i >= 0; i -= 1) {
    const trimmed = lines[i].trim();
    if (trimmed.length > 0) {
      return trimmed;
    }
  }
  return undefined;
}

function findFrontmatterRange(
  lines: string[],
): { start: number; end: number; insideFence: boolean } | undefined {
  for (let start = 0; start < lines.length; start += 1) {
    if (lines[start].trim() !== "---") {
      continue;
    }

    for (let end = start + 1; end < lines.length; end += 1) {
      if (lines[end].trim() !== "---") {
        continue;
      }

      const frontmatterContent = lines.slice(start + 1, end).join("\n");
      if (!isFrontmatterBlock(frontmatterContent)) {
        continue;
      }

      const previous = findPreviousNonEmptyLine(lines, start);
      return {
        start,
        end,
        insideFence: previous !== undefined && previous.startsWith("```"),
      };
    }
  }

  return undefined;
}

function trimTrailingNoise(lines: string[]): string[] {
  const appendixPatterns = [
    /^##+\s+summary of changes\b/i,
    /^\*\*changes made:?\*\*/i,
    /^\*\*changes from the original:?\*\*/i,
    /^key changes made:?$/i,
    /^key changes made in (?:(?:the|this) )?rewrite:?$/i,
    /^(?:[-*]\s+)?(?:#{1,6}\s*)?key changes made in (?:(?:the|this) )?rewrite:?$/i,
    /^would you like me\b/i,
    /^want me to write this to disk\??/i,
    /^want me to write (?:the|this) file\??/i,
    /^it looks like the file write needs permission\b/i,
    /^changes from the original:?$/i,
  ];

  let cutAt = lines.length;
  for (let i = 0; i < lines.length; i += 1) {
    const line = lines[i].trim();
    if (appendixPatterns.some((pattern) => pattern.test(line))) {
      cutAt = i;
      break;
    }
  }

  const trimmed = lines.slice(0, cutAt);
  while (trimmed.length > 0) {
    const last = trimmed[trimmed.length - 1].trim();
    if (last === "" || last === "```" || last === "---") {
      trimmed.pop();
    } else {
      break;
    }
  }

  return trimmed;
}

function extractFromLines(rawLines: string[]): string | undefined {
  const frontmatter = findFrontmatterRange(rawLines);
  if (!frontmatter) {
    return undefined;
  }

  let endOfDocument = rawLines.length;
  if (frontmatter.insideFence) {
    const fenceIndex = rawLines.findIndex(
      (line, index) => index > frontmatter.end && line.trim().startsWith("```"),
    );
    if (fenceIndex !== -1) {
      endOfDocument = fenceIndex;
    }
  }

  const lines = rawLines.slice(frontmatter.start, endOfDocument);
  const cleaned = trimTrailingNoise(lines);
  const output = cleaned.join("\n").trim();
  if (!output.startsWith("---")) {
    return undefined;
  }

  const boundary = output.split(/\r?\n/g);
  const secondBoundary = boundary.findIndex((line, index) => index > 0 && line.trim() === "---");
  if (secondBoundary === -1) {
    return undefined;
  }

  const header = boundary.slice(1, secondBoundary).join("\n");
  if (!isFrontmatterBlock(header)) {
    return undefined;
  }

  return output;
}

function extractSkillMarkdown(value: string): string | undefined {
  const normalized = value.replace(/\r\n/g, "\n").replace(/^\uFEFF/, "").trim();
  if (!normalized) {
    return undefined;
  }

  const sanitized = normalized
    .replace(/^markdown\s*\n/i, "")
    .replace(/^```(?:md|markdown)\s*\n/i, "")
    .trim();

  const direct = extractFromLines(sanitized.split("\n"));
  if (direct) {
    return direct;
  }

  const fenceExtracted = stripCodeFences(sanitized);
  const fencedDirect = extractFromLines(fenceExtracted.split("\n"));
  if (fencedDirect) {
    return fencedDirect;
  }

  const fencedMatches = Array.from(sanitized.matchAll(/```(?:md|markdown)?\s*([\s\S]*?)```/gi));
  for (const match of fencedMatches) {
    const content = (match[1] ?? "").trim();
    const extracted = extractFromLines(content.split("\n"));
    if (extracted) {
      return extracted;
    }
  }

  return undefined;
}

function normalizeDocument(value: string): string {
  return value
    .replace(/```markdown\b/gi, "```")
    .replace(/```md\b/gi, "```")
    .trim();
}

function renderPrompt(template: string, skill: SkillEntry, content: string): string {
  return template
    .replaceAll("{{SKILL_SLUG}}", skill.slug)
    .replaceAll("{{SKILL_PATH}}", skill.skillPath)
    .replaceAll("{{SKILL_CONTENT}}", content);
}

async function runClaude(
  command: string,
  args: string[],
  timeoutMs: number,
): Promise<{
  stdout: string;
  stderr: string;
  exitCode: number | null;
  timedOut: boolean;
}> {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, {
      stdio: ["ignore", "pipe", "pipe"],
      env: process.env,
    });

    let stdout = "";
    let stderr = "";
    let timedOut = false;

    child.stdout.on("data", (chunk) => {
      stdout += String(chunk);
    });
    child.stderr.on("data", (chunk) => {
      stderr += String(chunk);
    });
    child.on("error", (error) => {
      reject(error);
    });

    const timeoutId = setTimeout(() => {
      timedOut = true;
      child.kill("SIGTERM");
      setTimeout(() => {
        if (!child.killed) {
          child.kill("SIGKILL");
        }
      }, 5000);
    }, timeoutMs);

    child.on("close", (exitCode) => {
      clearTimeout(timeoutId);
      resolve({ stdout, stderr, exitCode, timedOut });
    });
  });
}

function parseClaudeOutput(stdout: string): ParsedClaudeOutput {
  const trimmed = stdout.trim();
  if (!trimmed) {
    return { text: "" };
  }

  try {
    const parsed = JSON.parse(trimmed) as Record<string, unknown>;
    const resultCandidate = parsed.result ?? parsed.text;
    if (typeof resultCandidate === "string") {
      return {
        text: resultCandidate,
        subtype: typeof parsed.subtype === "string" ? parsed.subtype : undefined,
        payloadType: typeof parsed.type === "string" ? parsed.type : undefined,
      };
    }
    return {
      text: "",
      subtype: typeof parsed.subtype === "string" ? parsed.subtype : undefined,
      payloadType: typeof parsed.type === "string" ? parsed.type : undefined,
    };
  } catch {
    return { text: trimmed };
  }
}

async function main(): Promise<void> {
  const options = parseArgs(process.argv.slice(2));
  const promptTemplate = await fs.readFile(options.promptFile, "utf8");

  if (!(await pathExists(options.skillsRoot))) {
    throw new Error(`Skills root not found: ${options.skillsRoot}`);
  }

  const includeSlugs = await readSlugList(options.includeFile);
  const excludeSlugs = await readSlugList(options.excludeFile);

  const allSkills = await findSkills(options.skillsRoot);
  let selected = allSkills.filter((skill) => {
    if (includeSlugs.size > 0 && !includeSlugs.has(skill.slug)) {
      return false;
    }
    if (excludeSlugs.has(skill.slug)) {
      return false;
    }
    return true;
  });

  if (options.sample && options.sample > 0) {
    selected = sampleSkills(selected, options.sample, options.seed);
  } else if (!options.all) {
    selected = [...selected];
  }

  if (selected.length === 0) {
    throw new Error("No skills selected after include/exclude filters");
  }

  console.log(`Total discovered skills: ${allSkills.length}`);
  console.log(`Selected skills: ${selected.length}`);
  console.log(`Concurrency: ${options.concurrency}`);
  console.log(`Retries: ${options.retries}`);
  console.log(`Timeout(ms): ${options.timeoutMs}`);
  console.log(`Command: ${options.command}`);
  console.log(`Model: ${options.model}`);

  if (options.dryRun) {
    console.log("\nDry-run selected slugs:");
    for (const skill of selected) {
      console.log(`- ${skill.slug}`);
    }
    return;
  }

  const runId = new Date().toISOString().replace(/[:.]/g, "-");
  const runDir = path.join(options.outputDir, runId);
  const promptDir = path.join(runDir, "prompts");
  const rawDir = path.join(runDir, "raw");
  const rewritesDir = path.join(runDir, "rewrites");
  await fs.mkdir(promptDir, { recursive: true });
  await fs.mkdir(rawDir, { recursive: true });
  await fs.mkdir(rewritesDir, { recursive: true });

  const resultsPath = path.join(runDir, "results.jsonl");
  const results: RunResult[] = [];
  const queue = [...selected];
  let completed = 0;

  async function processSkill(skill: SkillEntry): Promise<void> {
    const start = Date.now();
    const skillContent = await fs.readFile(skill.skillPath, "utf8");
    const prompt = renderPrompt(promptTemplate, skill, skillContent);
    const promptFile = path.join(promptDir, `${skill.slug}.prompt.txt`);
    await fs.writeFile(promptFile, prompt, "utf8");

    let status: RunResult["status"] = "failed";
    let error: string | undefined;
    let exitCode: number | null = null;
    let attempts = 0;
    let outputFile: string | undefined;

    for (let attempt = 1; attempt <= options.retries + 1; attempt += 1) {
      attempts = attempt;
      const args = ["-p", prompt, "--output-format", "json", "--max-turns", String(options.maxTurns)];
      args.push("--model", options.model);

      const outcome = await runClaude(options.command, args, options.timeoutMs);
      exitCode = outcome.exitCode;

      const stdoutPath = path.join(rawDir, `${skill.slug}.attempt-${attempt}.stdout.txt`);
      const stderrPath = path.join(rawDir, `${skill.slug}.attempt-${attempt}.stderr.txt`);
      await fs.writeFile(stdoutPath, outcome.stdout, "utf8");
      await fs.writeFile(stderrPath, outcome.stderr, "utf8");

      if (outcome.timedOut) {
        status = "timeout";
        error = `Timed out after ${options.timeoutMs}ms`;
        continue;
      }

      if (outcome.exitCode !== 0) {
        status = "failed";
        error = `Exit code ${String(outcome.exitCode)}`;
        continue;
      }

      const parsed = parseClaudeOutput(outcome.stdout);
      const resultText = extractSkillMarkdown(parsed.text);
      if (!resultText) {
        status = "invalid_output";
        if (parsed.subtype === "error_max_turns") {
          error = `Claude hit max turns (${options.maxTurns}); increase --max-turns`;
        } else {
          error = "Unable to extract SKILL.md frontmatter block";
        }
        continue;
      }

      const cleanedResultText = normalizeDocument(resultText);
      const rewritePath = path.join(rewritesDir, skill.slug, "SKILL.md");
      await fs.mkdir(path.dirname(rewritePath), { recursive: true });
      await fs.writeFile(rewritePath, `${cleanedResultText}\n`, "utf8");
      status = "success";
      outputFile = rewritePath;
      error = undefined;
      break;
    }

    const durationMs = Date.now() - start;
    const result: RunResult = {
      slug: skill.slug,
      skillPath: skill.skillPath,
      status,
      attempts,
      durationMs,
      exitCode,
      outputFile,
      error,
    };

    results.push(result);
    await fs.appendFile(resultsPath, `${JSON.stringify(result)}\n`, "utf8");
    completed += 1;
    const progress = `${completed}/${selected.length}`;
    console.log(`[${progress}] ${skill.slug}: ${status} (${durationMs}ms)`);
  }

  async function worker(): Promise<void> {
    while (queue.length > 0) {
      const next = queue.shift();
      if (!next) {
        return;
      }
      await processSkill(next);
    }
  }

  const workers = Array.from({ length: Math.min(options.concurrency, selected.length) }, () => worker());
  await Promise.all(workers);

  const summary = {
    total: results.length,
    success: results.filter((result) => result.status === "success").length,
    failed: results.filter((result) => result.status === "failed").length,
    timeout: results.filter((result) => result.status === "timeout").length,
    invalid_output: results.filter((result) => result.status === "invalid_output").length,
  };

  const failedRows = results
    .filter((result) => result.status !== "success")
    .map((result) => `- ${result.slug}: ${result.status}${result.error ? ` (${result.error})` : ""}`)
    .join("\n");

  const summaryMarkdown = `# Run Summary

- Run directory: ${runDir}
- Total: ${summary.total}
- Success: ${summary.success}
- Failed: ${summary.failed}
- Timeout: ${summary.timeout}
- Invalid output: ${summary.invalid_output}

## Failed Skills

${failedRows || "None"}
`;

  await fs.writeFile(path.join(runDir, "SUMMARY.md"), summaryMarkdown, "utf8");

  console.log("\nRun complete");
  console.log(`Summary written to: ${path.join(runDir, "SUMMARY.md")}`);
  if (summary.failed > 0 || summary.timeout > 0 || summary.invalid_output > 0) {
    process.exitCode = 1;
  }
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Runner failed: ${message}`);
  process.exit(1);
});
