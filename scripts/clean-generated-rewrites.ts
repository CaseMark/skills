#!/usr/bin/env bun

import { promises as fs } from "node:fs";
import path from "node:path";

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

async function listSkillFiles(targetDir: string): Promise<string[]> {
  const entries = await fs.readdir(targetDir, { withFileTypes: true });
  const files: string[] = [];

  for (const entry of entries) {
    const fullPath = path.join(targetDir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await listSkillFiles(fullPath)));
    } else if (entry.isFile() && entry.name === "SKILL.md") {
      files.push(fullPath);
    }
  }

  return files;
}

async function main(): Promise<void> {
  const targets = process.argv.slice(2);
  if (targets.length === 0) {
    console.error("Usage: bun runner/clean-generated-rewrites.ts <dir> [dir2 ...]");
    process.exit(1);
  }

  let checked = 0;
  let rewritten = 0;
  const failures: string[] = [];

  for (const target of targets) {
    const absolute = path.resolve(process.cwd(), target);
    const files = await listSkillFiles(absolute);
    for (const file of files) {
      checked += 1;
      const content = await fs.readFile(file, "utf8");
      const extracted = extractSkillMarkdown(content);
      if (!extracted) {
        failures.push(file);
        continue;
      }
      const normalized = normalizeDocument(extracted);
      const nextContent = `${normalized}\n`;
      if (content !== nextContent) {
        rewritten += 1;
        await fs.writeFile(file, nextContent, "utf8");
      }
    }
  }

  console.log(`Checked: ${checked}`);
  console.log(`Rewritten: ${rewritten}`);
  console.log(`Failures: ${failures.length}`);
  if (failures.length > 0) {
    for (const file of failures) {
      console.log(`- ${file}`);
    }
    process.exit(1);
  }
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Cleaner failed: ${message}`);
  process.exit(1);
});
