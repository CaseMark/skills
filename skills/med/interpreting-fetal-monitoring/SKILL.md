---
name: interpreting-fetal-monitoring
language: en
description: >
  Interprets intrapartum electronic fetal monitoring (EFM, fetal heart rate tracing, CTG strip)
  and reviews its charting using the 2008 NICHD definitions and the three-tier Category I,
  II and III system, applying the ACOG guidance in force on the date of care (Clinical Practice
  Guideline No. 10, October 2025, which replaced Practice Bulletins 106 and 116). Measures
  baseline and variability over 10-minute windows, accelerations by gestational age (15 x 15 at
  32 weeks or later, 10 x 10 before 32 weeks), early, late, variable and prolonged decelerations
  by the 30-second rule and nadir timing, recurrence against contractions in 20-minute windows,
  and tachysystole averaged over 30 minutes. Flags maternal heart rate recorded as fetal, paper
  speed and clock mismatches, and Category II risk features. Supports
  concurrent documentation, quality and peer review, and retrospective medical-legal strip
  review with an outcome-blind first pass. Drafts for clinician review; no orders, standard-of-care
  or causation opinions.
tags:
  - analysis
  - obstetrics-and-gynecology
metadata:
  author: casemark
  practice_areas:
    - Obstetrics
    - Gynecology
    - Maternal-Fetal Medicine
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Fetal Monitoring

Produces a segment-by-segment interpretation of an intrapartum fetal heart rate (FHR) tracing in NICHD 2008 terms: baseline, variability, accelerations, decelerations, uterine activity, and a Category I, II or III label for each timed segment, with the Category II features that raise or lower concern. For a completed labor it adds a clinical timeline, a comparison of charted interpretations with the tracing, and a record of responses against the guidance in force on the date of care. Every output is a draft for review by a qualified obstetric clinician; it is not an order, a standard-of-care opinion or a causation opinion.

## Why This Skill Exists

Nearly 90 percent of laboring patients in the United States have electronic fetal monitoring, and more than a quarter of primary cesareans are for nonreassuring fetal status (ACOG CPG No. 10, 2025). The NICHD 2008 nomenclature is precise, but reading against it is not: interobserver agreement is modest, Category II holds every tracing that is neither Category I nor Category III whatever its risk, and a handful of measurements (a 30-second onset, a nadir after the contraction peak, half of the contractions in 20 minutes, a 30-minute contraction average) decide the label. In retrospective review two further errors dominate: reading a tracing knowing the baby was injured, and judging 2024 care by 2026 guidance or the reverse. ACOG CPG No. 10 replaced Practice Bulletins 106 and 116 in October 2025 and changed points that reviewers rely on, including maternal oxygen. This skill makes every label traceable to a measurement and every rule traceable to the document in force.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| External Doppler segments, especially the second stage | The fetal heart rate itself | Maternal heart rate recorded as fetal: "accelerations" with each push or contraction, a rate matching the maternal pulse, or a sudden drop when a scalp electrode is applied; the earlier segment is then labeled Category I |
| The 10-minute baseline window | Baseline rate, tachycardia, bradycardia | Baseline read during decelerations or accelerations or from under 2 minutes of identifiable baseline; a 2-to-10-minute prolonged deceleration called bradycardia, or a 10-minute fall left as a "deceleration" |
| Variability amplitude | Variability class and the Category I or III line | 5 bpm called moderate; minimal called absent; amplitude measured across decelerations; a 1 cm/min strip read with 3 cm/min habits |
| Deceleration waveform against the contraction channel | Early, late, variable or prolonged | Onset-to-nadir not timed against the 30-second rule; late decelerations called early because they "mirror" contractions without checking the nadir against the peak; variable label given to a fall under 15 bpm or 15 seconds |
| Contraction count in the deceleration window | Recurrent versus intermittent | Recurrence counted by minutes or by "frequent" instead of 50 percent or more of contractions in a 20-minute window |
| Contraction record over 30 minutes | Tachysystole | One 10-minute block treated as decisive in either direction; tachysystole not qualified as with or without decelerations; "hyperstimulation" used |
| Gestational age and dating | Acceleration threshold | The 15 x 15 rule applied before 32 weeks, so a qualifying acceleration or induced response is reported as absent |
| Category II tracing | Level of concern and response | Category II treated as one risk level; CPG 10 Box 3 higher-risk features (recurrent late or variable, more than one prolonged deceleration, unexplained tachycardia, prolonged minimal variability) and protective features (moderate variability, accelerations) not listed |
| The guidance and policy in force on the date of care | Which rules and responses apply | CPG 10 applied to 2015 care, or PB 116 oxygen advice applied to 2026 care; facility documentation intervals ignored; an ACOG document treated as the legal standard of care, which it disclaims |
| Outcome data and the request letter in retrospective review | Context for the reviewer | Hindsight bias: the tracing read after the cord gas is known; the requested conclusion ("confirm Category III") adopted; a standard-of-care or causation opinion given that belongs to a qualified expert |
| EFM archive, EHR flowsheet and annotation times | Timeline of recognition and response | Clocks not aligned; late entries treated as contemporaneous; strip features read without medications, maternal vitals or labor stage |
| Twin or dual-channel tracings | Which fetus is being interpreted | One twin recorded twice; channels swapped between segments |

