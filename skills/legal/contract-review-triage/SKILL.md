name: contract-review-triage
language: en
description: Prioritizes contracts for human review by ML-assisted risk assessment — scores contracts by complexity, risk exposure, and negotiation urgency. Enables legal service providers and law firms to triage high-volume document reviews efficiently.
tags:
  - analysis
  - checklist
  - corporate
---

# ML-Assisted Contract Review Triage

Scores and prioritizes contracts for legal review based on ML-identified risk factors, complexity indicators, and business urgency — enabling efficient triage of high-volume contract portfolios.

## Prerequisites

Before executing, collect:

1. **Contract batch** — collection of contracts to triage (PDFs, DOCX, or text)
2. **Review criteria** — what matters most (risk, complexity, revenue impact, regulatory exposure)
3. **Risk thresholds** — what score ranges trigger urgent vs. routine vs. no-review
4. **Reviewer capacity** — how many contracts per reviewer per day determines prioritization

## Workflow

1. **Document ingestion** — batch load contracts with metadata (counterparty, type, execution date)
2. **ML risk scoring** — analyze each contract for risk signals: unusual terms, missing protections, asymmetric obligations
3. **Complexity scoring** — count clauses, cross-references, custom provisions vs. boilerplate ratio
4. **Business context** — weight scores by contract value, counterparty risk, regulatory environment
5. **Priority ranking** — sort contracts into triage tiers: critical review, standard review, light review, no-review
6. **Assignment** — route to appropriate reviewer based on specialty (commercial, employment, IP, etc.)
7. **Feedback loop** — capture reviewer corrections to improve ML model accuracy over time

## Pitfalls

- ML scores are probabilistic — low-risk scores can miss novel or jurisdiction-specific issues
- Scoring models need continuous calibration — feedback from reviewer corrections is essential
- High-volume contexts may require different thresholds than one-off reviews
- Custom contracts from sophisticated counterparties need senior reviewer assignment regardless of score
