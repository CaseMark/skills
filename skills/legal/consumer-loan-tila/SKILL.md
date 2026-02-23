---
name: consumer-loan-tila
description: Drafts TILA-compliant consumer loan agreements with Regulation Z federal disclosure boxes, accurate APR/finance charge calculations, and enforceable terms. Covers secured and unsecured consumer credit transactions including payment schedules, default provisions, collateral descriptions, and required regulatory notices. Use when drafting consumer loan agreements, TILA disclosure documents, promissory notes for consumer credit, or Reg Z compliant financing contracts.
tags:
  - agreement
  - drafting
  - regulatory
  - transactional
---

# Consumer Loan Agreement (TILA Compliant)

Drafts a comprehensive consumer loan agreement satisfying all Truth in Lending Act (15 U.S.C. § 1601 et seq.) and Regulation Z (12 CFR Part 1026) disclosure requirements.

## Prerequisites

1. **Borrower information** — full legal names, addresses, co-borrowers/guarantors
2. **Lender information** — legal entity name, DBA designations, physical address, regulatory filings
3. **Loan terms** — principal amount, interest rate, term, payment frequency
4. **Fee schedule** — origination fees, points, document prep fees, service charges
5. **Collateral description** (if secured) — make/model/VIN for personal property; legal description for real property
6. **Governing contract/institutional requirements** — notice clauses, state-specific restrictions
7. **Ancillary products** — credit insurance or debt protection elections, if any

## Output Structure

### Document Architecture

| Section | Purpose |
|---|---|
| Federal Truth in Lending Disclosure Box | Mandatory Reg Z disclosures — **must appear first, before any other terms** |
| Loan Terms & Conditions | Substantive contractual provisions |
| Default, Acceleration & Remedies | Events of default, cure rights, lender remedies |
| Insurance & Payment Application | Collateral insurance, force-placed coverage, payment waterfall |
| Special Notices | SCRA notice, FTC co-signer notice, state-specific notices |
| Execution & Signatures | Acknowledgments, signature blocks, copy delivery |

### TILA Disclosure Box Requirements

Heading: **"FEDERAL TRUTH IN LENDING DISCLOSURES"** — bold, ≥2pt larger than body text, visually segregated (borders/shading/white space), on page 1 before all other terms.

Required disclosures with **exact Reg Z labels**:

| Label (verbatim) | Content |
|---|---|
| "Annual Percentage Rate (The cost of your credit as a yearly rate)" | Calculated via actuarial/US Rule method; ≥2 decimal places; accurate within ⅛ of 1% [VERIFY tolerance for transaction type] |
| "Amount Financed (The amount of credit provided to you or on your behalf)" | Net credit extended minus prepaid finance charges; include financed ancillary products |
| "Finance Charge (The dollar amount the credit will cost you)" | Total dollar cost: all interest + origination fees + points + service/doc prep charges; itemize major components |
| "Total of Payments (The amount you will have paid after you have made all payments as scheduled)" | Amount Financed + Finance Charge |
| "Payment Schedule (Your payment schedule will be)" | Uniform payments: number × amount × frequency, first payment date. Irregular/balloon: full table with each amount and due date |

**Cross-verify**: All arithmetic must be internally consistent across disclosure items.

### Substantive Loan Terms

Draft the following provisions:

- [ ] **Parties and promise** — full legal names, fundamental obligation statement
- [ ] **Loan purpose** — "personal, family, or household purposes" or specific purpose if state-required
- [ ] **Prepayment rights** — clearly state if penalty-free; if penalty applies: conditions, duration, calculation method, maximum amount, state-law compliance check
- [ ] **Late charges** — amount/percentage, grace period (typically 10–15 days), single-assessment rule, no compounding; must comply with state caps
- [ ] **Collateral/security interest** (if secured):
  - Personal property: make, model, year, serial/VIN, location
  - Real property: full legal description + street address
  - Borrower covenants: maintain condition, keep free of liens, maintain insurance, no transfer without consent
- [ ] **Unsecured statement** (if unsecured): affirmative disclosure that no collateral secures the obligation

### Default & Remedies

Events of default:

1. Failure to make timely payment
2. Failure to maintain required insurance on collateral
3. Bankruptcy or insolvency
4. Material misrepresentation in application
5. Death of borrower (if loan does not survive)
6. Impairment of collateral or security interest

Include:
- State-required notice of default and right to cure (specify period and delivery method)
- Acceleration clause (subject to applicable notice requirements)
- Collateral remedies: repossession (judicial/self-help per state law), commercially reasonable sale, proceeds waterfall (costs → interest → principal → surplus to borrower), deficiency rights per state law
- Attorney's fees and collection costs (where state law permits)

### Payment Application Waterfall

> "We will apply each payment first to unpaid late charges, then to accrued but unpaid interest, then to principal, and finally to any other charges or fees owed under this Agreement."

### Required Regulatory Notices

| Trigger | Notice |
|---|---|
| All transactions | Borrower acknowledgment of receipt of completed agreement and TILA disclosures |
| Servicemember borrower | SCRA notice — potential 6% rate cap on pre-service obligations |
| Co-signer/guarantor not receiving proceeds | FTC co-signer notice (verbatim): *"You are being asked to guarantee this debt. Think carefully before you do. If the borrower does not pay the debt, you will have to. Be sure you can afford to pay if you have to, and that you want to accept this responsibility. You may have to pay up to the full amount of the debt if the borrower does not pay. You may also have to pay late fees or collection costs, which increase this amount."* |
| State-specific | Right-to-cure notices, pre-repossession notices, redemption rights — incorporate verbatim statutory language |

### Execution Section

- Acknowledgment statement immediately above signatures: receipt of completed copy, opportunity to ask questions/seek counsel, agreement to be bound
- Separate signature blocks (printed name, signature, date) for: each borrower, each co-borrower, each guarantor (with FTC notice), authorized lender officer (name + title)
- Lender commitment to deliver executed copy at signing

## Guidelines

- **Formatting**: ≥10pt body text; ≥12pt bold for TILA disclosure heading; numbered/lettered provisions; consecutive page numbers; header/footer with "Consumer Loan Agreement," borrower name, execution date
- **APR calculation**: Use actuarial method per Reg Z Appendix J; verify tolerance thresholds for transaction type
- **State law overlay**: Check for additional disclosure requirements, usury limits, prepayment penalty restrictions, deficiency judgment limitations, and force-placed insurance rules in the borrower's jurisdiction
- **Force-placed insurance**: If borrower fails to maintain coverage, lender may place and add cost to balance — disclose that force-placed insurance may cost more than borrower-obtained coverage
- **Mathematical verification**: Cross-check Amount Financed + Finance Charge = Total of Payments; verify payment schedule sums to Total of Payments
- **Do not** include waiver of jury trial, class-action waiver, or mandatory arbitration clauses without explicit instruction and state-law permissibility analysis
- **Mark** any statutory citations or regulatory references you cannot independently verify with `[VERIFY]`
