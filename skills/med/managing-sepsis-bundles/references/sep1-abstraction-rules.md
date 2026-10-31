# SEP-1 Abstraction Rules

Working summary of the CMS Severe Sepsis and Septic Shock: Management Bundle (SEP-1) for chart-abstracted review. It is a map to the manual, not a substitute for it. The governing text is the Specifications Manual for National Hospital Inpatient Quality Measures for the discharge date: the SEP-1 measure information form, the algorithm, and the Alphabetical Data Dictionary. Rules cited "DD, <element>" were read in that data element of the v5.18a Alphabetical Data Dictionary (KHA Quality mirror of the CMS manual, hosted by the Kentucky Hospital Association; see `references/primary-sources.md`). Every sub-rule marked `[VERIFY]` was not found in that text, usually because it sits in the measure information form or algorithm, which were not read; confirm it before a pass or fail depends on it.

## Contents

1. Version lock
2. Population and exclusions
3. Severe sepsis present and severe sepsis presentation time
4. Septic shock present and septic shock presentation time
5. Bundle elements and windows
6. Crystalloid volume and weight rules
7. Persistent hypotension, vasopressors and reassessment
8. Timestamp conventions
9. Frequent abstraction errors

## 1. Version lock

| Discharge period | Manual version | Status of this entry |
|---|---|---|
| 01/01/2026 to 12/31/2026 | 5.18a (5.18 plus addendum) | CMS notices 2025-66-IP (v5.18) and 2025-96-IP (v5.18a addendum); the data dictionary footer reads "Discharges 01-01-26 (1Q26) through 12-31-26 (4Q26)" |
| 01/01/2025 to 12/31/2025 | 5.17a | Cited by the April 2025 CMS SEP-1 training |
| 01/01/2027 to 12/31/2027 | 5.19 | CMS notice 2026-57-IP and the eCQI Resource Center notice, July 1, 2026; v5.19 includes updated SEP-1 abstraction guidance |

- Pick the version by discharge date, never by today's date or the abstraction date.
- The CMS IQR notice announcing v5.18 (listserve 2025-66-IP, June 24, 2025) states that the manual updates the chart-abstracted SEP-1 measure and removes the COVID-19 exclusion from the Initial Patient Population. A checklist that still excludes U07.1 is stale for 2026 discharges. The v5.18a data dictionary contains no COVID-19 abstraction instruction. Read the 5.18 release notes for their exact wording before quoting them `[VERIFY]`.
- SEP-1 is reported in the Hospital IQR Program (since FY 2017) and was adopted into the Hospital VBP Program Safety domain beginning with the FY 2026 program year (FY 2024 IPPS/LTCH PPS final rule). Program weights, baselines and later rule changes are year-specific `[VERIFY]`.

## 2. Population and exclusions

**Initial patient population.** Inpatient discharges, age 18 or older at admission, with an ICD-10-CM principal or other diagnosis code of sepsis, severe sepsis or septic shock from Appendix A, Table 4.01: Severe Sepsis and Septic Shock (SEP), which the v5.18a addendum updated for FY 2026 codes (notice 2025-96-IP). The code only admits the case to review; it does not establish that severe sepsis was present under the measure.

**Leaving the measure population.** Severe sepsis not present is not an exclusion: the case never enters the measure population (outcome "Not in population"). It is neither a pass nor a fail.

**Denominator exclusions.** The data dictionary defines the exclusion elements below; the algorithm that applies them was not read, so the length-of-stay and discharge-within-6-hours rules rest on CMS training `[VERIFY]`. An excluded case leaves the denominator entirely; none of its elements is scored.

