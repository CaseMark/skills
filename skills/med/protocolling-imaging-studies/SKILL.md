---
name: protocolling-imaging-studies
description: Selects appropriate imaging protocols based on clinical indication and patient factors. Use when choosing imaging protocols, selecting contrast parameters, or determining appropriate study type.
tags:
  - radiology
  - clinical
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Radiology
    - Diagnostic Imaging
  document_types:
    - Report
  skill_modes:
    - Analysis
---

# Protocolling Imaging Studies

Selects appropriate imaging protocols based on clinical indication and patient factors.

## Why This Skill Exists

Protocol selection is one of the most impactful decisions in radiology — an incorrectly protocolled study can miss the diagnosis entirely, requiring repeat imaging with additional radiation exposure, contrast administration, and cost. The ACR Appropriateness Criteria provide evidence-based guidelines for selecting the right imaging modality and protocol for over 200 clinical scenarios. Radiologists are responsible for reviewing orders, verifying clinical indications, selecting contrast type and phase timing, and ensuring patient safety considerations (allergy history, renal function, pregnancy) are addressed before the study is performed.

Protocol errors — wrong phase, wrong contrast agent, wrong body region — are among the most common "never events" in radiology departments. CMS reimbursement increasingly ties to appropriate-use criteria (AUC) through the Protecting Access to Medicare Act (PAMA), requiring clinical decision support consultation for advanced imaging. This skill ensures that every protocol decision is evidence-based, patient-safe, and clinically optimized.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **What is the clinical indication and specific clinical question?** (Default: Obtain from requisition — never protocol without this)
2. **What modality was ordered?** (Default: Verify modality matches indication per ACR Appropriateness Criteria)
3. **Does the patient have a contrast allergy?** (Default: No — verify in EMR)
4. **What is the patient's renal function (eGFR)?** (Default: Check within 30 days for IV contrast)
5. **Is the patient pregnant or possibly pregnant?** (Default: No — verify per institutional policy)
6. **Does the patient have implantable devices (pacemaker, stimulator, metallic implant)?** (Default: No — verify for MRI)
7. **Patient weight and body habitus?** (Default: Standard — adjust if >300 lbs or pediatric)
8. **Are there prior studies that should inform protocol selection?** (Default: Review prior imaging)

### Documents to Request

- Requisition with clinical indication and ICD-10 codes
- ACR Appropriateness Criteria for the clinical scenario
- Patient allergy history (contrast-specific)
- Recent lab values: eGFR/creatinine, TSH (if thyroid-related), coagulation (if intervention)
- MRI safety screening form (for MRI studies)
- Prior imaging reports to determine appropriate comparison protocol
- Institutional protocol library for scanner-specific parameters

---

## Step 1: Verify Modality Appropriateness

Before protocolling, confirm the ordered modality is appropriate per ACR Appropriateness Criteria.

| Clinical Scenario | Usually Appropriate | May Be Appropriate | Usually NOT Appropriate |
|------------------|--------------------|--------------------|----------------------|
| Acute chest pain, PE suspected | CTA chest | V/Q scan | Chest X-ray alone |
| Right lower quadrant pain, possible appendicitis | CT abdomen/pelvis with IV contrast | US (first-line if pediatric/pregnant) | MRI abdomen (limited availability) |
| New headache, worst of life | CT head non-contrast (then CTA) | MRI brain | Skull X-ray |
| Breast cancer staging | CT chest/abdomen/pelvis + bone scan or PET/CT | MRI body | Ultrasound body |
| Knee internal derangement | MRI knee without contrast | — | CT knee |
| Liver mass characterization, cirrhosis | MRI liver with extracellular or hepatobiliary contrast | Multiphase CT | Ultrasound alone |
| Acute stroke, <24 hours | CT head non-contrast + CTA head/neck | MRI brain with DWI | CT with contrast alone |

If the ordered modality is rated "Usually NOT Appropriate," contact the ordering provider to discuss alternatives.

---

## Step 2: Contrast Decision Matrix

### IV Iodinated Contrast (CT)

| Factor | Action |
|--------|--------|
| eGFR ≥30 mL/min | Safe to administer; standard protocol |
| eGFR <30 mL/min | Risk-benefit discussion; consider non-contrast or alternative modality |
| Dialysis-dependent | Can administer; no specific precautions for nephrotoxicity |
| Contrast allergy — mild (nausea, hives) | Premedication: prednisone 50 mg PO at 13h, 7h, 1h + diphenhydramine 50 mg PO/IV 1h before |
| Contrast allergy — severe (anaphylaxis) | Premedicate + consider alternative modality (MRI, US) |
| Metformin use | Hold 48h post-contrast if eGFR <30; standard care if eGFR ≥30 |
| Pregnancy | Iodinated contrast only if critical clinical need; discuss with referring provider |

### IV Gadolinium Contrast (MRI)

| Factor | Action |
|--------|--------|
| eGFR ≥30 mL/min | Group II agents (gadobutrol, gadoterate) are safe |
| eGFR <30 mL/min | Use Group II agents only; avoid Group I agents (NSF risk) |
| Prior gadolinium reaction | Premedicate per same protocol as iodinated contrast |
| Pregnancy | Gadolinium only if critical clinical need; document risk-benefit discussion |

### Oral Contrast

| Indication | Type | Timing |
|-----------|------|--------|
| Routine CT abdomen/pelvis | Positive oral (dilute barium) or neutral (water) | 60–90 min before scan |
| CT enterography | Neutral oral contrast (VoLumen) | 45–60 min before scan |
| Suspected perforation | Water-soluble (Gastrografin) | Never barium if perforation suspected |
| Pediatric | Flavored neutral oral contrast | Age-adjusted volume |

