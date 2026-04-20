---
name: managing-loan-documentation-review
language: en
description: Reviews loan agreements with covenant extraction, terms analysis, and compliance requirement identification. Use when reviewing loan documents, extracting covenants, or analyzing credit agreement terms.
tags:
  - management
  - commercial-banking
  - compliance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Commercial Banking
    - Trade Finance
    - Lending
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Loan Documentation Review

Reviews loan agreements with covenant extraction, terms analysis, and compliance requirement identification.

## When To Use

- Reviewing new credit agreements, term loans, or revolving credit facilities before execution
- Extracting financial and non-financial covenants from existing loan documentation for compliance tracking
- Analyzing amendment, waiver, or consent requests against original loan terms
- Onboarding syndicated or participated loans requiring multi-party documentation review
- Auditing loan files for regulatory examinations or internal credit review cycles
- Comparing terms across a portfolio of credit agreements for consistency or risk concentration

## Inputs To Gather

- **Loan agreement** (credit agreement, term loan agreement, or revolving credit facility) — full executed version including all schedules and exhibits
- **Amendment history** — all amendments, waivers, consents, and side letters modifying the original agreement
- **Borrower organizational documents** — entity structure, authorized signatories, guarantor relationships
- **Fee letter and pricing grid** — if separate from the main agreement
- **Compliance certificates** — recent borrower-submitted covenant compliance certificates, if reviewing ongoing compliance
- **Collateral documentation** — security agreements, UCC filings, pledge agreements, intercreditor agreements (if secured facility)
- **Loan type context** — whether the facility is bilateral, club deal, or broadly syndicated; whether governed by LMA or LSTA standards [VERIFY]

## Workflow

1. **Classify the facility**
   - Identify loan type: term loan (A/B), revolver, delayed-draw, swingline, letter of credit sub-facility, bridge loan
   - Note governing law, agent bank, and syndicate structure
   - Flag whether the agreement follows LSTA (US) or LMA (international) market conventions [VERIFY]

2. **Extract key commercial terms**
   - Principal amount, currency, maturity date, and any extension options
   - Interest rate mechanics: benchmark rate (SOFR, EURIBOR, etc.), spread, floor, fallback provisions [VERIFY current benchmark conventions]
   - Fees: commitment fee, utilization fee, LC fees, agent fees, prepayment premiums
   - Repayment schedule: amortization, bullet maturity, mandatory prepayment triggers (excess cash flow sweep, asset sale proceeds, insurance proceeds, debt issuance proceeds)

3. **Map the covenant package**
   - **Financial covenants**: leverage ratio (Total Debt / EBITDA), interest coverage ratio, fixed charge coverage, minimum liquidity, maximum capital expenditures — note testing frequency, cure rights, and equity cure mechanics
   - **Affirmative covenants**: financial reporting deadlines, compliance certificate delivery, insurance maintenance, property upkeep, further assurances
   - **Negative covenants**: restrictions on indebtedness, liens, investments, restricted payments (dividends/distributions), asset dispositions, affiliate transactions, fundamental changes (mergers/acquisitions), lines of business
   - **Reporting covenants**: annual audited financials, quarterly unaudited financials, compliance certificates, borrowing base certificates (for ABL facilities), budget/projections delivery

4. **Analyze key protective provisions**
   - Events of default: payment default, covenant default, cross-default/cross-acceleration thresholds, material adverse change, change of control, judgment thresholds, ERISA events
   - Grace and cure periods for each default category
   - Remedies upon default: acceleration, enforcement of security interests, cash dominion/springing lockbox triggers
   - Voting thresholds: required lender consent levels, amendments requiring unanimous consent vs. super-majority vs. simple majority

5. **Review conditions and mechanics**
   - Conditions precedent to closing and conditions to each borrowing/draw
   - Borrowing base mechanics and eligible collateral definitions (for asset-based facilities)
   - Assignment and participation provisions — minimum assignment amounts, consent requirements, eligible assignee restrictions
   - ERISA and sanctions representations, anti-money laundering provisions [VERIFY regulatory requirements by jurisdiction]

6. **Identify risks and exceptions**
   - Carve-outs and baskets within negative covenants — quantify permitted amounts (dollar baskets, ratio-based incurrence tests, general baskets)
   - "Builder basket" or retained excess cash flow capacity for restricted payments
   - Sunset or step-down provisions tied to ratings or leverage levels
   - Loose definitions that could permit aggressive borrower behavior (e.g., broad EBITDA add-backs, expansive "Permitted" definitions)

7. **Coordinate review outputs**
   - Assign covenant tracking responsibilities to credit monitoring team
   - Flag items requiring legal counsel review (unusual provisions, non-market terms)
   - Escalate documentation gaps or missing schedules/exhibits to relationship manager
   - Set calendar reminders for reporting deadlines, maturity, and renewal dates

## Output

Produce a **Loan Documentation Review Report** containing:

- **Facility summary table**: borrower, guarantors, agent, lenders, facility type, amount, maturity, pricing
- **Covenant matrix**: each covenant with its threshold, testing frequency, cure mechanics, and current compliance status (if certificates provided)
- **Negative covenant basket schedule**: each restricted action with its permitted baskets and carve-out amounts
- **Key dates calendar**: closing, first draw, reporting deadlines, amortization payments, maturity, extension option deadlines
- **Risk flags**: non-market terms, documentation gaps, unusually wide baskets, missing exhibits or schedules
- **Action items**: open items for legal, credit, operations, and relationship management with assigned owners and deadlines

## Quality Checks

- Verify all amendment history is incorporated — confirm the reviewed document reflects the "as-amended" state of the agreement
- Cross-check defined terms for internal consistency (e.g., "Consolidated EBITDA" definition against financial covenant calculations)
- Confirm interest rate fallback provisions address benchmark discontinuation adequately [VERIFY against current ARRC/SOFR transition guidance]
- Validate that financial covenant levels match the term sheet or commitment letter, if available
- Ensure collateral package descriptions align across the credit agreement, security agreement, and UCC filings
- Check that conditions precedent have been satisfied or appropriately waived — flag any outstanding CP items
- Mark jurisdiction-specific provisions with [VERIFY] — including governing law, regulatory compliance representations, and withholding tax gross-up obligations
