# Reperfusion Clocks, Quality Measures and Discharge Rules

Working map of the time targets, quality measures and discharge documentation items that an ACS case review relies on. It separates four kinds of authority that use the same words for different things: the 2025 ACC/AHA/ACEP/NAEMSP/SCAI ACS guideline (clinical recommendations with a Class of Recommendation and Level of Evidence), the CMS STEMI eCQM CMS996 (a reported measure with its own population and timestamps), the 2017 AHA/ACC STEMI/NSTEMI performance measures (measure specifications), and the NCDR Chest Pain-MI Registry (a registry data dictionary). Each source, URL and check date is in `references/primary-sources.md`. Guideline statements are population recommendations; never restate one as an order for a patient.

## Contents

1. Framework map
2. Clock table: each element with its own trigger
3. First medical contact: three definitions
4. CMS STEMI eCQM CMS996v6 (CY 2026 reporting)
5. 2017 AHA/ACC STEMI/NSTEMI performance measures used here
6. Fibrinolysis: the guideline contraindication table versus measure exclusions
7. NSTE-ACS invasive timing
8. Discharge and secondary prevention documentation items
9. Frequent errors

## 1. Framework map

| Question | Governing source | What it is | What it is not |
|---|---|---|---|
| What time target is recommended for this patient group? | 2025 ACC/AHA/ACEP/NAEMSP/SCAI ACS guideline (Rao et al.; JACC and Circulation, Feb. 27, 2025; corrections Mar. 31, June 23 and Nov. 10, 2025, none changing a time target) | Clinical recommendation with COR and LOE | A measure; it defines no denominator, exclusions or exceptions |
| Did the hospital meet a CMS-reported STEMI measure? | CMS996v6, "Appropriate Treatment for STEMI Patients in the ED", required in Hospital OQR for CY 2026 | eCQM with population, exclusions, exceptions | A clinical judgment of the care |
| Did the case meet an ACC/AHA performance measure? | 2017 AHA/ACC Clinical Performance and Quality Measures for STEMI and NSTEMI (still the current MI set listed by JACC as of 2026-10-30) | Measure specification (PM-1 to PM-17, QM-1 to QM-7) | A guideline recommendation |
| What does the registry abstract? | NCDR Chest Pain-MI Registry data dictionary (v3.2 decision reported in JACC: Advances, Sept. 2026) | Data element definitions | A CMS measure |

Report each framework on its own row. A case can meet the CMS eCQM and miss a guideline goal, or the reverse.

## 2. Clock table: each element with its own trigger

Each row names its own start event, stop event and target. Never assume one anchor for all of them.