---

## Step 3: Phase Selection and Timing

### CT Phase Timing (Post-Injection)

| Phase | Delay | Primary Use |
|-------|-------|------------|
| Non-contrast | Pre-injection | Renal stones, hemorrhage, adrenal characterization (HU), calcium scoring |
| Arterial (early) | 25–30 sec | CTA (PE, aortic dissection, vascular mapping) |
| Late arterial | 35–40 sec | Liver (HCC detection — arterial phase hyperenhancement) |
| Portal venous | 60–70 sec | Most routine CT: abdomen, pelvis, liver metastases |
| Nephrographic | 90–100 sec | Renal mass characterization |
| Delayed | 3–5 min | Urothelial evaluation (CTU), adrenal washout |
| Delayed (10–15 min) | 10–15 min | Adrenal washout protocol |

### MRI Sequences by Clinical Question

| Clinical Question | Essential Sequences | Optional |
|------------------|--------------------|---------| 
| Liver mass (LI-RADS) | T1 in/out phase, T2 fat-sat, DWI, dynamic post-contrast (arterial, venous, delayed) | Hepatobiliary phase (if using Eovist/Primovist) |
| Brain tumor | T1, T2, FLAIR, DWI, T1 post-contrast, perfusion | Spectroscopy, SWI |
| Knee meniscus/ligament | PD fat-sat (sagittal, coronal), T1 sagittal, T2 axial | Post-contrast only if infection/tumor |
| Prostate (PI-RADS) | T2 (3 planes), DWI with ADC (b-value ≥1400), DCE | No rectal coil required at 3T |
| Spine (disc/stenosis) | T1 sagittal, T2 sagittal, T2 axial through levels of interest | Post-contrast if post-op or infection |

---

## Step 4: Patient-Specific Protocol Modifications

| Patient Factor | Modification |
|---------------|-------------|
| Pediatric (<18 years) | Reduce kVp, mAs (CT); shorter scan times (MRI); weight-based contrast dosing |
| Pregnant | Avoid ionizing radiation when possible; MRI without gadolinium preferred |
| Obese (>300 lbs) | Increase kVp to 140 (CT); use larger bore MRI; verify table weight limit |
| Pacemaker/ICD | MRI-conditional: verify device and lead compatibility; follow institutional MRI-safety protocol |
| Claustrophobia | Short-bore MRI, anxiolysis protocol, or open MRI if available |
| Renal transplant | Adjust contrast dose; document transplant kidney location |
| Prior surgical hardware | CT may be preferred over MRI (metal artifact); use MARS protocol on MRI |

---

## Step 5: Document the Protocol Decision

The protocol order must include:

1. **Modality and body region** — e.g., "CT abdomen and pelvis"
2. **Contrast** — type, dose, route, timing, premedication if applicable
3. **Phases** — specific acquisitions with timing
4. **Special instructions** — reformats, thin-slice reconstructions, breath-hold coaching
5. **Safety clearance** — allergy status, renal function, pregnancy status, MRI safety screening
6. **Clinical justification** — per ACR Appropriateness Criteria rating
7. **Protocol modification rationale** — if deviation from standard

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Does the protocol match the clinical question per ACR Appropriateness Criteria?
2. Is contrast safety verified (allergy, renal function, pregnancy)?
3. Are the correct phases included for the clinical indication?
4. Are patient-specific modifications documented?
5. Will the protocol detect the suspected pathology if present?

---

## Quality Audit

- [ ] Clinical indication is confirmed and documented before protocolling
- [ ] Modality selection aligns with ACR Appropriateness Criteria
- [ ] Contrast allergy history is verified and premedication ordered if needed
- [ ] Renal function (eGFR) is documented within acceptable time window
- [ ] Pregnancy status is verified per institutional policy
- [ ] MRI safety screening is completed for MRI studies
- [ ] Phase timing matches the clinical question
- [ ] Contrast dose is weight-appropriate (especially pediatric)
- [ ] Oral contrast type and timing are specified when applicable
- [ ] Protocol modifications for body habitus, hardware, or devices are documented
- [ ] Prior imaging is reviewed to ensure protocol consistency for comparison
- [ ] Radiation dose optimization (kVp, mAs reduction) is applied per ALARA
- [ ] Protocol is recorded in the institutional protocol tracking system

---

## Guidelines

1. Never protocol a study without reviewing the clinical indication — the indication determines the protocol, not the ordered CPT code.
2. Apply ACR Appropriateness Criteria to validate modality selection; contact the ordering provider if the ordered study is rated "Usually NOT Appropriate."
3. Use the lowest radiation dose that answers the clinical question (ALARA principle); reduce kVp from 120 to 100 for thin patients on CT.
4. For liver mass characterization in cirrhosis, ensure late arterial phase timing (35–40 seconds) — standard portal venous timing will miss arterial-phase hyperenhancement.
5. Premedication for contrast allergy requires 13 hours lead time; if emergent, use the accelerated protocol (methylprednisolone 40 mg IV q4h × 2 doses + diphenhydramine 50 mg IV).
6. Gadolinium in pregnancy requires documented risk-benefit discussion and should only be administered if the information is critical to maternal/fetal care.
7. When the ordered study does not match the clinical question, recommend the appropriate study — this is a core radiologist responsibility under PAMA/AUC requirements.
