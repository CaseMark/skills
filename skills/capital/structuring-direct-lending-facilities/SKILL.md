---
name: structuring-direct-lending-facilities
language: en
description: Designs direct lending structures with pricing, covenant packages, and documentation tailored for middle-market borrowers. Use when structuring direct loans, designing covenant packages, or analyzing direct lending terms.
tags:
  - credit-and-institutional-lending
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
# Structuring Direct Lending Facilities

Designs direct lending structures with pricing, covenant packages, and documentation tailored for middle-market borrowers, typically in the $25M–$500M range where borrowers lack broad syndicated market access.

## When To Use

- Structuring a unitranche, first lien/second lien, or delayed-draw term loan for a middle-market sponsor or corporate borrower
- Designing a financial and operational covenant package for a direct lending facility
- Evaluating pricing (spread, OID, LIBOR/SOFR floor) relative to borrower credit profile and market conditions
- Comparing direct lending terms against broadly syndicated alternatives
- Reviewing or negotiating credit agreement provisions specific to direct lending (e.g., voting thresholds, amendment mechanics with a single or small lender group)

## Inputs To Gather

- **Borrower profile**: Industry, revenue, EBITDA (and adjustments), ownership (sponsor vs. non-sponsor), capital structure history
- **Transaction context**: LBO, refinancing, dividend recap, add-on acquisition, growth capital
- **Leverage parameters**: Target total leverage, senior secured leverage, and any mezzanine or subordinated debt layers
- **EBITDA adjustments**: Proposed add-backs (cost savings, synergies, run-rate) with supporting detail — flag aggressive adjustments
- **Requested facility features**: Revolver size, term loan amount, delayed-draw needs, accordion capacity, incremental facility provisions
- **Sponsor or borrower preferences**: Covenant-lite expectations, call protection sensitivity, flexibility for future M&A or distributions
- **Market benchmarks**: Comparable recent direct lending transactions in the same sector and leverage band [VERIFY against current market data]

## Workflow

1. **Credit assessment and sizing**
   - Analyze borrower EBITDA quality: recurring revenue mix, customer concentration, cyclicality, margin stability
   - Stress-test cash flows under downside scenarios (revenue decline of 10–25%, margin compression) to determine sustainable debt service capacity
   - Size the facility based on target leverage (e.g., 4.0–6.0x total for sponsor deals) and minimum DSCR of 1.2–1.5x under stress
   - Determine appropriate structure: unitranche (with or without first-out/last-out split), senior/sub split, or pure first lien

2. **Pricing and economics**
   - Set base rate spread relative to credit quality (typically SOFR + 500–700 bps for middle-market direct lending) [VERIFY against current market spreads]
   - Establish SOFR floor (commonly 75–100 bps) and OID (typically 97–99)
   - Define call protection schedule (e.g., 102/101/par or make-whole through Year 1, then 101/par)
   - Calculate undrawn fees on revolver and delayed-draw commitments (typically 50 bps)
   - Model all-in yield to lender including fees, OID, and floor value

3. **Covenant package design**
   - **Financial covenants**: Select maintenance vs. incurrence-based covenants
     - Maintenance (tested quarterly): Total Leverage Ratio, Fixed Charge Coverage Ratio, Minimum EBITDA
     - Set initial cushion of 20–30% above projected performance for leverage covenants
     - Define EBITDA calculation with permitted add-backs and a cap on pro forma / run-rate adjustments (commonly 15–25% of EBITDA)
   - **Negative covenants**: Draft restrictions on indebtedness, liens, restricted payments, investments, asset sales, affiliate transactions
     - Size baskets and carve-outs proportional to borrower EBITDA (e.g., general investment basket of $X or 10–15% of EBITDA)
     - Include builder basket mechanics tied to cumulative excess cash flow
   - **Affirmative covenants**: Monthly/quarterly financials delivery, annual audited statements, compliance certificates, budget delivery, insurance maintenance
   - **Reporting requirements**: Direct lenders typically require more frequent and granular reporting than syndicated deals — specify monthly financial packages with KPI dashboards

4. **Documentation and structural provisions**
   - Draft or review credit agreement based on borrower counsel's form or lender's preferred form (not LSTA standard for most direct deals) [VERIFY whether parties are using LSTA-based or custom documentation]
   - Key provisions to negotiate:
     - **Amendment and waiver thresholds**: In a single-lender or club deal, voting is simpler but consent rights must be clearly allocated
     - **Equity cure rights**: Number of cures permitted (typically 2–3 per year, 5 lifetime), cure amount mechanics (contributed equity vs. subordinated debt)
     - **Incremental facility terms**: MFN pricing protection (typically 50–75 bps sunset after 12–18 months), leverage incurrence test for incremental capacity
     - **Restricted payment conditions**: Leverage-based stepdowns (e.g., distributions permitted below 3.5x net leverage)
     - **Change of control definition**: Ensure sponsor transfer flexibility while protecting lender against non-approved ownership changes

5. **Term sheet and final deliverable assembly**
   - Produce a summary term sheet covering all economic and structural terms
   - Include a covenant compliance model showing projected performance against covenant levels for the first 3–5 years
   - Prepare a comparison matrix if evaluating multiple structure alternatives (unitranche vs. first/second lien split)
   - Flag any open negotiation points or borrower-requested flexibilities requiring further diligence

## Output

A structured direct lending facility report containing:

- **Executive summary**: Transaction overview, recommended structure, and key terms
- **Facility structure table**: Tranche details (type, size, maturity, pricing, amortization)
- **Covenant summary**: Financial covenant levels with cushion analysis, negative covenant baskets with dollar/percentage thresholds
- **Pricing benchmarking**: Comparison to 3–5 comparable recent direct lending transactions
- **Covenant compliance model**: Projected base case and downside covenant testing over the facility life
- **Open items list**: Unresolved terms, requested flexibilities, and items requiring further credit diligence

## Quality Checks

- Verify that leverage and coverage ratios are calculated consistently (same EBITDA definition) across the sizing model, covenant levels, and compliance projections
- Confirm call protection, prepayment mechanics, and excess cash flow sweep percentages are internally consistent
- Ensure covenant baskets (RP, investment, debt) do not inadvertently create leakage paths that undermine credit protections
- Cross-check EBITDA add-back caps and pro forma adjustment limits against the credit agreement definition section
- Validate that amendment/waiver mechanics reflect the actual lender composition (single lender vs. club)
- Mark any jurisdiction-dependent provisions (e.g., UCC perfection requirements, guarantor limitations for regulated entities) with [VERIFY]
- Stress-test the covenant compliance model: confirm the borrower trips covenants before liquidity is exhausted in the downside case (covenants should function as an early warning)
