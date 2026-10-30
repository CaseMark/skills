# SEP-1 Abstraction Rules

Working summary of the CMS Severe Sepsis and Septic Shock: Management Bundle (SEP-1) for chart-abstracted review. It is a map to the manual, not a substitute for it. The governing text is the Specifications Manual for National Hospital Inpatient Quality Measures for the discharge date: the SEP-1 measure information form, the algorithm, and the Alphabetical Data Dictionary. Every sub-rule below marked `[VERIFY]` was reported by CMS support-contractor training material or secondary sources but was not read in the current manual text; confirm it before a pass or fail depends on it.

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
| 01/01/2026 to 12/31/2026 | 5.18a (5.18 plus addendum) | Listed on the QualityNet inpatient specifications page |
| 01/01/2025 to 12/31/2025 | 5.17a | Cited by the April 2025 CMS SEP-1 training |
| 01/01/2027 to 12/31/2027 | 5.19 | Reported by a July 1, 2026 eCQI notice; one source only `[VERIFY]` |

- Pick the version by discharge date, never by today's date or the abstraction date.
- The CMS IQR notice announcing v5.18 (listserve 2025-66-IP, June 24, 2025) states that the manual updates the chart-abstracted SEP-1 measure and removes the COVID-19 exclusion from the Initial Patient Population. A checklist that still excludes U07.1 is stale for 2026 discharges. Read the 5.18 release notes for the exact wording before quoting them.
- SEP-1 is reported in the Hospital IQR Program (since FY 2017) and was adopted into the Hospital VBP Program Safety domain beginning with the FY 2026 program year (FY 2024 IPPS/LTCH PPS final rule). Program weights, baselines and later rule changes are year-specific `[VERIFY]`.

## 2. Population and exclusions

**Initial patient population.** Inpatient discharges, age 18 or older at admission, with an ICD-10-CM principal or other diagnosis code of sepsis, severe sepsis or septic shock from the manual's code table (Appendix A) `[VERIFY table number]`. The code only admits the case to review; it does not establish that severe sepsis was present under the measure.

**Leaving the measure population.** Severe sepsis not present is not an exclusion: the case never enters the measure population (outcome "Not in population"). It is neither a pass nor a fail.

**Denominator exclusions.** CMS SEP-1 algorithm training lists a comfort or palliative care directive within 6 hours of presentation, administrative contraindication to care, transfer in from another acute care facility or ambulatory surgery center, sepsis clinical trial enrollment, and discharge within 6 hours of presentation. Confirm the remaining rows and every time limit in the data dictionary `[VERIFY]`. An excluded case leaves the denominator entirely; none of its elements is scored.

