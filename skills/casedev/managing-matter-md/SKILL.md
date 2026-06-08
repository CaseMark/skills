---
name: managing-matter-md
language: en
description: Helps agents read, maintain, and implement MATTER.md legal matter context files. Use when working in a legal matter, vault, case file, transaction, litigation, investigation, or legal workspace where durable context should survive across agent sessions.
---

# Managing MATTER.md

`MATTER.md` is the durable matter whiteboard for legal agents.

Use it to understand what the matter is, how the user wants it worked, what source rules apply, what context should survive future sessions, and what the current durable work state is.

## Core Rules

- Read `MATTER.md` before doing matter-specific work.
- Treat it as durable project state, not as source evidence.
- Update it only when the information should survive future sessions.
- Keep it concise. As a rule of thumb, keep `MATTER.md` under 500 lines.
- Link to source documents, vault objects, or generated artifacts instead of copying long excerpts.
- Preserve existing section headings and table shapes unless a simpler structure is clearly better.
- Do not store full source text, chat transcripts, long research notes, every extracted fact, or implementation-specific sync metadata.

## What Belongs In MATTER.md

Durable matter-level context belongs in `MATTER.md`:

- what the matter is
- who the user represents
- adverse or important non-client parties
- matter goals and things to avoid
- jurisdiction, forum, or governing law
- source rules and citation expectations
- durable user preferences
- stable working context and decisions
- open questions that should survive future sessions
- a lightweight board for durable tasks
- short source map entries that point to documents or vault objects

## What Does Not Belong

Do not add:

- full document text
- bulk OCR, transcript, or exhibit content
- chat history
- scratchpad reasoning
- long legal research dumps
- every fact extracted from the sources
- transient task notes
- sync tokens, credentials, permissions, or storage internals

If the content is evidence, keep it in the document system and link to it. If it is temporary reasoning, keep it out of `MATTER.md`.

## Starter Template

If `MATTER.md` does not exist, create a concise file like this:

```markdown
---
mattermd: "0.1"
title: ""
---

# Matter

## What This Is

## Representation

## Goals

## Jurisdiction

## Source Rules

## Working Preferences

## Source Map

| Label | Source | Notes |
|---|---|---|

## Working State

## Open Questions

| Question | Why It Matters | Status |
|---|---|---|

## Board

| Status | Task | Notes |
|---|---|---|
```

Frontmatter is optional except when the host platform needs a mechanical handle. Keep it small. Put matter meaning in the Markdown body, not in YAML.

## Updating MATTER.md

Before editing, decide whether the change is durable. A good update helps a future agent or future session orient faster.

When updating:

1. Read the current `MATTER.md`.
2. Make the smallest edit that preserves the new durable context.
3. Prefer summary plus source link over copied source text.
4. Remove or compress stale details if the file is growing.
5. Keep tables small and readable.
6. If a factual statement comes from a source, include a short source pointer when available.

Use source pointers that fit the host environment. Examples:

- `obj_123`
- `vault:vault_abc/objects/obj_123`
- `Smith Dep. 45:12-46:3`
- `Generated memo: damages-summary.md`

## Agent Behavior

At the start of matter work:

1. Locate and read `MATTER.md` if present.
2. Use it to orient to the matter, representation, goals, source rules, open questions, and current board.
3. If it is missing and the workspace is clearly matter-scoped, create it from the starter template.

During work:

- Use the source system or vault tools for evidence.
- Use `MATTER.md` for stable context and coordination.
- Add open questions when a missing fact affects the matter work.
- Update the board only for tasks that should survive the current session.

Before finishing:

- Save durable changes to `MATTER.md`.
- Report material `MATTER.md` changes to the user.
- Do not claim `MATTER.md` is synced or canonical unless the host platform confirms that.

## Implementing MATTER.md Support

Host platforms should keep transport separate from the file convention.

A minimal implementation:

1. Discover `MATTER.md` in the matter workspace.
2. Load it after global agent instructions and before matter task execution.
3. Preserve it across context compaction.
4. Let the agent read and update the file through ordinary file tools or a small dedicated tool.
5. Persist the edited file using the host platform's storage layer.

Recommended tool surface:

- `matter_md_read`: return the current `MATTER.md`.
- `matter_md_save`: persist the current file.
- `matter_md_update_section`: replace one named section.
- `matter_md_append_open_question`: append a durable open question.
- `matter_md_upsert_board_item`: add or update a durable board item.

Do not require a database, schema registry, CRDT, or sync protocol to support `MATTER.md`. Version history is useful, but it belongs to the host platform, not the file format.

## Examples

Good durable update:

```markdown
## Goals

- Primary: prepare a plaintiff-side damages demand package.
- Avoid: overclaiming medical causation not supported by the records.
```

Good source map entry:

```markdown
| Police report | obj_123 | Incident narrative and responding officer notes |
```

Bad update:

```markdown
## Durable Context

[15 pages of copied deposition transcript]
```

Copying source text bloats the file and hides provenance. Link to the source instead.

## Troubleshooting

- If `MATTER.md` is missing, create it only when the workspace is clearly tied to a legal matter.
- If the file is longer than 500 lines, summarize durable points and replace bulky text with source links.
- If a host platform claims sync support, verify save behavior before relying on it.
- If multiple agents edit the file, prefer small section-level edits and preserve the latest visible user intent.
