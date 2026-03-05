---
name: analyzing-earnings-quality
description: Assesses earnings quality through accruals analysis, cash conversion, and accounting red flag identification. Use when evaluating earnings quality, detecting accounting anomalies, or analyzing accruals.
tags:
  - analysis
  - equity-research
  - accounting
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
# Analyzing Earnings Quality

## When To Use

- Evaluating a company's reported earnings before making buy/sell/hold recommendations
- Screening for accounting anomalies or aggressive revenue recognition in a portfolio or watchlist
- Conducting due diligence on an acquisition target's financial statements
- Comparing earnings quality across peer companies in an industry sector
- Investigating divergences between reported net income and operating cash flow

## Inputs To Gather

- **Income statement** (3-5 years minimum): Revenue, COGS, operating expenses, non-recurring items, net income
- **Cash flow statement** (matching period): CFO, capex, working capital changes, stock-based compensation
- **Balance sheet** (matching period): Total assets, receivables, inventory, payables, accrued liabilities, deferred revenue
- **Notes to financials**: Revenue recognition policies, changes in accounting estimates, related-party transactions
- **Audit opinion and any restatements**: Qualified opinions, material weaknesses, prior-period adjustments
- **Sector context**: Industry-typical accrual levels, seasonal patterns, capital intensity

## Workflow

1. **Compute accruals metrics**
   - Calculate total accruals: Net Income minus CFO
   - Derive accrual ratio: Total Accruals / Average Total Assets
   - Compute the Sloan accrual measure: (ΔCA - ΔCash) - (ΔCL - ΔSTD - ΔTP) - D&A, scaled by average total assets
   - Flag if accrual ratio exceeds ±5% of average total assets or deviates significantly from sector median

2. **Assess cash conversion quality**
   - Cash conversion ratio: CFO / Net Income (healthy benchmark: consistently >1.0)
   - Free cash flow yield vs. earnings yield — persistent gaps signal accrual-driven earnings
   - Track CFO-to-EBITDA over time; declining trend indicates deteriorating cash backing
   - Examine capex classification: operating vs. growth capex, and whether maintenance capex is being deferred

3. **Analyze revenue quality**
   - Revenue growth vs. receivables growth — receivables growing faster than revenue suggests channel stuffing or aggressive recognition
   - Days Sales Outstanding (DSO) trend: rising DSO relative to peers is a red flag
   - Deferred revenue trend: declining deferred revenue alongside rising reported revenue may indicate pull-forward
   - Bill-and-hold arrangements, percentage-of-completion changes, or contract modification patterns [VERIFY against ASC 606 / IFRS 15 applicability]

4. **Screen for expense manipulation**
   - Capitalization rates: rising proportion of capitalized vs. expensed costs (especially software development, exploration costs)
   - Reserve and accrual reversals boosting income (warranty reserves, bad debt provisions, restructuring reserves)
   - Pension and post-retirement assumption changes — discount rate, expected return on plan assets [VERIFY plan-specific assumptions]
   - Stock-based compensation: exclude SBC from "adjusted" earnings and assess magnitude relative to operating income

5. **Evaluate non-recurring and below-the-line items**
   - Frequency of "one-time" charges — truly one-time items should not recur in 3+ of the last 5 years
   - Gains on asset sales, debt extinguishment, or insurance recoveries inflating headline numbers
   - Classify each adjustment as sustainable or transient; compute a "clean" earnings figure

6. **Construct an earnings quality scorecard**
   - Assign ratings (Strong / Adequate / Weak) across dimensions: accrual level, cash conversion, revenue quality, expense integrity, non-recurring reliance
   - Weight each dimension by materiality to the specific company and sector
   - Summarize an overall earnings quality assessment with a composite score or rating

## Output

Deliver a structured earnings quality report containing:

- **Executive summary**: One-paragraph overall assessment with composite rating
- **Accruals analysis table**: Accrual ratios by year, trend direction, and sector comparison
- **Cash conversion dashboard**: CFO/NI ratio, FCF yield vs. earnings yield, trend charts
- **Red flag inventory**: Each flag with metric value, threshold, severity (High/Medium/Low), and supporting evidence
- **Clean earnings reconciliation**: Reported EPS to adjusted EPS bridge, with each adjustment categorized and explained
- **Earnings quality scorecard**: Dimension-level ratings and composite assessment
- **Limitations and caveats**: Data gaps, periods not covered, estimates used

## Quality Checks

- Confirm all financial data ties back to audited filings or authoritative sources — no analyst estimates without labeling
- Verify accrual calculations foot to the balance sheet and cash flow statement (total accruals = NI - CFO should reconcile)
- Cross-check DSO, DIO, and DPO calculations against stated revenue, COGS, and payables figures
- Ensure peer comparisons use consistent accounting standards (GAAP vs. IFRS) [VERIFY standard used by each peer]
- Flag any company with a recent auditor change, restatement, or material weakness as elevated risk regardless of metric results
- Confirm that "non-recurring" items are truly excluded from the clean earnings figure and not double-counted
- Mark any metric derived from estimated or incomplete data with [VERIFY]
