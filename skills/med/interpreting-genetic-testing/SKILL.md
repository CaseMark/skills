---
name: interpreting-genetic-testing
description: Structures genetic test result interpretation with variant classification (ACMG criteria) and clinical actionability. Use when interpreting genetic results, classifying variants, or documenting genetic findings.
tags:
  - analysis
  - pathology
  - clinical
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

# Interpreting Genetic Testing

Structures genetic test result interpretation with variant classification (ACMG criteria) and clinical actionability.

## Why This Skill Exists

Germline genetic testing has become central to cancer risk assessment, hereditary disease diagnosis, carrier screening, pharmacogenomics, and reproductive planning. The American College of Medical Genetics and Genomics (ACMG) and the Association for Molecular Pathology (AMP) published joint guidelines (Richards et al., 2015) that establish the five-tier variant classification framework now universally adopted by clinical laboratories. Misclassification of a variant — calling a pathogenic variant as VUS (variant of uncertain significance) or vice versa — can deny a patient life-saving surveillance, prevent cascade testing of at-risk family members, or cause unnecessary prophylactic surgery.

CAP accreditation (Molecular Pathology MOL checklist) requires documented variant interpretation workflows, use of standardized databases (ClinVar, ClinGen), and proficiency testing participation. CLIA mandates analytical validation of genetic tests including sensitivity, specificity, and reportable range. Beyond the laboratory, genetic test results carry unique implications for family members, employment and insurance (GINA protection in the US), and require integration with genetic counseling per ACMG practice guidelines.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Test type** — Single-gene, multi-gene panel, exome, genome, chromosomal microarray, or targeted variant analysis? Default: multi-gene panel.
2. **Clinical indication** — Hereditary cancer risk, hereditary cardiac disease, neurogenetic evaluation, carrier screening, prenatal diagnosis, pharmacogenomics, or diagnostic odyssey? Default: hereditary cancer risk.
3. **Patient demographics** — Age, sex, ethnicity (relevant for population-specific variant frequencies), family history? Default: not provided; request.
4. **Family history** — Three-generation pedigree available? Affected family members with known variants? Default: not provided; flag [VERIFY].
5. **Prior genetic testing** — Previous genetic test results (patient or family members)? Default: none on file.
6. **Informed consent** — Was pre-test genetic counseling and informed consent documented? Default: yes; flag if unknown.
7. **Incidental/secondary findings** — Does consent cover reporting of ACMG SF v3.2 secondary findings? Default: yes, per ACMG recommendations.

### Documents to Request

- Genetic testing requisition with clinical indication and family history
- Three-generation pedigree (drawn or documented)
- Prior genetic test reports (patient and family members)
- Informed consent documentation
- Clinical notes (phenotype, age of onset, diagnostic workup)
- Test methodology documentation (genes covered, platforms, limitations)
- Variant database records (ClinVar, ClinGen, LOVD, internal database)
- ACMG secondary findings gene list (SF v3.2) consent status

---

## Step 1: Pre-Analytical Assessment

Verify test appropriateness and quality metrics:

- **Test selection**: Confirm the test is appropriate for the clinical question. A hereditary breast/ovarian panel should include BRCA1, BRCA2, PALB2, ATM, CHEK2, and other high/moderate penetrance genes per NCCN guidelines.
- **Specimen quality**: DNA quality (DIN >= 6.0 for germline testing), quantity (typically >= 200 ng for NGS panels), and source (blood preferred; saliva or buccal acceptable with caveats about potential mosaicism detection limitations).
- **Coverage metrics**: Mean depth >= 100x for germline panels; > 99% of target bases at >= 20x. Regions with suboptimal coverage must be listed in the report.
- **Deletion/duplication analysis**: Confirm whether the assay includes CNV detection (MLPA, array CGH, or NGS-based read depth analysis). Many pathogenic variants in BRCA1, MSH2, and PMS2 are large deletions.

---

## Step 2: Variant Classification — ACMG/AMP Framework

Apply the 28-criteria ACMG/AMP framework systematically:

### Evidence Categories for Pathogenic Classification

