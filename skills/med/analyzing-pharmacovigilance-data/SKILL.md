---
name: analyzing-pharmacovigilance-data
language: en
description: Structures post-marketing safety surveillance with signal detection and PSUR reporting. Use when analyzing safety signals, preparing PSURs, or managing pharmacovigilance data.
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
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing Pharmacovigilance Data

## Why This Skill Exists

Pharmacovigilance (PV) is the science of detecting, assessing, understanding, and preventing adverse drug reactions after a product reaches the market. Unlike clinical trials with controlled conditions and selected populations, post-marketing surveillance covers millions of diverse patients, making signal detection both critically important and methodologically challenging. Regulatory obligations under 21 CFR 314.80/314.81 (NDA), 21 CFR 600.80 (BLA), EU pharmacovigilance legislation (Regulation 1235/2010, Directive 2010/84/EU), and ICH E2E define the framework. This skill provides the workflow for safety-signal detection, evaluation, PSUR/PBRER preparation, and risk-management planning.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What is the marketed product (trade name, INN, formulation, indication)?
2. What is the data source (spontaneous reports, EHR data, claims databases, registries, published literature)?
3. What safety database holds the ICSR data (Argus, AriSGlobal, other)?
4. What is the current MedDRA version for coding?
5. Is this a routine signal-detection cycle, ad-hoc signal evaluation, or aggregate report (PSUR/PBRER/DSUR)?
6. What is the data-lock point (DLP) for the reporting period?
7. Are there active Risk Evaluation and Mitigation Strategies (REMS) or Risk Management Plans (RMP)?
8. What disproportionality methods are currently in use (PRR, ROR, MGPS, BCPNN)?
9. Are there known safety signals under evaluation?
10. What is the target regulatory authority and reporting deadline?

### Required Source Documents
- Safety database case listings (ICSRs) for the reporting period
- Reference Safety Information (RSI) — current product labeling (USPI, SmPC)
- Previous PSURs/PBRERs and signal evaluation reports
- Published literature search results for the reporting period
- Clinical trial safety data (if post-marketing trials ongoing)
- Risk Management Plan (EU) or REMS (US) current version
- Regulatory correspondence regarding safety issues

---

## Step 1 — Process Individual Case Safety Reports (ICSRs)

Ensure data quality before signal detection:

1. **Case intake**: Minimum four elements for a valid ICSR per ICH E2D: identifiable reporter, identifiable patient, suspected medicinal product, suspected adverse reaction
2. **MedDRA coding**: Code verbatim reporter terms to MedDRA Preferred Terms (PTs) and map to System Organ Classes (SOCs); apply MedDRA Standardised MedDRA Queries (SMQs) for grouped analyses
3. **Causality assessment**: Apply the WHO-UMC system or company-defined algorithm to each case; document the rationale
4. **Seriousness assessment**: Classify per ICH E2D criteria (death, life-threatening, hospitalization, disability, congenital anomaly, important medical event)
5. **Expectedness/listedness**: Compare the reported reaction against the RSI (USPI for FDA, SmPC for EMA) — unlisted reactions flag potential new signals
6. **Duplicate detection**: Run duplicate-detection algorithms (matching patient demographics, event dates, reporter identity) before case enters analysis datasets
7. **Data quality review**: Check for completeness (age, sex, indication, dose, time-to-onset, outcome, concomitant medications); query reporters for missing critical information

---

## Step 2 — Conduct Quantitative Signal Detection

Apply disproportionality analysis to the safety database:

### Frequentist Methods
- **Proportional Reporting Ratio (PRR)**: Signal if PRR ≥ 2 AND chi-squared ≥ 4 AND N ≥ 3 (Evans criteria)
- **Reporting Odds Ratio (ROR)**: Analogous to PRR but uses odds ratio; lower 95% CI > 1 flags a signal

### Bayesian Methods
- **Multi-item Gamma Poisson Shrinker (MGPS/EBGM)**: FDA's preferred method for FAERS data; EB05 (lower 95% CI of EBGM) > 2 flags a signal
- **Bayesian Confidence Propagation Neural Network (BCPNN/IC)**: WHO-UMC's method for VigiBase; IC025 > 0 flags a signal

### Signal Thresholds
- No single statistical threshold defines a signal — disproportionality methods are screening tools, not confirmatory tests
- Apply clinical review to all statistical signals before classification
- Document the method, database version, data-lock point, and signal-detection parameters

### Routine Signal-Detection Cycle
- Conduct at defined intervals (monthly, quarterly, or per regulatory requirement)
- Compare current-period signals against prior-period results to identify new, strengthened, or resolved signals
- Maintain a signal-tracking log with status (new, under evaluation, confirmed, refuted, closed)

---

## Step 3 — Evaluate Identified Signals

For each detected signal, conduct a structured evaluation:

1. **Case-series review**: Retrieve all cases coded to the signal PT or SMQ; review for clinical pattern (time-to-onset distribution, dose relationship, dechallenge/rechallenge, concomitant medications, alternative causes)
2. **Biological plausibility**: Assess known pharmacology, mechanism of action, preclinical findings, and class effects
3. **Literature review**: Search for published case reports, case series, epidemiologic studies, or mechanistic data supporting the association
4. **Epidemiologic data**: If available, review comparative safety data from observational databases (CPRD, Sentinel, OMOP-CDM networks)
5. **Clinical trial review**: Re-examine safety data from clinical trials for the signal event (may have been overlooked or underpowered)
6. **Regulatory intelligence**: Check if other products in the same class have similar signals or labeling changes

