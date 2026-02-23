---
name: promissory-note-residential
description: Drafts enforceable residential promissory notes securing debt obligations against real property. Structures party identification, principal and interest terms, payment schedules, default/acceleration provisions, and security instrument cross-references with TILA and state usury compliance. Use when drafting promissory notes for residential mortgages, deeds of trust, or seller-financed home sales.
tags:
  - agreement
  - drafting
  - transactional
---

# Promissory Note (Residential)

Drafts a legally binding residential promissory note that creates an enforceable debt obligation secured by residential property, compliant with state usury laws and federal lending regulations.

## Prerequisites

1. **Governing transaction documents** — purchase agreement, security instrument (mortgage or deed of trust), any prior term sheets
2. **Party information** — full legal names of all borrowers (as on government ID) and lender (entity name + jurisdiction of formation)
3. **Property details** — complete street address matching the security instrument exactly
4. **Loan terms** — principal amount, interest rate (fixed or variable parameters), amortization period, maturity date
5. **State-specific requirements** — usury limits, late charge caps, notice requirements, prepayment penalty restrictions for the property's jurisdiction

## Output Structure

### Section 1: Header & Parties

| Element | Requirements |
|---------|-------------|
| Title | "PROMISSORY NOTE" |
| Execution date | Full month/day/year — establishes payment commencement and SOL reference |
| Property address | Exact match to security instrument (street, unit, city, state, ZIP) |
| Borrower(s) | Full legal names; specify joint and several liability if multiple; note marital status considerations |
| Lender | Full legal name; entity type + jurisdiction of formation if applicable |

### Section 2: Financial Terms

| Element | Requirements |
|---------|-------------|
| Principal | Numerals AND words (e.g., "Fifty Thousand Dollars ($50,000.00)"); unconditional promise satisfying UCC negotiability |
| Interest rate | Fixed: exact percentage. Variable: index, margin, adjustment frequency, caps, initial rate |
| Calculation method | Simple vs. compound; 360-day vs. actual-day year; accrual on unpaid principal balance |
| Payment schedule | Amount, frequency, due date, commencement date, total number of payments |
| Payment application | Order: accrued interest → principal → fees/charges |
| Maturity date | Explicit calendar date (not just term of years); balloon payment disclosure if not fully amortizing |

### Section 3: Borrower Rights

- **Prepayment**: Permitted with/without penalty; written notice requirement; specify how prepayments apply (reduce term vs. reduce payment vs. reduce balloon)
- **Partial prepayment**: Permitted Y/N; minimum amounts
- **Grace period**: Typically 10–15 calendar days
- **Late charge**: 4–5% of overdue P&I (not escrow); must not exceed state maximum; characterize as administrative cost estimate, not penalty

### Section 4: Default & Remedies

**Events of default checklist:**
- [ ] Failure to make payment when due
- [ ] Failure to pay balance at maturity
- [ ] Breach of security instrument covenants
- [ ] Bankruptcy/insolvency filing
- [ ] Material misrepresentation in loan application
- [ ] Failure to maintain property insurance
- [ ] Failure to pay property taxes

**Notice and cure:**
- Written notice specifying: the default, cure amount, cure deadline (typically 30 days)
- Delivery: personal delivery or certified mail to property address / last known address
- Cure = payment of all overdue amounts + late charges + costs → note reinstated
- Repeated defaults may permit acceleration without further notice

**Acceleration:**
- Upon uncured default, lender may declare entire balance immediately due
- Include anti-waiver language: acceptance of late/partial payments does not waive acceleration rights

### Section 5: Security & Cross-Default

- Reference the security instrument by type (Mortgage / Deed of Trust), date, and recording information (or "to be recorded in [County] land records")
- Cross-default: breach of either instrument = default under both
- Additional collateral / cross-collateralization only if applicable — flag consumer protection implications if used

### Section 6: General Provisions

| Provision | Content |
|-----------|---------|
| Governing law | State where property is located; no conflict-of-law principles |
| Jurisdiction | Courts in county where property is situated; borrower waives venue objection |
| Waiver | No waiver of one default waives subsequent defaults; acceptance of late payment ≠ waiver |
| Modification | Written only; signed by both parties; no oral modifications |
| Severability | Invalid provisions severable; remaining terms survive |
| Successors/assigns | Binds borrower's heirs/successors; lender may sell/assign without borrower consent |

### Section 7: Execution

- Signature lines for all borrowers with printed names and dates
- Representative capacity notation if signing as trustee or agent
- Acknowledgment block: borrower confirms receipt of copy, opportunity to consult counsel, voluntary execution
- Notarization: not required for enforceability but recommended for authentication

## Guidelines

1. **Usury compliance** — verify rate against the property state's usury ceiling before finalizing; flag any rate within 1% of the statutory cap
2. **TILA/RESPA** — if lender is a creditor under Regulation Z, this note alone is insufficient; flag need for Loan Estimate, Closing Disclosure, and right-of-rescission notices
3. **Consistency** — cross-check all terms (names, amounts, dates, property description) against the security instrument
4. **Payment math** — verify amortization schedule; confirm payments fully retire principal by maturity or clearly disclose balloon amount
5. **State-specific late charge caps** — common limits include: CA 6% [VERIFY], NY 2% [VERIFY], TX 5% [VERIFY]; always confirm current law
6. **Negotiability** — maintain unconditional promise to pay language to preserve holder-in-due-course protections under UCC Article 3
7. **Consumer protection** — avoid cross-collateralization in residential notes unless counsel confirms no additional disclosure obligations
8. **Plain language** — note must be understandable to non-attorney borrowers while remaining legally precise
