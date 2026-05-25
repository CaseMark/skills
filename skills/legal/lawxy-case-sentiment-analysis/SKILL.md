---
name: case-sentiment-analysis
description: Analyze case files to determine judicial and opposing-party sentiment, predict case trajectory, and identify key issues from pleadings, briefs, and evidence
tags:
  - practice_area: litigation
  - document_type: brief, pleading
  - skill_mode: analysis
---

# Legal Case Sentiment Analysis

Analyze litigation files to extract sentiment signals, predict likely outcomes, and surface critical strategic issues.

## Prerequisites

- Full case file (pleadings, briefs, motions, deposition excerpts)
- Jurisdiction and court context
- Opposing party profile (if available)

## Workflow

1. Ingest all case documents and build a complete matter timeline
2. Score sentiment per party, per judge, and per issue (strongly-positive → strongly-negative)
3. Identify pivotal moments: key motions filed, adverse rulings, evidentiary wins/losses
4. Map sentiment shifts across the litigation lifecycle
5. Produce a case narrative with predictive outcome ranges (settlement likelihood, trial probability, estimated damages)
6. Recommend strategic adjustments based on sentiment trajectory

## Pitfalls

- Sentiment ≠ legal merit; a positive sentiment score doesn't guarantee a win
- Judge-specific bias must account for published rulings history, not just current case
- Avoid overfitting to a small sample of the judge's past decisions
- Flag when sentiment analysis is unreliable (unclear authorship, ambiguous language)
