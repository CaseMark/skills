---
name: conducting-variance-analysis
description: Structures budget vs. actual variance analysis with driver decomposition and management narrative. Use when analyzing variances, explaining budget deviations, or preparing variance reports.
tags:
  - process
  - financial-planning-and-analysis
metadata:
  author: casemark
  practice_areas:
    - FP&A
    - Management Accounting
    - Business Intelligence
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Variance Analysis

## When To Use

- Monthly, quarterly, or annual close when comparing actuals against budget or forecast
- Preparing management commentary for board decks, earnings packages, or operating reviews
- Investigating unexpected P&L or balance sheet movements flagged by finance or business owners
- Rolling forecast updates that require rebaselining assumptions
- Ad hoc deep dives requested by CFO, controller, or business unit leads

## Inputs To Gather

- **Budget/forecast data**: Approved budget or latest forecast by line item, cost center, and period
- **Actual results**: General ledger trial balance or sub-ledger detail for the analysis period
- **Prior period actuals**: Prior year or prior quarter for trend context
- **Chart of accounts mapping**: Ensure budget and actuals align to the same account hierarchy
- **Volume/operational metrics**: Units sold, headcount, hours billed, transactions processed — whatever drives the line items
- **Known events log**: One-time items, reorgs, timing shifts, or reclassifications already identified by the business
- **Materiality threshold**: Dollar and percentage thresholds for which variances require narrative explanation (e.g., >$50K or >10%) [VERIFY — thresholds vary by organization and reporting level]

## Workflow

1. **Align data structure**
   - Map actuals to the budget hierarchy (cost center, department, GL account)
   - Reconcile total actuals to the posted trial balance before proceeding
   - Confirm the reporting period matches (calendar month vs. 4-4-5, fiscal vs. calendar year) [VERIFY]

2. **Compute raw variances**
   - Calculate dollar variance: Actual − Budget (favorable/unfavorable sign convention per company policy)
   - Calculate percentage variance: (Actual − Budget) / |Budget|
   - Flag any line where budget = 0 but actuals exist (new activity, misclassification, or timing)

3. **Apply materiality filter**
   - Rank variances by absolute dollar impact
   - Isolate items exceeding the materiality threshold for detailed analysis
   - Group immaterial variances into an "other" category with a brief roll-up note

4. **Decompose drivers**
   - **Volume variance**: (Actual volume − Budget volume) × Budget rate/price
   - **Rate/price variance**: (Actual rate − Budget rate) × Actual volume
   - **Mix variance**: Impact of product/service/channel mix shift on blended margins
   - **Timing variance**: Identify spend or revenue recognized in a different period than budgeted
   - **One-time / non-recurring items**: Isolate discrete events (severance, legal settlements, asset write-downs) from run-rate trends
   - For cost lines, distinguish between controllable variances (hiring pace, discretionary spend) and non-controllable variances (FX, commodity prices, allocated overhead)

5. **Build management narrative**
   - Lead each variance explanation with the dollar impact and direction (favorable/unfavorable)
   - State the primary driver in one sentence, then provide supporting detail
   - Connect variances to operational actions: "Revenue was $1.2M favorable driven by 8% higher unit volume in the Southeast region following the Q2 channel expansion"
   - Quantify offsetting variances explicitly — avoid netting without disclosure
   - Flag any variance expected to persist into future periods vs. one-time catch-ups

6. **Prepare forecast implications**
   - For each material variance, indicate whether the current full-year forecast should be adjusted
   - Note risks and opportunities with estimated dollar ranges
   - Recommend specific actions where a variance is unfavorable and controllable

## Output

- **Variance summary table**: Line item, budget, actual, $ variance, % variance, favorable/unfavorable flag — sorted by materiality
- **Driver decomposition detail**: For each material variance, a breakdown into volume, rate, mix, timing, and one-time components
- **Management narrative**: Plain-language explanations suitable for executive and board audiences, with each material line item addressed
- **Forecast impact section**: Adjustments recommended to the rolling forecast or full-year outlook, with risk/opportunity flags
- **Appendix**: Data reconciliation notes, threshold definitions, and any items marked [VERIFY]

## Quality Checks

- Total actuals in the variance report reconcile to the posted GL trial balance — no unexplained gaps
- All variances exceeding the materiality threshold have a narrative explanation with a named driver
- Volume and rate/price variance components sum back to the total line-item variance (no residual)
- Favorable/unfavorable sign convention is consistent throughout (revenue favorable = actual > budget; cost favorable = actual < budget)
- One-time items are explicitly separated from recurring run-rate variances
- Narrative avoids circular language ("costs were higher because spending increased") — every explanation ties to an operational or external cause
- Prior period trends are referenced where a variance represents an acceleration or reversal of an existing pattern
- Any data point sourced from outside the GL (headcount, volume, pricing) is cross-referenced or marked [VERIFY]
