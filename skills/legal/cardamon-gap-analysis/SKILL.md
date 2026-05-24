---
name: gap-analysis
language: en
description: >-
  Compares an organization's existing compliance controls, policies, and
  procedures against extracted regulatory obligations to identify coverage
  gaps. Produces a remediation plan with prioritized actions. Use when
  assessing compliance maturity or preparing for regulatory audits.
tags:
  - regulatory
  - compliance
  - analysis
---

# Gap Analysis

Systematic comparison of existing compliance posture against regulatory
obligations to identify, prioritize, and remediate coverage gaps.

## Prerequisites

- Extracted obligation register (from obligation-mapping)
- Inventory of existing policies, procedures, controls
- Risk methodology framework (existing or standard industry framework)
- Prior gap analysis results (if iterative)

## Workflow

1. **Control inventory** — catalog all existing compliance artifacts:
   - Policies and procedures (with effective dates and owners)
   - Technical controls (system configurations, access controls)
   - Training programs and completion rates
   - Monitoring and reporting mechanisms
2. **Mapping** — align each control against its corresponding obligation(s):
   - Direct match: control explicitly addresses the obligation
   - Partial match: control addresses part but not all elements
   - Gap: no corresponding control identified
3. **Scoring** — for each mapping:
   - Coverage completeness (full/partial/none)
   - Recency (control updated within last 12 months?)
   - Evidence quality (documented, tested, audited)
4. **Remediation planning** — for each gap:
   - Classify remediation type (new control, modify existing, augment)
   - Estimate effort (person-weeks)
   - Assign priority based on obligation severity and closure timeline
   - Draft the remediation action with acceptance criteria
5. **Reporting** — produce gap analysis report with executive summary,
   detailed findings by obligation, and remediation roadmap

## Pitfalls

- A control that exists on paper but is not tested or enforced is functionally a gap — verify operational effectiveness
- Don't ignore implicit controls: informal practices and tribal knowledge matter, document them
- Gap analyses are snapshots — establish a periodic cadence, not one-off exercises
- Be careful with third-party controls: vendors may provide compliance evidence but it doesn't transfer liability
- Over-mapping is the inverse risk: claiming a control covers an obligation when it actually covers a different one
