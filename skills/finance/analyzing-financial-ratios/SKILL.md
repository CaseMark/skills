---
name: analyzing-financial-ratios
description: Computes and interprets liquidity, profitability, leverage, and efficiency ratios with peer benchmarking. Use when analyzing financial statements, building comparable analyses, or evaluating company health metrics.
tags:
  - analysis
  - equity-research
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Financial Ratios

Computes, normalizes, and interprets financial ratios across four categories — liquidity, profitability, leverage, and efficiency — with mandatory peer benchmarking and time-series context. Produces analyst-ready output suitable for equity research reports, credit assessments, and comparable company analyses.

## When To Use

- Equity research initiation or update requiring comparable company analysis
- Credit review or loan underwriting where leverage and coverage ratios determine capacity
- M&A screening to identify valuation anomalies or operational gaps between target and acquirer
- Portfolio monitoring when financial statements are freshly filed and ratios need updating
- Board-level or investment committee reporting on company financial health
- Any scenario where a single ratio has been cited without peer or temporal context — this skill enforces the discipline of comparison

**Do not use** for pure valuation (DCF, multiples-based pricing) — this skill feeds into valuation but does not produce one.

## Inputs To Gather

Before computing any ratio, confirm every item below. Pause and ask if any are missing.

| Input | Details Required |
|---|---|
| **Subject company** | Legal name, ticker (if public), sector, sub-industry, fiscal year-end |
| **Analysis period** | Fiscal years (e.g., FY2022–FY2024), quarterly, and/or TTM; specify if calendar-year aligned |
| **Peer group** | 4–8 comparable companies with rationale for inclusion (size, geography, business mix) |
| **Data sources** | SEC filings, Bloomberg, CapIQ, company IR — specify which; note any data gaps |
| **Purpose** | Equity initiation, credit review, M&A screening, portfolio monitoring, or other — this affects which ratio categories to emphasize |
| **Accounting standards** | US GAAP vs. IFRS; note any recent standard changes affecting comparability (ASC 842, IFRS 16) [VERIFY] |
| **Known adjustments** | One-time charges, discontinued operations, restatements, fiscal year changes in peer group |

**Anti-hallucination rule**: Never fabricate financial data. If a data point is unavailable, insert `[DATA NEEDED: source]`. If a filing has not been released, state that explicitly.

## Workflow

### Step 1: Data Collection & Normalization

**1A. Pull raw financial data** for the subject and each peer from the three core statements:

- **Income Statement**: Revenue, COGS, gross profit, SGA, R&D, D&A, EBIT, interest expense, pre-tax income, tax provision, net income, diluted share count, SBC expense, restructuring charges
- **Balance Sheet** (period-end and average where needed): Cash & equivalents, short-term investments, AR, inventory, total current assets, total assets, AP, short-term debt, current portion of LTD, total current liabilities, long-term debt, total debt, total equity, goodwill & intangibles, operating lease liabilities (current + non-current)
- **Cash Flow Statement**: CFO, capex, FCF, dividends, share repurchases

**1B. Normalize for comparability** — apply these adjustments consistently across subject and all peers:

| Adjustment | When to Apply | Method |
|---|---|---|
| **Operating leases** | Comparing pre/post ASC 842 periods or GAAP vs. IFRS peers [VERIFY] | Capitalize remaining lease payments at incremental borrowing rate; add to debt and assets |
| **Goodwill & intangibles** | ROA, ROIC, or asset-based ratios | Compute both with and without; flag if goodwill > 30% of total assets |
| **Stock-based compensation** | Profitability margins, ROIC | Show GAAP and adjusted (add back SBC); note dilution impact separately |
| **One-time items** | Any margin or return metric | Remove restructuring, litigation, asset impairments, gain/loss on sale; document each |
| **Pension obligations** | Leverage ratios for companies with DB plans | Add unfunded pension to debt for adjusted leverage |
| **Minority interest** | Net income, equity | Use income attributable to parent; adjust equity accordingly |

Every adjustment must be documented with dollar amount and source filing reference.

**1C. Align time periods:**

- **Fiscal year** — when all companies share the same FYE or analysis is annual trend
- **TTM** — most recent performance snapshot (last annual + recent quarters − year-ago quarters)
- **Calendar-year aligned** — when peers have different FYEs; restate to CY using quarterly data
- **Quarterly** — seasonal analysis or recent inflection points

