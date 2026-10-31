---
name: managing-coding-denials
language: en
description: >
  Analyzes hospital coding denials and DRG and clinical validation denials (DRG downgrades,
  removed diagnoses, sepsis, inpatient status, 2-midnight) for Medicare
  fee-for-service, Medicare Advantage and commercial payers, and drafts appeal strategy and
  letters built on the record as it stood when the claim was billed. Classifies each
  denial as coding validation, clinical validation, medical necessity or technical so the
  argument matches it; computes every deadline from its own trigger (redetermination,
  reconsideration, ALJ, MA reconsideration under 42 CFR 422.582, contract windows, timely
  filing, Part B rebilling); applies 2026 amount-in-controversy thresholds; screens RAC, MAC
  and UPIC review limits; tests MA internal coverage criteria under 422.101(b)(6) and 422.138;
  reads Sepsis-3 or Sepsis-2 from the payer contract; weighs appeal against rebilling; logs
  peer-to-peer outcomes. Declines to present documentation altered or added after a
  denial as original. Drafts for coder, CDI and compliance review.
tags:
  - management
  - medical-coding-and-billing
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Coding Denials

Builds a denial analysis and appeal package for one hospital claim or a batch of related claims: a denial register, a clock table with every deadline computed from its own trigger, a classification of each denied item, a route election (appeal, correct and rebill, reopening, or accept), and a draft appeal letter whose arguments match the denial type and rest on the record as it stood when the claim was billed. The aim is accurate payment for documented, supported care, in either direction. Everything it produces is a draft for review by a qualified coder, CDI specialist, denials manager and, where legal questions arise, counsel; it is not a filed appeal or legal advice.

## Why This Skill Exists

Coding denials are lost on procedure more often than on merit. A redetermination counted from the day the denials team saw the letter instead of five days after the notice date is late; a request mailed on the last day is filed only when the contractor receives it. A clinical validation denial answered with "the physician documented it" (ICD-10-CM I.A.19) answers a question the payer did not ask, and a Sepsis-3 contract answered with SIRS criteria concedes the issue. Medicare Advantage plans cite screening tools the rules do not let them rely on, and contracted hospitals file regulatory appeals their contract routes elsewhere. Rebilling, reopening and appeal foreclose each other on different clocks. And the tempting fix, an addendum written after the denial and presented as part of the original note, turns a payment dispute into a record-integrity problem. This skill puts those checks ahead of the drafting.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Denial notice, demand letter, ERA, MA organization determination, audit letter | Starting every clock | Deadline counted from the day the denials team received the letter, or from the notice date without the 5-day presumed receipt; mailing date treated as filing date; the recoupment, Part B and contract clocks assumed to share one anchor |
| Reviewer's rationale (RAC, MAC, UPIC, MA plan, commercial auditor) | Classifying the denial and the argument | A clinical validation denial answered only with I.A.19, or a coding validation denial answered with clinical severity; medical necessity and coding issues merged into one argument |
| Payer contract, amendment and provider manual | Clinical definitions, appeal levels and windows | Sepsis-2 argued against a contract that specifies Sepsis-3, or the reverse, without reading the contract in force on the date of service; a commercial window replaced by Medicare's 120 days or 5-day presumption |
| MA plan letter citing internal criteria or a screening tool | Inpatient and medical necessity denials | Plan criteria treated as binding although 422.101(b)(6) limits them and 412.3 governs admissions; the 2-midnight presumption argued as binding on the plan; a prior concurrent approval (422.138(c)) overlooked |
| Party, contract status and reviewer authority | Choosing the appeal route and objections | A contracted hospital filing a 422.582 reconsideration its agreement routes to contract dispute; a non-contracted hospital omitting the waiver of liability; a RAC clinical validation finding (prohibited by the RAC SOW) argued only on the merits |
| Medical record, addenda, query responses, late entries | Evidence for the appeal | An addendum or query answer written after the claim or after the denial presented as original; entries without date and author; evidence first produced at the ALJ level, where it is excluded without good cause |
| Calendar for the deadline (weekends, federal holidays, payer or mailroom closures) | Setting the target receipt date | A deadline on a Saturday, Sunday or holiday assumed to roll to the next business day although the rule (for example 422.582(b)) or the contract has no roll provision; a submission planned for a day the receiving office is closed |
| Peer-to-peer notes and RAC discussion records | Informal resolution | Oral overturn never confirmed in writing; outcome, participants and reference number not recorded; written appeal deadline allowed to lapse while waiting |
| Rebill, reopening and Part B decisions | Choosing between correction and appeal | Part A appeal pursued past the 1-year Part B window measured from the "Through" date; a higher DRG sought after the 60-day 412.60(d) window; a reopening requested while the same issue is under appeal |

