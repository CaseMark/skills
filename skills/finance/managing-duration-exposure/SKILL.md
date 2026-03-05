---
name: managing-duration-exposure
description: Structures portfolio duration management with hedging strategies and benchmark tracking. Use when managing interest rate risk, hedging duration, or optimizing portfolio duration.
tags:
  - management
  - fixed-income
  - risk
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Duration Exposure

Structures portfolio duration management with hedging strategies and benchmark tracking for fixed-income portfolios.

## When To Use

- Rebalancing portfolio duration toward a target or benchmark (e.g., Bloomberg US Aggregate)
- Assessing interest rate risk after yield curve shifts or central bank policy changes
- Constructing or evaluating duration hedges using swaps, futures, or options
- Reviewing duration drift from cash flows, maturities, prepayments, or new allocations
- Preparing duration exposure reports for investment committees or risk oversight

## Inputs To Gather

- **Portfolio holdings** — CUSIP/ISIN-level positions with par amounts, market values, and coupon details
- **Duration metrics** — Effective duration, modified duration, key rate durations (KRDs) per holding and at portfolio level
- **Benchmark profile** — Target index or custom benchmark with duration, KRD breakdown, and sector composition
- **Yield curve data** — Current Treasury/swap curves, recent curve shifts, and forward rate expectations
- **Hedge instruments available** — Treasury futures contracts (2Y, 5Y, 10Y, Ultra), interest rate swaps, swaptions, caps/floors
- **Risk limits** — Mandated duration band (e.g., benchmark +/- 0.5 years), maximum DV01, tracking error tolerance
- **Scenario parameters** — Parallel shift sizes (e.g., +/-50bp, +/-100bp), curve twist/butterfly scenarios

## Workflow

1. **Measure Current Exposure**
   - Calculate portfolio effective duration, spread duration, and DV01
   - Decompose into key rate duration buckets (2Y, 5Y, 10Y, 30Y at minimum)
   - Compute duration contribution by sector (government, corporate, securitized, municipal)
   - Identify convexity profile — negative convexity from MBS/callables requires separate treatment

2. **Compare Against Benchmark/Target**
   - Map portfolio KRDs to benchmark KRDs at each tenor point
   - Calculate duration gap (portfolio duration minus benchmark duration)
   - Identify the largest KRD mismatches — these drive tracking error
   - Flag any duration drift from recent cash flows, paydowns, or new trades

3. **Design Hedging/Adjustment Strategy**
   - For parallel duration gap: size Treasury futures or swap overlays to close the gap
     - Futures hedge ratio = Target DV01 change / DV01 per contract [VERIFY contract specs for current delivery cycle]
     - Swap overlay: receive/pay fixed to lengthen/shorten duration
   - For curve positioning: use barbell/bullet trades or KRD-targeted futures to adjust specific tenor buckets
   - For convexity management: evaluate swaptions or Treasury options to offset MBS negative convexity
   - Estimate hedge cost: carry, roll, margin requirements, and bid-ask slippage

4. **Run Scenario Analysis**
   - Parallel shifts: +/-25bp, +/-50bp, +/-100bp — compute P&L impact on hedged vs. unhedged portfolio
   - Curve scenarios: bull steepener, bear flattener, twist — assess KRD mismatch impact
   - Spread scenarios: widening/tightening by sector to isolate spread duration risk from rate duration
   - Stress test: replay historical episodes (2013 taper tantrum, 2022 rate hiking cycle) against current positioning

5. **Document and Report**
   - Summarize current vs. target duration, KRD profile, and hedge positions
   - Present scenario P&L table with breakeven rate levels
   - List open hedge positions with notional, DV01 contribution, maturity/expiry, and roll dates
   - Note any residual risks: basis risk between hedges and portfolio, cross-currency duration if applicable
   - Flag upcoming events that could shift duration profile (Fed meetings, large maturities, MBS prepayment resets)

## Output

- **Duration Exposure Summary** — One-page table: portfolio duration, benchmark duration, gap, DV01, and KRD breakdown by tenor
- **Hedge Recommendation** — Instrument, direction, notional/contracts, expected DV01 impact, cost estimate
- **Scenario Analysis Matrix** — Grid of rate scenarios vs. portfolio P&L (total return and price return)
- **Risk Dashboard** — Tracking error estimate, duration band compliance status, largest KRD mismatches
- **Action Items** — Specific trades to execute, rebalancing triggers, next review date

## Quality Checks

- Duration and DV01 figures reconcile between portfolio analytics system and independent calculation
- Hedge sizing accounts for futures conversion factor and cheapest-to-deliver basis [VERIFY CTD bond for active contract]
- KRD buckets sum to approximately the total effective duration (within rounding tolerance)
- Scenario analysis includes both rate and spread duration effects — not rate-only
- MBS and callable bond durations use OAS-based effective duration, not modified duration
- Benchmark data is current — stale index rebalancing dates can distort duration comparisons [VERIFY index rebalance date]
- Hedge roll dates are flagged before expiry to avoid unintended duration gaps
- All duration figures specify the methodology (effective, modified, Macaulay) to prevent misinterpretation
