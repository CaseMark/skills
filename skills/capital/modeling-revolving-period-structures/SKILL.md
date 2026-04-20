---
name: modeling-revolving-period-structures
language: en
description: Builds revolving securitization models with replenishment criteria, early amortization triggers, and portfolio composition limits. Use when modeling revolving structures, analyzing credit card ABS, or evaluating asset purchase criteria.
tags:
  - modeling
  - structured-finance
  - portfolio
  - credit
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Revolving Period Structures

Builds revolving securitization models with replenishment criteria, early amortization triggers, and portfolio composition limits for credit card ABS, trade receivables, auto dealer floorplan, and similar asset classes with continuous origination.

## When To Use

- Modeling a revolving master trust or standalone revolving securitization (e.g., credit card ABS, trade receivable conduits)
- Evaluating asset purchase criteria and eligibility requirements during deal structuring
- Testing early amortization triggers and their impact on tranche cash flows
- Analyzing portfolio composition limits (concentration caps, seasoning floors, yield thresholds)
- Stress-testing replenishment assumptions under adverse scenarios (rising defaults, declining origination volume)

## Inputs To Gather

- **Deal documents**: Pooling and servicing agreement (PSA), indenture, series supplement — extract revolving period length, scheduled amortization date, and clean-up call threshold
- **Portfolio snapshot**: Current pool composition (balance, WAC, WAM, delinquency buckets, geographic/obligor concentrations)
- **Eligibility criteria**: Minimum/maximum receivable balance, required seasoning, excluded obligor types, maximum single-obligor concentration
- **Trigger definitions**: Early amortization events — typically excess spread < 0%, 3-month average default rate > X%, dilution rate > Y%, seller interest < minimum [VERIFY specific trigger levels from series supplement]
- **Historical performance**: Monthly data on gross yield, charge-offs, payment rate (MPR), dilutions, and purchase rate for at least 12-24 months
- **Replenishment assumptions**: Projected new receivable characteristics (yield, term, credit quality mix) and origination volume forecasts
- **Fee/cost structure**: Servicing fee, trustee fee, any credit enhancement fees, swap costs if applicable

## Workflow

1. **Map the revolving mechanics**
   - Define the revolving period start/end dates and conditions for extension or early termination
   - Model the seller's interest (retained percentage) — confirm minimum seller interest requirement [VERIFY]
   - Build the asset purchase mechanism: each period, principal collections are used to purchase new eligible receivables rather than pay down notes

2. **Build the portfolio replenishment engine**
   - Model new receivable purchases constrained by: available principal collections, eligibility criteria compliance, and concentration limit headroom
   - Apply composition limits as hard constraints — if new purchases would breach a concentration cap, reduce purchase volume or adjust the mix
   - Track portfolio characteristics dynamically: WAC, WAM, weighted average FICO (or equivalent), geographic distribution, single-obligor exposure

3. **Implement the cash flow waterfall**
   - Collections allocation: split into finance charge collections and principal collections per the PSA allocation percentages
   - Finance charge waterfall: servicing fee → note interest (by seniority) → credit enhancement replenishment → excess spread trapping or release
   - Principal waterfall during revolving period: principal collections fund new asset purchases; during amortization: principal collections pay down notes sequentially or pro rata [VERIFY allocation method from deal docs]
   - Model any reserve account or spread account mechanics — capture required balance, funding triggers, and release conditions

4. **Code early amortization triggers**
   - Implement each trigger as a monthly Boolean test applied against rolling averages or point-in-time metrics:
     - Three-month average excess spread falling below zero (or deal-specific threshold)
     - Portfolio yield declining below a defined floor
     - Monthly payment rate (MPR) dropping below minimum
     - Default rate or dilution rate exceeding ceilings
     - Seller/transferor interest falling below minimum required percentage
   - When any trigger fires, switch the model from revolving mode to controlled or rapid amortization — no further asset purchases, all principal collections applied to note paydown

5. **Run scenario and sensitivity analysis**
   - **Base case**: Use historical averages for MPR, default rate, yield, and purchase rate
   - **Stress cases**: Increase default rate by 2-3x, reduce MPR by 20-40%, compress portfolio yield by 100-300 bps, simulate origination volume decline (50-100% reduction in new purchases)
   - **Trigger proximity analysis**: For each trigger, calculate the distance-to-trigger under base and stress assumptions — identify which trigger is the binding constraint
   - **Amortization timing**: Model the controlled amortization schedule and confirm legal final maturity is met under stress

6. **Validate and reconcile**
   - Tie out total collections (finance charge + principal) to portfolio balance and assumed rates
   - Confirm cash flow waterfall balances: total inflows = total outflows + ending reserve balances
   - Verify that tranche balances at legal final maturity are zero under base case
   - Cross-check portfolio composition against eligibility criteria each period — no silent breaches

## Output

- **Monthly cash flow model** with separate tabs/sections for: portfolio dynamics (purchases, paydowns, defaults, recoveries), waterfall allocation, and tranche balances
- **Trigger monitoring dashboard** showing each early amortization trigger metric vs. threshold, with distance-to-trigger calculated monthly
- **Portfolio composition tracker** with period-by-period concentration levels vs. limits
- **Scenario summary table** comparing key outputs (WAL, tranche yields, credit enhancement levels, trigger breach timing) across base and stress cases
- **Assumptions log** documenting every input assumption, its source, and any [VERIFY] items requiring deal-level confirmation

## Quality Checks

- Revolving period principal collections are fully recycled into new purchases (no cash leakage) unless constrained by eligibility or volume limits
- Early amortization triggers use the correct averaging periods and metric definitions from the deal documents — do not default to generic thresholds
- Portfolio composition limits are enforced as binding constraints, not just tracked as informational metrics
- The model correctly transitions from revolving to amortization mode — verify no new purchases occur post-trigger and principal allocation shifts to note paydown
- Controlled amortization schedule (if applicable) pays the defined monthly principal amount; rapid amortization passes through all available principal [VERIFY which mode applies]
- Excess spread calculation correctly accounts for all fees, defaults, and dilutions before determining if spread is positive or negative
- Legal final maturity is respected — if notes are not fully repaid by that date under stress, flag the scenario as a ratings concern
