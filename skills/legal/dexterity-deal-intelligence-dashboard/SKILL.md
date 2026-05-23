---
name: dexterity-deal-intelligence-dashboard
description: Organize deal negotiation intelligence in real-time dashboards, aggregating data from email threads and document versions
tags:
  - practice: corporate, transactional
  - document: summary, checklist
  - mode: analysis, research
---

# Dexterity Deal Intelligence Dashboard

Aggregate and organize deal negotiation data from scattered email threads and document versions into a unified real-time dashboard.

## Prerequisites

- Email integration (Microsoft Outlook or Gmail)
- Document storage with version history
- Deal structure document mapping key terms to file locations
- Negotiation timeline tracking

## Workflow

1. Connect email and document systems to the deal workspace
2. Auto-classify incoming communications: draft version received, markup sent, term confirmation, internal note
3. Map key terms from each document version to a live comparison table
4. Track negotiation status per clause: open, countered, agreed, disputed
5. Generate deal health dashboard: version age, response time, bottleneck clauses, remaining items
6. Alert on stale items (>48h no response) and escalate to responsible party
7. Export consolidated term sheet from latest document versions

## Pitfalls

- Email parsing misses non-email communications (Slack, phone calls, meeting notes); document all outside communications
- Version conflicts: two parties may submit markups simultaneously; detect and flag concurrent edits
- Dashboard data is only as good as the source; manual entry of verbal agreements is essential
- High-volume email threads can obscure critical term changes; prioritize clause-level tracking over full-document review
- Client-facing dashboards must sanitize internal notes and flagged items before external sharing
