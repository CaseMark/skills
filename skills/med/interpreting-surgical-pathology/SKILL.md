---
name: interpreting-surgical-pathology
description: Structures surgical pathology reports with diagnosis, staging, margins, and prognostic markers. Use when interpreting biopsies, creating pathology reports, or documenting tissue diagnoses.
tags:
  - analysis
  - pathology
  - surgical
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

# Interpreting Surgical Pathology

Structures surgical pathology reports with diagnosis, staging, margins, and prognostic markers.

## Why This Skill Exists

Surgical pathology reports are the authoritative diagnostic documents that drive treatment decisions in oncology, transplant medicine, and every surgical discipline. A misclassified margin, an omitted prognostic marker, or an incorrect histologic grade can lead to under-treatment, unnecessary re-excision, or missed therapeutic windows. The College of American Pathologists (CAP) cancer protocols mandate structured synoptic reporting for all cancer resection specimens, and accreditation under CAP Laboratory Accreditation Program (LAP) requires compliance with these templates.

The stakes are concrete: CLIA 42 CFR 493.1274 requires that the laboratory director ensure reports contain sufficient information to serve the clinical purpose. Joint Commission and CAP inspectors audit report completeness, turnaround time, and amended-report rates. Failure to meet these standards risks laboratory accreditation, legal liability in malpractice claims, and measurable patient harm. This skill ensures every surgical pathology interpretation follows evidence-based frameworks and satisfies regulatory obligations.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before writing any interpretation, confirm the following with the requesting party:

1. **Specimen type** — Is this a biopsy (incisional, excisional, core needle, punch) or a resection specimen? Default: resection.
2. **Clinical history** — What is the documented indication, prior diagnosis, and relevant imaging? Default: not provided; flag with [VERIFY].
3. **Specimen orientation** — Were orientation markers (sutures, clips, ink colors) submitted by the surgeon? Default: assume standard CAP inking protocol.
4. **Prior pathology** — Are there previous biopsies, flow cytometry, or molecular results for this patient? Default: none on file.
5. **Target reporting template** — Which CAP cancer protocol or institutional synoptic applies? Default: latest CAP protocol for the organ site.
6. **Ancillary studies needed** — Are IHC, special stains, FISH, or molecular panels anticipated? Default: per institutional reflex-testing policy.
7. **Turnaround-time requirement** — Is there an intraoperative, urgent, or routine timeline? Default: routine (48-72 hours per CAP benchmark).

### Documents to Request

- Requisition form with clinical history and specimen labeling
- Operative report or procedure note
- Prior pathology reports (internal and external consults)
- Radiology reports (CT, MRI, PET) if staging-relevant
- CAP cancer protocol checklist for the specific organ site
- Institutional gross dissection protocols and section-submission guidelines
- Any prior IHC, flow cytometry, or molecular test reports

---

## Step 1: Gross Examination and Dictation

Perform or review the gross description following CAP and institutional standards:

- **Specimen identification**: Verify label matches requisition; two-identifier check per CAP ANP.11700.
- **Measurements**: Record three dimensions in centimeters for every discrete specimen and lesion.
- **Orientation and inking**: Document ink colors assigned to each margin (e.g., blue = superior, black = deep, green = lateral).
- **Sectioning protocol**: Follow organ-specific CAP gross dissection guidelines:

| Specimen Type | Section Submission Standard |
|---|---|
| Breast lumpectomy | Perpendicular sections through closest margin; entirely submit if < 3 cm |
| Colon resection | Sections through deepest invasion, proximal/distal margins, all lymph nodes |
| Prostate radical | Cone apex, base margin, bilateral posterior quadrants per Stanford protocol |
| Lung lobectomy | Tumor center, bronchial margin, visceral pleura, hilar lymph nodes |
| Skin excision | Bread-loaf or en-face margins per Mohs vs. standard protocol |

- **Lymph node harvest**: Count and submit all grossly identified lymph nodes. For colorectal specimens, the minimum benchmark is 12 nodes per AJCC/CAP.
- **Photographs**: Gross photographs for complex specimens (Whipple, laryngectomy, radical cystectomy).

---

## Step 2: Microscopic Evaluation

Systematic slide review following a structured checklist approach:

1. **Tumor type and subtype**: Classify per WHO Classification of Tumours (5th edition, blue books). Use the exact WHO preferred terminology.
2. **Histologic grade**: Apply the grading system specific to the organ:
   - Breast: Nottingham combined histologic grade (tubule formation + nuclear grade + mitotic count)
   - Colorectal: Low-grade (well/moderately differentiated) vs. high-grade (poorly differentiated)
   - Prostate: ISUP Grade Group (1-5) derived from Gleason score
   - Lung: Differentiation grade per WHO criteria
