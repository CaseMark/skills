---
name: managing-chemotherapy-protocols
language: en
description: >
  Verifies chemotherapy and other antineoplastic orders against the regimen, order set version
  and product labels, and reviews protocol adherence and safety documentation for pharmacists,
  oncology nurses and quality reviewers. Recomputes BSA from verified height and weight
  (Mosteller or the order set's formula), flags stale or estimated weights and BSA capped at
  2.0 m² without a documented reason (ASCO obesity dosing guideline), checks carboplatin Calvert
  dosing and the 125 mL/min GFR cap, builds lifetime anthracycline cumulative-dose ledgers that
  include outside facilities and earlier lines, confirms cycle day, interval and lab hold
  parameters, and audits the ASCO-ONS four verifications, oral chemotherapy orders, vincristine
  and vinca alkaloid minibag and intrathecal safety (ISMP), and USP <800> handling. Use for
  chemo order verification, double check, dose calculation check, cumulative dose, protocol
  deviation review or chemotherapy safety audit. Drafts for clinician review; never writes or
  changes orders.
tags:
  - management
  - pharmacy
  - treatment
metadata:
  author: casemark
  practice_areas:
    - Clinical Pharmacy
    - Pharmacy
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Chemotherapy Protocols

Builds a verification and protocol-adherence review for one antineoplastic order or treatment course: a source register, a regimen and version match, the dosing variables with their sources, a dose comparison table that sets each ordered dose beside the protocol-expected dose, a cumulative-dose ledger, cycle and clearance checks, route and handling checks, and the record of independent verifications. Everything it produces is a draft for a pharmacist, an oncology nurse and the prescriber. It never writes, chooses or changes a dose, and it never releases a product or signs a verification.

## Why This Skill Exists

ISMP treats antineoplastics as high-alert medications: an error is more likely to cause serious harm. Most chemotherapy errors are not exotic. A weight from last quarter, a BSA quietly capped at 2.0 m², a carboplatin dose computed from an uncapped creatinine clearance, a cumulative anthracycline total that starts at this hospital, a treatment calendar that never moved after a delayed Day 1, or a vincristine syringe sent to the procedure room with the intrathecal methotrexate. Each one passes a glance at the order. The ASCO-ONS administration safety standards (2024) answer with standardized order content and four separate verifications, and ISMP and the product labels add route and weight rules. This skill applies those checks in a fixed order and keeps three kinds of authority apart: the institution's order set and protocol (which govern the order), the product labels (which state what the manufacturer and FDA approved), and organization-level standards such as ASCO-ONS, ISMP and USP <800> (which govern process and documentation, not the clinical dose).

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Height and weight entries (flowsheet, order header, prior encounter) | BSA and mg/kg doses | A stated, estimated or prior-encounter weight used as the dosing weight; pounds entered as kilograms; no two-person verification at the start of a new plan; a weight change past the order set's recalculation trigger ignored |
| BSA field and dose calculation in the order | BSA-based doses | BSA capped at 2.0 m² or dosed on ideal or adjusted weight with no documented clinical reason; a formula or rounding rule different from the order set |
| Serum creatinine, lab eGFR, carboplatin order | GFR for the Calvert formula | GFR not capped at 125 mL/min where the order set caps it; an eGFR in mL/min/1.73 m² put straight into the formula; a very low creatinine taken at face value; a measured clearance used where the order set specifies an estimate; carboplatin read as mg/m² |
| Cumulative-dose tracker, outside records, earlier regimens | Lifetime anthracycline and anthracenedione totals | The tracker starts at this facility or this line of therapy; another facility's doses, pediatric treatment, a trial, or another anthracycline left out, although the labels say to include them |
| Treatment calendar, MAR, cycle and day field | Correct day of cycle and interval | Calendar built from the planned Day 1, not the actual one; a delay never rolled forward; Day 8 parameters applied on a Day 1 |
| Lab results and the order set's hold and modify parameters | Clearance to treat | Labs collected outside the window; thresholds taken from a generic table instead of the regimen; bilirubin or renal parameter not checked; a hold parameter met with no documented decision to treat |
| Oral antineoplastic prescriptions (specialty pharmacy, home supply) | The oral part of the regimen | Prescribed outside the EHR order set; refills not zero; days on and off missing; not on the medication list; never reaches the verification workflow |
| Vinca alkaloid and intrathecal products, labels, delivery plan | Route safety | Vincristine in a syringe; intrathecal and intravenous products delivered together; the label lacks "for intravenous use only, fatal if given by other routes" |
| Order set version, published regimen, trial protocol amendment | Protocol adherence | Order set built on a superseded version or amendment; an exception order with no second-practitioner authorization or recorded rationale; a research regimen without IRB approval on file |
| Verification records and signer roles | Proof of the independent checks and who may perform them | One person's check entered twice; the second checker worked from the first checker's numbers; the fourth (bedside) verification missing; a signer outside the roles the organization approved; a request to sign a check after the fact |

## Ground Rules

1. **Draft only.** Every output is a draft for a pharmacist, an oncology nurse and the prescriber. Never write, choose, round or change a dose; never release a product; never state that an order is verified or safe to give.
2. **No orders, ever.** Every dose figure is labeled "protocol-expected, for comparison" or "as ordered". A request such as "what dose should she get" is answered with the comparison and routed to the prescriber.
3. **Source-review gate.** Do not call a weight, lab, prior dose or signature missing until every supplied document has been opened and searched, including scans and outside records. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a label statement not confirmed for this manufacturer) or a policy election (for example the facility's tolerance or recalculation threshold).
4. **Hierarchy of authority.** For the order: the institution's current order set or the trial protocol, then the product label, then published regimen literature. Organization standards (ASCO-ONS, ISMP, USP <800>) govern process and documentation and never set a clinical dose. For facts: measured, dated source entries (flowsheet, lab report with collection time, MAR, outside records) govern over trackers, calendars, order headers and summaries. Name every conflict in the reconciliation table; never resolve one silently.
5. **Citation discipline.** Every value carries a source locator (document, date and time, author role) or `[UNVERIFIED]`. Every rule carries its source and edition (order set version, label revision date, ASCO-ONS 2024 standard number) or `[VERIFY]`.
6. **Compute; never copy.** Recompute BSA, GFR, Calvert doses, cumulative totals and cycle days from source variables and show the arithmetic. A calculated field in the order is a claim to check.
7. **Never estimate a dosing variable.** A missing height, weight, creatinine or prior-dose record makes the dependent element "Cannot verify".
8. **Do not impose or remove a cap.** BSA caps, vincristine maximums and GFR caps come from the order set or protocol. Where the order set is silent, show both readings and classify the question as a policy election.
9. **Route safety is never a judgment call.** A vinca alkaloid in a syringe, or an intravenous and an intrathecal product prepared or delivered together, is "Critical: escalate now", stated in the first line of the output.
10. **No attestation.** Never sign, complete or backdate a verification, a weight check or a cumulative-dose entry, and never suggest editing a record to make a review pass. A check that did not happen is reported as not documented.
11. **Outcome vocabulary.** Agent level: Consistent, Discrepancy, Not applicable, Cannot verify. Order level: No discrepancies found, Clarification required before preparation, Critical: escalate now, Cannot complete verification. Retrospective review: Adherent, Deviation with documented rationale, Deviation without documented rationale, Cannot determine. A timed check whose trigger has not yet occurred is "Not yet due". Add "provisional pending <facts>" when unchecked facts could change a result.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Review type: prospective order verification, pre-administration check, or retrospective protocol-adherence or safety review.
2. The order or orders under review: each drug, dose, unit, route, rate, days, cycle and day number, signature date and prescriber.
3. The regimen reference: the institution order set with version and effective date, the trial protocol and amendment, or the published regimen the order cites.
4. Dosing variables with dates and sources: height, weight (and whether two-person verified for a new plan), serum creatinine with collection time, and any other variable the order set uses.
5. Labs the order set's hold parameters name, with collection times.
6. Treatment history: actual administration dates for this course, prior lines of therapy, outside-facility records and any cumulative-dose tracker.
7. Preparation and administration records when the question concerns them: pharmacy log, labels, verification entries with signer roles, delivery plan for intrathecal doses.
8. Facility policies the order set relies on: weight and BSA rules, rounding, dose-variance tolerance, recalculation threshold.

Defaults when an input is missing:

- Facility tolerance, rounding or recalculation rule not supplied: report the raw difference and classify the rule as a policy election; do not adopt a number.
- No outside records but history suggests prior treatment: build the ledger from what is supplied, mark the total "provisional pending outside records" and name who can supply them.
- BSA formula not named: compute Mosteller, say so, and flag the formula as a policy election.

Hard stops:

- No order for the agent at issue: stop and list what is needed; do not reconstruct an order from a summary or a calendar.
- No regimen reference (order set, protocol or cited published regimen): do not score dose or protocol adherence; produce the source register and the intake list only.
- A dosing variable an agent depends on is missing or undated (height, weight, serum creatinine for carboplatin, prior anthracycline doses for a cumulative check): set that element to "Cannot verify"; do not estimate it.

Decline that part, then continue with the rest of the review:

- A request to choose, write or change a dose or regimen for a patient: give the comparison and route the decision to the prescriber.
- A request to sign, complete or backdate a verification or documentation entry: explain that the record must reflect what was done; report the gap.

## Step 1: Frame the Review

Restate the question in one line and name the review type and the order set version. Read `references/output-template.md` and set up the header and Section 1. If the user says "the protocol" while the order set and the published regimen differ, name the difference in the first line.

## Step 2: Build the Source Register and Match the Regimen

Open every supplied document and complete the source register. Compare the order element by element with the order set and with any published regimen or protocol the order set cites: drugs, dose per unit, route, rate, days, cycle length, number of cycles, supportive care and hold parameters. Read `references/safety-standards.md`, Sections 1 and 2, for exception orders, research regimens and required order elements, and record any element the order lacks.

## Step 3: Verify the Dosing Variables

Read `references/dose-verification-rules.md`, Sections 1 to 3, before calculating. Record height and weight with date, source, unit and whether two-person verified for a new plan; compare with the prior weight. Recompute BSA with the order set's formula and rounding; identify any cap or alternative weight and whether a clinical reason is documented. For carboplatin, recompute GFR by the order set's method, apply the order set's cap, and compute the Calvert dose; if the order set is silent on the cap, show both doses.

## Step 4: Compare Each Dose

Fill the dose comparison table in `references/output-template.md`, Section 5, using `references/dose-verification-rules.md`, Section 7: protocol dose per unit, the variable used, the protocol-expected dose for comparison, the dose as ordered, and the difference in mg and percent against the order set's tolerance. A documented dose reduction is checked against the protocol's dose levels; an undocumented one is a discrepancy.

## Step 5: Build the Cumulative-Dose Ledger

Read `references/dose-verification-rules.md`, Section 4. For each agent with cumulative toxicity, list every prior dose by date and source, including other facilities, earlier lines and other anthracyclines or anthracenediones. Compute the total after this dose and set it beside the label statement for that agent with the label's revision date, and the latest LVEF or other monitoring result. Never convert between anthracyclines without a sourced ratio.

## Step 6: Check Cycle Day, Interval and Clearance to Treat

Read `references/dose-verification-rules.md`, Sections 5, 6 and 8. Find the actual administration date of Day 1 of the current cycle in the MAR, count the day of cycle on the planned date, and compute the next Day 1. Apply the hold and modify parameters the order set states for that day to labs collected within its window. Each timed check uses its own trigger from the table in Section 8.

## Step 7: Check Route, Handling and Oral Therapy

Read `references/safety-standards.md`, Sections 3, 4, 6, 7 and 8. Check vinca alkaloid containers and labels, intrathecal separation and delivery, oral antineoplastic prescriptions (in the EHR order, quantity, refills, schedule, medication list), hazardous-drug labeling and CSTD use for administration. A route-safety failure goes to the first line of the output as "Critical: escalate now".

## Step 8: Audit the Verification Record

Read `references/safety-standards.md`, Sections 5 and 9. For the two-person height and weight check and each of the four verifications, record whether the required elements are documented, who signed, each signer's role, the time, and whether the checks were independent. Report missing or non-independent checks as found; never complete them.

## Step 9: Reconcile, Classify Gaps and Hand Off

Complete the reconciliation table, the hand-offs and the open items (`references/output-template.md`, Sections 10 to 12). Check each rule relied on against `references/primary-sources.md` and carry any `[VERIFY]` flag into the output. Set the order-level disposition last.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, for the order and order set version named?
2. Is every dose figure labeled "protocol-expected, for comparison" or "as ordered", with no instruction to give a dose?
3. Are BSA, GFR, Calvert doses, cumulative totals and cycle days recomputed from dated source variables, with the arithmetic shown?
4. Does every cap, tolerance or threshold applied come from the order set, protocol or label, with policy elections named where none does?
5. Is any route-safety failure in the first line as "Critical: escalate now"?
6. Are open items owned, with a next action, and does each result that rests on a `[VERIFY]` item say so?

## Quality Audit

1. The header names the order set version and effective date, the review type and each standard with its edition.
2. The source register covers every supplied document; nothing is called missing without a search.
3. Height and weight carry date, unit, source and two-person status; stale, stated or estimated weights are flagged.
4. BSA is recomputed with the named formula and rounding; any cap or alternative weight is tied to a documented reason or flagged.
5. Carboplatin rows show creatinine with collection time, the GFR method, the cap applied and its source, and the dose in mg.
6. Each ordered dose sits beside its protocol-expected comparison with the difference in mg and percent.
7. The cumulative ledger includes every source of prior doses, states the total after this dose, and cites the label with its revision date.
8. Cycle day is counted from the actual Day 1 and the hold parameters used are those for that day.
9. Oral antineoplastics are checked for EHR ordering, quantity, refills and schedule.
10. Vinca alkaloid container, label and intrathecal separation are checked, and any failure is the first line of the output.
11. The verification table records signers, roles, times and independence and contains nothing completed on anyone's behalf.
12. Every conflict is in the reconciliation table, every gap is classified, and every `[VERIFY]` relied on is in the open-items list.

## Guidelines

- The order set governs the order; the label states what was approved; ASCO-ONS, ISMP and USP <800> govern the process. Report each in its own place.
- ASCO 2021 recommends full weight-based dosing of cytotoxic chemotherapy regardless of obesity. A cap can still be a legitimate prescriber decision; the finding is the missing reason, not the cap itself.
- The Calvert formula yields mg. A lab eGFR is indexed to 1.73 m² and is not the GFR the formula expects unless the order set says how to convert it.
- A "2 mg vincristine maximum" is protocol content. Check the order against the protocol in use; the label does not set one.
- Concurrent review of a course in progress is provisional: a check whose trigger has not occurred is "Not yet due", never a discrepancy.
- Keep protected health information to what the review needs and de-identify shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Two weights on the same day | Stated and measured weights, or pounds and kilograms | List both with source and unit; use the measured, verified metric weight; add a reconciliation row; flag a 2.2-fold difference |
| Order set and published regimen disagree | Superseded version or local modification | Show each difference with its source; check for a documented exception order; route the question to the prescriber and the pharmacy and therapeutics owner |
| Outside records are scanned or illegible | Image-only faxes | Attempt OCR; if still unreadable, list the record as unreadable and mark the cumulative total provisional |
| Lab shows only eGFR, no creatinine | Interface displays the calculated value | Request the creatinine and collection time; set the carboplatin element to "Cannot verify" until supplied |
| Treatment calendar and MAR disagree | Calendar not updated after a delay | The MAR administration date controls; recompute the cycle day and next Day 1 |
| Verification fields signed but times identical | One person completed both, or a template default | Record as "independence not shown"; ask for the audit trail |
| Oral agent appears only on a specialty pharmacy label | Prescribed outside the order set | Record the missing EHR order elements; route reconciliation of the home supply |

## Related Skills

- managing-chemotherapy-toxicity: CTCAE grading and the toxicity-driven choice of a dose level.
- managing-oncologic-emergencies: tumor lysis, cord compression and other emergencies found during review.
- managing-renal-dose-adjustments: renal adjustment of supportive and non-antineoplastic medications.
- managing-hepatic-dose-adjustments: Child-Pugh assessment when a hepatic parameter drives a change.
- interpreting-echocardiograms: LVEF results behind a cumulative anthracycline decision.
- reconciling-medications: home oral antineoplastics and supplements across care settings.
- assessing-drug-interactions: interactions with oral agents and supportive medications.
- managing-adverse-drug-reactions: hypersensitivity and infusion reactions and their causality.
- managing-patient-safety-events: reporting a wrong-route, wrong-dose or wrong-day event or near miss.
- reviewing-medication-safety: program-level high-alert medication safeguards and root cause analysis.
- managing-workplace-safety-healthcare: USP <800> hazardous drug program compliance beyond a single order.
- managing-medication-use-evaluations: protocol-adherence audits across many patients.
- managing-drug-shortages: substitutions when a regimen drug is unavailable.
- coordinating-multidisciplinary-cancer-care: sequencing chemotherapy with surgery and radiation.

## Reference Files

- `references/dose-verification-rules.md`: height, weight and BSA rules, caps, Calvert formula and GFR cap, cumulative-dose label statements, cycle day, hold parameters, dose comparison, time-bound checks with their triggers.
- `references/safety-standards.md`: ASCO-ONS 2024 order elements, exception orders, oral therapy, labeling, the four verifications, intrathecal and vinca rules, ISMP best practices, USP <800>, who may do what.
- `references/output-template.md`: deliverable sections, dose comparison table, cumulative ledger, verification record, reconciliation table, hand-off table.
- `references/primary-sources.md`: each authority checked with URL, method and date, what is current as of 2026-10-30, corrections, and the `[VERIFY]` list.
