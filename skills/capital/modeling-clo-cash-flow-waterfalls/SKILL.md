---
name: modeling-clo-cash-flow-waterfalls
language: en
description: Builds CLO waterfall models with coverage tests, reinvestment criteria, and distribution allocation across tranches. Use when modeling CLO structures, analyzing OC/IC tests, or projecting tranche returns.
tags:
  - modeling
  - structured-finance
  - investment
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
# Modeling CLO Cash Flow Waterfalls

## When To Use

- Building or auditing a CLO waterfall model from an indenture or offering circular
- Projecting tranche-level returns under base, stress, and recovery scenarios
- Analyzing overcollateralization (OC) and interest coverage (IC) test triggers and cure mechanics
- Evaluating reinvestment period behavior including par-building trades and discretionary trading
- Comparing equity distributions across deal vintages or managers

## Inputs To Gather

- **Capital structure**: Tranche names, ratings, par amounts, spreads/coupons, payment frequency, and stated maturity vs. legal final
- **Collateral pool**: Par balance, WAS (weighted average spread), WAC (weighted average coupon), WARF (weighted average rating factor), WAL, diversity score, and CCC bucket concentration
- **Coverage test triggers**: OC and IC trigger levels and cure thresholds for each tranche (typically Class A/B OC, Class A/B IC, etc.)
- **Reinvestment criteria**: Reinvestment period end date, reinvestment target par, concentration limits, collateral quality tests (minimum WAS, maximum WARF, minimum diversity, CCC cap)
- **Default and recovery assumptions**: CDR (constant default rate), CPR (constant prepayment rate), recovery rate, and recovery lag in months
- **Fee structure**: Senior management fee (bps), subordinate management fee (bps), trustee/admin fees, and incentive management fee waterfall position
- **Payment dates and day count**: Quarterly vs. semi-annual, Act/360 vs. 30/360 [VERIFY against indenture]

## Workflow

1. **Map the priority of payments from the indenture**
   - Build the interest waterfall: trustee/admin fees → senior management fee → Class A interest → Class A OC/IC test → Class B interest → Class B OC/IC test → subordinate management fee → incentive fee → equity distributions
   - Build the principal waterfall: scheduled principal → turbo amortization from failed coverage tests → reinvestment bucket (during reinvestment period) → sequential principal paydown (post-reinvestment)
   - Identify any payment-in-kind (PIK) toggle provisions on mezzanine tranches

2. **Build the collateral cash flow engine**
   - Project monthly or quarterly interest collections from the pool using WAS, applying CPR and CDR vectors
   - Model defaults: apply CDR to performing par, subtract defaulted par, apply recovery rate after the specified lag period
   - Track performing par balance period-over-period: beginning par − scheduled amortization − prepayments − defaults + recoveries + reinvestment purchases
   - During the reinvestment period, reinvest principal proceeds at the reinvestment target spread subject to collateral quality test constraints

3. **Implement coverage tests**
   - OC test: (performing par + principal cash) / tranche par outstanding — compare to trigger level each payment date
   - IC test: interest collections (net of senior expenses) / tranche interest due — compare to trigger level each payment date
   - On test failure: divert interest proceeds to accelerate principal paydown of the senior-most tranche until test is cured or tranche is retired
   - Track cure status period-over-period — a cured test restores normal waterfall flow on the next payment date

4. **Run the distribution waterfall each period**
   - Allocate interest collections top-down per the interest priority of payments
   - Allocate principal collections per the principal waterfall (reinvestment vs. sequential paydown)
   - Calculate equity distributions as the residual after all obligations are met
   - Compute tranche-level IRR, WAL, yield-to-worst, and dollar price for each rated tranche

5. **Stress testing and scenario analysis**
   - Base case: consensus CDR (e.g., 2%), CPR (e.g., 20%), recovery (e.g., 70%, 12-month lag)
   - Stress case: elevated CDR (e.g., 4–6%), lower recoveries (e.g., 40–50%), extended lag
   - Front-loaded vs. back-loaded default timing vectors
   - Reinvestment spread compression scenarios (e.g., reinvesting at WAS − 50 bps)
   - Sensitivity tables: equity IRR and rated tranche WAL across CDR/recovery matrices

## Output

- **Waterfall schedule**: Period-by-period table showing interest collections, principal collections, fee payments, tranche interest payments, OC/IC test results (pass/fail with ratios), principal paydowns, and equity distributions
- **Coverage test dashboard**: OC and IC ratios each period with trigger levels, cushion (bps above trigger), and cure/fail status
- **Tranche return summary**: IRR, yield, WAL, and expected principal window for each tranche across base and stress scenarios
- **Equity return profile**: Equity IRR, cash-on-cash multiple, and distribution timeline under each scenario
- **Sensitivity matrix**: Two-variable tables (CDR vs. recovery, CDR vs. reinvestment spread) showing equity IRR and mezzanine tranche breakeven

## Quality Checks

- Par balance roll-forward reconciles each period: beginning par − amort − prepays − defaults + recoveries + reinvestments = ending par
- Total cash distributed (fees + interest + principal + equity) equals total cash collected each period — no leakage
- Coverage test ratios match hand-calculated spot checks for at least three periods
- OC test failure correctly triggers interest diversion and principal turbo in the waterfall
- Tranche stated maturities and legal final dates are correctly enforced — no payments after legal final [VERIFY]
- Reinvestment ceases on the reinvestment period end date and the model switches to sequential amortization
- Equity IRR is consistent with market context (broadly syndicated CLO equity typically targets 12–18% unlevered) — flag outliers for review
- CDR, CPR, and recovery assumptions are explicitly stated and sourced; if assumed, mark with [VERIFY]
