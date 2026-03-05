---
name: interpreting-genomic-profiling
description: Structures comprehensive genomic profiling interpretation with actionable mutations and matched therapies. Use when reviewing genomic test results, identifying targeted therapy options, or interpreting NGS panels.
tags:
  - analysis
  - oncology
metadata:
  author: casemark
  practice_areas:
    - Medical Oncology
    - Hematology-Oncology
    - Radiation Oncology
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Genomic Profiling

Structures comprehensive genomic profiling interpretation with actionable mutations and matched therapies.

## Why This Skill Exists

Comprehensive genomic profiling (CGP) using next-generation sequencing (NGS) panels has transformed oncology treatment selection. FDA-approved CGP tests (FoundationOne CDx, Tempus xT, MSK-IMPACT, Guardant360 CDx) identify actionable mutations that match patients to FDA-approved targeted therapies, immunotherapy biomarkers (MSI-H/dMMR, TMB-H), and clinical trials. However, a genomic report listing hundreds of variants is clinically meaningless without structured interpretation that separates actionable mutations from variants of uncertain significance (VUS).

CMS covers CGP for patients with advanced solid tumors who have exhausted standard therapies (National Coverage Determination 90.2). NCCN guidelines increasingly require molecular testing for treatment selection in NSCLC, breast cancer, colorectal cancer, cholangiocarcinoma, and many other tumor types. Failure to order or correctly interpret CGP can result in missed targeted therapy opportunities, inappropriate off-label drug use, or failure to identify patients eligible for tumor-agnostic approvals (pembrolizumab for MSI-H, larotrectinib/entrectinib for NTRK fusions).

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What CGP platform was used (FoundationOne CDx, Tempus xT, Guardant360, MSK-IMPACT, institutional panel)? (Default: specify)
2. Was the sample tissue-based (tumor biopsy) or liquid biopsy (ctDNA)? (Default: specify)
3. What is the cancer diagnosis, stage, and treatment history? (Default: [VERIFY])
4. What is the specific clinical question (first-line treatment selection, resistance mechanism, trial matching)? (Default: treatment selection)
5. When was the sample collected relative to the last treatment? (Default: document date)
6. Is the tumor fraction/content adequate for the assay? (Default: check QC metrics on report)
7. Has prior molecular testing been performed? (Default: document)
8. Does the patient have a known germline mutation? (Default: assess family history)

### Documents to Request

- Complete CGP report from the testing laboratory
- Pathology report confirming diagnosis and tumor content
- Treatment history with dates, agents, and response
- Prior molecular testing results (single-gene tests, smaller panels)
- Germline genetic testing results if performed
- Current NCCN guideline for the cancer type (molecular testing section)
- ClinicalTrials.gov search results for identified actionable alterations
- OncoKB, CIViC, or institutional molecular tumor board knowledgebase access

---

## Step 1: Review Report Quality Metrics and Sample Adequacy

Before interpreting variants, assess report quality:

1. **Tumor content/purity:** Most tissue-based CGP requires ≥20% tumor content. Reports with low tumor content may have false-negative results.
2. **Sequencing depth:** Adequate coverage typically >500× for tissue, >2000× for ctDNA.
3. **Specimen type:** Tissue biopsy provides a more complete profile than liquid biopsy. Liquid biopsy may miss certain alterations (gene fusions, amplifications) at low tumor fraction.
4. **Liquid biopsy ctDNA fraction:** If ctDNA is not detected or very low (<0.5%), a negative result is not reliable — recommend tissue-based testing.
5. **Microsatellite instability (MSI) and tumor mutational burden (TMB):** Confirm these are reported — they are required for tumor-agnostic therapy eligibility.

Document any quality limitations that affect interpretation reliability.

---

## Step 2: Classify Identified Alterations by Actionability

Use the OncoKB or AMP/ASCO/CAP tiered classification system:

**AMP/ASCO/CAP Tier System:**

| Tier | Description | Clinical Action |
|------|-------------|----------------|
| Tier I-A | FDA-approved companion diagnostic for the specific cancer type | Matched therapy available on-label |
| Tier I-B | FDA-approved for a different cancer type or strong evidence in same cancer type | Consider off-label use or tumor-agnostic approval |
| Tier II-C | Clinical trial evidence supporting activity | Trial enrollment or off-label consideration |
| Tier II-D | Preclinical evidence or case reports | Research interest; no clinical action |
| Tier III | Variant of uncertain significance (VUS) | No clinical action; do not report to patient as actionable |
| Tier IV | Benign or likely benign | Not actionable |

**Key actionable alterations by cancer type:**

