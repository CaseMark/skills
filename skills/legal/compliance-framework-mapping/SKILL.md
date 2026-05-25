name: compliance-framework-mapping
language: en
description: Maps regulatory requirements across multiple frameworks (GDPR, SOC 2, NIST, ISO 27001, etc.) to identify overlaps, gaps, and dual-fulfillment opportunities. Produces a cross-reference matrix enabling efficient compliance with simultaneous standards.
tags:
  - research
  - memo
  - regulatory
---

# Cross-Framework Regulatory Mapping

Identifies overlaps, gaps, and dual-fulfillment opportunities across multiple regulatory frameworks to streamline compliance programs and reduce redundant controls.

## Prerequisites

Before executing, collect:

1. **Applicable frameworks** — list of all regulations/standards the organization must comply with
2. **Jurisdictions** — countries/regions where the organization operates or processes data
3. **Industry sector** — healthcare, finance, SaaS, retail, etc. (affects applicable regulations)
4. **Data classification** — types of data handled (PII, financial, health, IP, etc.)

## Workflow

1. **Framework ingestion** — load requirements from each applicable framework/standard
2. **Requirement normalization** — express each requirement in a common reference format
3. **Overlap detection** — identify requirements across frameworks that address the same obligation
4. **Gap identification** — flag regulatory obligations not covered by existing controls
5. **Dual-fulfillment matrix** — produce cross-reference showing which controls satisfy which frameworks
6. **Priority ranking** — score by regulatory severity, audit frequency, and enforcement risk
7. **Roadmap output** — generate phased implementation plan addressing highest-impact requirements first

## Pitfalls

- Similar wording ≠ same requirement — check scope and exceptions carefully
- Framework updates are asynchronous — a mapping today may break with next revision
- Some frameworks have jurisdictional clauses that don't apply universally
- Over-optimizing for dual-fulfillment can create blind spots in framework-specific requirements
