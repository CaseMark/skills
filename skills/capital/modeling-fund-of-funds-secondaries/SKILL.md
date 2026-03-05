---
name: modeling-fund-of-funds-secondaries
description: Evaluates fund-of-funds secondary transactions with layer-on-layer fee analysis, double-carry impact, and net return adjustment. Use when pricing FoF secondaries, analyzing fee drag, or modeling net LP economics.
tags:
  - modeling
  - secondaries-and-gp-led
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Fund Of Funds Secondaries

Evaluates fund-of-funds secondary transactions with layer-on-layer fee analysis, double-carry impact, and net return adjustment. FoF secondaries carry structural complexity beyond single-fund deals because the buyer inherits two (or more) fee layers — the FoF manager's fees and carry plus the underlying GPs' fees and carry — all of which erode net returns and must be modeled explicitly to arrive at a defensible bid price.

## When To Use

- Pricing a secondary purchase of an LP interest in a fund-of-funds vehicle
- Comparing net economics of a FoF secondary versus direct secondary alternatives
- Analyzing fee drag and double-carry impact on projected net IRR and net MOIC
- Modeling LP-level cash flows for a portfolio of FoF positions being sold in bulk
- Evaluating GP-led restructurings where an FoF is rolling into a continuation vehicle

## Inputs To Gather

- **FoF-level terms**: management fee rate and basis (committed vs. invested), carry rate, preferred return, catch-up structure, fee offset provisions, GP commitment percentage
- **Underlying fund terms** (per fund in portfolio): management fee rate/basis, carry rate and waterfall structure (deal-by-deal vs. whole-fund), preferred return, GP clawback provisions
- **Portfolio data**: NAV by underlying fund, unfunded commitments, vintage year, fund life / expected remaining life, distribution pace assumptions
- **FoF financials**: FoF-level NAV, FoF unfunded commitments to underlying funds, FoF-level cash reserves, FoF operating expenses and organizational costs
- **Pricing inputs**: proposed purchase price (as % of FoF NAV), discount rate / target return, expected hold period
- **Underlying fund projections**: gross return assumptions by fund (or blended), pacing of capital calls and distributions, expected exit timing for key assets [VERIFY against most recent GP reporting]

## Workflow

1. **Map the fee stack.** Build a two-layer fee model: underlying GP fees/carry flowing up to the FoF, then FoF manager fees/carry applied on the net amounts. Confirm whether FoF management fees are still in the investment period (charged on commitments) or post-investment period (charged on NAV or invested capital). [VERIFY FoF LPA fee step-down provisions and any fee holidays]

2. **Project underlying fund cash flows.** For each material underlying fund position, model gross distributions and remaining capital calls based on fund maturity, sector, and GP track record. For tail-end funds, apply realization multiples; for mid-life funds, use growth-rate-based projections. Aggregate into a blended schedule of gross cash flows flowing to the FoF.

3. **Apply underlying GP fees and carry.** Deduct each underlying fund's management fees from capital calls and apply carried interest to distributions above the preferred return. Model waterfall mechanics — for whole-fund carry structures, track cumulative preferred return accrual; for deal-by-deal, apply carry per realization. Output: net distributions from underlying funds to the FoF.

4. **Apply FoF-level fees and carry.** From the net cash flows arriving at the FoF, deduct FoF management fees and operating expenses. Apply FoF-level carried interest using the FoF waterfall (typically whole-fund European style). Account for FoF GP clawback if modeling downside scenarios. Output: net distributions from FoF to the LP (the secondary buyer).

5. **Calculate net LP economics.** Using the purchase price as the initial outflow (plus any assumed unfunded obligations at the FoF level), compute net IRR, net MOIC, and DPI over the projected hold period. Break out total fee drag: show gross-to-net waterfall from underlying fund gross returns → after underlying GP fees → after FoF fees → net to LP.

6. **Run sensitivity analysis.** Key variables to stress-test:
   - Underlying fund gross return assumptions (±200 bps)
   - Exit timing / distribution pacing (±12 months)
   - Purchase price (±5% of NAV)
   - FoF fee renegotiation scenarios (fee waiver, reduced carry)
   - Unfunded commitment utilization rate (0%, 50%, 100% called)

7. **Quantify double-carry drag.** Isolate the incremental return erosion from the second carry layer. Compare net LP returns in the FoF structure versus a hypothetical direct secondary at equivalent gross returns. Express as basis-point drag on net IRR and percentage reduction in net MOIC.

## Output

- **Fee waterfall summary**: table showing gross return → net of underlying GP fees → net of FoF fees → net to buyer, expressed as both IRR and MOIC
- **Cash flow schedule**: quarterly or annual projected cash flows (capital calls, distributions, net to LP) over the hold period
- **Sensitivity matrix**: net IRR and net MOIC across key variable ranges (purchase price × gross return, purchase price × exit timing)
- **Double-carry impact analysis**: side-by-side comparison of FoF secondary versus equivalent direct secondary economics
- **Pricing recommendation**: breakeven purchase price at target return, with range based on scenario analysis
- **Assumption log**: all inputs, sources, and items flagged [VERIFY]

## Quality Checks

- Confirm that the sum of underlying fund NAVs reconciles to FoF-reported NAV (net of FoF-level adjustments and cash)
- Verify that fee calculations match LPA terms — particularly fee basis switches, offset provisions, and catch-up mechanics
- Check that carry is applied after preferred return accrual, not on total distributions
- Validate that unfunded commitments at both levels (FoF to underlying funds, buyer to FoF) are captured as potential future outflows
- Ensure gross-to-net bridge is internally consistent: gross return minus total fee drag equals net return
- Stress-test that breakeven pricing produces target IRR ± acceptable rounding tolerance
- Flag any underlying fund positions representing >15% of FoF NAV for individual review rather than blended assumptions
