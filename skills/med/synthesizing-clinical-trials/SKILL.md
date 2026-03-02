---
name: synthesizing-clinical-trials
description: Synthesizes multiple clinical trial publications into comparative efficacy summaries with effect sizes, confidence intervals, and evidence quality grades. Use when comparing treatments, reviewing trial evidence, or preparing evidence-based recommendations.
tags:
  - synthesis
  - research
  - evidence-based-medicine
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Pharmacology
  document_types:
    - Clinical Trial Publication
  skill_modes:
    - Synthesis
    - Analysis
---

# Synthesizing Clinical Trials

Produces structured comparisons across clinical trial publications.

## Workflow

1. **Identify** trials — extract PICO elements (Population, Intervention, Comparator, Outcome) from each
2. **Assess** quality — apply Jadad score or Cochrane Risk of Bias
3. **Extract** endpoints — primary, secondary, safety; with effect sizes and CIs
4. **Compare** across trials — alignment/conflict of results
5. **Grade** overall evidence — GRADE framework (High/Moderate/Low/Very Low)
6. **Synthesize** narrative — clinical significance, not just statistical significance

## Output Template

```markdown
## Clinical Trial Synthesis: [Intervention] for [Condition]

### Trials Included
| Trial | N | Population | Design | Duration | Quality |
|-------|---|-----------|--------|----------|---------|

### PICO Summary
- **P**: [Population]
- **I**: [Intervention details]
- **C**: [Comparator]
- **O**: [Primary outcome]

### Efficacy Comparison
| Outcome | Trial A | Trial B | Trial C | Direction |
|---------|---------|---------|---------|-----------|

### Safety Summary
| Adverse Event | Incidence (Intervention) | Incidence (Control) | NNH |
|--------------|-------------------------|--------------------|----|

### Evidence Grade: [GRADE level]
**Rationale**: [Why this grade]

### Clinical Bottom Line
[1-2 sentence summary a clinician can act on]
```

## Key Rules

- Always report effect sizes with confidence intervals, not just p-values
- Distinguish statistical significance from clinical significance
- Note heterogeneity across trial populations
- Flag industry-sponsored trials separately
- If trials conflict, explain possible reasons (population differences, dosing, endpoints)

For PICO framework details, see [references/PICO-FRAMEWORK.md](references/PICO-FRAMEWORK.md).
For evidence grading methodology, see [references/EVIDENCE-GRADING.md](references/EVIDENCE-GRADING.md).