## Ground Rules

1. **Draft only.** Every output is a draft for qualified human review. Never state that an appeal is filed, final or certain to succeed, and never give legal advice on litigation or contract enforcement.
2. **Source-review gate.** Do not call a document, notice or entry missing until every supplied file has been opened and searched, including scans and oddly named files. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (a rule not confirmed for the current year) or a policy election (a contract term not supplied, or the hospital's choice between routes).
3. **Hierarchy of authority.** For rules: statute and regulation, then CMS manuals and binding instructions, then contractor statements of work and CMS guidance, then the payer contract and provider manual in force on the date of service, then payer policy, then the denial letter's characterization. For facts: the record as it stood when the claim was billed, with audit trail, governs over later entries, abstracts, denial-letter summaries and vendor worksheets. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every clinical value, quotation and date carries a source locator (document, date and time, author role) or `[UNVERIFIED]`. Every rule carries its citation or `[VERIFY]`; every year-dependent figure carries its year.
5. **Record integrity.** Never draft, merge, backdate or re-date a clinical entry, and never present documentation created or altered after the claim or the denial as original. A late entry is disclosed with its own date and author. If asked otherwise, record a Declined request and continue with the record as it stands. If altered entries were already submitted, stop drafting that appeal and route to conducting-false-claims-analysis and compliance.
6. **Classify before arguing.** Label each denied item coding validation, clinical validation, medical necessity or status, or technical (`references/denial-analysis-rules.md`, Section 1). The argument must answer that type.
7. **Every clock has its own trigger.** Compute each deadline separately with its trigger, rule and arithmetic, its weekday, and who must receive it. Never carry one payer's presumption or window to another. A deadline that falls on a weekend or holiday does not roll unless the rule or contract provides one; set the target receipt date to the prior business day.
8. **Lock the payer and the party.** Name the product (Medicare FFS, MA HMO or PPO, commercial, ERISA plan, Medicaid) and the hospital's contract status before choosing a route. A contracted MA hospital follows its agreement; a non-contracted one follows 422.582 with a waiver of liability.
9. **Definitions come from the contract.** Apply the clinical definition the contract or policy in force on the date of service names. If it is not supplied, treat it as a policy election `[VERIFY]` and show the record under each candidate definition.
10. **Respect reviewer limits.** Raise scope objections first: a RAC may not perform clinical validation or look back more than 3 years; an MA plan may not deny on unposted internal criteria or after its own approval except as 422.138(c) allows.
11. **Recommendation vocabulary.** Each denied item gets one of: Appeal, Correct and rebill, Request reopening, Accept denial, or Hold: <fact>. Each deadline is Open, Urgent (10 days or fewer) or Expired: good cause only. A refused request is a Declined request with the rule behind it. The test for each label is in `references/output-template.md`, Section 12.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Today's date and the purpose: single-claim appeal, batch of related denials, pre-appeal triage, or denial-pattern review.
2. The denial notice itself (letter, ERA or portal notice), or a labelled excerpt giving its date, issuer, reference and key text, plus any demand letter and earlier appeal decisions.
3. Payer and product, the hospital's contract status, and for commercial or contracted MA claims the contract or provider manual sections on appeals and clinical definitions.
4. Claim data: bill type, "From" and "Through" dates, codes billed, DRG or status billed and as revised, amount at issue.
5. The medical record as billed for the issue in dispute (or quoted excerpts with date, time and author), plus every addendum, query and late entry with its creation date.
6. Peer-to-peer, discussion-period and correspondence records; mailroom or portal receipt evidence.

Defaults when an input is missing:

- Receipt date unknown: use the regulatory presumption for the payer, labeled as presumed; for commercial payers use the contract's trigger, and if the contract is not supplied, use the notice date and mark it `[VERIFY]`.
- Contract status unknown for an MA claim: show both routes (422.582 with waiver; contract dispute) and their deadlines, labeled provisional.
- Clinical definition not supplied: analyze under each candidate definition.

Hard stops (do not draft appeal arguments):

- No denial notice, remittance or audit letter, and no labelled excerpt of one ("Excerpt from the denial notice" giving its date, issuer, reference and the reviewer's stated reason), only an unlabelled description: produce the intake list and stop; no deadline is computed from a description.
- Payer or product unknown, so no appeal route can be selected.
- No record documentation at all for the issue in dispute (neither the record nor dated, attributed excerpts): compute the clocks, list what is needed, and stop before the argument.
- A request to create, alter, merge, backdate or re-date documentation, or to present a post-claim or post-denial entry as original: decline that part as a Declined request, then continue with the record as it stands.
- Evidence that altered entries were already submitted on this claim: stop the appeal draft and route to conducting-false-claims-analysis and compliance.

## Step 1: Frame the Payer, Party and Level

Read `references/appeal-clocks-and-levels.md`, Sections 1, 6 and 7. State the product, contract status, the current level and the next level available. Confirm who may appeal (provider, assignee, enrollee's representative) and whether an appointment of representative or waiver of liability is needed.

## Step 2: Build the Denial Register and Clock Table

Use `references/output-template.md`, Section 2. For each notice, record its date and issuer, then compute each timed element from its own trigger: the appeal window, recoupment, Part B rebilling, DRG review, reopening and any contract window. Show presumed receipt where a rule supplies one, the arithmetic, the receiving entity, and the deadline status. Read `references/appeal-clocks-and-levels.md`, Sections 2 to 5, for the rule behind each row. For any ALJ or court request, apply the threshold for the calendar year of filing and show the amount-in-controversy computation.

## Step 3: Classify Each Denied Item and Test Reviewer Authority

Read `references/denial-analysis-rules.md`, Sections 1, 2 and 5. Quote the reviewer's rationale, assign the denial type, and list scope objections: RAC clinical validation or look-back, MA criteria not posted or not permitted, a prior MA approval, a contractor imposing a coding rule that does not exist. Route the DRG grouping itself to managing-drg-optimization and use its result.

## Step 4: Build the Source Register and Check Record Integrity

Use `references/output-template.md`, Section 3, and `references/denial-analysis-rules.md`, Section 6. Open every document and record its author, creation date and whether it predates the claim and the denial. Late entries are labeled and disclosed; they are never merged into an original note. Apply the hard stops.

## Step 5: Test the Merits Under the Right Standard

Read `references/denial-analysis-rules.md`, Sections 2 to 5. Coding validation: quote the provider's documentation and the guideline section. Clinical validation: identify the definition the contract names, then tabulate each criterion with value, time and source, and say plainly where the record falls short. Medical necessity or status: show the admitting practitioner's expectation at the order, the time counted toward 2 midnights, and the complex medical factors. Where the record does not support the billed code or status, say so and recommend Accept denial or Correct and rebill.

## Step 6: Elect the Route

Read `references/denial-analysis-rules.md`, Sections 7 and 8. Fill the route election table (`references/output-template.md`, Section 5) with each route's deadline, what it recovers and what it forecloses. Put elections that belong to the hospital (Part A appeal against Part B rebilling; contract dispute against arbitration) to the hospital with both deadlines. Log every peer-to-peer and discussion with its outcome and written confirmation.

## Step 7: Draft the Appeal and Hand Off

Draft the letter from the skeleton in `references/output-template.md`, Section 6, answering each denial type in its own section, with dated enclosures. Complete the reconciliation table, gaps, hand-offs and open items (Sections 8 to 11). Check each rule relied on against `references/primary-sources.md` and carry any `[VERIFY]` flag into the open items.

## Checkpoint B: Post-Draft Alignment

1. Does each denied item have a type, a recommendation from the vocabulary, and an argument that answers that type?
2. Is every deadline computed from its own trigger, with presumed receipt where a rule supplies it, and the receiving entity named?
3. Does the route match the payer, product and contract status, and are scope objections raised before the merits?
4. Is every clinical value sourced and dated, and does every enclosure predate the claim or carry its own late-entry label?
5. Does any result depend on a `[VERIFY]` item, and would it change if the item reads the other way?
6. Is anything phrased as a guaranteed outcome, legal advice, or a suggestion to change documentation? Remove it.

## Quality Audit

1. The header names the payer, product, contract status, dates of service and current level.
2. The denial register lists every notice with date, issuer and reference.
3. Each clock row shows trigger, rule, arithmetic, deadline with its weekday, target receipt date, receiving entity and status, and no two rows share an anchor by assumption.
4. Medicare and MA deadlines apply the 5-day presumed receipt; commercial deadlines use the contract's own trigger.
5. Any ALJ or court threshold is the one for the calendar year of filing, with the computation shown.
6. Each denied item is classified, and clinical validation arguments rest on the contract's definition with a criterion table, not on I.A.19 alone.
7. Scope objections (RAC clinical validation, MA internal criteria, prior MA approval) are raised where the facts support them.
8. The source register records creation dates; no post-claim or post-denial entry is presented as original.
9. The route election shows each route's deadline and what it forecloses, including the Part B window and 412.60(d).
10. Peer-to-peer outcomes are logged with participants, reference number and written confirmation status.
11. Every conflict is in the reconciliation table and every gap is classified.
12. Every `[VERIFY]` relied on appears in the open items with what would settle it, and declined requests are listed.

## Guidelines

- A correct denial is accepted. The skill argues for the code or status the record supports, whether that raises or lowers payment.
- CARC and RARC codes describe the adjustment, not the reasoning; read the review rationale before classifying.
- A provider query used to clarify a record after a denial follows the facility's post-bill query policy and compliant query standards (managing-cdi-programs), never mentions the denial, and produces a dated addendum.
- A favorable peer-to-peer is not a payment; diary the written appeal deadline until written confirmation arrives.
- Submit the complete evidence at the earliest Medicare level possible; new provider evidence after the QIC is excluded without good cause.
- Keep protected health information to what the appeal needs; de-identify shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Two possible notice dates (letter date and ERA date) | Separate documents for one determination | Compute both, use the earlier deadline, and add a reconciliation row |
| Scanned record pages without legible dates | Image-only file | Attempt OCR; list unreadable pages and the arguments that depend on them as Cannot determine |
| Denial letter misstates the record | Reviewer summarized from an abstract | Quote the record with locators; the record controls |
| Contract supplied but silent on clinical definitions | Payer relies on policy outside the contract | Request the policy and its effective date; analyze under each candidate definition; policy election |
| Deadline already passed | Notice misrouted or clock miscounted | Draft a good-cause statement using the regulatory examples; mark Expired: good cause only |
| Record contains an undated addendum | EHR export dropped metadata | Request the audit trail before using the entry; until then treat it as a late entry of unknown date |

## Related Skills

- managing-drg-optimization: MS-DRG assignment, principal and secondary diagnosis validation, and CC/MCC questions behind a DRG downgrade.
- conducting-false-claims-analysis: altered or backdated records, overpayments found during appeal review, and patterns of unsupported codes.
- managing-cdi-programs: compliant provider queries when documentation conflicts.
- managing-observation-stays: inpatient versus observation status under 412.3.
- managing-payer-specific-coding: LCD, NCD and payer-specific coding rules behind a denial.
- managing-medical-records-compliance: amendment, late-entry and audit-trail policy.
- auditing-coding-accuracy: internal audits when denials point to a coding pattern.
- managing-sepsis-bundles: SEP-1 abstraction, which is a quality measure and not a coding or payment standard.
- contract-dispute-analysis: commercial payer contract disputes beyond the contractual appeal process.
- legal-research: ERISA, state external review and other law questions no dedicated skill covers.

## Reference Files

- `references/appeal-clocks-and-levels.md`: Medicare FFS levels and clocks, amount in controversy, review contractors, recoupment, reopening and rebilling clocks, Medicare Advantage and commercial routes.
- `references/denial-analysis-rules.md`: denial taxonomy, I.A.19, contract clinical definitions and Sepsis-3, 2-midnight rule, MA coverage criteria, record integrity, peer-to-peer, route selection.
- `references/output-template.md`: deliverable sections, clock table, source register, argument map, route election, letter skeleton, reconciliation and hand-off tables.
- `references/primary-sources.md`: each authority checked with URL, method and date, and the `[VERIFY]` list.
