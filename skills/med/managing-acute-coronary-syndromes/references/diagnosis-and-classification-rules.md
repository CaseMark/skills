# Diagnosis, ECG, Troponin and MI Classification Rules

Rules for reading the diagnostic record of a suspected ACS encounter: ECG criteria and STEMI-equivalent patterns, troponin interpretation against the assay in use, the Fourth (2018) and Fifth (2026) Universal Definitions of MI, MINOCA, and how clinical classification maps (and does not map) to ICD-10-CM. The review records what the documentation shows and where it conflicts. It does not read ECGs as the final interpreter, assign a final diagnosis, or assign codes. Sources and check dates are in `references/primary-sources.md`.

## Contents

1. STEMI ECG criteria
2. STEMI equivalents and occlusion patterns
3. Troponin: the assay decides
4. Myocardial injury and MI: Fourth versus Fifth UDMI
5. MINOCA
6. ICD-10-CM FY 2027 mapping
7. Unstable angina and risk scores
8. Frequent errors

## 1. STEMI ECG criteria

New or presumed new ST elevation at the J-point in 2 or more contiguous leads: 1 mm or more in all leads other than V2-V3; in V2-V3, 2 mm or more in men 40 or older, 2.5 mm or more in men under 40, 1.5 mm or more in women of any age (2025 guideline Table 3, adapted from the Fourth UDMI; repeated in Fifth UDMI Table 5, "in the absence of bundle branch block and/or left ventricular hypertrophy").

NSTE-ACS ECG evidence: new horizontal or downsloping ST depression 0.5 mm or more in 2 contiguous leads and/or T-wave inversion over 1 mm in 2 contiguous leads with prominent R wave or R/S over 1, or transient ST elevation (2025 Table 3). A normal or nonspecific ECG does not exclude ACS. Serial 12-lead ECGs are Class 1 when the initial ECG is nondiagnostic (3.1.2 rec 2, 1, B-NR; 3.1.1 rec 2 for a prehospital ECG nondiagnostic of STEMI); that recommendation is scoped to a nondiagnostic first ECG. When the first ECG shows ST depression in V1-V3, the governing text is the posterior-lead statement instead: "Posterior ECG leads (V7-V9) should be applied in patients with ongoing symptoms and a nondiagnostic ECG and those with ST-segment depressions in leads V1-V3" (3.1.1 supportive text; Table 3). In NCDR ACTION, 11 percent of patients finally diagnosed with STEMI had a nondiagnostic first ECG.

ST elevation also occurs in pericarditis, LVH, LBBB, Brugada syndrome, RV pacing, Takotsubo syndrome and early repolarization (2025 Table 3 footnote).

## 2. STEMI equivalents and occlusion patterns

| Pattern | Criteria as published | Source |
|---|---|---|
| Posterior MI | ST depression in V1-V3 (0.5 mm or more triggers posterior leads in the 2025 guideline; the Fifth UDMI cites 1 mm or more), dominant R in V1 or V2, upright anterior T waves; confirmed by ST elevation 0.5 mm or more in at least one of V7-V9 (1 mm or more in men under 40, Fourth UDMI) | 2025 Table 3 and 3.1.2 text; 2022 ACC ECDP Table 1; Fourth UDMI Section 28; Fifth UDMI Section 13 |
| LBBB or ventricular paced rhythm with Sgarbossa criteria | Concordant ST elevation 1 mm or more in leads with positive QRS (5 points); concordant ST depression 1 mm or more in V1-V3 (3 points); discordant ST elevation 5 mm or more (2 points); total 3 or more. Smith-modified: ST/S ratio of 25 percent or more replaces the 5 mm rule | 2022 ACC ECDP Table 1; Fifth UDMI Table 5 |
| New LBBB alone | Not a STEMI equivalent in isolation; a new LBBB in an asymptomatic patient is not a STEMI equivalent | 2025 Table 3 footnote; 2022 ECDP |
| New LBBB or RBBB with other signs of ischemia | May be considered equivalent to STEMI in the right clinical setting | Fifth UDMI Section 13 |
| de Winter T waves | Tall, prominent, symmetrical T waves from upsloping ST depression over 1 mm at the J-point in precordial leads; 0.5-1 mm ST elevation in aVR may be seen; proximal LAD occlusion, warrants immediate angiography | 2022 ECDP Table 1 and text; Fifth UDMI Table 5 |
| Hyperacute T waves | Broad, symmetric T waves disproportionate to the QRS in 2 contiguous leads; serial ECGs at short intervals | 2022 ECDP; Fifth UDMI Table 5 |
| aVR elevation with multilead ST depression | Usually diffuse subendocardial ischemia from left main or multivessel disease; listed among the 2017 PM "STEMI equivalents" | 2022 ECDP Table 1; 2017 PMs |
| Right ventricular MI | ST elevation in V3R-V6R; right-sided leads in suspected inferior STEMI | 2025 3.1.2 text; Fifth UDMI Section 13 |

