---
name: analyzing-epidemiological-data
language: en
description: Structures epidemiologic analysis with incidence, prevalence, rate calculations, and statistical inference. Use when calculating disease rates, analyzing epi data, or interpreting population statistics.
tags:
  - analysis
  - public-health
metadata:
  author: casemark
  practice_areas:
    - Public Health
    - Epidemiology
    - Preventive Medicine
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing Epidemiological Data

## Why This Skill Exists

Epidemiologic data analysis transforms raw surveillance counts into actionable intelligence — incidence rates, prevalence estimates, risk ratios, and trend assessments that drive public health decision-making. Errors in rate calculation, denominator selection, or age-adjustment produce misleading comparisons that can misallocate millions in public health funding. This skill provides the structured analytic workflow expected by CDC, CSTE, and state epidemiology offices, ensuring calculations follow the conventions established in Principles of Epidemiology in Public Health Practice (CDC SS1978) and are reproducible using standard tools like EpiInfo, SAS, or R.

---

## Checkpoint A — Intake and Scoping

### Intake Questions

1. What is the analytic question — disease burden estimation, trend comparison, risk factor association, or program effectiveness?
2. What data sources are available — NNDSS, BRFSS, YRBSS, NHANES, vital records, hospital discharge data, claims data, or custom surveillance?
3. What is the geographic unit of analysis — national, state, county, census tract, or zip code?
4. What is the time frame — single year, multi-year trend, or outbreak period?
5. Is age-adjustment required for comparison across populations?
6. What statistical software and version will be used? (Determines output format and weight handling.)
7. Are there suppression rules for small cell sizes (state or NCHS standards)?
8. Who is the audience — technical (epi team), policy (health officer), or public (health department website)?

### Required Documents

- Dataset or data extract with codebook/data dictionary
- Population denominators from Census Bureau (intercensal or postcensal estimates) or denominator files from the data system
- CSTE or program-specific case definitions applied during data collection
- Prior analytic reports for the same topic (for consistency in methods)
- Data-use agreement and IRB approval documentation if using restricted-access data
- Healthy People 2030 targets for the relevant indicators (if benchmarking)

---

## Step 1 — Assess Data Quality

Before any calculation:

- **Completeness**: Tabulate missing values for each key variable. Flag variables with > 15% missing for sensitivity analysis.
- **Accuracy**: Cross-validate a sample of records against source documents or laboratory confirmations.
- **Timeliness**: Determine reporting lag — median days from event to record entry. Note if provisional data may change.
- **Consistency**: Check for coding changes across years (ICD-9 to ICD-10 transition, CSTE case definition revisions).
- **Representativeness**: Assess whether the data capture the full population at risk or only a sentinel subset.

Document all data quality findings. They constrain the interpretive strength of any downstream analysis.

---

## Step 2 — Calculate Core Epidemiologic Measures

### Incidence

- **Incidence rate (person-time)** = New cases / Person-time at risk. Express per 100,000 person-years for chronic diseases, per 100,000 population for annual surveillance.
- **Cumulative incidence (risk)** = New cases / Population at risk at start of period. Used for fixed-cohort analyses.
- **Attack rate** = Cases / Population at risk during an outbreak. A special case of cumulative incidence.

### Prevalence

- **Point prevalence** = Existing cases at a point in time / Total population at that time.
- **Period prevalence** = Existing cases during a defined period / Mid-period population.

### Mortality

- **Crude death rate** = Deaths / Mid-year population × 100,000.
- **Cause-specific mortality rate** = Deaths from cause / Mid-year population × 100,000.
- **Case fatality rate** = Deaths from disease / Cases of disease × 100. (Not a true rate — a proportion.)

### Measures of Association

- **Relative risk (RR)** = Incidence in exposed / Incidence in unexposed. Used in cohort studies.
- **Odds ratio (OR)** = (a × d) / (b × c) from a 2×2 table. Used in case-control studies; approximates RR when disease is rare.
- **Attributable risk (AR)** = Incidence in exposed − Incidence in unexposed. Quantifies excess risk due to exposure.
- **Population attributable fraction (PAF)** = (Incidence total − Incidence unexposed) / Incidence total. Quantifies public health impact.

---

## Step 3 — Standardize and Adjust Rates

