---
name: patent-summary
description: Generates structured summaries of patent applications, extracting bibliographic data, technical descriptions, claims analysis, drawings, and legal-strategic observations. Produces prosecution-ready overviews balancing technical accuracy with accessibility. Use when summarizing patent filings, preparing for prosecution, licensing negotiations, portfolio review, or freedom-to-operate analysis.
tags:
  - analysis
  - summarization
  - summary
  - transactional
---

# Patent Application Summary

Produces a structured, prosecution-ready summary of a patent application covering bibliographic data, technical substance, claim scope, and strategic considerations.

## Prerequisites

1. **Patent application document** — specification, claims, abstract, drawings
2. **Priority/related applications** — if referenced in the filing
3. **Target audience context** — prosecution team, licensing, litigation, or portfolio management

## Output Structure

### 1. Executive Overview

Two to three sentences capturing the invention's essence, technical field, and broadest claim scope.

### 2. Bibliographic Data

| Field | Extract |
|---|---|
| Application No. | — |
| Filing Date | — |
| Inventor(s) | — |
| Assignee | — |
| Priority Claims | — |
| Related Applications | — |
| Technical Field | — |

### 3. Background & Problem

- Problem addressed by the invention
- Key prior art cited and how the applicant distinguishes from it
- Novelty and non-obviousness positioning

### 4. Invention Description

- How it works — key components, steps, or architecture
- Core innovative aspects vs. prior art
- Specific embodiments or examples with practical applications
- Write accessibly for attorneys outside the technology specialty while maintaining technical precision

### 5. Drawings & Figures

| Figure | Description |
|---|---|
| Fig. 1 | — |
| Fig. 2 | — |
| ... | ... |

### 6. Claims Analysis

| Claim | Type | Scope Summary |
|---|---|---|
| 1 | Independent | — |
| N | Independent | — |
| Key dependents | Dependent | — |

- **Total claims**: [count]
- **Independent claims**: [count]
- **Claim format flags**: Note any means-plus-function (35 U.S.C. § 112(f)), Beauregard, or Jepson claims

### 7. Strategic Observations

#### Scope & Strength
- Claim breadth assessment
- Potential limitations or design-around vulnerabilities
- Commercially significant dependent claim narrowings

#### Prosecution Risk Flags

| Issue | Risk Level | Notes |
|---|---|---|
| Enablement (§ 112(a)) | Low/Med/High | — |
| Written Description | Low/Med/High | — |
| Indefiniteness (§ 112(b)) | Low/Med/High | — |
| Prior Art Overlap | Low/Med/High | — |

#### Commercial & Portfolio Notes
- Competitive landscape implications
- Licensing or FTO considerations
- Recommended next steps for prosecution or portfolio strategy

## Guidelines

- Cite specific section headings, claim numbers, and figure references throughout
- Target length: 1–3 pages balancing comprehensiveness with conciseness
- Use precise IP terminology but keep descriptions accessible to non-specialist attorneys
- Flag any uncited prior art you identify as potentially relevant with `[NOTE]`
- Do not speculate on patentability conclusions — present observations, not opinions on allowability
- For continuation or divisional applications, note relationship to parent filing
- Jurisdiction: U.S. patent practice (USPTO) unless otherwise specified