Flag any peer with a fiscal year change during the analysis period.

### Step 2: Compute Ratios by Category

Compute all ratios below for the subject and each peer across all periods.

**Liquidity:**

| Ratio | Flags |
|---|---|
| Current Ratio | < 1.0 potential liquidity stress; > 3.0 may indicate inefficient capital deployment |
| Quick Ratio | Strips inventory; critical for manufacturing, retail |
| Cash Ratio | Most conservative; relevant for distressed or early-stage companies |

**Profitability:**

| Ratio | Flags |
|---|---|
| Gross Margin | Declining trend = pricing pressure or input cost inflation; compare within sub-industry |
| Operating Margin (EBIT) | Show both GAAP and adjusted; SBC treatment matters significantly for tech |
| Net Margin | Influenced by capital structure and tax jurisdiction; less useful for cross-border comps |
| ROE | Decompose via DuPont (Step 3); high ROE from leverage ≠ high ROE from operations |
| ROA | Use average total assets; compare with and without goodwill |
| ROIC | The single most important return metric; must exceed WACC for value creation |

**Leverage:**

| Ratio | Flags |
|---|---|
| Debt / Equity | > 2.0x warrants deeper investigation; meaningless if equity is negative |
| Total Debt / EBITDA | Market-standard leverage metric; include operating leases for adjusted version |
| Net Debt / EBITDA | Adjusts for cash; negative net debt = net cash position |
| Interest Coverage (EBIT / Interest) | < 3.0x raises credit concern; < 1.5x is distress territory |
| Fixed Charge Coverage | Adds lease payments and mandatory debt repayment to denominator |
| DSCR | CFO / (principal repayment + interest); critical for project finance and credit |

**Efficiency:**

| Ratio | Flags |
|---|---|
| Asset Turnover | Higher = more efficient; compare only within same industry |
| Inventory Turnover | Low = potential obsolescence; very high = potential stockout risk |
| DSO | Growing faster than revenue = collection deterioration or channel stuffing |
| DPO | Increasing = supplier leverage or liquidity management; watch for coercive practices |
| Cash Conversion Cycle | DSO + DIO − DPO; negative = company funded by suppliers |

### Step 3: DuPont Decomposition

Decompose ROE into three drivers for the subject across all periods:

```
ROE = Net Profit Margin × Asset Turnover × Equity Multiplier
    = (Net Income / Revenue) × (Revenue / Avg Assets) × (Avg Assets / Avg Equity)
```

| Period | Net Margin | × Asset Turnover | × Equity Multiplier | = ROE |
|---|---|---|---|---|
| FY20XX | X.X% | X.Xx | X.Xx | X.X% |

**Interpretation:**
- ROE rising from margin improvement → operational strength
- ROE rising from equity multiplier → leverage-driven, investigate sustainability
- ROE rising from asset turnover → efficiency gains, verify not from asset write-downs
- Declining margin offset by rising leverage → red flag for deteriorating quality of returns

### Step 4: Peer Benchmarking

**4A. Comparable table** for the most recent period (TTM or latest FY):

| Metric | Subject | Peer 1 | Peer 2 | … | Peer Median | Peer Mean |
|---|---|---|---|---|---|---|
| Revenue ($M) | | | | | | |
| Gross Margin | | | | | | |
| Operating Margin (adj.) | | | | | | |
| Net Margin | | | | | | |
| ROE | | | | | | |
| ROIC | | | | | | |
| Debt / EBITDA | | | | | | |
| Net Debt / EBITDA | | | | | | |
| Interest Coverage | | | | | | |
| DSO | | | | | | |
| Cash Conversion Cycle | | | | | | |
| Current Ratio | | | | | | |

Use **median** as the primary benchmark (resistant to outliers). Flag any metric where the subject deviates > 1 standard deviation from peer median.

**4B. Time-series trend** for the subject across all analysis periods. Highlight:
- Improving vs. deteriorating trends
- Inflection points and potential causes
- Convergence toward or divergence from peer median

### Step 5: Red Flag Identification

Systematically check for these warning signals:

