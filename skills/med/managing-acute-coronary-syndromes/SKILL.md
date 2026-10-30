---
name: managing-acute-coronary-syndromes
language: en
description: >
  Reviews acute coronary syndrome (ACS) care for one encounter as a coordination, documentation and quality draft: STEMI, NSTEMI, unstable angina, MINOCA. Builds a timestamp ledger from EMS, ED, cath
  lab and transfer records and computes each reperfusion clock from its own trigger (first medical
  contact to device, door-to-balloon, door-in-door-out, door-to-needle,
  NSTE-ACS invasive timing) against the 2025 ACC/AHA/ACEP/NAEMSP/SCAI ACS guideline, kept separate
  from the CMS STEMI eCQM (CMS996), ACC/AHA performance measures and NCDR registry definitions.
  Screens ECG documentation for STEMI equivalents (posterior MI, de Winter, LBBB or paced rhythm with
  Sgarbossa); checks troponin against the assay's sex-specific 99th percentile; separates myocardial
  injury, type 1 and type 2 MI (Fourth UDMI) and primary or secondary MI (Fifth UDMI, 2026) from
  ICD-10-CM codes; reviews fibrinolysis contraindications, transfers, discharge medications and
  cardiac rehab referral. Drafts for clinician review; no patient orders.
tags:
  - management
  - cardiology
  - risk
metadata:
  author: casemark
  practice_areas:
    - Cardiology
    - Interventional Cardiology
    - Electrophysiology
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Acute Coronary Syndromes

Builds an ACS care-coordination and quality review for one encounter: a source register and timestamp ledger across every facility involved, a clock table in which each timed element runs from its own trigger, a measure scorecard, a review of the diagnostic documentation (ECG, troponin, MI classification), a fibrinolysis and transfer review, a discharge checklist, and the conflicts, query candidates and hand-offs that follow. Clinical guideline goals, quality measure results, registry definitions and coding rules are reported on separate rows. Everything it produces is a draft for review by the treating clinicians, quality staff and coders; it is not a diagnosis, a code assignment or an order.

## Why This Skill Exists

ACS reviews are dominated by clocks and labels, and both are easy to get wrong without any error in care. The same phrase, "door-to-balloon", means first medical contact to device in the 2025 ACC/AHA/ACEP/NAEMSP/SCAI guideline, ED arrival to device deployment in the CMS STEMI eCQM, and receiving-hospital door to device on many dashboards; for a transfer these can differ by more than an hour. First medical contact itself now has two definitions (the 2025 guideline's and the NCDR registry's). The diagnostic vocabulary changed in August 2026, when the Fifth Universal Definition of MI replaced types 1 to 5 with primary, secondary and procedure-related MI, while ICD-10-CM FY 2027 still codes type 1 and type 2. Missed STEMI equivalents keep a reperfusion clock from ever starting; troponin read against a borrowed threshold turns injury into infarction; and a discharge note that says "recommend cardiac rehab" is not a referral. This skill keeps the frameworks apart, computes from source timestamps and names every conflict.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Reperfusion dashboard or abstract reporting "door-to-balloon" | Judging timeliness of primary PCI | Receiving-hospital door used for a transfer patient; cath lab arrival or procedure start used where device time governs; registration time substituted for arrival; a measure result reported as guideline concordance, or the reverse |
| EMS run sheet and first-facility ED record | First medical contact (FMC) | 2025 guideline FMC (first professional who can obtain and interpret an ECG) mixed with NCDR v3.2 FMC (first EMS evaluation) and with the eCQM's ED arrival; a walk-in FMC taken from the ECG time without showing arrival and triage readings |
| Measure population and facility attribution for a transfer | Which hospital's measure, which patients are in it | Referral hospital's door-in-door-out and the receiving hospital's door-to-device scored as one case; PM-8 applied to a transfer-in it excludes; a patient under 18 or a non-STEMI ED encounter scored in CMS996 |
| 12-lead ECG reports and machine reads | STEMI or NSTE-ACS, start of the reperfusion clock | ST depression in V1-V3 labeled NSTEMI with no posterior leads; de Winter or hyperacute T waves missed; LBBB or paced rhythm assessed without Sgarbossa criteria; a new LBBB alone treated as a STEMI equivalent |
| Troponin results and the laboratory's assay sheet | Myocardial injury, rise and fall, rule-in or rule-out | Threshold borrowed from another assay or a uniform cut-off used where the lab reports a sex-specific 99th percentile; ng/mL compared with ng/L; a pathway risk threshold read as the diagnostic limit; timing from symptom onset ignored |
| Provider diagnosis statements, problem list and coded abstract | MI classification and ICD-10-CM codes | Type 2 MI or non-ischemic myocardial injury coded I21.4; "NSTEMI" in the discharge summary against "demand ischemia" in progress notes with no query; Fifth UDMI "secondary MI" or "primary MI due to SCAD" translated into a type or code without saying so |
| Cath report with no stenosis of 50 percent or more | Final diagnosis after angiography | "MINOCA" recorded as final with no CMR, no angiogram re-review and no alternative diagnosis excluded; the Fifth UDMI's renaming to myocardial injury with non-obstructive coronary arteries ignored |
| Facility fibrinolysis checklist or order set | Whether fibrinolysis was contraindicated | A home-grown or outdated list labeling relative contraindications (oral anticoagulant, prior ischemic stroke over 3 months, hypertension that responded to treatment) as absolute; CMS996 exclusions read as clinical contraindications |
| Discharge summary, medication reconciliation and referral orders | Secondary prevention and transition of care | "Recommend cardiac rehab" counted as a referral; LVEF not documented; antiplatelet plan without duration or bleeding-reduction rationale; secondary MI patients not referred |

