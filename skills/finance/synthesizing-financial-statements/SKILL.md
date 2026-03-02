---
name: synthesizing-financial-statements
description: Synthesizes 10-K and 10-Q SEC filings into structured financial summaries with key metrics, trends, year-over-year comparisons, and risk factor highlights. Use when analyzing annual/quarterly reports, building company financial profiles, or preparing investment research.
tags:
  - synthesis
  - sec-filings
  - financial-analysis
metadata:
  author: casemark
  practice_areas:
    - Financial Analysis
    - Equity Research
  document_types:
    - 10-K
    - 10-Q
    - Annual Report
  skill_modes:
    - Synthesis
    - Analysis
---

# Synthesizing Financial Statements

Extracts structured financial intelligence from SEC filings.

## Workflow

1. **Extract** key financials — income statement, balance sheet, cash flow highlights
2. **Calculate** key ratios — profitability, liquidity, leverage, efficiency
3. **Compare** — YoY and sequential changes, identify trends
4. **Analyze** MD&A — management's explanation of results
5. **Flag** risk factors — new risks, changed risks, removed risks
6. **Note** accounting changes, restatements, or unusual items

## Output Template

```markdown
## Financial Statement Summary: [Company] — [Period]

### Income Statement Highlights
| Line Item | Current | Prior Year | Change % |
|-----------|---------|-----------|----------|
| Revenue | | | |
| Gross Profit | | | |
| Operating Income | | | |
| Net Income | | | |
| EPS (Diluted) | | | |

### Balance Sheet Highlights
| Item | Current | Prior Year | Change |
|------|---------|-----------|--------|
| Cash & Equivalents | | | |
| Total Debt | | | |
| Shareholders' Equity | | | |
| Net Debt | | | |

### Cash Flow Summary
| Category | Current | Prior Year |
|----------|---------|-----------|
| Operating CF | | |
| CapEx | | |
| Free Cash Flow | | |
| Dividends Paid | | |
| Share Repurchases | | |

### Key Ratios
| Ratio | Current | Prior Year | Industry Avg |
|-------|---------|-----------|-------------|

### MD&A Key Points
1. [Management's explanation of material changes]

### Risk Factors (New or Changed)
- [New risk factor or material change to existing]

### Notable Items
- [Restatements, accounting changes, one-time items, related-party transactions]
```

## Key Rules

- Always note the filing type (10-K vs. 10-Q) and fiscal year-end
- GAAP vs. non-GAAP: extract both, note reconciliation items
- Segment reporting: break out by segment when available
- Off-balance-sheet items: operating leases, variable interest entities
- Related-party transactions: always flag
- Compare to industry averages when context is available

For ratio calculation formulas, see [references/RATIO-DEFINITIONS.md](references/RATIO-DEFINITIONS.md).
For SEC filing navigation guide, see [references/SEC-FILING-GUIDE.md](references/SEC-FILING-GUIDE.md).
