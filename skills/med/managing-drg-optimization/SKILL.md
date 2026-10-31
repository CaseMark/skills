---
name: managing-drg-optimization
language: en
description: >
  Reviews MS-DRG assignment on one inpatient claim so the DRG is accurate and supported by provider
  documentation; DRG optimization here means correcting errors in both directions, never upcoding.
  Validates principal diagnosis selection under UHDDS and ICD-10-CM Official Guidelines Section II,
  secondary diagnoses and CC/MCC capture under Section III, CC exclusion list checks, MS-DRG Grouper
  V44 for FY 2027 discharges, POA and HAC impact, symptom codes as principal, sepsis coded
  to the provider's statement rather than Sepsis-2 or Sepsis-3 criteria, discharge and transfer
  rules, the 3-day payment window, procedure O.R. status and the inpatient order. Drafts non-leading
  CDI and clinical validation query candidates under the ACDIS/AHIMA 2026 compliant query
  guidelines. Use for DRG validation, DRG optimization review, CC/MCC capture, case mix index (CMI)
  accuracy, CDI second-level review or pre-bill audit. Declines adding unsupported diagnoses
  or leading providers. Drafts for coder, CDI and compliance review.
tags:
  - management
  - medical-coding-and-billing
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

# Managing DRG Optimization

Builds a DRG validation worksheet for one inpatient claim: a source register and code ledger, a principal diagnosis analysis, a severity and exclusion check under the grouper version for the discharge date, the resulting MS-DRG with the direction of any change, compliant query candidates, and hand-offs. The legitimate aim is accurate, documentation-supported DRG assignment: every code rests on a provider's statement and the coding rules, and errors are corrected whether the DRG goes up or down. Everything it produces is a draft for review by a credentialed coder, a CDI specialist and compliance; it is not a final code set, a query sent to a provider, or billing advice.

## Why This Skill Exists

MS-DRG assignment sets the Medicare inpatient payment for the stay, and most payers that pay by DRG copy the logic. A single secondary diagnosis can move a case between "without CC/MCC", "with CC" and "with MCC", so small coding errors carry large payment effects in both directions. Medicare contractors validate the principal diagnosis, secondary diagnoses and procedures against the record (PIM 100-08, ch. 6, 6.5.3), and an unsupported MCC billed at scale becomes an overpayment and, potentially, a False Claims Act problem. The rules change every October 1: Grouper V44 governs FY 2027 discharges, and the FY 2027 final rule moved ten housing-instability codes from CC to NonCC. Most errors are not exotic. They come from choosing the principal diagnosis by payment, coding from a lab value or a nursing note, missing a CC exclusion, using last year's CC list, or writing a query that tells the provider what to say. This skill makes each of those checks explicit.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| H&P, ED note, discharge summary | Selecting the principal diagnosis | Principal chosen for the higher-weighted DRG; II.C "equally meets" invoked for a condition that arose after admission; a symptom code (melena, chest pain) kept as principal when a related definitive diagnosis was established (II.A) |
| Lab results, vital signs, nursing, dietitian and therapist notes | Finding CC/MCC candidates | A CC or MCC coded from a creatinine, a sodium, "confused" in a nursing note, or a dietitian's malnutrition assessment with no provider diagnosis; the I.B.14 exceptions (BMI, pressure ulcer stage, SDOH and others) stretched to cover the diagnosis itself |
| V44 CC/MCC lists and Appendix C CC exclusions | Deciding whether a secondary code changes the DRG | An MCC counted although excluded with the principal (R65.20 with A41.x); a CC counted in a family that splits only on MCC (870-872); the excluded code deleted instead of kept |
| Coder worksheets, encoder tables, CDI tip sheets | Severity look-ups and expected DRG | A FY 2026 (V43) list applied to an FY 2027 discharge: Z59 housing codes still treated as CCs; deleted DRGs (466-468) still cited |
| The request and the claim itself: payer, claim type, inpatient order | Scope: whose rules and which grouper | An observation or outpatient claim reviewed as inpatient; no inpatient order under 42 CFR 412.3; a Medicare Advantage or commercial claim assumed to pay on MS-DRG without reading the contract |
| Draft queries and EHR or AI prompts | Clarifying documentation | Title naming the wanted diagnosis; DRG or MCC mentioned; yes/no used to introduce a new diagnosis; no sourced clinical indicators; no "Other" option; a dietitian note used as the sole basis for a yes/no query |
| CDI worklists and query policy | Choosing which cases to query | Queries sent only when the answer could raise the DRG, while documented MCCs without clinical support are never put to clinical validation |
| Provider sepsis documentation and payer denial letters | Coding sepsis and assessing denial risk | Sepsis removed or added by applying Sepsis-2 or Sepsis-3 criteria instead of the provider's statement (I.A.19); payer criteria treated as coding rules; R65.2- coded without linked organ dysfunction |
| POA indicators | HAC payment and quality data | POA set by the coder's assumption; a condition first diagnosed after the inpatient order marked Y; U left where the record or a query would settle it; ED conditions marked N |
| Operative reports, ICD-10-PCS codes and ventilator records | Surgical versus medical DRG; MS-DRG 870 | Root operation chosen from the surgeon's wording instead of the full PCS definition (B3.1a), so a non-O.R. code becomes O.R. or the reverse; integral steps coded separately (B3.1b); 5A1955Z reported without more than 96 consecutive hours of ventilation documented |
| Outpatient records from the 3 days before admission | Diagnoses and procedures on the inpatient claim | Preadmission diagnostic and related services in the payment window (42 CFR 412.2(c)(5)) left off the inpatient claim, or their CPT codes not converted to ICD-10-PCS; POA judged at outpatient registration instead of the inpatient order |
| Discharge disposition and transfer data | Full DRG versus per diem | Post-acute transfer from a qualifying DRG missed or invented; a discharge against medical advice treated as a transfer |
| Coding guideline section applied | Reporting uncertain diagnoses and findings | Section IV outpatient rules applied to an inpatient claim (dropping "probable" diagnoses), or II.H and III.C applied to an observation claim |

