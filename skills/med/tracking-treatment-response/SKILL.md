---
name: tracking-treatment-response
language: en
description: Monitors treatment response using imaging criteria, biomarkers, and clinical assessment with documentation. Use when assessing treatment response, documenting disease status, or tracking progression.
tags:
  - monitoring
  - oncology
  - clinical
  - treatment
metadata:
  author: casemark
  practice_areas:
    - Medical Oncology
    - Hematology-Oncology
    - Radiation Oncology
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---

# Tracking Treatment Response

Monitors treatment response using imaging criteria, biomarkers, and clinical assessment with documentation.

## Why This Skill Exists

Treatment response assessment determines whether to continue, modify, or discontinue cancer therapy. Incorrect response assessment leads to either premature discontinuation of effective therapy or continued exposure to toxic, ineffective treatment. RECIST 1.1 (Response Evaluation Criteria in Solid Tumors) is the international standard for solid tumor response assessment in clinical trials and increasingly in routine practice. Alternative criteria exist for specific contexts: iRECIST for immunotherapy, Lugano classification for lymphoma, RANO for CNS tumors, and mRECIST for hepatocellular carcinoma.

FDA drug approvals, clinical trial endpoints, and insurance continuation authorizations all depend on standardized response assessment. NCCN guidelines specify response assessment timing for each treatment regimen. Inconsistent measurement technique (different target lesions measured across time points, non-standard measurement methodology) introduces noise that obscures true response signal and leads to incorrect clinical decisions.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What cancer type and treatment is the patient receiving? (Default: [VERIFY])
2. What response criteria system is applicable (RECIST 1.1, iRECIST, Lugano, RANO, mRECIST)? (Default: RECIST 1.1 for solid tumors)
3. What is the baseline imaging date and documented baseline measurements? (Default: provide)
4. What target lesions were identified at baseline? (Default: document with measurements)
5. Are there non-target lesions and/or new lesions to track? (Default: document)
6. What imaging modality is being used for follow-up (CT, MRI, PET/CT)? (Default: same modality as baseline)
7. What is the assessment schedule per protocol or NCCN guideline? (Default: every 2–3 cycles or per guideline)
8. Are tumor markers being tracked concurrently? (Default: document if applicable)

### Documents to Request

- Baseline imaging with radiologist measurements of target lesions
- Current follow-up imaging with measurements
- All interval imaging studies for trend analysis
- Tumor marker serial values if applicable
- Treatment administration records (cycle dates, dose modifications)
- Clinical assessment notes (symptom changes, performance status)
- Prior response assessments for comparison
- Clinical trial protocol response assessment requirements if applicable

---

## Step 1: Apply RECIST 1.1 Criteria

**Baseline target lesion selection (at start of treatment):**
- Select up to 5 target lesions total, maximum 2 per organ
- Target lesions must be measurable: ≥10mm in longest diameter for non-nodal lesions, ≥15mm in short axis for lymph nodes
- Measure by CT with ≤5mm slice thickness; use calipers for consistent measurement
- Document each target lesion: location, measurement (mm), imaging modality, date

**Non-target lesions:** All other disease sites documented but not measured — tracked qualitatively as present/absent/unequivocal progression.

**Response categories:**

| Response | Target Lesions | Non-Target Lesions | New Lesions |
|----------|---------------|-------------------|-------------|
| **Complete Response (CR)** | All target lesions disappeared; all nodes <10mm short axis | All non-target lesions disappeared | No |
| **Partial Response (PR)** | ≥30% decrease in sum of longest diameters from baseline | Non-PD | No |
| **Progressive Disease (PD)** | ≥20% increase in sum AND ≥5mm absolute increase from nadir | Unequivocal progression | Yes (any new lesion) |
| **Stable Disease (SD)** | Neither PR nor PD criteria met | Non-PD | No |

**Key measurement rules:**
- Always compare current sum to baseline (for PR) AND to nadir (for PD)
- Lymph nodes: use short axis measurement; nodes that decrease to <10mm are considered normal but still included in sum
- Lesions too small to measure: record as 5mm (not zero) to avoid artificial "complete response"
- Lesion that cannot be measured due to coalescence: assign estimated measurement

---

## Step 2: Apply Modified Criteria for Special Contexts

**iRECIST (for immunotherapy):**
- First apparent progression = iUPD (immune unconfirmed progressive disease)
- Confirm progression with repeat imaging 4–8 weeks later
- If confirmed: iCPD (immune confirmed progressive disease) — true progression
- If not confirmed (stable/shrinkage): reset baseline — pseudoprogression resolved
- Pseudoprogression occurs in 5–10% of immunotherapy patients; most common in melanoma

