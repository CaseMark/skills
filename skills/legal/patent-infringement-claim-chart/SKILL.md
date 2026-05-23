---
name: patent-infringement-claim-chart
description: Generate AI-assisted patent claim charts mapping patent claims to product features
tags:
  practice: litigation
  document: analysis
  mode: drafting
---

# Patent Infringement Claim Chart

Generate structured claim charts comparing patent claim elements against target product features.

## Prerequisites

- Target patent number and claims (especially Claim 1)
- Target product description, specifications, or source code
- Product testing results or teardown documentation

## Workflow

1. **Extract claim elements** — Break down each claim into individual elements (element-by-element decomposition)
2. **Map to product features** — For each claim element, identify the corresponding product feature or component
3. **Gather evidence** — Cite specific product documentation, screenshots, test results, or source code lines
4. **Score confidence** — Assign a confidence score (0–100) for each element mapping based on evidence quality
5. **Generate analysis** — Write AI-powered analysis explaining why each element is met or not met
6. **Summary scoring** — Aggregate element scores into an overall infringement assessment

## Pitfalls

- Don't skip dependency chains — dependent claims add further limitations
- Element decomposition must be precise — vague elements lead to weak charts
- Product evidence must be specific (cite exact version, date, section)
- Missing elements can defeat infringement — flag gaps prominently
- Design patent claim charts use drawings, not text claims — adapt approach accordingly
