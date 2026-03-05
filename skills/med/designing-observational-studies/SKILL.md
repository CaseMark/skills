---
name: designing-observational-studies
description: Structures observational study designs (cohort, case-control, cross-sectional) with bias mitigation strategies. Use when designing observational research, mitigating bias, or planning epidemiologic studies.
tags:
  - design
  - clinical-research
  - research
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Biostatistics
    - Regulatory Affairs
  document_types:
    - Design Document
  skill_modes:
    - Design
---

# Designing Observational Studies

## Why This Skill Exists

Observational studies provide essential evidence when randomized trials are infeasible, unethical, or insufficient — particularly for rare adverse events, long-term outcomes, and real-world effectiveness. However, observational designs are inherently susceptible to confounding, selection bias, and information bias in ways that RCTs are not. Poorly designed observational studies produce misleading results that can harm patients and distort policy. This skill implements the STROBE (Strengthening the Reporting of Observational Studies in Epidemiology) framework, FDA guidance on real-world evidence, and ICH E17/E8(R1) principles to produce rigorous observational study protocols that meet regulatory and publication standards.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What is the research question (exposure, outcome, population, timeframe)?
2. What is the intended use (regulatory post-marketing requirement, label expansion, HTA, publication)?
3. Which study design is most appropriate (cohort, case-control, nested case-control, case-crossover, cross-sectional, self-controlled case series)?
4. What data sources are available (claims databases, EHR systems, registries, linked datasets)?
5. Is this a retrospective, prospective, or ambidirectional design?
6. What is the expected sample size and statistical power for the primary analysis?
7. Is this study registered (ENCePP, ClinicalTrials.gov, PROSPERO for systematic observational reviews)?
8. What confounders must be addressed, and are they measurable in the data source?
9. Are there specific regulatory requirements (FDA REMS, EMA PASS — Post-Authorization Safety Study)?
10. What is the target completion timeline?

### Required Source Documents
- Draft study protocol (following ENCePP/ISPE/FDA guidance structure)
- Data-source documentation (data dictionary, coding systems, coverage population, data-quality reports)
- Published literature on the exposure-outcome association (prior observational studies, RCTs)
- Target trial emulation framework (if applicable)
- Regulatory requirements (PASS protocol requirements, PMR/PMC letter)
- STROBE checklist (for reporting planning)

---

## Step 1 — Select Study Design

Choose the optimal design based on the research question, available data, and efficiency considerations:

### Cohort Study (prospective or retrospective)
- **Best for**: Incidence estimation, multiple outcomes from single exposure, exposure-response relationships
- **Structure**: Define exposed and unexposed cohorts; follow forward in time to outcome occurrence
- **Key measures**: Incidence rate, rate ratio, risk ratio, risk difference
- **Strengths**: Temporal sequence established; can estimate absolute risk
- **Limitations**: Inefficient for rare outcomes; loss to follow-up bias

### Case-Control Study
- **Best for**: Rare outcomes, multiple exposures for single outcome
- **Structure**: Identify cases (outcome+) and controls (outcome−); look backward at exposure history
- **Key measures**: Odds ratio (approximates rate ratio when rare-disease assumption holds or when density-sampled controls are used)
- **Control selection**: Population-based controls preferred; match or adjust for key confounders; sampling strategies (incidence-density sampling, case-cohort, nested case-control)
- **Limitations**: Susceptible to recall bias (self-reported exposures); cannot estimate incidence

### Cross-Sectional Study
- **Best for**: Prevalence estimation, hypothesis generation, resource-utilization assessment
- **Structure**: Measure exposure and outcome at the same time point
- **Key measures**: Prevalence, prevalence ratio, prevalence odds ratio
- **Limitations**: Cannot establish temporal sequence; survivor bias

### Self-Controlled Designs
- **Case-crossover**: For transient exposures and acute outcomes; each patient is their own control
- **Self-controlled case series (SCCS)**: For outcomes following time-varying exposures (e.g., vaccine safety); controls for all fixed confounders

