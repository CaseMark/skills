---
name: analyzing-annuity-products
description: Evaluates annuity structures with guaranteed benefit analysis, fee comparison, and surrender value modeling. Use when analyzing annuities, comparing guaranteed benefits, or evaluating annuity products.
tags:
  - analysis
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Annuity Products

Evaluates annuity structures with guaranteed benefit analysis, fee comparison, and surrender value modeling.

## When To Use

- Comparing fixed, variable, fixed-indexed, or registered index-linked annuity (RILA) products
- Evaluating guaranteed living benefit riders (GLWB, GMIB, GMAB, GMWB)
- Modeling surrender charge schedules and free withdrawal provisions
- Assessing total cost of ownership across competing annuity contracts
- Analyzing crediting strategies, cap rates, participation rates, and spread/margin structures
- Reviewing suitability of an annuity recommendation for a specific client profile

## Inputs To Gather

- **Contract prospectus or product specification sheet** — rider names, fee schedules, crediting methods, surrender periods
- **Guaranteed benefit rider details** — rollup rates, step-up frequencies, benefit bases, withdrawal percentages by age band
- **Fee schedule** — mortality & expense (M&E) charge, administrative fees, rider charges, sub-account expense ratios (variable annuities), spread/margin (FIAs)
- **Surrender schedule** — declining charge percentages by contract year, free withdrawal allowance, MVA (market value adjustment) presence [VERIFY]
- **Crediting strategy details** (indexed products) — index choices, cap rates, participation rates, floor, buffer/shield levels, crediting method (point-to-point, monthly average, monthly sum)
- **Client context** (if suitability review) — age, risk tolerance, income needs, time horizon, existing annuity holdings, tax status

## Workflow

1. **Classify the product type**
   - Determine: fixed / variable / fixed-indexed / RILA / immediate / deferred income annuity
   - Note the issuing carrier, AM Best rating [VERIFY], and state of issue [VERIFY state-specific annuity regulations]

2. **Map the fee structure**
   - Extract all explicit charges: M&E, admin, rider fees (basis points per year on benefit base vs. account value)
   - Identify implicit costs: spread/margin on indexed credits, sub-account expense ratios
   - Calculate **total annual drag** — sum of all recurring charges expressed in basis points

3. **Analyze guaranteed benefit riders**
   - Document the benefit base mechanics: simple vs. compound rollup rate, rollup duration cap, step-up rules
   - Map withdrawal percentages by attained age band (e.g., 5.0% at 65, 5.5% at 70)
   - Identify rider activation requirements: waiting periods, annuitization triggers, required holding periods
   - Note rider termination events: excess withdrawal impact, lump-sum triggers, spousal continuation rules

4. **Model surrender value trajectory**
   - Build a year-by-year projection of surrender charges from contract issue through full liquidity
   - Factor in free withdrawal corridor (typically 10% of account value or premium) [VERIFY per contract]
   - Flag MVA provisions — note whether MVA can increase or decrease surrender value based on interest rate movement

5. **Evaluate crediting strategy (indexed products)**
   - Document each available index allocation and its parameters (cap, participation rate, spread, floor/buffer)
   - Assess historical back-tested performance where available — note that back-tests are illustrative, not predictive
   - Identify whether caps/participation rates are guaranteed or subject to annual renewal at carrier discretion

6. **Run comparative analysis** (if multiple products)
   - Normalize fee comparison to a common basis (bps on account value per year)
   - Compare guaranteed income streams at identical withdrawal ages and initial premiums
   - Rank surrender liquidity by calculating breakeven year (when surrender value exceeds cumulative premium net of charges)
   - Compare crediting potential under bull, flat, and bear index scenarios

7. **Assess suitability alignment** (if client context provided)
   - Match product features to stated objectives: income guarantee vs. growth vs. principal protection
   - Flag concerns: surrender period exceeding client time horizon, rider fees eroding value for clients unlikely to use guaranteed income, 1035 exchange losing existing benefits

## Output

Produce a structured **Annuity Product Analysis Report** containing:

- **Product Summary Table** — carrier, product name, type, issue state, AM Best rating, surrender period length
- **Fee Comparison Matrix** — itemized charges with total annual cost in basis points
- **Guaranteed Benefit Rider Comparison** — rollup rates, withdrawal percentages, activation rules, termination triggers
- **Surrender Schedule Grid** — year-by-year charges with free withdrawal allowance noted
- **Crediting Strategy Summary** (indexed products) — index options, current caps/participation rates, floor/buffer levels
- **Comparative Ranking** (multi-product) — side-by-side on cost, income potential, liquidity, and downside protection
- **Suitability Notes** (if applicable) — alignment with client objectives, flagged concerns, recommendation rationale

## Quality Checks

- Verify all fee figures against the contract prospectus or product spec — do not rely on marketing materials alone
- Confirm guaranteed rollup rates and withdrawal percentages are contractual, not illustrated [VERIFY]
- Ensure surrender charge schedules match the specific share class or premium band [VERIFY]
- Flag any carrier credit ratings below A- (AM Best) as elevated counterparty risk
- Mark all cap rates, participation rates, and spreads as "current — subject to change" unless contractually guaranteed
- Note that tax treatment of annuity withdrawals (LIFO ordinary income, 10% penalty before 59.5) should be confirmed with a tax advisor [VERIFY applicable tax rules]
- Cross-check that state-specific annuity suitability standards (e.g., NAIC Best Interest model adoption) are referenced where relevant [VERIFY by state]