| Element | Start event (trigger) | Stop event | Target | Source |
|---|---|---|---|---|
| ECG acquisition and interpretation, prehospital | First medical contact (guideline definition, Section 3) | 12-lead ECG acquired and interpreted | 10 minutes | 2025 guideline, 3.1.1 rec 1 (COR 1, LOE B-NR) |
| ECG acquisition and interpretation, in hospital | Presentation with suspected ACS | ECG acquired and interpreted | 10 minutes | 2025 guideline, 3.1.2 rec 1 (1, B-NR) |
| Repeat troponin | Initial sample collection (time zero) | Repeat sample | 1 to 2 hours hs-cTn; 3 to 6 hours conventional cTn | 2025 guideline, 3.1.2 rec 4 (1, B-NR) |
| Primary PCI, direct presentation or EMS to PCI-capable hospital | First medical contact | First device activation | 90 minutes or less | 2025 guideline, 3.1.1 rec 3 (1, B-NR) and 5.2.1 rec 1 (1, A) |
| Primary PCI, transfer from non-PCI-capable hospital | First medical contact (at or before the referral hospital) | First device activation at the receiving hospital | 120 minutes or less | 2025 guideline, 5.2.1 rec 1 (1, A); 2017 PM-11 |
| Choice of fibrinolysis at a non-PCI-capable hospital | First medical contact, symptom onset under 12 hours | Anticipated delay to PCI | Fibrinolysis indicated if anticipated FMC-to-device delay exceeds 120 minutes and no contraindication | 2025 guideline, 5.3 rec 2 (1, A) |
| Transfer after fibrinolysis | Fibrinolytic administration | Transfer to a PCI-capable center | Immediately | 2025 guideline, 5.3.2 rec 1 (1, A) |
| Angiography after fibrinolysis | Fibrinolytic administration | Angiography | 2 to 24 hours (immediate if failed reperfusion suspected) | 2025 guideline, 5.3.2 recs 2-3 (1, B-R) |
| Hospital arrival to fibrinolysis (DTN) | Hospital arrival | Fibrinolytic administration | 30 minutes or less | 2017 PM-7; CMS996v6 uses ED arrival |
| Door-in-door-out at the referral hospital (DIDO) | ED arrival at the STEMI referral facility | ED discharge from that facility | 30 minutes or less | 2017 PM-10 |
| eCQM transfer criterion | ED arrival | Discharge to an acute care facility | 45 minutes or less | CMS996v6 numerator |
| eCQM PCI criterion | ED arrival | PCI device deployment (not procedure start) | 90 minutes or less | CMS996v6 numerator and guidance |
| Immediate invasive strategy, unstable NSTE-ACS | Hospital admission | Angiography with intent to revascularize | Under 2 hours | 2025 guideline, 6.1 rec 3 (1, C-LD) and supportive text |
| Early invasive strategy, high-risk NSTE-ACS | Decision for invasive strategy (trial anchors were symptoms, randomization or diagnosis) | Angiography | Within 24 hours (reasonable) | 2025 guideline, 6.1 rec 4 (2a, B-R) |
| Angiography, NSTE-ACS not high risk | Admission | Angiography | Before discharge (reasonable) | 2025 guideline, 6.1 rec 5 (2a, B-R) |
| LVEF assessment | Admission | LVEF documented | Before discharge | 2025 guideline, 10.4 (1, C-LD); 2017 PM-5 |
| Cardiac rehabilitation referral | Admission | Referral to an outpatient CR program | Before discharge | 2025 guideline, 10.5.3 rec 1 (1, A); 2017 PM-12 |
| CMR in MINOCA work-up | Presentation | CMR | Ideally within 2 weeks | Fifth UDMI 2026, Section 11 (citing practice guidelines) |

The 2025 guideline text was searched in full for a door-to-needle number and a door-in-door-out number and states neither; those 30-minute targets live in the measures (PM-7, PM-10, CMS996v6). The CMS996 rationale attributes the 30-minute fibrinolysis target to the 2013 STEMI guideline.

## 3. First medical contact: three definitions

| Source | Definition |
|---|---|
| 2025 ACS guideline (footnote to 3.1.1) | "The time point when the patient is initially assessed by a health care professional who can obtain and interpret the ECG and deliver initial interventions (eg, defibrillation)." For EMS-transported patients the goal runs from FMC by EMS to reperfusion. |
| NCDR Chest Pain-MI Registry v3.2 | The steering subcommittee kept "date and time when the patient was first evaluated by EMS before arrival at the first facility" for EMS-transported patients (JACC: Advances, Sept. 14, 2026). The data dictionary itself was not read `[VERIFY]`. |
| 2017 PM-11 | FMC "at or before ED arrival at STEMI referral facility". |
| CMS996v6 | Uses no FMC; every interval starts at ED arrival. |

For a walk-in patient the guideline definition can point to arrival, triage or the first ECG-capable assessment. Compute every plausible reading, show which one each framework uses, and state whether the result changes.

## 4. CMS STEMI eCQM CMS996v6 (CY 2026 reporting)