**Direct age-adjustment** (preferred when stratum-specific rates are stable):
- Apply observed age-specific rates to the 2000 U.S. standard population (19 age groups per NCHS).
- Sum the expected counts across strata and divide by the total standard population.
- Report as age-adjusted rate per 100,000.

**Indirect age-adjustment** (when stratum-specific rates are unstable due to small numbers):
- Apply a reference population's age-specific rates to the study population's age distribution.
- Calculate the Standardized Mortality Ratio (SMR) = Observed deaths / Expected deaths.
- SMR > 1.0 indicates excess mortality relative to the reference.

Always specify the standard population and method in footnotes. Never compare a directly adjusted rate to an indirectly adjusted rate.

---

## Step 4 — Test Hypotheses and Quantify Uncertainty

- Calculate 95% confidence intervals for all rates, ratios, and proportions.
- For rate comparisons: use normal approximation for large counts, exact Poisson for counts < 20.
- For 2×2 tables: chi-square test (expected cells ≥ 5) or Fisher's exact test (any expected cell < 5).
- For trend analysis: Joinpoint regression (NCI Joinpoint software) to identify statistically significant changes in annual percent change (APC).
- For multivariable analysis: logistic regression (binary outcome), Poisson/negative binomial regression (count outcome), Cox proportional hazards (time-to-event).
- For survey data (BRFSS, NHANES): apply survey weights, strata, and PSU using appropriate procedures (PROC SURVEYFREQ, svydesign in R).

Report p-values alongside confidence intervals, but emphasize magnitude of effect and public health significance over statistical significance alone.

---

## Step 5 — Visualize and Communicate Results

- **Tables**: Present rates with numerators, denominators, and 95% CIs. Suppress cells with counts 1-4 per NCHS reliability standards (RSE > 30% = unreliable; RSE 20-30% = flag).
- **Figures**: Epi curves, trend lines with confidence bands, choropleth maps with appropriate class intervals (quantile or natural breaks).
- **Comparisons**: Always include the referent group, the comparison period, and the standard population in table footnotes.
- **Context**: Benchmark against Healthy People 2030 targets, national MMWR data, or peer jurisdictions.
- **Interpretation**: State findings in plain language for non-epidemiologist audiences. Distinguish correlation from causation.

---

## Checkpoint B — Analysis Review

- [ ] All measures calculated with explicit numerator, denominator, and multiplier documented
- [ ] Age-adjustment method and standard population specified
- [ ] Confidence intervals reported for every point estimate
- [ ] Small-cell suppression rules applied consistently
- [ ] Survey weights applied for complex survey designs
- [ ] Data limitations section included in report
- [ ] All code/queries saved and version-controlled for reproducibility
- [ ] Results reviewed by senior epidemiologist before release

---

## Quality Audit

- [ ] Denominator source documented with Census vintage year
- [ ] ICD code version consistent across the entire analysis period (no mixed ICD-9/ICD-10 without crosswalk)
- [ ] Rate calculations match when manually verified for at least one stratum
- [ ] Joinpoint or trend test results include APC and p-value for each segment
- [ ] BRFSS/YRBSS analyses account for complex survey design (weighted, stratified, clustered)
- [ ] Mortality analyses distinguish underlying cause from contributing cause coding
- [ ] PAF calculations use correct formula variant for the study design (cohort vs. cross-sectional)
- [ ] All outputs labeled DRAFT until senior review complete

---

## Guidelines

- Never compare crude rates across populations with different age structures. Always age-adjust or present stratum-specific rates.
- Always report the absolute number of cases alongside rates. A rate of 500 per 100,000 based on 5 cases in a population of 1,000 is unreliable.
- Distinguish incidence from prevalence in all outputs. Incidence measures new cases; prevalence measures existing cases. Confusing them leads to incorrect intervention targeting.
- When using BRFSS data, acknowledge the shift from landline-only to dual-frame (landline + cell) sampling that occurred in 2011. Pre-2011 and post-2011 BRFSS data are not directly comparable without raking adjustment.
- For Healthy People 2030 benchmarking, use the data source and methodology specified in the objective's data documentation — not a proxy data source.
- Mark any AI-generated analysis output as [DRAFT — REQUIRES EPIDEMIOLOGIST REVIEW] until a credentialed professional has validated the methods and interpretation.