| Exclusion | Rule in v5.18a | Common error |
|---|---|---|
| Length of stay over 120 days | The Admission Date element accepts only dates 120 days or less before discharge; the exclusion itself is in the measure information form `[VERIFY]` | Counting from ED arrival instead of the admission date |
| Transfer in from another hospital or an ambulatory surgery center | Yes for a transfer from an outside hospital's inpatient, outpatient, ED or observation department, any LTAC, an acute rehab or psychiatric hospital (inside or outside), or a DMAT; No for an urgent care center, clinic, hospice, SNF, nursing home, assisted living, dialysis center, an outpatient department inside the hospital, or a site with the same CMS Certification Number; No when documentation conflicts and nothing supports one setting (DD, Transfer From Another Hospital or ASC) | Treating a clinic, SNF or same-system outpatient site as an acute transfer |
| Directive for comfort or palliative care | Physician, APN or PA documentation of comfort measures only, palliative care or another inclusion term, before or within 6 hours after severe sepsis presentation (the septic shock element uses septic shock presentation); a DNR order is expressly not comfort care; pre-arrival documentation other than a state-authorized portable order does not count (DD, Directive for Comfort Care or Palliative Care) | Treating a DNR or DNI order as comfort measures only; counting "discussion of comfort measures" or "pt on hospice at home" |
| Clinical trial | Enrollment in a trial studying sepsis, severe sepsis or septic shock, shown only by a signed consent form (DD, Clinical Trial) | Excluding for an unrelated trial |
| Discharge within 6 hours of severe sepsis presentation | Discharge time is when the patient left acute care, left AMA or expired (DD, Discharge Time); the 6-hour rule is in the algorithm `[VERIFY]` | Scoring the 3-hour elements and calling the case a fail; the exclusion removes the whole case |
| Antibiotic started more than 24 hours before presentation | The abstractor takes the first dose of an antibiotic that was also started more than 24 hours before presentation, looking back no more than 72 hours (DD, Broad Spectrum or Other Antibiotic Administration Time); how the algorithm scores that case is `[VERIFY]` | Counting oral doses, which the antibiotic element excludes |
| Administrative contraindication to care | Physician, APN, PA or nurse documentation that the patient or authorized advocate refused a blood draw, IV or IO fluids, or IV or IO antibiotic (septic shock element: vasopressor), or left against medical advice, before or within 6 hours after presentation (DD, Administrative Contraindication to Care) | Inferring refusal from a missed draw |

## 3. Severe sepsis present and severe sepsis presentation time

**Clinical criteria route.** All three met within six hours of each other, in any order (DD, Severe Sepsis Present):

1. Documentation of an infection. Physician, APN, PA or nursing documentation is acceptable, as is physician, APN, PA, nursing or pharmacist documentation that an IV or IO antibiotic is being given for an infection and was given within six hours of the other two criteria. Viral, fungal and parasitic infections do not count; colonization, positive cultures or test results without documentation of suspected infection do not count. Provider documentation within six hours that the infection is not present, or is viral, fungal or parasitic, cancels the earlier documentation.
2. Two or more SIRS criteria: temperature over 38.3 C or under 36.0 C; heart rate over 90; respiratory rate over 20; WBC over 12,000 or under 4,000, or over 10 percent bands.
3. One or more organ dysfunction criteria: SBP under 90 or MAP under 65; an SBP decrease of more than 40 mm Hg only with provider documentation that it occurred and is related to infection; creatinine over 2.0; urine output under 0.5 mL/kg/hour for two consecutive hours, only when hourly monitoring is documented; total bilirubin over 2 mg/dL; platelets under 100,000; INR over 1.5 or aPTT over 60 seconds, not used after an anticoagulant in Appendix C Table 5.3; lactate over 2 mmol/L; acute respiratory failure shown by a new need for invasive or non-invasive mechanical ventilation, timed when ventilation started. Creatinine is not used with documented ESRD on dialysis; with documented chronic kidney disease and a documented baseline, a rise of more than 0.5 above baseline is used.

