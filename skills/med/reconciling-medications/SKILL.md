---
name: reconciling-medications
language: en
description: >
  Drafts a medication reconciliation worksheet and prescriber discrepancy list across care
  settings: admission, external transfer in or out, discharge hand-off, and outpatient or ED
  encounters. Builds a best possible medication history (BPMH) from two or more sources
  (interview, bottles, fill history, outside MAR) and compares it with orders, the
  discharge list and summary. Flags single-source lists, fill data taken as proof of use, omitted
  OTC drugs, supplements, inhalers, patches and PRN drugs, dose, route and frequency
  mismatches, duplication after formulary substitution, holds not resumed, renal dose cuts not
  revisited, the patient's own supply, allergy conflicts, list versus summary conflicts,
  look-alike/sound-alike names, and high-alert anticoagulants, insulin and opioids. Applies
  NPG.14.05.01 (hospitals, 2026; NPSG.03.06.01 elsewhere), WHO High 5s, AHRQ MATCH and 42 CFR
  482.43(b). In-stay order continuity goes to reconciling-inpatient-medications. Draft for
  prescriber review; writes no orders.
tags:
  - reconciliation
  - pharmacy
  - patient-safety
metadata:
  author: casemark
  practice_areas:
    - Clinical Pharmacy
    - Pharmacy
  document_types:
    - Reconciliation Report
  skill_modes:
    - Reconciliation
    - Verification
---

# Reconciling Medications

Builds a medication reconciliation worksheet for one patient at one cross-setting transition (admission, external transfer in or out, discharge hand-off, or an outpatient or ED encounter): a source register, a best possible medication history (BPMH) with each line's verification status, a comparison against the orders or discharge list at that transition, and a prioritized discrepancy list written as neutral questions for the prescriber. Everything it produces is a draft for review by a pharmacist or the responsible prescriber. It never writes, changes or signs an order, and it never decides whether a discrepancy was intended.

## Why This Skill Exists

Transitions are where medication lists break. WHO High 5s reports that up to 27 percent of hospital prescribing errors trace to incomplete or inaccurate admission medication histories, with omission of a regular medicine the most common error. The Joint Commission puts medication errors in acute hospitals at about 6.5 per 100 admissions. Most reconciliation failures are not judgment errors; they are list errors: a home list copied from one fill feed, a substitute drug left running beside the home drug, a hold that nobody lifted, a discharge list that disagrees with the discharge summary. On January 1, 2026 the Joint Commission moved hospitals and critical access hospitals from National Patient Safety Goals to National Performance Goals, so the hospital requirement is now NPG.14.05.01, while other programs still use NPSG.03.06.01. This skill makes every source visible, labels every difference, and leaves every clinical decision to the prescriber.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Pharmacy fill or claims history | A BPMH source | Used as the only source; a recent fill treated as proof the patient takes the drug, including auto-refills after a prescriber stopped it; samples, VA or mail-order fills, cash fills elsewhere and OTC products missing from the feed |
| Prior discharge list, SNF transfer form, after-visit summary | Starting point for the home list | Copied forward as the BPMH, carrying its errors and missing every change since that date |
| Patient or caregiver interview | What the patient actually takes | Doses stated from memory ("about 40 units") entered as confirmed; OTC drugs, supplements, inhalers, patches, eye drops, weekly or monthly injectables and PRN drugs never asked about |
| Admission or transfer orders against the BPMH | The comparison at admission or transfer | Matching by drug name only, so dose, route, frequency or formulation mismatches (ER versus IR, weekly versus daily methotrexate) pass as matches |
| Therapeutic interchange records | Explaining an inpatient substitute | Substitute continued at discharge while the home drug is also resumed, producing a duplicate (two anticoagulants, two PPIs) |
| Hold orders and the inpatient MAR | Medications paused for a procedure, AKI or NPO | A hold with a resume condition never lifted, so the drug is missing from the discharge list with no stop documented |
| Discharge medication list, discharge summary, prescriptions | What the patient and the next provider receive | The list and the summary disagree on a drug or dose; the next provider gets a pointer to the EHR instead of an actual list |
| EHR reconciliation module entries | Recording what was continued, changed or stopped | A "discontinue, intentional" checkbox with no reason accepted as a documented decision |
| Drug names across sources | Matching lines across lists | Look-alike/sound-alike pairs (hydrALAZINE and hydrOXYzine, HumaLOG and HumuLIN) read as the same drug or silently corrected |
| Patient's own medications brought in | Home supply kept at the bedside or used under a self-administration order | Patient takes the home supply beside the hospital-issued substitute, or self-administers without an order, so the MAR understates what was taken and the BPMH and orders both look complete |
| Renal or hepatic dose changes made during the stay | Doses cut for AKI or liver injury | The reduced dose carried onto the discharge list after creatinine recovered, or the home dose resumed while function is still impaired, with no note either way |
| Allergy and intolerance records | Screening each line on every list | A drug on the admission or discharge list conflicts with a documented allergy, or allergy lists differ across sources, and nobody flags it |
| High-alert medications (anticoagulants, insulin, opioids, sulfonylureas, oral methotrexate) | Lines that need individual review | Batch-accepted with routine lines; duplicate opioids, or two acetaminophen-containing products, not caught |
| The request, the accreditation program and who decides | Scope, the standard cited, and who resolves discrepancies | The skill asked to write orders, finalize the list, pick the drug or attest compliance; an in-stay unit transfer handled here instead of by reconciling-inpatient-medications; NPSG.03.06.01 cited for a 2026 hospital, or NPG.14.05.01 for a nursing care center; a pharmacist's or tool's label treated as the prescriber's decision |

