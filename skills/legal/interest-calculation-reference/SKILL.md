---
name: interest-calculation-reference
description: Calculates and validates U.S. bankruptcy claim interest for creditor-side filing and review. Use for drafting or auditing a Proof of Claim, preparing objections/rebuts, generating attachment-ready worksheets, or estimating claim value using triggers like "proof of claim", "pre-petition interest", "bankruptcy claim", "interest worksheet", and "claim amount".
tags:
  - analysis
  - checklist
  - litigation
---

# Bankruptcy Interest Calculation Reference

Reference workflow for pre-petition interest calculations and charge inclusion decisions for creditor proofs of claim.

## Prerequisites

1. Case context: petition date and case number.
2. Governing loan/credit document set.
3. Payment history and balance ledger (chronological).
4. Contract or judgment terms for rate and accrual method.
5. State law source for prejudgment statutory rates (if no contract/judgment rate).
6. Collateral valuation and lien status if claim is secured.
7. Copies of fee provisions and statutory fee authorities.
8. Date calculator or verified date diff method (actual calendar days).

## Output Structure / Process

### 1) Core Inputs
| Field | Capture |
|---|---|
| Principal Balance | Outstanding principal as of last payment or cutoff date |
| Last Payment/Accrual Date | Date of last payment or latest principal application |
| Petition Date | Petition filing date |
| Annual Rate | Decimal or percentage |
| Rate Source | Contract / Judgment / State statutory / Federal |
| Day-Count Basis | 365, 360, or 30/360 |
| Claim Type | Unsecured, Secured, Priority |
| Charges Included | Late fees, NSF/returned-item fees, attorney fees, other |

### 2) Formula
- `Interest = Principal × Rate × (Days / Day-Count-Basis)`
- `Pre-petition Interest = Principal × Rate × (Accrual Days ÷ Day-Count-Basis)`
- `Per Diem = (Principal × Rate) ÷ Day-Count-Basis`
- `Total Claim = Principal + Pre-petition Interest + Allowed Other Charges`

### 3) Rate Source Priority
| Priority | Source | Use Rule |
|---|---|---|
| 1 | Contract | Use exact contractual rate and stated methodology |
| 2 | Judgment | Use judgment rate where claim is based on pre-petition judgment |
| 3 | State statutory prejudgment rate | Use applicable state rate only if higher-priority source absent |
| 4 | Federal 28 U.S.C. §1961 | Use only when judgment-rate path points to it as governing fallback |

### 4) Post-Petition Interest Entitlement
| Claim Type | Default Rule | Notes |
|---|---|---|
| Unsecured | No post-petition interest | Stop at petition date; include solvent-debtor exception only if affirmatively supported [VERIFY] |
| Secured | Allowable only if oversecured under 11 U.S.C. §506(b) | Limited by equity cushion (collateral value above claim) |
| Priority | Usually no post-petition interest | Confirm specific statutory priority language |

### 5) Charge Inclusion Gate
- Late/penalty charges: include only if contract-authorized, accrued pre-petition, and reasonable/non-punitive.
- NSF/returned-item/admin fees: include only if actually assessed pre-petition and authorized.
- Attorney fees: include only if contract or statute authorizes pre-petition recovery.
- Always attach supporting documentation to each charge line item.

### 6) Worksheet Template
```text
-----------------------------------------------
BANKRUPTCY INTEREST CALCULATION WORKSHEET
-----------------------------------------------
Debtor: ____________   Case No.: ____________
Creditor: ____________  Account No.: __________

1) Principal Section
Original principal:          $ ________
Payments to cutoff:         -$ ________
Principal as of [Last Payment/Accrual Date]: $ ________

2) Interest Section
Annual rate:               ________%
Rate source: [ ] Contract [ ] Judgment [ ] State [ ] Federal
Day-count basis: [ ] Actual/365 [ ] Actual/360 [ ] 30/360
Accrual period: [From] __ / [To] __ / Days ____

Per diem:                  $ ________
Pre-petition interest:     $ ________

3) Other Charges (include only if supported)
Late fees:                 $ ________
NSF/other fees:            $ ________
Attorney fees (pre-petition): $ ________
Other allowed charges:      $ ________
Other charges total:        $ ________

4) Claim Summary
Principal:                 $ ________
Pre-petition interest:     $ ________
Other charges:             $ ________
Total claim at petition:   $ ________

Documentation checklist:
[ ] Contract/judgment rate clause
[ ] Payment ledger
[ ] Day-count rationale
[ ] Charge authorization
[ ] Signature/date
```

### 7) Validation Checklist (run before filing)
| Error Pattern | Required Fix |
|---|---|
| Using wrong principal baseline | Reconcile to balance after last credited payment |
| Wrong day-count basis | Use contract/more favorable documented basis |
| Wrong compounding method | Match contract (simple unless explicitly stated otherwise) |
| Including unauthorized fees | Remove and note authority required |
| Missing rate source | Document section/article/statute or contract paragraph |
| Calculating beyond petition date | Cap unsecured and general claims at petition date |

### 8) Cross-References
- `@bankruptcy-proof-of-claim`
- `@bankruptcy-collateral-valuation-reference`
- `@bankruptcy-objection-to-proof-of-claim`
- `@commercial-loan-analysis`

## Guidelines

- Always preserve units: convert percentages to decimals only inside formulas.
- Prefer plain-text audit trail: list each numeric input, assumption, and source.
- Do not mix post-petition accrual into pre-petition totals.
- Treat federal post-judgment rate as a fallback path, not a first principle for non-judgment debt.
- State-law prejudgment rates vary by state and date; verify current statute/case law in that jurisdiction before relying on them.
- For uncertain statutory applications (e.g., solvent-debtor interest treatment), flag and [VERIFY] with venue-specific authority.

## References
- 11 U.S.C. §502(b)(2) (unmatured interest treatment)
- 11 U.S.C. §506(b) (post-petition interest for oversecured claims)
- 28 U.S.C. §1961 (post-judgment interest benchmarks)
- Applicable state prejudgment interest statute (case-specific; verify citation)
