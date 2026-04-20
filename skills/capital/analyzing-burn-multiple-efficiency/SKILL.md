---
name: analyzing-burn-multiple-efficiency
language: en
description: Evaluates capital efficiency with burn multiple, net new ARR per dollar burned, and path to profitability analysis. Use when analyzing burn efficiency, assessing capital needs, or modeling runway scenarios.
tags:
  - analysis
  - growth-equity
metadata:
  author: casemark
  practice_areas:
    - Growth Equity
    - Expansion Capital
    - Late-Stage Investing
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Burn Multiple Efficiency

## When To Use

- Evaluating a growth-stage company's capital efficiency before committing to a new round
- Benchmarking portfolio companies against peer cohorts on cash-to-growth conversion
- Stress-testing runway scenarios under different growth and spend assumptions
- Assessing whether a company is approaching a credible path to profitability or will require additional capital raises
- Responding to board or IC requests for a burn efficiency deep-dive

## Inputs To Gather

- **Income statement data** (trailing 12-month and quarterly): revenue, COGS, operating expenses broken out by S&M, R&D, G&A
- **ARR schedule**: beginning ARR, new ARR, expansion ARR, contraction, churn — by quarter for at least 4 quarters
- **Cash flow statement or treasury report**: net cash burn per period, ending cash balance, any non-recurring items that distort operating burn
- **Capitalization context**: last round size, post-money valuation, any outstanding debt or credit facilities
- **Comparable set** (if benchmarking): peer burn multiples by stage, vertical, and growth rate bracket
- **Management forecasts**: forward revenue plan, planned headcount additions, expected gross margin trajectory

## Workflow

1. **Calculate core burn multiple** — Divide net cash burned in the period by net new ARR added in the same period. Use quarterly and trailing-12-month windows. A burn multiple below 1.5x is considered efficient; 1.5–2.5x is acceptable for high-growth companies; above 3x signals inefficiency requiring explanation.
2. **Decompose the burn** — Break total operating burn into S&M, R&D, and G&A components. Identify which cost center drives the majority of cash consumption. Flag any single line item exceeding 50% of total burn.
3. **Compute CAC payback and magic number** — CAC payback = fully-loaded S&M spend ÷ (net new ARR × gross margin). Magic number = net new ARR ÷ prior-period S&M spend. Cross-reference these with burn multiple to distinguish sales-efficiency problems from general overhead bloat.
4. **Model runway scenarios** — Build at least three cases:
   - **Base case**: current burn rate, current growth trajectory
   - **Belt-tightening case**: 20–30% OpEx reduction, reduced growth assumptions
   - **Accelerated spend case**: planned hiring / GTM expansion with associated burn increase
   - For each, calculate months of runway remaining and the implied burn multiple.
5. **Benchmark against comparables** — Map the company's burn multiple against stage-appropriate peers. Adjust for gross margin differences (a 50% GM business and an 80% GM business are not directly comparable on raw burn multiple). Note where the company sits in the distribution (quartile ranking).
6. **Assess path to profitability** — Estimate the break-even revenue run rate assuming current cost structure scales linearly. Identify the "cash-flow crossover" quarter under base-case assumptions. Flag if break-even requires more capital than currently available. [VERIFY] any tax-credit or grant income that management includes in their break-even model.
7. **Synthesize findings** — Summarize the efficiency story: Is the company converting capital into durable ARR at an attractive rate? Where are the levers to improve? What conditions must hold for the runway to reach profitability without another raise?

## Output

- **Burn Multiple Summary Table**: quarterly and LTM burn multiple, net new ARR, net burn, with trend arrows
- **Cost Decomposition Chart**: percentage of burn by S&M / R&D / G&A with period-over-period change
- **Runway Scenario Matrix**: months remaining and implied next-raise timing for each case
- **Efficiency Benchmarking**: company vs. peer cohort on burn multiple, CAC payback, and magic number
- **Key Findings Narrative** (3–5 paragraphs): capital efficiency assessment, primary burn drivers, actionable recommendations, and flagged risks
- **[VERIFY] items list**: any data points sourced from management projections, unaudited figures, or assumptions requiring independent confirmation

## Quality Checks

- Confirm ARR figures reconcile between the schedule and the income statement (net new ARR + beginning ARR − churn = ending ARR)
- Validate that cash burn figures exclude non-operating items (financing proceeds, one-time legal settlements, asset sales)
- Ensure burn multiple is calculated on the same periodicity for both numerator and denominator — do not mix quarterly burn with LTM ARR
- Cross-check runway calculations against the most recent bank balance or treasury report date
- Verify that comparable companies are matched on stage, geography, and gross margin profile — flag any apples-to-oranges comparisons
- Mark any forward-looking management assumptions with [VERIFY] rather than presenting them as confirmed data