## Ground Rules

1. **Draft only.** Every output is a draft for a qualified obstetric clinician. Never present it as a final interpretation, a peer review finding, an expert opinion or an order.
2. **Source-review gate.** Do not call a segment, note or event missing until every supplied file, page and strip panel has been opened and searched, including scanned images. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a rule not confirmed in the guidance in force) or a policy election (for example the facility documentation interval).
3. **Hierarchy of authority.** For definitions: NICHD 2008 as restated in the ACOG document in force on the date of care, then facility policy for documentation and protocols. For facts: the tracing with its own timestamps governs over flowsheet summaries, charted categories and later narratives; the MAR and flowsheet govern medications and maternal vitals. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every tracing feature carries a strip locator (date, clock range, panel or page, mode) or `[UNVERIFIED]`. Every rule carries its source and year, or `[VERIFY]`.
5. **Confirm the signal before reading it.** A segment with maternal heart rate indicators that cannot be resolved is "Not categorized (signal source not confirmed)".
6. **Measure, then label.** Show the numbers behind each label: onset-to-nadir seconds, nadir minus contraction peak, recurrence fraction, 30-minute contraction average, amplitude range, gestational-age threshold. Measure time from printed time marks, never from an assumed paper speed.
7. **Categorize by segment.** Assign a category to each timed segment, last, after the components. List Category II higher-risk and protective features from CPG 10 Box 3 whenever the label is Category II.
8. **Outcome-blind first.** In retrospective work, interpret the tracing before opening outcome data, record that pass, then reconcile. Never infer a tracing feature from the outcome.
9. **Date of care decides the guidance.** Apply the ACOG document and facility policy in force when the care happened, and say which one.
10. **No orders, no verdicts, no record changes.** Never direct care for a patient, never state that care met or breached the standard of care or caused an injury, and never draft, backdate or alter a note or annotation.
11. **Outcome vocabulary.** Segment labels are Category I, Category II, Category III, or Not categorized (with the reason). Feature labels use NICHD terms verbatim; legacy terms are quoted and mapped, never adopted.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Purpose: concurrent documentation support, quality or peer review, or medical-legal review for counsel.
2. Date or dates of care, and the facility policies in force then (documentation interval, oxytocin protocol, escalation chain).
3. Gestational age on each date and its dating source.
4. The tracing: digital archive export or paper strips with time marks, paper speed and vertical scale, and the clock times at issue.
5. Monitoring mode for each segment: external Doppler or fetal scalp electrode; tocodynamometer or intrauterine pressure catheter; any maternal heart rate channel; twin channels.
6. Clinical timeline: labor stage and exams, membrane status, medications with times and rates, maternal pulse, blood pressure, temperature and SpO2, position changes, notifications, decision and delivery times.
7. Clock sources: EFM system time, EHR time, and any anchor event recorded in both.
8. For retrospective work: whether outcome data are in the file (to be set aside until the outcome-blind pass is done).

Defaults when an input is missing:

- Gestational age missing or near 32 weeks: report acceleration findings under both thresholds.
- Paper speed or scale unstated: measure only from printed time marks and record the speed as unknown.
- Tocodynamometer only: count contractions and time peaks, and note that intensity and resting tone are not measured.
- Facility policy missing: test documentation timing only as a policy-election gap.
- No clock anchor: keep EFM and EHR times in separate columns, unaligned.

Hard stops (do not assign a category to the affected segment):