| Code | Criterion | Strength |
|---|---|---|
| PVS1 | Null variant (nonsense, frameshift, canonical splice) in a gene where loss of function is a known disease mechanism | Very Strong |
| PS1 | Same amino acid change as a previously established pathogenic variant | Strong |
| PS2 | De novo (confirmed parentage) in a patient with the disease and no family history | Strong |
| PS3 | Well-established functional studies show damaging effect | Strong |
| PS4 | Prevalence in affected individuals significantly increased vs. controls | Strong |
| PM1 | Located in a mutational hotspot or well-established functional domain | Moderate |
| PM2 | Absent from controls (or extremely rare) in gnomAD | Moderate |
| PM3 | Detected in trans with a known pathogenic variant (recessive) | Moderate |
| PM4 | Protein length-changing variant in a non-repetitive region | Moderate |
| PM5 | Novel missense at a position where a different pathogenic missense is known | Moderate |
| PM6 | Assumed de novo (parentage not confirmed) | Moderate |
| PP1 | Cosegregation with disease in multiple family members | Supporting |
| PP2 | Missense in gene with low rate of benign missense and where missense is common mechanism | Supporting |
| PP3 | Multiple in silico tools predict deleterious (REVEL, CADD, SpliceAI) | Supporting |
| PP4 | Patient phenotype highly specific for the gene | Supporting |
| PP5 | Reputable source (ClinGen Expert Panel) classifies as pathogenic | Supporting |

### Evidence Categories for Benign Classification

| Code | Criterion | Strength |
|---|---|---|
| BA1 | Allele frequency > 5% in gnomAD (standalone benign) | Standalone |
| BS1 | Allele frequency greater than expected for the disorder | Strong |
| BS2 | Observed in healthy adult with full penetrance expected | Strong |
| BS3 | Functional studies show no damaging effect | Strong |
| BS4 | Lack of segregation in affected family members | Strong |
| BP1 | Missense in a gene where only truncating variants cause disease | Supporting |
| BP2 | Observed in trans with a pathogenic variant (dominant) or in cis with a pathogenic variant | Supporting |
| BP3 | In-frame insertion/deletion in a repetitive region | Supporting |
| BP4 | Multiple in silico tools predict no impact | Supporting |
| BP6 | Reputable source classifies as benign | Supporting |
| BP7 | Synonymous variant with no splice impact predicted | Supporting |

### Classification Rules (Combining Criteria)

| Classification | Minimum Criteria Combination |
|---|---|
| Pathogenic | PVS1 + >= 1 Moderate, OR >= 2 Strong, OR 1 Strong + >= 3 Supporting |
| Likely Pathogenic | PVS1 + 1 Moderate, OR 1 Strong + 1-2 Moderate, OR >= 3 Moderate |
| VUS | Criteria do not meet Pathogenic/Likely Pathogenic or Benign/Likely Benign thresholds |
| Likely Benign | 1 Strong + 1 Supporting, OR >= 2 Supporting |
| Benign | BA1 standalone, OR >= 2 Strong |

---

## Step 3: Database and Literature Review

For each variant, review authoritative sources:

- **ClinVar**: Check aggregate classification, number of submitters, and ClinGen Expert Panel reviews (3-star or 4-star classifications carry highest weight).
- **ClinGen**: Check for gene-disease validity, dosage sensitivity, and variant-level expert curation.
- **gnomAD**: Check allele frequency across populations. Note that some pathogenic variants (e.g., BRCA1 185delAG in Ashkenazi Jewish population) are present at low but non-negligible population frequencies.
- **LOVD/HGMD**: Gene-specific databases for additional variant records.
- **PubMed/literature**: Search for functional studies, case reports, and segregation data.
- **In silico predictions**: REVEL (score > 0.7 suggests pathogenic), CADD (> 20 suggests deleterious), SpliceAI (> 0.5 suggests splice impact).

---

## Step 4: Clinical Actionability and Reporting

Map classified variants to clinical management guidelines:

