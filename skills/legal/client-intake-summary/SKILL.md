---
name: client-intake-summary
description: >-
  Produces a US corporate-client intake summary from intake forms,
  consultation notes, and initial communications. Use when onboarding a new
  corporate matter to convert raw intake data into a structured, team-ready
  brief with factual source tags, conflict-awareness, urgency triage, fee
  context, and immediate action steps. Trigger: client intake, new matter,
  onboarding packet, consult notes, retainer discussion, conflict check,
  deadline flag, corporate governance matter.
tags:
  - corporate
  - summarization
  - summary
---

# Client Intake Summary

Summarizes new-corporate-matter intake materials into a single, evidence-ready intake brief for attorney review and matter activation.

## Prerequisites

1. Intake packet: forms, engagement data, identity/contact details, and represented entity structure.
2. All available communications: email, text, call notes, meeting notes, and preliminary documents.
3. Jurisdiction cues: governing state, filing location, or governing corporate documents where identified.
4. Conflict check inputs: firm CRM/conflict database, prior representation list, or confirmation that no check was possible.
5. Fee framework inputs: hourly/flat expectations, retainer discussion, billing constraints, and payor source.
6. Any time-sensitive facts: potential deadlines, hearings, board deadlines, contract dates, or expiration dates.
7. Permission scope and confidentiality scope noted for each document source.

## Output Structure / Process

Produce sections in fixed order; if unknown, mark `Unknown`.

| Section | Required content | Required format |
|---|---|---|
| Executive Overview | 2–3 sentence summary of matter, client objective, immediate urgency | Plain text |
| Client Profile | Individual/entity names, roles, contacts, communication preferences, language/accessibility needs, confidentiality sensitivity | Bulleted fields |
| Matter Snapshot | Matter type, legal issue, key parties, factual timeline, current status, governing entities | Chronological table |
| Preliminary Legal Considerations | Governing law cues, implied claims/issues, jurisdiction questions, privilege or authority risks, potential SOL flag | Checklist |
| Financial Notes | Fee discussion, retainer status, payment concerns, budget constraints, funding source, billing risk | Bulleted with dollar amounts standardized |
| Risks and Red Flags | Inconsistencies, credibility issues, unrealistic outcomes, complexity escalation indicators | Risk table (Low/Med/High) |
| Conflicts and Ethics | Conflict search status, adverse parties overlap, confidentiality conflicts, privilege boundaries | Status table |
| Follow-Up Queue | Missing facts, documents, and answers needed from client/team | Numbered action list |
| Immediate Next Steps | 24h actions, 7-day actions, owner and dependency | Prioritized checklist |

```text
OUTPUT TEMPLATE

Client:
Matter ID:
Matter Type:
Jurisdiction:
Intake Sources:
Date Received:
Status: New / Pending / Urgent

Executive Overview:
...

Client Profile:
- Name:
- Entity:
- Contacts:
- Communication Preferences:
- Special Instructions:

Matter Snapshot:
Date | Event | Parties | Source | Issues
...
```

### Core rules while drafting

1. Separate facts from inferences: `Fact` rows must include at least one source reference.
2. Use standardized date format: `YYYY-MM-DD`.
3. Preserve direct client quotes only when materially relevant.
4. Do not over-edit names; verify spellings against source materials.
5. Flag legal uncertainty explicitly with `[VERIFY]` and list what must be checked.
6. Include conflict and confidentiality posture before legal merits.

## Guidelines

1. Keep tone internal and professional; no legal advice or counseling recommendations.
2. Include at least one explicit urgency classification: `Immediate`, `This Week`, `Routine`.
3. If any potential statute-of-limitations or filing deadlines are mentioned, include governing trigger rule + `[VERIFY]` jurisdiction-specific requirement.
4. Do not fabricate missing timelines; request them in Follow-Up Queue.
5. Maintain strict confidentiality; avoid unnecessary sensitive disclosures in shared summaries.
6. For corporate governance matters, explicitly capture entity authority limits, board/committee roles, and document governance references.
7. End with a concise recommendation line: `Recommended assignment owner`, `recommended first filing/production task`, and `estimated start date`.