- Population: all ED encounters for patients 18 or older at the start of the encounter with a STEMI diagnosis during an ED encounter that ends in the measurement period; denominator equals the initial population. Episode-based: report each ED encounter.
- Numerator: ED arrival to fibrinolysis 30 minutes or fewer; or PCI within 90 minutes of arrival; or discharge to an acute care facility within 45 minutes of arrival. Guidance: use PCI device deployment time, not procedure start time.
- Denominator exclusions (v6, summarized): allergic reaction to a thrombolytic during the encounter; bleeding or bleeding diathesis, known malignant intracranial neoplasm, known structural cerebral vascular lesion, advanced dementia, pregnancy, or allergy to thrombolytics present at the start; active oral anticoagulant therapy at the start or within 90 days; within 24 hours before or during the encounter, aortic dissection or ruptured aneurysm, angina with documented spasm, heart or ventricular aneurysm, Takotsubo syndrome, severe neurologic impairment, mechanical circulatory assist placement or removal, intubation, or cardiopulmonary arrest or traumatic or prolonged CPR over 10 minutes; major surgery within 21 days; ischemic stroke, significant facial or closed head trauma, or peptic ulcer within 90 days; intracranial or intraspinal surgery within 90 days; expired in the ED; left against medical advice; hospice in the prior 6 months or active at the start.
- Denominator exceptions (v6): fibrinolytic therapy at another facility within 24 hours; a documented reason for not giving fibrinolytic therapy within 30 minutes; a documented reason for not performing PCI within 90 minutes.
- Reporting: required in Hospital OQR for CY 2026 (three self-selected quarters, deadline May 17, 2027); v7 applies to CY 2027. OP-2 and OP-3 (chart-abstracted fibrinolysis within 30 minutes; median time to transfer) were removed after Q1 2023 encounters.
- How the measure treats a patient who bypasses the receiving hospital's ED straight to the cath lab is not stated on the measure page `[VERIFY]`.

## 5. 2017 AHA/ACC STEMI/NSTEMI performance measures used here

| Measure | Population note | Target |
|---|---|---|
| PM-7 Time to fibrinolytic therapy | Excludes patients received in transfer | Hospital arrival to fibrinolysis 30 minutes or less |
| PM-8 FMC-to-device time | Primary PCI patients; excludes patients received in transfer | 90 minutes or less |
| PM-10 Door-in-door-out | Seen first at a non-PCI-capable hospital and transferred | ED arrival to ED discharge at the referral facility 30 minutes or less |
| PM-11 Time to primary PCI among transferred patients | Transferred and received primary PCI | FMC to primary PCI 120 minutes or less |
| PM-12 Cardiac rehabilitation referral | Hospitalized with AMI | Referred to outpatient CR before discharge; exceptions for documented medical or system barriers |
| PM-5 Evaluation of LVEF; PM-13 P2Y12 inhibitor at discharge; PM-4 high-intensity statin at discharge | Inpatient STEMI and NSTEMI | As specified |

These measures count "STEMI or its equivalent" (hyperacute T waves, true posterior MI, multilead ST depression with ST elevation in aVR, diagnostic criteria with LBBB). Each has denominator exceptions for documented medical, patient or system reasons; read the measure text before scoring.

## 6. Fibrinolysis: the guideline contraindication table versus measure exclusions

2025 guideline Table 14 (advisory, "may not be all-inclusive or definitive"):

| Absolute | Relative |
|---|---|
| Any prior intracranial hemorrhage | History of chronic, severe, poorly controlled hypertension |
| Known structural cerebral vascular lesion | Significant hypertension on presentation (SBP over 180 or DBP over 110) |
| Known malignant intracranial neoplasm | History of prior ischemic stroke more than 3 months earlier |
| Ischemic stroke within 3 months, except acute ischemic stroke within 4.5 hours | Dementia |
| Suspected aortic dissection | Known intracranial pathology not covered as absolute |
| Active bleeding or bleeding diathesis (excluding menses) | Traumatic or prolonged (over 10 minutes) CPR |
| Significant closed-head or facial trauma within 3 months | Major surgery within 3 weeks |
| Intracranial or intraspinal surgery within 2 months | Internal bleeding within 2 to 4 weeks |
| Severe uncontrolled hypertension unresponsive to therapy (SBP over 180 or DBP over 110) | Noncompressible vascular punctures; pregnancy; active peptic ulcer; oral anticoagulant therapy |