## Ground Rules

1. **Draft only.** Every output is a draft for a pharmacist or the responsible prescriber. Never write, rewrite or sign orders or prescriptions, never state a dose, start, stop, resume or switch for this patient, and never call the list final or reconciled.
2. **Source-review gate.** Do not call a medication, dose or document missing until every supplied document has been opened and searched, including scanned and oddly named files. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a requirement not confirmed for the organization's program) or a policy election (for example who the facility names as the qualified individual).
3. **Hierarchy of authority.** For requirements: the CMS Condition of Participation and its interpretive guidance, then the accreditation standard for the organization's program, then facility policy, then WHO High 5s and AHRQ MATCH as guidance. For facts: administration records and dated prescriber notes govern over summaries, transfer forms, order-set defaults and auto-generated lists. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every medication line, dose and reason carries a source locator (document, date and time, author role) or `[UNVERIFIED]`. Every requirement cited carries its standard and year, or `[VERIFY]` as listed in `references/primary-sources.md`.
5. **Two sources or a label.** Every BPMH line is Confirmed, Single source or Conflicting sources. A home list built from one source type is labeled single source at the top of the worksheet.
6. **Dispensed is not taken.** A fill, a bottle or a prior list shows what was dispensed or intended. Only the patient, a caregiver or an administration record shows use, and even then say which.
7. **No reason, no intent.** A difference is Documented change only when a source states the reason. A checkbox, a default or the bare word "intentional" leaves it an Unexplained discrepancy for the prescriber to classify.
8. **Questions, not answers.** Each discrepancy list item ends in a question the prescriber can answer either way. Never word it to suggest the answer.
9. **High-alert lines one at a time.** Reconcile each anticoagulant, insulin, opioid, sulfonylurea, oral methotrexate and other ISMP high-alert line individually and give it its own detail block.
10. **Use the vocabulary verbatim.** Row status: Match, Documented change, Unexplained discrepancy, Cannot determine. Verification: Confirmed, Single source, Conflicting sources. Priority: Critical, High, Moderate, Low. Definitions are in `references/reconciliation-rules.md`.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Transition point: admission, external transfer in, external transfer out, discharge, or an outpatient or ED encounter, with date and time. An in-stay transfer (ICU to floor, service change, post-op resumption) goes to reconciling-inpatient-medications.
2. Setting and accreditation program (hospital, critical access hospital, SNF, home care, clinic), so the right standard is cited.
3. Every available source for the home regimen: interview notes, bottles or photos of labels, fill or claims history, clinic notes, prior discharge list, transfer form, outside MAR, PDMP report.
4. The list to compare: admission orders; for an outpatient or ED encounter, the medications given or changed at the visit; for transfer out, the transfer medication list and sending MAR; for discharge, the active inpatient orders, the inpatient MAR, the discharge medication list, the discharge summary and any prescriptions.
5. Hold orders, therapeutic interchange records and procedure notes for the stay.
6. Allergies with reactions, from every source; any patient's-own-medication or self-administration orders; age; weight, renal and hepatic values, and pregnancy or lactation status where documented.
7. Who will review the output (pharmacist, prescriber) and the next provider for a discharge or transfer out.
8. Two patient identifiers (for example name and date of birth, or record number) as they appear on each source.

