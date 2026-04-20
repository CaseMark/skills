---
name: modeling-strip-and-tail-transactions
language: en
description: Builds strip and tail-end fund models with remaining portfolio analysis, unfunded obligation treatment, and duration-adjusted pricing. Use when modeling strip deals, evaluating tail-end portfolios, or analyzing remaining value.
tags:
  - modeling
  - secondaries-and-gp-led
  - treatment
  - portfolio
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
# Modeling Strip And Tail Transactions

Builds strip and tail-end fund models with remaining portfolio analysis, unfunded obligation treatment, and duration-adjusted pricing.

## When To Use

- Pricing a strip acquisition of select assets from a mature fund's remaining portfolio
- Modeling tail-end fund purchases where the GP is winding down and residual NAV needs valuation
- Evaluating GP-led continuation vehicle economics for remaining portfolio companies
- Assessing unfunded commitment obligations attached to late-life fund positions
- Comparing strip deal pricing against full LP interest secondary bids

## Inputs To Gather

- **Portfolio company data**: Latest GP-reported NAV per company, holding period to date, sector, and most recent valuation methodology (mark-to-market, comparable, DCF)
- **Fund-level data**: Vintage year, fund size, total called capital, remaining unfunded commitments, current DPI and RVPI, GP fee and carry terms through end-of-life
- **Strip selection**: Which portfolio companies are included in the strip vs. excluded; rationale for cherry-picking or adverse selection risk
- **Cash flow history**: Historical distribution pace for the fund (quarterly/annual) and any recent realizations
- **GP timeline guidance**: Expected hold period for remaining assets, planned exit routes, and any extension vote history
- **Unfunded treatment**: Whether unfunded commitments transfer with the interest, are capped, or are excluded from the strip [VERIFY]
- **Fee structure on residual**: Management fee basis (committed vs. invested capital), carry waterfall status (above/below preferred return hurdle)

## Workflow

1. **Map the remaining portfolio** — List each company with current NAV, entry date, ownership percentage, and GP's stated exit timeline. Flag any assets marked at cost for >3 years or showing write-down trends.

2. **Segment strip vs. tail** — For strip deals, isolate the selected assets and model them independently. For tail-end purchases, treat the entire residual portfolio as a unit. Identify concentration risk (single asset >30% of remaining NAV).

3. **Build company-level exit assumptions**:
   - Assign base-case exit multiples using sector comparables and GP track record on similar vintage assets
   - Model exit timing: near-term (0–12 months), mid-term (12–36 months), extended (36+ months)
   - Apply probability weighting to exit scenarios (e.g., 60% base / 25% downside / 15% upside)

4. **Model unfunded commitment exposure**:
   - Calculate remaining callable capital and likelihood of future calls based on fund age and GP guidance
   - For strip deals, determine whether unfunded obligations are proportionally assumed or excluded [VERIFY]
   - If unfunded transfers, model the incremental capital outlay and its impact on net return

5. **Construct cash flow waterfall**:
   - Project quarterly distributions based on exit timing assumptions
   - Layer in ongoing management fees (typically declining in extension periods — confirm fee step-down schedule) [VERIFY]
   - Model carry allocation: determine whether the GP is above or below the preferred return hurdle and how remaining exits affect carry crystallization

6. **Calculate duration-adjusted pricing**:
   - Discount projected net cash flows at the buyer's target IRR (typically 15–25% for tail/strip deals)
   - Compute implied price as % of NAV — strip deals often trade at wider discounts (10–30% discount to NAV) than clean secondary trades due to adverse selection and illiquidity
   - Run duration sensitivity: show how price changes if average hold extends by 6, 12, or 18 months

7. **Sensitivity and scenario analysis**:
   - Exit multiple stress: ±20% on base-case multiples
   - Timing stress: 12-month delay across all exits
   - Concentration stress: zero-recovery on largest single holding
   - Fee drag sensitivity: management fee rate through full extension vs. early wind-down

## Output

- **Portfolio summary table**: Company, NAV, % of total, sector, hold period, assigned exit multiple, projected exit date, probability-weighted proceeds
- **Cash flow schedule**: Quarterly projected gross distributions, fee deductions, carry, and net cash flows to buyer
- **Pricing matrix**: Implied purchase price at target IRRs of 15%, 18%, 20%, 25% — expressed as both dollar amount and % of current NAV
- **Unfunded exposure summary**: Total callable amount, expected call schedule, net capital outlay timeline
- **Scenario dashboard**: Base / downside / upside IRR and MOIC for the strip or tail portfolio, with tornado chart showing key sensitivities
- **Risk flags**: Concentration, J-curve re-entry risk on unfunded, GP alignment concerns, fee drag in extension periods

## Quality Checks

- Confirm NAV figures tie to the most recent audited or quarterly GP report — do not use stale marks
- Verify that strip asset selection does not double-count assets also valued in a parallel LP interest bid
- Ensure unfunded commitment treatment matches the actual transfer agreement terms, not assumptions [VERIFY]
- Validate that fee calculations reflect the fund's LPA terms during extension periods, including any fee reductions [VERIFY]
- Cross-check implied pricing against recent comparable strip/tail transactions in the market (Greenhill, Evercore, Jefferies secondary market data)
- Confirm discount rate assumptions align with buyer's stated return targets and current secondary market clearing rates
- Flag any asset where GP valuation methodology is opaque or where the last third-party valuation is >18 months old