### Target Trial Emulation
- For comparative effectiveness using observational data, explicitly specify the target trial that the observational study is attempting to emulate
- Define: eligibility criteria, treatment strategies, randomization analog (assignment at time zero), outcomes, causal contrast, analysis plan
- This framework prevents many common observational study design errors (immortal time bias, prevalent-user bias)

---

## Step 2 — Define the Study Population and Exposure

Specify precise, operationalizable definitions:

### Cohort Entry (Time Zero)
- Define the index date: first prescription, diagnosis date, procedure date
- Apply the new-user (incident-user) design to avoid prevalent-user bias — exclude patients with prior use during a defined lookback period
- Define the washout period (typically 6-12 months of continuous enrollment with no exposure)

### Eligibility Criteria
- Minimum continuous enrollment period (pre-index lookback for baseline assessment)
- Age restrictions, specific disease requirements, exclusion of contraindicated populations
- Operationalize each criterion using the specific codes available in the data source (ICD-10, CPT, NDC, READ, SNOMED)

### Exposure Definition
- Specify the exposure precisely: drug name, dose range, route, ATC code, NDC code
- Define exposure windows: current use, recent use, past use; grace period for prescription gaps
- For drug studies: define exposure duration, switching, augmentation, and discontinuation

---

## Step 3 — Define Outcomes and Covariates

### Outcome Assessment
- **Primary outcome**: Define using a validated algorithm when available (cite validation studies with PPV/sensitivity/specificity)
- **Outcome ascertainment window**: Define start (after index date) and end (study end, disenrollment, death, outcome occurrence)
- **Outcome validation**: For studies using claims/EHR data, plan chart review on a random sample to confirm algorithm PPV
- **Competing risks**: Identify and plan to address (death as competing risk for non-fatal outcomes)

### Covariate Assessment
- Measure all covariates in the pre-index (baseline) period only — never adjust for post-exposure variables
- **Demographics**: Age, sex, race/ethnicity (where available and appropriate)
- **Comorbidities**: Charlson/Elixhauser comorbidity indices, individual conditions relevant to the outcome
- **Comedications**: Medications that may confound or modify the exposure-outcome relationship
- **Healthcare utilization**: Number of physician visits, hospitalizations, ER visits (proxy for disease severity and health-seeking behavior)
- **Unmeasured confounding**: Identify confounders that cannot be measured in the data source; plan sensitivity analyses (E-value, probabilistic bias analysis)

---

## Step 4 — Develop the Analytic Strategy

### Primary Analysis
1. **Propensity-score methods** (for comparative cohort studies):
   - PS matching (1:1 nearest-neighbor, caliper = 0.2 × SD of logit PS)
   - PS stratification (quintiles or deciles)
   - Inverse probability of treatment weighting (IPTW) with stabilized weights
   - Assess covariate balance: standardized mean differences (SMD < 0.1 for adequate balance)
2. **Multivariable regression**: When PS methods are not feasible; include all pre-specified confounders
3. **Time-to-event analysis**: Cox proportional hazards for cohort studies; verify PH assumption
4. **Conditional logistic regression**: For matched case-control studies

### Sensitivity Analyses (pre-specified)
- Vary exposure definitions (broader/narrower)
- Vary outcome definitions (more/less specific algorithms)
- Restrict to subpopulations (e.g., new-users only, specific age groups)
- Apply different confounder-adjustment methods
- Quantitative bias analysis for unmeasured confounding (E-value, Ding & VanderWeele)
- Negative-control outcomes (outcomes not plausibly related to the exposure — to detect residual confounding)

---

## Step 5 — Address Key Biases

Systematically evaluate and mitigate the principal threats to validity:

