---
name: contract-negotiation-automation
description: Automates contract negotiation rounds by tracking counterparty redlines, generating responses based on company playbook positions, and managing the exchange.
tags:
  - contracts
  - negotiation
  - automation
---

# Contract Negotiation Automation

Manages multi-round contract negotiations by applying playbook positions to counterparty redlines.

## Prerequisites

1. **Company playbook** — acceptable, fallback, and walk-away positions per clause type
2. **Incoming redline** — counterparty's marked-up version
3. **Original draft** — version sent to counterparty
4. **Authority matrix** — which concessions the agent can make vs. what needs human approval

## Workflow

### 1. Analyze Redlines
Classify each change: editorial (accept), minor commercial (auto-respond), material (flag), non-starter (escalate). Map to playbook sections.

### 2. Apply Playbook
- Within acceptable range → accept
- Outside acceptable but within fallback → counter with fallback language
- Beyond fallback → escalate with recommendation
- Non-starter → reject with standard explanation

### 3. Generate Response
Accept editorial changes silently. Counter substantive changes with playbook language. Add comments for material counters. Produce clean redline.

### 4. Track State
Record: round number, changes accepted/countered/escalated, cumulative concessions, distance to agreement.

## Pitfalls
- Never concede beyond playbook authority — escalate unknowns
- Track cumulative concessions — individually acceptable changes may be unacceptable in aggregate
- Preserve every round's redline in vault
- Don't negotiate non-legal terms (pricing, scope) — route to business owner
