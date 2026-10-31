# HCC Model and Coding Rules

Rules for locking the model and period, screening each encounter, validating each diagnosis, and mapping supported codes to HCCs. Every rule names its source; the full citation and the date checked are in the primary sources file. Items marked `[VERIFY]` were not confirmed in primary text.

## Contents

1. Model and period lock
2. Encounter eligibility: source, provider, telehealth, signature, date
3. Diagnosis support under ICD-10-CM Section IV
4. History-of conditions and OIG high-risk groups
5. HCC mapping, hierarchies and RAF arithmetic
6. V24 to V28 label changes that cause errors
7. ACA HHS-HCC differences

## 1. Model and period lock

Medicare Advantage CMS-HCC models are prospective: the payment year uses diagnoses from dates of service in the prior calendar year (CY 2027 Rate Announcement: "Final risk adjusted payments for CY 2027 will be based on diagnoses from CY 2026 dates of service").

| Payment year (MA, non-PACE) | Dates of service | CMS-HCC model | Source |
|---|---|---|---|
| 2024 | 2023 | 67% 2020 model (V24) + 33% 2024 model (V28) | CY 2024 Rate Announcement |
| 2025 | 2024 | 33% 2020 model + 67% 2024 model | CY 2025 Rate Announcement |
| 2026 | 2025 | 100% 2024 model (phase-in complete) | CY 2026 Rate Announcement |
| 2027 | 2026 | 100% 2024 model, continued; no recalibration | CY 2027 Rate Announcement (April 2026) |

Other year-specific parameters:

- PACE: 2026 blends 10% 2024 model with 90% 2017 model; 2027 blends 50% and 50%. ESRD beneficiaries use the ESRD models (2027: 2023 ESRD models for non-PACE). Route ESRD-model questions as a scope gap.
- MA coding pattern adjustment: 5.90% for CY 2026 and CY 2027. Normalization factor for the 2024 CMS-HCC model: 1.067 (2026), 1.079 (2027). Both reduce the raw score.
- CY 2027 sources of diagnoses (non-PACE): diagnoses from unlinked chart review records (CRRs) with 2026 dates of service are excluded, except for beneficiaries who switch to a contract in a different parent organization; records whose risk-adjustment-eligible lines all carry modifier 93 or FQ (audio-only) are excluded (PACE included). CMS delayed both exclusions to the CY 2027 midyear model run (HPMS memo, July 9, 2026).
- RADV data collection period: the calendar year before the audited payment year (PY 2024: January 1 to December 31, 2023). An inpatient record counts only if its discharge date falls in that period.
- Each run has its own dates-of-service window and its own submission deadline, 8 pm ET (HPMS memos, April 28, 2025 and April 29, 2026):

| Run | Dates of service | Submission deadline |
|---|---|---|
| PY 2026 initial | 07/01/2024-06/30/2025 | Sept. 5, 2025 |
| PY 2026 mid-year | 01/01/2025-12/31/2025 | Mar. 6, 2026 |
| PY 2026 final | 01/01/2025-12/31/2025 | Feb. 1, 2027 |
| PY 2027 initial | 07/01/2025-06/30/2026 | Sept. 4, 2026 |
| PY 2027 mid-year | 01/01/2026-12/31/2026 | Mar. 5, 2027 |
| PY 2027 final | 01/01/2026-12/31/2026 | Jan. 31, 2028 |
| PY 2028 initial | 07/01/2026-06/30/2027 | Sept. 3, 2027 |

- After the final deadline CMS pays nothing for newly submitted diagnoses but still processes deletes in later runs (42 CFR 422.310(g); April 28, 2025 memo). A late deletion is still a deletion.

## 2. Encounter eligibility: source, provider, telehealth, signature, date

