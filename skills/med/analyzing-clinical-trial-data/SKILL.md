---
name: analyzing-clinical-trial-data
language: en
description: Structures clinical trial data analysis with primary endpoint evaluation and safety reporting. Use when analyzing trial results, evaluating endpoints, or preparing statistical reports.
tags:
  - analysis
  - clinical-research
  - clinical
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Biostatistics
    - Regulatory Affairs
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing Clinical Trial Data

## Why This Skill Exists

Clinical trial data analysis translates raw study data into evidence that regulators, clinicians, and payers act on. Errors in analysis — wrong population sets, incorrect handling of missing data, failure to control multiplicity — can result in complete response letters, advisory-committee failures, or post-marketing safety crises. This skill implements the statistical analysis workflow defined by ICH E9 (Statistical Principles for Clinical Trials), ICH E9(R1) (Estimands), FDA guidance on clinical trial endpoints, and CDISC standards to produce analyses that withstand regulatory scrutiny.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What is the study phase (I–IV) and therapeutic area?
2. What are the primary, secondary, and exploratory endpoints as defined in the protocol?
3. Is the Statistical Analysis Plan (SAP) finalized and locked before database lock?
4. What analysis populations are defined (ITT, mITT, per-protocol, safety)?
5. What is the randomization structure (stratification factors, adaptive elements)?
6. Are there interim analyses with alpha-spending considerations?
7. What is the data format (CDISC SDTM, ADaM, legacy)?
8. Has database lock been confirmed? What is the lock date?
9. Are there any protocol deviations affecting the analysis populations?
10. What are the deliverable formats (tables, listings, figures — TLF shells)?

### Required Source Documents
- Finalized and signed Statistical Analysis Plan (SAP)
- Protocol (including all amendments)
- TLF shells (mock table/listing/figure specifications)
- SDTM and ADaM datasets with define.xml
- Randomization list (unblinded, post-database lock)
- Protocol deviation log
- Data Management Report (query resolution status, edit checks)
- Medical coding dictionaries (MedDRA version, WHO Drug Dictionary version)

---

## Step 1 — Define and Verify Analysis Populations

Construct each analysis population per the SAP:

- **Intent-to-Treat (ITT)**: All randomized participants analyzed as randomized, regardless of protocol adherence. This is the primary population for superiority trials per ICH E9.
- **Modified ITT (mITT)**: ITT minus participants who never received study drug or have no post-baseline efficacy assessment. Document specific exclusion criteria.
- **Per-Protocol (PP)**: Participants who completed the study without major protocol deviations. Define deviation types that trigger PP exclusion (wrong treatment, insufficient exposure, prohibited medications, missed primary-endpoint assessments).
- **Safety population**: All participants who received at least one dose of study medication, analyzed as treated (not as randomized).

Reconcile population counts across datasets. Any discrepancy between randomization list and safety/ITT counts requires documentation.

---

## Step 2 — Produce Demographic and Baseline Tables

Generate the CONSORT-required baseline comparison table:

1. Demographics: age (mean, SD, median, range), sex, race/ethnicity (per FDA and NIH reporting requirements), BMI
2. Disease characteristics: diagnosis duration, disease severity scores, prior treatments, relevant biomarkers
3. Stratification factors: verify balance across treatment arms
4. Baseline efficacy measures: values for primary and key secondary endpoints at baseline
5. Present continuous variables as mean (SD) and median (Q1, Q3); categorical variables as n (%)
6. Do not perform hypothesis tests on baseline characteristics (CONSORT guidance) — describe imbalances narratively

---

## Step 3 — Analyze Primary Endpoint

Execute the pre-specified primary analysis exactly as stated in the SAP:

### For Continuous Endpoints
- ANCOVA with treatment as fixed effect, stratification factors as covariates, and baseline value as covariate
- MMRM (mixed model for repeated measures) for longitudinal data: treatment, visit, treatment-by-visit interaction, baseline, baseline-by-visit interaction; unstructured covariance
- Report: LS means per group, difference in LS means, 95% CI, p-value

### For Binary Endpoints
- CMH (Cochran-Mantel-Haenszel) test stratified by randomization strata
- Logistic regression as sensitivity analysis
- Report: response rates per group, difference in proportions, 95% CI, odds ratio with 95% CI, p-value

### For Time-to-Event Endpoints
- Kaplan-Meier estimates with log-rank test (stratified if applicable)
- Cox proportional hazards model for hazard ratio with 95% CI
- Verify proportional-hazards assumption (Schoenfeld residuals, log-log plot)
- Report: median time-to-event per group (with 95% CI), HR, p-value, KM curves at key timepoints

### For Count Data / Recurrent Events
- Negative binomial regression or Andersen-Gill model
- Report: rate per group, rate ratio with 95% CI, p-value

---

## Step 4 — Handle Missing Data

Implement the pre-specified missing-data strategy per ICH E9(R1) estimand framework:

