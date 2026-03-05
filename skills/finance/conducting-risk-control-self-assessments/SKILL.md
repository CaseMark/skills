---
name: conducting-risk-control-self-assessments
description: Designs and facilitates RCSA processes with risk identification, control evaluation, and action planning. Use when conducting RCSAs, evaluating internal controls, or identifying emerging risks.
tags:
  - process
  - risk-management
  - risk
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Risk Control Self Assessments

## When To Use

- Facilitating periodic (annual, semi-annual, quarterly) RCSA cycles for business units or functions
- Evaluating whether existing controls adequately mitigate identified risks after an organizational change, new product launch, or regulatory shift
- Onboarding a new business line or process into the enterprise risk framework
- Responding to audit findings, regulatory examination results, or incident post-mortems that require control reassessment
- Identifying emerging risks (e.g., market concentration, model risk, cyber exposure) not yet captured in the risk register

## Inputs To Gather

- **Risk taxonomy and universe**: Current enterprise risk taxonomy, including risk categories (credit, market, operational, compliance, strategic, reputational) and sub-categories
- **Existing risk register**: Prior RCSA results, residual risk ratings, and open action items
- **Control inventory**: Documented controls mapped to risks, including control type (preventive, detective, corrective), frequency, and owner
- **Loss event and incident data**: Internal loss history, near-miss reports, and external loss benchmarks relevant to the business unit
- **Key Risk Indicators (KRIs)**: Current KRI thresholds, breach history, and trend data
- **Organizational context**: Business unit org chart, process maps, materiality thresholds, and risk appetite statements [VERIFY: confirm risk appetite statement is current and board-approved]
- **Regulatory requirements**: Applicable regulatory expectations for RCSA (e.g., OCC Heightened Standards, Basel III operational risk, SOX 404) [VERIFY: jurisdiction-specific requirements]

## Workflow

1. **Define scope and methodology**
   - Confirm which business units, processes, or risk categories are in scope
   - Select assessment approach: top-down (risk-based) vs. bottom-up (process-based) vs. hybrid
   - Set the risk rating scale (e.g., 5×5 likelihood/impact matrix) and ensure it aligns with enterprise standards
   - Identify RCSA participants: process owners, control owners, first-line managers, second-line risk officers

2. **Conduct risk identification**
   - Facilitate workshops or structured interviews with process owners to identify risks per process step
   - Map each risk to the enterprise risk taxonomy category
   - Capture inherent risk ratings (likelihood × impact before controls) using the agreed scale
   - Flag risks not currently in the risk register as emerging or newly identified
   - Cross-reference against loss event data and external risk intelligence for completeness

3. **Evaluate controls**
   - For each identified risk, document the key controls that mitigate it
   - Assess control design effectiveness: Does the control address the root cause? Is it preventive or detective? Is frequency adequate?
   - Assess control operating effectiveness: Is the control consistently executed? What is the evidence (logs, sign-offs, reconciliations)?
   - Rate each control as Effective, Needs Improvement, or Ineffective
   - Calculate residual risk rating (inherent risk adjusted for control effectiveness)
   - Identify control gaps—risks with no mapped control or with ineffective controls

4. **Develop action plans**
   - For residual risks exceeding appetite, draft remediation actions with specific owners, target dates, and measurable milestones
   - Classify actions: accept (with documented rationale and approval authority), mitigate (new or enhanced control), transfer (insurance, hedging), or avoid (exit activity)
   - Link action items to KRIs so progress can be monitored between RCSA cycles
   - Escalate risks requiring risk acceptance above business-unit authority to the appropriate risk committee [VERIFY: escalation thresholds per risk appetite framework]

5. **Compile and report**
   - Produce the RCSA summary report: risk heat map, top residual risks, control gap analysis, and action plan tracker
   - Prepare executive dashboard for risk committee or board presentation
   - Update the enterprise risk register with new/changed risk entries and residual ratings
   - Archive supporting evidence (workshop notes, interview records, control testing samples)

## Output

- **RCSA risk register update**: Each risk with inherent rating, mapped controls, control effectiveness rating, residual rating, and risk owner
- **Control gap analysis**: Table of risks with absent, inadequate, or ineffective controls, ranked by residual risk severity
- **Risk heat map**: Visual 5×5 matrix plotting residual risks by likelihood and impact, color-coded to appetite thresholds
- **Action plan tracker**: Remediation items with owners, deadlines, status, and linked KRIs
- **Executive summary**: One-page narrative highlighting material risk movements, new/emerging risks, overdue actions, and escalation items

## Quality Checks

- Every risk in scope has at least one mapped control; any unmapped risk is explicitly flagged as a control gap
- Residual risk ratings are mathematically consistent with inherent ratings and control effectiveness scores
- No action plan is assigned without a named owner and a target completion date
- Risk ratings use the enterprise-standard scale—no ad hoc or inconsistent scales across business units
- Loss event data and KRI trends are reconciled against RCSA findings (material disconnects are investigated)
- [VERIFY] Regulatory-specific RCSA requirements are addressed (OCC Heightened Standards, COSO framework alignment, Basel operational risk standards as applicable)
- All risks rated above appetite have either a remediation plan or a documented risk acceptance approved at the required authority level
- Workshop participation is documented to demonstrate first-line ownership and accountability
