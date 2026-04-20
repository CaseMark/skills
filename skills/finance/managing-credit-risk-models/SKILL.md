---
name: managing-credit-risk-models
language: en
description: Evaluates and monitors credit risk models (PD, LGD, EAD) with calibration and discrimination metrics. Use when validating credit models, assessing model performance, or calibrating default models.
tags:
  - management
  - risk-management
  - risk
  - credit
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Credit Risk Models

## When To Use

- Periodic validation of Probability of Default (PD), Loss Given Default (LGD), or Exposure at Default (EAD) models
- Annual or triggered model performance reviews required by internal model governance or regulatory mandate (e.g., SR 11-7, CRD/CRR, IFRS 9 ECL frameworks) [VERIFY jurisdiction-specific regulatory requirements]
- Recalibration following material portfolio shifts, macroeconomic regime changes, or post-merger data integration
- Comparing challenger models against incumbent production models before promotion
- Preparing model risk management reports for MRC/board-level review

## Inputs To Gather

- **Development sample and out-of-time/out-of-sample validation data** — confirm vintage coverage, default definition consistency, and exclusion criteria
- **Model documentation** — original methodology paper, variable selection rationale, and any prior validation findings
- **Current production scorecards or parameter estimates** — PD term structures, LGD cure/workout assumptions, EAD CCF tables
- **Realized outcome data** — observed default flags, recovery cashflows, drawn/undrawn balances at default
- **Portfolio segmentation** — rating grades, facility types, collateral categories, geographic or industry cuts
- **Regulatory and policy thresholds** — minimum discrimination (e.g., Gini > 0.40), calibration tolerance bands, override rate caps [VERIFY institution-specific thresholds]

## Workflow

1. **Scope the validation exercise**
   - Identify which model components are in scope (PD only, full PD/LGD/EAD suite, segment-level vs. portfolio-level)
   - Confirm the observation window and default/loss outcome definitions match the model's design assumptions
   - Document any data limitations or exclusions upfront

2. **Assess discrimination performance**
   - Compute Gini coefficient (Accuracy Ratio), AUC-ROC, and Kolmogorov-Smirnov statistic on the validation sample
   - Generate CAP (Cumulative Accuracy Profile) and ROC curves
   - Segment discrimination by key risk drivers (vintage, industry, geography) to detect pockets of weakness
   - Compare current-period metrics against development-sample benchmarks and prior validation results

3. **Evaluate calibration accuracy**
   - Run Binomial test, Hosmer-Lemeshow test, or traffic-light approach (Basel) across PD buckets
   - For LGD: compare predicted vs. realized loss severity by collateral type and workout path
   - For EAD: compare predicted CCFs against observed utilization at default
   - Assess calibration across economic cycles — flag if model was calibrated to benign conditions and current environment is stressed [VERIFY whether TTC vs. PIT calibration applies]

4. **Evaluate stability and concentration**
   - Population Stability Index (PSI) on score distributions between development and recent periods
   - Characteristic Stability Index (CSI) on key input variables
   - Herfindahl index or grade-concentration analysis to detect rating migration clustering
   - Flag PSI > 0.25 or CSI > 0.25 as material shifts requiring deeper investigation [VERIFY institution-specific PSI thresholds]

5. **Stress-test and sensitivity analysis**
   - Perturb key macro drivers (GDP, unemployment, HPI) and assess PD/LGD migration under stressed scenarios
   - Identify variables with outsized sensitivity — single-variable stress contributions exceeding a defined threshold
   - Cross-check stressed outputs against institution's CCAR/DFAST or ICAAP submissions if applicable [VERIFY regulatory stress testing framework]

6. **Document findings and recommend actions**
   - Classify findings by severity: Tier 1 (material, requires remediation before next use), Tier 2 (significant, remediation within defined timeline), Tier 3 (minor, monitor)
   - Provide specific recalibration or redevelopment recommendations with target timelines
   - Draft executive summary for Model Risk Committee or board reporting

## Output

- **Model Validation Report** containing:
  - Executive summary with overall model rating (e.g., Satisfactory / Needs Improvement / Unsatisfactory)
  - Discrimination metrics table (Gini, AUC, KS) with trend comparison across validation periods
  - Calibration test results by grade, segment, and time horizon
  - Stability analysis with PSI/CSI tables and heatmaps
  - Findings register with severity tier, description, and remediation action/owner/deadline
  - Appendices: data quality notes, exclusion log, detailed statistical output

## Quality Checks

- Confirm default and loss definitions used in validation match the model's training definitions exactly — misalignment here invalidates all downstream metrics
- Verify that validation data has no lookahead bias (outcomes must post-date the score assignment)
- Cross-check sample sizes per rating grade — bins with fewer than 30 defaults produce unreliable calibration test results
- Ensure discrimination and calibration metrics are computed on the same population; filtered vs. unfiltered samples can yield contradictory conclusions
- Validate that any override or judgmental adjustment rates are reported separately and not mixed into statistical performance metrics
- Confirm findings are mapped to specific model components — avoid blanket "model is weak" conclusions without identifying which parameter (PD, LGD, or EAD) and which segment drives the issue
