---
name: managing-compliance-testing
language: en
description: Designs and executes compliance testing programs with sampling methodology and findings documentation. Use when conducting compliance testing, designing test procedures, or documenting testing results.
tags:
  - management
  - financial-compliance
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Regulatory Compliance
    - Financial Regulation
    - Compliance
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Compliance Testing

## When To Use

- Designing a new compliance testing program for a regulatory requirement (AML/BSA, consumer lending, privacy, sanctions screening, etc.)
- Building or refining test procedures and sampling plans for periodic compliance reviews
- Executing a compliance test cycle and documenting findings, exceptions, and remediation items
- Preparing compliance testing reports for management, audit committees, or regulators
- Responding to regulatory examination findings that require enhanced testing protocols

## Inputs To Gather

- **Regulatory scope**: Specific regulations, rules, or internal policies being tested (e.g., Reg E, TILA-RESPA, OFAC, GDPR, SOX controls) [VERIFY applicable jurisdiction and current rule versions]
- **Testing universe**: Total population of transactions, accounts, processes, or controls subject to testing, with date range
- **Risk assessment**: Prior risk ratings, examination findings, audit results, or known deficiency areas that inform scope weighting
- **Sampling parameters**: Confidence level, margin of error, acceptable exception rate; or prescribed sample sizes from regulatory guidance [VERIFY if regulator mandates specific sample sizes]
- **Control documentation**: Existing policies, procedures, process maps, and control matrices for the areas under test
- **Prior test results**: Previous testing cycle findings, remediation status, and trend data
- **Stakeholder requirements**: Reporting audience (compliance committee, board, regulator) and deliverable format expectations

## Workflow

1. **Define testing scope and objectives**
   - Map each regulatory requirement or policy provision to testable control assertions
   - Prioritize testing areas using a risk-based approach — weight toward higher-risk products, channels, or geographies
   - Document scope inclusions, exclusions, and rationale

2. **Design sampling methodology**
   - Determine sampling approach: statistical (random, stratified, systematic) vs. judgmental (targeted, risk-based)
   - For statistical sampling, calculate minimum sample size using population size, confidence level (typically 90-95%), and tolerable error rate (typically 2-10%) [VERIFY against any regulator-prescribed minimums]
   - For judgmental sampling, document selection criteria and basis for sample size
   - Define data extraction procedures and source system(s)

3. **Develop test procedures**
   - Write step-by-step test scripts for each control assertion, specifying: what to inspect, the pass/fail criteria, data fields to capture, and how to document exceptions
   - Include attribute testing (binary pass/fail) and substantive testing (accuracy/completeness checks) as appropriate
   - Build a test workpaper template with columns for: item ID, sample attributes, test result, exception description, root cause category, and evidence reference

4. **Execute testing**
   - Extract sample population and select items per the methodology
   - Perform each test step, recording results contemporaneously in workpapers
   - Classify exceptions by severity: critical (regulatory violation with consumer harm), significant (control failure without immediate harm), minor (procedural deviation, low risk)
   - Escalate critical findings immediately to the Chief Compliance Officer or designated authority — do not wait for report finalization

5. **Analyze results and identify root causes**
   - Calculate exception rates per control area and compare against tolerable thresholds
   - Determine whether exceptions are isolated or systemic (pattern analysis across business units, time periods, or personnel)
   - Assign root cause categories: training gap, system limitation, policy ambiguity, process breakdown, third-party failure, or intentional override
   - Assess whether sample results can be projected to the full population (for statistical samples) or are indicative only (for judgmental samples)

6. **Document findings and remediation**
   - Draft findings with: condition (what was found), criteria (what was required), cause (root cause), effect (actual or potential impact), and recommendation
   - Assign remediation owners, target completion dates, and validation procedures
   - Rate overall compliance health for each tested area: satisfactory, needs improvement, or unsatisfactory

7. **Report and track**
   - Compile the testing report with executive summary, methodology description, detailed findings, and trending data versus prior periods
   - Present to designated governance body (compliance committee, audit committee, or board)
   - Enter remediation items into a tracking system with milestone dates and evidence requirements for closure
   - Schedule validation testing to confirm remediation effectiveness before closing findings

## Output

The deliverable is a **Compliance Testing Report** containing:

- **Executive summary**: Scope, period, overall results, and key themes
- **Methodology section**: Sampling approach, population sizes, sample sizes, confidence parameters, and any limitations
- **Findings detail**: Each finding in condition/criteria/cause/effect/recommendation format, with severity rating
- **Exception rate summary table**: By regulation, control area, and business unit
- **Trend analysis**: Comparison to prior testing cycles with directional indicators
- **Remediation tracker**: Open items with owners, due dates, and status
- **Appendices**: Sample selection log, workpaper references, and data source descriptions

## Quality Checks

- Confirm sample sizes meet or exceed any regulatory or internal audit minimums [VERIFY]
- Verify that test procedures map back to specific regulatory provisions or policy sections — no orphan tests
- Ensure every exception has a documented root cause category and remediation recommendation
- Check that severity ratings are applied consistently using the defined classification criteria
- Validate that exception rate calculations use the correct denominators (items tested, not population size, unless projecting)
- Confirm the report distinguishes between statistical projections and judgmental observations
- Review for completeness: all scope areas appear in findings (even if no exceptions — document "satisfactory" results)
- Verify remediation timelines are realistic and aligned with regulatory expectations [VERIFY any regulator-imposed deadlines]
- Ensure workpapers are retained per the organization's document retention schedule [VERIFY retention period requirements]
