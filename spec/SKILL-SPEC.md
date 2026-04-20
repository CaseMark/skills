# CaseMark Skill Specification

This document defines the authoring standard for skills in the CaseMark/skills repository. It extends the [Agent Skills specification](https://agentskills.io/specification) with CaseMark-specific conventions.

## Directory Layout

Every skill is a directory containing at minimum a `SKILL.md` file:

```
skill-name/
├── SKILL.md              # Required — instructions + metadata
└── references/           # Optional — detailed docs loaded on demand
    └── REFERENCE.md
```

Skills live under one of two top-level directories:

| Directory | Audience | Embedding |
|-----------|----------|-----------|
| `skills/casedev/` | case.dev developers | None — file-based only |
| `skills/legal/` | Legal professionals | Embedded on merge into pgvector DB |

## SKILL.md Format

### Frontmatter (required)

```yaml
---
name: skill-name
language: en
description: What this skill does and when to use it.
---
```

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | Yes | Max 64 chars. Lowercase letters, numbers, hyphens only. Must match the parent directory name. |
| `description` | Yes | Max 1024 chars. Non-empty. Third person. Describes what the skill does and when to use it. |
| `language` | No | ISO 639-1 two-letter code for the skill's primary language (`en`, `es`, `fr`, …). Defaults to `en`. |
| `license` | No | License identifier or reference to bundled file. |
| `tags` | No | Flat array of canonical tags from the controlled vocabulary (see [Legal Skills: Tags](#legal-skills-tags)) |

### Name rules

- Lowercase alphanumeric + hyphens only (`a-z`, `0-9`, `-`)
- Must not start or end with `-`
- Must not contain consecutive hyphens (`--`)
- Must match the parent directory name exactly

### Description rules

- Write in **third person** ("Processes documents..." not "I process documents..." or "Use this to process...")
- Include specific trigger keywords that help agents find this skill
- Include both what it does and when to use it

### Body content

The markdown body after frontmatter contains the skill instructions. Keep it:

- **Under 500 lines** for the main SKILL.md
- **Concise** — assume the agent is already smart. Only add context it doesn't have.
- **Concrete** — include specific commands, examples, and expected outputs
- **Consistent** — use one term for each concept throughout

## Progressive Disclosure

Structure skills so context is loaded efficiently:

1. **Metadata** (~100 tokens): `name` and `description` are loaded at startup for all skills
2. **Instructions** (<5000 tokens recommended): Full SKILL.md body loaded when the skill activates
3. **References** (as needed): Separate files loaded only when required

### Reference files

- Keep references **one level deep** from SKILL.md (no nested chains)
- Use descriptive filenames (`API-REFERENCE.md`, not `doc2.md`)
- Add a table of contents to reference files over 100 lines
- Link from SKILL.md with relative paths: `See [API Reference](references/API-REFERENCE.md)`

## Content Guidelines

### Do

- Use consistent terminology (pick one term, stick with it)
- Provide concrete input/output examples
- Include a Troubleshooting section for common errors
- Match specificity to the task's fragility (see "Degrees of Freedom" below)
- Test with multiple models (Haiku, Sonnet, Opus)

### Don't

- Include time-sensitive information ("after August 2025, use...")
- Explain things Claude already knows (what a PDF is, how HTTP works)
- Offer multiple approach options without a clear default
- Use Windows-style paths (`\`) — always use forward slashes
- Add "voodoo constants" without justification

## Degrees of Freedom

Match instruction specificity to the task:

- **High freedom** (text guidance): When multiple approaches are valid and context determines the best one
- **Medium freedom** (pseudocode/templates): When a preferred pattern exists but variation is acceptable
- **Low freedom** (exact scripts): When operations are fragile, order-dependent, or consistency is critical

## Legal Skills: Tags

Skills under `skills/legal/` use a flat `tags` array for search filtering and classification. Tags come from a controlled vocabulary of 18 values across three axes:

```yaml
---
name: deposition-summarization
description: Summarizes deposition transcripts...
tags:
  - litigation
  - summary
  - summarization
---
```

### Controlled vocabulary

| Axis | Tags |
|------|------|
| **Practice area** | `litigation`, `corporate`, `transactional`, `regulatory` |
| **Document type** | `agreement`, `pleading`, `motion`, `brief`, `memo`, `letter`, `summary`, `analysis`, `checklist`, `policy` |
| **Skill mode** | `drafting`, `summarization`, `analysis`, `research` |

Rules:
- All tags are **lowercase**
- A skill can have **multiple tags** from any axis (e.g., `litigation` + `transactional` + `drafting` + `agreement`)
- Use only tags from the controlled vocabulary above
- Tags power the filter search in the Legal Agent Skills MCP and the agentskills.legal website

## Validation Checklist

Before submitting a PR:

- [ ] `name` matches directory name, is lowercase-hyphenated, under 64 chars
- [ ] `description` is third-person, under 1024 chars, includes trigger keywords
- [ ] SKILL.md body is under 500 lines
- [ ] No time-sensitive information
- [ ] Consistent terminology throughout
- [ ] Concrete examples included
- [ ] Reference files are one level deep
- [ ] Troubleshooting section present
- [ ] `tags` use only values from the controlled vocabulary
- [ ] No semantic overlap (cosine similarity < 0.85) with existing skills
