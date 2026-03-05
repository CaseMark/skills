---
name: managing-compliance-audits
description: Structures coding compliance audit programs with sampling methodology and corrective action plans. Use when conducting compliance audits, designing audit samples, or implementing corrective actions.
tags:
  - management
  - medical-coding-and-billing
  - compliance
  - audit
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Compliance Audits

Structures coding compliance audit programs with statistically valid sampling methodology, risk-based audit targeting, finding classification, corrective action plan development, and ongoing monitoring. Covers internal audit programs, external audit response (RAC, ZPIC, SMRC, MAC, OIG), and Seven Elements of an Effective Compliance Program implementation.

## Why This Skill Exists

The OIG requires healthcare organizations to have an effective compliance program, with internal auditing and monitoring as a core element. Medicare Recovery Audit Contractors (RACs) alone have recovered over $4 billion in improper payments. Organizations without proactive internal audit programs discover coding errors only when external auditors find them — at which point the errors are subject to extrapolation, interest, and potential penalties. A structured compliance audit program identifies and corrects errors before they become liabilities, demonstrates good-faith compliance effort, and can serve as a mitigating factor in enforcement actions. OIG Compliance Program Guidance identifies regular auditing as non-negotiable for an effective program.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What is the audit purpose? (routine internal, triggered by external event, risk-based targeted, baseline)
2. What service lines, providers, or code families are in scope?
3. What date-of-service range and claim population are included?
4. What sampling methodology will be used? (random, stratified, targeted)
5. What is the organization's risk profile based on prior audits and denial trends?
6. Is this audit in response to an external inquiry (RAC, ZPIC, MAC, OIG)?
7. Who will conduct the audit? (internal compliance team, external auditor, hybrid)

### Documents Required

- Compliance program policy and audit plan
- Prior audit findings and corrective action status
- OIG Work Plan items relevant to the organization's service mix
- Comparative billing reports (CBRs) and other CMS data
- Denial trend reports by CARC/RARC code
- Provider-specific coding profiles and outlier analysis
- Payer audit correspondence (if responding to external audit)
- Sampling frame data (total claims by code, provider, and date of service)

---

## Step 1 — Design the Audit Plan

Define scope, objectives, and methodology before any records are reviewed.

**Risk-based audit targeting:**
- Review the current OIG Work Plan for items relevant to your organization's service lines.
- Analyze denial trends — high-denial codes or providers indicate risk areas.
- Review comparative billing reports — providers billing significantly above specialty peers warrant scrutiny.
- Assess prior audit findings — areas with prior errors should be re-audited to verify corrective action effectiveness.
- Consider external audit activity — if RAC or ZPIC is reviewing a service area, proactive internal audit is prudent.

**Audit types:**
- **Baseline audit**: Establishes current error rates before implementing new processes or education. Should be conducted before any corrective action.
- **Routine monitoring audit**: Ongoing periodic audits (quarterly or semi-annually) to maintain compliance.
- **Targeted audit**: Focused on a specific code, provider, service line, or risk area identified through data analysis.
- **External response audit**: Conducted in response to an external audit request, prepayment review, or investigation. Requires legal counsel involvement.

## Step 2 — Establish Statistically Valid Sampling

Select the sample using defensible statistical methodology.

**Random sampling:**
- Define the universe (all claims meeting scope criteria).
- Calculate sample size based on desired confidence level and margin of error.
- For a 95% confidence level with ±5% margin of error, typical sample sizes: population <500 → 30 minimum; population 500–5,000 → 50–80; population >5,000 → 80–100.
- Use a random number generator to select specific claims from the universe.
- Document the sampling methodology, universe size, sample size, and selection method in audit work papers.

**Stratified sampling:**
- Divide the universe into strata (e.g., by CPT code range, provider, or service line).
- Sample proportionally from each stratum to ensure representation.
- Stratification improves accuracy when error rates vary across subgroups.

**Targeted (judgmental) sampling:**
- Select specific records based on risk indicators (e.g., all claims for a specific code, all claims from a flagged provider).
- Targeted samples are not statistically representative — findings cannot be extrapolated to the full population.
- Use targeted samples for focused investigations, not for calculating organizational error rates.

## Step 3 — Execute the Audit Review

Re-code each sampled encounter from source documentation.

- The auditor must independently review the complete medical record and assign codes as if coding from scratch.
- Compare the auditor's code assignment against the originally submitted codes.
- Classify each discrepancy using a standardized error taxonomy (see Auditing Coding Accuracy skill).
- Score each record: agree (no error), disagree-overcoded, disagree-undercoded, disagree-incorrect code, disagree-modifier error, disagree-documentation deficiency.
- Calculate error rates: (number of errors / total code assignments reviewed) × 100.
- Separate financial errors (affect reimbursement) from non-financial errors (e.g., sequencing issues that do not change payment).
- Document each finding with specific guideline references supporting the auditor's position.

