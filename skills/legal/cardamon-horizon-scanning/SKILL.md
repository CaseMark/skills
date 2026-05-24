---
name: horizon-scanning
language: en
description: >-
  Continuously monitors regulatory landscapes for changes relevant to a
  specific business. Ingests global regulatory updates, filters by relevance,
  summarizes impact, and produces an actionable change advisory. Use when
  tracking regulatory developments affecting a particular product or market.
tags:
  - regulatory
  - compliance
  - research
---

# Horizon Scanning

Structured process for detecting, filtering, and analyzing regulatory changes
that may affect a specific business.

## Prerequisites

- Business profile (products, services, jurisdictions, activity types)
- Source regulatory feeds (government gazettes, agency calendars, monitors)
- Time window (rolling 30 days, quarterly, ad-hoc)

## Workflow

1. **Signal collection** — aggregate regulatory signals from defined sources:
   - New legislation, regulations, directives
   - Agency guidance, interpretive letters, FAQs
   - Enforcement actions and consent orders
   - Draft regulations and proposed rules
2. **Filtering** — apply relevance filters:
   - Jurisdiction overlap with business operations
   - Sector/domain match (products/services engaged)
   - Effective date window (active or upcoming within 12 months)
3. **Impact assessment** — for each relevant signal:
   - Summarize the change in plain language
   - Identify affected obligations (new, modified, repealed)
   - Assess materiality (high/medium/low) based on operational impact
4. **Advisory output** — produce a structured update with:
   - Regulation identifier, effective date, source
   - Business-specific impact statement
   - Recommended action items and responsible parties
   - Links to full text and comment periods

## Pitfalls

- Don't over-filter: early-stage draft regulations can still signal enforcement priorities
- Enforcement actions, while not new rules, often reveal how agencies interpret existing obligations
- International regulations in translation may lose nuance — flag and note the original language
- Multiple overlapping regulations may address the same issue — identify the controlling hierarchy
- Comment periods for draft regulations are compliance-critical opportunities — never miss deadlines
