---
name: summarizing-fund-prospectuses
description: Summarizes mutual fund and ETF prospectuses into structured overviews of investment strategy, fee structure, risk factors, and portfolio characteristics. Use when evaluating investment products, comparing fund options, or preparing client fund recommendations.
tags:
  - summarization
  - asset-management
  - funds
metadata:
  author: casemark
  practice_areas:
    - Asset Management
    - Wealth Management
  document_types:
    - Prospectus
    - Fund Summary
  skill_modes:
    - Summarization
---

# Summarizing Fund Prospectuses

Distills fund prospectuses into investor-actionable summaries.

## Workflow

1. **Identify** fund type, structure, and benchmark
2. **Extract** strategy — investment objective, approach, constraints
3. **Break down** fees — expense ratio, loads, 12b-1, redemption fees
4. **Summarize** risks — principal risks ranked by prominence in prospectus
5. **Capture** portfolio characteristics — top holdings, sector allocation, turnover
6. **Note** tax considerations and distribution policy

## Output Template

```markdown
## Fund Summary: [Fund Name] ([Ticker])

### Overview
| Field | Value |
|-------|-------|
| Fund Type | [Mutual Fund / ETF / Closed-End] |
| Asset Class | |
| Benchmark | |
| Inception Date | |
| AUM | |
| Min Investment | |

### Investment Strategy
[Concise description of how the fund invests]

### Fee Structure
| Fee | Amount |
|-----|--------|
| Expense Ratio (Net) | |
| Expense Ratio (Gross) | |
| Front Load | |
| Back Load | |
| 12b-1 Fee | |
| Redemption Fee | |

### Top Holdings
| Holding | Weight |
|---------|--------|

### Risk Factors (by prominence)
1. [Primary risk]
2. [Secondary risk]

### Performance (if included)
| Period | Fund | Benchmark | Difference |
|--------|------|-----------|------------|

### Tax Considerations
- [Distribution frequency, capital gains history, tax efficiency]
```

## Key Rules

- Net vs. gross expense ratio: always report both if available
- Distinguish share classes — fee structures vary significantly (A, C, Institutional)
- "Principal risks" section ordering in the prospectus indicates perceived severity
- Past performance data comes with required disclaimers — note the disclaimer
- Concentration risk: flag any single holding >5% or sector >25%
- Turnover ratio indicates trading activity and tax efficiency
