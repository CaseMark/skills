---
name: analyzing-vital-statistics
description: Structures vital records analysis with birth, death, and demographic trend reporting. Use when analyzing vital statistics, interpreting mortality data, or reporting demographic trends.
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

# Analyzing Vital Statistics

## Why This Skill Exists

Vital statistics — data derived from birth certificates, death certificates, fetal death reports, and marriage/divorce records — are the foundational data system of public health. They provide the numerators for infant mortality rates, maternal mortality ratios, life expectancy calculations, and cause-specific death rates; and the denominators (through birth data) for perinatal outcome rates. The National Vital Statistics System (NVSS), operated by NCHS, compiles state vital records into national datasets. State vital records offices, following NCHS/NAPHSIS (National Association for Public Health Statistics and Information Systems) standards, are the primary producers. The 2003 revision of the U.S. Standard Certificate of Live Birth and the ongoing modernization of death certification (electronic death registration systems, EDRS) have changed data elements and quality. Errors in vital statistics analysis — wrong denominator vintage, misattributed cause of death, failure to use the linked birth-infant death file — produce misleading indicators that misinform policy. This skill provides the rigorous analytic framework for vital records analysis.

---

## Checkpoint A — Intake and Scoping

### Intake Questions

1. What vital records data are being analyzed — births, deaths (all-cause or cause-specific), fetal deaths, linked birth-infant deaths, or a combination?
2. What is the time period and geographic scope — single year, multi-year trend, state, county, or sub-county?
3. What indicators are being calculated — infant mortality rate, neonatal/postneonatal components, maternal mortality ratio, life expectancy, cause-specific death rates, preterm birth rate, low birth weight rate?
4. Is this analysis for a routine annual vital statistics report, a CHNA, a Title V needs assessment, or a specific research question?
5. What cause-of-death coding is relevant — ICD-10 underlying cause, multiple cause, or injury cause (external cause codes)?
6. Are linked files available (linked birth-infant death file, linked birth-maternal mortality file)?
7. What suppression rules apply for small cell sizes (state-specific or NCHS standards)?
8. What denominator source will be used — live births from vital records (for perinatal rates), Census population estimates (for death rates)?

### Required Documents

- Birth certificate data file (individual-level or tabulated) with data dictionary
- Death certificate data file with ICD-10 underlying cause and multiple cause codes
- Fetal death report data (if analyzing perinatal mortality)
- Linked birth-infant death file (period or cohort linked file from NCHS or state)
- Census Bureau population estimates (postcensal or intercensal) for denominator calculations
- 2003 U.S. Standard Certificate of Live Birth — to understand available data elements
- NCHS vital statistics data quality report for the relevant state and year
- State vital records statutes governing data access, suppression, and release

---

## Step 1 — Prepare and Validate Vital Records Data

