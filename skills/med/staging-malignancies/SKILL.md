---
name: staging-malignancies
language: en
description: Applies AJCC/UICC TNM staging with pathologic parameters and prognostic groupings. Use when staging cancers, applying TNM criteria, or documenting pathologic staging.
tags:
  - pathology
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Report
  skill_modes:
    - Analysis
---

# Staging Malignancies

Applies AJCC/UICC TNM staging with pathologic parameters and prognostic groupings.

## Why This Skill Exists

Cancer staging is the single most important prognostic determinant and the primary driver of treatment selection across virtually all solid and many hematologic malignancies. The AJCC Cancer Staging Manual (8th edition, effective January 2018) and the UICC TNM Classification of Malignant Tumours (8th edition) provide the globally accepted framework for staging. A staging error — misclassifying pT3 as pT2 because of incorrect depth measurement, or undercounting lymph nodes causing inaccurate pN assignment — directly changes prognostic grouping and may lead to stage-inappropriate therapy (e.g., omission of adjuvant chemotherapy for under-staged disease).

CAP cancer protocols mandate synoptic reporting that includes pTNM assignment for every cancer resection specimen. The Commission on Cancer (CoC) requires AJCC staging for cancer registry reporting and benchmarking. Hospital cancer committees review staging accuracy as a quality metric. This skill ensures correct application of AJCC/UICC staging rules with full documentation of the parameters that determine each T, N, and M category.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Tumor site** — Primary anatomic site and subsite (e.g., sigmoid colon, not just "colon")? Default: not specified; flag [VERIFY].
2. **Specimen type** — Biopsy only (clinical staging) or resection specimen (pathologic staging)? Default: resection.
3. **Prior treatment** — Did the patient receive neoadjuvant therapy (chemotherapy, radiation, immunotherapy)? Default: no. If yes, use yp prefix.
4. **Clinical staging data** — Imaging, endoscopy, and clinical exam findings for cTNM? Default: not provided.
5. **AJCC edition** — Confirm 8th edition applies (cases diagnosed 2018 or later). Default: 8th edition.
6. **Histologic type** — WHO classification histologic type and grade? Default: per surgical pathology report.
7. **Biomarker data** — Are prognostic biomarkers available (e.g., ER/PR/HER2 for breast, MSI for colorectal)? Default: pending.

### Documents to Request

- Surgical pathology report with gross and microscopic findings
- CAP cancer protocol checklist for the specific organ site
- Imaging reports (CT, MRI, PET/CT) for clinical staging correlation
- Endoscopy or procedure reports
- Neoadjuvant treatment records if applicable
- Prior biopsy reports
- Molecular/biomarker results (IHC, FISH, NGS)
- AJCC Cancer Staging Manual 8th edition chapter for the specific site

---

## Step 1: Determine Staging Classification Type

Identify the correct staging prefix and classification:

| Prefix | Meaning | When to Use |
|---|---|---|
| c | Clinical staging | Based on physical exam, imaging, endoscopy, biopsy (before definitive treatment) |
| p | Pathologic staging | Based on surgical resection specimen with microscopic examination |
| yc | Post-neoadjuvant clinical | Clinical restaging after neoadjuvant therapy, before surgery |
| yp | Post-neoadjuvant pathologic | Pathologic staging of resection after neoadjuvant therapy |
| r | Recurrence | Staging at time of recurrence after disease-free interval |
| a | Autopsy | Staging determined at autopsy |

**Rules for staging classification:**
- pT requires resection of the primary tumor sufficient to evaluate the highest T category.
- pN requires removal of sufficient lymph nodes to evaluate the highest N category. The minimum lymph node count varies by site (e.g., 12 for colorectal per AJCC).
- pM can be assigned based on microscopic confirmation of distant metastasis from any source (biopsy or resection).
- cM1 can be used for pathologic staging grouping even without microscopic confirmation if imaging is definitive.

---

## Step 2: Assign T Category (Primary Tumor)

Apply site-specific T criteria from AJCC 8th edition. Key examples:

### Colorectal

| Category | Definition |
|---|---|
| Tis | Carcinoma in situ (intramucosal, lamina propria involvement only) |
| T1 | Invades submucosa |
| T2 | Invades muscularis propria |
| T3 | Invades through muscularis propria into pericolorectal tissues |
| T4a | Penetrates visceral peritoneum |
| T4b | Directly invades other organs or structures |

### Breast

| Category | Definition |
|---|---|
| Tis | DCIS or Paget disease with no invasive component |
| T1mi | Microinvasion <= 1 mm |
| T1a | > 1 mm but <= 5 mm |
| T1b | > 5 mm but <= 10 mm |
| T1c | > 10 mm but <= 20 mm |
| T2 | > 20 mm but <= 50 mm |
| T3 | > 50 mm |
| T4a | Chest wall invasion (not pectoralis muscle alone) |
| T4b | Skin ulceration/satellite nodules/edema |
| T4c | Both T4a and T4b |
| T4d | Inflammatory carcinoma |

### Lung

| Category | Definition |
|---|---|
| T1a | <= 1 cm |
| T1b | > 1 cm but <= 2 cm |
| T1c | > 2 cm but <= 3 cm |
| T2a | > 3 cm but <= 4 cm, or involves main bronchus (not carina), invades visceral pleura, or causes partial atelectasis |
| T2b | > 4 cm but <= 5 cm |
| T3 | > 5 cm but <= 7 cm, or invades chest wall/phrenic nerve/pericardium, or separate nodule in same lobe |
| T4 | > 7 cm, or invades mediastinum/diaphragm/heart/great vessels/recurrent nerve/esophagus/vertebra/carina, or separate nodule in different ipsilateral lobe |