Screen the encounter before reading its diagnoses. A diagnosis from an ineligible encounter is "Ineligible source" whatever the note says. A date outside the payment year's period is "Outside period for PY <year>", not an ineligible source: check every run in the Section 1 table whose window holds the date and whose deadline is still open on the review date (on 2026-10-30, a 2025 date of service still counts for the PY 2026 final run, deadline Feb. 1, 2027).

| Test | Rule | Source |
|---|---|---|
| Acceptable source | Hospital inpatient, hospital outpatient and physician only. All diagnoses must be documented in the medical record as a result of a face-to-face visit | Medicare Managed Care Manual (MMCM) ch. 7, §40, §120.1.1 |
| Diagnostic radiology | Not acceptable for risk adjustment, whether billed by the outpatient department or as the physician component; confirmation comes from the referring provider | MMCM ch. 7, §120.1.1 |
| Invalid record sources in RADV | Hospice, home health, lab only, superbill, non-face-to-face encounters (INV5) | PY 2024 RADV methods, App. A |
| Acceptable provider types | Only specialties on CMS's Acceptable Physician Specialty Types list for the payment year. The PY 2026 list (2025 dates of service) includes nurse practitioner, physician assistant, clinical nurse specialist, clinical psychologist, licensed clinical social worker, physical and occupational therapists, optometry and chiropractic; it omits diagnostic radiology and registered dietitian | CMS PY 2025 and PY 2026 lists (identical) |
| Excluded providers | Do not submit data from a provider excluded by OIG | MMCM ch. 7, §120.1.1 |
| Telehealth (MA) | Meets the face-to-face requirement only when delivered by real-time interactive audio and video (modifier 95). Audio-only (modifier 93 or FQ) does not; PHE-era telehealth flexibility ended May 11, 2023 | HPMS memo May 4, 2022; PY 2024 RADV methods, fn. 16-17; CY 2027 Rate Announcement |
| Signature | Legibly signed by the credentialed provider who conducted the visit; an electronic signature needs an attestation statement such as "signed by" or "authenticated by" (INV2 missing signature) | PY 2024 RADV methods, §6 fn. 15, App. A |
| Credentials | Credential (MD, DO, NP, PA) or specialty reference for the one named provider (INV7) | PY 2024 RADV methods, App. A |
| Unsigned note outside RADV | Cannot determine until the rendering provider authenticates it under the facility's late-signature policy; never signed by another clinician; the late signature is dated when made | Policy election; PY 2024 RADV methods, §6 fn. 15 for the RADV standard |
| Attestation | In RADV only, a CMS-generated attestation, signed by the provider who rendered the service, may cure a missing signature or credential on physician or outpatient records; never inpatient records; altered or non-CMS forms and forms signed by someone else are invalid | PY 2024 RADV methods, §6.4 |
| Date | Complete date of service (INV4) inside the data collection period (INV14); for submissions, inside the window of a run whose deadline is still open | PY 2024 RADV methods, App. A; HPMS deadline memos |
| Health risk assessment | May be submitted in RADV as an outpatient record type; it still must meet every test above, and each diagnosis still needs support in that visit's documentation | PY 2024 RADV methods, §6.1 |

## 3. Diagnosis support under ICD-10-CM Section IV

The FY 2027 ICD-10-CM Official Guidelines govern dates of service from October 1, 2026; FY 2026 guidelines govern October 1, 2025 to September 30, 2026. Section IV lettering below is FY 2027; check the year's lettering before citing.

