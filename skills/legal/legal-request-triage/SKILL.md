---
name: legal-request-triage
description: Triages and routes incoming legal requests from business teams to the appropriate legal specialist or workflow. Classifies request type, assigns urgency, and creates structured intake records.
tags:
  - legal-ops
  - intake
  - routing
---

# Legal Request Triage

Classifies, prioritizes, and routes incoming legal requests from business teams.

## Prerequisites

1. **Incoming request** — email, form, or message describing what the business user needs
2. **Legal team directory** — who handles what (contracts, compliance, IP, employment, litigation)
3. **Routing rules** — request types mapped to team members or queues

## Workflow

### 1. Parse the Request
Extract: requester name/department, request type, counterparty, deadline, attachments. Upload attachments to vault.

### 2. Classify
Map to categories: Contract (draft/review/amendment), Compliance (regulatory/policy), IP, Employment, Litigation, General.

### 3. Prioritize
- **Critical** — regulatory deadline <24h, active litigation, data breach
- **High** — contract deadline <1 week, executive request
- **Standard** — routine reviews, policy questions
- **Low** — informational, no time pressure

### 4. Route
Auto-assign to designated specialist. Create structured intake record. Notify requester with expected response time. Escalate to legal ops lead if no clear match.

## Pitfalls
- Don't guess jurisdiction — flag cross-border issues for human classification
- Don't assume urgency from tone — analyze actual deadlines
- Confirm ambiguous requests before routing
- Preserve original message verbatim in vault alongside structured record
