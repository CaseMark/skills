# Skill Body Rewrite Prompt

You are rewriting an existing SKILL.md file to improve quality.

Hard requirements:
1. Preserve the YAML frontmatter block EXACTLY as-is (character-for-character, same keys/order/spacing).
2. Preserve the main heading title line (`# ...`) unless it is obviously malformed.
3. Rewrite the body content below the heading to be domain-specific, practical, and non-generic.
4. Do not add any appendix/meta commentary (no "summary of changes", no "key changes made", no permission notes).
5. Do not wrap output in code fences.
6. Output ONLY the final SKILL.md document.

Quality requirements for the rewritten body:
- Must be tailored to the exact skill name/description and practice area tags in frontmatter.
- Replace generic boilerplate workflows with concrete task steps and decision points.
- Include sections with clear operational value, using concise headings and bullets.
- Keep the content concise but substantive (roughly 300-700 words unless topic needs less).
- Include explicit "[VERIFY]" markers for jurisdiction/regulation/statute-dependent points that vary.
- Avoid legal-specific assumptions for non-legal verticals unless the skill itself is legal/compliance.

Preferred structure after the heading:
- `## When To Use`
- `## Inputs To Gather`
- `## Workflow`
- `## Output`
- `## Quality Checks`

Context:
- Skill slug: {{SKILL_SLUG}}
- Source path: {{SKILL_PATH}}

Current SKILL.md content:
{{SKILL_CONTENT}}