1. **Primary approach**: The method that aligns with the chosen estimand (e.g., MMRM under MAR assumption for treatment-policy estimand)
2. **Sensitivity analyses** (required — at least two):
   - Tipping-point analysis: Determine how extreme imputed values must be to reverse the conclusion
   - Pattern-mixture model (MNAR): Reference-based imputation (copy-reference, jump-to-reference)
   - Multiple imputation under various assumptions
   - Worst-case / best-case imputation for binary endpoints
3. **Supplementary analyses**: Complete-case analysis, last-observation-carried-forward (document as sensitivity only — LOCF is no longer acceptable as primary per FDA and EMA guidance)
4. **Documentation**: Report the number and reasons for missing data by treatment arm and visit

---

## Step 5 — Analyze Secondary Endpoints with Multiplicity Control

Apply the pre-specified multiplicity adjustment strategy:

1. **Hierarchical (fixed-sequence) testing**: Test secondary endpoints in pre-specified order; stop testing at first non-significant result. This is the most common approach for pivotal trials.
2. **Graphical approach** (Bretz et al.): Allocate alpha across endpoints with pre-specified propagation rules
3. **Hochberg or Holm step-up/step-down**: When endpoints are independent or positively correlated
4. **Gate-keeping strategies**: For families of primary and secondary endpoints

Analyze each secondary endpoint using the same methodology specified for its data type. Report adjusted and nominal p-values.

---

## Step 6 — Conduct Safety Analysis

Analyze the safety population:

### Adverse Events
- Summarize by System Organ Class (SOC) and Preferred Term (PT) using the specified MedDRA version
- Present: any AE, drug-related AE, serious AE (SAE), AE leading to discontinuation, AE leading to death
- Tabulate by severity grade (CTCAE v5 or mild/moderate/severe)
- For each PT, report incidence (n, %) per treatment arm — not number of events (one participant with multiple episodes counts once)
- Flag imbalances (≥2% difference between arms or ≥2× rate ratio) for medical review

### Laboratory Data
- Shift tables (baseline category → worst post-baseline category)
- Potentially clinically significant (PCS) values: define thresholds per parameter; tabulate n (%) meeting PCS criteria by arm
- Liver safety: apply Hy's Law criteria (ALT >3× ULN + bilirubin >2× ULN without cholestasis); generate eDISH plot

### Vital Signs, ECG, Other Safety
- Summarize by visit with change-from-baseline; flag PCS values
- QTc analysis per ICH E14 if applicable

---

## Step 7 — Generate Tables, Listings, and Figures (TLFs)

Produce all TLFs per the pre-approved shells:

- Follow CDISC Analysis Results Metadata (ARM) standards
- Tables: formatted with proper headers, footnotes, population counts (N = per arm), and statistical references
- Listings: participant-level data for SAEs, deaths, discontinuations, protocol deviations, and concomitant medications
- Figures: KM plots, forest plots for subgroups, waterfall plots (oncology), spider plots (tumor response), bar/line charts for PRO scores
- All output must be reproducible from ADaM datasets with documented programs

---

## Checkpoint B — Analysis Review

1. [ ] Primary analysis matches the SAP exactly (no unplanned modifications)
2. [ ] All analysis populations are correctly derived and counts reconcile
3. [ ] Missing-data handling follows the estimand framework with sensitivity analyses
4. [ ] Multiplicity adjustment is correctly applied in the specified order
5. [ ] Safety tables use correct MedDRA version and incidence-based (not event-based) counting
6. [ ] Hy's Law assessment is completed for studies with hepatotoxicity potential
7. [ ] All TLFs match the pre-approved shells
8. [ ] Subgroup analyses (sex, age, race, region, baseline severity) are conducted for primary endpoint
9. [ ] Statistical programs are validated (double-programming or independent QC)
10. [ ] Unblinding log confirms no premature unblinding occurred

---

## Quality Audit

- [ ] SAP version matches the version referenced in the CSR
- [ ] ADaM datasets are CDISC-compliant with submitted define.xml
- [ ] All p-values are reported to the appropriate decimal precision (typically 4 decimal places)
- [ ] Confidence intervals are consistently 2-sided 95% unless otherwise specified
- [ ] KM curves include number-at-risk tables
- [ ] Forest-plot subgroup analyses include interaction p-values
- [ ] All post-hoc analyses are clearly labeled as exploratory
- [ ] No results are presented that are not derivable from the submitted datasets
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. The SAP must be finalized before database lock and unblinding — any changes after unblinding must be documented and justified as pre-specified sensitivity or clearly labeled post-hoc
2. Never change the primary analysis method after seeing the data without regulatory disclosure
3. Use ITT as the primary population for superiority trials; per-protocol as co-primary for non-inferiority
4. LOCF is no longer acceptable as a primary missing-data method — use MMRM or multiple imputation
5. All statistical programs must have independent QC (double-programming or code review)
6. Report effect estimates with confidence intervals, not only p-values — p-values without effect sizes are insufficient
7. Safety analyses are descriptive — hypothesis testing of AE incidence rates is generally inappropriate
8. Apply the CONSORT flow diagram to document participant disposition through analysis populations
9. Mark any deviation from the SAP with [VERIFY] for biostatistics-lead review
10. This skill produces analysis results — interpretation for regulatory submission requires clinical and regulatory team review
