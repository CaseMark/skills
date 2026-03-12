---
name: legal-compliance-qa
description: Answers legal and compliance questions from business teams using internal knowledge bases, company policies, and regulatory sources. Provides sourced, caveated responses with confidence levels. Use when building internal legal helpdesks, compliance chatbots, or self-service legal knowledge systems.
tags:
  - compliance
  - knowledge-base
  - legal-ops
---

# Legal Compliance Q&A

Answers internal legal and compliance questions using company knowledge bases and approved sources.

## Prerequisites

1. **Question** — the specific legal or compliance question from a business user
2. **Knowledge base** — company policies, procedures, regulatory guidance documents in vault
3. **Source hierarchy** — which sources are authoritative (company policy > external guidance > general knowledge)
4. **Confidence thresholds** — when to answer directly vs. when to escalate to a human lawyer

## Workflow

### 1. Classify the Question

- **Policy question** — "Can we do X under our data retention policy?"
- **Regulatory question** — "What are our GDPR obligations for this data transfer?"
- **Process question** — "How do I get a contract approved?"
- **Risk question** — "Is this arrangement permissible?"

### 2. Search and Retrieve

Search vault for relevant sources in priority order:
1. Company policies and SOPs directly on point
2. Prior approved responses to similar questions
3. Regulatory guidance documents
4. External legal references (flag as general, not advice)

### 3. Compose Response

Every response must include:
- **Direct answer** — clear yes/no/it-depends with explanation
- **Source citations** — specific policy sections, document names, page numbers
- **Caveats** — scope limitations, jurisdictional notes, when the answer might not apply
- **Confidence level** — High (directly addressed by policy), Medium (interpreted from policy), Low (escalate)

### 4. Escalation

Escalate to human lawyer when:
- No relevant policy or precedent exists
- Question involves novel risk or regulatory interpretation
- Answer could vary significantly by jurisdiction
- Confidence level is Low

## Pitfalls

- **Never give legal advice** — frame as "based on company policy" not "you should legally do X"
- **Always cite sources** — unsourced answers erode trust and can't be verified
- **Flag stale policies** — if the most relevant policy hasn't been updated in >12 months, note this
- **Don't extrapolate across jurisdictions** — a US policy answer doesn't apply to EU operations without explicit confirmation
