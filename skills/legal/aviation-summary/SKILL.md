---
name: aviation-summary
description: >-
  Generates U.S. aviation-law summary documents by synthesizing FAA, DOT, and
  TSA rules, treaties, and precedent into an actionable legal analysis. Use
  for rapid briefings on air traffic rights, aircraft operations,
  airworthiness/certification, carrier liability, and incident/compliance
  exposure. Trigger keywords: aviation law, FAA, DOT, TSA, 14 CFR, FAA Part
  121/125/135, Montreal Convention, Warsaw Convention, ICAO, air traffic
  rights, route authority, code-sharing, slot allocation, accident liability.
tags:
  - analysis
  - regulatory
  - research
  - summarization
  - summary
---

# Aviation Law Summary

Produces a structured, defensible aviation-law summary for internal counsel, aviation operators, regulators, and legal teams.

## Prerequisites

1. Issue statement: define legal question, party posture, desired depth, and decision use (advisory, compliance memo, litigation prep).
2. Jurisdiction and scope: at minimum U.S. federal law; include foreign states of departure/arrival/operations when international carriage is involved.
3. Source set: uploaded documents + whether fresh legal research is permitted.
4. Output audience: client-facing versus internal counsel-facing tone and detail level.
5. Compliance constraints: confidentiality/classification limits and any preferred citation standards.

## Output Structure / Process

### 1) Source Triage (required first)
| Priority | Source Type | Action |
|---|---|---|
| 1 | Uploaded matter files | Extract facts, governing instruments, cited authorities, dates, and any pending procedural posture. |
| 2 | Primary law | Pull official statutes/regulations/treaties/cases from authoritative sources; capture exact text and effective dates. |
| 3 | Secondary support | Use only for context or trend analysis; never as the sole basis for a legal rule. |
| 4 | Gap assessment | Flag missing facts/legal authority and list what is needed to complete the summary. |

### 2) Authority Capture (must include all)
```markdown
| Type | Citation | Pinpoint | Jurisdiction | Core Holding/Rule | Direct Relevance | Confidence |
|---|---|---|---|---|---|---|
| Statute/Regulation | | | US/Federal/State/Foreign | | | |
| Treaty/Convention | | | | | | |
| Case Law | | | | | | |
| Agency Rule/Order | | | | | | |
```
- Add `[VERIFY]` on any citation, version, or quote not independently confirmed.

### 3) Mandatory Summary Sections
| Section | Minimum Content |
|---|---|
| Executive Overview | Core issue, legal posture, controlling framework, top 5 takeaways, immediate risks. |
| Regulatory Stack | FAA/Federal regulatory regime, DOT/TSA overlays, state law interactions, treaty intersections. |
| Jurisdictional Map | Domestic vs international application; country-of-treatment analysis for carriage and liability matters. |
| Case Law Matrix | Case name, citation, facts, holding, reasoning, practical effect, any splits/uncertainty. |
| Liability & Exposure | Accident, cargo, and passenger/counterparty exposure; limitation defenses; insurance/indemnity considerations. |
| Operations & Compliance | Certification, training, maintenance, reporting, record-retention, enforcement exposure, remedial controls. |
| Enforcement & Proceedings | Civil/administrative pathways, penalties, certificate actions, appeals, potential criminal threshold indicators. |
| Emerging Issues | UAS, advanced air mobility, commercial space overlaps, and open regulatory questions. |
| Table of Authorities | Complete list with Bluebook-formatted citations and pinpoint calls. |
| Recommendations | Priority actions, documentation plan, escalation points, monitoring triggers. |

### 4) Aviation-Specific Analytical Checklist
- Distinguish regime by claim type:
  - Passenger/cargo claims (international carriage framework vs domestic framework).
  - Operational compliance (operations, routes, slots, code-sharing).
  - Incident/accident aftermath (regulatory reporting vs civil exposure).
- Identify if treaty regime preempts or coexists with U.S. law.
- Confirm whether liability caps/defenses apply and when they are lost.
- Separate regulatory violation findings from tort-based exposure (no automatic civil shield).
- Track retroactivity and effective-date impacts.

## Guidelines

- Use concise headings, explicit issue labels, and matrix-style output for quick legal triage.
- Keep wording neutral and evidence-first; avoid overbroad conclusions.
- Flag jurisdictional uncertainty explicitly (state law overlay, treaty ratification timelines, forum clauses).
- Do not fabricate citations, holdings, or amendment dates.
- Mark every unconfirmed authority, quote, or version with `[VERIFY]`.
- If sources are thin, state: “insufficient authority” and list exact missing items.
- Default to U.S. federal sources first; escalate to foreign-source harmonization only when the fact pattern requires it.
- Include caveat when external search is used versus document-only scope.
