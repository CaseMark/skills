---
name: analyzing-agency-mortgage-bonds
language: en
description: Evaluates agency MBS with prepayment modeling, OAS analysis, and convexity assessment. Use when analyzing agency MBS, modeling prepayments, or evaluating mortgage bond convexity.
tags:
  - analysis
  - fixed-income
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Agency Mortgage Bonds

Evaluates agency MBS (Fannie Mae, Freddie Mac, Ginnie Mae) by modeling prepayment behavior, computing option-adjusted spread, and assessing negative convexity to support relative-value decisions in pass-throughs, CMOs, and specified pools.

## When To Use

- Screening agency pass-throughs or CMO tranches for portfolio inclusion
- Comparing OAS across coupons, vintages, or specified-pool stories (e.g., low-balance, high-LTV, NY geo)
- Stress-testing mortgage portfolios against rate shocks or housing scenarios
- Evaluating roll-down, carry, and dollar-roll economics
- Assessing negative convexity exposure and hedge ratios for a book of MBS

## Inputs To Gather

- **Bond identifiers**: CUSIP, pool number, or CMO tranche ID
- **Pool-level data**: WAC, WAM, WALA, original LTV, loan count, geographic concentration, loan size distribution, servicer
- **Market data**: current coupon TBA price, swap curve or Treasury curve, volatility surface (swaption vols), funding rate
- **Prepayment model choice**: dealer model (e.g., Bloomberg BCPS, Yield Book, Andrew Davidson) or proprietary CPR/CDR vectors
- **Analysis horizon**: static (spot OAS) vs. total-return over a holding period
- **Scenario set**: parallel shifts (±25/50/100/200 bp), curve twist, housing-price shock, refi-wave overlay

## Workflow

1. **Profile the collateral**
   - Pull pool-level factor data: current face, factor, WAC, WAM, WALA, avg loan size, geo mix, servicer
   - Identify prepayment-relevant attributes: burnout level (months since origination vs. coupon incentive history), curtailment seasoning, credit characteristics
   - For CMO tranches, map the cash-flow waterfall (sequential, PAC/support, IO/PO, Z-bond) and identify the effective collateral group

2. **Generate prepayment projections**
   - Run the selected prepayment model to produce monthly CPR (or SMM) and CDR vectors under each rate scenario
   - Decompose CPR into turnover, refinancing, curtailment, and default/liquidation components
   - Compare model output to recent 1-month, 3-month, and 6-month actual speeds; flag divergences >15% as [VERIFY]
   - Sensitivity-check the refi S-curve: confirm the model's media effect, burnout, and loan-size adjustments are reasonable for the pool's profile

3. **Compute OAS and key risk metrics**
   - Build the cash-flow engine: apply monthly prepayment/default vectors to the amortization schedule, net of servicing and guarantee fees
   - Discount cash flows over a Monte Carlo or lattice interest-rate model calibrated to the current swaption vol surface
   - Output: OAS (bp), Z-spread, effective duration, effective convexity, key-rate durations (2y, 5y, 7y, 10y, 30y)
   - For CMOs, report tranche-level metrics plus the average life window under slow/median/fast prepay assumptions

4. **Assess convexity and optionality**
   - Calculate price response to ±50 bp and ±100 bp parallel shifts; derive empirical duration and convexity
   - Quantify negative convexity cost: the OAS give-up attributable to the embedded prepay option versus a bullet swap at equivalent duration
   - Evaluate PVBP asymmetry: how much more the bond loses in a rally vs. what it gains in a sell-off
   - For specified pools, compute the pay-up (price premium over TBA) and the breakeven prepayment advantage needed to justify it

5. **Run relative-value comparison**
   - Rank candidates by OAS per unit of effective duration or OAS vs. empirical vol-adjusted spread
   - Compare carry + roll-down vs. comparable-duration Treasuries, swaps, or corporate bonds
   - Assess dollar-roll specialness for TBA-eligible pools: implied financing rate vs. repo
   - Factor in liquidity (bid-ask, daily volume, TBA deliverability) and balance-sheet cost (risk-weight, LCR treatment) [VERIFY regulatory capital treatment against current rules]

6. **Stress-test and scenario analysis**
   - Run total-return projections over the target horizon under base, bull, and bear rate scenarios plus a refi-wave overlay
   - Shock housing prices (–10%, –20%) and evaluate CDR sensitivity for credit-risk transfer reference pools if applicable
   - Identify breakeven spread widening: how many bp of OAS widening erases the carry advantage over the alternative

## Output

- **Executive summary**: Recommended action (buy/hold/sell/switch) with 1-2 sentence rationale
- **Collateral profile table**: WAC, WAM, WALA, avg loan size, top-3 states, servicer, burnout indicator
- **Prepayment exhibit**: CPR vectors under base/bull/bear, comparison to recent actuals
- **Risk metrics table**: OAS, Z-spread, effective duration, effective convexity, key-rate durations
- **Relative-value grid**: OAS, carry, roll-down, and total-return rank across the comparison set
- **Scenario matrix**: Price and total-return outcomes under each rate/housing/refi scenario
- **Key risks and caveats**: Model risk, liquidity, regulatory-capital treatment, extension/contraction risk

## Quality Checks

- Confirm OAS is computed against the correct benchmark curve (swaps vs. Treasuries) and state which was used
- Verify prepayment model vintage — stale model versions may mis-price the current refi incentive [VERIFY model version/date]
- Cross-check effective duration against empirical duration from recent price moves; flag discrepancies >0.3 years
- Ensure pay-up analysis for specified pools uses a consistent TBA base price (same settlement month)
- Validate that Monte Carlo path count is sufficient (typically >=500 paths) for OAS convergence within ±1 bp
- Confirm all prices are on the same settlement date and factor month
- Flag any pool with factor <0.10 as potentially illiquid with unreliable prepayment statistics