**Lugano Classification (for lymphoma):**
- Uses PET/CT (Deauville 5-point scale) for FDG-avid lymphomas
- Deauville 1–3 = metabolic CR; Deauville 4–5 with decreased uptake = PR; Deauville 4–5 with increased uptake or new lesions = PD
- CT-based criteria used for non-FDG-avid lymphomas

**RANO Criteria (for CNS tumors):**
- Measures enhancing and non-enhancing disease separately
- Requires consideration of corticosteroid dose (steroid increase without tumor growth is not response)
- Pseudoprogression common after temozolomide + radiation (occurs within first 3–6 months)

**mRECIST (for HCC):**
- Measures viable (arterially enhancing) tumor, not total tumor size
- Necrotic/non-enhancing areas after locoregional therapy are not measured

---

## Step 3: Integrate Imaging with Clinical and Biomarker Assessment

Response assessment should integrate three data streams:

1. **Imaging response** per applicable criteria (RECIST 1.1, iRECIST, etc.)
2. **Biomarker response** (tumor markers trending per interpreting-tumor-markers skill)
3. **Clinical response** (symptom improvement, performance status change, weight change)

**Discordance management:**

| Imaging | Biomarkers | Clinical | Likely Assessment |
|---------|-----------|---------|-------------------|
| PR | Declining | Improving | True response — continue treatment |
| SD | Rising | Stable | Mixed response possible — consider additional imaging or biopsy |
| PD | Declining | Stable | Pseudoprogression possible (especially with immunotherapy) — confirm with repeat imaging |
| SD | Stable | Declining | Clinical progression may precede radiographic progression — escalate evaluation |

When discordance exists, document each data stream separately and provide an integrated clinical assessment with rationale.

---

## Step 4: Document the Response Assessment

Structure each response assessment as:

1. **Assessment date** and imaging modality/date
2. **Target lesion measurements:** Each lesion with current measurement, baseline measurement, nadir measurement, and percent change from baseline and from nadir
3. **Sum of target lesions:** Current, baseline, nadir, percent change
4. **Non-target lesion status:** Present/absent/unequivocal progression for each
5. **New lesions:** Present/absent — if present, document location and size
6. **Overall response:** CR, PR, SD, PD (or iCR, iPR, iSD, iUPD, iCPD for immunotherapy)
7. **Best overall response** to date
8. **Biomarker correlation** if applicable
9. **Clinical correlation:** Symptom trajectory, PS change
10. **Treatment recommendation:** Continue, modify dose, switch regimen, proceed to next planned phase

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are the same target lesions measured at each time point using the same imaging modality?
2. Is the response category correctly assigned per RECIST 1.1 (or applicable criteria) with supporting measurements?
3. Has progression been assessed against both baseline (for PR) and nadir (for PD)?
4. For immunotherapy patients, has iRECIST been applied with confirmation of suspected progression?
5. Is the response assessment correlated with biomarker trends and clinical status?

---

## Quality Audit

- [ ] Response criteria system specified (RECIST 1.1, iRECIST, Lugano, RANO, mRECIST)
- [ ] Baseline target lesions documented with measurements (up to 5 total, max 2 per organ)
- [ ] Same target lesions measured at each assessment time point
- [ ] Same imaging modality used across assessments (CT→CT, not CT→MRI)
- [ ] Sum of target lesion diameters calculated and compared to baseline and nadir
- [ ] Non-target lesion status documented (present/absent/progression)
- [ ] New lesions assessed and documented
- [ ] Response category correctly assigned per criteria with supporting arithmetic
- [ ] Pseudoprogression considered for immunotherapy and post-radiation contexts
- [ ] Biomarker correlation documented when applicable
- [ ] Clinical correlation (symptoms, PS) integrated into overall assessment
- [ ] Best overall response tracked across all assessments
- [ ] Treatment recommendation linked to response assessment
- [ ] Assessment timing aligned with protocol or NCCN guideline schedule

---

## Guidelines

- Always measure the same target lesions at each assessment — changing target lesions invalidates the response calculation
- Use the same imaging modality and ideally the same scanner for serial assessments — modality changes introduce measurement variability
- RECIST 1.1 response requires confirmation: PR must be confirmed on a subsequent scan ≥4 weeks later in clinical trial settings; SD must be documented at a minimum interval of 6–8 weeks from baseline
- A single new lesion, regardless of size, constitutes progressive disease in RECIST 1.1 — this is frequently missed
- For immunotherapy, always consider pseudoprogression before declaring PD — apply iRECIST and confirm with 4–8 week repeat imaging
- Bone-only disease is generally non-measurable per RECIST 1.1 — response in bone metastases requires supplementary criteria (sclerotic healing, decreased uptake on PET)
- Effusions (pleural, peritoneal) are non-measurable per RECIST 1.1 — do not use effusion volume for response assessment
- Radiologic response does not always equal clinical benefit — SD maintained for many months may represent meaningful clinical benefit, especially in indolent diseases