- IV.J: code all documented conditions that coexist at the encounter and require or affect patient care, treatment or management. Do not code conditions previously treated that no longer exist. History codes (Z80-Z87) may be secondary when the history affects current care.
- IV.H: do not code "probable", "suspected", "questionable", "rule out", "compatible with", "consistent with", "working diagnosis" or similar; code the sign, symptom or abnormal finding instead.
- IV.I: chronic diseases treated on an ongoing basis may be coded each time the patient receives treatment and care for them. The encounter must still show that care.
- IV.F.3: code to the highest specificity the record supports, and no higher.
- I.A.19: code assignment rests on the provider's diagnostic statement, not on clinical criteria. A coder may not derive a CKD stage from an eGFR, a heart failure type from an ejection fraction or malnutrition severity from weight loss; without the provider's words, code the unspecified form or raise a query candidate.
- I.B.9: assign only the combination code when it fully identifies the conditions. I50.23 (acute on chronic systolic heart failure) already includes the chronic component, so I50.22 beside it is Not supported.
- I.A.15: "with" in a code title, the Alphabetic Index or a Tabular instructional note presumes a causal link unless the documentation says the conditions are unrelated. Refusing E11.22 for documented type 2 diabetes and CKD with no other cause stated is an error in the other direction. The N18 note "Code first any associated: diabetic chronic kidney disease (... E11.22 ...)" is confirmed in the FY 2027 Tabular List; the Index entry itself is `[VERIFY]`.
- IV.K: for diagnostic-services-only encounters, code confirmed diagnoses in a physician's interpretation. This is a coding rule for the radiology claim; it does not make diagnostic radiology an acceptable risk adjustment source. Name the conflict when a user cites IV.K.
- I.B.14: code assignment rests on the documentation of the patient's provider. BMI (Z68) is reported only with an associated reportable diagnosis, such as obesity, documented by the patient's provider.

What does not support a code on its own: a problem list entry, past medical history, a medication list, a superbill or encounter form, a lab value, an imaging report, a template that carries forward unchanged, or a diagnosis in a referral or prior-authorization form. Each is a lead to find evidence in the provider's assessment, never the evidence itself.

MEAT (monitor, evaluate, assess, treat) and TAMPER (treatment, assessment, monitor or medicate, plan, evaluate, referral) are industry evidence checklists, not CMS or ICD-10-CM rules. Use them to find text showing that the condition "required or affected" care at that visit under IV.J; cite the guideline, not the acronym, as the rule.

## 4. History-of conditions and OIG high-risk groups

- Malignancy (I.C.2.m): code the primary malignancy while treatment is directed to it. When it was excised or eradicated, no further treatment is directed to that site and there is no evidence of existing malignancy, use Z85 (personal history). Adjuvant therapy status changes the answer; record whether treatment is ongoing.
- Stroke (I.C.9.d): I63 is the acute event. Without neurologic deficits, use Z86.73, not I69 and not I63. Secondary-prevention drugs (antiplatelet, statin) do not make a past stroke current.
- Myocardial infarction (I.C.9.e): I21 may be reported while the infarction is four weeks old or less; after that, care related to it uses the guideline's later codes.
- OIG toolkit (report A-07-23-01213; errors as of November 2023) found these groups miscoded at high rates: acute stroke (96% of 945 sampled), acute heart attack (95%), embolism (79%), lung cancer (88%), breast cancer (96%), colon cancer (94%), prostate cancer (89%), potentially mis-keyed codes (81%). Its acute stroke group was an acute stroke diagnosis on one physician claim with no matching inpatient or outpatient hospital claim, where a history-of-stroke code (no HCC) typically should have been used.

## 5. HCC mapping, hierarchies and RAF arithmetic

The 2024 CMS-HCC model has 115 payment HCCs (CY 2024 Rate Announcement, Table VIII-1). Map each supported code with the CMS crosswalk for the payment year's model, then apply Table VIII-4: when a higher HCC in a hierarchy is present, drop the lower ones.

| Hierarchy (2024 model) | Higher HCC drops |
|---|---|
| Cancer 17 > 18 > 19 > 20 > 21 > 22 > 23 | each drops every lower number in the chain |
| Diabetes 35 (pancreas transplant) > 36 > 37 > 38 | 36 drops 37, 38; 37 drops 38 |
| Heart failure 221 > 222 > 223 > 224 > 225 > 226 > 227 | 224 drops 225, 226, 227; 226 drops 227 |
| Stroke 248 > 249; paralysis 253 > 254 | 248 drops 249 |
| Vascular 263 | drops 264, 383, 409 |
| Lung 276 > 277 > 278 > 279 > 280 | 279 drops 280 |
| Kidney 326 > 327 > 328 > 329 | 327 drops 328, 329 |

