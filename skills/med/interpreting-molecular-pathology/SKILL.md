---
name: interpreting-molecular-pathology
description: Structures molecular test interpretation including NGS panels, FISH, and PCR-based assays. Use when interpreting molecular results, reporting genetic variants, or documenting molecular findings.
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

# Interpreting Molecular Pathology

Structures molecular test interpretation including NGS panels, FISH, and PCR-based assays.

## Why This Skill Exists

Molecular pathology drives precision oncology, pharmacogenomics, and hereditary disease diagnosis. Next-generation sequencing (NGS) panels, fluorescence in situ hybridization (FISH), and PCR-based assays identify actionable genomic alterations that determine eligibility for targeted therapies, immunotherapy, and clinical trials. Misinterpretation of variant significance, failure to detect fusion genes, or incorrect tumor mutational burden (TMB) calculations can deny patients effective treatment or expose them to inappropriate therapy.

CAP accreditation requires compliance with the Molecular Pathology (MOL) checklist including validated bioinformatics pipelines, documented variant interpretation workflows, and proficiency testing. The Association for Molecular Pathology (AMP), American Society of Clinical Oncology (ASCO), and College of American Pathologists jointly published standards for somatic variant interpretation and reporting. Germline variant classification follows ACMG/AMP guidelines. CLIA 42 CFR 493.1253 mandates that molecular test performance characteristics be established and verified before clinical use.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Test type** — NGS panel, single-gene PCR, FISH, RT-PCR, methylation assay, or comprehensive genomic profiling? Default: NGS panel.
2. **Specimen type** — FFPE tissue, fresh tissue, peripheral blood, bone marrow, liquid biopsy (ctDNA)? Default: FFPE.
3. **Tumor type** — Specific histologic diagnosis and primary site? Default: not specified; flag [VERIFY].
4. **Tumor content** — Estimated tumor cellularity (percentage)? Default: per pathologist macro-dissection estimate.
5. **Clinical question** — Therapy selection, prognostication, diagnosis, hereditary risk, or MRD? Default: therapy selection.
6. **Prior molecular testing** — Any prior NGS, FISH, or PCR results? Default: none on file.
7. **Specimen adequacy** — Sufficient DNA/RNA quantity and quality (DIN, RIN values)? Default: QC passed.

### Documents to Request

- Surgical pathology report with histologic diagnosis and tumor percentage
- Prior molecular/genetic test reports
- Specimen QC metrics (DNA/RNA concentration, DIN/RIN, library yield)
- Sequencing run QC (mean depth of coverage, percentage of target bases at minimum depth)
- NCCN guidelines for the specific tumor type
- Clinical notes including treatment history and clinical trial eligibility questions
- Bioinformatics pipeline validation documentation

---

## Step 1: Pre-Analytical Quality Assessment

Verify specimen and sequencing quality metrics:

| Metric | Acceptable for NGS | Marginal | Insufficient |
|---|---|---|---|
| Tumor cellularity | >= 20% | 10-20% (macro-dissect) | < 10% |
| DNA input (FFPE) | >= 50 ng | 10-50 ng | < 10 ng |
| DNA integrity (DIN) | >= 3.0 | 2.0-3.0 | < 2.0 |
| RNA input (fusion panel) | >= 50 ng | 20-50 ng | < 20 ng |
| Mean coverage depth | >= 500x (somatic) | 250-500x | < 250x |
| Percentage targets >= 100x | >= 95% | 90-95% | < 90% |
| ctDNA input (liquid biopsy) | >= 20 ng cfDNA | 10-20 ng | < 10 ng |

Document any QC flags and their impact on sensitivity: low tumor content reduces limit of detection for low-frequency variants.

---

## Step 2: Variant Identification and Filtering

Apply the validated bioinformatics pipeline with systematic variant filtering:

1. **Sequence alignment**: Verify alignment to reference genome (GRCh37/hg19 or GRCh38).
2. **Variant calling**: SNVs, indels, CNAs, gene fusions/rearrangements per validated pipeline.
3. **Filtering thresholds**:
   - Variant allele frequency (VAF) >= 5% for FFPE somatic panels (or >= 0.1-0.5% for ctDNA assays)
   - Coverage at variant site >= 100x
   - Strand bias filter applied
   - Recurrent FFPE artifacts filtered (e.g., C>T deamination artifacts)
4. **Annotation**: Cross-reference variants against ClinVar, COSMIC, gnomAD, OncoKB, and internal databases.
5. **Germline filtering**: Use paired tumor-normal or population frequency filtering (gnomAD AF > 1% suggests germline polymorphism unless known hotspot).

---

## Step 3: Variant Classification and Tiering

### Somatic Variants — AMP/ASCO/CAP Four-Tier System

