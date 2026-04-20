---
name: analyzing-unitranche-financing
language: en
description: Evaluates unitranche structures with first-out/last-out splits, blended pricing, and agreement among lenders provisions. Use when analyzing unitranche options, comparing unitranche vs traditional structures, or modeling blended costs.
tags:
  - analysis
  - debt-capital-markets
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Unitranche Financing

## When To Use

- Evaluating a unitranche proposal from a direct lender or club against a traditional first-lien/second-lien structure
- Modeling blended cost of capital when the first-out/last-out waterfall split is known or estimated
- Reviewing an Agreement Among Lenders (AAL) for intercreditor risk, voting mechanics, and enforcement triggers
- Advising a sponsor or borrower on whether unitranche execution speed and certainty justify the pricing premium
- Comparing unitranche terms across competing lender proposals in a competitive financing process

## Inputs To Gather

- **Term sheet or commitment letter** — headline rate, OID, LIBOR/SOFR floor, maturity, call protection schedule
- **First-out/last-out split details** — tranche sizes, respective coupons, and any disclosed or implied waterfall economics
- **Agreement Among Lenders (AAL)** — voting thresholds, buy-out rights, cure rights, enforcement standstill periods, information-sharing restrictions
- **Borrower financials** — LTM EBITDA, projected EBITDA, total leverage, interest coverage, free cash flow profile
- **Comparable traditional structure** — first-lien and second-lien (or mezzanine) terms for the same credit to enable apples-to-apples comparison
- **Market context** — current broadly syndicated loan spreads, direct lending benchmarks, and relevant recent precedent transactions

## Workflow

1. **Map the capital structure** — Identify total unitranche commitment, first-out and last-out tranche sizes, and any unfunded revolving component. Calculate first-out vs. last-out as percentages of total facility and implied attachment/detachment points.

2. **Calculate blended cost** — Compute the weighted-average coupon across the first-out and last-out tranches. Add OID amortization (spread over expected life, not stated maturity) and any upfront fees. Express as all-in yield to the borrower and compare to the blended cost of an equivalent first-lien/second-lien stack.

3. **Analyze the AAL** — Review critical provisions:
   - **Voting and amendment rights** — Which decisions require unanimous vs. first-out-only consent? Can the last-out lender block amendments to payment waterfall, maturity, or collateral release?
   - **Buy-out mechanics** — At what price and under what triggers can first-out or last-out purchase the other tranche? Is the buy-out at par, par plus accrued, or fair market value?
   - **Enforcement and standstill** — How long must the last-out lender wait before it can direct enforcement after an event of default? What cure rights does the sponsor retain?
   - **Information barriers** — Are there restrictions on sharing borrower information between agent and last-out holders? [VERIFY applicability of specific AAL form — LSTA vs. bespoke]

4. **Stress-test the waterfall** — Model downside scenarios (e.g., 20–30% EBITDA decline) to evaluate:
   - Whether the borrower can still service the blended unitranche coupon
   - How first-out recovery holds up relative to a standalone first-lien facility
   - At what EBITDA level the last-out tranche becomes functionally impaired
   - Impact of PIK toggles or cash-sweep mechanics if present

5. **Compare execution factors** — Beyond pricing, assess:
   - **Certainty of close** — Single lender or small club vs. syndication risk
   - **Speed** — Typical 2–4 week close for unitranche vs. 6–8 weeks for syndicated
   - **Documentation flexibility** — Covenant package, permitted baskets, incremental capacity
   - **Relationship dynamics** — Ongoing amendment and waiver process with one counterparty vs. a broad syndicate

6. **Synthesize recommendation** — Frame the unitranche option in terms of total cost of capital, execution risk, covenant flexibility, and structural complexity. Quantify the premium (if any) the borrower pays for unitranche simplicity.

## Output

- **Structure summary table** — Side-by-side comparison: unitranche (with first-out/last-out breakdown) vs. traditional first-lien/second-lien, showing size, pricing, blended yield, maturity, and call protection
- **Blended cost analysis** — All-in yield calculation with OID and fee amortization
- **AAL risk assessment** — Key findings on voting, buy-out, standstill, and enforcement provisions with risk ratings (low/medium/high)
- **Stress-test results** — Downside coverage ratios and recovery analysis at defined EBITDA shock levels
- **Execution comparison** — Timeline, certainty, and flexibility trade-offs
- **Recommendation narrative** — Clear statement of when unitranche is preferable and the quantified cost of that preference

## Quality Checks

- Verify that blended coupon math reconciles — weighted-average of first-out and last-out rates must equal the stated borrower rate (within rounding)
- Confirm OID is amortized over expected life (typically 3–4 years for leveraged credits), not stated maturity [VERIFY expected-life assumption against deal-specific prepayment expectations]
- Ensure AAL analysis addresses all five core pillars: voting, buy-out, standstill, enforcement, and information rights
- Check that the comparable traditional structure uses contemporaneous market pricing, not stale benchmarks [VERIFY spreads against current LSTA or LCD data]
- Validate that stress scenarios use consistent EBITDA definitions (adjusted vs. unadjusted) across both structures
- Confirm all-in cost comparison accounts for any differences in amortization schedules, mandatory prepayment sweeps, and call protection economics
