---
name: interpreting-immunohistochemistry
description: Guides IHC panel selection and interpretation for tumor classification and prognostication. Use when ordering IHC panels, interpreting staining patterns, or classifying tumors by immunophenotype.
tags:
  - analysis
  - pathology
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Immunohistochemistry

Guides IHC panel selection and interpretation for tumor classification and prognostication.

## Why This Skill Exists

Immunohistochemistry (IHC) is the most widely used ancillary technique in surgical pathology, essential for tumor classification, prognostication, prediction of therapy response, and determination of site of origin in metastatic disease. Misinterpretation of IHC results — a false-negative ER causing omission of endocrine therapy, a misread HER2 leading to inappropriate trastuzumab, or an incorrect CK7/CK20 profile misdirecting the search for a primary tumor — directly harms patients and exposes laboratories to liability. ASCO/CAP guidelines mandate specific IHC scoring systems for predictive markers (ER, PR, HER2), and CAP accreditation (IHC checklist series) requires validated antibodies, documented controls, and proficiency testing.

Every laboratory performing IHC must validate each new antibody per CAP IHC.25100 requirements, participate in external proficiency programs (CAP Surveys, NordiQC, UK NEQAS), and maintain documentation of antibody clones, antigen retrieval conditions, and scoring criteria. CLIA classifies IHC as a high-complexity test, requiring laboratory director oversight of result interpretation.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Clinical question** — Tumor typing, site-of-origin determination, prognostic marker assessment, predictive marker testing, or mismatch repair evaluation? Default: tumor classification.
2. **Histologic context** — What is the morphologic differential diagnosis from H&E evaluation? Default: undifferentiated malignancy, NOS.
3. **Panel design** — What antibodies are being ordered and why? Default: per institutional reflex panel for the differential.
4. **Specimen type** — FFPE biopsy, resection, cell block, cytology smear, or decalcified bone specimen? Default: FFPE biopsy.
5. **Prior IHC** — Are there previous IHC results from outside institutions? Default: none on file.
6. **Tissue availability** — Is tissue sufficient for the planned panel, or must the panel be prioritized? Default: sufficient tissue.
7. **Scoring system** — Which quantitative scoring system applies (Allred, H-score, percentage, 0-3+ scale)? Default: per marker-specific ASCO/CAP guidelines.

### Documents to Request

- H&E stained sections with morphologic differential diagnosis
- Prior IHC and special stain results
- Clinical notes including primary site, treatment history, and imaging
- Antibody validation records for each marker in the panel
- External positive and negative control documentation
- Manufacturer package inserts for antibody clones used
- CAP/NordiQC proficiency testing results for each antibody

---

## Step 1: Panel Design — Systematic Approach

Design the IHC panel based on the morphologic differential diagnosis. Use an evidence-based, stepwise approach:

### Carcinoma of Unknown Primary (CUP) — First-Line Panel

| Marker | Pattern | Interpretation |
|---|---|---|
| CK7 | + | Upper GI, lung, breast, ovary, endometrium, thyroid, pancreas, biliary |
| CK20 | + | Colorectal, urothelial, Merkel cell, gastric |
| CK7+/CK20- | Most common | Lung, breast, ovary, endometrium, thyroid, pancreas |
| CK7-/CK20+ | | Colorectal, Merkel cell |
| CK7+/CK20+ | | Urothelial, upper GI (stomach, pancreas), ovarian mucinous |
| CK7-/CK20- | | Renal cell, hepatocellular, prostate, adrenal, squamous (some) |

### Second-Line Organ-Specific Markers

| Marker | Primary Site Suggested | Sensitivity/Specificity Notes |
|---|---|---|
| TTF-1 | Lung adenocarcinoma, thyroid | ~75% sensitivity for lung adeno; also positive in small cell carcinoma |
| PAX8 | Renal, ovarian, thyroid, endometrial | Not specific for a single organ; use in combination |
| CDX2 | Colorectal, upper GI | ~95% for colorectal adeno; also positive in mucinous ovarian, bladder |
| GATA3 | Breast, urothelial | ~90% breast, 80-90% urothelial |
| NKX3.1 | Prostate | ~98% specific for prostate; more specific than PSA |
| Hepatocyte (HepPar1) | Hepatocellular carcinoma | ~80% sensitivity; Arginase-1 is more specific |
| WT1 | Ovarian serous, mesothelioma | Nuclear pattern for ovarian; nuclear+cytoplasmic for mesothelioma |
| SATB2 | Colorectal | ~85% sensitivity, high specificity when combined with CDX2 |

### Melanoma vs. Carcinoma vs. Lymphoma

| Marker | Melanoma | Carcinoma | Lymphoma |
|---|---|---|---|
| S100 | + (95%) | - | - |
| SOX10 | + (98%) | - | - |
| Melan-A/MART-1 | + (80-90%) | - | - |
| HMB-45 | + (70-80%) | - | - |
| Pan-CK (AE1/AE3) | - | + | - |
| LCA (CD45) | - | - | + |

---

## Step 2: Predictive Marker Scoring — ASCO/CAP Guidelines

Score predictive markers using the ASCO/CAP-mandated systems:

### ER and PR (Breast Cancer) — ASCO/CAP 2020

- **Positive**: >= 1% of tumor nuclei staining at any intensity
- **Low positive**: 1-10% (report separately; clinical benefit of endocrine therapy uncertain in this range)
- **Negative**: < 1% staining
- Report: Percentage of positive nuclei and predominant intensity (weak, moderate, strong)

### HER2 (Breast Cancer) — ASCO/CAP 2023