## Ground Rules

1. **Draft only.** Every output is a draft for a credentialed coder, a CDI specialist and compliance. Never state that a claim is final, billed or validated by a payer, and never send or word a query as sent.
2. **Source-review gate.** Do not call any documentation missing until every supplied document has been opened and searched, including scanned and oddly named files. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a code's exclusion not yet read in V44 Appendix C) or a policy election (for example a payer contract's sepsis definition or the facility's query policy).
3. **Hierarchy of authority.** For rules: ICD-10-CM conventions (Tabular and Index), then the Official Guidelines for the discharge year, the UHDDS definitions, the MS-DRG Definitions Manual for the grouper version, CMS manuals, then payer contracts and facility policy, which never override the classification. For facts: the patient's provider documentation governs; ancillary documentation is a clinical indicator except for the I.B.14 list; coder worksheets, encoder output, CDI worksheets and dashboards are secondary. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every code carries its provider statement with a locator (document, date, author role) or `[UNVERIFIED]`. Every rule carries its source and version, or `[VERIFY]`.
5. **Documentation-supported codes only.** The aim is the DRG the record supports. Never add a diagnosis no provider documented, select or resequence a principal diagnosis for payment, change a POA indicator without documentation, or ask a provider to document a condition. Each such request is a "Declined request" (Checkpoint A).
6. **Lock the version.** Select the grouper and the guideline year by discharge date and state both in the header. V44 and the FY 2027 Guidelines cover discharges from October 1, 2026.
7. **Principal diagnosis by Section II and UHDDS.** Apply "after study, chiefly responsible for occasioning the admission". Use II.B or II.C only when the facts make the conditions interrelated or equal, and record those facts; relative weight is never a reason.
8. **Secondary diagnoses by Section III.** A code needs a provider's statement and a Section III reason. Abnormal findings and ancillary notes become query candidates, not codes.
9. **Check exclusions and splits before claiming an impact.** Confirm the V44 severity, the Appendix C PDX collection and the family's split logic. Keep an excluded code on the claim when the rules require it.
10. **Compliant queries, chosen in both directions.** Draft queries to the ACDIS/AHIMA 2026 standard: neutral title, sourced indicators, no payment or quality language, multiple choice with "Other" to introduce a diagnosis. Select candidates on clinical indicators; a documented CC/MCC without support is a clinical validation candidate even when the answer could lower the DRG.
11. **Code to the provider's statement, not to a clinical definition.** Sepsis-2, Sepsis-3 and payer criteria do not add or remove a code; insufficient indicators lead to a clinical validation query, and a payer's definition goes to a denial-risk note.
12. **Outcome vocabulary.** These are fixed labels, used verbatim. Each code is Supported; Not supported, remove; Query candidate; Excluded as CC/MCC (still coded); or Declined request. The MS-DRG is stated with "provisional pending <facts>" when an open query or unread source could change it.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Review type: pre-bill, retrospective, CDI second-level, or record review for counsel.
2. Admission date, inpatient order date and time, discharge date, and discharge disposition.
3. Payer and, for non-Medicare FFS claims, the contract's payment basis and any clinical definitions it applies.
4. The record: H&P, progress notes, consults, operative reports, ventilator records, discharge summary, ED record, nursing, dietitian and social work notes, labs, imaging, MAR, and outpatient records from the 3 days before admission.
5. The draft or billed code set with POA indicators, and the grouper output.
6. Open or answered queries, and the facility query policy.

