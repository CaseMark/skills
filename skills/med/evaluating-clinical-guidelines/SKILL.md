---
name: evaluating-clinical-guidelines
description: Evaluates clinical practice guidelines against specific patient scenarios, extracting evidence-graded recommendations with strength ratings. Use when applying guidelines to patient cases, comparing guideline recommendations, or summarizing guideline updates.
tags:
  - analysis
  - evidence-based-medicine
  - guidelines
metadata:
  author: casemark
  practice_areas:
    - General Practice
    - Specialty Medicine
  document_types:
    - Clinical Guideline
  skill_modes:
    - Analysis
    - Assessment
---

# Evaluating Clinical Guidelines

Maps clinical guidelines to patient-specific recommendations.

## Workflow

1. **Identify** applicable guidelines (source organization, version, date)
2. **Extract** relevant recommendations for the clinical question
3. **Note** evidence grade and recommendation strength for each
4. **Apply** to patient context — which recommendations apply given patient specifics
5. **Flag** conflicts between guidelines from different organizations
6. **Summarize** with clear action items

## Output Template

```markdown
## Guideline Evaluation: [Clinical Question]

### Applicable Guidelines
| Organization | Guideline | Version/Year | Link |
|-------------|-----------|-------------|------|

### Relevant Recommendations
| # | Recommendation | Strength | Evidence Grade | Source |
|---|---------------|----------|---------------|--------|

### Patient-Specific Application
- **Applies**: [Recommendations that apply to this patient]
- **Does Not Apply**: [Recommendations excluded and why]
- **Conflicts**: [Where guidelines disagree]

### Action Items
1. [Specific clinical action with supporting guideline reference]
```

## Key Rules

- Always cite the specific guideline section/page
- Distinguish "strong recommendation" from "conditional/weak recommendation"
- Note when guidelines are outdated (>5 years) or superseded
- Acknowledge when patient falls outside guideline population
- Never present guideline recommendations as absolute mandates
