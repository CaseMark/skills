---
name: cognovit-promissory-note
description: >-
  Drafts a U.S. cognovit promissory note with confession of judgment
  provisions, jurisdictional enforceability checks, and execution formalities.
  Use when preparing commercial loan notes that may include a cognovit clause,
  confession of judgment language, or waiver of notice/hearing rights. Trigger
  keywords: cognovit, confession of judgment, promissory note, commercial
  loan, warrant of attorney, waiver of defenses.
tags:
  - agreement
  - analysis
  - drafting
  - research
  - transactional
---

# Cognovit Promissory Note

Draft a cognovit promissory note that is enforceable, properly disclosed, and compliant with governing law.

## Prerequisites

1. **Governing law and forum** — proposed state law and venue for enforcement
2. **Parties** — full legal names, entity types, formation states, addresses, authorized signers
3. **Loan terms** — principal, interest type, rate, term, payment schedule, fees, prepayment
4. **Transaction type** — commercial vs consumer classification and any statutory exemptions
5. **Authority docs** — resolutions, incumbency certificates, or member/partner consents
6. **Collateral/guaranties** — if secured or guaranteed, summary of related documents

## Output Structure / Process

**1) Enforceability Gate (Do first)**
| Check | Action | Output |
| --- | --- | --- |
| Cognovit permitted for this transaction type? | Research statutes + recent case law for the governing state. | Allow/deny with citations or `[VERIFY]`. |
| Consumer restriction? | Confirm borrower classification and any consumer protections. | If consumer or mixed-use, treat as prohibited unless clearly permitted. |
| Required warnings/format? | Identify mandatory warning language, font size, capitalization, separate acknowledgment. | Insert exact statutory warning or `[VERIFY]`. |
| Execution formalities? | Check witness/notary/affidavit or attorney requirements. | Add signature formalities and exhibits. |

If prohibited or materially restricted: output alternative structure (standard note + guaranty + security agreement) and stop before drafting a cognovit clause.

**2) Party and Authority Block**
| Field | Required |
| --- | --- |
| Lender legal name | Entity type, formation state, address, signatory title |
| Borrower legal name | Entity type or individual, address, signatory title |
| Authority evidence | Resolution/consent, incumbency, power/authority certification |

**3) Core Economic Terms**
| Term | Required Details |
| --- | --- |
| Principal | Numeric and words; fees/points treatment |
| Interest | Fixed/variable; index, margin, caps/floors; accrual method; day-count |
| Payments | Amounts, dates, schedule type, grace period |
| Application | Order of application: fees, interest, principal (or specified alternative) |
| Prepayment | Allowed? Penalty? Formula and compliance check |

**4) Confession of Judgment Clause**
Include all of the following:
- **Authority grant**: borrower authorizes any attorney to confess judgment after default
- **Scope**: principal, interest, fees, costs, attorney fees
- **Timing**: immediately upon default or after cure period
- **Forum**: courts permitted; tie to governing law and venue clause
- **Waivers**: notice, hearing, defenses, discovery, jury trial (if allowed)
- **Statutory warning**: required text and formatting

**5) Defaults and Remedies**
| Category | Include |
| --- | --- |
| Monetary default | failure to pay, grace period |
| Cross-default | if applicable, specify thresholds |
| Insolvency events | bankruptcy, insolvency, assignment for benefit |
| Misrepresentation | material statements |
| Collateral events | if secured, impairment/transfer/insurance failures |
| Remedies | acceleration, confession of judgment, collection costs |

**6) Governing Law, Jurisdiction, Venue**
- Governing law with substantial relationship
- Consent to jurisdiction and venue
- Waiver of forum non conveniens (if allowed)
- Jury trial waiver (conspicuous)

**7) Execution and Acknowledgments**
- Signature blocks with titles and entity capacity
- Witness and notary blocks if required
- Separate cognovit acknowledgment if required

**8) Exhibits (Optional but common)**
| Exhibit | Purpose |
| --- | --- |
| Amortization schedule | verify payment amounts |
| Authority documents | show signatory power |
| Collateral schedule | if secured |

**Template Skeleton**
```text
COGNOVIT PROMISSORY NOTE

Date: [Date]
Principal Amount: $[Numeric] ([Words])

FOR VALUE RECEIVED, [Borrower], a [Entity Type] organized under the laws of [State], with its principal place of business at [Address] (“Borrower”), promises to pay to the order of [Lender], a [Entity Type] organized under the laws of [State], with its principal place of business at [Address] (“Lender”), the Principal Amount plus interest as set forth below.

1. Interest. [Fixed/Variable; rate; index; margin; caps; accrual; day-count; compounding].
2. Payments. [Schedule, due dates, grace period, payment methods].
3. Application of Payments. [Fees → interest → principal].
4. Prepayment. [Permitted/penalty; formula].
5. Events of Default. [List].
6. Remedies; Acceleration. [Optional acceleration; costs; attorneys’ fees].
7. Confession of Judgment. [Full clause + statutory warning + waivers].
8. Governing Law; Jurisdiction; Venue. [State; court; consent].
9. Jury Trial Waiver. [Conspicuous].
10. Notices. [Addresses and method].
11. Miscellaneous. [Severability, amendments, counterparts, integration].

BORROWER:
[Name]
By: ______________________
Name/Title:
Date:

LENDER:
[Name]
By: ______________________
Name/Title:
Date:

[Notary / Witness Blocks if required]
```

## Guidelines

- Do not draft a cognovit clause unless enforceability is confirmed for the transaction type in the governing state.
- Consumer or mixed-use transactions: treat cognovit clauses as prohibited unless a clear statutory exception exists.
- Required warning language must be exact, conspicuous, and placed per statute; use `[VERIFY]` if unsure.
- Ensure the confession clause and forum selection align with governing law and have a substantial relationship to the transaction.
- Usury analysis must include fees/charges treated as interest; note any exemptions.
- Keep waivers conspicuous and separate; avoid burying them in standard boilerplate.
- If enforceability is unclear, recommend a standard note plus guaranty/security agreement.