| IHC Score | Staining Pattern | Interpretation |
|---|---|---|
| 0 | No staining or incomplete faint membrane in <= 10% | Negative |
| 1+ | Incomplete faint membrane in > 10% | Negative |
| 2+ | Weak-to-moderate complete membrane in > 10% OR strong complete membrane in <= 10% | Equivocal — reflex to FISH |
| 3+ | Strong complete membrane in > 10% | Positive |

**HER2-low**: IHC 1+ or IHC 2+/FISH non-amplified. Relevant for trastuzumab deruxtecan (T-DXd) eligibility.

### PD-L1 Scoring

| Assay (Clone) | Scoring System | Tumor Type | Positive Threshold |
|---|---|---|---|
| 22C3 (Dako) | TPS | NSCLC | >= 1% (some benefit); >= 50% (monotherapy) |
| 22C3 (Dako) | CPS | Gastric, cervical, HNSCC, urothelial | >= 1 or >= 10 (site-dependent) |
| SP142 (Ventana) | IC | Urothelial, TNBC | >= 1% IC |
| SP263 (Ventana) | TC/IC | Urothelial | >= 25% TC or IC |

---

## Step 3: Mismatch Repair (MMR) and Microsatellite Instability

Interpret the four-antibody MMR panel:

| Pattern | MLH1 | PMS2 | MSH2 | MSH6 | Interpretation |
|---|---|---|---|---|---|
| Intact | + | + | + | + | MMR proficient (pMMR) |
| Loss of MLH1/PMS2 | - | - | + | + | MLH1 promoter methylation or Lynch syndrome; reflex to BRAF V600E and/or MLH1 methylation |
| Loss of MSH2/MSH6 | + | + | - | - | Lynch syndrome (MSH2 germline); refer to genetics |
| Loss of MSH6 only | + | + | + | - | Lynch syndrome (MSH6 germline) or secondary to treatment |
| Loss of PMS2 only | + | - | + | + | Lynch syndrome (PMS2 germline); refer to genetics |

**Scoring rule**: Internal positive control (stromal cells, lymphocytes, normal epithelium) MUST show nuclear staining for the result to be valid. If internal controls are negative, the stain is invalid and must be repeated.

---

## Step 4: Quality Control and Validation

Verify IHC quality before interpretation:

- **External positive control**: Tissue with known expression of the target antigen included on the same slide or in the same run.
- **External negative control**: Same tissue processed without primary antibody or with isotype control.
- **Internal controls**: Endogenous cell populations expected to express (positive) or not express (negative) the antigen serve as built-in quality indicators.
- **Staining quality**: Assess for background, edge artifact, necrosis artifact, and fixation artifact. Under-fixed tissue (< 6 hours in 10% NBF) may produce false-negative results for ER, PR, HER2.
- **Fixation time**: ASCO/CAP requires 6-72 hours in 10% neutral buffered formalin for breast biomarkers.

---

## Step 5: Report Construction

Structure the IHC interpretation report:

1. **Antibody panel**: List each antibody with clone, vendor, and result.
2. **Scoring**: Apply appropriate scoring system for each predictive marker.
3. **Interpretation**: State the immunophenotypic profile and the favored diagnosis.
4. **Differential diagnosis refinement**: Explain how IHC results narrow or confirm the differential.
5. **Discordance notes**: If IHC results are unexpected for the morphologic diagnosis, discuss possible explanations (aberrant expression, fixation artifact, sampling).
6. **Recommendations**: Suggest additional markers if the panel is inconclusive.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are all predictive markers (ER, PR, HER2, PD-L1) scored using the ASCO/CAP-mandated system?
2. Are external and internal controls valid for each antibody in the panel?
3. Does the IHC panel logically address the morphologic differential diagnosis?
4. Is the MMR panel result correctly interpreted with internal control validation?
5. Are fixation time requirements met for breast biomarkers (6-72 hours per ASCO/CAP)?

---

## Quality Audit

- [ ] Each antibody validated per CAP IHC.25100 requirements
- [ ] External positive and negative controls included and valid
- [ ] Internal positive controls present and staining appropriately
- [ ] Antibody clone and vendor documented for each marker
- [ ] ER/PR scored per ASCO/CAP 2020 guidelines with percentage and intensity
- [ ] HER2 scored per ASCO/CAP 2023 four-tier system
- [ ] HER2 equivocal (2+) reflexed to FISH per protocol
- [ ] PD-L1 scored with correct system (TPS, CPS, IC) for the tumor type and assay
- [ ] MMR panel interpreted with internal control validation
- [ ] Fixation time documented and within ASCO/CAP requirements for predictive markers
- [ ] Proficiency testing participation current (CAP Surveys, NordiQC)
- [ ] Staining artifacts (background, edge, necrosis) addressed in interpretation
- [ ] Report includes antibody clone, scoring system, and interpretation for each marker

---

## Guidelines

- Always design the IHC panel based on the morphologic differential diagnosis from H&E; avoid shotgun panels that waste tissue and introduce interpretive noise
- Score ER, PR, and HER2 strictly per the current ASCO/CAP guidelines; no institutional modifications to the scoring criteria are permitted for these predictive markers
- Report HER2-low status (IHC 1+ or 2+/FISH non-amplified) explicitly, as it now affects therapy eligibility for T-DXd
- Validate the internal positive control before interpreting any IHC stain as negative; if internal controls fail, repeat the stain before reporting
- For CUP workup, use a stepwise panel approach starting with CK7/CK20 and broad markers before adding organ-specific antibodies
- Never diagnose melanoma on a single marker; require positivity for at least two melanocytic markers (S100, SOX10, Melan-A, HMB-45)
- When MMR loss involves MLH1/PMS2, always recommend reflex testing for BRAF V600E and/or MLH1 promoter methylation to distinguish sporadic from Lynch syndrome
- Document the specific antibody clone used for every marker, as different clones may have different performance characteristics (e.g., SP1 vs. 1D5 for ER)