| Red Flag | Detection Method |
|---|---|
| Declining ROIC with increasing leverage | ROIC trend vs. Debt/EBITDA trend; value destruction signal |
| DSO growing faster than revenue | DSO % change vs. revenue % change; potential revenue quality issue |
| Negative working capital trend | Current ratio declining toward 1.0x with tightening quick ratio |
| Gross margin compression | Multi-period gross margin decline; pricing power erosion |
| Interest coverage deterioration | Coverage approaching 2.0x with upcoming maturities |
| EBITDA adjustments > 20% of reported EBITDA | Adjusted vs. GAAP gap; management credibility concern |
| Capex consistently below D&A | Under-investment; unsustainable margin improvement |
| Inventory build outpacing revenue growth | Demand weakness or obsolescence risk |
| Leverage through the cycle | Debt/EBITDA at cycle peak vs. trough; assess sustainability in downturn |

Every red flag must cite the specific data points that triggered it and a severity assessment: **watch** / **concern** / **critical**.

### Step 6: Synthesis & Narrative

Write a structured narrative covering:

1. **Financial health summary** — 2–3 sentence assessment citing the most significant ratios
2. **Strengths** — where the subject outperforms peers, with specific metrics
3. **Weaknesses** — where the subject underperforms, with specific metrics
4. **Trend assessment** — improving, stable, or deteriorating, with DuPont drivers
5. **Key risks** — red flags from Step 5, ranked by materiality
6. **Credit perspective** (if applicable) — leverage capacity, coverage adequacy, maturity profile
7. **Conclusion** — what the ratio analysis implies for the investment thesis or credit view

## Output

```
# Financial Ratio Analysis: [COMPANY NAME] ([TICKER])
## Analysis Period: [PERIOD] | Peer Group: [LIST]
## Date: [DATE] | Analyst: [NAME]

### Executive Summary
[2–3 sentence overall assessment]

### Adjustments Applied
| Adjustment | Amount ($M) | Periods Affected | Source |
|---|---|---|---|

### Ratio Dashboard
[Comparable table from Step 4A]

### Time-Series Analysis
[Trend table from Step 4B]

### DuPont Decomposition
[Table and interpretation from Step 3]

### Red Flags & Watchlist Items
[Findings from Step 5, ranked by severity]

### Narrative Analysis
[Structured commentary from Step 6]

### Data Sources & Limitations
[List all sources; note any data gaps or estimation methods]

### Disclaimer
This analysis is based on publicly available financial data and is intended
for informational purposes. It does not constitute investment advice.
All financial data should be independently verified against primary sources.
```

## Quality Checks

| Criterion | Verification |
|---|---|
| **Arithmetic accuracy** | Every ratio is independently calculable from the stated inputs; no circular references |
| **Adjustment consistency** | Same adjustments applied identically across subject and all peers; documented in table |
| **Period alignment** | All companies compared on same time basis; FYE differences noted |
| **Source traceability** | Every data point traceable to a specific filing, page, or database field |
| **Interpretation validity** | No ratio interpreted without industry context; no standalone numbers presented as good/bad |
| **Completeness** | All four ratio categories covered; DuPont decomposition included; red flag scan completed |
| **Anti-hallucination** | No fabricated data; all gaps marked `[DATA NEEDED]`; no assumed filing data |
| **GAAP vs. adjusted clarity** | Clear labeling of which metrics are GAAP and which are adjusted; no mixing |
| **Outlier treatment** | Peer outliers flagged and explained, not silently excluded |
| **Disclaimer present** | Analysis includes appropriate disclaimer language |

**Escalate to human review** when: subject company has negative equity, recent restatement, going concern opinion, or complex multi-segment structure requiring allocation judgments.

**Standing rules:**
- Ratios without peer or temporal context are prohibited — never present a ratio without comparison
- GAAP and adjusted figures must always be clearly distinguished
- Flag all one-time items explicitly, even if immaterial — let the analyst decide significance
- Non-GAAP adjustments must be sourced from management's own reconciliation or independently derived and labeled as such

## Reference Files

| File | Description |
|---|---|
| `references/RATIO-DEFINITIONS.md` | Complete ratio definitions, exact formulas, input definitions, and interpretation guidance for all ratio categories |
