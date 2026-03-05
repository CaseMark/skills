#!/usr/bin/env bun

import { promises as fs } from "node:fs";
import path from "node:path";

function splitFrontmatter(content: string): { frontmatter: string; body: string } | null {
  const normalized = content.replace(/\r\n/g, "\n");
  if (!normalized.startsWith("---\n")) return null;

  const second = normalized.indexOf("\n---\n", 4);
  if (second === -1) return null;

  const frontmatter = normalized.slice(0, second + 5);
  const body = normalized.slice(second + 5);
  return { frontmatter, body };
}

async function listSkillFiles(root: string): Promise<string[]> {
  const out: string[] = [];
  const stack = [root];

  while (stack.length > 0) {
    const current = stack.pop();
    if (!current) continue;
    const entries = await fs.readdir(current, { withFileTypes: true });

    for (const entry of entries) {
      const full = path.join(current, entry.name);
      if (entry.isDirectory()) {
        stack.push(full);
      } else if (entry.isFile() && entry.name === "SKILL.md") {
        out.push(full);
      }
    }
  }

  return out.sort();
}

async function main(): Promise<void> {
  const [skillsRootArg, rewritesDirArg] = process.argv.slice(2);
  if (!skillsRootArg || !rewritesDirArg) {
    console.error("Usage: bun scripts/apply-rewrites-preserve-frontmatter.ts <skills-root> <rewrites-dir>");
    process.exit(1);
  }

  const skillsRoot = path.resolve(process.cwd(), skillsRootArg);
  const rewritesDir = path.resolve(process.cwd(), rewritesDirArg);

  const skills = await listSkillFiles(skillsRoot);

  let applied = 0;
  let unchanged = 0;
  let missing = 0;
  const missingSlugs: string[] = [];

  for (const skillPath of skills) {
    const slug = path.basename(path.dirname(skillPath));
    const rewritePath = path.join(rewritesDir, slug, "SKILL.md");

    let rewriteContent: string;
    try {
      rewriteContent = await fs.readFile(rewritePath, "utf8");
    } catch {
      missing += 1;
      missingSlugs.push(slug);
      continue;
    }

    const originalContent = await fs.readFile(skillPath, "utf8");
    const originalParts = splitFrontmatter(originalContent);
    const rewriteParts = splitFrontmatter(rewriteContent);

    if (!originalParts || !rewriteParts) {
      console.error(`Invalid frontmatter format for slug: ${slug}`);
      process.exit(1);
    }

    const next = `${originalParts.frontmatter}${rewriteParts.body.trim()}\n`;
    if (next === originalContent) {
      unchanged += 1;
      continue;
    }

    await fs.writeFile(skillPath, next, "utf8");
    applied += 1;
  }

  console.log(`Total skills: ${skills.length}`);
  console.log(`Applied: ${applied}`);
  console.log(`Unchanged: ${unchanged}`);
  console.log(`Missing rewrites: ${missing}`);

  if (missingSlugs.length > 0) {
    const missingPath = path.resolve(process.cwd(), `output/missing-rewrites-${path.basename(skillsRoot)}.txt`);
    await fs.mkdir(path.dirname(missingPath), { recursive: true });
    await fs.writeFile(missingPath, `${missingSlugs.join("\n")}\n`, "utf8");
    console.log(`Missing slug list: ${missingPath}`);
  }
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(`Apply failed: ${message}`);
  process.exit(1);
});
