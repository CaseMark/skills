---
name: analyzing-high-yield-credit
language: en
description: Structures high-yield credit analysis with recovery rate estimation and distressed debt evaluation. Use when analyzing high-yield bonds, estimating recovery rates, or evaluating distressed credits.
tags:
  - analysis
  - fixed-income
  - credit
  - valuation
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
# Analyzing High Yield Credit

## When To Use

- Evaluating a new-issue high-yield bond for purchase or pass
- Reassessing an existing holding after a credit event, earnings miss, or covenant breach
- Estimating recovery rates for distressed or defaulted debt
- Comparing relative value across high-yield issuers within the same sector
- Building a credit opinion to support a trade recommendation (long, short, or hedged)

## Inputs To Gather

- **Issuer financials**: Last 3 years of income statements, balance sheets, and cash flow statements; most recent interim period
- **Capital structure**: Full debt stack with seniority, maturity dates, coupon rates, call schedules, and outstanding amounts
- **Bond terms**: Indenture highlights — covenants (incurrence vs. maintenance), restricted payments baskets, change-of-control provisions, permitted liens
- **Industry context**: Sector fundamentals, competitive positioning, cyclicality, and comparable issuer spreads
- **Market data**: Current bid/ask, OAS, yield-to-worst, CDS spreads (if available), and recent trading volume
- **Rating agency reports**: Current ratings and outlooks from Moody's/S&P/Fitch; any recent rating actions [VERIFY availability per issuer]
- **Event catalysts**: Pending M&A, litigation, regulatory changes, refinancing windows, or maturity walls

## Workflow

1. **Map the capital structure**
   - Rank all debt obligations by seniority: secured → senior unsecured → subordinated → mezzanine → preferred equity
   - Note any structural subordination from operating-company vs. holding-company debt
   - Calculate total leverage, secured leverage, and net leverage ratios
   - Identify nearest maturity and any springing maturities or cross-default triggers

2. **Assess credit fundamentals**
   - Compute key ratios: Debt/EBITDA, Interest Coverage (EBITDA/Interest), FCF/Debt, Fixed Charge Coverage
   - Normalize EBITDA for one-time items; flag add-backs exceeding 15% of reported EBITDA as aggressive [VERIFY add-back legitimacy]
   - Evaluate revenue concentration (customer, geography, product) and margin trajectory
   - Stress-test cash flows under a downside scenario (e.g., 20% EBITDA decline) and check covenant headroom

3. **Analyze covenants and structural protections**
   - Classify covenant package strength: tight (maintenance-based with restricted baskets) vs. covenant-lite (incurrence-only)
   - Identify leakage risk: permitted investment baskets, unrestricted subsidiary designations, collateral release provisions
   - Flag any J. Crew / Chewy-style trapdoor provisions that allow asset stripping [VERIFY against actual indenture language]

4. **Estimate recovery in a default scenario**
   - Select recovery methodology: enterprise-value waterfall approach for going-concern or liquidation analysis for asset-heavy issuers
   - For enterprise-value waterfall: apply a distressed EBITDA multiple (typically 4x-6x for HY, sector-dependent) to estimate firm value, then distribute per the priority-of-claims stack [VERIFY appropriate multiples for the sector]
   - For liquidation: haircut assets by category — cash (100%), receivables (70-85%), inventory (50-70%), PP&E (30-60%), intangibles (0-20%) [VERIFY against industry-specific benchmarks]
   - Compute recovery rate per tranche and implied loss-given-default (LGD)

5. **Perform relative value assessment**
   - Compare OAS and yield-to-worst against same-rating/same-sector peers
   - Assess spread compensation relative to estimated default probability and recovery rate
   - Calculate breakeven spread widening: how much can spreads widen before total return turns negative over the holding period?
   - Consider optionality: if bond is callable, compute yield-to-call vs. yield-to-worst and assess likelihood of early redemption

6. **Form credit opinion and recommendation**
   - Summarize the bull case, bear case, and base case with probability weightings
   - State a clear directional view: overweight / market-weight / underweight, or buy / hold / sell
   - Identify key monitoring triggers that would change the recommendation (e.g., leverage above Xх, loss of a key customer, downgrade watch)

## Output

The analysis report should include:

- **Executive summary**: One-paragraph credit opinion with recommendation and target spread/price
- **Capital structure table**: All tranches with seniority, size, coupon, maturity, current price, YTW, and OAS
- **Credit metrics dashboard**: Leverage, coverage, and liquidity ratios with trend (improving/stable/deteriorating)
- **Recovery analysis**: Waterfall table showing estimated recovery per tranche under base and stress scenarios
- **Relative value snapshot**: Spread comparison vs. 3-5 closest comps with brief rationale for any premium or discount
- **Risk factors**: Ranked list of material risks with estimated probability and impact
- **Monitoring triggers**: Specific thresholds or events that warrant immediate re-evaluation

## Quality Checks

- All leverage and coverage ratios tie back to sourced financials — no orphan numbers
- Recovery waterfall sums correctly and respects strict priority (no value leakage past senior claims unless surplus exists)
- Covenant analysis references actual indenture terms, not generic descriptions
- Spread and yield data are date-stamped; stale pricing (>2 business days) is flagged
- Downside stress scenario is plausible and internally consistent (e.g., EBITDA decline flows through to FCF and coverage ratios)
- Any assumed EBITDA multiples, haircut rates, or default probabilities are labeled with source or marked [VERIFY]
- Recommendation is consistent with the analysis — no disconnect between bearish fundamentals and a buy recommendation without explicit justification
