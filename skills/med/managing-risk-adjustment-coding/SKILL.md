---
name: managing-risk-adjustment-coding
language: en
description: >
  Reviews Medicare Advantage CMS-HCC and ACA HHS-HCC risk adjustment coding for documentation
  support and RADV audit readiness. Validates each submitted or proposed ICD-10-CM diagnosis
  against the face-to-face encounter note, acceptable data source and provider type, telehealth
  rules (audio-video only for MA), signature and credentials, and the data collection period;
  applies ICD-10-CM Section IV outpatient rules, history-of rules for cancer and stroke, and the
  2024 CMS-HCC model (V28) with its hierarchies. Runs two-way retrospective chart reviews that
  delete unsupported codes as well as add supported ones, builds HCC and RAF impact tables and
  RADV support packets, and redesigns recapture and suspect-list prompts so providers evaluate
  rather than confirm. Use for HCC coding audit, RAF score validation, chart review, RADV
  preparation, V24 to V28 transition, MEAT or TAMPER documentation, unlinked chart review
  records, or HCC recapture. Drafts for coder, CDI and compliance review; never codes from
  problem lists.
tags:
  - management
  - medical-coding-and-billing
  - risk
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

# Managing Risk Adjustment Coding

Builds a documentation-supported risk adjustment coding review for one member, one chart review batch or one RADV sample: a source register, an encounter eligibility screen, a diagnosis-by-diagnosis validation table, HCC hierarchy and relative-factor impact, a two-way reconciliation of codes to submit and codes to delete, and, on request, a RADV support packet. Its aim is accurate payment: every code reflects a condition the provider evaluated at an eligible encounter, whether that raises or lowers the score. Everything it produces is a draft for review by a certified coder, a CDI specialist and the compliance officer; it is not a submission, a deletion, an attestation or legal advice.

## Why This Skill Exists

Risk adjustment converts diagnoses into payment. In Medicare Advantage the 2024 CMS-HCC model (V28) has governed 100 percent of non-PACE risk scores since payment year 2026, and CMS kept it for 2027 while excluding unlinked chart review diagnoses and audio-only diagnoses. CMS now aims to audit every eligible contract each payment year, and DOJ has resolved False Claims Act allegations over unsupported MA diagnoses for hundreds of millions of dollars, including $556 million from Kaiser affiliates in January 2026 over addenda adding diagnoses after visits. The errors are predictable: a condition lifted from a problem list, a cancer or stroke from years ago coded as current, a telephone visit or a radiology report treated as a valid source, a lower HCC counted beside a higher one, a V24 category used in a V28 year, and chart reviews that only add. This skill checks each of them against the record before any code moves.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Problem list, past medical history, medication list, superbill, carried-forward template | Leads to conditions the provider may have evaluated | Condition coded from the list alone with no assessment or plan at the visit (ICD-10-CM IV.J); copied-forward text read as evaluation; a drug on the medication list read as treatment of a condition the note never addresses |
| Vendor chart review file and the review's scope statement | Finding codes to submit and codes to delete | "Add-only" scope: unsupported submitted codes are seen and never deleted, or deletions are "out of scope"; the plan's duty to delete (MMCM ch. 7, §40) and Cigna's "failing to withdraw" settlement ignored |
| "History of" entries for cancer, stroke, myocardial infarction | Current versus historical condition | Treated cancer with no current treatment coded as active instead of Z85; past stroke without deficits coded I63 instead of Z86.73; I21 reported after four weeks; antiplatelet or statin read as active stroke treatment |
| Radiology, laboratory and pathology reports | Clinical indicators | Emphysema on a CT or a low eGFR coded without provider assessment; IV.K (coding a radiology claim) cited to make diagnostic radiology an acceptable risk adjustment source |
| Telehealth notes, visit modifiers and member's program | Face-to-face test; which program's rules apply | Audio-only (modifier 93 or FQ) counted for MA; a real-time audio-video visit (95) rejected; the MA audio-only rule applied to an ACA member, where HHS accepts certain audio-only codes; CMS-HCC numbers used in an HHS-HCC review |
| Notes by dietitians, nurses, medical assistants, home health or hospice | Supporting detail | Ineligible provider type or source treated as the diagnosing provider; BMI or "morbid obesity" from a dietitian coded without obesity documented by the patient's provider |
| Signature blocks, credentials and attestations | Record validity | Unsigned note; electronic signature without "signed by" or similar; no credential; someone other than the rendering provider signs or attests; an attestation used for an inpatient record |
| Dates of service and the payment year | Data collection period | A December visit counted for the wrong payment year; an inpatient stay whose discharge falls outside the period; RADV period confused with the current year |
| HCC list, RAF worksheet, interaction table | Score impact | Hierarchy ignored (HCC 224 and 226 both counted); interactions or count factors added before the hierarchy; V24 numbers and labels (HCC 85, 18, 21, 59) used for a V28 year; dollar figures without county rate or bid inputs |
| Pre-visit suspect lists, recapture reports, provider scorecards and incentives | Prompting evaluation of chronic conditions | A "confirm" checkbox that offers the diagnosis; prior-year HCCs pre-filled as this year's assessment; bonuses per closed gap; queries that lead to addenda months later (the Kaiser allegations) |
| Chart review records (linked and unlinked) and addenda | Correcting encounter data | Unlinked CRR diagnoses for 2026 dates of service relied on for 2027; a CRR linked to an unrelated encounter to keep a diagnosis; a late addendum adding a diagnosis not addressed at the visit |
| Contract, plan type and RADV status | Who is in scope and which rules apply | PACE, ESRD or ACA member run through the non-PACE MA model; the different-parent-organization switcher exception missed; overpayment reporting not suspended for a sampling-frame enrollee during a RADV audit, or suspended for one outside it |

