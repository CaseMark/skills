---
name: policy-manual
description: Generates structured policy manual summaries that distill complex legal policies, regulatory compliance guidelines, and organizational procedures into accessible employee-facing reference documents. Organizes content by functional area with purpose, requirements, procedures, citations, consequences, and practical examples. Use when creating compliance manuals, employee policy guides, regulatory summaries, onboarding compliance materials, or organizational procedure handbooks.
tags:
  - regulatory
  - summarization
  - summary
---

# Policy Manual Summary

Distills complex legal policies, procedures, and regulatory compliance guidelines into a structured, plain-language policy manual for organizational use.

## Prerequisites

1. **Source materials** — existing policies, regulatory frameworks, industry standards, organizational guidelines
2. **Organizational context** — industry, jurisdiction(s), departmental structure
3. **Audience specification** — employee level (all-hands, management, department-specific)
4. **Scope definition** — which functional areas or regulatory domains to cover

## Output Structure

### Document Framework

| Section | Contents |
|---|---|
| **Cover & Revision History** | Title, effective date, version, last review date, next scheduled review |
| **Table of Contents** | Auto-generated section navigation |
| **Executive Summary** | Critical policies in 1–2 pages; highest-priority obligations |
| **Policy Sections** | Organized by functional area (see below) |
| **Glossary** | Defined terms on first use, consolidated here |
| **Appendices** | Forms, flowcharts, contact directories |

### Per-Policy Section Template

```
## [Policy Area]: [Policy Name]

**Effective Date:** [Date] | **Applies To:** [Roles/Departments] | **Owner:** [Department]

### Purpose & Scope
[1–2 sentences: why this policy exists, who it covers]

### Key Requirements
- [ ] Requirement 1
- [ ] Requirement 2

### Procedures
1. Step-by-step procedural guidance
2. Decision points noted with criteria

### Legal Authority
- [Statute/regulation citation] — [brief description]
- [Industry standard reference]

### Non-Compliance Consequences
- [Disciplinary, civil, criminal, or regulatory consequences]

### Examples & Scenarios
- **Scenario:** [Practical situation] → **Required Action:** [What to do]

### Questions & Escalation
- Contact: [Role/department] at [contact info]
```

### Cross-Cutting Compliance Themes

Address each if present in source materials:

| Theme | Key Elements |
|---|---|
| Data privacy & security | Collection limits, retention, breach notification, access controls |
| Anti-discrimination & harassment | Protected classes, reporting channels, investigation process |
| Ethics & conflicts of interest | Disclosure obligations, gift policies, outside activities |
| Health & safety | OSHA/jurisdiction-specific requirements, reporting, PPE |
| Financial controls & reporting | Authorization levels, segregation of duties, audit trails |

## Guidelines

- **Plain language first** — write for non-lawyers; define technical terms at first use
- **Preserve legal precision** — accessible does not mean imprecise; maintain accuracy of obligations and standards
- **Jurisdiction-specific distinctions** — clearly flag where requirements vary by state, locality, or operating jurisdiction
- **Citation currency** — verify all regulatory citations are current; flag uncertain citations with `[VERIFY]`
- **Multi-jurisdiction operations** — use a base federal/national standard, then note state/local variations in callout boxes
- **Privilege protection** — do not reproduce attorney work product or privileged legal analysis; summarize the compliance obligation only
- **Visual aids** — recommend flowcharts for multi-step processes or decision trees; note placement with `[FLOWCHART: description]`
- **Review cadence** — recommend annual review minimum; quarterly for rapidly evolving regulatory areas
- **Version control** — include revision history table tracking date, author, and nature of each change