**Pregnancy (new in v5.18).** When the Pregnant 20 Weeks Through Day 3 Post-delivery element is Yes, use the pregnancy thresholds: temperature 38 C or more or under 36.0 C; heart rate over 110; respiratory rate over 24; WBC over 15,000 or under 4,000 or over 10 percent bands; SBP under 85 or MAP under 65 (also for initial and persistent hypotension); creatinine over 1.2; and no lactate obtained during active delivery. With no documentation of pregnancy, the non-pregnant criteria apply.

**Values that do not count.** A SIRS or organ dysfunction value is not used when physician, APN or PA documentation, before or within 24 hours after presentation and in the same sentence or paragraph, attributes it to what is normal for the patient, a chronic condition, a medication, or an acute condition with a non-infectious source; less severe values of the same measure are then excluded too. An acute or acute-on-chronic condition without a stated non-infectious source does not remove the value. Values from the OR, interventional radiology, a code, procedural sedation, orthostatic checks or dialysis, or set by a ventilator, are not used.

**Provider documentation route.** Physician, APN or PA documentation of "severe sepsis", "septic shock", "severe sepsis with shock" or "sepsis with shock"; "bacteremia" and "septicemia" do not count. Positive qualifiers such as "possible", "suspected", "likely", "probable", "presumed" and "rule out" count; negative qualifiers such as "unlikely", "risk for", "ruled out", "evolving", "questionable" and "monitor" do not. Additional provider documentation at the same time or within six hours that the patient is not septic, or that the sepsis is viral, fungal or parasitic, makes severe sepsis not present. Order-set titles, alert headings and "severe sepsis exam completed" do not count. Documentation in a discharge note or summary is disregarded.

**Presentation time.** The earliest time the last of the three clinical criteria was met, or the earliest time a physician, APN or PA documented severe sepsis, whichever is earlier (DD, Severe Sepsis Presentation Time). For lab values, the criterion time is the lab result time; supporting sources apply only if the result time is unavailable (DD, Severe Sepsis Present). Use the earliest documented ED arrival time when severe sepsis criteria or provider documentation appear in pre-hospital records, or a provider documents severe sepsis present on arrival; for a direct admission with pre-hospital criteria or documentation, use arrival on the floor or unit. For "present on admission" documentation, use the earliest of the provider note, admit order, disposition to inpatient or arrival on the unit. The data dictionary has no ED triage-time rule. Not time zero: the sepsis alert or best-practice-advisory fire time, an order-set time, triage time when the criteria were not yet met, a sepsis navigator's "recognition" time, or a time chosen by the bedside team for the hour-1 bundle.

## 4. Septic shock present and septic shock presentation time

Severe sepsis present plus either persistent hypotension (in the hour after the target crystalloid volume is completely infused) or an initial lactate of 4 mmol/L or more; or physician, APN or PA documentation of septic shock, severe sepsis with shock or sepsis with shock (DD, Septic Shock Present). Septic shock presentation more than six hours after severe sepsis presentation is "not present". The presentation time is the later of severe sepsis presentation and the qualifying event: for persistent hypotension, the last of the consecutive hypotensive readings; for the lactate route, the lactate result time from the lab (DD, Septic Shock Presentation Time). Septic shock presentation time starts the 6-hour vasopressor and reassessment clocks, and starts the crystalloid clock only when no earlier initial hypotension did.

## 5. Bundle elements and windows

Each timed element has its own trigger and clock. Do not run every septic shock element from septic shock presentation: when the fluid trigger is initial hypotension, septic shock is not yet established, because persistent hypotension after the fluids is what establishes it.