## Ground Rules

1. **Draft only.** Every output is a draft for a certified coder, CDI specialist and compliance officer. Never state that a code was submitted, deleted, attested or validated by CMS, and never give legal conclusions.
2. **Source-review gate.** Do not call a record, signature or date missing until every supplied file has been opened and searched, including scans and oddly named files. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a code-to-HCC mapping not checked in the year's CMS file) or a policy election (for example the plan's late-entry policy).
3. **Hierarchy of authority.** For rules: statute and regulation (42 CFR part 422; 45 CFR 153.630 for ACA), then the Rate Announcement and HPMS memos for the payment year, then the RADV audit methods for the audited year, then Medicare Managed Care Manual chapter 7 where later documents are silent; the ICD-10-CM Official Guidelines and Coding Clinic govern code assignment; plan and vendor policies rank last. When a coding rule and a payment-eligibility rule point different ways (ICD-10-CM IV.K against the chapter 7 exclusion of diagnostic radiology), name both and apply the eligibility rule to risk adjustment. For facts: the signed encounter note's assessment and plan govern over other parts of the record, which govern over problem lists, claims, vendor files, suspect lists and dashboards. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every diagnosis carries its encounter, date, provider and credential, and the quoted supporting text with a page or line, or `[UNVERIFIED]`. Every rule carries its source and year, or `[VERIFY]`.
5. **Documentation-supported coding only.** Code what the eligible encounter supports, at the specificity it supports, and nothing else. Never add a diagnosis the record does not support, never select a code more specific than the documentation, and never let the factor value influence which code is chosen: compute RAF impact only after the determination.
6. **Two-way review.** Every retrospective review reads the same records for deletions as well as additions. Unsupported submitted codes are reported as Delete with the same prominence as additions. A review that only adds is not drafted.
7. **No coding from lists or reports alone.** A problem list, history, medication list, superbill, lab value or imaging report is a lead, never support. MEAT and TAMPER are evidence checklists, not rules; the rule is ICD-10-CM IV.J (the condition required or affected care at that visit).
8. **Lock the program, year and model.** State the program, payment or benefit year, model and blend, dates of service in scope and guideline year in the header (`references/hcc-model-and-coding-rules.md`, Section 1).
9. **Eligibility before diagnosis.** Screen each encounter for face-to-face or audio-video modality, acceptable source, acceptable provider type for the year, signature and credential, and date inside the period before reading its diagnoses.
10. **No documentation fixes.** Never suggest an addendum that adds a diagnosis not addressed at the visit, backdating, a signature or attestation by anyone other than the rendering provider, or linking a chart review record to an unrelated encounter. Genuine ambiguity becomes a non-leading query candidate routed to managing-cdi-programs.
11. **Outcome vocabulary.** Each diagnosis is Supported, Supported at a different code, Not supported, Ineligible source, or Cannot determine; each carries an action: Submit, Retain, Delete, Query candidate, or No action. "Cannot determine" names the missing fact and who can supply it.
12. **Route exposure; do not decide it.** Known unsupported codes that were paid, add-only history, incentive designs tied to capture counts, and prior-year error patterns go to conducting-false-claims-analysis with the facts and records. This skill does not opine on knowledge, materiality, damages or disclosure.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Program and segment: MA non-PACE, PACE, ESRD, or ACA individual or small group; contract or plan if known.
2. Payment year (MA) or benefit year (ACA), and the dates of service in scope.
3. Review type: prospective (pre-visit), concurrent (pre-submission), retrospective chart review, RADV preparation, or program design.
4. The record set: encounter notes with signature blocks, dates, provider names, credentials and specialties, visit modality and modifiers; inpatient records with admission and discharge dates.
5. The codes at issue: submitted diagnoses (encounter data, chart review records, MAO-004 or EDGE extract) and any candidate list from a vendor, suspect report or provider.
6. For RAF impact: the member's segment (community or institutional, dual status, aged or disabled) and the factor table to use.
7. RADV status: whether the contract was selected for the payment year and whether the member is in the sampling frame.
8. Plan policies: chart review procedure, query policy, amendment and late-signature policy.