| Cancer | Alteration | Matched Therapy |
|--------|-----------|----------------|
| NSCLC | EGFR exon 19 del/L858R | Osimertinib (1st-line) |
| NSCLC | ALK fusion | Alectinib, lorlatinib |
| NSCLC | ROS1 fusion | Crizotinib, entrectinib |
| NSCLC | KRAS G12C | Sotorasib, adagrasib |
| NSCLC | MET exon 14 skip | Capmatinib, tepotinib |
| Breast | PIK3CA mutation | Alpelisib + fulvestrant |
| Breast | ESR1 mutation | Elacestrant |
| CRC | KRAS/NRAS wild-type | Anti-EGFR (cetuximab, panitumumab) |
| Cholangiocarcinoma | FGFR2 fusion | Futibatinib, pemigatinib |
| Any solid tumor | MSI-H/dMMR | Pembrolizumab (tumor-agnostic) |
| Any solid tumor | NTRK fusion | Larotrectinib, entrectinib (tumor-agnostic) |
| Any solid tumor | TMB-H (≥10 mut/Mb) | Pembrolizumab (tumor-agnostic) |
| Any solid tumor | BRAF V600E | Dabrafenib + trametinib (tumor-agnostic) |

---

## Step 3: Assess Resistance Mechanisms and Co-Mutations

For patients who have progressed on targeted therapy, interpret the CGP report for resistance:

- **EGFR T790M** after first/second-gen EGFR TKI → osimertinib (if not already used)
- **EGFR C797S** after osimertinib → clinical trial or combination approaches
- **ALK resistance mutations** (G1202R, compound mutations) → lorlatinib
- **ESR1 mutations** in ER+ breast cancer → resistance to aromatase inhibitors
- **BRCA reversion mutations** → loss of PARP inhibitor sensitivity
- **MET amplification** as bypass resistance in EGFR-mutant NSCLC → EGFR + MET combination

Document co-occurring mutations that affect prognosis or treatment selection:
- TP53 co-mutation worsens prognosis in EGFR-mutant NSCLC
- STK11/KEAP1 co-mutations in NSCLC predict poor response to immunotherapy
- PTEN loss may confer resistance to certain targeted therapies

---

## Step 4: Generate the Interpretive Report

Structure the interpretation:

1. **Report summary:** Platform, specimen type, quality metrics, key findings
2. **Tier I actionable findings:** Each alteration with matched FDA-approved therapy, evidence level, and NCCN recommendation
3. **Tier II findings:** Clinical trial opportunities and emerging evidence
4. **MSI/TMB status:** Document for tumor-agnostic therapy eligibility
5. **Resistance mutations:** Identified mechanisms with clinical implications
6. **Prognostic biomarkers:** Co-mutations affecting prognosis or treatment response prediction
7. **VUS:** Listed for completeness but explicitly noted as not actionable
8. **Germline implications:** Flag pathogenic variants that may have germline significance (BRCA1/2, Lynch syndrome genes) and recommend confirmatory germline testing
9. **Clinical trial matches:** Specific NCT numbers for actionable alterations without on-label therapies
10. **Recommended actions:** Specific treatment changes, additional testing, or molecular tumor board referral

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are report quality metrics reviewed and any limitations documented?
2. Is each alteration classified using the AMP/ASCO/CAP tier system or OncoKB evidence levels?
3. Are actionable mutations matched to FDA-approved therapies with correct indications (on-label vs. tumor-agnostic)?
4. Have variants of uncertain significance been explicitly labeled as not actionable?
5. Are germline implications flagged for pathogenic variants in hereditary cancer genes?

---

## Quality Audit

- [ ] CGP platform and specimen type documented
- [ ] Sample quality metrics reviewed (tumor content, sequencing depth, ctDNA fraction)
- [ ] Each alteration classified by actionability tier
- [ ] Tier I mutations matched to FDA-approved therapies with correct indication
- [ ] MSI-H/dMMR status reported and tumor-agnostic eligibility assessed
- [ ] TMB score reported with threshold for pembrolizumab eligibility (≥10 mut/Mb)
- [ ] NTRK fusion status assessed for tumor-agnostic therapy eligibility
- [ ] Resistance mutations interpreted in context of prior treatment
- [ ] Co-mutations affecting prognosis documented
- [ ] VUS explicitly noted as not actionable
- [ ] Germline implications flagged with recommendation for confirmatory testing
- [ ] Clinical trial matches identified for actionable alterations without on-label therapy
- [ ] Liquid biopsy limitations noted if ctDNA fraction is low
- [ ] Report reviewed by molecular tumor board or qualified genomic specialist

---

## Guidelines

- Never recommend treatment based on a VUS — only Tier I and selected Tier II alterations are actionable
- Liquid biopsy with undetectable ctDNA is not the same as "no mutations found" — recommend tissue-based testing if liquid biopsy is negative in a patient with known active disease
- MSI-H/dMMR, TMB-H, and NTRK fusions are tumor-agnostic biomarkers — assess for every solid tumor patient regardless of cancer type
- Germline pathogenic variants detected on tumor profiling (especially BRCA1/2, MLH1, MSH2, MSH6, PMS2) require confirmatory germline testing and genetic counseling referral
- For NSCLC, NCCN requires broad molecular testing (EGFR, ALK, ROS1, BRAF, KRAS, MET, RET, HER2, NTRK) before first-line treatment selection — single-gene sequential testing is no longer acceptable
- Report interpretation should be updated if new FDA approvals or guideline changes create actionability for previously non-actionable findings
- Molecular tumor board review is recommended for complex cases with multiple actionable findings or uncertain actionability
- Document the date of the CGP report and the NCCN guideline version used for interpretation — both are time-sensitive
