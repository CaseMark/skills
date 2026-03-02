---
name: reviewing-formulary-coverage
description: Evaluates medication formulary coverage status, identifies tier placement, and recommends therapeutic alternatives when coverage is limited. Use when checking insurance drug coverage, finding formulary alternatives, or preparing step therapy documentation.
tags:
  - analysis
  - pharmacy
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Pharmacy
    - Health Insurance
  document_types:
    - Formulary Review
  skill_modes:
    - Analysis
---

# Reviewing Formulary Coverage

Maps medications to formulary status with alternatives.

## Workflow

1. **Identify** medication, formulation, and dose
2. **Check** formulary tier (Tier 1-5 or not covered)
3. **Note** restrictions — prior authorization, step therapy, quantity limits
4. **Identify** covered alternatives in same therapeutic class
5. **Document** for PA submission if needed

## Output Template

```markdown
## Formulary Review

### Requested Medication
| Drug | Strength | Formulation | Therapeutic Class |
|------|----------|------------|-------------------|

### Coverage Status
- **Tier**: [1-5 or Not Covered]
- **Prior Auth Required**: [Yes/No]
- **Step Therapy**: [Requirements]
- **Quantity Limits**: [If any]

### Formulary Alternatives
| Alternative | Tier | Restrictions | Clinical Notes |
|------------|------|-------------|----------------|

### Recommendation
[Most appropriate covered alternative, or PA justification path]
```

## Key Rules

- Always check both brand and generic coverage
- Note that formularies change quarterly — timestamp the review
- Step therapy requirements must be documented before PA submission
- Distinguish between medical benefit and pharmacy benefit coverage
- Flag specialty pharmacy requirements for high-cost medications