Defaults when an input is missing:

- Review type not stated: run a two-way review.
- Segment not stated: show per-HCC factors for the Community, NonDual, Aged segment, labeled, and give no total risk score.
- Guideline year: chosen by date of service (FY 2027 from October 1, 2026).
- Provider specialty or credential missing: the encounter is Cannot determine for eligibility; request it.

Hard stops (do not issue the blocked determination):

- Program or payment or benefit year unknown: no model mapping, HCC assignment or RAF figure until it is supplied.
- No encounter record for a diagnosis this review is asked to validate or add (only a code list, problem list export, claim, superbill, vendor summary or suspect list): that diagnosis is Cannot determine; list the records needed; never recommend submitting it. A finding from the user's own completed audit may be carried forward, labeled "plan audit finding, not re-reviewed".
- Unsupported addition: a request to submit, add or retain a diagnosis the encounter record does not support. That code is Not supported; it is never added, and if already submitted its action is Delete.
- Problem-list-only support: a condition whose only support is a problem list, history, medication list, superbill or a report without provider assessment is not coded; it is Not supported, or a Query candidate when an eligible visit shows clinical indicators.
- Add-only scope: a request to review only for additions, or to submit additions while leaving unsupported submitted codes in place. Do not deliver an additions-only list; restate the scope as a two-way review of the same records and proceed only on that basis.
- Known unsupported, paid diagnosis with a request to leave it in place or not report it: stop on that item, state Delete and that 42 CFR 422.326 governs reporting and return, and route to conducting-false-claims-analysis.

Decline that part, then continue the review:

- Prompts that offer a diagnosis for confirmation, pre-filled assessments, or incentives per captured HCC: offer non-leading evaluation prompts instead.
- Addenda adding diagnoses after the visit, backdating, signatures or attestations by anyone other than the rendering provider, or linking a chart review record to an unrelated encounter.

## Step 1: Frame the Review and Lock the Model

