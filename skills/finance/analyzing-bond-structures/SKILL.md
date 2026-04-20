---
name: analyzing-bond-structures
language: en
description: Deconstructs bond indenture terms including covenants, call provisions, and credit support features. Use when analyzing bond structures, reviewing indentures, or evaluating bond terms.
tags:
  - analysis
  - fixed-income
  - credit
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
# Analyzing Bond Structures

Deconstructs bond indenture terms including covenants, call provisions, and credit support features for fixed income professionals, credit analysts, and bond traders.

## When To Use

- Reviewing a bond indenture or offering document to extract key structural terms
- Comparing covenant packages across issuers or tranches in a capital structure
- Evaluating call, put, and redemption provisions for yield and duration impact
- Assessing credit support mechanisms (guarantees, collateral, subordination)
- Preparing trade recommendations or credit opinions that depend on structural features
- Analyzing new issue terms against secondary-market comparables

## Inputs To Gather

- **Indenture or offering document** — the primary source; confirm whether it is a base indenture, supplemental indenture, or preliminary term sheet
- **Bond CUSIP / ISIN and issuer name** — for cross-referencing against rating agency reports and pricing services
- **Tranche details** — coupon, maturity, currency, par amount, seniority, and secured/unsecured status
- **Rating agency reports** — Moody's, S&P, Fitch assessments on the issuer or specific tranche
- **Comparable bond terms** — recent deals from the same issuer, sector, or rating tier
- **Capital structure summary** — outstanding debt by seniority, maturity schedule, and lien priority [VERIFY against latest 10-K/Q or trustee report]

## Workflow

1. **Classify the bond type and structure**
   - Fixed-rate, floating-rate, zero-coupon, step-up, PIK, convertible, or hybrid
   - Secured vs. unsecured; senior vs. subordinated; investment-grade vs. high-yield
   - Note any special features: asset-backed, project-finance, green/sustainability-linked KPIs

2. **Extract and map covenant terms**
   - **Affirmative covenants** — financial reporting obligations, maintenance of assets, insurance requirements
   - **Negative/restrictive covenants** — limitations on indebtedness, restricted payments (dividends, buybacks), asset sales, sale-leaseback, merger/consolidation, liens, transactions with affiliates
   - **Incurrence vs. maintenance tests** — identify whether financial ratios are tested only upon a triggering event (incurrence) or on an ongoing periodic basis (maintenance) [VERIFY: high-yield indentures typically use incurrence-only; IG may have none]
   - **Basket and carve-out inventory** — catalog permitted debt baskets (general basket, ratio basket, credit facility basket), permitted lien baskets, and restricted payment capacity with dollar caps and builder-basket formulas

3. **Analyze call, put, and redemption features**
   - **Optional redemption schedule** — extract make-whole spread, par call date, and declining premium schedule
   - **Equity clawback** — percentage callable, time window, and minimum outstanding requirement post-clawback
   - **Change-of-control put** — trigger events (acquisition, going-private), put price (typically 101%), and rating downgrade conditions
   - **Special/mandatory redemption** — asset sale proceeds sweep, excess cash flow sweep percentages and step-downs, tax redemption
   - Calculate yield-to-call, yield-to-worst, and option-adjusted spread impact of each provision

4. **Evaluate credit support and structural protections**
   - **Collateral package** — asset types pledged, lien priority, release mechanics, and collateral coverage ratios
   - **Guarantees** — upstream, downstream, or cross-guarantees; guarantor coverage test (percentage of consolidated revenue, assets, or EBITDA) [VERIFY guarantor coverage against offering document]
   - **Subordination mechanics** — structural subordination (operating-company debt below holdco) vs. contractual subordination; payment waterfall in default
   - **Credit enhancements** — reserve funds, surety bonds, letters of credit, overcollateralization levels (for securitized structures)

5. **Benchmark against comparables**
   - Score covenant quality using a standardized framework (e.g., Moody's Covenant Quality Index methodology or internal scoring rubric)
   - Flag materially weaker or stronger terms relative to sector norms
   - Note any J-Crew or Chewy-style trapdoor provisions, unrestricted subsidiary leakage paths, or EBITDA add-back inflation risks

## Output

Produce a structured **Bond Structure Analysis Report** containing:

- **Summary table** — issuer, CUSIP, coupon, maturity, rating, seniority, call schedule, covenant type (incurrence/maintenance)
- **Covenant map** — organized by category with dollar thresholds, ratio tests, and notable carve-outs
- **Redemption profile** — timeline graphic or table showing call prices by date, make-whole terms, and mandatory redemption triggers
- **Credit support summary** — collateral description, guarantor list, subordination diagram
- **Comparative scorecard** — side-by-side view against 2-3 comparable bonds with a qualitative tighter/in-line/looser assessment per covenant category
- **Risk flags** — items requiring further diligence or legal review, each tagged with [VERIFY] where jurisdiction or document-specific confirmation is needed

## Quality Checks

- Confirm all covenant thresholds and baskets are sourced directly from the indenture text, not summarized from third-party commentary
- Verify that the call schedule matches the pricing supplement or final term sheet, not just the preliminary offering memo
- Cross-check guarantor and collateral descriptions against the security agreement and intercreditor agreement if available
- Ensure yield calculations (YTC, YTW, OAS) use the correct day-count convention and settlement date [VERIFY: 30/360 for corporates, ACT/ACT for Treasuries]
- Validate that any credit rating referenced is current; note rating watch or outlook if applicable
- Flag any defined terms in the indenture that use non-standard definitions (e.g., "Consolidated Net Income" with aggressive add-backs) that could materially affect covenant headroom calculations
