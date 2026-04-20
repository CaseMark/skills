---
name: managing-model-risk
language: en
description: Structures model validation with independent testing, limitation documentation, and ongoing monitoring. Use when validating risk models, documenting model limitations, or managing model governance.
tags:
  - management
  - risk-management
  - risk
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
# Managing Model Risk

Structures model validation with independent testing, limitation documentation, and ongoing monitoring for quantitative risk models used in pricing, credit decisioning, market risk measurement, and capital adequacy.

## When To Use

- Performing or coordinating independent model validation (initial or periodic)
- Documenting model limitations, assumptions, and compensating controls
- Building or updating a model risk inventory / model registry
- Preparing for regulatory examination of model governance (OCC SR 11-7, Fed SR 15-18, ECB TRIM) [VERIFY jurisdiction-specific guidance]
- Assessing materiality tier assignments for new or modified models
- Reviewing model performance monitoring results and back-testing exceptions

## Inputs To Gather

- **Model documentation package**: methodology paper, mathematical specification, implementation notes, change log
- **Validation scope memo**: model name/ID, tier classification, intended use, prior validation findings
- **Performance data**: back-testing results, benchmarking outputs, sensitivity analyses, P&L attribution reports
- **Data lineage**: source systems, transformations, proxy usage, missing-data treatments
- **Governance artifacts**: model owner sign-off, approval committee minutes, prior MRA/MRIA items
- **Regulatory context**: applicable supervisory guidance and any outstanding findings from exams [VERIFY against current regulatory expectations]

## Workflow

1. **Classify the model and confirm tier**
   - Map the model to the firm's tiering framework (e.g., Tier 1 = material/critical, Tier 2 = significant, Tier 3 = limited impact)
   - Confirm the model's intended use, downstream consumers, and materiality to financial statements or capital ratios
   - Verify that model registration in the central inventory is current

2. **Evaluate conceptual soundness**
   - Review theoretical basis, mathematical derivation, and key assumptions
   - Assess whether the chosen methodology is appropriate for the portfolio/risk type
   - Identify known limitations of the approach (e.g., distributional assumptions, stationarity requirements, calibration window sensitivity)

3. **Perform independent testing**
   - Replicate key calculations or run parallel implementations where feasible
   - Execute back-testing against realized outcomes (e.g., VaR exceptions, PD/LGD accuracy ratios, stress-test hit rates)
   - Run sensitivity and stress analyses on critical inputs and parameters
   - Benchmark against challenger models or industry proxies

4. **Assess data quality and lineage**
   - Trace input data from source systems through transformations to model consumption
   - Flag any proxy variables, manual overrides, or gap-filling techniques
   - Evaluate the representativeness of calibration and validation data sets relative to the current portfolio

5. **Document findings and limitations**
   - Categorize findings by severity: MRA (Matter Requiring Attention), MRIA (Matter Requiring Immediate Attention), or observation
   - For each limitation, specify the condition under which it becomes material and any compensating controls in place
   - Draft a clear limitations section that model users can reference when interpreting outputs

6. **Establish ongoing monitoring framework**
   - Define KPIs and thresholds for model performance (e.g., back-test exception counts, stability indices, discriminatory power metrics)
   - Set monitoring frequency aligned with model tier (Tier 1: monthly/quarterly; Tier 2: quarterly/semi-annual; Tier 3: annual) [VERIFY against firm policy]
   - Specify escalation triggers: what level of deterioration requires ad-hoc re-validation vs. parameter recalibration vs. model replacement

7. **Report and obtain governance approval**
   - Present validation report to the model risk committee or equivalent governance body
   - Track open findings in the MRA/MRIA tracker with owners and remediation deadlines
   - Confirm that model approval status is updated in the inventory (approved / approved with conditions / rejected)

## Output

The deliverable is a **Model Validation Report** containing:

- Executive summary with overall validation opinion (satisfactory / satisfactory with conditions / unsatisfactory)
- Tier classification and scope of review
- Conceptual soundness assessment
- Independent testing results with statistical evidence (tables, charts)
- Data quality evaluation
- Findings table: finding ID, severity, description, compensating control, remediation owner, target date
- Limitations inventory with materiality conditions
- Ongoing monitoring plan with KPIs, thresholds, and escalation paths
- Appendices: replication code references, data samples, benchmarking details

## Quality Checks

- Every finding has a clear severity rating, an assigned owner, and a remediation deadline
- Limitations are expressed in terms of the conditions under which the model may underperform — not just abstract caveats
- Back-testing uses an adequate observation window (minimum 1 year for market risk; 5+ years for credit risk where available) [VERIFY against internal policy and regulatory minimums]
- The report distinguishes between model risk inherent in the methodology vs. implementation risk (coding, data feeds)
- Ongoing monitoring thresholds are calibrated to historical performance distributions, not arbitrary round numbers
- All regulatory references cite the correct guidance version and effective date [VERIFY current versions of OCC 2011-12, SR 11-7, and any local equivalents]
- The validation opinion is consistent with the severity and count of open findings — no "satisfactory" rating with outstanding MRIAs