Up to 1 in 4 patients managed as NSTEMI without classical ST elevation have an acutely occluded culprit artery (Fifth UDMI Section 13). Fibrinolysis for ST depression alone is Class 3: Harm except when true posterior STEMI is suspected (2025, 5.3 rec 4).

The review asks whether the documentation shows the pattern was looked for (posterior or right-sided leads, comparison with prior ECG, serial ECGs, Sgarbossa assessment) and what the treating clinician concluded. It does not convert an NSTEMI to a STEMI on its own reading; an ECG question goes to `interpreting-emergency-ecgs` and to physician review.

## 3. Troponin: the assay decides

- Myocardial injury: a troponin value above the 99th percentile upper reference limit (URL), which is assay-specific (2025 3.1.2 text; Fourth UDMI Section 25). The Fifth UDMI requires sex-specific 99th percentile URLs to define injury (Box 1; Section 14.1.1); the female URL is lower than the uniform URL and, for the newest hs-cTnT assay, half the male URL.
- Acute injury: a rise and/or fall with at least one value above the URL. Chronic injury (Fifth UDMI Box 2): two or more values above the URL in a stable setting; a change under 20 percent favors chronic, a criterion based only on assay imprecision.
- Delta values are assay-specific and cannot be transferred between assays; absolute deltas are preferred near the URL (Fifth UDMI 14.1.4; 2022 ECDP definitions).
- Accelerated diagnostic pathways (0-hour, 0/1-hour, 0/2-hour, High-STEACS) use assay-specific thresholds, often uniform rather than sex-specific, for risk stratification; they do not define injury or confirm MI (Fifth UDMI 14.1.5). The 0/3-hour 99th-percentile approach is not recommended by the 2022 ECDP.
- Timing: repeat at 1-2 hours (hs-cTn) or 3-6 hours (conventional) from the first sample (2025, 1, B-NR). A single-sample rule-out needs symptom onset at least 3 hours before the draw (2025 3.1.2 text). Troponin can be below the URL in about 1 in 6 STEMI patients in the first hours (Fifth UDMI 14.1.3); never delay reperfusion for a troponin result.
- Units: hs-cTn is reported in ng/L; conventional assays often in ng/mL. Check the unit and the assay generation on the report before comparing with any threshold.
- Interference: suspect it when values are inconsistent with the clinical picture or vary without pattern; repeat on an alternative assay (Fifth UDMI 14.1.2).

The review records, for every value: assay and generation, unit, sample collection time, time from symptom onset, the lab's 99th percentile URL (sex-specific where the lab reports one), the pathway in use and its thresholds. Missing assay information is an unknown fact, not a reason to borrow a threshold from another assay.

## 4. Myocardial injury and MI: Fourth versus Fifth UDMI

| Situation | Fourth UDMI (2018) | Fifth UDMI (2026) |
|---|---|---|
| Atherothrombotic MI | Type 1 | Primary MI |
| SCAD, coronary embolism, vasospasm | Type 2 | Primary MI |
| Stent thrombosis, restenosis, graft failure | Stent thrombosis type 4b and restenosis type 4c at any time after the procedure; type 5 only for CABG-related MI within 48 hours | Primary MI if more than 30 days after the procedure; procedure-related if within 30 days |
| Supply-demand imbalance from another acute condition | Type 2 (needs one ischemia feature: symptoms, new ischemic ECG change, pathological Q waves, or imaging) | Secondary MI: considered with one clinical or ECG feature; confirmed by obstructive CAD (70 percent or more, or 50 percent or more and flow-limiting) without acute coronary pathology, or new regional wall motion abnormality or loss of viable myocardium |
| Cardiac death before testing | Type 3 | Term removed; classify by setting |
| PCI or CABG complication | Types 4a and 5 with troponin multiples | Procedure-related MI within 30 days; no troponin multiple |
| Troponin rise and fall without ischemia | Acute myocardial injury (non-ischemic) | Acute myocardial injury (Table 2 lists mechanisms) |

