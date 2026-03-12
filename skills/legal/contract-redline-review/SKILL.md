---
name: contract-redline-review
description: Reviews incoming contracts against company standards and generates redline markups identifying deviations, risks, and required changes. Compares clause-by-clause against approved positions and produces annotated review documents. Use when processing high volumes of third-party paper, vendor agreements, or any contract not drafted from company templates.
tags:
  - contracts
  - review
  - redlining
---

# Contract Redline Review

Reviews third-party contracts against company standards and generates redline markups with recommended changes.

## Prerequisites

1. **Incoming contract** — the third-party document to review, uploaded to vault
2. **Company standards** — approved clause language, acceptable ranges, and non-negotiable terms by contract type
3. **Risk tolerance matrix** — which deviations are acceptable, which need flagging, which are blockers

## Workflow

### 1. Extract and Parse

- OCR the document if needed (scanned PDFs)
- Identify contract type, governing law, and key structural elements
- Parse into clause-level segments for comparison

### 2. Clause-by-Clause Review

For each substantive clause, compare against company standard:

| Review Area | Check |
|---|---|
| Liability & indemnification | Caps, carve-outs, mutual vs. one-way |
| IP ownership | Assignment vs. license, work product scope |
| Confidentiality | Duration, scope, exceptions, survival |
| Termination | Notice period, cure rights, termination for convenience |
| Data protection | Processing terms, breach notification, sub-processors |
| Governing law & dispute | Jurisdiction, arbitration vs. litigation, venue |
| Payment | Net terms, late fees, price escalation |
| Insurance | Required coverage types and minimums |

### 3. Risk Score

Assign each deviation a severity:
- **Green** — within acceptable range, note but don't redline
- **Yellow** — outside standard but negotiable, redline with suggested language
- **Red** — material risk or non-starter, redline and flag for human review

### 4. Generate Redline

- Mark all Yellow and Red items with tracked changes
- Add comments explaining the risk and suggested alternative language
- Produce summary table: total clauses reviewed, deviations found by severity
- Store annotated version in vault

## Pitfalls

- **Don't miss boilerplate traps** — assignment clauses, entire agreement, amendment provisions often hide material terms
- **Check definitions section** — defined terms can redefine standard language to mean something unexpected
- **Flag missing clauses** — absence of a standard protection (e.g., no limitation of liability) is itself a Red finding
- **Never approve by omission** — if a clause isn't in your standards library, flag it for human review rather than skipping
