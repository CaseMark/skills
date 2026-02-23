---
name: reaffirmation-agreement
description: Drafts Reaffirmation Agreements for U.S. bankruptcy proceedings under 11 U.S.C. § 524(c). Structures the document with agreement summary tables, original and modified loan terms, debtor certification, attorney certification, and court approval sections. Enforces Bankruptcy Rule 4008 and Official Form 240A compliance. Use when a debtor reaffirms a dischargeable debt to retain secured collateral such as vehicles or homes.
tags:
  - agreement
  - drafting
  - litigation
---

# Reaffirmation Agreement

Drafts a court-ready reaffirmation agreement allowing a debtor to retain secured collateral by voluntarily reaffirming a dischargeable debt under 11 U.S.C. § 524(c).

## Prerequisites

1. **Debtor and creditor identification** — full legal names, addresses, case number, chapter filed
2. **Original loan documentation** — date, principal, interest rate, payment amount/frequency, maturity
3. **Current account status** — outstanding balance (principal + accrued interest + fees), payment history, default status
4. **Collateral details** — description, current fair market value, lien position
5. **Proposed modified terms** (if any) — reduced rate, extended term, principal reduction
6. **Debtor's Schedule I and J** — current income and expenses for undue hardship analysis
7. **Representation status** — whether debtor has counsel (determines court approval requirement)

## Output Structure

### Part A: Agreement Summary

Present in tabular format:

| Field | Value |
|---|---|
| Debtor Name | {name} |
| Case Number | {case no.} |
| Creditor Name | {name} |
| Total Debt Reaffirmed | ${amount} |
| — Principal | ${amount} |
| — Accrued Interest | ${amount} |
| — Fees/Costs | ${amount} |
| Collateral Description | {description} |
| Collateral Fair Market Value | ${amount} |
| Annual Percentage Rate | {rate}% |
| Monthly Payment | ${amount} |
| Payment Duration | {months/years} |
| Total of Payments | ${amount} |

### Part B: The Agreement

1. **Party identification** — full legal names, addresses
2. **Original loan terms** — date, principal, rate, payment, frequency, maturity
3. **Reaffirmed terms** — state whether original terms apply or modifications negotiated
4. **If modified**, present side-by-side comparison:

| Term | Original | Reaffirmed |
|---|---|---|
| Interest Rate | {orig}% | {new}% |
| Monthly Payment | ${orig} | ${new} |
| Remaining Term | {orig} | {new} |
| Total Remaining | ${orig} | ${new} |

### Part C: Debtor Certification

Debtor certifies under penalty of perjury:

- [ ] Agreement is voluntary and not required
- [ ] Debtor has ability to make required payments
- [ ] Agreement does not impose undue hardship on debtor or dependents
- [ ] Debtor understands right to rescind within 60 days after agreement filed with court, or before discharge is entered, whichever is later (11 U.S.C. § 524(c)(4))
- [ ] Debtor understands that if default occurs, creditor may repossess collateral AND pursue deficiency balance

### Part D: Attorney Certification

Required when debtor is represented. Attorney certifies:

- [ ] Agreement fully explained to debtor
- [ ] Debtor entered agreement voluntarily and with informed consent
- [ ] Debtor advised of legal effect, consequences, and consequences of default
- [ ] Attorney believes debtor can afford the payments
- [ ] Agreement does not impose undue hardship on debtor or dependents

### Part E: Court Approval

Court approval required when:
- Debtor is **not represented by counsel**, OR
- Debtor's income minus expenses (Schedule I and J) is **insufficient** to cover reaffirmed payments

Include: notice that hearing will be scheduled; court must find (1) no undue hardship and (2) agreement is in debtor's best interest.

### Signature Block

```
DEBTOR:
Signature: ________________________  Date: __________
Printed Name: _____________________

CREDITOR:
Signature: ________________________  Date: __________
Printed Name: _____________________
Title: ____________________________

DEBTOR'S ATTORNEY (if applicable):
Signature: ________________________  Date: __________
Printed Name: _____________________
Bar Number: _______________________

[NOTARIZATION BLOCK — include if required by local rules]
```

## Guidelines

- **Comply with Official Form 240A** and Bankruptcy Rule 4008 — use the official form structure as the baseline
- **Collateral-to-debt ratio**: If debt substantially exceeds collateral value, flag for additional disclosure and note vulnerability to judicial scrutiny under undue hardship standard
- **Rescission rights**: Always include the statutory rescission period — omission renders agreement unenforceable
- **No coercion language**: Agreement must affirmatively state debtor is not required to reaffirm any debt
- **Default consequences**: Prominently warn that creditor may repossess collateral AND pursue deficiency balance
- **Verify local rules**: Some bankruptcy courts require notarization or additional local forms
- **U.S. Trustee review**: Draft anticipating potential objection from the U.S. Trustee; ensure economic justification is apparent on the face of the document
- **Plain language**: Use clear language while maintaining legal precision — the debtor must actually understand the obligation
