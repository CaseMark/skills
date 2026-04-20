---
name: coding-radiology-services
language: en
description: Assigns radiology CPT codes with professional/technical component and supervision level documentation. Use when coding imaging studies, applying 26/TC modifiers, or coding interventional procedures.
tags:
  - coding
  - medical-coding-and-billing
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Coded Record
  skill_modes:
    - Coding
    - Classification
---

# Coding Radiology Services

Assigns radiology CPT codes (70010–79999) with correct professional/technical component billing, supervision level documentation, contrast material reporting, and interventional radiology procedure coding. Covers diagnostic radiology, ultrasound, nuclear medicine, radiation oncology, and image-guided interventional procedures.

## Why This Skill Exists

Radiology coding requires precise management of component billing (modifier 26/TC), multi-code procedures combining imaging guidance with interventional techniques, contrast administration rules, and CMS supervision requirements. Radiology generates high claim volumes with significant denial rates — the most common errors involve incorrect component billing, missing imaging guidance codes, failure to report contrast, and laterality mistakes. CMS technical component/professional component splits vary by code, and incorrect modifier application directly affects reimbursement.


Radiology coding complexity is increasing with the expansion of AI-assisted imaging, advanced interventional techniques, and hybrid imaging modalities (PET/MRI, SPECT/CT). CMS payment policies for radiology — including the Multiple Procedure Payment Reduction (MPPR) for the technical component, Appropriate Use Criteria (AUC) for advanced imaging, and packaging rules under OPPS — require ongoing vigilance.
---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What imaging study or procedure was performed?
2. What is the billing entity — physician practice, hospital outpatient department, or independent facility?
3. Is this a professional-only, technical-only, or global billing scenario?
4. Was contrast material used? (oral, IV, intrathecal, intra-articular)
5. Was image guidance used for an interventional procedure?
6. What is the anatomic site and laterality?
7. Is this a diagnostic or screening study? (affects ICD-10-CM diagnosis coding)

### Documents Required

- Radiology report (final interpretation with findings and impression)
- Procedure order with clinical indication
- Contrast administration documentation (type, route, volume)
- Interventional procedure notes (if applicable)
- Equipment/technical logs (for TC billing)
- Prior imaging for comparison (referenced in the report)
- Fluoroscopy time documentation (when applicable)

---

## Step 1 — Determine the Imaging Modality and Code Section

Identify the correct CPT subsection.

- **Diagnostic Radiology (70010–76499)**: X-ray, CT, MRI, fluoroscopy. Organized by anatomic region (head/neck, chest, spine, abdomen, extremities).
- **Diagnostic Ultrasound (76506–76999)**: Real-time sonography. Includes obstetric (76801–76828) and non-obstetric (76506–76776) subsections.
- **Radiologic Guidance (77001–77022)**: Fluoroscopic, CT, and MRI guidance for procedures. Often reported in addition to the interventional procedure code.
- **Radiation Oncology (77261–77799)**: Treatment planning, dosimetry, treatment delivery, brachytherapy.
- **Nuclear Medicine (78012–78999)**: Diagnostic and therapeutic nuclear medicine procedures.
- Each subsection has its own coding conventions — read the section guidelines before assigning codes.

### Radiology CPT Section Quick Reference

| CPT Range | Modality | Key Conventions |
|---|---|---|
| 70010-70559 | Head/Neck (X-ray, CT, MRI) | Contrast status differentiates codes |
| 71045-71552 | Chest (X-ray, CT, MRI) | View count matters for X-ray |
| 72020-72159 | Spine (X-ray, CT, MRI) | Level specificity required |
| 73000-73725 | Upper Extremity | Laterality modifiers required |
| 73501-73725 | Lower Extremity | Laterality modifiers required |
| 74018-74178 | Abdomen (X-ray, CT) | Combined abd/pelvis codes exist |
| 76506-76999 | Ultrasound | OB vs. non-OB subsections |
| 77001-77022 | Radiologic Guidance | Often reported with procedure code |
| 77261-77799 | Radiation Oncology | Planning, delivery, brachytherapy |
| 78012-78999 | Nuclear Medicine | Diagnostic and therapeutic |

