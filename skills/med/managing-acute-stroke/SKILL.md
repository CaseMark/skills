---
name: managing-acute-stroke
language: en
description: >
  Reviews acute stroke care for one encounter and drafts a coordination, documentation and
  quality review for clinician and stroke-coordinator sign-off. Builds a timestamp ledger and
  clock block: last known well (LKW) versus symptom discovery, wake-up stroke, arrival,
  door-to-needle (DTN), door-in-door-out (DIDO) and door-to-puncture. Compares care with the
  AHA/ASA 2026 acute ischemic stroke guideline (alteplase or tenecteplase within 4.5 hours,
  extended-window imaging selection, blood pressure before and after thrombolysis,
  thrombectomy windows including large core and basilar occlusion, NIHSS, dysphagia screen)
  and the 2022 ICH guideline (blood pressure, anticoagulant reversal), and keeps that apart
  from Joint Commission STK-4, CSTK-01, CSTK-04 and STK-OP-1 abstraction and Target: Stroke
  goals. Flags outdated contraindication lists, late NIHSS, FDA label conflicts and transfer
  delays. Use for stroke alert review, stroke measure abstraction, code stroke audit or
  stroke documentation gaps. No patient orders.
tags:
  - management
  - emergency-medicine
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Acute Stroke

Builds a stroke care review for one encounter: a timestamp ledger from the source record, a clock block in which every window runs from its own trigger, a comparison with the AHA/ASA 2026 acute ischemic stroke guideline (or the 2022 ICH guideline), and, kept separate, a Joint Commission measure scorecard and Target: Stroke time figures. It also lists documentation gaps, compliant query candidates and hand-offs. Everything it produces is a draft for review by a clinician and a stroke coordinator or quality abstractor; it is not an order, an eligibility decision for a current patient or a final abstraction.

## Why This Skill Exists

Stroke reviews go wrong on clocks and versions more often than on care. Four frameworks speak about the same minutes: the 2026 AIS guideline (published January 26, 2026, replacing the 2018 guideline and its 2019 update), the FDA labels, the Joint Commission measures, and the AHA Target: Stroke goals. Each anchors its clock differently: last known well for thrombolysis and STK-4, symptom recognition for MRI-selected wake-up stroke, arrival for door-to-needle, IVT start for post-thrombolysis blood pressure. Order sets still carry the 2019 contraindication checklist, dashboards start the door at triage, and andexanet still appears in ICH order sets although US sales ended December 22, 2025. This skill keeps each framework, clock and version separate so the reviewer sees which one decides each finding.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| EMS run sheet, code stroke form, triage note | Last known well | Symptom discovery, the 911 call or arrival time copied as LKW; a wake-up stroke timed from waking instead of when the patient was last seen normal; a resolved earlier episode used instead of the most recent onset; a nurse's time preferred over a code stroke form or a physician entry |
| Wake-up or unknown-onset presentation | Extended-window thrombolysis | Called "outside the window, ineligible" without asking whether DWI-FLAIR or perfusion selection was considered; or treated as standard-window from the discovery time; each extended pathway's own trigger (recognition, midpoint of sleep, LKW) not computed |
| BP flowsheet around thrombolysis or thrombectomy | Blood pressure threshold at each time point | The pre-IVT 185/110 threshold (AIS 2026 §4.3 rec 5) applied after the bolus, where 180/105 (rec 7) governs for 24 hours; an ICH target (SBP 140, ICH 2022 §5.1) applied to ischemic stroke; an SBP below 140 target after IVT or successful EVT presented as guideline care; missed 15-minute checks in the first 2 hours |
| NIHSS flowsheet and notes | Severity, disabling-deficit decision, CSTK-01 | Item scores with no total read as a score; a total inferred from components; the first total charted after the needle; a modified or estimated NIHSS counted; a low score read as "not eligible" without a disabling-deficit assessment |
| Thrombolysis checklist, order set, drug label | Contraindications and agent | The 2019 absolute list (prior ICH, stroke within 3 months, DOAC within 48 hours) used for 2026 care where the 2026 table grades them relative; the TNKase label's 3-hour window or STEMI-only contraindications applied as stroke rules; a stroke tenecteplase dose above 25 mg (AIS 2026 §4.6.2; STEMI bands on the 2025 TNKase label go to 50 mg) |
| ED tracking board, registry dashboard, triage stamp | Door-to-needle and door-to-device | Door taken from triage, registration completion, stroke alert or CT time instead of the earliest documented arrival; one case called "Target: Stroke met" although the goals are hospital percentages; STK-4 scored from the door instead of LKW |
| Transfer record, both hospitals' charts | DIDO, EVT timing, who counts the case | DIDO from the transfer call or from CT; hub door-to-puncture started at the spoke; a thrombolytic given at the spoke counted in the hub's STK-4 numerator; repeat imaging at the hub treated as required |
| Anticoagulant history, INR, ICH order set | Reversal for hemorrhagic stroke | Reversal held for an INR result; the VKA threshold (INR 2.0, ICH 2022 §5.2.1) applied to a factor Xa inhibitor; andexanet listed as first line for US care after its withdrawal; the CSTK-04 INR cut-off (1.4) confused with a clinical threshold |
| MAR and swallow screen record | Dysphagia screen before oral intake; antithrombotic timing | Oral aspirin or other oral medicines given before the swallow screen; an antiplatelet started before the 24-hour post-IVT scan; dysphagia cited as an STK measure |
| Request, certification level, measure version | Scope: which framework, hospital and population | A CSTK measure applied at a primary stroke center; a 2019 guideline applied to 2026 care or the reverse; an ED transfer scored as an inpatient STK case; manual version not matched to the discharge date |

