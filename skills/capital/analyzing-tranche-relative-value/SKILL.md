---
name: analyzing-tranche-relative-value
language: en
description: Evaluates structured product tranche pricing with spread analysis, yield attribution, and comparable structure benchmarking. Use when assessing tranche value, comparing structured product pricing, or analyzing spread components.
tags:
  - analysis
  - structured-finance
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Tranche Relative Value

## When To Use

- Evaluating new-issue tranche pricing against secondary market comparables
- Comparing spread levels across tranches within a single deal capital structure
- Assessing whether a tranche offers adequate compensation for its risk position (credit enhancement, WAL, subordination)
- Benchmarking CLO, ABS, RMBS, or CMBS tranches against peer deals, index levels, or corporate credit alternatives
- Supporting buy/sell/hold decisions on structured product positions

## Inputs To Gather

- **Deal documents**: Offering circular/supplement, waterfall description, collateral summary
- **Tranche specifics**: Rating, coupon type (fixed/floating), spread at issuance, credit enhancement level, expected WAL, payment window
- **Collateral profile**: Asset class, weighted-average coupon, WALA/WARM, delinquency and loss assumptions, concentration limits
- **Comparable pricing**: Recent new-issue spreads for same asset class, rating, and tenor; secondary bid/offer levels; dealer color sheets
- **Benchmark references**: SOFR swap curve, interpolated Treasury yields, relevant index levels (e.g., Palmer Square CLO index, ABX, CMBX) [VERIFY: confirm current benchmark conventions for the specific asset class]
- **Structural features**: Step-down triggers, turbo amortization provisions, optional redemption/call features, reinvestment period terms

## Workflow

1. **Map the capital structure** — Lay out all tranches from senior to equity: rating, size, spread/coupon, credit enhancement, and expected WAL. Calculate the cost-of-funds stack and excess spread available to subordinate tranches.

2. **Decompose the spread** — Break each tranche's nominal spread into component drivers:
   - **Expected loss compensation**: Modeled credit losses allocated to the tranche under base, stress, and rating-agency scenarios
   - **Liquidity premium**: Bid/ask width, dealer inventory depth, repo-ability, index eligibility
   - **Structural complexity premium**: Waterfall optionality, extension risk, prepayment variability, trigger proximity
   - **Residual/pure spread**: Compensation beyond quantifiable risk factors

3. **Run comparable analysis** — Identify 3-5 recent deals with similar collateral, vintage, and structural features. Normalize for differences in:
   - Credit enhancement levels (higher CE should trade tighter, all else equal)
   - WAL and duration profile
   - Sponsor/servicer quality and track record
   - Collateral composition (e.g., prime vs. non-prime, static vs. revolving)

4. **Assess cross-market value** — Compare the tranche spread to:
   - Same-rated corporate bonds at comparable duration
   - Other structured product sectors at the same rating tier
   - Historical spread range for this tranche type (percentile ranking over 1yr/3yr/5yr windows)

5. **Evaluate structural protections** — Determine whether the tranche's position in the waterfall justifies the spread:
   - Distance to trigger breach under stress scenarios
   - Sensitivity of WAL to prepayment speed changes (PSA multiples or CPR scenarios for MBS; CDR/CPR for CLOs)
   - Overcollateralization and interest coverage cushion trajectories over time
   - Call risk and reinvestment period impact on effective yield [VERIFY: confirm call provisions and exercise incentives for the specific deal type]

6. **Synthesize relative value conclusion** — Assign a relative value assessment (rich / fair / cheap) supported by quantified spread differential versus comparables and historical context.

## Output

Structure the analysis report with:

- **Executive Summary**: Asset class, tranche identifier, rating, spread, and relative value conclusion in 2-3 sentences
- **Capital Structure Overview**: Table of all tranches with key metrics (rating, size, spread, CE, WAL)
- **Spread Decomposition**: Breakdown of nominal spread into component drivers with estimated basis-point attribution
- **Comparable Deal Matrix**: Table of 3-5 peer tranches with normalized spread comparison and key differentiating factors
- **Cross-Market Context**: Chart or table showing the tranche versus same-rated corporate and other structured product alternatives
- **Structural Risk Assessment**: Summary of waterfall stress results, trigger cushions, and extension/call scenarios
- **Recommendation**: Rich/fair/cheap determination with supporting spread basis and identified catalysts or risks to the view

## Quality Checks

- Confirm all spread quotes are as-of the same date and use the same benchmark convention (DM to SOFR, Z-spread, I-spread) [VERIFY: benchmark convention varies by asset class and market]
- Verify credit enhancement percentages are calculated consistently (as % of current balance vs. original balance)
- Ensure comparable deals are genuinely comparable — same asset class, similar vintage, and structural form
- Check that WAL assumptions align with the prepayment/default scenarios used for the comparables
- Validate that any rating-agency model outputs cited match the current methodology version [VERIFY: rating agency criteria updates may affect tranche-level analysis]
- Flag any tranche where the spread decomposition leaves a residual exceeding 30% of nominal spread — this suggests missing risk factors or mispricing worth investigating
- Confirm liquidity assessment reflects actual market conditions (dealer axes, recent BWIC/OWIC results) rather than theoretical assumptions