Read `references/hcc-model-and-coding-rules.md`, Section 1. Restate the question in one line. Name the program, payment or benefit year, model and blend, dates of service window and guideline year. For MA payment year 2027 note the unlinked chart review and audio-only exclusions; for ACA name the HHS-HCC concurrent model and do not use CMS-HCC numbers.

## Step 2: Build the Source Register

Open every supplied file and complete the source register in `references/output-template.md`, Section 2: type, date of service, provider and credential, signature status. Mark problem lists, superbills, vendor files and suspect lists as leads, not support.

## Step 3: Screen Each Encounter for Eligibility

Read `references/hcc-model-and-coding-rules.md`, Section 2. For each encounter, test modality, source, provider type against the year's specialty list, signature and credential, and date. Record Eligible, Ineligible source (naming the failed test) or Cannot determine. A diagnosis from an ineligible encounter is not coded from that encounter, but look for the same condition at an eligible one.

## Step 4: Validate Each Diagnosis Against the Note

Read `references/hcc-model-and-coding-rules.md`, Sections 3 and 4. For every submitted and every candidate diagnosis, quote the assessment or plan text that shows the condition required or affected care at that visit. Apply IV.H to uncertain terms, the malignancy and stroke history rules, and IV.F.3 specificity. Assign the result and action from Ground Rule 11 and fill `references/output-template.md`, Section 4.

## Step 5: Map to HCCs, Apply Hierarchies and Compute Impact

Read `references/hcc-model-and-coding-rules.md`, Sections 5 and 6. Map Supported codes with the model year's CMS mapping (flag `[VERIFY]` where not checked), apply the hierarchy table, then show relative factors with segment and source. Sum after the hierarchy, state included and excluded components, and recompute totals with a script. Check every HCC number and label against the model in force; flag V24 categories.

## Step 6: Reconcile Two Ways

Read `references/radv-and-compliance.md`, Sections 1 and 2. Fill the two-way table in `references/output-template.md`, Section 6: Delete rows for unsupported submitted codes, Submit rows for supported codes not yet submitted (linked to the actual encounter), Query rows for clinical indicators without a documented diagnosis. Report counts in both directions in the summary.

## Step 7: Prepare the RADV Support Packet (When Asked)

Read `references/radv-and-compliance.md`, Section 3. For each audited HCC, keep its model-version label, choose the one best record, cite the supporting location and a fallback, and note record-validity risks. Note whether overpayment reporting is suspended for the member under the audit instructions.

## Step 8: Review Recapture and Query Workflows (When Asked)

Read `references/radv-and-compliance.md`, Section 4. Replace confirm checkboxes and pre-filled diagnoses with prompts that name the clinical indicator and ask for evaluation, including "not present" and "resolved". Update V24 labels to the model in force and drop conditions with no payment HCC from payment-driven prompts. Route query wording to managing-cdi-programs and incentive design to conducting-false-claims-analysis.

## Step 9: Close Out, Route and List Open Items

Complete the reconciliation, gaps, hand-offs and open items in `references/output-template.md`, Sections 8 to 11. Read `references/radv-and-compliance.md`, Section 5, and route each exposure fact. Check every rule relied on against `references/primary-sources.md` and carry its `[VERIFY]` flag into the output.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question for the program, year and model named in the header?
2. Does every diagnosis rest on quoted text from an eligible encounter, with nothing coded from a list or report alone?
3. Does the reconciliation show deletions as well as additions, with counts?
4. Are hierarchies applied before any sum, with V28 numbers for a V28 year?
5. Is anything phrased as advice to add, backdate, link or re-sign documentation? Remove it.
6. Is each exposure fact routed, with no legal conclusion drawn here?

## Quality Audit

