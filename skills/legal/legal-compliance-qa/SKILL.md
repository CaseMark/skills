---
name: legal-compliance-qa
description: Answers legal and compliance questions from business teams using internal knowledge bases and approved sources. Provides sourced, caveated responses with confidence levels.
tags:
  - regulatory
  - analysis
  - research
---

# Legal Compliance Q&A

Answers internal legal and compliance questions using company knowledge bases.

## Prerequisites

1. **Question** — specific legal or compliance question from a business user
2. **Knowledge base** — company policies, procedures, regulatory guidance in vault
3. **Source hierarchy** — company policy > external guidance > general knowledge
4. **Confidence thresholds** — when to answer vs. escalate

## Workflow

### 1. Classify
- Policy question ("Can we do X under our retention policy?")
- Regulatory question ("What are our GDPR obligations?")
- Process question ("How do I get a contract approved?")
- Risk question ("Is this arrangement permissible?")

### 2. Search
Search vault in priority order: directly applicable policies, prior approved responses, regulatory guidance, external references.

### 3. Respond
Every response includes: direct answer, source citations (policy section, page number), caveats and scope limitations, confidence level (High/Medium/Low).

### 4. Escalate
Escalate when: no relevant policy exists, novel regulatory interpretation, jurisdiction-dependent answer, Low confidence.

## Pitfalls
- Frame as "based on company policy" not "you should legally do X"
- Always cite sources — unsourced answers can't be verified
- Flag stale policies (>12 months without update)
- Don't extrapolate across jurisdictions without confirmation