Defaults when an input is missing:

- Setting or program not stated: cite NPG.14.05.01 only if the documents show a hospital; otherwise name both standards and mark the program an unknown fact.
- Only one source for the home regimen: build the BPMH, label the list single source, and list the sources to obtain.
- No discharge summary at discharge: compare against the discharge list and orders, and list the summary as still needed.
- Identifiers not shown on the sources: write "not checked: identifiers not supplied" in the header field and list it as an unknown fact; this is not a hard stop.
- Organ-function values missing: say renal and hepatic dosing was not reviewed; do not assume doses are appropriate.

Hard stops (do not produce the comparison or the discrepancy list):

- No compared list at all (no orders, no transfer orders, no discharge list): produce the BPMH worksheet and the source register only, labeled "comparison not run".
- The transition point cannot be identified from the request or the documents: ask, because the comparison pair depends on it.
- The only transition is an in-stay transfer (ICU to floor, service change, post-op resumption): route to reconciling-inpatient-medications.
- A source carries a patient name, date of birth or record number that conflicts with the other sources: exclude it, say why, and continue only if the remaining sources still identify the patient.

Decline that part, record it in the Declined part section with its fixed label (`references/output-template.md`, Section 12), then continue with the worksheet:

- A request to write orders, prescriptions or an order set for the next facility (Declined: order writing).
- A request to pick the drug, the dose or which duplicate to keep (Declined: drug or dose selection).
- A request to mark discrepancies intentional or fill in reasons (Declined: intent classification).
- A request to finalize or sign the list without the prescriber's documented decision (Declined: finalizing the list).
- A request to attest or document that an accreditation or CMS requirement was met (Declined: compliance attestation).

## Step 1: Frame the Transition and the Standard

Read `references/transition-requirements.md`, Sections 1 and 7. Restate in one line the transition, the comparison pair (`references/reconciliation-rules.md`, Section 5), the setting and the standard that applies (NPG.14.05.01 for a 2026 hospital, NPSG.03.06.01 for programs that still use it). Note any facility policy supplied on who reconciles and when.

## Step 2: Register Every Source

Open every document and complete the source register (`references/output-template.md`, Section 2). Check two patient identifiers on each source and record the result in the header field for the identifier match. Record the date of each source; a list is only as current as its date. Say whether the home regimen rests on one source type.

## Step 3: Build the BPMH

Read `references/reconciliation-rules.md`, Sections 1 to 4. Enter every product from every source, including OTC drugs, supplements, inhalers, patches, drops, weekly or monthly injectables, samples and PRN drugs, with strength, formulation, dose, route, frequency, indication and last dose. Label each line Confirmed, Single source or Conflicting sources. Where a fill appears without confirmation of use, or the patient reports a dose that no label or prescriber confirms, say so on the line. Check names against the ISMP confused-name pairs (Section 10) before merging lines.

## Step 4: Compare at the Transition Point