| Exclusion | Common error |
|---|---|
| Length of stay over 120 days | Counting from ED arrival instead of the admission date the manual uses |
| Transfer in from another acute care hospital (including another hospital's ED) or an ambulatory surgery center | Treating a transfer from a free-standing clinic, SNF or same-system outpatient site as an acute transfer |
| Directive for comfort or palliative care within 6 hours of severe sepsis presentation | Treating a DNR or DNI order as comfort measures only; counting "discussion of comfort measures" |
| Clinical trial enrollment relating to sepsis | Excluding for an unrelated trial |
| Discharge date and time within 6 hours of severe sepsis presentation | Scoring the 3-hour elements and calling the case a fail; the exclusion removes the whole case |
| IV antibiotics given more than 24 hours before presentation | Counting oral or prophylactic doses `[VERIFY]` |
| Administrative contraindication (patient or surrogate refusal) documented in the window | Inferring refusal from a missed draw |

## 3. Severe sepsis present and severe sepsis presentation time

**Clinical criteria route.** All three met within 6 hours of each other `[VERIFY span wording]`:

1. Documentation of an infection, suspected infection or source (provider or nursing documentation as the data dictionary allows `[VERIFY]`).
2. Two or more SIRS criteria. Thresholds as reported in CMS training: temperature over 38.3 C or under 36.0 C; heart rate over 90; respiratory rate over 20; WBC over 12,000 or under 4,000 per microliter, or over 10 percent bands `[VERIFY each inequality]`.
3. One or more organ dysfunction criteria: SBP under 90 or MAP under 65 (or an SBP fall of more than 40 mm Hg from a documented baseline, with documentation); creatinine over 2.0 or urine output under 0.5 mL/kg/hour for 2 hours; bilirubin over 2 mg/dL; platelets under 100,000; INR over 1.5 or aPTT over 60 seconds; lactate over 2 mmol/L; acute respiratory failure with a new need for invasive or non-invasive mechanical ventilation `[VERIFY each]`.

A value a provider documents as due to a chronic condition or a medication, not to infection, is not used `[VERIFY]`.

**Provider documentation route.** Physician, APN or PA documentation of "severe sepsis" or "septic shock"; documentation that does not say the patient has severe sepsis is disregarded, and documentation earlier than the clinical criteria sets the presentation time (CMS Q&A). Handling of "rule out" and later-negated language follows the version's data dictionary `[VERIFY]`.

**Presentation time.** The earlier of (a) the time the last of the three clinical criteria was met inside the 6-hour span, and (b) the time of qualifying provider documentation. Training material also describes using the ED triage time when all criteria were met at triage `[VERIFY in the 5.18a data dictionary]`. Not time zero: the sepsis alert or best-practice-advisory fire time, an order-set time, arrival time when criteria were not yet met, a sepsis navigator's "recognition" time, or a time chosen by the bedside team for the hour-1 bundle.

## 4. Septic shock present and septic shock presentation time

Severe sepsis present plus any of: initial lactate of 4 mmol/L or more; hypotension that persists in the hour after the target crystalloid volume is infused; or provider documentation of septic shock `[VERIFY]`. When the route is the lactate, training material treats the lactate result time as the septic shock time if it is later than severe sepsis presentation `[VERIFY]`. Septic shock presentation time starts the 6-hour vasopressor and reassessment clocks, and starts the crystalloid clock only when no earlier initial hypotension did.

## 5. Bundle elements and windows

Each timed element has its own trigger and clock. Do not run every septic shock element from septic shock presentation: when the fluid trigger is initial hypotension, septic shock is not yet established, because persistent hypotension after the fluids is what establishes it.

| Element | Required when | Clock starts at | Window |
|---|---|---|---|
| Initial lactate | Severe sepsis present | Severe sepsis presentation | 6 hours before through 3 hours after |
| Blood cultures | Severe sepsis present | Severe sepsis presentation | Collected before the antibiotic and by 3 hours after; look-back 48 hours `[VERIFY]` |
| Antibiotic from the manual's tables | Severe sepsis present | Severe sepsis presentation | Started by 3 hours after; look-back 24 hours `[VERIFY]` |
| Repeat lactate | Initial lactate over 2 | Severe sepsis presentation (not the initial lactate time) | By 6 hours after |
| 30 mL/kg crystalloid | Initial hypotension, or septic shock (including initial lactate of 4 or more) | The earlier of initial hypotension and septic shock presentation | Ordered and started 6 hours before through 3 hours after |
| Vasopressor | Persistent hypotension after the target crystalloid volume | Septic shock presentation | By 6 hours after |
| Repeat volume status and tissue perfusion assessment | Septic shock present (persistent hypotension or initial lactate of 4 or more) | Septic shock presentation | After crystalloid completion and by 6 hours after |

The antibiotic element is met by one agent from the monotherapy table, or by agents from two different classes on the combination table with both started in the window (CMS Q&A); table contents change by version, so check the agent against the version's tables.

SEP-1 is all-or-none: one failed element fails the case. A case that is excluded or not in the population is neither a pass nor a fail.

## 6. Crystalloid volume and weight rules

- Target is 30 mL/kg of crystalloid; an ordered volume within 10 percent below target is accepted, but the 10 percent allowance does not apply to the volume actually infused (v5.16 training). The measure sets no time by which the ordered volume must finish infusing (2019 Q&A).
- Actual weight is the default. Ideal, predicted, adjusted or dosing weight is accepted when a physician, APN or PA documents obesity (BMI over 30) and directs that weight for the target volume (v5.8 training; adjusted weight accepted when so directed, 2024 Q&A).
- An order for less than 30 mL/kg is accepted only when provider documentation meets the manual's listed criteria (reason such as heart failure or renal failure, the volume ordered, in the window) `[VERIFY the 5.18a criteria]`.
- Only crystalloids named by the manual count; blood products, albumin and maintenance-rate infusions do not `[VERIFY]`.

## 7. Persistent hypotension, vasopressors and reassessment

- Persistent hypotension is assessed in the hour after the target volume is completely infused and requires two consecutive hypotensive readings in that hour (CMS composite-measure training); a single low reading followed by a normal one does not establish it.
- Initial hypotension (the fluid trigger) is two hypotensive readings, not necessarily consecutive, within 3 hours of each other (CMS Q&A for v5.5a); confirm the v5.18a wording `[VERIFY]`. Version 5.3a set no maximum gap, so older worksheets differ.
- Vasopressor: a qualifying agent from the manual's table, started within 6 hours of septic shock presentation when hypotension persists.
- Reassessment: after crystalloid completion and within 6 hours of septic shock presentation, either a physician, APN or PA attestation that a volume status and tissue perfusion assessment was performed, or the alternative routes the manual lists (a focused exam; or measures such as central venous pressure, central venous oxygen saturation, bedside cardiovascular ultrasound, passive leg raise or fluid challenge) `[VERIFY current wording]`. A note signed before the crystalloid finished does not count.

## 8. Timestamp conventions

| Event | Use | Do not use |
|---|---|---|
| Lactate, blood cultures | Specimen collection time (result time where the manual says so for a criterion) `[VERIFY]` | Order time |
| Antibiotic, crystalloid, vasopressor | Administration or infusion start time on the MAR | Order, verification or dispense time |
| Provider documentation | Time of the entry or the time stated in it, per the manual's rule for that element `[VERIFY]` | Signature time of a later addendum |

## 9. Frequent abstraction errors

- Crystalloid clock run from septic shock presentation when the trigger was initial hypotension.
- An agent not on the monotherapy table given alone, or only one agent of a combination started in the window; both agents of a combination must start within 3 hours.

- Repeat lactate clock anchored to the initial lactate instead of presentation time.
- Antibiotic judged against one hour (an SSC aspiration) instead of the SEP-1 3-hour window.
- 30 mL/kg required for a lactate between 2 and 3.9 with no hypotension.
- Bolus volume computed on actual weight where the provider documented obesity and directed ideal weight.
- Severe sepsis taken from a SOFA score or the word "sepsis" in a note.