### Signal Assessment Outcome
- **Confirmed signal (validated safety concern)**: Requires risk-benefit reassessment and potential regulatory action
- **Refuted signal**: Evidence does not support a causal association; document rationale and close
- **Ongoing evaluation**: Insufficient data; continue monitoring and specify next evaluation date

---

## Step 4 — Prepare the PSUR/PBRER

For Periodic Benefit-Risk Evaluation Reports (PBRERs) per ICH E2C(R2) or PSURs:

### PBRER Sections
1. **Introduction**: Product identification, reporting period, DLP
2. **Worldwide marketing authorization status**: Approved indications, formulations, markets
3. **Actions taken for safety reasons**: Labeling changes, regulatory actions, withdrawals
4. **Changes to RSI**: New AEs added, frequency changes, new warnings
5. **Estimated exposure**: Patient-years of exposure (sales data, prescription data, defined daily doses)
6. **Presentation of data**: Cumulative and interval case counts by SOC/PT; serious/non-serious; fatal outcomes
7. **Signal and risk evaluation**: New signals detected; evaluation of ongoing signals; completed signal evaluations
8. **Benefit evaluation**: Efficacy data from new studies, registries, or real-world evidence
9. **Integrated benefit-risk analysis**: Structured assessment of benefits vs. risks; comparison with alternatives
10. **Conclusions and actions**: Summary of safety profile; proposed regulatory actions

### DSUR (for investigational products)
- Follow ICH E2F structure: annual report from IND anniversary date
- Focus on ongoing clinical-trial safety data with reference safety information comparison
- Different from PBRER — covers development phase, not post-marketing

---

## Step 5 — Update Risk Management

Based on signal evaluation and aggregate review, update risk-management instruments:

### Risk Management Plan (RMP — EU)
- Update safety specification (identified risks, potential risks, missing information)
- Revise pharmacovigilance plan (routine and additional PV activities)
- Update risk-minimization measures (routine and additional)
- Submit RMP update with next regulatory procedure or within 6 months of significant new safety information

### REMS (US)
- Assess whether REMS modifications are needed based on new safety data
- Update medication guide, communication plan, or ETASU (Elements to Assure Safe Use) as warranted
- Submit REMS modification supplement if required

### Labeling Updates
- Propose labeling changes (new warnings, precautions, adverse reactions, contraindications) based on confirmed signals
- For FDA: CBE-0 supplement (safety labeling changes not requiring prior approval), CBE supplement, or PAS
- For EMA: Type II variation for significant labeling changes

---

## Checkpoint B — Pharmacovigilance Review

1. [ ] ICSR data quality meets ICH E2D minimum requirements (four valid elements)
2. [ ] MedDRA coding is consistent and uses the current dictionary version
3. [ ] Disproportionality analysis is conducted with documented methodology and thresholds
4. [ ] All detected signals have a documented evaluation with outcome classification
5. [ ] PBRER/PSUR covers the complete reporting period with accurate exposure estimates
6. [ ] Benefit-risk analysis is structured and balanced
7. [ ] Risk-management instruments (RMP/REMS) are current
8. [ ] Labeling accurately reflects the known safety profile
9. [ ] Regulatory reporting timelines are met (15-day expedited, periodic reports)
10. [ ] Signal-tracking log is current with all open signals under active evaluation

---

## Quality Audit

- [ ] Safety database is reconciled (no unprocessed cases at DLP)
- [ ] Duplicate cases have been identified and merged
- [ ] Causality assessment is documented for every serious case
- [ ] SMQ application is consistent across reporting periods
- [ ] Exposure denominators are calculated using the best available method with documented limitations
- [ ] Literature search strategy is documented and reproducible
- [ ] PBRER submission meets the EURD list schedule (EU) and NDA/BLA periodic-report schedule (FDA)
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. Disproportionality signals are hypotheses, not proof of causation — clinical evaluation is always required
2. Absence of a disproportionality signal does not mean absence of risk — spontaneous reporting is subject to underreporting (estimated 1-10% of actual AEs)
3. Never dismiss a signal based solely on low case counts — rare but serious events (liver failure, anaphylaxis, PML) may have very small numbers
4. The PBRER is a benefit-risk document, not just a safety summary — benefit evidence must be presented alongside risks
5. MedDRA coding decisions can materially affect signal detection — standardize coding practices and document any coding conventions
6. For combination products, assess component-specific and combination-specific safety profiles
7. Real-world evidence from observational databases complements spontaneous reporting but has its own biases (confounding, channeling, protopathic bias)
8. Maintain a clear audit trail for all signal-detection runs, evaluation decisions, and regulatory actions
9. Mark any signal evaluation with uncertain causality with [VERIFY] for qualified PV physician review
10. This skill produces PV analysis frameworks and reports — final safety conclusions and regulatory actions require Qualified Person for Pharmacovigilance (QPPV) or equivalent sign-off
