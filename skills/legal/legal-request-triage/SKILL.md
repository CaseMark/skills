---
name: legal-request-triage
description: Triages and routes incoming legal requests from business teams to the appropriate legal specialist or workflow. Classifies request type, assigns urgency, and creates structured intake records. Use when building legal intake automation, request routing agents, or legal ops ticketing systems.
tags:
  - legal-ops
  - intake
  - routing
---

# Legal Request Triage

Classifies, prioritizes, and routes incoming legal requests from business teams to the right legal resource.

## Prerequisites

1. **Incoming request** — email, form submission, or chat message describing what the business user needs
2. **Legal team directory** — who handles what (contracts, compliance, IP, employment, litigation)
3. **Routing rules** — which request types go to which team members or queues
4. **Escalation thresholds** — what triggers immediate human review vs. automated handling

## Workflow

### 1. Parse the Request

Extract from the incoming message:

| Field | Example |
|---|---|
| Requester | Name, department, role |
| Request type | NDA review, policy question, contract approval, litigation hold |
| Counterparty | If applicable — company name, jurisdiction |
| Deadline | Explicit or implied urgency |
| Attachments | Contracts, policies, correspondence |

Upload any attachments to vault for downstream processing.

### 2. Classify

Map to standard categories:

- **Contract** — new draft, review, amendment, renewal, termination
- **Compliance** — regulatory question, policy interpretation, audit support
- **IP** — trademark, patent, trade secret, licensing
- **Employment** — hiring, termination, accommodation, dispute
- **Litigation** — hold notice, discovery, subpoena response
- **General** — catch-all for unclassified requests

### 3. Prioritize

| Priority | Criteria |
|---|---|
| Critical | Regulatory deadline <24h, active litigation, data breach |
| High | Contract deadline <1 week, executive request |
| Standard | Routine reviews, policy questions, no hard deadline |
| Low | Informational, future planning, no time pressure |

### 4. Route

Based on classification + priority:
- Auto-assign to the designated specialist per routing rules
- If no clear match, escalate to legal ops lead
- Create structured intake record with all extracted fields
- Notify the requester with expected response time

## Pitfalls

- **Don't guess jurisdiction** — if cross-border issues, flag for human classification
- **Don't assume urgency from tone** — "URGENT" in subject doesn't override actual deadline analysis
- **Always confirm ambiguous requests** — if it could be two categories, ask before routing
- **Preserve original message** — store verbatim in vault alongside structured intake record