Selected relative factors, Community, NonDual, Aged segment, before normalization and the coding adjustment (CY 2024 Rate Announcement, Table VIII-1): HCC 23 0.186; HCC 36, 37, 38 each 0.166 (constrained equal); HCC 48 0.186; HCC 155 0.299; HCC 222 and 223 each 2.505; HCC 224, 225, 226 each 0.360; HCC 227 0.189; HCC 249 0.239; HCC 280 0.319; HCC 327 0.514; HCC 328 and 329 each 0.127. Interactions include DIABETES_HF 0.112 and HF_CHR_LUNG 0.078; the model also adds a payment-HCC-count factor (D5 0.050 in this segment).

Arithmetic rules: show each factor with its segment and source; sum after the hierarchy, never before; state which components (demographic, interaction, count, normalization, coding adjustment) are included; recompute every total with a script. Never present a dollar impact without the county rate, bid and plan factors; label any per-member estimate as illustrative.

## 6. V24 to V28 label changes that cause errors

| 2020 model (V24) | 2024 model (V28) | Trap |
|---|---|---|
| HCC 17, 18, 19 diabetes tiers | HCC 36, 37, 38, coefficients constrained equal | A specificity change no longer moves the factor; pushing for "with complications" has no payment purpose |
| HCC 85 congestive heart failure | Heart failure HCCs 222-226 by type and acuity, under HCC 221 (heart transplant status); HCC 227 cardiomyopathy split out | Coding I50.23 and I50.22 together and counting 224 and 226 |
| HCC 21 protein-calorie malnutrition | No payment HCC | Suspect lists still prompting it |
| HCC 22 morbid obesity | HCC 48 | Old number on forms |
| HCC 59 major depressive, bipolar, paranoid | HCC 152 (psychotic features), 154 (bipolar), 155 (major depression, moderate or severe) | Mild or unspecified depression treated as a payment HCC |
| HCC 88 angina pectoris | Non-payment (HCC 230) | Stable angina prompted as a gap |
| HCC 108 vascular disease | HCC 263, 264; intermittent claudication non-payment (HCC 265) | Claudication or "PVD" prompted as a gap |
| HCC 111 COPD | HCC 280 | Old number |
| HCC 138 CKD stage 3 | HCC 328 (3B), 329 (3 except 3B) | Old number |

RADV enrollee data lists label each audited HCC with its model version (for example V24HCC19). Never relabel a V24 HCC with a V28 number in a RADV packet.

## 7. ACA HHS-HCC differences

- Concurrent model: benefit-year diagnoses predict the same benefit year's liability. Data come from the issuer's EDGE server. The 2027 benefit year models are recalibrated on 2021-2023 EDGE data (2027 Payment Notice, May 2026).
- HHS-HCC numbers and hierarchies differ from CMS-HCC numbers (the 2026 DIY instructions use the V08 HHS condition category crosswalk); never carry a CMS-HCC number into an ACA review.
- Source filtering: HHS filters institutional outpatient and professional claims using allowable CPT/HCPCS service codes listed in the benefit year's "Do It Yourself" (DIY) software instructions. An acceptable service is two-way, real-time interactive communication equivalent to a face-to-face encounter with a professional licensed to diagnose. Certain audio-only codes remain acceptable; asynchronous codes are not (HHS telehealth FAQ, March 11, 2026). Whether a specific code is on the 2026 list is `[VERIFY]` against the DIY instructions.
- HHS-RADV (45 CFR 153.630): an independent initial validation audit (IVA) by an entity the issuer engages, then a second validation audit (SVA) by HHS's contractor, validating medical records "according to industry standards for coding and reporting".