| Element | Required when | Clock starts at | Window (v5.18a data dictionary) |
|---|---|---|---|
| Initial lactate | Severe sepsis present | Severe sepsis presentation | Drawn 6 hours before through 3 hours after (DD, Initial Lactate Level Collection) |
| Blood cultures | Severe sepsis present | Severe sepsis presentation | Collected from 24 hours before presentation, or from 24 hours before an antibiotic started in the 24 hours before presentation, through 3 hours after; collected before the antibiotic unless an acceptable delay is documented (DD, Blood Culture Collection; Blood Culture Collection Acceptable Delay) |
| Antibiotic | Severe sepsis present | Severe sepsis presentation | Started from 24 hours before through 3 hours after, IV (IM or IO only with documentation that IV access could not be established) (DD, Broad Spectrum or Other Antibiotic Administration) |
| Repeat lactate | Initial lactate over 2.0 | Severe sepsis presentation (not the initial lactate time) | After the initial lactate draw and by 6 hours after presentation (DD, Repeat Lactate Level Collection) |
| 30 mL/kg crystalloid | Initial hypotension, or septic shock (including initial lactate of 4 or more) | The earlier of initial hypotension and septic shock presentation | Ordered and started 6 hours before through 3 hours after; target volume completely infused, with no deadline for completion (DD, Crystalloid Fluid Administration) |
| Vasopressor | Persistent hypotension after the target crystalloid volume | Septic shock presentation | Started, or already infusing, by 6 hours after; an agent from Appendix C Table 5.2, IV or IO (DD, Vasopressor Administration) |
| Repeat volume status and tissue perfusion assessment | Septic shock present (persistent hypotension or initial lactate of 4 or more) | Septic shock presentation | From the Crystalloid Fluid Administration Time (the infusion start) through 6 hours after septic shock presentation (DD, Repeat Volume Status and Tissue Perfusion Assessment Performed) |

The v5.18a antibiotic element ("Broad Spectrum or Other Antibiotic Administration", updated in v5.18) names routes and times but no antibiotic table, and the v5.18a index has no separate antibiotic selection element. CMS Q&A for earlier versions required one agent from the monotherapy table or agents from two classes on the combination table, both started in the window. Whether v5.18a still applies those tables, and their numbers and contents, is `[VERIFY]` in the algorithm and Appendix C; state it as a dependency, never assume it either way.

SEP-1 is all-or-none: one failed element fails the case. A case that is excluded or not in the population is neither a pass nor a fail.

## 6. Crystalloid volume and weight rules

All from DD, Crystalloid Fluid Administration, unless noted.

