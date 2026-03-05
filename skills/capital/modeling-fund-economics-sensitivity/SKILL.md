---
name: modeling-fund-economics-sensitivity
description: Builds fund economic models with sensitivity across deployment pace, exit multiples, and fee/carry structures for LP and GP returns. Use when modeling fund economics, projecting LP net returns, or analyzing fee-adjusted performance.
tags:
  - modeling
  - fund-formation-and-structuring
metadata:
  author: casemark
  practice_areas:
    - Fund Formation
    - Fund Structuring
    - Partnership Law
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Fund Economics Sensitivity

Builds fund economic models with sensitivity analysis across deployment pace, exit multiples, and fee/carry structures to project LP net returns and GP economics.

## When To Use

- Modeling projected LP net IRR and net TVPI for a new fund's PPM or marketing materials
- Comparing fee/carry structures during LPA negotiations (e.g., 2/20 vs. 1.5/20 with catch-up variations)
- Stress-testing fund returns under different deployment and exit timing scenarios
- Evaluating GP economics (carried interest, management fee revenue) across fund life
- Presenting sensitivity tables to an LP advisory committee or investment committee

## Inputs To Gather

- **Fund parameters**: target fund size, GP commitment percentage, fund term (investment period + harvest period), extension options
- **Fee structure**: management fee rate and basis (committed vs. invested capital), fee step-down timing and rate, organizational expense cap, fund expense budget
- **Carry structure**: carried interest percentage, preferred return (hurdle rate), catch-up split and rate (e.g., 80/20 catch-up to 20%), whole-fund vs. deal-by-deal waterfall, clawback provisions
- **Deployment assumptions**: number of investments, average check size, deployment pace (e.g., 3–5 year investment period), recycling percentage of returned capital
- **Exit assumptions**: target gross MOIC range (e.g., 1.5x–3.0x), holding period distribution (3–7 years), exit timing curve (early realizations vs. back-loaded)
- **Sensitivity ranges**: define low/base/high cases for each key variable

## Workflow

1. **Build the capital call schedule**
   - Model LP capital calls based on deployment pace assumptions (front-loaded, even, or J-curve profile)
   - Layer in management fees drawn from commitments (or net against invested capital, depending on LPA terms)
   - Account for GP co-investment and any fee offsets (e.g., portfolio company monitoring fees credited against management fees)

2. **Model the portfolio and exit cash flows**
   - Project gross investment returns for each scenario using target MOIC and holding period
   - Distribute exits across the harvest period — apply a realization curve rather than assuming a single exit date
   - If recycling is permitted, model reinvestment of early proceeds within the investment period [VERIFY: confirm recycling cap in LPA, typically 100–125% of commitments]

3. **Apply the waterfall distribution**
   - Calculate return of capital, preferred return accrual, catch-up allocation, and residual carried interest split
   - For whole-fund waterfalls: aggregate all proceeds before splitting carry; track cumulative preferred return threshold
   - For deal-by-deal waterfalls: compute carry on each realization separately; model escrow/holdback for clawback protection [VERIFY: escrow percentage — commonly 20–30% of carry distributions]
   - Compute net distributions to LPs after carry and expenses

4. **Calculate return metrics**
   - **LP net IRR**: time-weighted return on LP cash flows (calls in, distributions out) net of all fees and carry
   - **LP net TVPI**: total value to paid-in capital (distributions + remaining NAV / total called capital)
   - **LP DPI**: distributions to paid-in (realized returns only)
   - **GP carry**: total carried interest dollars and as a multiple of GP commitment
   - **GP management fee revenue**: cumulative fees over fund life, before and after step-down

5. **Run sensitivity analysis**
   - Build a matrix varying **exit multiple** (rows) against **deployment pace** (columns) for LP net IRR and net TVPI
   - Run a second matrix varying **fee/carry structure** against **exit multiple** for LP net returns
   - Test specific scenarios: (a) rapid deployment with lower multiples, (b) slow deployment with higher multiples, (c) early realizations enabling recycling
   - Highlight breakeven exit multiple where LP net IRR equals the preferred return hurdle

6. **Stress-test edge cases**
   - Model a loss scenario (0.5x–0.8x gross MOIC) to show LP downside and confirm no carry is distributed
   - Test the impact of fund extensions (1–2 years) on IRR drag from continued fee payments
   - Verify clawback triggers under deal-by-deal waterfalls with mixed winner/loser outcomes

## Output

- **Summary table**: base case LP net IRR, net TVPI, DPI, and GP carry for the primary scenario
- **Sensitivity matrices**: 2–3 tables showing LP net IRR and net TVPI across variable combinations
- **Cash flow schedule**: annual summary of calls, distributions, net cash flow, and cumulative metrics
- **Fee analysis**: total management fees, fee offsets, organizational expenses, and net fee load as percentage of committed capital
- **GP economics summary**: carry dollars by scenario, management fee revenue, and total GP compensation
- **Assumptions register**: all inputs clearly stated with sources, including any [VERIFY] flags for terms pending LPA finalization

## Quality Checks

- Confirm that LP net IRR is always lower than gross IRR — if not, the fee/carry layer is misapplied
- Verify that at the preferred return hurdle, zero carry is distributed (waterfall integrity check)
- Ensure capital calls never exceed total commitments (unless recycling is modeled and within permitted limits)
- Cross-check that LP net TVPI = (total distributions + remaining NAV) / total called capital — arithmetic consistency
- Validate that management fee step-down timing matches LPA terms (commonly steps down from committed to invested capital basis after investment period) [VERIFY: confirm step-down trigger and rate]
- Compare modeled J-curve profile against industry benchmarks for the fund's strategy (e.g., buyout funds typically show positive net cash flow by years 5–6)
- Flag any scenario where GP carry exceeds 30% of total fund profits as unusual and warranting review
