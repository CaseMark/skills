---
name: contract-negotiation-automation
description: Automates contract negotiation rounds by tracking counterparty redlines, generating responses based on company playbook positions, and managing the back-and-forth exchange. Use when scaling contract negotiation capacity, reducing legal bottleneck on routine negotiations, or building autonomous negotiation agents.
tags:
  - contracts
  - negotiation
  - automation
---

# Contract Negotiation Automation

Manages multi-round contract negotiations by applying company playbook positions to counterparty redlines.

## Prerequisites

1. **Company playbook** — acceptable positions, fallback positions, and walk-away terms for each clause type
2. **Incoming redline** — counterparty's marked-up version of the contract
3. **Original draft** — the version sent to the counterparty
4. **Authority matrix** — which concessions the agent can make autonomously vs. what requires human approval

## Workflow

### 1. Analyze Counterparty Redlines

For each change in the counterparty markup:
- Classify as: editorial (accept), minor commercial (auto-respond), material (flag), or non-starter (escalate)
- Map each change to the relevant playbook section
- Score overall deviation from company standard position

### 2. Apply Playbook Responses

| Counterparty Position | Playbook Response |
|---|---|
| Within acceptable range | Accept the change |
| Outside acceptable but within fallback | Counter with fallback position |
| Beyond fallback range | Escalate to human with recommendation |
| Non-starter term | Reject with standard explanation language |

### 3. Generate Response Markup

- Accept editorial changes silently
- Counter substantive changes with playbook language
- Add explanatory comments for material counters
- Produce clean redline showing the agent's responses

### 4. Track Negotiation State

Maintain per-negotiation record:
- Round number and date
- Changes accepted, countered, escalated per round
- Cumulative concessions made
- Estimated distance to agreement

### 5. Close or Escalate

- If all terms resolved → generate execution-ready version
- If stalled after N rounds → escalate with negotiation summary
- If walk-away threshold triggered → flag for human decision

## Pitfalls

- **Never concede beyond playbook authority** — if the playbook doesn't cover a term, escalate rather than guess
- **Track cumulative concessions** — individual concessions may be acceptable but the aggregate may not be
- **Preserve negotiation history** — every round's redline goes to vault; never overwrite prior versions
- **Don't negotiate non-legal terms** — pricing, scope, timeline changes get routed back to the business owner