Read `references/reconciliation-rules.md`, Sections 5 to 7 and 11. Build the comparison worksheet with one row per medication across the baseline and every compared list. Compare drug, strength, dose, route, frequency and formulation, not names alone. Assign each row a status and, where it is not Match, a discrepancy type. For each substitute, hold and new order, look for the reason in the notes and cite it; trace every interchange forward to the discharge list, every hold forward to a resume or a documented stop, and every renal or hepatic dose change forward to the discharge list with the latest organ-function value. Check for the patient's own supply at the bedside and any self-administration order.

## Step 5: Review High-Alert Lines and Shared Ingredients

Read `references/reconciliation-rules.md`, Sections 8 to 10. Give each high-alert line with any item its own detail block. Check for two drugs of one class and for products sharing an ingredient (acetaminophen in opioid combinations and OTC products); compute the largest daily amount the listed sigs allow and report it without setting a limit. Check every line on every list against each documented allergy and complete the allergy check (`references/output-template.md`, Section 7); send interaction grading to `assessing-drug-interactions`.

## Step 6: Write the Discrepancy List

Assign each item a priority from `references/reconciliation-rules.md`, Section 8. Write what each source says with locators, why the item is flagged, and one neutral question for the prescriber, with an owner (`references/output-template.md`, Sections 5 to 8). Put source and document conflicts in the reconciliation table, naming the stronger evidence and why, while still asking the prescriber to confirm.

## Step 7: Check the Hand-Off (Discharge, Transfer Out, Outpatient)

Read `references/transition-requirements.md`, Sections 2 and 6. For a discharge or transfer out, complete the discharge information check: an actual reconciled list going to the next provider, changes marked, OTC and herbal products included, allergies listed, written information for the patient, and agreement among the discharge list, summary and prescriptions. For an outpatient or ED encounter, check the written information EP 4 requires when the regimen changed (only the new drug when a short-term drug was the only change).

## Step 8: Gaps, Hand-Offs and Sign-Off

Complete the gaps and open items, the hand-off table, any Declined part entries and the reviewer sign-off (`references/output-template.md`, Sections 10 to 13). Check each requirement relied on against `references/primary-sources.md` and carry its `[VERIFY]` flag into the output.

## Checkpoint B: Post-Draft Alignment

1. Does the worksheet cover the transition asked about, with the right comparison pair and the right standard for the program?
2. Does every source supplied appear in the register, and every product from every source appear in the BPMH?
3. Is any line labeled Confirmed on one source, or any difference labeled Documented change without a stated reason? Fix it.
4. Does any sentence read as an order, a dose, a start, a stop or a choice between drugs? Rewrite it as a question.
5. Are the discharge list and the discharge summary compared with each other, not only with the BPMH?
6. Does every open item have an owner and a next step?

## Quality Audit

1. The header names the transition, comparison pair, setting, the standard cited for the program and year, and the patient-identifier match across sources.
2. The source register lists every document supplied with a status, and states whether the home list rests on one source type.
3. Every BPMH line has strength, dose, route, frequency, formulation where relevant, a source locator and a verification label.
4. OTC drugs, supplements, inhalers, patches, drops, injectables on long intervals, samples and PRN drugs were asked about or are listed as not asked.
5. No fill, bottle or prior list is presented as proof of current use.
6. Every comparison row compares dose, route, frequency and formulation, not names alone, and uses the status vocabulary verbatim.
7. Every Documented change cites the reason and its locator; no checkbox or default counts as a reason.
8. Every interchange is traced to the discharge list and every hold to a resume or a documented stop.
9. Look-alike/sound-alike pairs found across sources are named and left as Conflicting sources for the prescriber.
10. Every high-alert line with an item has a detail block and Critical priority; duplicate classes, shared ingredients and documented allergies are checked, with any combined daily amount computed and every allergy conflict in the allergy check.
11. At discharge, the discharge list, discharge summary and prescriptions are compared with each other, and the discharge information check is complete.
12. No sentence directs therapy or attests compliance; every discrepancy item ends in a neutral question with an owner; every declined request carries its fixed label.
13. Every `[VERIFY]` relied on appears in the open items with what would settle it.