The Fifth UDMI was published in late August and September 2026 (European Heart Journal, JACC and Circulation). The 2025 ACS guideline and the FY 2027 ICD-10-CM guidelines still use the Fourth UDMI type language. A record may therefore use either vocabulary, and an older note "type 2 MI due to vasospasm" maps to Fifth UDMI primary MI. State which definition each statement in the record uses; never translate silently.

## 5. MINOCA

- AHA 2019 scientific statement: MINOCA requires an acute MI by Fourth UDMI criteria, no stenosis of 50 percent or more in any major epicardial vessel, and no specific alternative diagnosis (sepsis, pulmonary embolism, myocarditis). It is a working diagnosis at angiography until other causes are excluded; re-review of the angiogram may be required.
- Fifth UDMI: renamed "myocardial injury with non-obstructive coronary arteries", a working, not final, diagnosis. CMR is recommended, ideally within 2 weeks; MI is the final diagnosis in 22-27 percent after CMR, which more often shows myocarditis or Takotsubo syndrome. When MI is confirmed, classify it as primary, secondary or procedure-related.
- The 2025 ACS guideline covers type 1 MI and refers type 2 MI, SCAD and MINOCA to separate documents.
- ICD-10-CM FY 2027 I.C.9.e.6: I21.B covers MI with coronary microvascular dysfunction, including MINOCA with microvascular disease. A discharge diagnosis of "MINOCA" alone with no work-up is a documentation gap, not a final classification.

## 6. ICD-10-CM FY 2027 mapping

Effective October 1, 2026 (guideline section I.C.9.e):

- I21.0-I21.4 are for type 1 MI only; I21.3 for type 1 STEMI without site; I21.4 for type 1 NSTEMI. A type 1 NSTEMI that evolves to STEMI is coded STEMI; a STEMI converted to NSTEMI by thrombolysis stays STEMI.
- Type 2 MI ("due to demand ischemia or secondary to ischemic imbalance"): I21.A1 with the underlying cause first. If a type 2 MI is described as NSTEMI or STEMI, assign only I21.A1. Do not assign I24.89 for the demand ischemia.
- Types 3, 4a-4c and 5: I21.A9. I22 only when both MIs are type 1 or unspecified.
- I21.9 is the default for unspecified AMI or unspecified type.
- Non-ischemic myocardial injury (acute, chronic or unspecified): I5A (tabular; new FY 2022; seen on a secondary code site).

The coder assigns codes from provider documentation. When the documentation conflicts ("NSTEMI" in the discharge summary, "demand ischemia" or "troponin leak" in progress notes), the review lists the conflict and routes a non-leading query to `managing-cdi-programs`. How a Fifth UDMI term such as "secondary MI" or "primary MI due to SCAD" should be coded in ICD-10-CM has no official guidance found as of 2026-10-30 `[VERIFY]`.

## 7. Unstable angina and risk scores

- Unstable angina: ischemic symptoms with MI excluded by serial troponin; less common with hs-cTn; still part of the ACS spectrum (Fifth UDMI Section 10).
- GRACE 2.0, TIMI UA/NSTEMI and TIMI STEMI scores (2025 Table 5) stratify risk; they are not diagnostic and do not decide the MI class. Recompute a score only from documented values and show each input with its source.

## 8. Frequent errors

- A troponin over a borrowed or uniform threshold called MI with no rise and fall and no ischemic feature.
- An ADP "rule-in" threshold treated as the diagnostic 99th percentile, or the reverse.
- A conventional troponin in ng/mL compared with an hs threshold in ng/L.
- "Troponin leak", "demand ischemia" or "type 2 MI" in progress notes and "NSTEMI" in the discharge summary, with I21.4 coded and no query.
- A new LBBB treated as automatic STEMI, or ST depression in V1-V3 treated as NSTEMI without posterior leads.
- MINOCA recorded as a final diagnosis with no CMR, no angiogram re-review and no alternative diagnosis excluded.
- A Fifth UDMI term translated into a Fourth UDMI type, or into a code, without saying so.
