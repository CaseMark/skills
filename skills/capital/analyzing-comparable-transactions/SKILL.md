---
name: analyzing-comparable-transactions
description: Identifies and analyzes comparable M&A transactions with deal multiples, premium analysis, and transaction characteristics for valuation benchmarking. Use when valuing companies for sale, assessing acquisition offers, or building M&A fairness opinions.
tags:
  - analysis
  - m-and-a
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Investment Banking
    - Corporate Finance
  document_types:
    - Comparable Transaction Analysis
  skill_modes:
    - Analysis
---

# Analyzing Comparable Transactions

Builds precedent transaction sets for valuation.

## Workflow

1. **Define** criteria — industry, size, geography, time period
2. **Screen** transactions — identify relevant completed deals
3. **Extract** metrics — enterprise value, multiples, premiums
4. **Adjust** — normalize for size, timing, strategic vs. financial buyer
5. **Analyze** — ranges, medians, means, outlier explanations
6. **Apply** to target — implied valuation range

## Output Template

```markdown
## Comparable Transaction Analysis: [Target Company]

### Screening Criteria
| Criterion | Filter |
|-----------|--------|
| Industry | [NAICS/SIC codes] |
| Deal Size | [$X - $Y] |
| Geography | |
| Time Period | [Last X years] |
| Deal Type | [Strategic/Financial/Both] |

### Transaction Set
| Date | Target | Acquirer | EV ($M) | EV/Rev | EV/EBITDA | Premium |
|------|--------|---------|---------|--------|-----------|---------|

### Statistical Summary
| Metric | EV/Revenue | EV/EBITDA | Premium |
|--------|-----------|-----------|---------|
| Mean | | | |
| Median | | | |
| 25th Pctile | | | |
| 75th Pctile | | | |

### Implied Valuation for [Target]
| Basis | Target Metric | Multiple Range | Implied EV |
|-------|--------------|---------------|-----------|
| Revenue | | [Low-High] | |
| EBITDA | | [Low-High] | |

### Outlier Notes
- [Explanation for any deals significantly above/below range]
```

## Key Rules

- Recent transactions are more relevant — weight accordingly
- Control premiums: 20-40% is typical but varies by sector
- Strategic vs. financial buyers pay different multiples — segment the analysis
- Size matters: smaller companies trade at lower multiples (size discount)
- Synergy assumptions inflate strategic deal multiples — adjust for comparison
- Market conditions at time of deal affect multiples — bull vs. bear market
