---
name: flipthrough-contract-proposal-analysis
tags:
  practice: corporate
  document: analysis
  mode: analysis
---

# Contract and Proposal Analysis

## Purpose
Analyze vendor proposals, MSAs, SOWs, SLAs, and licensing agreements. Identify key terms, risk exposures, liabilities, and negotiation leverage points. Output is a structured analysis with scoring and recommendations.

## Prerequisites
- The contract or proposal document (PDF, Word, or text)
- Buyer's standard terms and playbooks (if available)
- Procurement category (IT, services, cloud, etc.)
- Deal context: competitive or sole-source

## Workflow
1. Classify the document type (MSA, SOW, SLA, license, proposal, NDA) and extract the header terms: parties, effective date, term, governing law
2. Extract and analyze key clauses: indemnification, liability caps, IP ownership, data protection, termination, renewal, pricing, SLA/service credits
3. Score each clause against buyer's standard terms: (a) matches standard, (b)偏离 with rationale, (c) material deviation
4. Identify hidden risks: auto-renewal traps, unilateral change rights, broad IP grants, uncapped liability, onerous service credits
5. Rank issues by negotiation priority: (1) must-fix, (2) should-negotiate, (3) nice-to-have
6. Provide recommended alternative language for each material deviation
7. Produce a one-page deal summary with total risk score and negotiation strategy

## Pitfalls
- Do not assume vendor documents are in good faith — flag all asymmetrical risk allocations
- Pricing terms in proposals are often placeholder — flag for commercial verification
- Service-level commitments in proposals may not appear in the final contract — flag for negotiation
- Beware of cross-references to other documents that change the terms materially
- Distinguish between the proposal (marketing document) and the actual contract (legal obligation)
