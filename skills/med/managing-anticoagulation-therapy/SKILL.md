---
name: managing-anticoagulation-therapy
language: en
description: >
  Reviews one patient's anticoagulation and drafts findings for the prescriber and pharmacist;
  never writes orders. Checks DOAC eligibility (mechanical valve, moderate to severe
  mitral stenosis, triple-positive APS) and dose against FDA labels for apixaban, rivaroxaban,
  dabigatran and edoxaban: apixaban two-of-three reduction (age, weight, creatinine),
  Cockcroft-Gault CrCl on the right weight, not eGFR, P-gp and CYP3A4 interactions, enoxaparin
  at CrCl below 30, feeding-tube use. Reads warfarin INR trends against the dose log. Builds periprocedural interruption and resumption
  timelines per CHEST 2022, PAUSE and BRIDGE, each element on its own clock; flags bridging
  without a high-risk reason. Checks transitions for duplicate anticoagulants and
  switch rules; reviews reversal (idarucizumab, 4F-PCC, andexanet alfa's end of U.S. sales) and
  Joint Commission NPG.14.04.01. Use for DOAC or enoxaparin dosing review, warfarin monitoring,
  periop anticoagulation, bridging, reversal or anticoagulation protocol review.
tags:
  - management
  - pharmacy
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

# Managing Anticoagulation Therapy

Drafts an anticoagulation review for one patient episode: an anticoagulant ledger, an eligibility and dose check against the current FDA label, a creatinine clearance worksheet, an interaction screen, a warfarin INR-and-dose review, a periprocedural timeline, a transition and duplication check, and a reversal readiness or event review, each finding tied to its source. The review supports the prescribing clinician and the pharmacist; it states what the label or guideline says and where the plan differs, and leaves every decision to them. Everything it produces is a draft for qualified clinical review. It never writes, enters or phrases an order.

## Why This Skill Exists

Anticoagulant errors run in both directions: too much drug causes bleeding, too little causes stroke or recurrent clot, and the 2023 ACC/AHA/ACCP/HRS AF guideline reports that inappropriately low DOAC doses were associated with more stroke without less bleeding. Most errors come from rules that look alike and are not: apixaban reduces on two of three criteria while edoxaban for VTE reduces on any one; apixaban uses serum creatinine while the others use creatinine clearance; a "1 day off" hold means about 36 hours, not 24. The facts sit in different places (MAR, home list, echo, lab report, schedule), and the rules changed recently: andexanet alfa left the U.S. market on December 22, 2025, and on January 1, 2026 the Joint Commission moved its anticoagulation requirement from NPSG.03.05.01 to NPG.14.04.01 for hospitals. This skill lines up each fact with the rule it is tested against.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Apixaban order with age, weight and SCr | NVAF dose check | 2.5 mg twice daily chosen on one criterion (age 80 or older alone) when the label needs two of three; a CrCl substituted for the SCr criterion; the VTE regimen judged by the AF rule |
| Lab report, EHR CrCl calculator, weight record | Renal band for rivaroxaban, dabigatran, edoxaban | eGFR in mL/min/1.73 m2 used as CrCl; ideal or adjusted weight used where the rivaroxaban label says actual weight; a stale or unstable SCr; edoxaban given with CrCl above 95 in NVAF |
| Echo report, problem list, valve history | DOAC eligibility | "Nonvalvular" taken from the problem list while the echo shows moderate mitral stenosis; a mechanical valve on dabigatran (contraindicated) or another DOAC; TAVR on rivaroxaban |
| Enoxaparin or heparin order with CrCl, weight and platelet history | Therapeutic LMWH or UFH check | Enoxaparin 1 mg/kg every 12 hours continued at CrCl below 30 where the Lovenox label regimen is 1 mg/kg once daily; prophylactic 40 mg kept at CrCl below 30; weight extremes (low weight, BMI over 30) not flagged; heparin product or 4F-PCC with a HIT history; a facility nomogram cited as label content |
| Medication list with start dates | Interaction screen | A combined P-gp and strong CYP3A4 inhibitor or inducer missed; the apixaban 50 percent rule applied to a patient already on 2.5 mg; the edoxaban NVAF "no reduction for P-gp inhibitors" rule ignored; clarithromycin treated like ketoconazole |
| Administration record, feeding-tube orders, surgical history, post-PCI discharge list | Route, absorption and antiplatelet co-therapy | Dabigatran capsules opened for a tube; rivaroxaban given into a tube ending past the stomach; a DOAC after bariatric surgery with no note of the absorption concern (AF guideline 10.4); aspirin, a P2Y12 inhibitor and an anticoagulant with no aspirin stop date after PCI (AF guideline 6.8.1) |
| INR log and warfarin dose calendar | Warfarin monitoring | INR read alone, without the doses taken in the prior days, missed doses, or an antibiotic started 3 days earlier; a dose changed in response to an INR that still reflects the previous change |
| Pre-procedure plan, surgical schedule | Interruption days | Days off counted from the procedure time instead of full days without a dose; dabigatran with CrCl below 50 held as if CrCl were normal; the label's 48-hour apixaban minimum for moderate bleed risk not reconciled with CHEST's 1 day off |
| Bridging order set | Whether bridging applies | LMWH bridging during DOAC interruption, or for AF on warfarin without recent stroke or TIA, a mechanical valve or another documented high-risk feature (BRIDGE, PAUSE, CHEST 2022) |
| Post-op orders and op note | Resumption time | DOAC or bridging restarted on the evening of a high-bleed-risk procedure; no note that hemostasis is adequate; resumption clocked from the last dose instead of the end of the procedure |
| Admission order set, MAR, discharge list | Transitions and switches | Prophylactic enoxaparin running with a therapeutic DOAC; apixaban continued "until INR is 2" after warfarin starts although apixaban raises the INR; home drug and formulary substitute both on the discharge list |
| Reversal protocol, order set, event record | Agent choice and readiness | Idarucizumab given for a factor Xa inhibitor; andexanet listed as first-line after its U.S. sales ended; the Eliquis label's "an agent to reverse ... is available" read as current; Kcentra's VKA-only indication not noted when used for a DOAC |
| Facility protocol, accreditation binder, collaborative practice agreement | Who may decide and which requirement applies | A protocol citing NPSG.03.05.01 for a 2026 hospital survey; the NPG applied to short-term VTE prophylaxis it excludes; a reviewer treated as authorized to change a dose without a collaborative practice agreement `[VERIFY]` by state |

## Ground Rules

1. **Draft only, never an order.** Every output is a draft for the prescribing clinician and pharmacist. State label or guideline content with its citation and the plan's difference from it; never write "give", "start", "hold" or "change to" as an instruction, never produce an order sentence, order-set entry or patient-specific dose.
2. **Source-review gate.** Do not call a value, note or order missing until every supplied document has been opened and searched, including scanned files. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (a label or guideline point not confirmed) or a policy election (a facility protocol choice).
3. **Hierarchy of authority.** For drug rules: the current FDA label, then the guideline (CHEST 2022 perioperative, CHEST 2021 VTE, 2023 AF guideline), then the facility protocol, then secondary references. For availability, FDA notices govern over label text. For facts: MAR administration times, lab reports with collection dates, measured weights, echo reports and the procedure schedule govern over home lists, discharge summaries, calculators and recall. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every patient value carries a source locator (document, date, author role) or `[UNVERIFIED]`. Every rule carries its label section or guideline statement or `[VERIFY]`.
5. **Outcome vocabulary.** Each item is "Consistent with label", "Discrepancy", "Source conflict", "Cannot determine" or "Not applicable". "Cannot determine" names the missing fact and who can supply it. Use "Consistent with guideline" when the label is silent.
6. **Count criteria one by one.** Show each dose-adjustment criterion with value, threshold and met or not met before any conclusion.
7. **Compute CrCl; never copy it.** Use Cockcroft-Gault with the weight the label names, show inputs, and never place an eGFR in a CrCl band.
8. **One trigger per clock.** Every interruption, bridging and resumption element is anchored to its own trigger event (procedure day, procedure start, end of procedure with hemostasis), shown as a calendar date, weekday and hours.
9. **Decisions belong to named people.** The proceduralist assigns bleed risk; the prescriber chooses the regimen; P&T owns the protocol. The review asks; it does not decide.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Question and setting: dose review, warfarin monitoring, procedure planning, transition, reversal event review, or protocol review.
2. Indication(s) for anticoagulation with source and start date; for VTE, the date of the event and whether provoked.
3. Every anticoagulant exposure, including heparin and enoxaparin: drug, dose, route (oral, tube, subcutaneous, IV), times, last dose taken, and source (MAR, home list, prescription); antiplatelets with start dates; HIT history; bariatric surgery history.
4. Age, sex, weight with date and source, height if a facility policy uses ideal or adjusted weight, SCr with collection date.
5. Valve status from an echo report (mechanical valve, mitral stenosis grade, TAVR, bioprosthesis) and APS status.
6. Full medication list with start dates, for the interaction screen.
7. For warfarin: INR log with draw times, dose calendar, target range and its source.
8. For a procedure: date and start time, proceduralist-assigned bleed-risk category, thromboembolic risk inputs, neuraxial plan.
9. For a reversal review: event timeline, agent and product given, times, and the protocol in force.

Defaults when an input is missing:

- Valve status unknown: eligibility is "Cannot determine (valve status)"; continue the other checks.
- Height missing: compute CrCl on actual weight only and note that alternative-weight comparisons could not be run.
- Facility protocol not supplied: compare against label and guideline only and list the protocol as still needed.
- Interacting-drug start dates missing: screen the drugs and mark timing as an unknown fact.

Hard stops:

- No documented indication: produce the ledger and stop before any eligibility or dose result.
- A dose result for a CrCl-banded DOAC without age, sex, weight and SCr, or for apixaban without age, weight and SCr: that item is "Cannot determine"; give no dose result.
- A periprocedural timeline without the procedure date and the proceduralist's bleed-risk category: list what is missing and give no timeline.
- Active bleeding now: state that care follows the hospital reversal protocol and the treating team, record drug class and last-dose time if supplied, and give no agent or dose.

Decline that part, then continue the review. Record each declined part under the "Declined part" block of `references/output-template.md` with exactly one of its labels:

- A request to write an order, prescription or patient dose: `Declined part: order or prescription`; offer the label and guideline comparison instead.
- A request for a dosing, holding or restart plan addressed to the patient: `Declined part: patient instructions`.
- A request for an order sentence, order-set entry or protocol wording: `Declined part: order-set or protocol text`; give findings for P&T.
- A request to record a bleeding-risk or hemostasis assessment that is not in the record, or to date one earlier: `Declined part: undocumented assessment`; route it to the responsible clinician.

## Step 1: Frame the Question and Build the Ledger

Restate the question in one line and name the sources that will be applied with their versions. Open every document and fill the source register and anticoagulant ledger in `references/output-template.md`, Sections 2 and 10. Include prophylactic and parenteral doses. Where two sources disagree on a dose or time, record both.

## Step 2: Check Eligibility

Read `references/label-dosing-rules.md`, Section 1. Test valve status, mitral stenosis grade, TAVR, APS and the edoxaban CrCl ceiling against the echo report and labs, not the problem list. Name the label section or guideline statement for each result. Grading an unclear valve lesion goes to managing-valvular-heart-disease.

## Step 3: Compute Renal Function

Read `references/label-dosing-rules.md`, Section 2. Fill the worksheet in `references/output-template.md`, Section 4. Use actual weight for rivaroxaban as its label states; if a facility policy uses another weight, compute both and record the policy election and whether the band changes. Note SCr stability. Report any eGFR from the lab separately and do not use it for a band.

## Step 4: Check the Dose and Interactions

Read `references/label-dosing-rules.md`, Sections 3 to 8, and Sections 11 and 12 when heparin or enoxaparin, a feeding tube, a weight extreme or bariatric surgery is involved. List each adjustment criterion with value, threshold and met or not met, then compare the ordered dose with the label content for that indication. Screen the medication list against Section 8, and check antiplatelet co-therapy after PCI against Section 10. Report the result in the vocabulary of Ground Rule 5. Interactions outside the label pairs go to assessing-drug-interactions.

## Step 5: Review Warfarin INR Against the Dose Log

When warfarin is involved, read `references/label-dosing-rules.md`, Section 7. Fill the INR table in `references/output-template.md`, Section 6, aligning each INR with doses taken over the prior days, missed doses, interacting drug starts and diet or illness changes. Flag any dose change made in response to an INR drawn before the previous change could take effect. Do not propose a new warfarin dose.

## Step 6: Build the Periprocedural Timeline

Read `references/periprocedural-and-reversal.md`, Sections 1 to 6. Write each element on its own trigger: last dose against the procedure day, bridging against the procedure start, resumption against the end of the procedure with hemostasis documented. Count days off as full days with no dose and give the date and weekday of the last permitted dose. Compare the plan with CHEST 2022, the AF guideline Table 18 and the label minimum, and name any conflict between them. Test any bridging plan against the documented high-risk feature that would justify it.

## Step 7: Check Transitions and Duplication

Read `references/periprocedural-and-reversal.md`, Section 7, and `references/label-dosing-rules.md`, Section 9. At each transition, list drugs active before and after, compute overlaps or gaps in hours, and compare switches with the label conversion rule. Full reconciliation of the non-anticoagulant list goes to reconciling-medications or reconciling-inpatient-medications.

## Step 8: Review Reversal Readiness or a Reversal Event

Read `references/periprocedural-and-reversal.md`, Sections 8 and 9. Match each agent in the protocol or event to the drug class its label covers, check availability on the event date against the FDA notice, record the Eliquis label conflict when apixaban is involved, and check whether the protocol cites NPG.14.04.01 for a hospital. Protocol changes are findings for P&T, not drafted orders.

## Step 9: Reconcile, List Gaps and Hand Off

Complete the review summary, reconciliation table, gaps and questions, hand-offs and open items in `references/output-template.md`. Check each rule relied on against `references/primary-sources.md` and carry its `[VERIFY]` flag into the output.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, for the setting asked, with each item scored separately?
2. Is any sentence phrased as an order, order sentence or patient dose? Rewrite it as label content plus a question.
3. Does every dose result show its criteria or CrCl inputs, and every timeline row its own trigger?
4. Does any result depend on a `[VERIFY]` item, and would it change if that item reads differently?
5. Are the decision owners named (prescriber, proceduralist, P&T) and every open item owned?

## Quality Audit

1. The header names the indication, setting and each source with its version.
2. The source register covers every supplied document; nothing is called missing without a search.
3. The anticoagulant ledger includes prophylactic and parenteral exposures with source and time.
4. Eligibility rests on echo and lab sources, with label sections cited for valve, stenosis, APS and edoxaban CrCl.
5. CrCl uses Cockcroft-Gault with the label's weight, inputs shown; no eGFR fills a CrCl band; alternative weights appear only as a named policy election.
6. Apixaban criteria are counted one by one, and the two-of-three rule is not confused with edoxaban's any-one VTE rule.
7. Interactions, route of administration, enoxaparin renal regimens and post-PCI antiplatelet co-therapy are checked against the cited label or guideline content.
8. Warfarin INR results are read with the dose log and interacting drugs, and no new dose is proposed.
9. Every periprocedural element has its own trigger, a calendar date and weekday, hours, and the source interval; dabigatran days reflect CrCl.
10. Bridging is flagged unless a documented high-risk feature supports it; DOAC bridging is a discrepancy without a recorded reason.
11. Resumption is tied to the end of the procedure and documented hemostasis.
12. Reversal agents match drug class; andexanet's end of U.S. sales and the Eliquis label statement are named when relevant.
13. No order, order sentence or patient dose appears anywhere; each declined request carries its fixed "Declined part" label; every `[VERIFY]` relied on is in the open items.

## Guidelines

- Underdosing is an error too. A reduced DOAC dose without a label criterion is a discrepancy, not a cautious choice.
- Apixaban NVAF dosing uses SCr, not CrCl; do not run Cockcroft-Gault to decide it, though CrCl still matters for its periprocedural floor.
- DOACs are not monitored by INR; dabigatran activity, when needed, is assessed with aPTT or ECT per its label.
- Warfarin peak effect may lag 72 to 96 hours; compare INR with the doses that produced it.
- A label minimum and a guideline schedule can both be met; when they differ, report both rather than choosing.
- Short-term VTE prophylaxis is outside NPG.14.04.01 but still counts toward duplication.
- Keep protected health information to what the review needs.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Two weights in the chart | Stated, bed-scale and clinic weights differ | List each with source and date; use the most recent measured weight; show whether the band changes |
| SCr rising or falling | Acute kidney injury or recovery | Mark the CrCl band provisional and name the SCr dates; ask for a repeat value |
| EHR shows a CrCl that differs from the worksheet | Calculator uses eGFR, ideal weight or rounding | Add a reconciliation row; the label method controls |
| Home list and MAR disagree on dose | Outdated list or formulary substitution | The MAR controls for inpatient exposure; flag the discharge list |
| Scanned or image-only echo or op note | Text search missed it | Open it, attempt OCR; if unreadable, list it and set dependent items to Cannot determine |
| Plan says "hold 2 days" with no date | Ambiguous counting | Show both readings with dates and hours and ask the prescriber which was meant |
| Protocol and guideline disagree | Older protocol | Report both; protocol updates go to P&T |

## Related Skills

- assessing-drug-interactions: full interaction screen and severity grading beyond the anticoagulant label pairs.
- managing-renal-dose-adjustments: renal dosing of other medications that the CrCl worksheet affects.
- managing-atrial-fibrillation: CHA2DS2-VASc scoring, rate and rhythm decisions, and whether to anticoagulate at all.
- managing-venous-thromboembolism-prophylaxis: choosing prophylaxis regimens, which this review only checks for duplication.
- managing-valvular-heart-disease: grading mitral stenosis or classifying a prosthetic valve when the echo is unclear.
- reconciling-medications: full medication reconciliation across care settings.
- reconciling-inpatient-medications: admission, inpatient and discharge list comparison in the hospital.
- conducting-pre-operative-evaluations: overall surgical risk assessment beyond anticoagulant timing.
- managing-adverse-drug-reactions: causality assessment and reporting of a bleeding event.
- reviewing-medication-safety: program-level high-alert medication safeguards.
- managing-medication-use-evaluations: population audits of DOAC dosing or reversal agent use.

## Reference Files

- `references/label-dosing-rules.md`: eligibility screens, renal input by label, DOAC, warfarin, enoxaparin and heparin label content, interactions, switching rules, guideline overlays, route and weight extremes, quality measures.
- `references/periprocedural-and-reversal.md`: timeline inputs, clocks with one trigger each, days-off counting, source conflicts, bridging evidence, restart documentation, transitions, reversal agents, NPG.14.04.01.
- `references/output-template.md`: deliverable sections, declined-part labels, ledger, CrCl worksheet, timeline, reconciliation table, gaps, hand-offs.
- `references/primary-sources.md`: each authority checked with URL, method and date, confirmed statements, corrections, and the `[VERIFY]` list.
