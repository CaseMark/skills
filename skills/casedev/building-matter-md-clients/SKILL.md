---
name: building-matter-md-clients
language: en
description: Specification and implementation guidance for adding MATTER.md support to a legal agent harness or client. Use when building or extending an agent harness (such as a legal agent runtime) to discover, load, persist, and version MATTER.md durable context files. For how an agent should read and edit MATTER.md during matter work, see using-matter-md.
---

# Building MATTER.md Clients

`MATTER.md` is a plain-Markdown durable context file for a legal matter — the matter-level equivalent of a project instructions file. A harness implements MATTER.md by discovering the file, loading it into the agent's context at the right point, and persisting agent edits through its own storage layer.

Keep **transport separate from the file convention.** The file is just Markdown; the harness owns where it lives and how it is versioned.

## File format

A `MATTER.md` file is Markdown with optional YAML frontmatter:

```markdown
---
mattermd: "0.1"
title: "Smith v. Jones"
---

# Matter

## What This Is
...
```

- `mattermd`: format version string. Lets clients detect and migrate the convention over time.
- `title`: human label for the matter.

Frontmatter is optional except where the host platform needs a mechanical handle (lookup, display, indexing). Keep it small — matter *meaning* lives in the Markdown body, not in YAML. Do not require fields beyond what the platform mechanically needs.

The body is freeform Markdown. `using-matter-md` ships a starter template with suggested sections (`What This Is`, `Goals`, `Source Map`, `Open Questions`, `Board`, etc.), but these are **illustrative, not normative** — legal work varies too much to fix a schema. Agents add, drop, and reshape sections per matter. Do not parse or validate the body against a section list; treat it as opaque Markdown.

## Loading lifecycle

A minimal implementation:

1. **Discover** the file named `MATTER.md` at the root of the matter workspace (e.g. the vault root).
2. **Load** it after global agent instructions and before matter task execution.
3. **Preserve** it across context compaction — it is durable state, not a transient turn.
4. Let the agent **read and update** the file through ordinary file tools.
5. **Persist** the edited file using the host platform's storage layer.

Edit via plain file tools. A client *may* add dedicated MATTER.md tools, but only if it accepts the schema that implies — the convention itself assumes nothing beyond "a Markdown file you can read and write."

## Concurrency

The convention does not define a locking model — clients own conflict resolution. If multiple agents can write one `MATTER.md`, keep edits append-friendly (append to list/table sections rather than rewriting prose) so concurrent writes are less likely to clobber each other, and resolve the rest with whatever your storage layer offers (e.g. conditional writes).

## Principles

- **No heavy infrastructure required.** Do not require a database, schema registry, CRDT, or sync protocol to support `MATTER.md`. A file and a place to put it are enough.
- **Version history belongs to the host, not the file.** Snapshots, diffs, and audit trails are valuable for a legal matter — implement them in your storage layer, not inside the Markdown.
- **Storage is the host's choice.** The file may live alongside working files, in a vault as a matter object, or both. Pick what fits your platform; the convention is location-agnostic.
- **Confirm saves.** Surface real save success/failure to the agent so it does not tell the user the matter is synced when it is not.
- **Keep it bounded.** The convention targets concise files (~500 lines). Clients should not auto-dump evidence or logs into it; that responsibility stays with the agent's editing discipline.

## Relationship to using-matter-md

This skill defines the format and the client contract. `using-matter-md` defines agent behavior — when to read, what is durable enough to write, and how to edit without bloating the file. Ship both: implement the contract here, load `using-matter-md` (or equivalent guidance) into the agent that operates on the file.
