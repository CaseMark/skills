---
name: verified-legal-research
language: en
description: >-
  Conducts legal research with optional human lawyer verification. Combines
  AI-generated research answers with a lawyer-in-the-loop verification step
  for jurisdiction-specific accuracy. Use when research accuracy is critical
  and verification can reduce hallucination risk.
tags:
  - research
  - drafting
  - analysis
---

# Verified Legal Research

Legal research workflow that couples AI-generated answers with human verification
for jurisdiction-specific accuracy and confidence.

## Prerequisites

- Clear research question (single issue, scoped to one jurisdiction)
- Identified governing law and authority sources
- Knowledge that verification is available for the target jurisdiction

## Workflow

1. **AI research generation** — produce an initial research answer:
   - Identify the legal issue and applicable jurisdiction
   - Retrieve primary authority (statutes, regulations, case law)
   - Supplement with secondary authority and practice guidance
   - Draft the answer with inline source references
2. **Self-audit** — review the AI-generated answer:
   - Are all citations current and still good law?
   - Does the answer address the precise question asked?
   - Are there competing authorities not mentioned?
   - Is the jurisdiction correctly scoped?
3. **Verification handoff** (optional) — for questions requiring verified accuracy:
   - Submit the research question and AI-generated answer to a local practicing attorney
   - Attorney reviews the answer against the source authorities
   - Attorney provides corrections, additions, or confirmation
4. **Final delivery** — produce the verified research output:
   - State whether verification was performed
   - If verified, include the verifier's modifications and confidence level
   - If not verified, include standard AI accuracy disclaimer
   - Provide all source links and a research trail

## Pitfalls

- Never present unverified AI research as authoritative without clear disclaimers
- Verification doesn't guarantee correctness — verify the verifier's answer against sources when possible
- Jurisdiction is the most common error vector — confirm venue rules and local procedures
- AI can hallucinate citations that look real but don't exist — always validate every citation independently
- The lawyer-in-the-loop adds latency — for routine research, the AI answer with self-audit may be sufficient