Defaults when an input is missing:

- Payer not stated: group under MS-DRG for the discharge date and mark the payer's payment basis as a policy election.
- POA indicators absent: assign them from the record per Appendix I and mark each U that a query could settle.
- No grouper output: group from the V44 Definitions Manual; mark any relative weight `[VERIFY]`.
- Query policy absent: apply the 2026 brief and name the gap.

Hard stops (do not state an MS-DRG):

- No discharge date and no way to identify the grouper version.
- No inpatient order or the claim is observation or outpatient: say MS-DRG review does not apply and route observation or conversion questions to managing-observation-stays and status denials to managing-coding-denials. No skill currently claims prospective 2-midnight status review; this skill does not perform one.
- No provider documentation supplied, only a code list or grouper output: list the documents needed and stop before validating.

Hard stop on the improper part (decline it as a "Declined request", then continue the compliant review):

- A request to add a diagnosis the record does not support, to keep one after the review shows it unsupported, or to query for one without indicators; a request to choose or resequence the principal diagnosis for payment, or to change POA without documentation.
- A request to lead a provider: a query or message that names the wanted diagnosis in its title, mentions DRG, MCC or payment, uses yes/no to introduce a diagnosis, or omits sourced indicators or "Other".

## Step 1: Frame the Question and Lock the Version

Read `references/drg-coding-rules.md`, Section 1, before anything else. Restate the question in one line, name the grouper version and guideline year from the discharge date, and note any worksheet or tip sheet built on an earlier version as a source to reconcile.

## Step 2: Build the Source Register and Code Ledger

Open every supplied document and complete the source register and code ledger in `references/output-template.md`, Section 2. For each code, find the provider statement that supports it and its locator. Where only an ancillary note, a lab value or a worksheet supports a code, mark it for Step 5.

## Step 3: Confirm Scope, Status and Payer Basis

Read `references/drg-coding-rules.md`, Sections 8 and 9. Confirm an inpatient order under 42 CFR 412.3 and that the inpatient guideline sections apply. Record the payer and its payment basis; a contract not read is a policy election. Apply the hard stops.

## Step 4: Validate the Principal Diagnosis

Read `references/drg-coding-rules.md`, Section 2. List each candidate with its admission evidence and the guideline that decides it (II.A to II.K), and complete `references/output-template.md`, Section 3. Replace a symptom code with the established related diagnosis. Reject any candidate that arose after the inpatient order. If the user asked for a principal diagnosis chosen by payment, record a Declined request.

## Step 5: Validate Secondary Diagnoses and POA

Read `references/drg-coding-rules.md`, Sections 3, 6 and 7. For each secondary code, confirm a provider statement and a Section III reason; apply the I.B.14 exceptions exactly. Code sepsis to the provider's statement and confirm organ-dysfunction linkage for R65.2-. Assign POA from the time of the inpatient order and check HAC categories. Remove unsupported codes and move their indicators to query candidates.

## Step 6: Check Severity, Exclusions and Group the Case

Read `references/drg-coding-rules.md`, Sections 4 and 5. For each CC or MCC, record the V44 severity, the PDX collection checked and the result, and the family's split. Check each procedure code against the operative report, the PCS root operation definition and its V44 O.R. status, since an O.R. procedure moves the case to a surgical DRG. Confirm that 5A1955Z rests on documented ventilation of more than 96 consecutive hours, and that procedures from the 3-day preadmission window are on the claim. Complete the grouping block in `references/output-template.md`, Section 5, and state the direction of change against the draft claim. Mark any code not confirmed in V44 `[VERIFY]` and say whether it could change the DRG.

## Step 7: Draft Query Candidates and Clinical Validation Items

Read `references/query-compliance.md`. Draft each candidate with the template in its Section 5: neutral title, sourced indicators, nonleading question, supported options, "Other". Add clinical validation candidates for documented diagnoses whose indicators look insufficient, whatever the DRG direction. Redraft any user-supplied query that fails the standard and record the original as a Declined request.

## Step 8: Check Disposition and Transfer

Read `references/drg-coding-rules.md`, Section 8. Confirm the discharge disposition against the discharge summary and case management notes, and whether a transfer rule applies; mark the FY 2027 qualifying list `[VERIFY]` unless read.

## Step 9: Reconcile, Hand Off and List Open Items

Complete the reconciliation table, declined requests, hand-offs, and open items (`references/output-template.md`, Sections 7 to 10). Check each rule relied on against `references/primary-sources.md` and carry its `[VERIFY]` flag into the output.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, for the claim and payer named, with the grouper version stated?
2. Does every code have a provider statement, and every removed code a reason?
3. Was the principal diagnosis chosen without reference to payment?
4. Were exclusions and the family's split checked before any impact was claimed?
5. Are query candidates compliant, and do they include clinical validation items that could lower the DRG?
6. Is every declined request named, with a compliant alternative?
7. Are open items owned, and is the DRG labeled provisional where they could change it?

