---
name: writing-clinical-study-reports
language: en
description: Creates ICH E3-compliant clinical study reports with required sections and data presentation. Use when writing CSRs, formatting study reports, or preparing regulatory submissions.
tags:
  - drafting
  - clinical-research
  - regulatory
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Biostatistics
    - Regulatory Affairs
  document_types:
    - Written Document
  skill_modes:
    - Drafting
---

# Writing Clinical Study Reports

## Why This Skill Exists

The Clinical Study Report (CSR) is the definitive regulatory document for a completed clinical trial and a required component of CTD Module 5 in NDA/BLA/MAA submissions. ICH E3 defines the structure, and regulators evaluate the CSR's completeness and accuracy as a measure of data integrity. A deficient CSR generates FDA information requests, delays review timelines, and can undermine an entire submission. This skill encodes the ICH E3 section-by-section writing workflow with current FDA and EMA expectations.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What is the study number, phase, and therapeutic area?
2. Is this a full CSR, abbreviated CSR, or synoptic CSR?
3. What is the regulatory pathway (NDA 505(b)(1), 505(b)(2), BLA, MAA)?
4. What is the finalized and locked Statistical Analysis Plan (SAP) version?
5. Are all TLFs (tables, listings, figures) finalized and QC-complete?
6. Has the database been locked and the data management report finalized?
7. What medical writing style guide applies (AMA, sponsor-specific)?
8. What are the individual study reports included in the submission (for cross-referencing)?
9. Are there any FDA or EMA deficiency letters or meeting minutes affecting this report?
10. What is the target completion date for the CSR?

### Required Source Documents
- Protocol and all amendments
- Statistical Analysis Plan (final locked version)
- Final TLFs (tables, listings, figures)
- SDTM and ADaM datasets with define.xml
- Investigator's Brochure (current edition)
- Data Management Report
- Medical Monitor's safety review
- DSMB reports and recommendations (if applicable)
- Protocol deviation log
- Participant narratives for deaths, SAEs, and discontinuations due to AEs

---

## Step 1 — Build the ICH E3 Section Structure

Create the report using the mandatory ICH E3 structure. Key sections:

| Section | Title | Key Content |
|---------|-------|-------------|
| 1 | Title Page | Study number, compound, indication, sponsor, report date |
| 2 | Synopsis | 3-5 page structured summary (not an abstract — a standalone summary) |
| 3 | Table of Contents | All sections, tables, figures, appendices with page numbers |
| 4 | List of Abbreviations | Every abbreviation used in the report |
| 5 | Ethics | IRB/IEC approvals, consent process, compliance with GCP |
| 6 | Investigators and Study Sites | List of all investigators, sites, and enrollment per site |
| 7 | Introduction | Background, rationale, development context |
| 8 | Study Objectives | Primary, secondary, exploratory — verbatim from protocol |
| 9 | Investigational Plan | Study design, population, treatments, endpoints, statistical methods |
| 10 | Study Participants | Disposition (CONSORT diagram), protocol deviations, demographics |
| 11 | Efficacy Evaluation | Primary and secondary endpoint results |
| 12 | Safety Evaluation | AEs, lab, vital signs, ECG, safety conclusions |
| 13 | Discussion and Conclusions | Benefit-risk interpretation |
| 14 | Tables, Figures, Graphs | Referenced in text |
| 15 | Reference List | Published literature cited |
| 16 | Appendices | 16.1 Protocol, 16.2 SAP, 16.3 IRB docs, 16.4 Investigators, and others as specified |

---

## Step 2 — Write the Synopsis

The synopsis is often the first (and sometimes only) section reviewers read. Structure it as:

1. **Study identification**: Title, number, phase, compound, INN
2. **Study design**: Brief description including blinding, randomization, controls, duration
3. **Objectives**: Primary and key secondary
4. **Methodology**: Population, sample size, key procedures
5. **Statistical methods**: Primary analysis, key sensitivity analyses
6. **Study population**: Disposition (screened, randomized, completed, discontinued with reasons)
7. **Efficacy results**: Primary endpoint result with CI and p-value; key secondary results
8. **Safety results**: Overview of AE profile; SAEs and deaths summary
9. **Conclusions**: 2-3 sentences on efficacy and safety conclusions

The synopsis must be self-contained — a reader should understand the study without reading the full CSR.

---

## Step 3 — Write the Efficacy Section (Section 11)

Structure the efficacy evaluation:

1. **Analysis populations**: Define and justify each population used; present disposition table
2. **Primary endpoint analysis**: Present the pre-specified analysis exactly as in the SAP; include the primary TLF, LS means or proportions, CI, p-value, and effect size
3. **Sensitivity analyses**: Present each planned sensitivity analysis and whether it supports the primary conclusion
4. **Missing data**: Describe extent of missing data by arm and visit; present sensitivity analyses for missing data (tipping point, pattern mixture)
5. **Secondary endpoints**: Present in hierarchical order per multiplicity plan; clearly state whether each met statistical significance accounting for the adjustment
6. **Subgroup analyses**: Forest plots for pre-specified subgroups (sex, age, race, region, baseline severity); report interaction p-values; do not claim subgroup effects without pre-specification
7. **Exploratory analyses**: Clearly label as hypothesis-generating; present without formal inferential statements

