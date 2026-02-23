---
name: policy-summary
description: Generates structured summaries of policy documents, legislative materials, regulatory frameworks, and institutional policies. Distills complex content into executive overviews, detailed breakdowns, and practical compliance insights. Use when summarizing policies, regulations, legislative proposals, compliance requirements, institutional rules, or preparing policy briefing materials.
tags:
  - analysis
  - regulatory
  - summarization
  - summary
---

# Policy Summary

Produces a structured, standalone summary of a policy document that captures scope, obligations, and practical compliance impact.

## Prerequisites

1. **Primary policy document(s)** — statute, regulation, institutional policy, or legislative proposal
2. **Amendments or supplements** — any modifications to the primary text
3. **Implementation guidance** — agency guidance, FAQs, or interpretive memoranda (if available)

## Process

### Step 1: Document Review

Search all uploaded matter files. Identify and extract:

| Element | What to capture |
|---|---|
| Defined terms | Terms with specific legal meaning that control interpretation |
| Scope & applicability | Who/what is covered; geographic and temporal reach |
| Requirements & prohibitions | Mandatory obligations vs. permissive provisions |
| Compliance mechanisms | Deadlines, thresholds, procedural steps |
| Enforcement | Penalties, consequences for non-compliance |
| Exceptions & carve-outs | Safe harbors, exemptions, de minimis thresholds |
| Cross-references | Links to other policies, statutes, or regulations |

### Step 2: Produce Summary

Use this output structure:

```
## Executive Overview
{2-3 paragraphs: core purpose, who it applies to, most significant provisions}

## Key Definitions
{Table of defined terms and their operative meanings}

## Substantive Provisions
### {Descriptive heading per topic area}
- What the policy requires / permits / prohibits
- Deadlines, thresholds, procedural requirements
- Ambiguities flagged with available interpretive guidance

## Compliance & Practical Implications
- [ ] Action items for stakeholders
- [ ] Risk/exposure areas
- [ ] Recommended next steps

## Conflicts & Open Questions
{Flag any conflicts with existing requirements or interpretive ambiguities}

## Source References
{Section/page citations to source documents}
```

### Step 3: For Legislative/Regulatory Proposals

When the policy involves proposed changes, search for current legal authorities to identify:
- What existing requirements would be modified
- Net-new obligations introduced
- Transition timelines and effective dates

## Guidelines

- **Distinguish obligation levels precisely**: use "must"/"requires" for mandatory; "may"/"allows" for permissive; flag aspirational/hortatory language separately
- **Separate summary from interpretation**: clearly distinguish what the policy states vs. your analytical observations
- **Preserve qualifications**: do not flatten conditions, limitations, or carve-outs — these are critical for compliance
- **Use descriptive headings**: organize by substance, not by source document section numbers
- **Cite specifically**: reference section numbers or page numbers for every substantive claim
- **Flag ambiguity**: note provisions subject to multiple interpretations and reference any available guidance
- **Accessible language**: minimize jargon while maintaining legal precision; the audience includes non-legal stakeholders
