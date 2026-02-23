---
name: consumer-loan-agreement
description: Drafts a TILA-compliant U.S. consumer loan agreement under 15 U.S.C. § 1601 et seq. and Regulation Z (12 CFR Part 1026). Enforces the mandatory federal disclosure box with Reg Z-prescribed labels, accurate APR/finance charge calculations within tolerance thresholds, complete payment schedules, default and remedies provisions, and required consumer notices (SCRA, FTC co-signer). Use when drafting consumer installment loan agreements, personal loan contracts, or any consumer finance transaction requiring federal disclosure compliance.
tags:
  - agreement
  - drafting
  - regulatory
  - transactional
---

# Consumer Loan Agreement (TILA Compliant)

Drafts a fully executed-ready consumer loan agreement with a Regulation Z–compliant federal disclosure box and comprehensive contractual provisions.

## Prerequisites

1. **Lender identity** — full legal name (including DBA), address, and contact information as registered with regulatory authorities
2. **Borrower identity** — full legal name(s) of all borrowers/co-borrowers, current addresses
3. **Loan economics** — principal amount, interest rate, loan term, payment frequency, first payment date
4. **Fee schedule** — all charges imposed as a condition of credit (origination fees, points, doc prep fees, service charges) for finance charge calculation
5. **Collateral** — full description (VIN/serial number/legal description) if secured; confirmation if unsecured
6. **Governing state** — for state-specific rate caps, prepayment penalty restrictions, deficiency judgment rules, and cure notice requirements
7. **Co-borrower/guarantor info** — if applicable, triggers FTC co-signer notice requirement

## Output Structure

### 1. Federal Truth in Lending Disclosure Box

Display first on page one, visually segregated (border/shading), heading in bold at ≥12pt, body at ≥10pt.

| Reg Z Label | Content |
|---|---|
| **Annual Percentage Rate** — The cost of your credit as a yearly rate | APR to ≥2 decimal places; use actuarial or U.S. Rule method; tolerance: ±⅛% for regular transactions (12 CFR § 1026.22) |
| **Finance Charge** — The dollar amount the credit will cost you | Total interest over loan life + all fees imposed as condition of credit; itemize major components |
| **Amount Financed** — The amount of credit provided to you or on your behalf | Principal minus prepaid finance charges; excludes finance charge |
| **Total of Payments** — The amount you will have paid after making all scheduled payments | Amount Financed + Finance Charge |
| **Payment Schedule** — Your payment schedule will be | Uniform payments: count + amount + frequency; Irregular/balloon: full table with date and amount per payment |

> **Math check**: Amount Financed + Finance Charge = Total of Payments. APR must be recalculated if any fee or term changes.

---

### 2. Loan Terms and Conditions

**Loan Purpose** (include if required by state or relevant to regulatory classification):
> "This loan is extended for personal, family, or household purposes."

**Prepayment**
- If no penalty: *"You may prepay in whole or in part at any time without penalty beyond accrued interest to the prepayment date. Refunds of precomputed finance charges, if any, calculated by actuarial method."*
- If penalty applies: Disclose conspicuously — conditions, penalty period, calculation method, maximum amount; confirm compliance with state law (many states prohibit prepayment penalties on consumer/residential loans).

**Late Charges**
> *"If payment not received within [10–15] days of due date, late charge of [5%] of unpaid scheduled payment or [$25], whichever is less. Assessed once per late payment; not compounded."*
> Confirm amount is reasonable estimate of administrative cost, not a penalty; verify state cap.

**Payment Application Order**
> Late charges → accrued interest → principal → other fees/charges

**Security Interest** (if secured):
- Grant of security interest in described collateral
- Borrower covenants: maintain condition, keep free of liens, maintain required insurance (lender as loss payee/additional insured), no transfer without consent
- Lender's right to force-place insurance if borrower fails; cost added to principal balance

**Unsecured Loan** (if applicable):
> *"This is an unsecured loan. No collateral is pledged. Lender's remedies upon default are limited to those available for unsecured debt under applicable law."*

---

### 3. Default, Acceleration, and Remedies

**Events of Default** (non-exhaustive list to include):
- Failure to make timely payment
- Failure to maintain required collateral insurance
- Bankruptcy or insolvency
- Material misrepresentation on loan application
- Impairment of collateral or security interest
- Death of borrower (if loan does not survive)

**Acceleration**: Upon default, lender may declare entire unpaid principal and accrued interest immediately due, subject to any state-required notice and cure period (specify days and delivery method).

**Collateral Remedies** (if secured): Right to repossess (self-help to extent permitted by state law), sell at public or private sale (UCC-compliant notice), apply proceeds: repossession/sale costs → interest → principal; deficiency remains borrower obligation to extent permitted by state law.

---

### 4. Required Notices

| Trigger | Notice Required |
|---|---|
| Borrower is or may be a servicemember | SCRA notice: right to 6% rate cap on pre-service obligations; instruct borrower to notify lender upon activation |
| Co-signer/guarantor not receiving loan proceeds | FTC Co-Signer Notice verbatim (16 CFR Part 444): *"You are being asked to guarantee this debt. Think carefully before you do..."* |
| State law | Incorporate any required verbatim notices (cure rights, pre-repossession notice, right of redemption) |

---

### 5. Execution Block

**Borrower acknowledgment** (above signature lines):
> *"By signing below, I/we acknowledge receipt of a completed copy of this Agreement including the Federal Truth in Lending Disclosures. I/we have read, understand, and agree to all terms."*

- Signature line(s): printed name, signature, date — one block per borrower/co-borrower
- Separate guarantor block with FTC notice if applicable
- Lender block: authorized officer name, title, signature, date
- Lender to provide executed copy to borrower at signing

---

## Guidelines

- **APR tolerance**: ±⅛% (0.125%) for regular transactions; ±¼% for irregular transactions (12 CFR § 1026.22) [VERIFY current tolerances post-amendment]
- **Conspicuousness**: TILA box must precede all other contract terms and be visually distinct — a buried or merged disclosure box is a Reg Z violation
- **State law layering**: State usury caps, prepayment penalty bans, mandatory cure periods, and deficiency judgment restrictions vary significantly — always confirm governing state rules
- **No TILA box modification**: Use Reg Z–prescribed labels verbatim; do not paraphrase disclosure headings
- **Math accuracy**: Verify Amount Financed, Finance Charge, APR, and Total of Payments are internally consistent before finalizing
- **Variable-rate loans**: Additional Reg Z ARM disclosure requirements apply (12 CFR § 1026.19(b)); this template covers fixed-rate transactions only
- **Mortgage/HELOC**: Subject to additional RESPA, TRID, and state recording requirements — outside scope of this skill
