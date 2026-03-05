---
name: interpreting-biostatistics
description: Structures statistical analysis interpretation with p-value, confidence interval, and effect size reporting. Use when interpreting study statistics, explaining statistical results, or reviewing biostatistical analyses.
tags:
  - analysis
  - clinical-research
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Biostatistics
    - Regulatory Affairs
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Biostatistics

## Why This Skill Exists

Statistical results from clinical studies drive regulatory decisions, clinical practice changes, and billion-dollar market outcomes — yet misinterpretation of p-values, confidence intervals, and effect sizes is endemic in medical literature. A statistically significant result is not necessarily clinically meaningful; a non-significant result does not prove no effect. This skill provides a structured framework for interpreting biostatistical outputs from clinical trials and observational studies, following ASA (American Statistical Association) guidelines on p-values, ICH E9/E9(R1) statistical principles, and CONSORT/STROBE reporting standards.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What type of study produced these results (RCT, observational cohort, case-control, meta-analysis)?
2. What is the primary endpoint and its data type (continuous, binary, time-to-event, ordinal, count)?
3. What statistical test was used for the primary analysis?
4. Was the study designed as superiority, non-inferiority, or equivalence?
5. What was the pre-specified alpha level and was it adjusted for multiplicity or interim analyses?
6. What was the sample size and was the study adequately powered?
7. How was missing data handled (MMRM, multiple imputation, complete case)?
8. What analysis population was used (ITT, mITT, per-protocol)?
9. Are there subgroup analyses, and were they pre-specified?
10. What is the clinical context — what effect size would be considered clinically meaningful?

### Required Source Documents
- Statistical Analysis Plan (SAP) or published methods section
- Results tables (primary endpoint, secondary endpoints, safety)
- Forest plots (for subgroup analyses or meta-analyses)
- Kaplan-Meier curves (for time-to-event data)
- Study protocol (for design parameters and power calculation)
- CONSORT, STROBE, or PRISMA checklist (depending on study type)

---

## Step 1 — Interpret P-Values Correctly

Apply the ASA 2016 statement on statistical significance:

### What a P-Value Is
- The probability of observing data as extreme as (or more extreme than) the observed data, assuming the null hypothesis is true
- It is NOT the probability that the null hypothesis is true
- It is NOT the probability that the result occurred by chance
- It is NOT the probability that the alternative hypothesis is false

### Correct Interpretation Framework
1. **P < alpha (typically 0.05)**: The observed data are unlikely under the null hypothesis. Reject the null in the context of the pre-specified test. This does not prove the treatment works — it means the data are inconsistent with the null at the chosen alpha level.
2. **P ≥ alpha**: The data are not sufficiently inconsistent with the null hypothesis to reject it. This does NOT prove no effect exists — it may reflect inadequate power, large variability, or a true null.
3. **P-values near alpha (e.g., 0.04 vs. 0.06)**: These represent essentially the same level of evidence — do not treat the alpha boundary as a cliff. Report exact p-values; describe the strength of evidence qualitatively.

### Common Misinterpretations to Flag
- "The treatment showed a trend toward significance (p=0.08)" — this is not a valid statistical inference; either the result meets the pre-specified threshold or it does not
- "The study proved the drug is safe" — clinical studies are powered for efficacy, rarely for safety; absence of evidence is not evidence of absence
- "The groups were similar at baseline (all p>0.05)" — hypothesis tests on baseline characteristics are inappropriate; use standardized mean differences
- "The subgroup analysis was significant" — unless pre-specified and adequately powered, this is hypothesis-generating only

---

## Step 2 — Interpret Confidence Intervals

Confidence intervals provide more information than p-values alone:

### Correct Interpretation
- A 95% CI means: if the study were repeated many times, 95% of the calculated CIs would contain the true parameter value
- The CI width reflects precision — determined by sample size and variability
- The CI location relative to the null value (0 for differences, 1 for ratios) determines statistical significance at the corresponding alpha level

