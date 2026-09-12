---
name: skill-creator
language: en
description: Create a new private skill in the case.dev skills registry for the user's organization. Use when the user wants to create, save, build, or register a new skill or reusable workflow — e.g. "create a skill", "save this as a skill", "turn this process into a workflow", "make this reusable". Covers interviewing the user, drafting the skill, and creating it with the casedev CLI.
---

# Skill Creator

Create a new **private (org-scoped) skill** in the case.dev skills registry. A
skill is a reusable instruction set a legal AI agent loads with `skill_read`
and follows exactly. Once created, the skill appears in the organization's
Skills page and can be attached to any chat with `$`.

## Process

Work through these four steps in order. Never create the skill before the
user approves the draft.

### 1. Interview

Ask only what you need to draft well — usually one short round of questions:

- What should the skill do? (the task, end to end)
- What does it work from? (matter documents, user-provided facts, both)
- What output is expected? (document type, structure, length, tone)
- Any firm-specific conventions? (templates, phrasing, review steps,
  jurisdiction defaults)

If the user already described the task in detail, skip questions you can
answer from their message.

### 2. Draft

Draft all three fields and show them to the user for approval:

- **name** — short, imperative, title case. `Demand Letter Draft`, not
  `A skill that helps with demand letters`.
- **summary** — one sentence saying what the skill does **and when to use
  it**. Concrete trigger phrases beat vague descriptions: agents decide
  whether to load a skill from this line alone, and they under-trigger on
  vague summaries. Good: "Drafts a demand letter from the matter record;
  use when the user asks for a demand letter, settlement demand, or
  pre-suit letter." Bad: "Helps with letters."
- **content** — markdown instructions written **for the agent, not the
  user**: step-by-step procedure, what inputs to gather, exact output
  format, and quality checks before delivering. State the steps as
  commands ("Extract every treatment date", not "Treatment dates could be
  extracted").

### 3. Create

After explicit approval, create the skill with the pre-authenticated casedev
CLI. Write the JSON to a file first to avoid shell-quoting issues:

```bash
cat > /tmp/skill.json <<'EOF'
{
  "name": "Demand Letter Draft",
  "summary": "Drafts a demand letter from the matter record; use when the user asks for a demand letter, settlement demand, or pre-suit letter.",
  "content": "# Demand Letter Draft\n\n..."
}
EOF
casedev api POST /skills --body "$(cat /tmp/skill.json)"
```

The response includes the created skill's `slug`. Skills created this way are
**private to the organization** — they are org custom skills, not published
anywhere public.

To update an existing skill, use `casedev api PUT /skills/<slug>` with the
same body shape. To verify a skill exists, use the native `skill_read <slug>`
tool.

### 4. Confirm

Report the result in plain language: the skill's name and slug, that it now
appears under **Skills → Your firm**, and that it can be attached in any chat
by typing `$`. Suggest a quick test run.

## Rules

- Never create a skill before the user approves the full draft.
- Never paste raw API responses at the user — report results in plain
  language.
- Never print, echo, or reveal `CASEDEV_API_KEY` or any credential.
- The CLI is pre-authenticated: never run `casedev login` and never pass
  `--api-key`.

## Troubleshooting

- **409 / slug conflict** — a skill with that name already exists. Ask the
  user whether to update the existing skill (`PUT /skills/<slug>`) or pick a
  different name.
- **401/403** — the runtime key cannot write skills; tell the user the
  creation failed and to contact support. Do not retry in a loop.
- **Content too long** — skill content is capped (64KB). Trim reference
  material; link to matter documents instead of inlining them.