- No tracing or tracing data, only narrative notes or a charted category: produce the source register and the list of what is needed.
- No usable time reference (no time marks and no export timestamps): no timing-dependent label.
- Maternal heart rate indicators in a segment that the record cannot resolve: label it Not categorized (signal source not confirmed).

Decline that part, then continue with the interpretation:

- A request for orders or real-time management for a current patient. Say a bedside clinician must decide; if the description includes Category III criteria, tell the user to escalate to the responsible clinician now.
- A request to add, alter or backdate a note or tracing annotation.
- A request to state that care met or breached the standard of care, or caused an injury; route it to a qualified expert.
- A request to confirm a pre-set conclusion; give the actual reading and record the request as a conflict.

## Step 1: Frame the Question and the Guidance in Force

Read `references/retrospective-review-rules.md`, Section 1. State the purpose, the dates of care, the ACOG document in force for each date and the facility policies supplied. If care falls between Sept. 18 and Oct. 31, 2025, show both documents and treat the choice as a policy election.

## Step 2: Build the Source Register, Timeline and Clock Offset

Use `references/output-template.md`, Sections 2 and 3. Open every file. Record each strip's paper speed and scale or export settings. Find an anchor event in both the EFM and EHR clocks and state the offset; read `references/retrospective-review-rules.md`, Section 3 for entry-time and late-entry handling.

## Step 3: Confirm the Signal and Tracing Quality

Read `references/nichd-definitions-and-categories.md`, Sections 6 and 7. For each segment compare the recorded rate with the maternal pulse at the same time, look for accelerations with pushing or contractions, and note mode changes, gaps, double- or half-counting and twin duplication. Segments that fail stay Not categorized.

## Step 4: Assess Uterine Activity

Read `references/nichd-definitions-and-categories.md`, Section 4. Count contractions in each 10-minute block, show the 30-minute average, and label tachysystole with or without associated decelerations. Log contraction onset, peak and end times; Step 7 needs the peaks.

## Step 5: Determine Baseline and Variability per 10-Minute Window

Read `references/nichd-definitions-and-categories.md`, Sections 1 and 2. Exclude periodic and episodic changes, confirm at least 2 minutes of identifiable baseline, round to 5 bpm, and classify variability by the amplitude range. Decide prolonged deceleration versus baseline change by the 10-minute rule.

## Step 6: Identify Accelerations by Gestational Age

Apply the threshold for the documented gestational age on the tracing date (Section 3 of the definitions file). Record peak, onset-to-peak and duration. For stimulation tests, record the stimulus time and whether an acceleration meeting the threshold followed.

## Step 7: Classify Each Deceleration and Its Recurrence

Fill the deceleration log in `references/output-template.md`, Section 5. For each one: onset-to-nadir against 30 seconds, nadir time minus contraction peak, depth and duration. Then count decelerations of each type against the contractions in each 20-minute window and state recurrent or intermittent with the fraction.

## Step 8: Assign a Category per Segment

Apply Section 5 of the definitions file. Category III needs absent variability with recurrent late, recurrent variable decelerations or bradycardia, or a sinusoidal pattern; Category I needs every Category I criterion; everything else is Category II with its Box 3 features listed. Name any NICHD 2008 versus CPG 10 wording difference that a reader might rely on (Section 8).

## Step 9: Retrospective Layer (When the Labor Is Complete)

Read `references/retrospective-review-rules.md`, Sections 2, 4 and 5. Record the outcome-blind result, then open outcome data and list any reading that changes, with the tracing feature that supports it. Compare each charted interpretation with the tracing for the same window. Place each response on the timeline with its own trigger: finding, recognition, notification and action. Describe guidance content as guidance in force; do not grade the care.

## Step 10: Reconcile, List Gaps and Hand Off

Complete `references/output-template.md`, Sections 8 to 10. Check each rule relied on against `references/primary-sources.md` and carry any `[VERIFY]` flag into the open items.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, for the segments asked, with a category per timed segment?
2. Is the guidance named for the date of care, and is every rule sourced?
3. Was the signal confirmed fetal for every categorized segment?
4. Does every label show its measurement, and was time taken from time marks?
5. In retrospective work, was the outcome-blind pass recorded before outcome data were used?
6. Is anything phrased as an order, a standard-of-care verdict, a causation opinion or a documentation change? Remove it.

## Quality Audit