### Clinical Interpretation Framework
1. **CI excludes the null AND excludes the MCID**: Statistically significant AND clinically meaningful
2. **CI excludes the null BUT includes the MCID threshold**: Statistically significant BUT uncertain clinical meaningfulness — the true effect could be trivially small
3. **CI includes the null BUT is narrow**: Study adequately powered; likely no clinically meaningful effect
4. **CI includes the null AND is wide**: Study may be underpowered; cannot conclude effect or no effect — inconclusive
5. **CI entirely above the MCID**: Strong evidence of clinically meaningful benefit

### Non-Inferiority Interpretation
- The treatment is non-inferior if the lower bound of the CI for the difference (or upper bound for the ratio, depending on convention) does not cross the pre-specified non-inferiority margin (delta)
- A study can demonstrate both non-inferiority AND superiority if the entire CI excludes zero and the NI margin

---

## Step 3 — Interpret Effect Sizes

Effect sizes quantify the magnitude of the treatment effect:

### For Continuous Outcomes
| Measure | Calculation | Interpretation Anchors |
|---------|-------------|----------------------|
| Mean Difference (MD) | Treatment mean − Control mean | Clinical units; interpret against MCID |
| Standardized Mean Difference (SMD/Cohen's d) | MD / pooled SD | 0.2 small, 0.5 medium, 0.8 large (Cohen's benchmarks — use domain-specific MCIDs when available) |

### For Binary Outcomes
| Measure | Calculation | Interpretation |
|---------|-------------|----------------|
| Risk Difference (RD) | Risk_treatment − Risk_control | Absolute effect; directly yields NNT = 1/RD |
| Relative Risk (RR) | Risk_treatment / Risk_control | Relative effect; RR < 1 means reduced risk |
| Odds Ratio (OR) | Odds_treatment / Odds_control | Approximates RR when event rate <10%; overestimates for common outcomes |
| Number Needed to Treat (NNT) | 1 / RD | How many patients need treatment for one additional good outcome |

### For Time-to-Event Outcomes
| Measure | Calculation | Interpretation |
|---------|-------------|----------------|
| Hazard Ratio (HR) | Instantaneous rate_treatment / rate_control | HR < 1 means slower event rate in treatment; assumes proportional hazards |
| Median Survival Difference | Median_treatment − Median_control | Clinical time units; meaningful when KM curves separate |
| Restricted Mean Survival Time (RMST) | Area under KM curve up to a specified time | Useful when PH assumption violated; yields time gained |

### Always Interpret Effect Size in Context
- A statistically significant but clinically trivial effect size may not support treatment adoption
- A large effect size with a wide CI (few events, small study) needs confirmation
- Relative measures (RR, HR) can exaggerate perceived benefit when baseline risk is low — always report absolute measures alongside

---

## Step 4 — Evaluate Multiplicity and Multiple Comparisons

### When Multiplicity Adjustment Is Required
- Multiple primary endpoints tested at the same alpha
- Multiple secondary endpoints with inferential claims
- Interim analyses that consume alpha
- Multiple subgroup analyses with confirmatory intent

### How to Verify Multiplicity Control
1. **Check the SAP**: Was a multiplicity strategy pre-specified (hierarchical testing, graphical approach, Hochberg, Holm)?
2. **Verify implementation**: Were adjusted p-values or family-wise error rate calculations correctly applied?
3. **Identify claims**: Any secondary endpoint presented as "statistically significant" must have been tested within the multiplicity framework; otherwise it is exploratory
4. **Gate-keeping**: If the primary endpoint failed, secondary endpoints cannot be formally tested regardless of their nominal p-values

### Common Red Flags
- "Significant" secondary endpoints when the primary endpoint missed
- Cherry-picked subgroups with no pre-specification or multiplicity adjustment
- Multiple post-hoc analyses presented as "hypothesis-generating" but framed as though confirmatory

---

## Step 5 — Interpret Subgroup Analyses

Apply the Oxman and Guyatt criteria for credible subgroup effects:

