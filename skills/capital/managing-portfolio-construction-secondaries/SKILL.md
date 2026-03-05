---
name: managing-portfolio-construction-secondaries
description: Structures secondary portfolio construction with vintage diversification, strategy mix, and geographic allocation optimization. Use when building secondary portfolios, managing allocation targets, or optimizing portfolio composition.
tags:
  - management
  - secondaries-and-gp-led
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Portfolio Construction Secondaries

## When To Use

- Building or rebalancing a secondary fund's portfolio allocation framework
- Setting vintage year, strategy, and geography targets for a new secondary fund
- Evaluating whether a prospective secondary deal fits within existing portfolio parameters
- Preparing portfolio construction reports for LPs or investment committees
- Analyzing concentration risk across an active secondary portfolio

## Inputs To Gather

- **Fund mandate and strategy documents**: target fund size, return objectives (net IRR, net MOIC), investment period, and any LP side-letter constraints
- **Current portfolio snapshot**: existing holdings by vintage year, strategy type (LP-led, GP-led continuation, direct secondary, structured secondary, preferred equity), geography, sector, and underlying GP
- **Pipeline and committed deals**: deals in closing or under LOI with projected deployment amounts
- **Pricing and NAV data**: latest NAV marks, purchase price discounts/premiums, and J-curve assumptions per strategy type
- **Benchmark data**: secondary fund peer benchmarks for allocation bands (e.g., Greenhill, Jefferies, Evercore secondary market surveys) [VERIFY: confirm latest available benchmark year]
- **Macro overlay**: interest rate environment, denominator effect dynamics, and LP liquidity trends influencing secondary supply

## Workflow

1. **Define allocation framework**
   - Set target bands for each construction dimension:
     - **Vintage diversification**: maximum concentration per vintage year (typically 15–25% of committed capital per vintage) [VERIFY: confirm against fund LPA limits]
     - **Strategy mix**: LP-led portfolio purchases vs. GP-led continuation vehicles vs. direct secondaries vs. structured/preferred equity — set target and maximum percentages for each
     - **Geography**: North America, Europe, Asia-Pacific, Rest of World — set target ranges reflecting sourcing capability and hedging appetite
     - **Sector**: technology, healthcare, industrials, consumer, financial services, energy — set soft targets to avoid unintended concentration
   - Document whether bands are hard limits (LPA-driven) or soft targets (IC-guided)

2. **Map current portfolio against targets**
   - Aggregate holdings by each dimension and calculate current allocation percentages
   - Identify overweight and underweight positions relative to target bands
   - Flag single-GP concentration (typically cap at 10–15% of NAV) and single-fund concentration
   - Calculate weighted average discount to NAV and blended expected return across the book

3. **Stress-test and scenario analysis**
   - Model the impact of pipeline deals on allocation percentages before approving new commitments
   - Run scenarios: (a) baseline NAV growth, (b) market correction with 15–20% NAV writedown, (c) accelerated distributions reducing exposure to older vintages
   - Assess liquidity coverage: unfunded commitments from GP-led vehicles vs. expected distributions from mature LP positions

4. **Optimize portfolio composition**
   - Prioritize deal sourcing to fill underweight buckets — e.g., if GP-led allocation is below target, increase sourcing focus on continuation vehicles
   - Evaluate trade-offs: LP portfolios offer vintage diversification but carry tail-end exposure; GP-led deals offer higher return potential but concentrate manager risk
   - Apply pricing discipline: set maximum bid prices per strategy type to maintain portfolio-level return targets
   - Consider FX hedging costs when adjusting geographic allocation

5. **Generate portfolio construction report**
   - Produce allocation tables showing current vs. target vs. maximum for each dimension
   - Include visual dashboards (vintage waterfall, strategy pie, geographic heat map)
   - Summarize top-10 holdings by NAV with underlying GP, fund, vintage, and purchase discount
   - Highlight drift alerts where any dimension exceeds soft or hard limits
   - Provide forward deployment plan showing projected allocation after pipeline deals close

## Output

- **Portfolio construction report** containing:
  - Executive summary with portfolio-level metrics (total NAV, committed capital deployed %, weighted average discount, blended target return)
  - Allocation tables across vintage, strategy, geography, and sector with current / target / max columns
  - Concentration analysis: top-GP exposure, top-fund exposure, single-deal maximums
  - Scenario analysis results with sensitivity to NAV changes and distribution timing
  - Forward deployment recommendations with specific allocation gaps to fill
  - Risk flags and [VERIFY] markers for any data points requiring confirmation (stale NAVs, unconfirmed commitments, pending GP consent)

## Quality Checks

- Confirm all NAV data is from the most recent reporting period; mark older marks with [VERIFY]
- Validate that allocation percentages sum correctly across each dimension
- Cross-check that hard limits from the LPA are accurately reflected — misstatement of LPA constraints is a material compliance risk
- Ensure GP-led continuation vehicle allocations account for both the new commitment and any rolled exposure from the predecessor fund
- Verify that FX rates used for geographic allocation reflect current spot or hedged rates, not stale figures
- Confirm that the denominator used (committed capital vs. invested capital vs. NAV) is consistent throughout and matches the fund's stated methodology