| Tier | Definition | Examples |
|---|---|---|
| Tier I: Strong Clinical Significance | FDA-approved therapy or included in professional guidelines (NCCN) for this tumor type | EGFR L858R in NSCLC, BRAF V600E in melanoma |
| Tier II: Potential Clinical Significance | FDA-approved therapy for a different tumor type, or investigational therapy with clinical evidence | NTRK fusions (tissue-agnostic), KRAS G12C |
| Tier III: Unknown Clinical Significance | Not observed in population databases or cancer databases; no current therapeutic implication | Novel missense variants in known oncogenes |
| Tier IV: Benign or Likely Benign | Observed at high frequency in population databases; no functional or clinical evidence | Common polymorphisms, synonymous variants |

### Germline Variants — ACMG/AMP Five-Tier System

Classify using the 28 evidence criteria (PVS1, PS1-PS4, PM1-PM6, PP1-PP5 for pathogenic; BA1, BS1-BS4, BP1-BP7 for benign):

| Class | Definition |
|---|---|
| Pathogenic | Strong evidence of disease causation |
| Likely Pathogenic | Evidence favoring pathogenicity (>90% probability) |
| VUS | Uncertain significance; insufficient evidence |
| Likely Benign | Evidence favoring benign (>90% probability) |
| Benign | Strong evidence against disease causation |

---

## Step 4: Clinical Correlation and Actionability

- **NCCN guideline mapping**: For each Tier I/II variant, cite the specific NCCN guideline recommendation (e.g., "NCCN NSCLC v.4.2024: EGFR exon 19 deletion — osimertinib recommended as first-line therapy").
- **FDA-approved companion diagnostics**: Note if the detected variant has a linked CDx (e.g., cobas EGFR Mutation Test v2 for EGFR).
- **Clinical trial eligibility**: Flag variants that match open basket/umbrella trials (NCI-MATCH, TAPUR).
- **TMB calculation**: Report mutations per megabase (mut/Mb). TMB-High threshold >= 10 mut/Mb per FDA pembrolizumab approval.
- **MSI status**: Report as MSI-High, MSI-Low, or MSS based on NGS-derived MSI score.
- **Pharmacogenomic implications**: If germline PGx variants detected (DPYD, UGT1A1), flag for dosing adjustment.

---

## Step 5: Report Construction

Structure the report per AMP/CAP molecular reporting standards:

1. **Test information**: Panel name, gene list, methodology, reference genome, pipeline version.
2. **Specimen**: Type, tumor percentage, QC metrics summary.
3. **Results summary table**: Gene, variant (HGVS), VAF, tier, clinical significance.
4. **Detailed interpretation**: For each Tier I/II variant, provide therapeutic implication narrative.
5. **Negative pertinent findings**: Specifically note clinically expected targets not detected (e.g., "No EGFR mutations detected" in NSCLC).
6. **Limitations**: State limit of detection, regions with suboptimal coverage, known assay blind spots (e.g., large rearrangements not detected by amplicon-based panels).
7. **Signatures**: Interpreting molecular pathologist and laboratory director.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are all variants classified using the appropriate tiering system (AMP somatic or ACMG germline)?
2. Is HGVS nomenclature used correctly for all variant descriptions?
3. Are Tier I/II variants linked to specific NCCN guideline recommendations?
4. Are assay limitations explicitly stated, including limit of detection and coverage gaps?
5. Is TMB/MSI status reported when the panel supports these calculations?

---

## Quality Audit

- [ ] Specimen QC metrics documented (tumor %, DNA/RNA quantity, DIN/RIN)
- [ ] Sequencing QC documented (mean coverage, on-target percentage)
- [ ] Variants annotated against ClinVar, COSMIC, gnomAD, and OncoKB
- [ ] Somatic variants tiered per AMP/ASCO/CAP four-tier system
- [ ] Germline variants classified per ACMG/AMP five-tier system when applicable
- [ ] HGVS nomenclature used for all variant descriptions
- [ ] Tier I/II variants linked to NCCN guideline-specific recommendations
- [ ] TMB and MSI status reported when panel supports calculation
- [ ] Assay limitations explicitly stated with limit of detection
- [ ] Negative pertinent findings documented for expected targets
- [ ] FFPE deamination artifacts addressed in variant filtering
- [ ] Report signed by board-certified molecular pathologist
- [ ] CAP MOL checklist compliance verified

---

## Guidelines

- Always use HGVS nomenclature (c. and p. notation) for variant descriptions; include both coding and protein-level annotations
- Classify somatic variants per AMP/ASCO/CAP tiering and germline variants per ACMG/AMP criteria — never mix the two systems
- For each Tier I/II finding, cite the specific guideline (NCCN, FDA label) and therapy recommendation
- Explicitly state the limit of detection for the assay; for FFPE panels this is typically 5% VAF at 500x coverage
- Report TMB only when the panel covers sufficient genomic territory (>= 1 Mb of coding sequence) to produce a reliable estimate
- Flag VUS variants but do not recommend clinical action based solely on VUS findings; suggest periodic reclassification review
- For liquid biopsy, note that a negative result does not exclude the presence of tumor mutations (low shedding tumors)
- Maintain bioinformatics pipeline version control and document any updates in the report