## Step 2 — Apply Component Billing (26/TC)

Determine which component is being billed.

- **Global (no modifier)**: The same entity provides and bills for both the professional interpretation and the technical service (equipment, supplies, technologist). Common in freestanding radiology practices with their own equipment.
- **Modifier 26 — Professional component**: The radiologist's interpretation, report, and clinical correlation only. Used when the physician reads images taken at a hospital or another facility.
- **Modifier TC — Technical component**: The facility's equipment, supplies, technologist time, and overhead. Billed by the hospital outpatient department or imaging center.
- **Key rule**: The sum of 26 + TC RVUs equals the global RVU for each code. They are not additive beyond the global fee.
- Hospital-employed radiologists reading studies in the hospital: the hospital bills TC, the physician bills 26 (or the hospital bills global under the provider's NPI depending on employment arrangement).
- Never append 26 and TC on the same claim line from the same billing entity.

## Step 3 — Code Contrast Material Correctly

Apply contrast rules specific to each modality.

- **CT with contrast**: CPT differentiates "without contrast" (e.g., 70450), "with contrast" (70460), and "without contrast followed by with contrast" (70470). The "without followed by with" code is a separate study — not just adding contrast to an ongoing exam.
- **MRI with contrast**: Same structure — without (70551), with (70552), without followed by with (70553).
- **Oral contrast alone does not qualify** as "with contrast" for CT or MRI coding purposes. "With contrast" means IV, intrathecal, or intra-articular administration.
- **HCPCS contrast codes**: Report the contrast agent separately using HCPCS Level II codes (e.g., Q9965–Q9967 for low osmolar contrast, A9575–A9580 for MRI contrast).
- If both oral and IV contrast are administered for a CT, the code selection is based on the IV contrast (oral alone = "without contrast").

## Step 4 — Code Interventional Radiology Procedures

Apply multi-code conventions for image-guided interventions.

- Interventional radiology procedures typically require separate codes for: (1) the surgical/interventional procedure, (2) the imaging guidance (fluoroscopy, CT, or ultrasound), and (3) any radiological supervision and interpretation (RS&I).
- Some CPT codes bundle the imaging guidance — read the parenthetical notes carefully. Example: 36902 (dialysis circuit maintenance) includes fluoroscopic guidance — do not separately report 77001.
- When imaging guidance is separately reportable, match the guidance code to the modality: 76942 (ultrasound guidance), 77002 (fluoroscopic guidance), 77012 (CT guidance), 77021 (MRI guidance).
- Catheter placement codes: Code the most distal vessel selectively catheterized per vascular family. Non-selective catheterization into the aorta (36200) is included in selective catheterization codes.
- Report all vessels injected with separate RS&I codes when applicable.
- **Appropriate Use Criteria (AUC)** --- For advanced imaging (CT, MRI, PET, nuclear medicine), CMS requires ordering professionals to consult AUC through a qualified Clinical Decision Support Mechanism (CDSM) before ordering. Document the CDSM consultation result (appropriate, may be appropriate, not appropriate, not applicable) on the order. Claims must include the AUC consultation information (CDSM identifier, consultation result, ordering professional NPI)

## Step 5 — Apply Radiology-Specific Modifiers

Select modifiers beyond 26/TC as needed.

- **Modifier 50 — Bilateral**: For bilateral imaging studies (e.g., bilateral mammography, bilateral extremity X-rays). Some payers want modifier 50 on one line; others want RT/LT on separate lines.
- **Modifier 52 — Reduced service**: When fewer views or a limited study is performed compared to the code descriptor (e.g., 2-view chest X-ray code but only 1 view obtained).
- **Modifier 59 / XS — Separate structure**: When imaging different anatomic regions in the same session (e.g., CT abdomen and CT pelvis as separate studies rather than combined CT abdomen/pelvis).
- **Modifier 76 — Repeat by same physician**: Same imaging study repeated on the same date (e.g., repeat chest X-ray post-procedure).
- **Modifier 77 — Repeat by different physician**: Same study, different interpreting radiologist.
- **Laterality modifiers (RT/LT)**: Required for unilateral imaging of paired structures (extremities, eyes, breasts).

## Step 6 — Validate Diagnosis Coding for Medical Necessity

Link ICD-10-CM diagnoses to support the imaging order.

- The primary diagnosis should reflect the reason for the imaging study — the clinical indication, not the finding.
- Screening studies use Z-codes (e.g., Z12.31 for screening mammography) — do not use symptom codes unless symptoms are present.
- If abnormal findings are identified, report the finding codes as secondary diagnoses.
- Check LCD/NCD coverage requirements — some imaging studies have specific diagnosis code requirements for Medicare coverage (e.g., NCD 220.1 for CT colonography).
- Incidental findings should be coded if they are documented in the report and are clinically significant.

- **AI-assisted imaging coding** --- When AI/CAD is used to assist interpretation: if AI is used as a concurrent reader (radiologist reviews AI output), no additional CPT code is required. If a specific AI analysis is separately ordered and performed (e.g., coronary artery calcium scoring with AI quantification), check for applicable CPT codes. AI use should be documented in the radiology report but does not change the base interpretation code
---

## Checkpoint B — Review

- [ ] Correct CPT code selected for the modality, anatomic region, and contrast status
- [ ] Component modifier (26/TC/global) matches the billing entity's role
- [ ] Contrast reporting is accurate — IV/intrathecal contrast qualifies; oral alone does not
- [ ] Interventional codes are complete — procedure + guidance + RS&I as applicable
- [ ] Laterality modifiers are applied for unilateral studies of paired structures
- [ ] ICD-10-CM diagnoses support medical necessity for the study ordered
- [ ] Multi-study sessions have appropriate modifiers to distinguish separate studies

- [ ] AUC consultation documented for applicable advanced imaging orders
- [ ] AI-assisted interpretation documented in the report without incorrect additional coding
- [ ] MPPR impact assessed for multiple radiology procedures on the same date
---

## Quality Audit

- [ ] Component billing matches the provider/facility arrangement — no double-billing of global + 26
- [ ] Contrast codes (HCPCS) are reported separately when contrast is administered
- [ ] Bundled imaging guidance is not separately reported (check parenthetical notes)
- [ ] Screening vs. diagnostic coding is correct (Z-codes vs. symptom codes)
- [ ] Repeat study modifiers (76/77) include documented clinical necessity for the repeat
- [ ] LCD/NCD coverage requirements are met for Medicare-covered imaging services
- [ ] Interventional radiology RS&I codes are paired with corresponding procedure codes

- [ ] AUC/CDSM consultation results are captured for all applicable advanced imaging orders
- [ ] AI-assisted interpretation is documented in reports per organizational policy
- [ ] OPPS packaging rules checked for hospital outpatient radiology claims
- [ ] Multiple Procedure Payment Reduction (MPPR) impact is calculated for same-day multiple procedure claims
---

## Guidelines

- Follow CPT Radiology section guidelines and subsection notes for each modality
- Apply CMS Medicare Claims Processing Manual Chapter 13 for radiology billing rules
- Reference ACR Appropriateness Criteria for medical necessity support when needed
- Use AMA CPT Assistant radiology-specific articles for code interpretation
- Apply CMS OPPS rules for hospital outpatient radiology — some codes are packaged and not separately payable
- Never bill for a study that was not interpreted with a final written report
- Mark with [VERIFY] any code selection where the imaging modality, contrast status, or interventional components are ambiguous
- Include disclaimer that code assignment is based on documentation provided and payer-specific rules may affect reimbursement

- AUC compliance for advanced imaging ordering is a CMS requirement with payment implications. Educate ordering providers on AUC consultation requirements and ensure the CDSM is integrated into the EHR ordering workflow
- AI in radiology does not change the fundamental coding principle: a qualified radiologist must provide the interpretation and sign the report. AI-assisted analysis does not generate a separately billable service unless a specific CPT code applies