1. The header names program, payment or benefit year, model and blend, dates of service and guideline year.
2. The source register covers every file with a status; nothing is called missing without a search.
3. Every encounter has an eligibility result naming each failed test.
4. Every diagnosis row quotes supporting assessment or plan text with a locator, or is Not supported or Cannot determine.
5. No code rests on a problem list, history, medication list, superbill, lab value or imaging report alone.
6. Cancer, stroke and myocardial infarction codes pass the history-of tests, with the test shown.
7. Uncertain diagnoses are coded to signs or symptoms under IV.H.
8. HCC numbers and labels match the model in force; hierarchies are applied; factors show segment and table; totals are recomputed.
9. The two-way table lists deletions and additions; no additions-only deliverable is produced.
10. Telehealth, provider type, signature, credential and date rules are applied per program (MA versus ACA).
11. No step suggests creating, backdating, re-signing or re-linking documentation; queries are non-leading and routed.
12. Exposure facts are routed to conducting-false-claims-analysis without conclusions on knowledge or damages.
13. Every `[VERIFY]` relied on appears in the open-items list with what would settle it.

## Guidelines

- HCCs do not carry forward. A chronic condition counts for a payment year only when evaluated and documented at an eligible visit in that year's dates of service.
- Diabetes HCCs 36, 37 and 38 carry equal factors in the 2024 model; a specificity change there serves accuracy, not payment.
- The CY 2027 exclusions do not make a linked chart review record valid by itself: the linked encounter's record must contain the support.
- A health risk assessment is a record type, not a shortcut; its diagnoses meet the same tests as any other visit.
- Per-member dollar figures depend on county rates, bids and plan factors; give them only with those inputs and label them illustrative.
- Keep protected health information to what the review needs; de-identify member identifiers in shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Only a code list or vendor spreadsheet supplied | Records not pulled | Hard stop for those diagnoses; list the encounters needed by date and provider |
| Scanned note unreadable or signature block cut off | Image quality or page missing | Attempt OCR; if still unreadable, mark Cannot determine and request the full page |
| Vendor HCC numbers do not match the model | V24 file or prior-year crosswalk | Re-map under the model in force; add a reconciliation row |
| Claim date and note date differ | Billing lag or wrong note attached | The note controls; add a reconciliation row; check the data collection period both ways |
| Note unsigned or signed without a credential | Signature pending or EHR export dropped the block | Request the signed version; Cannot determine until the rendering provider authenticates it under the late-signature policy; never another clinician |
| Provider specialty unclear (for example "provider" only) | Credential missing in signature | Look for the credential or specialty elsewhere in the note header; otherwise Cannot determine |
| User cites MEAT as the rule | Industry convention | Apply IV.J and quote the text; mention MEAT only as the checklist used |
| Member's program unclear | Mixed MA and ACA book | Ask; run nothing under a model until the program is known |

## Related Skills

- conducting-false-claims-analysis: False Claims Act risk, overpayment reporting and self-disclosure when unsupported codes were paid or a review only added codes.
- managing-cdi-programs: wording compliant, non-leading queries for clinical indicators without a documented diagnosis.
- managing-clinical-documentation-improvement: program-level documentation metrics behind recurring risk adjustment gaps.
- auditing-coding-accuracy: encounter coding audits beyond risk adjustment diagnoses.
- managing-compliance-audits: sampling methodology and corrective action plans for a coding audit program.
- coding-medical-encounters: assigning diagnosis and procedure codes for a visit outside a risk adjustment review.
- coding-telehealth-services: telehealth modifiers and place of service for audio-video and audio-only visits.
- managing-medical-records-compliance: amendment and late-entry policy questions.
- managing-drg-optimization: inpatient MS-DRG assignment, which follows different rules.
- legal-research: RADV appeals and litigation status; no dedicated skill covers RADV appeals.

## Reference Files

- `references/hcc-model-and-coding-rules.md`: model and period lock, encounter eligibility, Section IV rules, history-of tests, hierarchies and factors, V24 to V28 changes, ACA differences.
- `references/radv-and-compliance.md`: two-way review duty, chart review records and addenda, RADV methodology and status, recapture and query design, FCA routing, verified settlements.
- `references/output-template.md`: deliverable sections, eligibility screen, validation table, HCC impact, two-way reconciliation, RADV packet, hand-offs.
- `references/primary-sources.md`: each authority checked with URL, method and date, corrections, and the `[VERIFY]` list.
