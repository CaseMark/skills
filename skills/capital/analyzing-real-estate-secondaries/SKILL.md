---
name: analyzing-real-estate-secondaries
description: Evaluates real estate fund secondary transactions with NAV validation, property-level assessment, and sector/vintage analysis. Use when pricing RE secondaries, analyzing property portfolios, or evaluating REIT fund interests.
tags:
  - analysis
  - secondaries-and-gp-led
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Real Estate Secondaries

Evaluates real estate fund secondary transactions with NAV validation, property-level assessment, and sector/vintage analysis.

## When To Use

- Pricing an LP interest in a real estate fund on the secondary market
- Evaluating a GP-led continuation vehicle involving real estate assets
- Assessing a portfolio of RE fund interests for a multi-fund secondary trade
- Reviewing a REIT fund stake or non-traded REIT secondary opportunity
- Validating reported NAV against independent property-level underwriting

## Inputs To Gather

- **Fund financials**: Most recent quarterly NAV statement, capital account statement, audited financials (confirm vintage of NAV — stale NAVs >6 months require adjustment)
- **Property-level data**: Rent rolls, occupancy rates, lease expiration schedules, capital expenditure budgets, and property appraisals (if available)
- **Fund terms**: LPA provisions on transfers, ROFR/consent requirements, unfunded commitments, fee structure (management fee, carried interest, catch-up, clawback)
- **GP track record**: Prior fund performance (net IRR, net MOIC, DPI), realization history, asset management capabilities
- **Market context**: Comparable secondary transaction pricing (% of NAV), current cap rate benchmarks by sector/geography, interest rate environment
- **Portfolio composition**: Sector breakdown (multifamily, office, industrial, retail, hospitality, data centers), geographic concentration, vintage distribution

## Workflow

1. **Validate reported NAV**
   - Compare GP-reported NAV date to transaction date; apply time-adjustment if NAV is stale (>1 quarter)
   - Cross-check cap rates embedded in appraisals against current market cap rates for the relevant sector/geography
   - Identify any NAV adjustments for leverage, pending dispositions, or unrealized development gains
   - Flag properties carried at cost or with no recent third-party appraisal

2. **Conduct property-level assessment**
   - For top 10 assets by value (or all assets if portfolio is concentrated): review occupancy, tenant credit quality, lease rollover risk, and deferred capex
   - Categorize each property as core, value-add, or opportunistic based on current stabilization status
   - Assess sector-specific risks: office return-to-work exposure, retail e-commerce disruption, multifamily rent regulation risk [VERIFY — jurisdiction-specific rent control laws]
   - Note any development or construction assets and stage of completion

3. **Analyze fund structure and remaining economics**
   - Calculate remaining fund life and expected hold period for unrealized assets
   - Model distribution waterfall: estimate GP carry accrual, management fee drag on remaining NAV, and any preferred return hurdles
   - Quantify unfunded commitment exposure — determine if buyer assumes unfunded obligations and model potential capital calls
   - Review transfer mechanics: consent requirements, ROFR timelines, transfer fee provisions [VERIFY — specific LPA transfer restriction language]

4. **Build pricing framework**
   - Establish base case, upside, and downside scenarios using adjusted NAV as the anchor
   - Apply sector-level discount/premium adjustments (e.g., industrial portfolios may trade at tighter discounts than office-heavy funds)
   - Factor in vintage analysis: late-life funds with near-term liquidity warrant tighter pricing; early-vintage funds with J-curve risk warrant wider discounts
   - Compare implied pricing to recent secondary market benchmarks (Greenhill/Jefferies secondary market data, Lazard benchmarks)
   - Calculate implied IRR to buyer at proposed pricing under each scenario

5. **Assess GP and fund-level risk factors**
   - Evaluate GP organizational stability, key-person risk, fundraising trajectory
   - Review fund-level leverage: subscription lines, asset-level debt maturity profiles, LTV ratios
   - Identify any litigation, environmental liabilities, or regulatory issues tied to underlying properties
   - For GP-led transactions: assess alignment of interests, rollover percentage, third-party validation (staple financing, fairness opinion)

## Output

- **Executive summary**: Transaction overview, recommended bid range (expressed as % of NAV), and key risk/return drivers
- **NAV bridge**: Walk from reported NAV to adjusted NAV with line-item adjustments (cap rate revaluation, stale NAV time adjustment, fee drag, unfunded commitments)
- **Property-level heat map**: Ranking of top assets by risk-adjusted value contribution, flagging concentration risks
- **Scenario analysis table**: Base/upside/downside with implied IRR, MOIC, and DPI to buyer at various pricing levels
- **Risk register**: Itemized risks with severity ratings (sector, leverage, GP, structural, transfer/legal)
- **Recommendation**: Clear bid/pass/conditional recommendation with stated assumptions

## Quality Checks

- Confirm NAV date and ensure all adjustments are time-stamped and sourced
- Verify cap rate assumptions against at least two independent benchmarks (e.g., NCREIF, Green Street, CBRE)
- Ensure unfunded commitment treatment is consistent with proposed transaction structure (assumed vs. excluded)
- Cross-check waterfall math: carry accrual, preferred return, and GP clawback provisions against LPA terms
- Validate that sector/geographic concentration percentages sum correctly
- Mark all jurisdiction-dependent assumptions (rent control, transfer taxes, zoning) with [VERIFY]
- Flag any data gaps — missing rent rolls, outdated appraisals, or absent audited financials — as material limitations