1. **Pre-specified**: Was the subgroup hypothesis specified before data analysis?
2. **Limited number**: Were only a small number of subgroup comparisons made?
3. **Biological plausibility**: Is there a credible biological mechanism for differential effect?
4. **Consistent direction**: Is the finding consistent across related studies?
5. **Statistical evidence**: Is there a significant interaction test (not just within-subgroup p-values)?
6. **Within vs. between**: Do both subgroups show internally consistent results, or does one drive the overall effect?

### Interpretation Rules
- Report interaction p-values, not within-subgroup p-values
- Forest plots should show subgroup estimates with CIs and interaction tests
- Subgroup analyses in a single trial are hypothesis-generating unless the trial was specifically designed and powered for subgroup detection
- Never recommend treatment decisions based on a single subgroup finding from an exploratory analysis

---

## Step 6 — Synthesize the Statistical Interpretation

Produce an integrated interpretation statement:

1. **Primary result**: State the treatment effect (estimate + CI), statistical significance relative to pre-specified alpha, and clinical meaningfulness relative to MCID
2. **Robustness**: Did sensitivity analyses (different populations, missing-data methods, alternative models) support the primary conclusion?
3. **Safety balance**: What is the NNT for benefit vs. NNH (number needed to harm) for key safety events?
4. **Subgroup consistency**: Is the treatment effect consistent across pre-specified subgroups, or are there signals of differential effect?
5. **External consistency**: Is the result consistent with prior studies in the same indication?
6. **Limitations**: State key statistical limitations (power, missing data, multiplicity, post-hoc nature of certain analyses)

---

## Checkpoint B — Interpretation Review

1. [ ] P-values are correctly interpreted per ASA guidance (not as probability of null)
2. [ ] Confidence intervals are reported for all key effect estimates
3. [ ] Effect sizes are interpreted against clinically meaningful thresholds, not just statistical significance
4. [ ] Non-inferiority/equivalence interpretation uses correct CI boundary and margin
5. [ ] Multiplicity adjustment is verified and correctly applied
6. [ ] Subgroup analyses are assessed using interaction tests and credibility criteria
7. [ ] Missing-data impact on conclusions is explicitly addressed
8. [ ] Absolute and relative effect measures are both presented
9. [ ] Statistical limitations are clearly stated
10. [ ] Clinical context is integrated with statistical findings

---

## Quality Audit

- [ ] No p-values are described as "trends toward significance"
- [ ] No baseline-characteristic comparisons use hypothesis tests (SMDs used instead)
- [ ] Non-significant results are not described as "no difference" without power assessment
- [ ] NNT/NNH calculations are based on absolute risk differences, not relative measures
- [ ] Hazard-ratio interpretation includes verification of proportional-hazards assumption
- [ ] Post-hoc analyses are explicitly labeled throughout
- [ ] CONSORT or STROBE checklist items for statistical reporting are satisfied
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. Always report effect estimates with confidence intervals — p-values alone are insufficient for clinical decision-making
2. Statistical significance ≠ clinical significance — a p=0.001 result can be clinically meaningless if the effect size is trivial
3. Absence of evidence is not evidence of absence — non-significant results in underpowered studies are inconclusive, not negative
4. Use absolute measures (RD, NNT) alongside relative measures (RR, OR, HR) — relative measures alone can mislead when baseline risks differ
5. The pre-specified SAP is the contract — any deviation from it must be documented and the analysis labeled as post-hoc
6. Bayesian analyses require prior specification transparency — assess sensitivity to prior choice
7. For non-inferiority trials, a finding of non-inferiority does not imply equivalence or superiority — state the conclusion precisely
8. Forest plots for subgroup analyses must include the interaction p-value, not just within-subgroup p-values
9. Mark any statistical interpretation that requires clinical-domain judgment with [VERIFY] for clinical-team review
10. This skill produces statistical interpretation frameworks — final clinical and regulatory conclusions require integrated review by biostatistician, clinician, and regulatory strategist
