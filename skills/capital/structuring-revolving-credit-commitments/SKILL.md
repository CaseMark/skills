---
name: structuring-revolving-credit-commitments
description: Designs revolver structures with commitment sizing, utilization analysis, and availability management for credit fund portfolios. Use when structuring revolvers, sizing commitments, or managing availability exposure.
tags:
  - credit-and-institutional-lending
  - portfolio
  - credit
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Revolving Credit Commitments

## When To Use

- Sizing a new revolving credit commitment for a direct lending or leveraged finance deal
- Evaluating whether to include a revolver tranche alongside a term loan in a unitranche or multi-tranche facility
- Analyzing portfolio-level revolver exposure, unfunded commitments, and liquidity reserves
- Stress-testing utilization assumptions for existing revolver book across borrower segments
- Structuring delayed-draw or accordion features that function like revolving availability

## Inputs To Gather

- **Borrower financials**: TTM EBITDA, revenue, cash flow projections, working capital cycle, and seasonal patterns
- **Credit agreement terms**: total facility size, term loan commitments, existing revolver capacity, maturity dates
- **Proposed revolver parameters**: commitment amount, tenor, pricing (spread, commitment fee, utilization fee tiers), borrowing base mechanics if applicable
- **Availability controls**: financial covenant levels (leverage, fixed charge coverage), borrowing base formula components (eligible receivables, inventory advance rates), springing covenant triggers
- **Fund-level data**: total unfunded commitments across portfolio, liquidity facility size, NAV, leverage ratio, LP capital call mechanics
- **Historical utilization**: borrower-level draw history, peak/average utilization rates, seasonal draw patterns, time-to-repay metrics

## Workflow

1. **Profile borrower liquidity need** — Analyze working capital cycle, capex timing, and seasonal cash flow swings to determine the genuine revolver requirement. Distinguish between revolvers used as true working capital lines vs. those functioning as quasi-term facilities (high sustained utilization).

2. **Size the commitment** — Set revolver commitment as a function of borrower need, typically 10–20% of total facility for sponsor-backed deals or sized to 1–2x peak working capital deficit. Validate that the commitment amount does not create outsized unfunded exposure relative to fund liquidity. [VERIFY] Sizing conventions vary by market segment (broadly syndicated vs. direct lending vs. ABL).

3. **Design availability mechanics** — Define borrowing base formula (if asset-based) or covenant-driven availability. Specify:
   - Eligible collateral categories and advance rates
   - Financial covenant triggers that restrict availability (springing leverage tests, minimum liquidity)
   - Borrowing conditions and certification requirements for each draw

4. **Structure pricing and fees** — Set the economics to compensate for contingent funding risk:
   - Commitment fee on undrawn amounts (typically 25–50 bps for leveraged credit) [VERIFY]
   - Utilization fee tiers (e.g., additional 25 bps when >50% drawn)
   - Drawn spread relative to term loan spread (usually at parity or slight premium)
   - Ticking fee or delayed-draw premium if applicable

5. **Model utilization scenarios** — Build base, stress, and peak utilization cases:
   - Base case: average historical utilization (often 20–40% for middle-market revolvers)
   - Stress case: simultaneous peak draws across correlated borrowers in downturn
   - Tail case: 100% draw scenario for fund liquidity planning
   - Calculate weighted-average return on commitment including fee income vs. funded yield drag

6. **Assess fund-level exposure** — Aggregate unfunded revolver commitments across the portfolio. Test against:
   - Fund liquidity reserves and subscription credit line availability
   - LP capital call capacity and timing constraints
   - Regulatory or fund documentation limits on unfunded commitments as a percentage of NAV
   - Concentration of unfunded exposure by sector, borrower, or vintage

7. **Document the structure** — Produce a revolver structuring memo covering commitment rationale, sizing methodology, availability mechanics, pricing, utilization modeling, and portfolio-level impact.

## Output

- **Revolver Structuring Memo** containing:
  - Borrower liquidity profile and revolver need justification
  - Commitment size recommendation with supporting analysis
  - Availability framework: borrowing base or covenant-gated structure
  - Fee and pricing schedule with market comparables
  - Utilization scenario analysis (base / stress / tail) with expected return impact
  - Fund-level unfunded commitment summary showing pre- and post-deal exposure
  - Risk flags: concentration, liquidity mismatch, correlated draw risk
  - Recommendations on structural protections (notice periods, minimum draw amounts, clean-down provisions)

## Quality Checks

- Commitment size is supported by borrower cash flow analysis, not just rule-of-thumb percentages
- Availability mechanics include at least one protective trigger (financial covenant, borrowing base, or springing test)
- Utilization modeling includes a stress scenario with simultaneous multi-borrower draws
- Fund-level unfunded commitment total is tested against actual liquidity sources with a coverage buffer
- Pricing is benchmarked against comparable recent transactions in the same market segment [VERIFY]
- Clean-down requirements or annual utilization limits are considered for revolvers at risk of becoming quasi-term facilities
- All jurisdiction-specific regulatory constraints on unfunded commitments are flagged with [VERIFY] markers
