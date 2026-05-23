---
name: dexterity-version-control-deals
description: Manage document version control for deal negotiations with automated comparison and consolidated term extraction
tags:
  - practice: corporate
  - document: agreement, summary
  - mode: analysis, drafting
---

# Dexterity Deal Version Control

Automated document version comparison and term consolidation for multi-round deal negotiations.

## Prerequisites

- Source document with structured clause numbering or headings
- Clause-by-clause negotiation tracker
- Historical document versions stored in accessible location
- Change summary template for each negotiation round

## Workflow

1. Import all document versions for the negotiation thread
2. Run automated comparison engine across versions to identify clause-level changes
3. Generate version delta summary: added, removed, modified, unchanged per clause
4. Extract current negotiated state of each term from the latest version
5. Produce consolidated term sheet reflecting the final agreed position on every clause
6. Compare consolidated terms against original deal expectations and identify gaps
7. Deliver version-control report to deal team with clear recommendations on remaining open items

## Pitfalls

- Auto-comparison may miss subtle wording changes that shift legal meaning; always do manual clause review
- Structured clauses with cross-references break comparison engines; verify cross-references after merge
- Redline-only tracking loses negotiated compromises hidden in markup; ensure clean versions are also ingested
- Term extraction assumes clause headings match across versions; rename anomalies break mapping
- Don't rely on version count as deal health indicator — 20 versions with no term movement means stale negotiations