3. **Tumor extent**: Measure maximum dimension and depth of invasion in millimeters.
4. **Margins**: Report distance to closest margin in millimeters. For CAP-reportable cancers, state whether margins are positive, close (< 2 mm for most sites), or negative.
5. **Lymphovascular invasion (LVI)**: Present or not identified. Use elastic stains (EVG, D2-40) when equivocal.
6. **Perineural invasion (PNI)**: Present or not identified.
7. **Lymph node status**: Number positive / total examined. Report extranodal extension if present.
8. **Additional findings**: Dysplasia, in-situ carcinoma, inflammation, treatment effect (per Ryan, Mandard, or CAP regression grading).

---

## Step 3: Ancillary Studies Integration

Incorporate results from ancillary testing into the final interpretation:

- **IHC panel results**: Record antibody, clone, scoring system (Allred, H-score, percentage), and interpretation.
- **ER/PR (breast)**: Report percentage positive and intensity per ASCO/CAP guidelines (positive >= 1%).
- **HER2 (breast/gastric)**: Report IHC score (0, 1+, 2+, 3+) and FISH ratio if IHC 2+ per ASCO/CAP 2023 guidelines.
- **MMR/MSI**: Report MLH1, PMS2, MSH2, MSH6 status as intact or lost. If MLH1/PMS2 lost, note recommendation for BRAF V600E and/or MLH1 promoter methylation.
- **PD-L1**: Report TPS or CPS depending on tumor type and assay (22C3, SP263, SP142).
- **Molecular results**: Integrate NGS, FISH, PCR findings. Cross-reference variant interpretation with the main histologic diagnosis.

---

## Step 4: Synoptic Report Assembly

Construct the final report using the applicable CAP cancer protocol checklist:

1. **Procedure type**: Match to CAP terminology (e.g., "Radical prostatectomy" not "prostate removal").
2. **Tumor site and laterality**: Use specific anatomic sub-site nomenclature.
3. **Histologic type**: Verbatim WHO 5th edition terminology.
4. **Grade**: Organ-specific system with numeric values.
5. **Pathologic staging (pTNM)**: Apply current AJCC Cancer Staging Manual (8th edition). Include prefix designators (y for post-treatment, r for recurrence).
6. **Margins**: Named margin with distance or positive/negative status.
7. **LVI, PNI, treatment effect**: As evaluated.
8. **Ancillary results**: Summarized with scoring.
9. **Comment section**: Address discordances, limitations, and recommendations for additional testing.

---

## Step 5: Report Finalization and Sign-Out

- Compare the diagnosis with the clinical impression and imaging; document any discordances in a comment.
- Verify all CAP required elements are answered; no blank fields.
- Apply SNOMED CT or ICD-O-3 codes where required by institutional policy.
- Confirm the report is compliant with CAP checklist COM.30000 series requirements.
- If amendment is needed post-sign-out, follow CAP ANP.11850 amendment procedures with reason, date, and signature.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Before finalizing any surgical pathology interpretation, verify:

1. Does the diagnosis match the WHO classification terminology exactly?
2. Are all CAP synoptic data elements completed with no blanks or defaults?
3. Is the pTNM stage consistent with the descriptors (tumor size, node count, invasion depth)?
4. Have all ancillary results been integrated and any pending studies flagged?
5. Is the report turnaround within CAP benchmark (routine <= 2 working days for biopsies, <= 3 for resections)?

---

## Quality Audit

- [ ] Specimen identification verified with two patient identifiers
- [ ] Gross description includes three-dimensional measurements for all lesions
- [ ] Ink colors documented and correlated with margin orientation
- [ ] WHO 5th edition histologic type terminology used
- [ ] Appropriate grading system applied for organ site
- [ ] Margins reported with distance in millimeters or positive/negative designation
- [ ] Lymph node count meets minimum benchmark for the specimen type
- [ ] pTNM staging uses current AJCC 8th edition criteria
- [ ] All CAP synoptic checklist required elements answered
- [ ] Ancillary studies (IHC, molecular) results integrated with proper scoring
- [ ] Discordances between clinical and pathologic findings addressed in comment
- [ ] Report complies with CLIA 42 CFR 493.1274 content requirements
- [ ] Amendment procedures followed if changes made post-sign-out

---

## Guidelines

- Always use the current CAP cancer protocol checklist for the specific organ site and specimen type
- Report histologic type using WHO Classification of Tumours 5th edition preferred terminology only
- Stage all malignancies per AJCC Cancer Staging Manual 8th edition; never use outdated editions
- When margins are equivocal, recommend deeper levels or additional sections before calling positive
- Flag all pending ancillary studies with expected completion date; do not hold the report unless institutionally required
- Document any inter-observer consultation or external review in the report
- For amended reports, preserve the original diagnosis and clearly document reason for amendment per CAP ANP.11850
- Maintain a personal concordance log for frozen-section to permanent-section discrepancies as part of ongoing quality improvement
