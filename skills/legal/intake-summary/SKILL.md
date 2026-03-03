---
name: intake-summary
description: >-
  Produces a structured, source-cited U.S. corporate client intake summary
  from forms, consultation notes, and initial communications. Trigger when
  the user requests a client intake summary, new matter onboarding overview,
  or corporate governance intake write-up.
tags:
  - corporate
  - summarization
  - summary
---

# Client Intake Summary (Corporate)

Convert raw intake materials into a structured, source-cited matter overview for initial attorney review. Scoped to U.S. corporate governance.

## Quick Start

Gather before generating:

- **Intake materials** — forms, notes, emails, attachments
- **Client identifiers** — legal name, entity type (if available)
- **Matter scope** — corporate governance or related issue
- **Jurisdiction signals** — state(s) of formation, operations, or dispute nexus

## Core Workflow

1. **Build source map** — Assign each document a Source ID (e.g., `INTAKE-01`, `EMAIL-2025-03-15`). List in the Source Map table.
2. **Extract facts into template sections** — Tag every factual statement with `(Source: {ID/page/line})`. Mark gaps as `Unknown`.
3. **Flag risks and gaps** — Surface inconsistencies, missing authority, unrealistic expectations, and conflicts-check status in the Risks section.
4. **Generate follow-ups** — Convert each `Unknown` and each risk flag into a specific follow-up question.
5. **Draft next steps** — List immediate actions (conflicts check, document requests, engagement letter, etc.).

## Output Template

```
# Executive Overview
2–3 sentences: issue, client objective, urgency. Include source tags.

# Client Profile
| Field | Details | Source |
|---|---|---|
| Legal name | | |
| Entity type | | |
| Formation state | | |
| Primary contacts | | |
| Preferred communication | | |
| Language/access needs | | |
| Key stakeholders | | |

# Matter Description
| Topic | Details | Source |
|---|---|---|
| Issue summary | | |
| Key parties | | |
| Client objectives | | |
| Business context | | |
| Prior actions taken | | |
| Documents referenced | | |

# Timeline of Key Events
| Date (YYYY-MM-DD) | Event | Source |
|---|---|---|
| | | |

# Preliminary Legal Considerations
- Areas implicated:
- Jurisdiction questions:
- Governance instruments (bylaws, charter, operating agreement):
- Deadlines / time sensitivity:
- Conflicts check status:

# Financial Discussions
| Item | Details | Source |
|---|---|---|
| Fee structure | | |
| Retainer amount | | |
| Budget constraints | | |
| Billing preferences | | |

# Risks / Red Flags
- Inconsistencies or credibility issues:
- Unclear authority or standing:
- Complexity indicators:
- Unrealistic expectations:

# Follow-Up Questions
-
-

# Immediate Next Steps
-
-

# Source Map
| Source ID | Description | Date | Notes |
|---|---|---|---|
| | | | |
```

## Pitfalls and Checks

- **No unsourced facts** — every claim cites a source; unsourced paraphrase is not acceptable.
- **Neutral tone** — no advocacy or conclusions beyond what sources support.
- **Verify spellings** — entity names and dates must match source documents exactly.
- **Non-U.S. issues** — if foreign jurisdiction surfaces, label as jurisdictional uncertainty; do not analyze.
- **Conflicts** — flag potential conflicts and urgency without assuming outcomes.

---

Key changes from the original:

- **Description** — tightened to third-person with explicit trigger guidance; removed "Trigger keywords" list in favor of natural trigger phrasing.
- **Prerequisites → Quick Start** — renamed and condensed to a bullet list.
- **Added Core Workflow** — 5 clear numbered steps that were previously implied but never spelled out (build source map first, extract, flag, follow-up, next steps).
- **Output Template** — preserved all tables and sections but trimmed redundant headers ("Output Structure / Process" → "Output Template") and removed the instruction paragraph that restated what the workflow already covers.
- **Guidelines → Pitfalls and Checks** — renamed per best practices; condensed 6 bullets to 5 tighter ones without losing any rule.

Want me to retry writing the file, or would you like to copy this directly?
