---
name: modeling-resource-depletion-economics
description: Builds depletion models with production decline, reserve replacement economics, and terminal value analysis for finite-life assets. Use when modeling depletion, analyzing resource longevity, or evaluating reserve life economics.
tags:
  - modeling
  - real-assets-and-natural-resources
metadata:
  author: casemark
  practice_areas:
    - Natural Resources
    - Energy Capital
    - Commodity Investment
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Resource Depletion Economics

Builds depletion models with production decline, reserve replacement economics, and terminal value analysis for finite-life assets.

## When To Use

- Valuing oil & gas properties, mining concessions, or timber tracts where asset life is bounded by extractable reserves
- Forecasting production revenue streams under hyperbolic, exponential, or harmonic decline assumptions
- Evaluating reserve replacement economics — whether infill drilling, secondary recovery, or exploration capex extends economic life at acceptable returns
- Calculating terminal/salvage value and asset retirement obligations (ARO) for finite-life assets
- Stress-testing resource investments against commodity price, decline rate, and cost escalation scenarios

## Inputs To Gather

- **Reserve estimates**: Proved (1P), proved + probable (2P), and contingent resource volumes with classification basis (SEC, PRMS, NI 51-101) [VERIFY classification standard used]
- **Current production rates**: Recent monthly/quarterly production data (BOE/d, tons/month, MBF/year as applicable)
- **Decline curve parameters**: Initial decline rate (Di), b-factor (hyperbolic exponent), and minimum decline rate (Dmin) if using modified hyperbolic
- **Commodity pricing**: Strip pricing, flat-price assumptions, or escalation model; specify real vs. nominal terms
- **Operating costs**: LOE/per-unit lifting costs, royalties/overriding royalties, severance/ad valorem taxes [VERIFY applicable fiscal regime]
- **Capital program**: Maintenance capex, development capex schedule, and reserve replacement investment plan
- **Discount rate / WACC**: Risk-adjusted rate appropriate to resource type and jurisdiction
- **ARO / reclamation costs**: Plugging & abandonment, mine closure, or reforestation obligations with timing estimates

## Workflow

1. **Establish reserve base and production profile**
   - Classify reserves by category (PDP, PDNP, PUD, probable, possible)
   - Fit decline curves to historical production; select decline model (exponential for mature assets, hyperbolic for unconventional, harmonic where warranted)
   - Set economic limit — production rate at which net revenue equals operating cost

2. **Build revenue forecast**
   - Apply production volumes to commodity price deck on a per-period basis
   - Account for product mix (oil/gas/NGL ratios, ore grade variation over mine life)
   - Incorporate hedging or contract pricing if applicable

3. **Layer in cost structure**
   - Fixed vs. variable opex separation; apply per-unit variable costs to production schedule
   - Schedule development capex tied to reserve category conversion (PUD → PDP)
   - Include royalty burdens, production taxes, and income tax modeling [VERIFY royalty/tax rates by jurisdiction]

4. **Model reserve replacement economics**
   - For each tranche of replacement capex, calculate incremental reserves added, F&D cost ($/BOE or $/ton), and recycle ratio (netback ÷ F&D)
   - Compare recycle ratios against hurdle (typically >1.5× for conventional, >2.0× for unconventional) [VERIFY current market benchmarks]
   - Determine whether reserve additions extend asset life beyond base decline or merely slow decline rate

5. **Calculate terminal value and ARO**
   - Terminal value = salvage value of surface equipment + land residual − ARO obligation (discounted)
   - For mining: include reclamation bonding costs and post-closure monitoring
   - If perpetual tail production exists (e.g., low-rate stripper wells), capitalize at economic limit or apply a terminal multiple

6. **Run depletion and valuation**
   - Compute unit-of-production depletion for each period: (period production ÷ remaining reserves) × depletable basis
   - Generate PV-10 (undiscounted and at 10% per SEC convention) and NPV at project WACC
   - Calculate reserve life index (RLI = reserves ÷ annual production) at each forecast point

7. **Sensitivity and scenario analysis**
   - Vary commodity price (±20%, ±40%), decline rate (b-factor ±0.2), and opex escalation (CPI vs. oilfield-specific indices)
   - Run breakeven analysis: minimum commodity price to achieve target IRR or positive NPV
   - Tornado chart of top-5 value drivers ranked by impact on PV-10

## Output

The completed model should include:

- **Production forecast table**: Annual volumes by reserve category with cumulative depletion percentage
- **Cash flow waterfall**: Revenue → royalties → opex → capex → taxes → net cash flow, per period
- **Depletion schedule**: Unit-of-production depletion by period with remaining depletable basis
- **Reserve replacement summary**: F&D cost, recycle ratio, and incremental RLI per capex tranche
- **Valuation summary**: PV-10, NPV at WACC, IRR, and payback period
- **Sensitivity outputs**: Tornado chart, breakeven price, and scenario comparison table
- **Assumptions log**: Every key input with source, date, and [VERIFY] flags where data is uncertain

## Quality Checks

- Confirm cumulative production in forecast does not exceed total recoverable reserves (1P or 2P as specified)
- Verify decline curve fit against at least 12 months of historical production — flag assets with insufficient history
- Check that economic limit is correctly applied: no periods should show negative net operating income unless explicitly modeling pre-production or development phases
- Ensure depletion basis ties to acquisition/development cost less accumulated depletion and impairment
- Validate that PV-10 calculation uses pre-tax, pre-financing cash flows per SEC methodology when presented as PV-10 (vs. post-tax NPV)
- Cross-check RLI trajectory — if RLI is increasing while production declines, confirm reserve additions are the driver
- Confirm ARO timing is consistent with expected plug/abandonment or closure schedule, not artificially deferred