---

## Step 3: Assign N Category (Regional Lymph Nodes)

Determine nodal status using site-specific criteria:

**General principles:**
- Count total lymph nodes examined and number with metastases.
- Measure the largest metastatic deposit.
- Note extranodal extension (ENE) when applicable (ENE is a staging criterion for head and neck cancers in AJCC 8th edition).

| Site | N1 | N2 | N3 |
|---|---|---|---|
| Colorectal | 1-3 positive regional LNs | 4-6 positive regional LNs (N2a) or >= 7 (N2b) | N/A |
| Breast | Mobile ipsilateral Level I/II axillary LN metastasis | Fixed/matted Level I/II axillary or ipsilateral internal mammary clinically detected | >= 10 axillary LNs, or infraclavicular, or ipsilateral supraclavicular |
| Lung | Ipsilateral peribronchial/hilar | Ipsilateral mediastinal or subcarinal | Contralateral mediastinal/hilar or any scalene/supraclavicular |

**Isolated tumor cells (ITCs)**: Clusters <= 0.2 mm in greatest dimension. Classified as pN0(i+); do not upstage.
**Micrometastases**: > 0.2 mm but <= 2.0 mm. Classified as pN1mi.

---

## Step 4: Assign M Category and Prognostic Stage Group

**M categories (all sites):**
- M0: No distant metastasis
- M1: Distant metastasis present (subclassify by site when applicable: M1a, M1b, M1c per site-specific rules)

**Prognostic stage grouping**: Combine T, N, M into the stage group using the AJCC 8th edition prognostic staging tables for each site.

**Site-specific prognostic factors** that modify stage grouping in AJCC 8th edition:

| Site | Prognostic Factors That Modify Staging |
|---|---|
| Breast | ER, PR, HER2, grade (Nottingham), oncotype DX (used for anatomic vs. prognostic stage) |
| Prostate | PSA, Grade Group (Gleason) |
| Thyroid (differentiated) | Age (< 55 vs. >= 55) |
| Esophageal/EGJ | Grade, location (for squamous) |
| Soft tissue sarcoma | Grade (FNCLCC), depth, site |

Document the complete staging:
- Anatomic stage group (T + N + M only)
- Prognostic stage group (T + N + M + biomarkers, when applicable)

---

## Step 5: Documentation and Reporting

Assemble the staging report as part of the synoptic pathology report:

1. **pT category**: With specific parameter values (e.g., "pT3: Tumor invades through muscularis propria into pericolorectal tissues, depth of invasion 4 mm beyond muscularis propria").
2. **pN category**: With counts (e.g., "pN1b: Metastatic carcinoma in 3 of 18 regional lymph nodes, no extranodal extension").
3. **pM category**: With source of confirmation (e.g., "pM1: Confirmed by liver biopsy").
4. **Stage group**: Anatomic and prognostic (e.g., "AJCC 8th Edition Prognostic Stage Group: IIA").
5. **Prefix designators**: yp, r, or a as applicable.
6. **Biomarker summary**: Results that affect prognostic grouping.
7. **Lymph node adequacy statement**: State whether minimum node count was met for the specimen type.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the correct AJCC 8th edition chapter applied for the primary tumor site?
2. Is the staging prefix correct (p, yp, c, r) based on the clinical scenario?
3. Does the pT assignment match the measured parameters (size, depth of invasion)?
4. Is the lymph node count sufficient for reliable pN staging (e.g., >= 12 for colorectal)?
5. Are prognostic biomarkers included when they modify the prognostic stage group (breast ER/PR/HER2, prostate PSA/Grade Group)?

---

## Quality Audit

- [ ] Correct AJCC 8th edition chapter identified for the primary tumor site
- [ ] Staging prefix (p, yp, c, r, a) correctly assigned
- [ ] T category based on measured tumor parameters (size, depth, invasion)
- [ ] N category includes total nodes examined and number positive
- [ ] Minimum lymph node count met for specimen type
- [ ] Extranodal extension assessed and documented where applicable
- [ ] ITCs and micrometastases classified correctly (pN0(i+), pN1mi)
- [ ] M category documented with source of confirmation
- [ ] Anatomic stage group assigned from TNM combination
- [ ] Prognostic stage group assigned incorporating biomarkers where applicable
- [ ] Treatment effect grading applied for post-neoadjuvant specimens (ypTNM)
- [ ] Stage group consistent with individual T, N, M categories (no arithmetic errors)
- [ ] CAP synoptic checklist staging fields completed
- [ ] Cancer registry reporting requirements met (CoC)

---

## Guidelines

- Always verify you are using the AJCC 8th edition (effective 2018); do not apply earlier editions to newly diagnosed cases
- Use the site-specific chapter — many sites have unique T definitions that differ substantially between organ systems
- Apply the correct prefix: yp for post-neoadjuvant resection, p for primary resection without pretreatment, c for clinical staging only
- When the lymph node count is below the recommended minimum, note this as a staging qualifier and state that the N category may be understaged
- Distinguish anatomic stage group (based solely on T, N, M) from prognostic stage group (incorporating biomarkers) — both should be documented for breast, prostate, and other sites where they differ
- For post-neoadjuvant specimens, apply the treatment effect grading system specified by the AJCC (e.g., Ryan system for rectal cancer, RCB for breast) in addition to ypTNM
- Isolated tumor cells (ITCs <= 0.2 mm) are classified as pN0(i+) and should not be counted as positive lymph nodes for staging purposes
- Report staging in the synoptic format per CAP cancer protocol; free-text staging without synoptic documentation does not meet CAP/CoC standards
