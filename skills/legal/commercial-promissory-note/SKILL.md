---
name: commercial-promissory-note
description: Drafts a legally enforceable U.S. Commercial Promissory Note for commercial real estate finance transactions. Produces UCC-compliant negotiable instruments with precise principal, interest, payment schedule, default, and enforcement provisions that protect lender interests at closing. Use when drafting promissory notes secured by real property, deed of trust, or mortgage in commercial lending transactions.
tags:
  - agreement
  - drafting
  - transactional
---

# Commercial Promissory Note

Drafts a senior-complexity, UCC-compliant Commercial Promissory Note for U.S. commercial real estate finance transactions, structured to protect the Payee/lender at negotiation and closing.

## Prerequisites

1. **Parties** — Full legal names and entity types for Maker (borrower) and Payee (lender); principal place of business for each
2. **Loan economics** — Principal amount, interest rate (fixed or variable index + margin), day-count convention, maturity date
3. **Payment structure** — Installment amounts/frequency, interest-only period (if any), balloon payment date (if any)
4. **Security** — Recording county/state, property address, legal description or reference to deed of trust/mortgage of even date
5. **State of execution** — Governing law jurisdiction (required for usury and prepayment penalty compliance)
6. **Prepayment terms** — Permitted/prohibited, penalty schedule if applicable, exceptions (casualty, condemnation)

## Output Structure

### Header
- Title: `PROMISSORY NOTE` (centered, all caps)
- Principal amount in numerals **and** written form (e.g., `$500,000.00 (Five Hundred Thousand and 00/100 Dollars)`)
- Execution date (full format), city, state

### Section Template

| Section | Required Elements | Key Drafting Rules |
|---|---|---|
| **Promise to Pay** | Maker identity, Payee identity, "for value received," "to the order of" | Unconditional language only — conditions destroy UCC negotiability |
| **Interest Rate** | Rate (% per annum), simple vs. compound, day-count (360 or actual/365), accrual start date | For variable rate: index (SOFR or Prime), margin, caps/floors, adjustment frequency; confirm rate ≤ state usury max; include excess-interest savings clause |
| **Payment Schedule** | Number of payments, amount per payment or calculation method, due date (e.g., "1st of each calendar month"), commencement date, maturity date | Specify payment address/account; grace period before late charge; credit date = receipt date unless stated otherwise |
| **Application of Payments** | Priority: (1) late charges/fees → (2) accrued interest → (3) principal | Address partial payments; flag negative amortization risk if interest-only |
| **Late Charges** | Grace period (10–15 days typical), charge = % of overdue payment (4–5% typical) or flat fee | Must not exceed state law maximum; acceptance of late charge ≠ waiver of default |
| **Prepayment** | Permitted/prohibited; partial or whole; penalty schedule; exceptions | Step-down penalty if used (e.g., 3%/2%/1% over years 1–3); address casualty/condemnation proceeds; partial prepayment → reduced payments or shortened term |
| **Events of Default** | Monetary default (payment failure + cure period); non-monetary defaults (covenant breach, bankruptcy, misrepresentation, insurance/tax failure); cross-default to security instruments | Monetary cure: 10 days after written notice typical; non-monetary cure: 30 days typical; use objective, not subjective, triggers |
| **Remedies / Acceleration** | Optional (not automatic) acceleration of full unpaid balance + accrued interest; all remedies cumulative; no election of remedies limitation | Payee non-exercise ≠ waiver; include default rate of interest if permitted; attorneys' fees as part of secured obligation |
| **Security Reference** | Reference deed of trust/mortgage of even date; property address + county/state; note = recourse or non-recourse | Non-recourse carve-outs (personal liability): fraud, misrepresentation, environmental, waste, misapplication of rents |
| **Maker Waivers** | Presentment, demand, notice of dishonor, notice of default/acceleration/intent to accelerate, notice of protest, protest | Use bold or ALL CAPS per state law conspicuousness requirements; waive right to require Payee to proceed against collateral first |
| **Attorneys' Fees** | Prevailing party entitled to reasonable fees + costs; covers trial, appeal, bankruptcy, post-judgment collection | May specify floor (e.g., 15% of outstanding balance); fees = part of secured obligation; check state mandatory-mutuality rules |
| **General / Boilerplate** | Governing law; severability; binding on successors/assigns; written amendment only; notice addresses + delivery methods; time is of the essence; integration clause | No Maker setoff/counterclaim rights unless negotiated |
| **Signature Block** | Individual: signature + printed name + date; Entity: full legal name + "By:" + signatory name/title + date | Confirm signatory authority; joint Makers = joint and several liability; counterparts clause recommended |

## Guidelines

- **UCC Negotiability** — Promise must be unconditional and payable to order or bearer (UCC Art. 3). Any conditional language risks destroying negotiability.
- **Usury** — Confirm stated rate does not exceed the governing state's maximum before finalizing. Include savings clause: any excess interest applied to principal or refunded. [VERIFY applicable state usury ceiling before finalizing]
- **Day-Count** — 360-day year is standard for most commercial notes; actual/365 used in some jurisdictions. State explicitly.
- **Variable Rate Index** — Use SOFR (not LIBOR). Confirm index publication source and fallback language.
- **Prepayment Penalties** — Several states restrict or prohibit prepayment penalties on certain commercial loans. [VERIFY governing state rules]
- **Non-Recourse Carve-outs** — If note is non-recourse, enumerate carve-outs explicitly; vague carve-outs are frequently litigated.
- **Consistency** — Terms must align precisely with the related deed of trust/mortgage, loan agreement, and any guaranty. Cross-default provisions must be mirrored in all security documents.
- **Consumer Protection** — If any Maker is an individual, confirm no TILA, Regulation Z, or state consumer lending statutes apply (this skill targets commercial transactions only).
