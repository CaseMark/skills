---
name: regulatory-submission-summary
description: Generates structured summaries of regulatory submissions (FDA NDAs, 510(k)s, environmental permits, rate filings) for government approval processes. Distills clinical data, manufacturing info, compliance evidence, and supporting documentation into standardized overviews for regulatory reviewers, compliance teams, and executives. Use when summarizing submission packages, preparing regulatory filing overviews, or creating executive briefings on approval applications.
tags:
  - regulatory
  - summarization
  - summary
---

# Regulatory Submission Summary

Produces a structured summary of a regulatory submission package, enabling reviewers to quickly assess purpose, scope, supporting evidence, and compliance posture.

## Prerequisites

1. **Primary submission documents** — application form, cover letter, filing type identification
2. **Supporting technical data** — clinical trials, safety/efficacy studies, engineering analyses, environmental assessments, economic analyses (as applicable)
3. **Manufacturing/operational documentation** — quality control, facility info, process descriptions
4. **Labeling or public-facing materials** — proposed labels, consumer disclosures, service descriptions
5. **Agency correspondence** — pre-submission meeting minutes, prior feedback, deficiency responses
6. **Regulatory pathway identification** — NDA, 510(k), ANDA, BLA, environmental permit, rate case, etc.

## Output Structure

### 1. Executive Overview

| Field | Content |
|-------|---------|
| Submitting Entity | Name, address, contact |
| Regulatory Body | FDA, EPA, FCC, state PUC, etc. |
| Submission Type | NDA, 510(k), BLA, ANDA, EIS, rate case, etc. |
| Submission Date | Date filed or to be filed |
| Requested Action | Approval, clearance, permit, authorization |
| Regulatory Framework | Statutory/regulatory basis with specific citations |
| Expedited Pathways | Breakthrough, fast track, priority review, waivers (if any) |

### 2. Subject Matter Description

- Product/device/substance/service identification (names, classifications, compositions)
- Intended use, target population, or scope of authorized operations
- Key identifiers (NDC, device class, CAS number, facility ID as applicable)

### 3. Supporting Evidence Summary

Present as a table mapping each regulatory criterion to the evidence submitted:

| Approval Criterion | Evidence Submitted | Key Findings |
|--------------------|--------------------|--------------|
| Safety | [Study type, N=] | [Primary endpoints, results] |
| Efficacy / Performance | [Study type, N=] | [Primary endpoints, results] |
| Manufacturing Quality | [CMC data, GMP compliance] | [Key controls, validation status] |
| Environmental / Public Impact | [Assessment type] | [Conclusions, mitigation measures] |

- Report statistical results with effect sizes, confidence intervals, p-values
- Flag any novel aspects, first-in-class designations, or areas lacking established regulatory pathways

### 4. Compliance Strategy

- Applicable statutes and regulations (cite specific sections)
- Guidance documents relied upon
- Pre-submission interactions and how agency feedback was incorporated
- Basis for any waiver, exemption, or special designation requests

### 5. Review Process & Timeline

| Milestone | Expected Date/Timeframe |
|-----------|------------------------|
| Filing/acceptance review | |
| Substantive review period | |
| Information request window | |
| Advisory committee (if applicable) | |
| Public comment period (if applicable) | |
| Target action date | |

### 6. Submission Package Inventory

Number and briefly describe each major attachment/appendix:

1. **Module/Volume X** — [Brief description]
2. **Appendix A** — [Brief description]
3. *(Continue for all components)*

### 7. Compliance Assessment

- [ ] Submission completeness relative to regulatory checklist
- [ ] Identified gaps or areas likely to trigger information requests
- [ ] Conditions or limitations that may attach to approval
- [ ] Post-approval commitments (REMS, Phase IV, monitoring, reporting)
- [ ] Ongoing compliance obligations

## Guidelines

- Use precise regulatory terminology; cite specific CFR sections, USC provisions, or agency guidance by name and number
- Mark any citation you cannot verify from the source materials with `[VERIFY]`
- Present data with appropriate qualifications — distinguish between statistically significant and clinically meaningful results
- Clearly label interpretive conclusions vs. factual statements from the submission
- Maintain jurisdiction awareness — FDA, EPA, FCC, and state agencies have distinct frameworks; do not conflate
- For FDA submissions, follow the CTD (Common Technical Document) module structure where applicable
- Flag any regulatory risk areas transparently; do not minimize uncertainties
- Format for professional regulatory file inclusion — suitable for executive review and agency correspondence
