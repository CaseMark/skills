---
name: classifying-imaging-findings
language: en
description: Applies standardized classification systems (BI-RADS, LI-RADS, TI-RADS, Lung-RADS, PI-RADS) to imaging findings. Use when categorizing imaging findings, applying RADS classifications, or determining follow-up recommendations.
tags:
  - radiology
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

# Classifying Imaging Findings

Applies standardized classification systems (BI-RADS, LI-RADS, TI-RADS, Lung-RADS, PI-RADS) to imaging findings.

## Why This Skill Exists

Radiology classification systems translate complex imaging findings into standardized categories with defined management pathways. These systems — BI-RADS (breast), LI-RADS (liver), TI-RADS (thyroid), Lung-RADS (lung cancer screening), PI-RADS (prostate), and others — are mandated by the ACR for their respective organ systems and represent decades of evidence-based development. Incorrect classification directly impacts patient management: an under-classified breast lesion may delay cancer diagnosis; an over-classified thyroid nodule may lead to unnecessary biopsy. Medicare and many commercial payers require appropriate RADS classification for reimbursement. The Joint Commission and ACR accreditation programs audit classification accuracy as a quality metric.

Each classification system uses specific imaging features scored against defined criteria to produce a category that maps to a management recommendation. Radiologists must understand the precise criteria, applicable modality, and patient-population requirements for each system. This skill consolidates the major RADS systems into a single reference with their scoring rubrics, management algorithms, and common pitfalls.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Which classification system is required?** (Default: Determine from organ system and modality)
2. **What imaging modality was used?** (Default: Identify — CT, MRI, US, mammography, PET/CT)
3. **Is the patient in a screening or diagnostic population?** (Default: Diagnostic)
4. **What is the patient's relevant risk history?** (Default: Average risk — update with actual history)
5. **Are prior studies available for comparison?** (Default: No priors)
6. **Is the patient in the appropriate population for this classification system?** (Default: Verify eligibility)

### Documents to Request

- Current imaging study with all sequences/phases
- Prior imaging in the same modality for comparison
- Relevant clinical history (cancer history, risk factors, cirrhosis status, PSA levels)
- Prior biopsy results if applicable
- Requisition with clinical indication

---

## Step 1: Select the Appropriate Classification System

| Organ System | Classification | Applicable Modality | Population Requirement |
|-------------|---------------|--------------------|-----------------------|
| Breast | BI-RADS (5th ed.) | Mammography, US, MRI | All breast imaging |
| Liver | LI-RADS v2018 | CT, MRI (with extracellular or hepatobiliary contrast) | At-risk for HCC (cirrhosis, chronic HBV, prior HCC) |
| Thyroid | ACR TI-RADS 2017 | Ultrasound | All thyroid nodules on US |
| Lung | Lung-RADS v1.1 | Low-dose CT | LDCT lung cancer screening only |
| Prostate | PI-RADS v2.1 | Multiparametric MRI (T2W, DWI, DCE) | Pre-biopsy or active surveillance |
| Ovary | O-RADS | Ultrasound, MRI | Adnexal masses |
| Kidney | Bosniak v2019 | CT, MRI | Renal cystic masses |
| Adrenal | ACR Incidental Findings | CT, MRI | Incidentally discovered adrenal nodules |
| Coronary | CAD-RADS 2.0 | Coronary CTA | Suspected coronary artery disease |

**Critical rule:** Never apply a classification system outside its intended population (e.g., LI-RADS only applies to patients at risk for HCC, not all liver lesions).

---

## Step 2: Apply the Classification Criteria

### BI-RADS (Breast Imaging)

| Category | Assessment | Management | Cancer Likelihood |
|----------|-----------|------------|------------------|
| 0 | Incomplete | Additional imaging needed | N/A |
| 1 | Negative | Routine screening | 0% |
| 2 | Benign | Routine screening | 0% |
| 3 | Probably benign | Short-interval follow-up (6 months) | ≤2% |
| 4a | Low suspicion | Biopsy recommended | 2–10% |
| 4b | Moderate suspicion | Biopsy recommended | 10–50% |
| 4c | High suspicion | Biopsy recommended | 50–95% |
| 5 | Highly suggestive of malignancy | Biopsy required | ≥95% |
| 6 | Known malignancy | Surgical management | 100% |

### LI-RADS (Liver — HCC Risk Population Only)

| Category | Criteria | Management |
|----------|---------|------------|
| LR-1 | Definitely benign | Return to surveillance |
| LR-2 | Probably benign | Return to surveillance |
| LR-3 | Intermediate probability | Repeat diagnostic imaging in 3–6 months |
| LR-4 | Probably HCC | Multidisciplinary discussion; may biopsy |
| LR-5 | Definitely HCC | Treat as HCC without biopsy |
| LR-M | Probably or definitely malignant, not HCC-specific | Biopsy to determine histology |
| LR-TIV | Tumor in vein | Treat as HCC with vascular invasion |