## Ground Rules

1. **Draft only; no orders.** Every output is a draft for a clinician and a stroke coordinator. Never phrase guideline content as an order for a patient: no doses, agents, rates or eligibility decisions for a current patient. State what the guideline says, what the record shows, and leave the decision to the treating team.
2. **Source-review gate.** Do not call a time, score, note or result missing until every supplied document has been opened and searched, including scanned and oddly named files. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a measure rule not confirmed in the current manual) or a policy election (for example the facility's choice of agent or BP protocol).
3. **Hierarchy of authority.** For clinical comparison: the guideline in force on the care date (AIS 2026 from January 26, 2026; ICH 2022), then the FDA label, then facility protocol; a label or protocol that differs is named as a conflict, never merged into "the standard". For measures: the Joint Commission manual version for the discharge date, then its data dictionary, then facility abstraction notes. For facts: primary entries (code stroke form, physician notes, MAR administration times, flowsheet readings, imaging timestamps) govern over dashboards, tracking boards and registry extracts. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every timestamp, score and quoted note carries a source locator (document, date and time, author role) or `[UNVERIFIED]`. Every clinical value carries its guideline, section and year, and every measure rule its manual version, or `[VERIFY]`.
5. **Name the framework on every conclusion.** Write "AIS 2026 §4.3 rec 7: not consistent", "STK-4 v2026B1: not in population", "Target: Stroke: DTN 50 minutes, within the 60-minute band". Never merge them into one pass or fail.
6. **Every clock runs from its own trigger.** Standard IVT and EVT from LKW; DWI-FLAIR selection from symptom recognition; wake-up perfusion selection from the midpoint of sleep; door-to-needle and DIDO from arrival; post-IVT blood pressure and neuro checks from IVT start; ICH reversal from diagnosis. Show each in the clock block from `references/output-template.md`.
7. **Compute LKW; never copy it.** List every LKW candidate with source and reject each one not used, with the reason. A wake-up stroke's LKW is when the patient was last known normal, not when the deficit was found.
8. **Contraindications from the right list.** For 2026 care, compare against the AIS 2026 risk gradient (Table 8), and report the order-set or label list as a separate row when it differs. Never present a relative item as an absolute bar or the reverse.
9. **No documentation fixes.** Never suggest adding, backdating or editing an entry to change a result. A late entry follows facility policy with its true entry time; an unclear entry becomes a neutral query candidate routed to `managing-cdi-programs`.
10. **Scope before scoring.** Confirm the hospital's certification level, whether it sent or received the patient, and the measure population before applying a measure. A thrombolytic counts only at the hospital that started it.
11. **Outcome vocabulary.** Guideline rows: Consistent, Not consistent, Not applicable, or Cannot determine. Measure results: Numerator, Not in numerator, Excluded, Not in population, or Cannot determine. Add "provisional pending <facts>" when an unchecked fact could change it. "Cannot determine" always names the missing fact and who can supply it.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Purpose: concurrent coordination on an open encounter, retrospective measure abstraction, quality or peer-review case review, transfer review, or record review for counsel.
2. Care dates and times, arrival and discharge dates (care date selects the guideline; discharge date selects the manual version).
3. Stroke type on imaging (ischemic, ICH, SAH, TIA, not established) and age.
4. Hospital certification level and role (sending or receiving), and which frameworks to apply. Default: guideline comparison plus the measures the hospital reports.
5. Record set: EMS run sheet, code stroke form, triage and ED notes, neurology or telestroke notes, NIHSS flowsheet, BP flowsheet, MAR, imaging reports with times, transfer records from both hospitals, swallow screen, order sets and the facility stroke protocol in force.

Defaults when an input is missing:

- Certification level unknown: score STK measures only and list CSTK measures as conditional on comprehensive-center status.
- Frameworks not stated: produce the guideline comparison and the STK-4 and Target: Stroke rows; offer the rest.
- Facility protocol not supplied: compare with the guideline only and mark protocol rows as an open policy election.
- Weight missing for a dose check: mark the dose row Cannot determine; never estimate a weight.

Hard stops (do not produce the dependent result):

- No documented LKW and no documented symptom discovery time: build the ledger, mark every window and STK-4 Cannot determine, and stop before any timing conclusion.
- Stroke type not established on imaging: do not apply ischemic thrombolysis or ICH reversal rules; list what imaging would settle it.
- Measure scoring requested with no discharge date or manual version: stop before measure results.
- Patient under 18: stroke measures exclude the case; route pediatric questions to `managing-pediatric-emergencies`.

Decline that part, then continue the review:

- A request for an order, dose, agent choice or eligibility decision for a current patient: offer the guideline comparison and the clinician questions instead.
- A request to create, backdate or alter documentation so a case passes: explain the late-entry policy and route genuine ambiguity to a compliant query.

## Step 1: Frame the Question, Stroke Type and Frameworks

Read `references/stroke-clinical-rules.md`, Section 1, and `references/measure-abstraction-rules.md`, Section 1. Restate the question in one line; name the stroke type, the guideline for the care date, the manual version for the discharge date, and the hospital's role. If the user's premise mixes frameworks ("STK-4 failed because DTN was over 60 minutes"), name the mismatch in the first line.

## Step 2: Build the Source Register and Timestamp Ledger

Open every document and complete the source register and ledger in `references/output-template.md`, Section 2. Record every candidate time for LKW, discovery and arrival with its source and time type. Where two sources differ, record both and add a reconciliation row.

## Step 3: Fix LKW and Write the Clock Block

Read `references/stroke-clinical-rules.md`, Section 2, and `references/measure-abstraction-rules.md`, Section 3. Choose LKW for the clinical review and, separately, apply the Time Last Known Well data element for measures (they usually agree; show it when they do not). Then compute every window from its own trigger and write the clock block.

## Step 4: Compare the Thrombolysis Decision With the Guideline

Read `references/stroke-clinical-rules.md`, Sections 3 and 4. Check glucose timing, the disabling-deficit assessment and NIHSS documentation, the window used, the agent and the documented dose against weight, consent documentation, and each contraindication against the 2026 gradient, with the order-set or label list in its own row. For wake-up or unknown onset, record whether DWI-FLAIR or perfusion selection was considered and when each pathway's window closed. Do not decide whether this patient should have been treated; report the comparison.

## Step 5: Compare Thrombectomy, Imaging Selection and Transfer

Read `references/stroke-clinical-rules.md`, Sections 6 and 7. Record occlusion site, NIHSS, prestroke mRS, ASPECTS or PC-ASPECTS, the window from LKW, and the recommendation tier each fact places the case in, including large-core criteria. For transfers, compute DIDO from spoke arrival and door-to-puncture from hub arrival, and note any repeat imaging at the hub.

## Step 6: Review Blood Pressure, Monitoring and Early In-Hospital Care

Read `references/stroke-clinical-rules.md`, Sections 5 and 8. Test each BP reading against the threshold for its time point and list readings above it; test check frequency against the schedule from IVT start; compare any facility BP target with the guideline. Check the swallow screen against the first oral intake, including oral medicines, and the first antithrombotic against the 24-hour post-IVT scan.

## Step 7: Hemorrhagic Stroke Branch

Read `references/stroke-clinical-rules.md`, Sections 5 and 9. Record anticoagulant, last dose, renal function and INR with times; time from diagnosis to reversal start; the agent used against the 2022 recommendation and its current US availability; BP against the ICH targets. Route agent choice and restart timing to `managing-anticoagulation-therapy`.

## Step 8: Score the Measures

Read `references/measure-abstraction-rules.md`, Sections 2 to 7. Confirm the population and scope, then score each requested measure with its own clock, showing STK-4 Timing I and Timing II in minutes. Report Target: Stroke figures in minutes and bands; report STK-OP-1 as minutes in its stratum.

## Step 9: Reconcile, List Gaps and Hand Off

Complete the reconciliation table, gaps and query candidates, hand-offs and open items (`references/output-template.md`, Sections 6 to 9). Check each rule relied on against `references/primary-sources.md` and carry its `[VERIFY]` flag into the output.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, with each framework on its own row and named with its version?
2. Is LKW computed with rejected candidates listed, and does every window run from its own trigger?
3. Are contraindications compared with the list for the care date, with label and order-set conflicts named?
4. Does any result depend on a `[VERIFY]` item, and would it change if that item reads differently?
5. Is anything phrased as an order, a dose for a patient, or advice to change documentation? Remove it.
6. Are open items owned, with a next action?

## Quality Audit

1. The header names stroke type, hospital role and certification level, the guideline for the care date and the manual version for the discharge date.
2. The source register covers every supplied document; nothing is called missing without a search.
3. Every ledger entry has a value, time, time type and source locator.
4. The clock block shows LKW with rejected candidates, and each window with its own trigger.
5. Wake-up or unknown-onset cases show every extended pathway's window and whether it was considered.
6. Each BP reading is tested against the threshold for its time point; post-IVT readings use 180/105 from IVT start.
7. NIHSS rows show each documented total with its time against the IVT or EVT start; component scores are not summed into a total.
8. Contraindications are compared with the AIS 2026 gradient, and label or order-set differences have their own rows.
9. Door-to-needle and DIDO start at the earliest documented arrival; STK-4 uses LKW; single cases are not called Target: Stroke passes.
10. Measure scope is checked: certification level, sending or receiving hospital, population and exclusions.
11. ICH reviews show reversal timing from diagnosis, the agent against the 2022 guideline and current US availability, and the CSTK-04 INR rule kept apart from clinical thresholds.
12. No patient-directed dose, agent or order appears; no step suggests altering documentation.
13. Every `[VERIFY]` relied on appears in the open-items list with what would settle it.

## Guidelines

- Time is the variable that decides most findings; state minutes, not adjectives.
- A low NIHSS does not end the thrombolysis question; the 2026 guideline turns on whether the deficit is disabling (AIS 2026 §4.6.1, Table 4).
- Tenecteplase and alteplase are both COR 1 within 4.5 hours (AIS 2026 §4.6.2); the STK-4 data element counts both.
- Intensive SBP lowering below 140 is not guideline care after IVT (no benefit) or after successful EVT (harm) (AIS 2026 §4.3 recs 8 and 10).
- A wake-up stroke is not automatically ineligible; it is a different clock.
- Measures and guidelines disagree by design (STK-4: treat within 180 minutes of LKW; guideline: 4.5 hours). Report both.
- Keep protected health information to what the review needs; de-identify case identifiers in shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Three different LKW times | EMS, nurse and physician each recorded one | List all; apply the clinical rule and the measure hierarchy separately; route the conflict to a query candidate if a physician time is absent |
| Scanned EMS sheet or code stroke form | Text search missed it | Open it and attempt OCR; if unreadable, list it and set dependent windows to Cannot determine |
| Dashboard DTN differs from the chart | Tool uses triage or alert time | The earliest documented arrival controls; add a reconciliation row naming the tool's rule |
| NIHSS totals conflict | Different examiners or times | List each total with examiner and time; use the first total for CSTK-01 and the pre-treatment total for the guideline comparison |
| Order set predates 2026 | Version drift | Compare with AIS 2026 and list each differing line; for care before January 26, 2026, compare with the 2019 update |
| Records from only one hospital in a transfer | Other chart not supplied | Score only what this chart shows; list the other hospital's times as still needed |
| ICH patient on an unknown anticoagulant | Medication list incomplete | Record the gap as an unknown fact; do not infer the agent from an INR |

## Related Skills

- interpreting-neuroradiology: ASPECTS, core volume, perfusion mismatch and hemorrhage reads behind an eligibility question.
- managing-anticoagulation-therapy: reversal agent choice, DOAC timing and anticoagulant restart after stroke.
- managing-atrial-fibrillation: anticoagulation decisions behind STK-3 and cardioembolic stroke.
- managing-hypertensive-emergencies: blood pressure management outside the stroke thresholds covered here.
- coordinating-emergency-transfers: transfer process and DIDO delays beyond the timestamps.
- managing-emtala-compliance: transfer obligations when a stroke patient is sent from the ED.
- managing-quality-reporting: hospital rates, sampling, submission and data validation.
- managing-accreditation-compliance: certification program requirements beyond single-case measures.
- managing-cdi-programs: compliant queries for ambiguous LKW, stroke type or NIHSS documentation.
- documenting-informed-consent: consent or emergency-waiver documentation for thrombolysis or thrombectomy.
- managing-speech-therapy-assessments: swallow evaluation after a failed bedside screen.
- managing-pediatric-emergencies: patients under 18.
- conducting-mortality-reviews: case review of a stroke death beyond process timing.
- medical-record-chronology: a litigation chronology when counsel needs the full timeline rather than a review.

## Reference Files

- `references/stroke-clinical-rules.md`: AIS 2026 and ICH 2022 content: clocks with triggers, agents and doses, 2026 risk gradient and label conflicts, BP by time point, EVT windows, transfer, early care, reversal.
- `references/measure-abstraction-rules.md`: Joint Commission version lock, populations, LKW and arrival data elements, STK-4 logic, CSTK-01, CSTK-04, STK-OP-1, Target: Stroke goals.
- `references/output-template.md`: deliverable sections, timestamp ledger, clock block, guideline comparison, measure scorecard, reconciliation table, hand-off table.
- `references/primary-sources.md`: each authority checked with URL, method and date, corrections, and the `[VERIFY]` list.
