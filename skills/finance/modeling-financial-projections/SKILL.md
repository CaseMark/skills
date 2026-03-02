---
name: modeling-financial-projections
description: Builds financial projection models from historical data and assumptions, generating projected income statements, balance sheets, and cash flow statements. Use when forecasting financial performance, stress-testing scenarios, or preparing business plans.
tags:
  - analysis
  - modeling
  - forecasting
metadata:
  author: casemark
  practice_areas:
    - Financial Planning
    - Investment Banking
  document_types:
    - Financial Model
    - Projection
  skill_modes:
    - Modeling
---

# Modeling Financial Projections

Constructs structured financial forecasts from historical data and assumptions.

## Workflow

1. **Establish** historical base — 3-5 years of financials
2. **Define** assumptions — revenue growth, margins, CapEx, working capital
3. **Project** income statement — top-down or bottom-up
4. **Project** balance sheet — driven by income statement and assumptions
5. **Derive** cash flow statement — from P&L and balance sheet changes
6. **Stress test** — sensitivity analysis on key assumptions

## Output Template

```markdown
## Financial Projections: [Company] — [Projection Period]

### Key Assumptions
| Assumption | Historical Avg | Projected | Rationale |
|-----------|---------------|-----------|-----------|
| Revenue Growth | | | |
| Gross Margin | | | |
| OpEx Growth | | | |
| CapEx % Revenue | | | |
| Working Capital Days | | | |
| Tax Rate | | | |

### Projected Income Statement
| Line Item | FY+1 | FY+2 | FY+3 | CAGR |
|-----------|------|------|------|------|

### Projected Balance Sheet
| Line Item | FY+1 | FY+2 | FY+3 |
|-----------|------|------|------|

### Projected Cash Flow
| Line Item | FY+1 | FY+2 | FY+3 |
|-----------|------|------|------|

### Sensitivity Analysis
| Scenario | Revenue Growth | EBITDA Margin | FCF | Valuation Impact |
|----------|---------------|-------------|-----|-----------------|
| Bull | | | | |
| Base | | | | |
| Bear | | | | |

### Key Metrics
| Metric | FY+1 | FY+2 | FY+3 |
|--------|------|------|------|
| EBITDA | | | |
| FCF | | | |
| Net Debt/EBITDA | | | |
| ROIC | | | |
```

## Key Rules

- Every assumption needs a rationale — "because management said so" is valid, note the source
- Balance sheet must balance — Assets = Liabilities + Equity (always verify)
- Cash flow should reconcile to balance sheet cash changes
- Revenue: specify whether top-down (market share) or bottom-up (units x price)
- Working capital: model DSO, DIO, DPO separately for accuracy
- Circular references (interest on debt that depends on cash that depends on interest): iterate or use average balances