## Step 4 — Analyze Findings and Calculate Impact

Aggregate individual findings into actionable compliance intelligence.

- Calculate overall error rate and error rates by type (overcoding, undercoding, modifier, bundling, documentation).
- Calculate net financial impact: (overcoding dollars − undercoding dollars) = net overpayment/underpayment.
- Identify root causes: Is the error pattern consistent across providers (systemic issue) or concentrated in specific providers (individual knowledge gap)?
- Determine if errors are random or systematic — systematic errors suggest process or training failures.
- Apply extrapolation to the full universe IF the sample was randomly selected: projected overpayment = (sample error rate × universe total).
- Note: Extrapolation should be used cautiously for internal purposes and only with statistically valid random samples.
- OIG considers a >5% error rate a significant compliance concern warranting immediate corrective action.

## Step 5 — Develop Corrective Action Plans

Create specific, measurable, time-bound corrective actions for each root cause.

**Corrective action elements:**
- **Finding**: Specific error identified with guideline reference.
- **Root cause**: Why the error occurred (e.g., coder did not apply NCCI edits, provider documentation lacked specificity, EMR template prompted incorrect code).
- **Corrective action**: Specific remedy (e.g., coder education on NCCI bundling rules, provider documentation training on E/M specificity, EMR template correction).
- **Responsible party**: Named individual accountable for implementing the action.
- **Deadline**: Date by which the action must be completed.
- **Re-audit date**: Date by which a follow-up audit will verify the corrective action's effectiveness.
- **Success metric**: Measurable outcome (e.g., error rate <3% on re-audit, modifier denial rate <2%).

**Refund/repayment obligations:**
- If the audit identifies systematic overcoding or overpayment, consult legal counsel regarding self-disclosure obligations.
- CMS Self-Referral Disclosure Protocol and OIG Self-Disclosure Protocol provide frameworks for voluntary disclosure.
- Refunds to Medicare must be made within 60 days of identifying an overpayment per Section 6402 of the ACA (60-Day Repayment Rule).
- Document the refund calculation, methodology, and supporting analysis.

## Step 6 — Implement Ongoing Monitoring

Transition from audit mode to continuous compliance monitoring.

- Schedule follow-up audits 90–120 days after corrective action implementation to verify effectiveness.
- Establish recurring audit schedules by service line (quarterly for high-risk, semi-annually for moderate-risk).
- Implement automated monitoring tools: claim scrubbers, NCCI edit software, E/M leveling analyzers.
- Track key compliance indicators monthly: error rate by provider, denial rate by code, modifier usage rates, charge patterns.
- Report audit findings and corrective action status to the compliance committee quarterly.
- Update the annual compliance audit work plan based on findings, risk changes, and new OIG Work Plan items.

---

## Checkpoint B — Review

- [ ] Audit plan documents scope, methodology, and risk-based targeting rationale
- [ ] Sampling methodology is statistically valid and documented in work papers
- [ ] Each finding references a specific coding guideline or CMS policy
- [ ] Error rates are calculated correctly (errors / total assignments, not errors / total records)
- [ ] Financial impact includes both overcoding (refund exposure) and undercoding (recovery opportunity)
- [ ] Root causes are identified for each error pattern — not just "coder error"
- [ ] Corrective action plans have responsible parties, deadlines, and re-audit dates
- [ ] Legal counsel has been consulted regarding self-disclosure if systematic overpayment is identified

---

## Quality Audit

- [ ] Audit methodology would withstand external scrutiny (OIG, RAC, or payer audit)
- [ ] Auditor qualifications are documented (CPC, CCS, RHIA, or equivalent credential)
- [ ] Inter-rater reliability is tested when multiple auditors are involved (>90% agreement target)
- [ ] Corrective action completion rates are tracked and reported
- [ ] Re-audit results demonstrate improvement from baseline audit findings
- [ ] Compliance committee receives regular reports on audit program status
- [ ] Self-disclosure obligations are evaluated for identified overpayments per the 60-Day Rule

---

## Guidelines

- Follow OIG Compliance Program Guidance for hospitals, physician practices, and applicable provider types
- Apply OIG Work Plan priorities for risk-based audit targeting
- Reference CMS Program Integrity Manual for external audit response requirements
- Follow AHIMA Practice Brief on Internal Audit Functions for audit program design
- Apply ACA Section 6402 (60-Day Repayment Rule) for identified overpayments
- Use the OIG Self-Disclosure Protocol and CMS Self-Referral Disclosure Protocol when appropriate
- Never destroy or alter audit work papers — they are discoverable in legal proceedings
- Mark with [VERIFY] any finding where the auditor's interpretation differs from the original coder's by a narrow margin
- Include disclaimer that compliance audit findings may create legal obligations and legal counsel should be consulted
