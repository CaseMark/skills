---
name: litigation-risk-modeling
description: Build automated litigation risk models from pleadings, calculate probability-weighted outcomes for claimant and defendant perspectives
tags:
  - practice_area: litigation
  - document_type: analysis, memo
  - skill_mode: analysis
---

# Automated Litigation Risk Modeling

Generate deterministic risk models from legal pleadings with dual-party perspective analysis and probability-weighted outcomes.

## Prerequisites

- Court pleadings (statement of claim, defense, reply)
- Applicable jurisdiction's case law database
- Cost framework for the relevant court/tribunal

## Workflow

1. Ingest pleadings and automatically extract the dispute model (parties, claims, defenses, damages sought)
2. Build a risk model using jurisdiction-specific precedent weights
3. Generate claimant-side outcome probability distribution (win/loss/ partial, expected damages)
4. Generate defendant-side outcome probability distribution independently
5. Identify the Model Settlement Value where both probability lines intersect
6. Apply lawyer refinement overlay for strategy, costs, and settlement offers
7. Output a Settle Chart showing both parties' risk curves and the Model Settlement Value

## Pitfalls

- Risk models are probabilistic, not deterministic — always present confidence ranges
- Lawyer refinement must be clearly labeled as advisory, not replacing legal judgment
- Cost projections must be jurisdiction-specific; generic cost models produce misleading results
- Dual-party models must be generated independently to avoid confirmation bias