**LI-RADS major features:** arterial-phase hyperenhancement (APHE), nonperipheral "washout," enhancing "capsule," size, threshold growth (≥50% increase in ≤6 months).

### Lung-RADS v1.1 (LDCT Screening Only)

| Category | Finding | Management |
|----------|---------|------------|
| 1 | Negative: no nodules, or definite benign (calcified) | Annual LDCT |
| 2 | Benign appearance: solid <6 mm, part-solid <6 mm total | Annual LDCT |
| 3 | Probably benign: solid 6–8 mm, part-solid ≥6 mm with solid <6 mm | 6-month LDCT |
| 4A | Suspicious: solid 8–15 mm, growing <8 mm | 3-month LDCT or PET/CT |
| 4B | Very suspicious: solid ≥15 mm, new/growing ≥8 mm | Tissue sampling or PET/CT + short-interval CT |
| 4X | Additional suspicious features | As for 4A/4B with consideration of additional workup |

### PI-RADS v2.1 (Prostate MRI)

| Category | Assessment | Likelihood of Significant Cancer |
|----------|-----------|--------------------------------|
| 1 | Very low | Clinically significant cancer highly unlikely |
| 2 | Low | Clinically significant cancer unlikely |
| 3 | Intermediate/equivocal | Equivocal |
| 4 | High | Clinically significant cancer likely |
| 5 | Very high | Clinically significant cancer highly likely |

**Zone-specific dominant sequence:** T2W for transition zone; DWI/ADC for peripheral zone.

---

## Step 3: Document the Classification

For every classified finding, the report must include:

1. **Finding description** — size, location, morphologic features
2. **Scoring features** — itemize each criterion used (e.g., TI-RADS points per category)
3. **Assigned category** — explicit category with system version (e.g., "BI-RADS 4B per 5th edition")
4. **Management recommendation** — per the classification algorithm
5. **Comparison** — change from prior classification if available
6. **Caveats** — any features that could upgrade/downgrade the category

### Documentation Template
```
[Organ] [Location]: [Size] [descriptor]
- Features: [list scored features]
- Classification: [System] [Category] ([version])
- Recommendation: [Management per algorithm]
- Prior: [Change from prior or "no prior comparison"]
```

---

## Step 4: Handle Edge Cases and Discordance

| Scenario | Action |
|----------|--------|
| Features span two categories | Assign the higher category and document rationale |
| Technical limitation prevents scoring a feature | Note limitation; consider recommending repeat study |
| Prior biopsy yielded benign but imaging is suspicious | Recommend re-biopsy or short-interval follow-up with clear documentation |
| Patient outside target population (e.g., LI-RADS for non-cirrhotic) | Do NOT apply the system; describe findings descriptively |
| Multiple classification systems could apply | Apply the most specific system; note others considered |
| Subcentimeter lesion below size threshold | Document as "too small to characterize" with follow-up recommendation |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the correct classification system applied for the organ, modality, and population?
2. Are all individual scoring features documented?
3. Does the assigned category match the scoring criteria exactly?
4. Is the management recommendation consistent with the assigned category?
5. Are edge cases and limitations explicitly documented?

---

## Quality Audit

- [ ] Classification system version is stated (e.g., LI-RADS v2018, BI-RADS 5th ed.)
- [ ] Patient eligibility for the classification system is confirmed
- [ ] Each scored feature is individually documented
- [ ] Total score/category is stated explicitly
- [ ] Management recommendation matches the assigned category
- [ ] Finding is measured in the correct axis per system requirements
- [ ] Comparison with prior classification is included when available
- [ ] Multiple lesions are each individually classified
- [ ] Lesions below size thresholds are handled per system-specific rules
- [ ] Caveats and technical limitations are noted
- [ ] Report avoids applying classification systems outside their intended population
- [ ] Category assignment is not modified based on clinical suspicion (classifications are imaging-based)
- [ ] The specific management pathway is spelled out (not just the category number)

---

## Guidelines

1. Always state the classification system version — criteria change between editions and versioning prevents ambiguity.
2. Never apply LI-RADS to patients without established HCC risk factors (cirrhosis, chronic HBV, prior HCC).
3. Lung-RADS applies exclusively to low-dose CT lung cancer screening; do not use it for diagnostic CTs or incidental nodules.
4. For BI-RADS, always document density category (A through D) separately from the assessment category.
5. PI-RADS scoring uses a zone-specific dominant sequence — misapplying T2W as the dominant sequence in the peripheral zone is a common error.
6. When a lesion's features straddle two categories, assign the higher category and document the reasoning.
7. TI-RADS requires itemized point scores for all five feature categories — do not skip features or assign a level without documentation.
8. If a classification system does not apply, describe findings using standardized descriptors without forcing a RADS category.
