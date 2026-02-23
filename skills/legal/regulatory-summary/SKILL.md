---
name: regulatory-summary
description: Generates structured summaries of regulatory documents including agency rules, guidance, enforcement actions, and compliance frameworks. Extracts key provisions, requirements, deadlines, obligations, penalties, safe harbors, and actionable compliance insights with pinpoint citations. Use when summarizing regulations, agency guidance, rulemaking notices, enforcement orders, compliance advisories, or administrative decisions for regulatory matters.
tags:
  - analysis
  - regulatory
  - summarization
  - summary
---

# Regulatory Document Summarization

Produces a structured, citation-grounded summary of regulatory documents that serves as both a standalone reference and a roadmap for deeper analysis.

## Prerequisites

1. **Regulatory document(s)** — final rules, proposed rules, guidance, enforcement actions, no-action letters, compliance frameworks, or administrative decisions
2. **Context** (if available) — client industry, existing compliance posture, specific questions to address

## Output Structure

### 1. Executive Overview (2–3 sentences)
- Issuing authority and document type
- Core purpose and most significant takeaway
- Effective date or comment deadline

### 2. Document Metadata Table

| Field | Detail |
|---|---|
| Issuing Agency | |
| Document Type | Final rule / Proposed rule / Guidance / Enforcement / Other |
| Citation / Docket No. | |
| Effective Date | |
| Comment Deadline | (if applicable) |
| Compliance Deadline(s) | |
| Regulated Entities | |
| Supersedes / Amends | |

### 3. Key Provisions

For each major provision, provide:

| # | Provision | Requirement / Prohibition | Citation (§, ¶, p.) | Compliance Action Required |
|---|---|---|---|---|
| 1 | | | | |

- Quote operative definitions and critical language verbatim
- Flag areas of ambiguity or discretionary agency interpretation with `[AMBIGUOUS]`

### 4. Changes from Prior Framework

| Area | Prior Rule | New Rule | Impact |
|---|---|---|---|
| | | | |

Skip this section if the document is not amending a prior framework.

### 5. Safe Harbors & Exemptions

- List each safe harbor, exemption, or de minimis threshold with citation
- Note qualifying conditions

### 6. Enforcement & Penalties

| Violation Type | Penalty Range | Enforcement Mechanism | Citation |
|---|---|---|---|
| | | | |

### 7. Cross-References

List referenced statutes, regulations, or guidance with brief relevance explanation:
- **[Citation]** — relevance to this document

### 8. Compliance Action Items

| Priority | Action | Deadline | Notes |
|---|---|---|---|
| Immediate | | | |
| Near-term | | | |
| Ongoing | | | |

### 9. Open Questions & Ambiguities

- Areas where regulatory text is unclear or subject to interpretation
- Expected future guidance or rulemaking
- Issues requiring follow-up research or specialist consultation

## Guidelines

- Ground every statement in the source text; never infer requirements not present in the document
- Provide pinpoint citations (section, paragraph, page) for every substantive claim
- Quote verbatim when precision matters: definitions, operative requirements, deadlines
- Use plain language alongside technical regulatory terminology
- Flag interpretive uncertainty with `[AMBIGUOUS]` — do not resolve ambiguity by guessing agency intent
- Scale summary length to document complexity: 1 page for simple guidance, up to 3 pages for complex final rules
- If the document is part of a broader rulemaking initiative, note the procedural posture (NPRM, final rule, interim final rule)
- Do not editorialize on policy merits; maintain analytical neutrality