- **Birth data**: Verify data elements from the 2003 revision birth certificate (or the 1989 revision for jurisdictions that have not yet adopted). Key variables: maternal age, race/ethnicity (mother's self-reported), education, prenatal care (month of first visit, number of visits), gestational age (obstetric estimate), birth weight, plurality, delivery method, maternal morbidity, paternity acknowledgment.
- **Death data**: Verify ICD-10 underlying cause coding. Understand that underlying cause is determined by NCHS automated (SuperMICAR/MMDS) or manual nosologist coding from the cause-of-death chain on the death certificate. Key variables: decedent demographics, date of death, place of death, manner of death, underlying and contributing causes, certifier type (physician, medical examiner/coroner).
- **Data quality checks**:
  - Completeness of registration (≥ 99% for births and deaths in most U.S. jurisdictions).
  - Percent of death certificates with ill-defined underlying cause (R99, R00-R99 block): should be < 2% for a well-functioning vital records system.
  - Percent of birth certificates with unknown gestational age or birth weight: flag if > 1%.
  - Percent of death certificates certified by medical examiner/coroner vs. attending physician (affects cause-of-death accuracy for different cause categories).
- **Linkage**: For infant mortality analysis, use the NCHS linked birth-infant death file, which links each infant death record to its corresponding birth certificate. This enables analysis of infant mortality by birth certificate characteristics (maternal age, race, prenatal care, birth weight, gestational age).

---

## Step 2 — Calculate Core Vital Statistics Indicators

### Birth-Based Indicators
- **General fertility rate** = Live births / Women aged 15-44 × 1,000
- **Total fertility rate** = Sum of age-specific fertility rates × 5 (synthetic cohort estimate of lifetime births per woman)
- **Preterm birth rate** = Live births < 37 weeks gestation / Total live births × 100
- **Low birth weight rate** = Live births < 2,500 grams / Total live births × 100
- **Very low birth weight rate** = Live births < 1,500 grams / Total live births × 100
- **Cesarean delivery rate** = Cesarean deliveries / Total live births × 100
- **Teen birth rate** = Live births to mothers aged 15-19 / Female population aged 15-19 × 1,000

### Death-Based Indicators
- **Crude death rate** = Deaths / Mid-year population × 100,000
- **Age-adjusted death rate** = Direct method using 2000 U.S. standard population (19 age groups per NCHS standard)
- **Cause-specific death rate** = Deaths from cause X / Mid-year population × 100,000
- **Infant mortality rate (IMR)** = Infant deaths (< 1 year) / Live births × 1,000 (use period-linked file for annual estimates)
- **Neonatal mortality rate** = Deaths < 28 days / Live births × 1,000
- **Postneonatal mortality rate** = Deaths 28-364 days / Live births × 1,000
- **Perinatal mortality rate** = (Fetal deaths ≥ 28 weeks + early neonatal deaths < 7 days) / (Live births + fetal deaths ≥ 28 weeks) × 1,000
- **Maternal mortality ratio** = Maternal deaths (ICD-10 codes O00-O99, A34 within 42 days of pregnancy termination) / Live births × 100,000

### Life Table Indicators
- **Life expectancy at birth** = Expected number of years a newborn would live under current age-specific mortality rates. Constructed from an abridged life table (Chiang method or Greville method).
- **Years of potential life lost (YPLL)** = Sum of (reference age − age at death) for all deaths before reference age (typically 75).

---

## Step 3 — Analyze Trends and Disparities

- Plot multi-year trends (10-20 year series) for key indicators. Use Joinpoint regression (NCI Joinpoint software) to identify statistically significant trend changes. Report annual percent change (APC) for each segment.
- Stratify all indicators by race/ethnicity. For birth outcomes, use mother's race/ethnicity. For death outcomes, use decedent's race/ethnicity. Note that race/ethnicity on death certificates is reported by the funeral director (proxy report), which introduces misclassification, particularly for American Indian/Alaska Native and Hispanic decedents.
- Calculate disparity ratios (e.g., Black IMR / White IMR) and absolute differences. Track whether disparities are narrowing or widening over time.
- For small-population analyses (counties, racial/ethnic subgroups), use 3-year or 5-year aggregated rates to stabilize estimates. Calculate 95% confidence intervals using the gamma method for rates based on small counts.
- Compare to benchmarks: Healthy People 2030 targets, national NCHS rates, state averages, and peer jurisdiction rates.

---

## Step 4 — Conduct Special Analyses

Based on the analytic question, conduct deeper analysis:

- **Infant mortality decomposition**: Use Kitagawa decomposition to partition IMR differences between populations into components attributable to differences in birth weight distribution vs. differences in birth weight–specific mortality rates.
- **Excess mortality analysis**: For pandemic or disaster impact assessment, calculate excess deaths = observed deaths − expected deaths (based on prior 5-year average or model-predicted baseline). Use the Serfling regression method or CDC's excess mortality model.
- **Multiple cause-of-death analysis**: Analyze all conditions listed on the death certificate (not just underlying cause) to assess the contribution of conditions like diabetes, hypertension, or substance use that frequently appear as contributing causes.
- **Maternal mortality review**: Support Maternal Mortality Review Committees (MMRCs) by providing vital records data linked to medical records for case abstraction. Classify maternal deaths by timing (pregnancy, delivery, postpartum), preventability (probably/possibly preventable), and contributing factors (using the CDC MMRIA system).

---

## Step 5 — Report and Disseminate

- Produce the annual vital statistics report following NCHS/state conventions: executive summary, data tables, figures, technical notes.
- Include detailed technical notes: data sources, population denominators, cause-of-death coding, suppression rules, standard population used for age-adjustment, and data quality caveats.
- Publish data through multiple channels: annual report document, interactive data dashboard, community health data portal, and data briefs on priority topics.
- Ensure data access policies comply with state vital records statutes — some states restrict access to individual-level data to authorized researchers with approved protocols.

---

## Checkpoint B — Analysis Review

- [ ] Data quality assessment completed (completeness, ill-defined causes, missing variables)
- [ ] Indicators calculated with explicit numerator, denominator, and multiplier documented
- [ ] Linked birth-infant death file used for infant mortality analysis (not unlinked)
- [ ] Age-adjustment applied using 2000 U.S. standard population
- [ ] Confidence intervals reported for all rates, especially those based on small counts
- [ ] Racial/ethnic misclassification acknowledged for death certificate–based indicators
- [ ] Trend analysis includes Joinpoint results with APC and statistical significance
- [ ] Technical notes complete and appended to the report

---

## Quality Audit

- [ ] Birth certificate revision (2003 vs. 1989) documented, with notes on comparability for jurisdictions that transitioned mid-series
- [ ] ICD-10 coding used for all death data from 1999 forward; ICD-9 to ICD-10 comparability ratios applied if bridging pre/post-1999 data
- [ ] Gestational age variable uses obstetric estimate (2003 revision) rather than LMP-based estimate for preterm birth calculations
- [ ] Maternal mortality ratio uses pregnancy checkbox (2003 revision) with awareness that its introduction inflated reported maternal mortality
- [ ] Race/ethnicity bridging file applied when comparing across race classification changes (1977 OMB vs. 1997 OMB standards)
- [ ] Suppression rules applied consistently: suppress rates based on numerator < 10 (or per state standard); flag rates based on numerator 10-19 as unreliable
- [ ] Life expectancy tables use an appropriate method (Chiang or Greville) with decrement assumptions stated
- [ ] All data files stored per state vital records data security requirements

---

## Guidelines

- Vital statistics are legal records. Every birth and death certificate is a legal document, and data derived from them carry particular obligations for accuracy, confidentiality, and responsible use.
- The 2003 birth certificate revision introduced significant changes (obstetric estimate of gestational age, new maternal morbidity fields, revised race/ethnicity categories). Do not mix data from 2003-revision and 1989-revision jurisdictions in the same analysis without adjustment.
- Maternal mortality measurement in the U.S. is confounded by the pregnancy checkbox on the death certificate, which was adopted on different dates across states (2003-2017). This staggered adoption artificially inflated the apparent maternal mortality ratio. Note the checkbox adoption date for any state in the analysis.
- Race/ethnicity on death certificates is reported by funeral directors (proxy report) and is known to undercount American Indian/Alaska Native and Hispanic decedents. Use NCHS misclassification correction factors where available.
- For county-level analysis, single-year rates for small counties are unstable. Use multi-year aggregation, Bayesian smoothing, or spatial smoothing to produce reliable sub-state estimates.
- Excess mortality analysis should present ranges (e.g., "estimated 15,000-20,000 excess deaths") rather than false-precision point estimates. Model assumptions (baseline period, expected seasonal pattern, demographic changes) significantly influence results.
- Escalate to state vital registrar or NCHS when: a data quality issue is identified (e.g., spike in ill-defined cause-of-death codes), a coding change affects trend comparability, or a request for individual-level data requires legal review.