- Streptokinase is no longer available in the United States (Table 13), so a checklist line about prior streptokinase exposure is a sign of an old template.
- Fibrinolysis for ST depression only is Class 3: Harm, except when true posterior STEMI is suspected (5.3 rec 4).
- The CMS996v6 exclusion list overlaps Table 14 but is a different instrument: an exclusion removes the case from the measure; it does not show that fibrinolysis was contraindicated. Pregnancy, dementia and oral anticoagulant therapy are relative contraindications in Table 14 yet measure exclusions.
- Whether fibrinolysis should have been given in a case with relative contraindications is a clinician judgment. The review reports the facts, the list the facility used, how its labels compare with Table 14, and routes the question to physician peer review.

## 7. NSTE-ACS invasive timing

- Intermediate or high risk and a revascularization candidate: invasive approach during hospitalization (1, A). Low risk: routine or selective invasive approach (1, A); selective-invasive patients should have noninvasive testing or CCTA before discharge.
- Refractory angina or hemodynamic or electrical instability: immediate invasive strategy (1, C-LD); supportive text gives under 2 hours from admission and immediate transfer from a non-PCI-capable hospital.
- High risk: early invasive within 24 hours is reasonable (2a, B-R). Supportive text lists GRACE over 140, diabetes, age over 75 and elevated biomarkers as favoring earlier angiography. The Figure 8 list of high-risk features was not extractable `[VERIFY]`.
- GRACE 2.0 and TIMI scores (Table 5) stratify risk in suspected or confirmed ACS; they are not diagnostic tools.

## 8. Discharge and secondary prevention documentation items

Check that each item is documented as done, declined, contraindicated with a reason, or deferred with an owner. Do not choose agents, doses or durations.

| Item | Guideline basis (2025 unless noted) |
|---|---|
| DAPT (aspirin plus oral P2Y12 inhibitor) for at least 1 year if not at high bleeding risk; documented bleeding-reduction strategy when used (ticagrelor monotherapy after 1 month post-PCI, de-escalation, single antiplatelet therapy) | 11.1 recs 1-5 (1, A to 2b, B-R) |
| PPI when at high gastrointestinal bleeding risk on DAPT or anticoagulant | 11.1 rec 3 (1, A) |
| High-intensity statin; nonstatin added if LDL-C 70 mg/dL or more on maximally tolerated statin (1, A); reasonable at 55-69 mg/dL (2a, B-R) | 4.5 recs 1, 2 and 4; lipid reassessment 11.2 |
| Oral beta-blocker started early (under 24 hours) without contraindication | 4.6 (1, A) |
| ACEi or ARB in LVEF 40 percent or less, hypertension, diabetes or anterior STEMI | 4.7 (1, A) |
| LVEF assessed before discharge | 10.4 (1, C-LD) |
| Medication reconciliation including sublingual nitroglycerin unless contraindicated | Table 21 |
| Outpatient CR referral placed before discharge; home-based CR a reasonable alternative | 10.5.3 (1, A; 2a, B-R); Table 21 "confirm referral to CR" |
| Patient education, follow-up appointments, barriers to medications and CR | Tables 20 and 21 |

Medicare Part B covers cardiac rehabilitation after an acute MI within the preceding 12 months (42 CFR 410.49(b)(1)(i)). The Fifth UDMI notes CR is less often offered after secondary MI; check referral regardless of MI class.

## 9. Frequent errors

- Receiving-hospital door-to-device reported as the patient's reperfusion time for a transfer.
- Procedure start or cath lab arrival used where device deployment governs.
- Registration or triage time substituted for ED arrival, or the reverse, without saying which framework uses which.
- A guideline goal reported as a measure result ("failed the 2025 guideline") or a measure result reported as guideline concordance.
- A measure exclusion read as a clinical contraindication.
- "Recommend cardiac rehab" or "follow up with cardiology" counted as a referral.
