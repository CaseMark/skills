---
name: modeling-interest-rate-and-basis-risk
language: en
description: Analyzes structural interest rate exposure with fixed/floating mismatch, basis risk, and cap/floor adequacy assessment. Use when modeling structural rate risk, analyzing basis risk, or evaluating interest rate hedging needs.
tags:
  - modeling
  - structured-finance
  - risk
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
# Modeling Interest Rate And Basis Risk

## When To Use

- Evaluating fixed/floating mismatch in a securitization or structured credit vehicle (ABS, MBS, CLO)
- Quantifying basis risk where asset and liability reference rates differ (e.g., SOFR vs. Prime, 1M SOFR vs. 3M SOFR, legacy LIBOR transition mismatches)
- Stress-testing adequacy of interest rate caps, floors, or swaps embedded in a deal structure
- Assessing net interest margin (NIM) erosion under parallel and non-parallel rate shifts
- Modeling waterfall sensitivity to rate movements for investor reporting or new-issue structuring

## Inputs To Gather

- **Asset-side rate terms**: Index, spread, reset frequency, periodic/lifetime caps and floors, accrual basis (ACT/360, 30/360, etc.)
- **Liability-side rate terms**: Tranche coupon type (fixed or floating), index, spread, reset frequency, accrual basis
- **Hedge instruments**: Cap/floor strike rates, notional schedules, swap fixed rates, maturity dates, counterparty details
- **Forward rate curve**: Current benchmark curve (SOFR, Treasury, etc.) plus stressed scenarios [VERIFY curve source and as-of date]
- **Collateral cash flow projections**: Prepayment vectors (CPR/PSA), default/loss assumptions (CDR/severity), recovery lag
- **Deal waterfall rules**: Priority of payments, trigger definitions tied to coverage ratios or overcollateralization levels
- **Historical basis spread data**: Time series of spread between relevant indices (e.g., 1M SOFR vs. 3M SOFR) for calibrating basis volatility

## Workflow

1. **Map the rate structure** — Catalog every rate index, reset date, and day-count convention on both asset and liability sides. Identify each point of mismatch: index basis (different benchmarks), tenor basis (different reset frequencies), and day-count basis.

2. **Build the base-case cash flow model** — Project asset collections and liability payments period-by-period using the current forward curve. Calculate gross interest income, debt service, and excess spread through the waterfall. Confirm the model ties to the deal's payment date report or offering memorandum examples.

3. **Quantify fixed/floating mismatch** — Compute net interest rate sensitivity per tranche:
   - Duration gap between fixed-rate assets and floating-rate liabilities (or vice versa)
   - DV01 of each leg (dollar change per 1 bp parallel shift)
   - Excess spread compression under +100, +200, +300 bp parallel shifts and corresponding downward shifts

4. **Isolate basis risk** — Hold the overall rate level constant and shock the basis spread between mismatched indices:
   - Widen/narrow the spread between asset and liability indices by historical 1-sigma and 2-sigma moves
   - Model reset-date timing mismatch (e.g., assets reset on the 1st, liabilities on the 15th) to capture intra-period carry leakage
   - If transitioning from LIBOR to SOFR, model the credit spread adjustment (CSA) impact on net margin [VERIFY applicable CSA terms per deal docs]

5. **Evaluate cap/floor adequacy** — For deals with purchased interest rate caps:
   - Compare cap strike to breakeven coupon rate at which excess spread turns negative
   - Project cap notional amortization against expected collateral balance to detect uncovered exposure windows
   - Stress-test whether the cap remains in-the-money under the deal's rating-agency required rate scenarios [VERIFY agency-specific stress levels: S&P, Moody's, Fitch, KBRA, DBRS]

6. **Run scenario matrix** — Construct a table of outcomes across rate paths:
   - Parallel shifts: -100, 0, +100, +200, +300 bp
   - Non-parallel: steepener (+50 short / +200 long), flattener (+200 short / +50 long), inversion
   - Basis stress: index spread widening of +25, +50, +75 bp
   - Combined: worst-case rate shift + basis stress + elevated prepayments

7. **Assess waterfall triggers** — Determine whether any rate/basis scenario causes:
   - Overcollateralization or interest coverage triggers to breach
   - Principal cash flow redirection from subordinate to senior tranches
   - Reserve fund draws or liquidity facility taps

## Output

- **Rate risk summary table**: Per-tranche DV01, duration, and excess spread under base and stressed curves
- **Basis risk heat map**: Matrix showing NIM impact across combinations of rate level and basis spread shocks
- **Cap/floor adequacy assessment**: Period-by-period comparison of cap coverage vs. exposure, flagging any uncovered windows
- **Trigger proximity analysis**: Distance (in bps of excess spread) to each waterfall trigger under each scenario
- **Recommendation memo**: Identify whether additional hedging is warranted, specify notional, strike, and tenor for any recommended cap or swap overlay

## Quality Checks

- Confirm asset and liability cash flows balance through the waterfall under the base case (no unexplained leakage)
- Verify day-count conventions are applied consistently — a 30/360 vs. ACT/360 mismatch between model and deal docs is a common source of error
- Cross-check model DV01 against Bloomberg or vendor analytics where available
- Ensure forward curve inputs match a documented source and snapshot date [VERIFY]
- Validate that cap notional schedules match the confirmation or offering circular, not just assumed amortization
- Test for sign errors: rising rates should compress excess spread in a receive-fixed / pay-floating structure, not expand it
- Confirm basis spread shocks are applied only to the relevant index differential, not double-counted in the parallel shift