## Guidelines

- The prescriber, or the qualified individual the facility names, resolves discrepancies; the worksheet only surfaces them.
- A good-faith effort to gather the history meets NPG.14.05.01 EP 1 intent, but the worksheet still shows which sources were tried and which were not available.
- WHO's 24-hour reconciliation goal after admission is guidance; facility policy sets the deadline.
- Pregnancy letter categories were removed from prescription labeling under the FDA PLLR; describe the labeling concern instead.
- Renal, hepatic and pharmacokinetic dosing questions go to the skills built for them; this worksheet notes the values and the question.
- Keep protected health information to what the review needs; de-identify shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Patient cannot be interviewed and no caregiver is reachable | Acuity, sedation, cognition | Build from other sources, label lines Single source, and list the interview as still needed at the next opportunity |
| Fill history and interview disagree | Stopped drug still auto-filling, or patient taking it differently | Mark Conflicting sources, show both, and ask which reflects use |
| Scanned or photographed labels or lists | Text search misses them | Open them, attempt OCR, and if still unreadable list them as unreadable with dependent lines Cannot determine |
| Outside transfer list disagrees with the outside MAR | Transfer form typed from memory or an old list | Treat the MAR as stronger evidence of what was given, record the conflict, and ask the prescriber to confirm with the sending facility |
| EHR module shows every home drug as "continued" | Default selection | Compare line by line against orders; a default is not a decision |
| Two discharge documents disagree | Summary written before late changes, or list auto-generated | Record both in the reconciliation table and put the item on the discrepancy list |
| Organization's program unclear | Hospital-based clinic, SNF unit, home care arm | Name both standards and mark the program an unknown fact |

## Related Skills

- assessing-drug-interactions: grading drug-drug, drug-food and drug-disease interactions on the reviewed list.
- managing-anticoagulation-therapy: duplicate anticoagulant, switch-rule and periprocedural timing review.
- managing-atrial-fibrillation: choosing an anticoagulant for atrial fibrillation when a duplicate or interchange leaves the agent open.
- managing-diabetes-mellitus: insulin regimen questions raised by an insulin item.
- converting-medication-routes: IV-to-oral changes and opioid equianalgesic questions raised by an opioid item.
- managing-renal-dose-adjustments: dose questions tied to creatinine clearance or eGFR.
- reviewing-medication-safety: system-level high-alert medication safeguards behind a recurring item.
- managing-patient-safety-events: reporting a discrepancy that reached the patient.
- managing-adverse-drug-reactions: classifying a reaction found while taking the history.
- summarizing-discharge-notes: the patient-facing discharge summary once the prescriber has decided each item.
- coordinating-care-transitions: post-discharge follow-up of the reconciled list and readmission prevention after the hand-off.
- reconciling-inpatient-medications: in-stay order continuity only (ICU to floor, post-op resumption, service change, hold and resume during the stay). This skill owns the BPMH and every cross-setting comparison: admission, external transfer in and out, discharge hand-off, and outpatient or ED encounters.
- medical-record-chronology (the legal skill medical-record-chronology): a litigation chronology when counsel needs the full medication timeline rather than a worksheet.

## Reference Files

- `references/reconciliation-rules.md`: medication definition, BPMH sources and labels, interview prompts, comparison pairs, status vocabulary, discrepancy types, priority tiers, high-alert and confused-name lists, substitution and hold rules.
- `references/transition-requirements.md`: which accreditation standard applies, NPG.14.05.01 and NPSG.03.06.01 elements, WHO High 5s, AHRQ MATCH, CMS 482.43(b) and A-0810, hierarchy of authority.
- `references/output-template.md`: header, source register, BPMH and comparison worksheets, discrepancy list, high-alert detail, reconciliation table, discharge check, hand-off table, sign-off.
- `references/primary-sources.md`: each authority checked with URL, method and date, corrections, and the `[VERIFY]` list.
