---
name: using-matter-md
language: en
description: Operational guidance for working with a MATTER.md durable context file during legal matter work. Use when working inside a legal matter, vault, case file, transaction, litigation, or investigation where a MATTER.md exists or should exist. Covers when to read it, what context is durable enough to write, and how to update it without bloating it. To implement MATTER.md support in a harness, see building-matter-md-clients.
---

# Using MATTER.md

`MATTER.md` is the durable whiteboard for a legal matter. It tells you what the matter is, who the user represents, how they want it worked, what source rules apply, and what the current durable work state is — so you and future sessions can orient fast.

Treat it as durable project state, **not** as source evidence. Evidence lives in the document system or vault; `MATTER.md` links to it.

## At the start of matter work

1. Locate and read `MATTER.md` before doing matter-specific work.
2. Use it to orient: representation, goals, jurisdiction, source rules, open questions, current board.
3. If it is missing and the workspace is clearly tied to a legal matter, create it from the starter template below.

Read and persist `MATTER.md` through your harness's MATTER.md tools if it exposes them, otherwise through ordinary file tools.

## Deciding whether to write

Before editing, ask one question: **will this help a future agent or session orient faster?** If yes, it is durable and belongs. If it is temporary reasoning or raw evidence, keep it out.

**Belongs in MATTER.md** (durable, matter-level):

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
- short source-map entries that point to documents or vault objects

**Does not belong** (keep it in the source system or discard it):

- full document text, bulk OCR, transcript, or exhibit content
- chat history or scratchpad reasoning
- long legal-research dumps
- every fact extracted from the sources
- transient task notes
- sync tokens, credentials, permissions, or storage internals

If the content is evidence, keep it in the document system and link to it. If it is temporary reasoning, leave it out.

## How to update

1. Read the current `MATTER.md` first.
2. Make the smallest edit that captures the new durable context.
3. Prefer a short summary plus a source link over copied source text.
4. When a factual statement comes from a source, include a short source pointer.
5. Compress or remove stale details if the file is growing.
6. Keep tables small and readable; preserve existing headings and table shapes unless a simpler structure is clearly better.
7. Keep the file concise — under ~500 lines. If it grows past that, summarize durable points and replace bulky text with source links.

Source pointers should fit the host environment. Examples:

- `obj_123`
- `vault:vault_abc/objects/obj_123`
- `Smith Dep. 45:12-46:3`
- `Generated memo: damages-summary.md`

## During work

- Use the source system or vault tools for evidence — not `MATTER.md`.
- Add an **open question** when a missing fact materially affects the matter work.
- Update the **board** only for tasks that should survive the current session, not for transient to-dos.

## Before finishing

- Save durable changes to `MATTER.md`.
- Report material `MATTER.md` changes to the user.
- Do not claim `MATTER.md` is synced or canonical unless the harness confirms the save succeeded.

## Starter template

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

Keep the matter's meaning in the Markdown body, not in YAML. Frontmatter stays small.

## Examples

Good durable update:

```markdown
## Goals

- Primary: prepare a plaintiff-side damages demand package.
- Avoid: overclaiming medical causation not supported by the records.
```

Good source-map entry:

```markdown
| Police report | obj_123 | Incident narrative and responding officer notes |
```

Bad update — copying source text bloats the file and hides provenance; link instead:

```markdown
## Durable Context

[15 pages of copied deposition transcript]
```

## Troubleshooting

- Missing file: create it only when the workspace is clearly tied to a legal matter.
- File over ~500 lines: summarize durable points, replace bulky text with source links.
- Multiple agents editing: prefer small section-level edits and preserve the latest visible user intent.
- Harness claims sync support: verify the save succeeded before relying on it.
