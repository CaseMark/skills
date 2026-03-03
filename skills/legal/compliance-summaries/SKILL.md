---
name: compliance-summaries
description: >-
  Generates structured compliance summaries assessing regulatory posture, identifying
  gaps, and producing prioritized remediation roadmaps across finance (SEC, FINRA),
  healthcare (HIPAA, FDA), environmental (EPA), and data privacy (GDPR, CCPA) sectors.
  Use when drafting regulatory compliance reports, audit readiness assessments, or
  governance documents for executives, boards, or regulators.
---

# Compliance Summary

Produces a governance-ready compliance summary with gap analysis and prioritized remediation roadmap. Outputs target dual audiences: board-level oversight and operational compliance teams.

## Prerequisites

Before drafting, confirm:

1. **Sector and jurisdiction** — finance, healthcare, environmental, data privacy, or other; federal, state, or international scope
2. **Source documents** — compliance policies, internal audits, regulatory correspondence, incident reports, consent orders, prior summaries
3. **Scope** — full enterprise, specific business unit, or defined regulatory domain

## Output Structure

### 1. Executive Summary

| Field | Content |
|---|---|
| Overall Posture | Compliant / Substantially Compliant / Non-Compliant / Under Active Regulatory Scrutiny |
| Top 3 Risks | Ranked by severity and regulatory exposure |
| Immediate Action Items | Items requiring executive or board attention now |
| Review Period | Date range covered |

Write accessibly for non-lawyers. Detailed sections may use technical regulatory terminology.

### 2. Regulatory Requirements Matrix

For each applicable requirement, organize by regulatory domain (e.g., SEC/FINRA, HIPAA/FDA, EPA, CCPA/GDPR) or by business unit:

| Requirement | Citation | Obligation | Responsible Party | Deadline/Frequency | Penalty Exposure |
|---|---|---|---|---|---|

### 3. Compliance Status Assessment

For each requirement in the matrix:

- **Status**: Compliant | Gap Identified | Deficiency | Unknown/Insufficient Evidence
- **Supporting Evidence**: policies, training records, audit results, certifications, filings
- **Gap Description**: specific deficiency with factual basis
- **Remediation**: action steps, owner, target date, resource estimate

### 4. Compliance Infrastructure Assessment

Evaluate whether the organization has:

- Designated compliance officer(s) with appropriate authority
- Board-approved compliance program and policies
- Regular risk assessments with defined frequency
- Employee training program with completion tracking
- Monitoring and auditing cadence
- Incident response and breach notification procedures
- Escalation path to senior management and board
- Regulatory examination readiness protocols

### 5. Temporal Compliance Calendar

Track upcoming deadlines in a table covering: license/cert renewals, pending audits/exams, and upcoming regulatory changes requiring program modification. Include item, type, deadline, owner, and status.

### 6. Prioritized Action Plan

Rank remediation by: (1) regulatory deadline, (2) risk severity, (3) resource availability, (4) workstream dependencies.

| Priority | Action | Owner | Target Date | Success Metric |
|---|---|---|---|---|

## Checks

- **Cite precisely** — include CFR sections, statute numbers, and agency guidance identifiers; flag uncertain citations with `[VERIFY]`
- **Distinguish evidence quality** — separate documented compliance from self-reported or assumed compliance
- **Flag gray areas** — note regulatory interpretive uncertainty; recommend regulator engagement or outside counsel review where applicable
- **Emerging regulations** — flag anticipated regulatory changes requiring future program modification
- **No legal advice** — frame as compliance assessment; note where legal counsel review is required before reliance

---

Key changes from the original:

- **Description**: Trimmed from ~90 words to ~50 while preserving trigger keywords and regulatory domains. Removed `tags` (not part of the spec's required frontmatter).
- **Dual-audience note**: Moved from buried guideline to inline context in the Executive Summary section where it's actionable.
- **Template placeholders removed**: Stripped `[Reg name]`, `[Cite]`, empty numbered rows — Claude knows how to fill tables.
- **Horizontal rules removed**: Unnecessary visual separators between subsections.
- **Infrastructure checklist**: Converted from checkbox format to prose list (checkboxes are for workflow tracking, not output templates).
- **Temporal Calendar**: Collapsed from a full template table into a one-line instruction — Claude can generate the table from the description.
- **Guidelines → Checks**: Renamed to match the concise pattern; removed the "dual-audience" bullet (relocated above) and "emerging trends" was tightened to "emerging regulations."
- **Line count**: Reduced from 112 to ~68 lines (~40% reduction) while preserving all domain-specific regulatory content.
