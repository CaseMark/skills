---
name: maritime-case-summary
description: Produces structured summaries of maritime law cases covering admiralty jurisdiction, shipping contracts, collisions, liens, salvage, cargo damage, and personal injury aboard vessels. Extracts key facts, legal issues, procedural posture, holdings, and practical implications using maritime-specific doctrines and terminology. Use when summarizing admiralty cases, maritime dispute opinions, collision rulings, Jones Act claims, or charter party litigation.
tags:
  - litigation
  - summarization
  - summary
---

# Maritime Law Case Summary

Generates a structured analytical summary of maritime law cases from uploaded case materials.

## Prerequisites

1. **Case materials** — judicial opinion, pleadings, or briefs for the maritime matter
2. **Identify case type** — collision/allision, cargo damage, personal injury, charter party dispute, lien enforcement, salvage, limitation of liability, or jurisdictional challenge

## Output Structure

Produce the summary using these sections in order:

### 1. Case Caption & Citation

| Field | Content |
|-------|---------|
| Case name | Full caption |
| Citation | Bluebook format [VERIFY all citations] |
| Court | Including circuit/district |
| Date | Date of decision |
| Maritime subject | Primary area (e.g., collision, cargo, Jones Act) |

### 2. Procedural Posture

- Litigation stage and specific motion/appeal being decided
- Whether brought in admiralty or diversity jurisdiction (note significance)

### 3. Factual Background

Extract from case materials:
- Vessel name(s), type, and flag state
- Parties and roles (owner, charterer, shipper, cargo interest, seafarer)
- Date, location, and jurisdictional waters of incident
- Weather/sea conditions if relevant
- Chronological sequence of events
- Monetary amounts in dispute

### 4. Legal Issues

Frame each issue in terms of maritime doctrine. Common categories:

| Domain | Key Questions |
|--------|--------------|
| Jurisdiction | Admiralty jurisdiction under location test + nexus test; Extension of Admiralty Jurisdiction Act |
| Choice of law | General maritime law vs. state law; foreign-flag analysis |
| Collision/allision | Fault allocation under Navigation Rules; Reliable Transfer comparative fault |
| Liability limits | Limitation of Liability Act applicability |
| Contract | Charter party or bill of lading interpretation; Hague-Visby Rules, Hamburg Rules |
| Personal injury | Jones Act, LHWCA, or general maritime law cause of action; seaman status |
| Liens | Maritime lien priority and enforcement |
| Salvage | Voluntary service, danger, success elements |
| Economic loss | Robins Dry Dock rule application |
| Environmental | OPA 90, CWA liability |
| International | UNCLOS, applicable conventions |

Summarize each party's position and note any circuit splits or novel questions.

### 5. Holding & Reasoning

- Court's resolution of each identified issue
- Specific maritime doctrines applied (name the doctrine)
- Key statutory or regulatory provisions relied upon (cite specifically)
- Treatment of any international conventions
- Dissenting opinions that may signal future challenges

### 6. Practical Implications

- Impact on vessel owners, charterers, cargo interests, insurers, or seafarers
- Whether decision establishes new precedent or clarifies unsettled law
- Operational guidance derived from the ruling

## Guidelines

- **Terminology precision**: Use "vessel" not "boat"; distinguish "collision" (two moving vessels) from "allision" (vessel strikes fixed object); "charterer" vs. "shipper"; "seaman"/"seafarer" not generic terms
- **Damage categories**: Distinguish property damage, personal injury, economic loss, and environmental damages
- **Technical concepts**: When referencing general average, particular average, demurrage, deviation, or salvage, include a one-line definition for non-specialist readers
- **Citations**: Bluebook format; mark any unverified citation with [VERIFY]
- **Scope**: Comprehensive enough as standalone reference, concise enough for quick review
- **Jurisdiction flags**: Always note whether admiralty jurisdiction was contested and how it was resolved
