---
name: obligation-mapping
language: en
description: >-
  Extracts regulatory obligations from dense regulations across jurisdictions.
  Breaks down multi-level regulations into clear article-level obligations,
  classifies applicability to a business, and prioritizes by risk level.
  Use when translating regulations into actionable compliance requirements.
tags:
  - regulatory
  - compliance
  - analysis
---

# Obligation Mapping

Systematic process for extracting, classifying, and prioritizing regulatory obligations from complex regulatory text.

## Prerequisites

- Source regulation text (statute, directive, regulation, guidance)
- Target business description (products, activities, markets, jurisdictions)
- Jurisdiction and effective dates

## Workflow

1. **Regulation ingestion** — identify the full regulatory text including all levels (law, regulation, directive, guidance)
2. **Obligation extraction** — parse each article/section for mandatory language (shall, must) vs. permissive language (may) vs. aspirational (should)
3. **Applicability scoring** — match extracted obligations against the target business profile:
   - Product/Service fit: does the business offer regulated products or services?
   - Activity match: does the business engage in covered activities?
   - Geographic scope: are operations in covered jurisdictions?
   - Entity type: does the entity type fall under the regulation?
4. **Risk prioritization** — assign priority (critical/high/medium/low) based on:
   - Enforcement severity (fines, criminal, license revocation)
   - Probability of enforcement action
   - Remediation complexity and cost
5. **Output format** — produce a structured obligation register with article reference, obligation text, applicability rationale, priority, and responsible function

## Pitfalls

- Don't conflate permissive guidance with mandatory obligation — always flag the exact statutory language
- Watch for nested obligations: an article may reference another regulation for the actual requirement
- International regulations often have implementation deadlines that differ from entry-into-force dates
- Cross-references between regulations can create cascading obligations — trace the full chain
- Translated regulations may use ambiguous terminology — note language version and flag uncertain translations