---

## Step 4 — Write the Safety Section (Section 12)

Structure the safety evaluation per ICH E3 and FDA safety-reporting expectations:

1. **Extent of exposure**: Duration, dose levels, total participant-years of exposure per arm
2. **Adverse events**: Overall AE incidence; table by SOC and PT (≥X% in any arm); treatment-related AEs; AEs leading to discontinuation
3. **Deaths and serious adverse events**: Individual narratives for all deaths; SAE summary table; narratives for treatment-related SAEs
4. **Adverse events of special interest**: Protocol-defined AESIs with detailed analysis
5. **Laboratory evaluations**: Shift tables (baseline → worst post-baseline); PCS values; Hy's Law analysis with eDISH plot
6. **Vital signs and ECG**: Summarize by visit with clinically notable values flagged
7. **Safety conclusions**: Integrated narrative of the safety profile; characterize the most common AEs, serious risks, and any signals requiring further monitoring

---

## Step 5 — Write the Discussion and Conclusions (Section 13)

This section provides the interpretive framework:

1. **Efficacy interpretation**: Place primary-endpoint results in context of clinical meaningfulness and prior studies; discuss consistency across sensitivity analyses and subgroups
2. **Safety interpretation**: Characterize the safety profile relative to the therapeutic area and comparator; identify new safety signals vs. known class effects
3. **Benefit-risk assessment**: Synthesize efficacy and safety findings into an overall benefit-risk statement for the target population
4. **Study limitations**: Address design limitations, missing data impact, generalizability considerations
5. **Conclusions**: Concise summary of key findings and implications for the development program

---

## Step 6 — Compile Appendices (Section 16)

ICH E3 specifies the following appendix structure:

- **16.1**: Protocol and protocol amendments (with dates)
- **16.2**: Sample CRF (annotated with SDTM mapping is current best practice)
- **16.3**: IRB/IEC approvals and consent forms (list of all sites with approval dates)
- **16.4**: List of investigators and qualifications
- **16.5**: Randomization scheme documentation (not the actual list, which is kept separately)

Additional appendices as needed:
- Individual participant data listings for safety (deaths, SAEs, discontinuations)
- Bioanalytical methods validation reports (PK studies)
- Publications arising from the study

---

## Step 7 — Quality Review and Formatting

Before declaring the CSR final:

1. **Internal consistency check**: All numbers in text match TLFs; CONSORT diagram counts reconcile; enrollment numbers are consistent across sections
2. **Cross-referencing**: All table/figure/section references resolve correctly
3. **Medical writing review**: AMA style compliance, consistent terminology, defined abbreviations
4. **Biostatistics review**: Statistical methods and results descriptions are accurate
5. **Clinical review**: Medical interpretation is appropriate; benefit-risk is balanced
6. **Regulatory review**: ICH E3 completeness checklist; CTD Module 5 formatting requirements

---

## Checkpoint B — CSR Review

1. [ ] All ICH E3 sections are present and in the correct order
2. [ ] Synopsis is self-contained and accurately reflects the full report
3. [ ] Primary endpoint analysis matches the SAP exactly
4. [ ] All TLFs are referenced in text and appendices are complete
5. [ ] CONSORT flow diagram is included with reconciled counts
6. [ ] Safety section includes narratives for all deaths and treatment-related SAEs
7. [ ] Hy's Law analysis is included (or documented as not applicable)
8. [ ] Discussion presents a balanced benefit-risk assessment
9. [ ] Appendix 16.1-16.4 are complete
10. [ ] All numbers in text have been verified against source TLFs

---

## Quality Audit

- [ ] ICH E3 section numbering is correct and complete
- [ ] No efficacy claims exceed what the statistical analysis supports
- [ ] Multiplicity-adjusted conclusions are correctly stated for secondary endpoints
- [ ] MedDRA version is cited in the safety methods
- [ ] All post-hoc analyses are explicitly labeled
- [ ] Protocol deviations that could affect efficacy conclusions are discussed
- [ ] Participant narratives include all required elements (demographics, medical history, event description, causality, outcome)
- [ ] Report version control metadata (date, version number, author) is present
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. The CSR is a factual document — do not include promotional language or unsupported conclusions
2. Present data with confidence intervals, not only p-values; regulators expect effect-size quantification
3. Never modify TLFs in the CSR text — if a discrepancy is found, resolve in the source dataset and regenerate
4. Use past tense for methods and results; present tense for general statements and conclusions
5. The synopsis must function as a standalone document — it is extracted for regulatory review summaries
6. For multi-regional trials, present regional consistency analyses per ICH E17
7. Safety narratives should be clinical descriptions, not recitations of CRF data — add medical interpretation
8. Appendix 16.2 CRF annotations should map to CDISC SDTM domains and variables
9. Mark any section where source data is incomplete or inconsistent with [VERIFY] for team resolution
10. This skill produces CSR drafts — final sign-off requires sponsor medical officer, biostatistician, and regulatory signatory