1. The header names the NICHD 2008 nomenclature, the ACOG document in force on each date of care and the facility policies supplied.
2. Every segment has a clock range, a monitoring mode and a category or a Not categorized reason.
3. Each categorized segment passed the maternal heart rate check, and any unresolved segment is Not categorized.
4. Baseline rests on at least 2 minutes of identifiable baseline in its 10-minute window, and no prolonged deceleration is labeled bradycardia.
5. Variability classes match the amplitude ranges (absent, minimal 5 bpm or fewer, moderate 6-25, marked over 25).
6. Accelerations use the threshold for the documented gestational age, or both thresholds are shown.
7. Each deceleration shows onset-to-nadir seconds and nadir timing against the contraction peak; variable decelerations meet 15 bpm and 15 seconds.
8. Recurrence is a fraction of contractions in a stated 20-minute window.
9. Tachysystole rests on a 30-minute average and is qualified as with or without decelerations.
10. Every Category II label lists CPG 10 Box 3 higher-risk and protective features present.
11. Paper speed, scale and the clock offset are recorded; conflicts are in the reconciliation table.
12. Retrospective drafts record the outcome-blind pass and contain no standard-of-care or causation statement.
13. Every `[VERIFY]` relied on is in the open items with what would settle it.

## Guidelines

- Describe the components before the category; the category compresses them and loses detail (CPG 10).
- A charted category is evidence of what a clinician wrote, not of what the tracing showed.
- Moderate variability and accelerations reliably predict the absence of metabolic acidemia at the time observed; minimal or absent variability alone does not reliably predict acidemia (NICHD 2008).
- FHR patterns reflect current acid-base status and cannot predict cerebral palsy (NICHD 2008).
- Category III tracings are rare, under 1 percent, and not uniform: absent variability, bradycardia and a sinusoidal pattern carry different implications (CPG 10).
- Guidance content on responses (CPG 10 Table 2) is listed only to describe what was done; never convert it into a dose, rate or instruction.
- In concurrent use, a draft description never replaces bedside interpretation; Category III criteria prompt an instruction to escalate now.
- Keep protected health information to what the review needs; de-identify shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Rate jumps when the scalp electrode goes on | External segment was maternal or artifact | Label the earlier segment Not categorized (signal source not confirmed); interpret from the FSE start |
| Paper strip with no visible time marks | Photocopy or cropped image | Request the archive export; leave timing-dependent labels open |
| Contraction channel flat or missing | Toco displaced or not recorded | Classify decelerations as abrupt or gradual only; mark early or late as unclassified (no contraction reference) |
| EFM and EHR times differ | Unsynchronized clocks | State the offset from an anchor event; if none, keep times separate |
| Charted category differs from the tracing | Charting error or a different window | Reconciliation row with both windows; do not overwrite the chart |
| Twin tracings look identical | Duplicate monitoring of one twin | Flag both channels; do not interpret the second as a different fetus |
| Care date near the CPG 10 publication | Guidance transition | Show PB 106 and 116 and CPG 10 side by side; policy election |
| Scanned strips unreadable | Low resolution | Attempt enhancement; list as unreadable with dependent segments Not categorized |

## Related Skills

- managing-labor-and-delivery: labor progress, cervical change and delivery summary that supply the timeline.
- managing-high-risk-pregnancies: maternal conditions (preeclampsia, diabetes, growth restriction) that shape the clinical context.
- documenting-cesarean-sections: operative report when the tracing led to cesarean delivery.
- managing-newborn-assessments: neonatal condition at birth; this skill gives no neonatal opinion.
- documenting-nursing-notes: structure of contemporaneous nursing EFM documentation.
- managing-patient-safety-events: event reports and root cause analysis after an adverse outcome.
- managing-risk-management-healthcare: claims handling and loss prevention after a review.
- medical-record-chronology: litigation chronology with Bates citations when counsel needs the full record timeline.
- expert-medical-record-omissions: testing an expert's report against the full record set.

## Reference Files

- `references/nichd-definitions-and-categories.md`: windows with their triggers, definitions, uterine activity, categories, Category II features, maternal heart rate checks, paper speed, source differences.
- `references/retrospective-review-rules.md`: guidance by date of care, outcome-blind protocol, timeline and clocks, charted interpretation, responses, scope limits.
- `references/output-template.md`: deliverable sections, segment worksheet, deceleration log, reconciliation and hand-off tables.
- `references/primary-sources.md`: each authority checked with date and what it supports, corrections, and the `[VERIFY]` list.