- Target is 30 mL/kg of crystalloid; an ordered volume within 10 percent below 30 mL/kg is accepted without a documented reason, but the target ordered volume must still be documented as completely infused. The target need not finish infusing within the window.
- An order for less than 30 mL/kg is the target when a physician, APN or PA orders that specific or weight-based volume and documents, in a single note or order, the volume and a reason (for example concern for fluid overload, heart failure, renal failure, blood pressure responding to a lesser volume, or part of the volume given as colloids with an order and documentation that they were given). If 30 mL/kg is documented as the target within six hours after the lesser order, 30 mL/kg is the target.
- Weight: the weight in the fluid order, then the weight closest before the order, then the closest after; pounds divided by 2.2 and rounded to a whole kilogram. Ideal, predicted, adjusted or dosing weight is used only when a physician, APN or PA documents obesity or a BMI over 30, documents that the ideal weight sets the target volume, and the ideal weight is in the record; the abstractor does not calculate it.
- An order counts toward the target only if it states the fluid type, the volume, and a rate or duration ("bolus" or "wide open" suffices); an order missing any of these is not used. Completion must be shown by a rate, a duration or an end time with the start time.
- Acceptable fluids are crystalloid or balanced crystalloid solutions (0.9 percent saline, lactated Ringer's, Normosol, PlasmaLyte, Isolyte), IV or IO only. Fluids at 125 mL/hour or less do not count; flushes do not count; crystalloid used to dilute medications may count. Colloids enter only through the lesser-volume reason above. Blood products are not on the list.
- The element has a separate value when the patient has an implanted VAD, the patient or advocate refused IV fluids, or no fluids were ordered because measured cardiac output, cardiac index, stroke volume, stroke volume index or carotid flow time showed the patient was not fluid responsive; how the algorithm scores that value is `[VERIFY]`.

## 7. Persistent hypotension, vasopressors and reassessment

- Persistent hypotension is assessed in the hour after the target volume is completely infused, using the last two consecutive readings in that hour: low then low establishes it; low then normal, or normal then normal, does not; normal then low establishes it only if a vasopressor was given. With only one reading in the hour, a low reading establishes it only if a vasopressor was given; no reading, or a single low reading without a vasopressor, is "not assessed" (DD, Persistent Hypotension). Readings in the OR, interventional radiology, a code or procedural sedation do not count.
- Initial hypotension (the fluid trigger) is two hypotensive readings, not necessarily consecutive, within three hours of each other, between six hours before and six hours after severe sepsis presentation and before the target volume was completely infused; its time is the second reading. A reading the provider attributes to a medication, a chronic condition or a non-infectious cause is not used (DD, Initial Hypotension; Initial Hypotension Time). Version 5.3a set no maximum gap, so older worksheets differ.
- Vasopressor: an IV or IO agent from Appendix C Table 5.2, started or already infusing within 6 hours after septic shock presentation; an order alone does not count (DD, Vasopressor Administration).
- Reassessment, within the window in Section 5, by any one of three routes (DD, Repeat Volume Status and Tissue Perfusion Assessment Performed, updated in v5.18): (1) physician, APN or PA documentation attesting to a physical examination, perfusion assessment, sepsis-focused exam or systems review; (2) physician, APN or PA documentation reviewing at least five of eight parameters (arterial oxygen saturation, capillary refill, cardiopulmonary assessment, peripheral pulses, shock index, skin color or condition, urine output, vital signs), not necessarily in one note; or (3) documentation, by anyone, of central venous or right atrial pressure, central venous oxygen saturation, an echocardiogram, a fluid challenge or passive leg raise, or carotid flow time. A note timed before the crystalloid start time or later than 6 hours after septic shock presentation does not count.

## 8. Timestamp conventions

| Event | Use | Do not use |
|---|---|---|
| Lab value as a severe sepsis or septic shock criterion | Lab result time; then a time tied to the value in a note, a flowsheet time, the draw time, the note open time, in that order | Order time |
| Initial and repeat lactate elements | Draw time from the lab, then a flowsheet or a narrative time; if no draw time, the earliest supporting time (sent, received or result) | Order time, "labs drawn" |
| Blood cultures | Documentation that the culture was drawn, sent or received; a failed attempt counts | Order time, "labs drawn" |
| Antibiotic, crystalloid, vasopressor | Administration or infusion start time with name, route, date and time; for multiple fluid orders, the start of the infusion that completed the target | Order, verification or dispense time; IV access time |
| Vital signs | Time taken; recorded time only if that is missing; narrative only if nothing else | A later charting time |
| Provider documentation | The time stated in the note, else the note open time, then the provider care-initiated time, then the scribe time | Signature time of a later addendum |

## 9. Frequent abstraction errors

- Crystalloid clock run from septic shock presentation when the trigger was initial hypotension.
- An oral, test or IM dose counted for the antibiotic element, or older-version antibiotic tables applied to a 2026 discharge without stating the `[VERIFY]` dependency.
- Repeat lactate clock anchored to the initial lactate instead of presentation time.
- Antibiotic judged against one hour (an SSC aspiration) instead of the SEP-1 3-hour window.
- 30 mL/kg required for a lactate between 2 and 3.9 with no hypotension.
- Bolus volume computed on actual weight where the provider documented obesity and directed ideal weight.
- A fluid order without a rate, duration, "bolus" or "wide open" counted toward the target.
- Reassessment rejected because it was charted before the crystalloid finished, although the window opens at the infusion start.
- Non-pregnant thresholds applied when pregnancy of 20 weeks or more, or day 3 or earlier after delivery, is documented.
- Severe sepsis taken from a SOFA score or the word "sepsis" in a note.
