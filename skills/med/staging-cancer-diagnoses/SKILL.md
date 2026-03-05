---
name: staging-cancer-diagnoses
description: Applies AJCC 8th edition TNM staging with pathologic and clinical stage documentation. Use when staging cancers, applying TNM classifications, or documenting cancer stage.
tags:
  - oncology
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Medical Oncology
    - Hematology-Oncology
    - Radiation Oncology
  document_types:
    - Report
  skill_modes:
    - Analysis
---

# Staging Cancer Diagnoses

Applies AJCC 8th edition TNM staging with pathologic and clinical stage documentation.

## Why This Skill Exists

Accurate cancer staging is the single most consequential classification in oncology — it determines treatment eligibility, prognosis, clinical trial candidacy, and insurance authorization. The AJCC 8th edition (effective January 2018) introduced site-specific prognostic stage groups for breast, prostate, and other cancers that incorporate biomarkers beyond anatomy alone. Incorrect staging leads to inappropriate treatment, denied claims, and flawed tumor registry data.

Commission on Cancer (CoC) accreditation requires documented staging per AJCC guidelines within established timeframes. State cancer registries mandated by the National Program of Cancer Registries (NPCR) and SEER depend on correct stage assignment. Errors discovered post-treatment can trigger CoC compliance reviews and affect facility quality metrics.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the primary cancer site and histologic type? (Default: specify ICD-O-3 topography and morphology codes)
2. Is this a clinical stage (cTNM), pathologic stage (pTNM), or post-therapy stage (ypTNM)? (Default: clinical)
3. Has definitive surgery been performed? If yes, provide surgical pathology report. (Default: pending)
4. What edition of AJCC staging is required? (Default: 8th edition)
5. Are biomarker results available (ER/PR/HER2 for breast, PSA/Gleason for prostate, etc.)? (Default: pending)
6. Is there evidence of distant metastasis on imaging? (Default: not assessed)
7. Has neoadjuvant therapy been administered prior to staging? (Default: no)
8. What is the laterality for paired organs? (Default: not applicable)

### Documents to Request

- Surgical pathology report with margin status and lymph node counts
- Diagnostic imaging reports (CT, PET/CT, MRI, bone scan)
- Biopsy/cytology reports with histologic grade
- Biomarker and molecular testing results
- Operative notes documenting extent of resection
- Prior staging documentation if restaging after treatment
- Endoscopy or bronchoscopy reports when applicable

---

## Step 1: Identify Primary Site and Apply Site-Specific Staging Rules

Confirm the primary cancer site using ICD-O-3 topography codes. Each AJCC chapter has site-specific rules — do not apply generic TNM criteria across sites.

**Key site-specific considerations in AJCC 8th edition:**

| Site | Major 8th Edition Change |
|------|-------------------------|
| Breast | Prognostic stage incorporates grade, ER, PR, HER2, Oncotype DX |
| Prostate | Prognostic stage uses PSA and Grade Group (replacing Gleason) |
| HPV+ Oropharynx | Separate staging system (p16 positive = different chapter) |
| Pancreas | T stage redefined by size (replacing vessel involvement) |
| Liver (HCC) | New staging chapter added |
| Cervix | Imaging and pathology now permitted for staging |

For each primary site, confirm: (a) correct AJCC chapter, (b) required biomarkers for prognostic staging, (c) applicable staging classification type (clinical vs. pathologic).

---

## Step 2: Assign T, N, and M Categories

**T (Primary Tumor):**
- TX: primary tumor cannot be assessed
- T0: no evidence of primary tumor
- Tis: carcinoma in situ
- T1–T4: increasing size and/or local extent (site-specific definitions)

**N (Regional Lymph Nodes):**
- NX: regional nodes cannot be assessed
- N0: no regional node metastasis
- N1–N3: increasing number or extent of regional node involvement
- Document method of assessment: clinical (cN), pathologic (pN), sentinel node (sn)

**M (Distant Metastasis):**
- M0: no distant metastasis (note: clinical M0 requires no confirmatory imaging — it is assigned when no evidence of metastasis exists)
- M1: distant metastasis present — subcategorize by site when applicable (M1a, M1b, M1c per site-specific rules)

Record the prefix for each category: c (clinical), p (pathologic), yp (post-neoadjuvant pathologic), yc (post-neoadjuvant clinical), r (recurrence).

