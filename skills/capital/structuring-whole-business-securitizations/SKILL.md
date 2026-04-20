---
name: structuring-whole-business-securitizations
language: en
description: Designs whole business securitization with IP collateral, franchise cash flows, and operating covenant structures. Use when structuring WBS transactions, analyzing franchise securitizations, or evaluating non-traditional collateral.
tags:
  - structured-finance
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Whole Business Securitizations

Designs whole business securitization (WBS) structures where the collateral pool is an entire operating business—its IP, franchise agreements, brand value, and associated cash flows—rather than discrete financial assets.

## When To Use

- Structuring a new WBS transaction for franchise systems, restaurant chains, or brand-licensing platforms
- Evaluating whether an operating business's cash flows qualify as securitizable assets
- Analyzing existing WBS deal structures for refinancing, upsizing, or covenant compliance
- Comparing WBS economics against traditional corporate debt or asset-backed alternatives
- Assessing IP and franchise agreement enforceability as collateral support

## Inputs To Gather

- **Business description**: Industry vertical, number of locations/franchisees, ownership mix (company-owned vs. franchised), geographic footprint
- **Revenue data**: Trailing 3–5 years of system-wide sales, royalty streams, advertising fund contributions, company-owned unit EBITDA
- **IP portfolio**: Trademarks, trade names, patents, proprietary recipes/processes, domain names, and registration status [VERIFY jurisdiction-specific IP perfection requirements]
- **Franchise agreements**: Key terms—royalty rate, term/renewal, territorial exclusivity, transfer restrictions, default/cure provisions
- **Existing debt stack**: Outstanding secured/unsecured obligations, lien positions, intercreditor arrangements
- **Management projections**: Forward revenue and EBITDA forecasts, unit growth pipeline, capex budget
- **Target deal parameters**: Desired advance rate, tranche structure, tenor, fixed vs. floating rate preference, call protection

## Workflow

1. **Cash-flow mapping**
   - Disaggregate revenue by source: franchise royalties, franchise fees (initial + renewal), advertising fund fees, company-owned unit revenues, licensing/sublicensing income
   - Identify contractual vs. discretionary cash-flow components; only contractual streams typically qualify for investment-grade tranches
   - Build a base-case debt-service coverage ratio (DSCR) model using net operating cash flow after management fees and required capex reserves

2. **Collateral analysis**
   - Catalogue all IP assets and confirm perfection pathway (UCC filings, USPTO/copyright office recordings) [VERIFY state-specific UCC filing requirements for IP]
   - Evaluate franchise agreement assignability—confirm whether securitization-vehicle assignment triggers consent requirements or change-of-control provisions
   - Assess concentration risk: top-10 franchisee revenue share, geographic concentration, single-unit vs. multi-unit operator mix
   - Determine whether a "manager" structure or "special-purpose operating entity" is needed to maintain business operations post-hypothetical bankruptcy

3. **SPV and structural design**
   - Design the special-purpose entity (SPE) stack: typically a holding company that owns the IP and franchise agreements, with a co-issuer structure for notes
   - Define bankruptcy-remoteness features: independent directors, separateness covenants, limited-purpose provisions, non-petition agreements
   - Set the cash-flow waterfall: senior note interest → senior note scheduled principal → reserve account replenishment → subordinate note interest/principal → management fee/equity distributions
   - Size reserve accounts: liquidity reserve (typically 1–3 months debt service), cash trap triggers, rapid amortization triggers

4. **Covenant framework**
   - Draft operating covenants: minimum DSCR (typically 1.20x–1.75x for senior notes), minimum unit count, brand-standard compliance, franchisee default rate caps
   - Define cash-trap triggers (e.g., DSCR < 1.50x) and rapid-amortization events (e.g., DSCR < 1.20x or manager termination event)
   - Specify permitted activities and negative covenants for the SPE: no additional debt, no asset sales outside ordinary course, no merger/consolidation
   - Address manager replacement mechanics and back-up manager identification [VERIFY rating agency expectations for back-up manager requirements]

5. **Rating and execution considerations**
   - Prepare rating-agency presentation addressing business stability, cash-flow volatility, management quality, and franchise system health metrics
   - Model stress scenarios: same-store sales decline (−10%, −20%), franchisee attrition (5%, 10%), commodity cost spikes, recession-case DSCR
   - Identify anticipated rating-agency concerns: key-man risk, brand concentration, recharacterization risk, true-sale opinion scope
   - Outline legal opinion requirements: true-sale/contribution, non-consolidation, security interest perfection, IP ownership [VERIFY local counsel opinion requirements for multi-state franchise systems]

## Output

- **WBS Structure Memo** containing:
  - Executive summary with recommended tranche sizes, advance rate, and indicative pricing
  - Cash-flow waterfall diagram with trigger levels
  - Collateral description and perfection summary
  - Covenant term sheet (DSCR triggers, cash trap, rapid amortization, events of default)
  - Stress-test results table (base, downside, severe downside DSCR)
  - Key risk factors and mitigants
  - Outstanding diligence items and [VERIFY] flags

## Quality Checks

- Confirm DSCR calculations use net cash flow after all required reserves, fees, and capex—not gross revenue
- Verify that IP perfection steps cover all relevant jurisdictions and filing offices
- Ensure franchise agreement analysis addresses assignability, consent requirements, and change-of-control triggers
- Cross-check that covenant trigger levels are internally consistent (cash trap fires before rapid amortization, which fires before event of default)
- Validate that SPE structure satisfies rating-agency bankruptcy-remoteness criteria (independent director, separateness covenants, non-petition language)
- Flag any single-franchisee concentration exceeding 10% of system revenue as a risk factor
- Mark all jurisdiction-dependent or regulation-dependent conclusions with [VERIFY]