## Ground Rules

1. **Draft only.** Every output is a draft for the treating clinicians, quality staff and coders. Never state that a case is final, submitted or validated, and never phrase guideline content as an order for this patient: no agents, doses, routes, durations or procedures directed at the patient.
2. **Source-review gate.** Do not call a timestamp, tracing, value or note missing until every supplied document has been opened and searched, including scanned files and the records of every facility involved. Classify each unresolved gap as an unknown fact, a source conflict, an unverified external lookup (for example a measure logic rule not read) or a policy election (for example the facility's chosen hs-cTn pathway).
3. **Hierarchy of authority.** For clinical recommendations: the 2025 ACS guideline as corrected, then the documents it defers to (2021 chest pain guideline, AHA MINOCA statement), then facility protocol. For measure results: the measure specification for the reporting period, never the guideline. For definitions: the Universal Definition the record or the request names. For codes: ICD-10-CM Official Guidelines for the discharge date. For facts: source entries (EMS times, ECG acquisition time, specimen collection time, device time in the procedure log, MAR) govern over dashboards, registries and summaries. Name every conflict in the reconciliation table; never resolve one silently.
4. **Citation discipline.** Every timestamp, value and quoted note carries a source locator (document, facility, date and time, author role) or `[UNVERIFIED]`. Every rule carries its source and year, and its COR and LOE for a guideline statement, or `[VERIFY]`.
5. **Name the framework on every conclusion.** Write "2025 guideline transfer goal (120 min): not met", "CMS996v6, Hospital A: not in numerator" or "Fourth UDMI type 2 criteria: not documented". Never merge frameworks into one pass or fail.
6. **Lock the versions.** State the guideline and correction date, the eCQM version for the reporting period (CMS996v6 for CY 2026), the performance measure set (2017), the Universal Definition (Fourth, 2018, or Fifth, 2026) and the ICD-10-CM fiscal year for the discharge date (FY 2027 from October 1, 2026).
7. **Each clock has its own trigger and timestamp type.** Compute every element from the start event its source names (`references/reperfusion-and-measure-rules.md`, Section 2). Use device time, not procedure start; ED arrival, not registration, unless the source says otherwise; collection time for troponin samples. Where the anchor is ambiguous (walk-in FMC), compute every plausible reading and say whether the result changes.
8. **The assay governs troponin.** Interpret values only against the laboratory's own assay, unit, sex-specific 99th percentile and pathway thresholds. A missing assay sheet is an unknown fact; never borrow a threshold.
9. **Diagnosis and codes belong to clinicians and coders.** Record what the documentation says, which definition it uses, and which criteria the record supports or lacks. Do not assign a final MI class, read an ECG as the final interpreter, or assign a code.
10. **No documentation steering.** Never suggest adding, backdating or editing an entry, or wording a diagnosis, so that a case enters or leaves a measure, registry, cohort or payment group. Genuine ambiguity becomes a non-leading query candidate routed to `managing-cdi-programs`; a late entry follows facility policy and is labeled as one.
11. **Scope and attribution.** For every measure row, name the facility it is attributed to and test the population before scoring: a transfer usually produces separate rows for the referral and receiving hospitals.
12. **Outcome vocabulary.** Clock elements: Met, Not met, Not applicable, Not yet due, Cannot determine. Measure rows: In numerator, Not in numerator, Excluded, Exception documented, Not in population, Cannot determine. Documentation items: Documented, Not documented, Conflict. Add "provisional pending <facts>" where unchecked facts could change a result; "Cannot determine" names the missing fact and who can supply it.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Collect before Step 1:

1. Purpose: concurrent coordination on an open encounter, retrospective quality review, registry abstraction support, peer-review packet, or record review for counsel.
2. Facilities involved, each marked PCI-capable or not, and the role of each (referral, receiving).
3. Age, sex as documented, arrival mode (EMS, walk-in, interfacility transfer), arrival and discharge dates.
4. The record set: EMS run sheet, ED records of every facility, every ECG with acquisition and interpretation times, troponin reports with collection times and the lab's assay sheet, cath and procedure logs with device times, MAR, transfer records, discharge summary, medication reconciliation and referral orders, and any dashboard, registry abstract or coded abstract under review.
5. Which frameworks the user wants addressed. Default: the 2025 guideline clock table and the discharge checklist; add a measure only when the user names it or asks about measure performance.
6. Facility protocols in play: hs-cTn pathway, fibrinolysis checklist, STEMI transfer protocol.

Defaults when an input is missing:

- Arrival mode not stated: treat FMC as an unknown fact and show each candidate anchor; never assume walk-in or EMS.
- Assay sheet missing: list troponin values with units and times, set injury and delta judgments to Cannot determine, and request the lab's 99th percentile and pathway.
- Discharge date missing on a retrospective review: state the ICD-10-CM year and measure version as provisional.
- Open encounter: windows not yet closed are "Not yet due".

Hard stops (do not score the affected item):

- No timestamped source for the events at issue (only a narrative or a dashboard): produce the ledger of what is missing and stop before scoring clocks or measures.
- Measure scoring requested with no way to identify the reporting period or version: do not score that measure.
- Patient under 18: outside CMS996 and the 2017 measures; say so and route pediatric questions to `managing-pediatric-emergencies`.
- A request that the review itself assign the final MI class, interpret an ECG as final, or assign a code: record the documentation and conflicts, and route the decision to the clinician, `interpreting-emergency-ecgs` or coding.

Decline that part, then continue the review of the record as it stands:

- A request to write orders, doses or treatment for a current or past patient: offer the guideline comparison instead.
- A request to create, backdate or alter documentation, or to word a diagnosis, so the case passes a measure, enters or leaves a registry or cohort, or changes a code: explain the late-entry and query policies and route genuine ambiguity to a compliant query.

## Step 1: Frame the Question and the Frameworks

Read `references/reperfusion-and-measure-rules.md`, Section 1. Restate the question in one line and list each framework that will be addressed with its version. If the request uses "door-to-balloon", "D2B" or "the STEMI measure" without saying which, name the candidate definitions in the first line of the output and score each separately.

## Step 2: Build the Source Register and Timestamp Ledger

Open every supplied document and complete the source register and ledger in `references/output-template.md`, Section 2. Record each event with facility, value, time, time type and source. Where two sources give different times for one event (dashboard against procedure log, registration against arrival), record both and add a reconciliation row.

## Step 3: Review the ECG Documentation

Read `references/diagnosis-and-classification-rules.md`, Sections 1 and 2. For each ECG, record acquisition and interpretation times, the documented findings and the clinician's conclusion. Screen the documentation for posterior, right-ventricular, de Winter, hyperacute T, aVR and LBBB or paced patterns and whether the record shows they were looked for (posterior or right-sided leads, Sgarbossa assessment, comparison and serial ECGs). Record a possible missed pattern as a finding for physician review and hand off to `interpreting-emergency-ecgs`; do not reclassify the case.

## Step 4: Review Troponin and MI Classification

Read `references/diagnosis-and-classification-rules.md`, Sections 3 to 6. Fill the troponin block with the lab's own assay data, compute absolute and relative deltas, and state acute, chronic or cannot determine. Then fill the classification block: each diagnostic statement, the definition it uses, the criteria the record supports, and the code on the abstract. List every conflict (for example "NSTEMI" against "demand ischemia", or I21.4 against documented type 2 MI) as a query candidate. Treat MINOCA as a working diagnosis and list the missing work-up.

## Step 5: Compute the Clocks

Read `references/reperfusion-and-measure-rules.md`, Sections 2 and 3. Fill the clock table in `references/output-template.md`, Section 3, one row per element, each from its own start event. For transfers, compute the referral hospital's door-in-door-out, the FMC-to-device interval across both facilities, and the receiving hospital's door-to-device, and label which framework uses which. Show alternative anchors and whether they change the result.

## Step 6: Score the Measures Requested

Read `references/reperfusion-and-measure-rules.md`, Sections 4 and 5. For each measure the user named, test population, exclusions and exceptions before the numerator, and name the attributed facility. Mark any rule you could not read as `[VERIFY]` and say whether it could change the row.

## Step 7: Review the Reperfusion Choice and NSTE-ACS Timing

Read `references/reperfusion-and-measure-rules.md`, Sections 6 and 7. For STEMI at a non-PCI-capable hospital, record the anticipated transfer time, the documented choice, and each contraindication fact with the facility checklist label, its 2025 Table 14 category and its CMS996 exclusion status. For NSTE-ACS, record the documented risk features and the time to angiography against the guideline category. Label concordance questions "for physician peer review"; do not say what should have been given.

## Step 8: Review Discharge and Transitions

Read `references/reperfusion-and-measure-rules.md`, Section 8. Fill the discharge checklist in `references/output-template.md`, Section 7, recording documentation status only. A cardiac rehab referral counts only when a referral to a named outpatient program was placed before discharge or a documented exception exists.

## Step 9: Reconcile, List Gaps and Hand Off

Complete the reconciliation table, gaps and query candidates, hand-offs and open items (`references/output-template.md`, Sections 8 to 11). Check each rule relied on against `references/primary-sources.md` and carry its `[VERIFY]` flag into the output.

## Checkpoint B: Post-Draft Alignment

1. Does the output answer the question asked, for the frameworks asked, each on its own row?
2. Is every version named: guideline and corrections, eCQM version, measure set, Universal Definition, ICD-10-CM year?
3. Does every clock row show its own start event, stop event and timestamp type, with alternative anchors where FMC is ambiguous?
4. Is every measure row attributed to a facility, with population, exclusions and exceptions tested before the numerator?
5. Is any sentence phrased as an order, a final diagnosis, a final ECG read, a code assignment or a suggestion to change documentation? Remove it.
6. Does every result that depends on a `[VERIFY]` rule say so, and would it flip if the rule reads differently?

## Quality Audit

1. The header names each framework and version, the facilities and their roles, and the purpose.
2. The source register covers every supplied document from every facility; nothing is called missing without a search.
3. Every ledger entry has a value, a time, a time type, a facility and a source locator.
4. Every clock row has its own trigger; device time, arrival time and collection time are used where the source requires them, and each substitution is flagged.
5. Transfer cases show referral-hospital door-in-door-out, cross-facility FMC-to-device and receiving-hospital door-to-device as separate rows.
6. Measure rows test population, exclusions and exceptions, and name the attributed facility; no guideline goal is reported as a measure result.
7. ECG review records whether posterior, right-sided, Sgarbossa and serial assessments were documented, without reclassifying the case.
8. Troponin interpretation cites the lab's assay, unit, sex-specific 99th percentile and pathway, or says Cannot determine.
9. The classification block names the definition each statement uses and lists every conflict between notes, summary and codes as a query candidate.
10. MINOCA, if present, is treated as a working diagnosis with the missing work-up listed.
11. Fibrinolysis facts are compared with 2025 Table 14 and, separately, with CMS996 exclusions.
12. The discharge checklist records documentation status only, and counts a CR referral only when placed before discharge.
13. No dose, order or documentation change is suggested, and every `[VERIFY]` relied on appears in the open-items list.

## Guidelines

- The 2025 ACS guideline covers type 1 MI; it refers type 2 MI, SCAD and MINOCA to other documents. Do not apply its reperfusion clocks to a supply-demand presentation without saying so.
- The 2025 guideline states FMC-to-device goals (90 and 120 minutes) but no door-to-needle or door-in-door-out number; the 30-minute and 45-minute figures are measure targets.
- Never delay or criticize reperfusion for a pending troponin; troponin can be below the URL early in STEMI.
- A measure exclusion removes a case from a denominator; it says nothing about whether care was appropriate.
- Concurrent review on an open encounter is provisional; windows still open are "Not yet due".
- Keep protected health information to what the review needs; de-identify case identifiers in shared drafts.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Two FMC times for one patient | Walk-in, or several EMS units arrived | Compute each reading, show which framework uses which, and state whether the result changes |
| Dashboard door-to-balloon disagrees with the ledger | Dashboard uses receiving-hospital door, procedure start or registration time | The procedure log and ED arrival entries control; add a reconciliation row naming the dashboard's rule |
| ECG available only as a scanned image or a machine read | Tracing not exported | Open it; if unreadable, record it as unreadable and set dependent items to Cannot determine; request the tracing |
| Troponin units or assay unclear | Mixed conventional and hs results, or a send-out lab | List each value with its unit and lab; request the assay sheet; do not compare across assays |
| Notes use Fourth UDMI types and the request uses Fifth UDMI terms | Definition change in 2026 | Show both vocabularies in the classification block and route coding questions to a query |
| Facility checklist disagrees with Table 14 | Home-grown or outdated template | Record both labels; route the concordance question to physician peer review |
| Referral and receiving records give different times for the same transfer | Clock drift or manual entry | Record both, use each facility's own record for its own measure, and flag the difference |

## Related Skills

- managing-acute-chest-pain: undifferentiated chest pain work-up and ED disposition before an ACS diagnosis is made.
- interpreting-emergency-ecgs: final reading of tracings with possible STEMI-equivalent patterns.
- interpreting-electrocardiograms: complete rhythm, interval and morphology interpretation.
- interpreting-cardiac-catheterization: angiographic findings, culprit lesion and procedural detail.
- coordinating-emergency-transfers: transfer documentation and stabilization requirements.
- managing-emtala-compliance: EMTALA questions raised by a delayed or refused transfer.
- calculating-emergency-risk-scores: computing HEART, GRACE or TIMI scores from documented inputs.
- managing-cdi-programs: compliant queries when MI type, injury or MINOCA documentation conflicts.
- abstracting-clinical-documentation: codeable diagnoses and specificity for the final abstract.
- managing-quality-reporting: hospital-level rates, eCQM submission and data validation.
- managing-cardiac-rehabilitation: CR enrollment, risk stratification and exercise prescription after referral.
- managing-lipid-therapy: lipid follow-up and nonstatin therapy decisions after discharge.
- managing-anticoagulation-therapy: patients on oral anticoagulants who also need antiplatelet therapy.
- managing-heart-failure: reduced LVEF or cardiogenic shock follow-up after ACS.
- managing-sepsis-bundles: sepsis encounters in which troponin elevation raises a secondary MI or injury question.
- conducting-mortality-reviews: case review of an ACS death beyond process timing.
- medical-record-chronology: a litigation chronology when counsel needs the full timeline rather than a quality review.

## Reference Files

- `references/reperfusion-and-measure-rules.md`: framework map, clock table with a trigger for each element, FMC definitions, CMS996v6, 2017 performance measures, fibrinolysis Table 14 versus measure exclusions, NSTE-ACS timing, discharge items.
- `references/diagnosis-and-classification-rules.md`: STEMI criteria and equivalents, troponin interpretation, Fourth versus Fifth UDMI, MINOCA, ICD-10-CM FY 2027 mapping, risk scores.
- `references/output-template.md`: deliverable sections, ledger, clock table, measure scorecard, diagnostic blocks, discharge checklist, reconciliation and hand-off tables.
- `references/primary-sources.md`: each authority checked with URL, method and date, confirmed statements, changes, and the `[VERIFY]` list.