---

## Step 3: Determine Anatomic and Prognostic Stage Groups

After assigning T, N, M categories, map to stage group:

**Standard anatomic stage grouping:**

| Stage | General Criteria |
|-------|-----------------|
| Stage 0 | Tis, N0, M0 |
| Stage I | Small primary, node-negative |
| Stage II | Larger primary or limited node involvement |
| Stage III | Locally advanced or significant node involvement |
| Stage IV | Distant metastasis (any T, any N, M1) |

For sites with prognostic staging (breast, prostate), apply biomarker modifiers. Example for breast: anatomic Stage IIA (T2N0M0) may become Prognostic Stage IA if ER+/PR+/HER2−, Grade 1, and favorable Oncotype DX score.

Always document both anatomic and prognostic stage groups when prognostic staging is defined for the site.

---

## Step 4: Document Stage with Required Data Elements

Each stage assignment must include:

1. **Staging basis** — clinical, pathologic, or post-therapy
2. **T category** with size in centimeters and local extent descriptors
3. **N category** with number of nodes examined and number positive
4. **M category** with site of metastasis if M1
5. **Overall stage group** — both anatomic and prognostic when applicable
6. **Biomarker values** incorporated into prognostic staging
7. **Grade** per site-specific grading system (Nottingham for breast, Grade Group for prostate, differentiation for soft tissue sarcoma)
8. **Date of diagnosis** used as the staging reference date

If any component is unknown, record as X (e.g., NX) — never leave blank or assume normal.

---

## Step 5: Handle Special Staging Scenarios

- **Multiple primaries:** Apply AJCC multiple primary rules — stage each independently. Synchronous bilateral breast cancers are staged separately.
- **Unknown primary (CUP):** Stage as TX. The N and M categories reflect the identified disease.
- **Restaging after recurrence:** Use the "r" prefix (rTNM). Do not alter the original stage.
- **Post-neoadjuvant:** Use "yp" prefix. Document pre-treatment clinical stage and post-treatment pathologic stage separately.
- **Lymphoma and leukemia:** Use Ann Arbor (Lugano modification) or disease-specific staging — not TNM.
- **Pediatric tumors:** Many use disease-specific systems (e.g., INSS for neuroblastoma, FIGO for pediatric germ cell tumors).

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Does the assigned stage match the AJCC 8th edition chapter for this specific cancer site?
2. Are all TNM categories documented with the correct prefix (c, p, yp, r)?
3. For sites with prognostic staging, are required biomarkers included and the prognostic stage group assigned?
4. Is the number of lymph nodes examined and number positive recorded for pathologic staging?
5. Does the stage assignment align with the imaging and pathology findings provided?

---

## Quality Audit

- [ ] Correct AJCC edition and chapter applied for the primary site
- [ ] T category matches tumor size and extent per site-specific rules
- [ ] N category includes node count data for pathologic staging
- [ ] M category supported by imaging documentation
- [ ] Clinical vs. pathologic vs. post-therapy prefix correctly assigned
- [ ] Stage group correctly derived from TNM combination
- [ ] Prognostic stage group assigned when applicable (breast, prostate)
- [ ] Biomarker values documented and incorporated into prognostic staging
- [ ] Histologic grade recorded per site-specific grading system
- [ ] Unknown components recorded as X, not left blank
- [ ] Multiple primaries staged independently per AJCC rules
- [ ] Staging date of diagnosis documented
- [ ] No conflicting staging data between summary and supporting documents
- [ ] Output formatted for cancer registry abstraction compatibility

---

## Guidelines

- Always use the AJCC 8th edition unless the diagnosis date falls before January 1, 2018 (use 7th edition for diagnoses before that date)
- Never upstage or downstage based on clinical suspicion alone — staging requires documented evidence
- Clinical stage is never changed after it is assigned; pathologic stage is a separate, additional classification
- For breast cancer, both anatomic stage and prognostic stage must be recorded
- Document the method of M1 confirmation (biopsy-proven vs. imaging-based)
- When sentinel lymph node biopsy is performed, use the (sn) suffix on the N category
- Flag any staging discrepancies between clinical and pathologic classifications for tumor board review
- Include ICD-O-3 histology code to ensure correct chapter selection