- **Pathogenic/Likely Pathogenic**: State the clinical implications explicitly. For BRCA1 pathogenic variant: cite NCCN Genetic/Familial High-Risk Assessment guidelines for recommended surveillance (breast MRI, risk-reducing surgery consideration, family testing).
- **VUS**: Clearly state that VUS should NOT be used for clinical decision-making. Recommend periodic reclassification review (VUS reclassification rate: ~10% over 5 years, with ~90% of reclassified VUS being downgraded to benign).
- **Benign/Likely Benign**: No clinical action required; report for completeness.
- **Secondary findings (ACMG SF v3.2)**: If incidental pathogenic/likely pathogenic variants are found in the 81 ACMG-recommended genes and consent permits, report per ACMG policy.
- **Pharmacogenomic implications**: If PGx variants are detected (e.g., DPYD, CYP2D6, CYP2C19), report with CPIC guideline-based dosing recommendations.

---

## Step 5: Report Construction

Structure the genetic test report per ACMG reporting standards:

1. **Test information**: Gene list, methodology, platform, reference genome, CNV detection capability.
2. **Results summary**: Positive, negative, or inconclusive (VUS only). List all pathogenic/likely pathogenic variants and VUS.
3. **Variant details**: Gene, transcript, HGVS nomenclature (c. and p.), zygosity, classification, evidence summary.
4. **Clinical interpretation**: For each pathogenic/likely pathogenic variant, state the associated condition, inheritance pattern, penetrance, and management guideline.
5. **VUS section**: List separately with statement about periodic reclassification.
6. **Negative pertinent findings**: Specifically state key genes that were negative when clinically expected.
7. **Limitations**: Coverage gaps, genes not included, CNV detection limitations, and any regions with suboptimal depth.
8. **Recommendations**: Genetic counseling referral, cascade family testing, and clinical follow-up.
9. **Signatures**: Interpreting geneticist/molecular pathologist and laboratory director.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is every reported variant classified using the ACMG/AMP five-tier system with documented evidence criteria?
2. Are HGVS nomenclature conventions followed for all variant descriptions (transcript ID, c. and p. notation)?
3. Is actionability guidance provided for pathogenic/likely pathogenic variants with specific guideline citations?
4. Is the VUS statement clear that VUS should not guide clinical decisions?
5. Are test limitations (coverage gaps, CNV detection capability) explicitly stated?

---

## Quality Audit

- [ ] Clinical indication and family history documented
- [ ] Informed consent verified including secondary findings preference
- [ ] Specimen quality and sequencing coverage metrics documented
- [ ] Each variant classified per ACMG/AMP five-tier system with evidence codes cited
- [ ] ClinVar, ClinGen, and gnomAD reviewed for each variant
- [ ] In silico predictions documented (REVEL, CADD, SpliceAI)
- [ ] HGVS nomenclature used with transcript reference
- [ ] Pathogenic/likely pathogenic variants linked to clinical management guidelines (NCCN, ACMG)
- [ ] VUS reported with explicit statement against clinical use
- [ ] ACMG SF v3.2 secondary findings addressed per consent
- [ ] CNV/deletion-duplication analysis status documented
- [ ] Test limitations and coverage gaps stated
- [ ] Genetic counseling referral recommended
- [ ] Report signed by qualified molecular geneticist or molecular pathologist

---

## Guidelines

- Apply the ACMG/AMP five-tier classification framework to every germline variant; do not use custom tiers or hybrid classification systems
- Document every evidence criterion (PVS, PS, PM, PP, BS, BP) used to reach the classification; the classification must be reproducible from the documented evidence
- Check ClinVar for ClinGen Expert Panel classifications (3-star or 4-star) before independent curation; these carry the highest authority
- Never recommend clinical action based on a VUS; clearly communicate to the clinician and patient that VUS may be reclassified with additional evidence over time
- For BRCA1/2 and Lynch syndrome genes, ensure deletion/duplication analysis is included; up to 15% of pathogenic variants in BRCA1 are large genomic rearrangements
- Apply gene-specific ACMG/AMP specification rules when available (e.g., ClinGen-published specifications for RASopathy genes, hearing loss genes)
- Always recommend genetic counseling for patients receiving pathogenic/likely pathogenic results, both for the patient and for at-risk family members
- Periodically reclassify VUS (at minimum annually or when new evidence is published); maintain a VUS tracking system for proactive reclassification
