---
name: analyzing-financial-ratios
description: Calculates and interprets comprehensive financial ratio analysis from statement data covering liquidity, profitability, leverage, and efficiency metrics with trend and peer comparison. Use when evaluating company financial health, preparing credit analysis, or benchmarking performance.
tags:
  - analysis
  - financial-analysis
  - ratios
metadata:
  author: casemark
  practice_areas:
    - Financial Analysis
    - Credit Analysis
  document_types:
    - Ratio Analysis
  skill_modes:
    - Calculation
    - Analysis
---

# Analyzing Financial Ratios

Computes and interprets financial ratios with context.

## Workflow

1. **Extract** required line items from financial statements
2. **Calculate** ratios by category — liquidity, profitability, leverage, efficiency
3. **Trend** — compare across periods (minimum 3 years preferred)
4. **Benchmark** — compare to industry averages or peer set
5. **Interpret** — what the ratios say about financial health
6. **Flag** — deteriorating trends, covenant-relevant ratios, outliers

## Ratio Categories

### Liquidity
| Ratio | Formula | Healthy Range |
|-------|---------|--------------|
| Current Ratio | Current Assets / Current Liabilities | >1.5 varies by industry |
| Quick Ratio | (Cash + Receivables) / Current Liabilities | >1.0 |
| Cash Ratio | Cash / Current Liabilities | Context-dependent |

### Profitability
| Ratio | Formula |
|-------|---------|
| Gross Margin | Gross Profit / Revenue |
| Operating Margin | Operating Income / Revenue |
| Net Margin | Net Income / Revenue |
| ROE | Net Income / Shareholders' Equity |
| ROA | Net Income / Total Assets |
| ROIC | NOPAT / Invested Capital |

### Leverage
| Ratio | Formula |
|-------|---------|
| Debt-to-Equity | Total Debt / Equity |
| Debt-to-EBITDA | Total Debt / EBITDA |
| Interest Coverage | EBIT / Interest Expense |
| Net Debt / EBITDA | (Total Debt - Cash) / EBITDA |

### Efficiency
| Ratio | Formula |
|-------|---------|
| Asset Turnover | Revenue / Total Assets |
| Inventory Turnover | COGS / Average Inventory |
| DSO | (Receivables / Revenue) x 365 |
| DPO | (Payables / COGS) x 365 |
| Cash Conversion Cycle | DSO + DIO - DPO |

## Output Template

```markdown
## Financial Ratio Analysis: [Company]

### Summary
| Category | Assessment |
|----------|-----------|
| Liquidity | [Strong / Adequate / Weak] |
| Profitability | [Strong / Adequate / Weak] |
| Leverage | [Conservative / Moderate / Aggressive] |
| Efficiency | [Strong / Adequate / Weak] |

### Detailed Ratios
| Ratio | FY-2 | FY-1 | FY Current | Trend | Peer Avg |
|-------|------|------|-----------|-------|----------|

### Key Observations
1. [Most significant finding]

### Concerns
- [Deteriorating trends or ratios outside normal range]
```

## Key Rules

- Always specify whether using trailing twelve months (TTM) or fiscal year
- Average balance sheet items for ratios mixing P&L and B/S (ROA, turnover)
- Industry context is critical — a 2x debt/equity is fine for utilities, alarming for tech
- One ratio alone means nothing — look at patterns across categories
- Adjusted vs. reported: note which EBITDA definition is used

For complete ratio formulas and industry benchmarks, see [references/RATIO-FORMULAS.md](references/RATIO-FORMULAS.md).