## Quality Audit

1. The header names the grouper version and guideline year matching the discharge date.
2. The source register covers every supplied document; nothing is called missing without a search.
3. Every code in the ledger has a provider statement with a locator, or an outcome other than Supported.
4. The principal diagnosis analysis cites the Section II rule applied and lists rejected candidates.
5. No symptom code is principal when a related definitive diagnosis is established.
6. No CC or MCC rests on a lab value, vital sign or ancillary note alone, outside the I.B.14 list.
7. Every CC and MCC shows its V44 severity, the PDX collection checked and the family split.
8. Excluded codes remain on the claim when required, labeled Excluded as CC/MCC (still coded).
9. POA indicators follow Appendix I, and HAC categories are checked for N and U.
10. Sepsis codes follow the provider's statement and I.C.1.d; payer criteria appear only as a denial-risk note.
11. Every query candidate has a neutral title, sourced indicators, "Other", and no payment or quality language.
12. Every declined request, conflict and `[VERIFY]` item appears in its table.
13. The direction of change is stated, and the DRG is marked provisional when an open item could change it.

## Guidelines

- A DRG that goes down after review is a correct result. Report decreases with the same prominence as increases.
- A lab value or a nursing observation is evidence for a question, never an answer. The provider decides what it means.
- R65.2- can never be principal; when a severe sepsis code is excluded as an MCC with the sepsis principal, the organ dysfunction codes may still carry severity.
- The FY 2027 Z59 change affects severity, not reportability: housing codes from social work documentation are still reported.
- Medicare Advantage plans must follow 412.3 admission criteria, but their payment basis and clinical definitions come from the contract.
- Physician advisors who did not treat the patient cannot answer a query (2026 brief, Section VII).
- De-identify case identifiers in shared drafts and keep protected health information to what the review needs.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Grouper output and manual grouping disagree | Wrong version, wrong POA, or an exclusion missed | Re-run with the version for the discharge date; list each input that differs in the reconciliation table |
| Scanned or image-only notes | Text search missed them | Open and attempt OCR; if still unreadable, list them as unreadable and mark dependent codes provisional |
| Attending and consultant disagree on a diagnosis | Conflicting provider documentation | Do not pick one; add a reconciliation row and a query candidate to the attending |
| Discharge summary lists a diagnosis not found elsewhere | Copy-forward or late documentation | Treat it as the provider's statement unless it conflicts; flag clinical validation if indicators are absent |
| Code not found in the severity tables read | New FY 2027 code or unread page | Check Table 6A and the V44 Appendix C page; until read, mark `[VERIFY]` and show the DRG with and without it |
| Payer letter cites a clinical definition | Contract term, not a coding rule | Request the contract language; keep coding per the Guidelines; route the contract-definition dispute and any appeal to managing-coding-denials |
| User insists on a declined change | Pressure to reach a target DRG | Restate the rule once, keep the declined row, and note the compliance hand-off |

## Related Skills

- managing-cdi-programs: issuing, tracking and escalating the query candidates this review drafts.
- managing-clinical-documentation-improvement: program-level query metrics and documentation trends behind recurring DRG errors.
- managing-coding-denials: MS-DRG downgrade and clinical validation denials, payer or Medicare Advantage contract sepsis definitions (Sepsis-3 or Sepsis-2), inpatient-status and 2-midnight denials, and DRG validation appeals.
- conducting-false-claims-analysis: patterns of unsupported codes, one-way query policies, or overpayment and self-disclosure questions.
- auditing-coding-accuracy: sample-based coding audits across many claims.
- managing-observation-stays: observation status and conversion to inpatient. No skill currently claims prospective 2-midnight status review.
- managing-sepsis-bundles: SEP-1 abstraction, which uses its own sepsis criteria.
- managing-risk-adjustment-coding: HCC risk adjustment, which follows different rules from MS-DRG grouping.
- managing-payer-specific-coding: payer-specific coding policies and contract rules.
- abstracting-clinical-documentation: extracting codeable diagnoses and procedures from notes before grouping.

## Reference Files

- `references/drg-coding-rules.md`: version lock and FY 2027 changes, Section II and III rules, CC/MCC and exclusions, V44 families, sepsis, POA and HAC, status and transfers, guideline sections.
- `references/query-compliance.md`: ACDIS/AHIMA 2026 query rules, formats, when to query, declined requests, query template.
- `references/output-template.md`: deliverable sections, code ledger, grouping block, reconciliation table, hand-off table.
- `references/primary-sources.md`: each authority checked with date and what it supports, and the `[VERIFY]` list.
