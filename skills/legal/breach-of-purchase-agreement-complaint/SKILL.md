---
name: breach-of-purchase-agreement-complaint
description: >-
  Drafts a U.S. litigation complaint for breach of a purchase agreement and
  prepares it for filing in pre-filing and pleading workflows. Use when the
  user requests a complaint, breach-of-contract claim, forum-selection
  analysis, or remedy package in real-estate/asset purchase disputes. Trigger
  keywords: complaint drafting, breach of purchase agreement, purchase
  agreement breach pleading, specific performance, attorney fee clause,
  damages prayer.
tags:
  - drafting
  - litigation
  - pleading
---

# Complaint for Breach of Purchase Agreement

Produces a filing-ready complaint that secures liability and remedies while preserving evidentiary precision for litigation.

## Prerequisites

1. Executed purchase agreement and all related documents (amendments, riders, addenda, notices, cure letters, correspondence, and payment records).
2. Verified party identity and capacity data, including legal names, entity types and formation states, addresses, and registered agents where applicable.
3. Transaction timeline and factual support for each element: negotiation, execution, performance milestones, breach event, notice, and mitigation efforts.
4. Jurisdictional directives: target court/system, forum-selection and choice-of-law terms, arbitration scope, and local filing/declaration requirements.
5. Damages and remedy inputs: direct damages, consequential damages, incidental costs, interest expectations, and attorney-fee basis.

## Output Structure / Process

1. Generate filing scaffold with official caption, court heading, case number placeholder, title of action, attorney block, and plaintiff/defendant blocks in court-compliant order.

2. Add `Jurisdiction and Venue` section with explicit, jurisdiction-anchored grounds.

| Item | Required findings | Draft output |
|---|---|---|
| Subject-matter jurisdiction | diversity, federal question, or state-law basis | select and plead one primary basis |
| Personal jurisdiction | defendant presence, contacts, or minimum contacts | include jurisdictional facts |
| Venue | contract formation, performance, breach location, defendant residence/business location | tie each venue fact to paragraph-supported allegation |
| Forum-selection and choice of law | exclusive forum, governing law, arbitration requirements | enforceability and applicability analysis |

3. Build parties section with structured party records.

| Party role | Required fields |
|---|---|
| Plaintiff | legal name, status/capacity, role in transaction, full address |
| Defendant | legal name, aliases, legal structure, address, registered agent |
| Additional parties | guarantors, assignees, successors if needed |

4. Build factual chronology section as numbered paragraphs in strict temporal order with exhibit references where possible.

5. Draft breach of contract cause of action using element-to-fact mapping.

| Element | Pleading requirement | Exhibit linkage |
|---|---|---|
| Contract formation | valid agreement, parties’ authority, consideration, essential terms | purchase agreement and signatures |
| Defendant duty | exact breached provision and expected performance | contract sections/clauses |
| Breach | specific omission/late performance and date | breach notice timeline |
| Plaintiff performance | performance completed or valid excuse for nonperformance | payment receipts, approvals |
| Causation and damages | direct causation plus resulting harm | accounting, expense logs, market proof |

6. Generate damages section with an itemized ledger.

| Damage category | Calculation method | Supporting input |
|---|---|---|
| Expectancy/direct | contract-differential or replacement-cost method | invoice, payment records, market evidence |
| Consequential | foreseeable losses tied to breach | loss projections, mitigation records |
| Incidental | re-listing, storage, administrative follow-up costs | receipts, bills, service logs |
| Fees/costs | only if contract/statute authorizes | fee clause or statutory basis |

7. Draft Prayer for Relief with explicit relief buckets: damages (sum or proof at trial), specific performance where unique subject matter, pre/post-judgment interest, costs, fees if authorized, attorney costs, and injunctive relief if warranted.

8. Include jury demand, filing status labels, and any anti-damages cap/liquidated-damages interpretation caveats.

9. Add verification and signature blocks.

```text
Verification block:
- use unsworn declaration or notarized statement per jurisdictional requirement
- include penalty-of-perjury wording if applicable

Attorney block:
- name, bar number, firm, address, phone, email, signature/date
- paralegal/firm representative as required by court rules
```

10. Return final compliance checklist appended to complaint.

| Check | Pass/Flag |
|---|---|
| Jurisdiction and venue are sufficient and internally consistent |  |
| Party descriptors are complete and uniformly styled |  |
| Each element has paragraph-level fact support |  |
| Remedy requests match available authority |  |
| Court formatting and signature standards met |  |

11. Insert `[VERIFY]` on any assertion of statute, rule, interest rate, filing prerequisite, or remedy authorization not directly supplied by user materials.

## Guidelines

- Keep factual allegations separate from legal conclusions in each paragraph.
- Prioritize contract language over paraphrase for breach trigger allegations.
- Do not invent forum, amount-in-controversy, or statutory authority.
- Preserve and enforce forum-selection, arbitration, and liquidated-damage clauses.
- Do not include extra settlement language or demand-letter posture inside the pleadings.
- Use `[VERIFY]` markers for unknown or disputed law and request user confirmation before final legal assertion.
