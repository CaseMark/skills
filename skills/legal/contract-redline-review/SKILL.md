---
name: contract-redline-review
description: Reviews incoming contracts against company standards and generates redline markups identifying deviations, risks, and required changes.
tags:
  - contracts
  - review
  - redlining
---

# Contract Redline Review

Reviews third-party contracts against company standards and generates recommended changes.

## Prerequisites

1. **Incoming contract** — third-party document uploaded to vault
2. **Company standards** — approved clause language and acceptable ranges by contract type
3. **Risk tolerance matrix** — acceptable vs. flagged vs. blocked deviations

## Workflow

### 1. Parse
OCR if needed. Identify contract type, governing law, structural elements. Parse into clause-level segments.

### 2. Review
Compare each clause against standards: liability/indemnification, IP ownership, confidentiality, termination, data protection, governing law, payment terms, insurance requirements.

### 3. Score
- **Green** — within acceptable range, note but don't redline
- **Yellow** — outside standard but negotiable, redline with suggested language
- **Red** — material risk or non-starter, flag for human review

### 4. Generate Redline
Mark Yellow and Red items with tracked changes. Add explanatory comments. Produce summary table of deviations by severity. Store annotated version in vault.

## Pitfalls
- Check definitions section — defined terms can redefine standard language unexpectedly
- Flag missing clauses — absence of a standard protection is itself a Red finding
- Don't miss boilerplate traps — assignment, entire agreement, amendment provisions
- Never approve by omission — unfamiliar clauses get flagged, not skipped
