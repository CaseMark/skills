# Contributing to CaseMark Agent Skills

We welcome contributions to both legal and case.dev platform skills.

## Skill Types

| Type | Directory | Who contributes | What happens on merge |
|------|-----------|-----------------|----------------------|
| Legal | `skills/legal/` | Legal professionals, law firms, legal AI builders | Embedded into vector DB, surfaced on agentskills.legal |
| Medical | `skills/med/` | Healthcare professionals, health AI builders | Embedded into vector DB, surfaced on agentskills.med |
| Finance | `skills/finance/` | Financial professionals, fintech builders | Embedded into vector DB, surfaced on agentskills.finance |
| case.dev | `skills/casedev/` | case.dev developers, platform engineers | Nothing extra — files are the product |

## Creating a New Skill

1. **Start from the template**:
   ```bash
    cp -r template/ skills/legal/your-skill-name/
    # or
    cp -r template/ skills/med/your-skill-name/
    # or
    cp -r template/ skills/finance/your-skill-name/
    # or
    cp -r template/ skills/casedev/your-skill-name/
   ```

2. **Edit `SKILL.md`**:
   - Set `name` to match your directory name (lowercase, hyphens, max 64 chars)
   - Write a `description` in third person (max 1024 chars) that explains what it does AND when to use it
   - Write clear, concise instructions in the body

3. **Follow the spec**: See [spec/SKILL-SPEC.md](spec/SKILL-SPEC.md) for the full authoring standard.

4. **Open a PR**: The `skill-qa` workflow will automatically validate your skill and post a review.

## Quality Standards

Before submitting:

- [ ] `name` matches directory name, lowercase-hyphenated, under 64 chars
- [ ] `description` is third-person, under 1024 chars, includes trigger keywords
- [ ] SKILL.md body is under 500 lines
- [ ] No time-sensitive information
- [ ] Consistent terminology throughout
- [ ] Concrete examples included
- [ ] Reference files are one level deep from SKILL.md
- [ ] Troubleshooting section present
- [ ] Tested with at least one Claude model

## PR Review Process

Every PR touching `skills/**` triggers automated QA:

1. **Format validation**: Frontmatter schema, line count, reference depth
2. **Semantic overlap check**: New skill descriptions are compared against existing skills. Flagged if cosine similarity > 0.85 with any existing skill.
3. **Content review**: An AI reviewer checks for conciseness, third-person descriptions, concrete examples, and adherence to the spec.
4. **Human review**: A CaseMark maintainer reviews the PR.

## Vertical Skills: Additional Metadata

Legal, medical, and finance skills support extra metadata fields for the vector DB:

```yaml
metadata:
  author: your-name
  practice_areas:
    - Litigation
    - Employment Law
  document_types:
    - Deposition Transcript
    - Motion
  skill_modes:
    - Summarization
    - Drafting
```

These power filtering and discovery on [agentskills.legal](https://agentskills.legal), [agentskills.med](https://agentskills.med), and [agentskills.finance](https://agentskills.finance).

## Improving Existing Skills

1. Read the current skill thoroughly
2. Make targeted improvements (don't rewrite everything)
3. Ensure changes don't break the validation checklist
4. Explain your changes in the PR description

## Questions?

Open an issue or reach out at [case.dev](https://case.dev).