| Bias Type | Mitigation Strategy |
|-----------|---------------------|
| Confounding | Propensity scores, multivariable adjustment, restriction, negative controls |
| Immortal time bias | Properly define time zero; use time-varying exposure; avoid conditioning on future events |
| Prevalent-user bias | New-user (incident-user) design with washout period |
| Protopathic bias | Lag exposure window (exclude events occurring immediately after exposure initiation) |
| Detection/surveillance bias | Adjust for healthcare utilization; use active-comparator design |
| Misclassification (exposure) | Validated coding algorithms; sensitivity analyses varying definitions |
| Misclassification (outcome) | Validated outcome algorithms with known PPV; chart-review validation substudy |
| Selection bias | Use active-comparator (head-to-head) design rather than non-user comparator; assess and report loss to follow-up |
| Channeling bias | Active-comparator design; restrict to common indication; PS adjustment including channeling variables |
| Time-related bias | Align exposure groups at time zero; avoid time-varying confounding through proper study design |

---

## Step 6 — Draft the Study Protocol

Structure the protocol per ENCePP/ISPE/FDA guidance:

1. Title, version, investigators, sponsor
2. Abstract/synopsis
3. Background and rationale
4. Research question and objectives
5. Study design and type
6. Data source(s) with description
7. Study population (eligibility criteria with operational definitions)
8. Exposure definition (with codes)
9. Outcome definition (with codes and validation information)
10. Covariates (with measurement approach)
11. Sample-size estimation and power
12. Statistical analysis plan (primary, secondary, sensitivity analyses)
13. Bias assessment and mitigation
14. Limitations
15. Quality control procedures
16. Data management and privacy
17. Timeline and milestones
18. References

---

## Checkpoint B — Design Review

1. [ ] Study design is appropriate for the research question
2. [ ] New-user design is applied (or deviation is justified)
3. [ ] Time zero is clearly defined and aligned across comparison groups
4. [ ] Exposure and outcome definitions use validated algorithms with cited PPV/sensitivity
5. [ ] All major confounders are identified and measurable in the data source
6. [ ] Propensity-score or multivariable adjustment strategy is pre-specified
7. [ ] Sensitivity analyses address unmeasured confounding, misclassification, and key design choices
8. [ ] STROBE checklist is completed for the protocol/reporting plan
9. [ ] Study is registered (ENCePP, ClinicalTrials.gov) before analysis begins
10. [ ] IRB/privacy-board review is obtained or waiver documented

---

## Quality Audit

- [ ] No post-exposure variables are included as confounders
- [ ] Immortal time is not introduced by study-design choices
- [ ] Active-comparator design is used where feasible (preferred over non-user comparator)
- [ ] Outcome validation data (PPV, sensitivity) are cited
- [ ] Negative-control analyses are included to assess residual confounding
- [ ] E-value or quantitative bias analysis is planned for primary result
- [ ] Sample-size calculation accounts for expected covariate adjustment
- [ ] Data-source limitations are explicitly acknowledged
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. Observational studies cannot prove causation — frame conclusions appropriately as associations unless the totality of evidence (Bradford Hill criteria) supports causal language
2. The new-user (incident-user) active-comparator design is the gold standard for comparative drug-safety studies
3. Never adjust for variables that are mediators (on the causal pathway) or colliders — use DAGs (directed acyclic graphs) to guide confounder selection
4. Report standardized mean differences for all covariates before and after PS adjustment — p-values for balance are inappropriate
5. For regulatory submissions (FDA Sentinel, EMA PASS), follow the specific agency's study-design requirements
6. Pre-register the study protocol and analysis plan before accessing outcome data — post-hoc analyses must be clearly labeled
7. Database studies require an understanding of data-generation processes (how codes are assigned, what missingness means, coding incentives)
8. Large sample sizes in observational studies produce narrow CIs but do not eliminate bias — precision is not accuracy
9. Escalate to epidemiologist when novel biases are suspected or when target-trial emulation involves complex treatment strategies
10. This skill produces study designs and protocols — final design decisions require epidemiologist, biostatistician, and clinical-domain expert review
