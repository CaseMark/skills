---
name: analyzing-credit-agreement-terms
description: Evaluates credit agreement provisions with borrower flexibility, lender protections, and documentation comparison analysis. Use when reviewing credit agreements, analyzing doc terms, or comparing loan documentation.
tags:
  - analysis
  - credit-and-institutional-lending
  - credit
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Credit Agreement Terms

Evaluates credit agreement provisions focusing on borrower flexibility, lender protections, covenant structures, and documentation comparison across credit facilities. Applies to syndicated loans, direct lending facilities, leveraged credit agreements, and refinancing documentation.

## When To Use

- Reviewing a new credit agreement or amendment for key risk provisions
- Comparing a proposed credit agreement against a precedent deal or market-standard terms (e.g., LSTA model credit agreement)
- Assessing borrower-favorable vs. lender-favorable tilts in covenant packages
- Evaluating flex provisions, MFN protections, or incremental facility terms
- Analyzing documentation in the context of a leveraged buyout, refinancing, or add-on transaction

## Inputs To Gather

- **Credit agreement** (or draft term sheet / commitment letter) to be analyzed
- **Comparison document** (if applicable): precedent deal, model form, or competing proposal
- **Transaction context**: deal type (LBO, refi, dividend recap, add-on), borrower industry, sponsor involvement
- **Borrower financials**: LTM EBITDA, leverage levels, total debt quantum (needed for covenant and basket analysis)
- **Specific focus areas** (if any): e.g., "focus on J. Crew protections," "assess EBITDA addback caps," "compare incremental terms"

## Workflow

1. **Classify the facility structure**
   - Identify facility types (revolver, TL-A, TL-B, delayed draw, incremental)
   - Note maturity dates, amortization schedules, and springing maturity provisions
   - Flag any accordion / incremental capacity and the associated conditions (ratio-based vs. freebie baskets)

2. **Analyze financial covenants**
   - Identify covenant type: covenant-lite (no maintenance covenants on TL) vs. maintenance-covenanted
   - For maintenance covenants: extract leverage ratio, coverage ratio, or minimum liquidity tests; note testing frequency and step-downs
   - For incurrence-based covenants: identify the applicable ratio (typically Total Net Leverage or Secured Net Leverage) and where it gates (incremental debt, restricted payments, investments)
   - Evaluate EBITDA definition and addbacks — flag uncapped or loosely defined addbacks (synergies, cost savings, run-rate adjustments) and any sunset periods [VERIFY: check whether addback caps are percentage-based or fixed-dollar]

3. **Assess negative covenant baskets and builder provisions**
   - **Restricted Payments**: general basket size, builder basket mechanics (retained excess cash flow vs. cumulative credit), starter basket, available amount
   - **Permitted Investments**: size of general basket, carve-outs for unrestricted subsidiaries, and any "J. Crew" or "Chewy" trapdoor risk
   - **Permitted Debt**: incremental facilities (ratio-based capacity, freebie/fixed amount, MFN sunset, maturity/WAL protections, inside-maturity restrictions)
   - **Asset Sale / Reinvestment**: reinvestment period length, mandatory prepayment waterfall, step-downs tied to leverage
   - **Lien baskets**: general permitted liens capacity, ratio debt liens, incremental equivalent debt provisions

4. **Review borrower flexibility provisions**
   - Equity cure rights: frequency limits, dollar caps, deemed repayment mechanics
   - Classification and reclassification rights for covenant baskets
   - "Yank-a-bank" and replacement lender provisions
   - Ability to designate unrestricted subsidiaries and move assets outside the credit group
   - Amendment and waiver thresholds — identify which provisions require unanimity vs. required-lender consent vs. supermajority

5. **Evaluate lender protections**
   - Sacred rights requiring unanimous consent (maturity extensions, rate reductions, release of all/substantially all collateral or guarantors, pro rata sharing)
   - Anti-subordination protections (anti-layering, limitations on priming debt)
   - Collateral package scope: pledge of equity (65% foreign sub limitation), real property thresholds, excluded assets [VERIFY: jurisdiction-specific UCC perfection requirements]
   - Guarantor coverage test and guarantor release mechanics
   - Events of default: cross-default thresholds, change-of-control definitions (including portability provisions), material adverse effect definition

6. **Perform documentation comparison** (if benchmark provided)
   - Build a side-by-side comparison matrix of key terms
   - Highlight material deviations from the comparison document
   - Categorize deviations as borrower-favorable, lender-favorable, or neutral
   - Note market-trend context for any deviations (e.g., "post-2020 LBO documentation commonly includes this flexibility")

## Output

Produce a structured analysis report containing:

- **Executive Summary**: one-paragraph assessment of overall borrower-friendliness vs. lender-protectiveness, with the 3–5 most significant provisions flagged
- **Facility Overview Table**: facility types, commitments, maturities, pricing (if available), amortization
- **Covenant Analysis**: financial covenant terms (or covenant-lite confirmation), EBITDA definition review, key basket sizes with dollar amounts and ratio triggers
- **Flexibility vs. Protection Scorecard**: for each major category (RP, investments, debt incurrence, asset sales, amendments), rate as borrower-favorable / market / lender-favorable with brief justification
- **Comparison Matrix** (if applicable): side-by-side table with deviation flags
- **Risk Flags**: specific provisions that create outsized risk (e.g., uncapped addbacks, wide trapdoor provisions, weak sacred rights)
- **[VERIFY] Items**: list of provisions requiring confirmation of dollar thresholds, defined terms, or cross-references that could not be fully resolved from the provided document

## Quality Checks

- All dollar-amount baskets and ratio thresholds are extracted with precise figures — no paraphrasing of numbers
- EBITDA addback analysis includes each enumerated category, not just a summary statement
- Incremental facility analysis addresses both ratio-based and freebie components separately
- If comparing against a benchmark, every material deviation is captured — err on over-inclusion
- Cross-references within the agreement (e.g., "Permitted Investments" definition referencing "Available Amount") are traced to their source definitions
- Sacred rights / unanimous consent provisions are listed exhaustively
- Any provision that varies by jurisdiction or governing law is marked [VERIFY]
