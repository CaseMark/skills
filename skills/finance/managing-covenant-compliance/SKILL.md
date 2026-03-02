---
name: managing-covenant-compliance
description: Calculates and tracks loan covenant compliance with financial ratio testing, certification preparation, and early warning identification for borrowers and lenders. Use when preparing covenant compliance certificates, monitoring credit agreements, or assessing covenant headroom.
tags:
  - compliance
  - lending
  - covenants
metadata:
  author: casemark
  practice_areas:
    - Commercial Lending
    - Corporate Treasury
  document_types:
    - Covenant Compliance Certificate
  skill_modes:
    - Calculation
    - Compliance
---

# Managing Covenant Compliance

Tracks and certifies covenant compliance.

## Workflow

1. **Extract** covenant requirements from credit agreement
2. **Calculate** covenant metrics using agreed-upon definitions
3. **Test** compliance — actual vs. required threshold
4. **Measure** headroom — how close to breach
5. **Prepare** compliance certificate
6. **Alert** on trending toward breach

## Output Template

```markdown
## Covenant Compliance Report: [Period]

### Facility Summary
| Field | Detail |
|-------|--------|
| Borrower | |
| Lender(s) | |
| Facility Amount | |
| Outstanding Balance | |
| Testing Date | |

### Financial Covenants
| Covenant | Required | Actual | Compliant? | Headroom |
|----------|---------|--------|-----------|---------|
| Max Leverage (Debt/EBITDA) | <3.5x | | | |
| Min DSCR | >1.25x | | | |
| Min Current Ratio | >1.5x | | | |
| Max CapEx | <$Xm | | | |
| Min Net Worth | >$Xm | | | |

### Calculation Detail
#### [Covenant Name]
| Component | Amount | Source |
|-----------|--------|--------|
| [Numerator items] | | [GL account / line item] |
| [Denominator items] | | [GL account / line item] |
| **Result** | **[Ratio]** | |

### Trend Analysis
| Covenant | Q-2 | Q-1 | Current | Direction |
|----------|-----|-----|---------|-----------|

### Early Warnings
| Covenant | Headroom | Quarters to Breach (at trend) | Risk Level |
|----------|---------|-------------------------------|-----------|

### Compliance Certificate
I certify that as of [date], the Borrower is in compliance with all financial covenants...

Officer: _________________ Title: _________ Date: _______
```

## Key Rules

- EBITDA definition in the credit agreement controls — it may differ from standard EBITDA
- Pro forma adjustments (acquisitions, dispositions) per agreement terms
- Permitted add-backs: know exactly what the agreement allows
- Cure rights: know if equity cure or other cure mechanisms exist
- Testing frequency: quarterly is most common, but check the agreement
- Covenant breach triggers cross-default provisions in other agreements

For covenant calculation conventions, see [references/COVENANT-CALCULATIONS.md](references/COVENANT-CALCULATIONS.md).
