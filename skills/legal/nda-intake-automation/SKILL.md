---
name: nda-intake-automation
description: Automates end-to-end NDA processing from intake request through drafting, review, negotiation, and execution tracking.
tags:
  - transactional
  - agreement
  - drafting
---

# NDA Intake Automation

Processes NDAs end-to-end from intake through execution.

## Prerequisites

1. **NDA request** — who needs it, counterparty details, purpose, type (mutual vs. one-way)
2. **NDA templates** — approved mutual and one-way templates in vault
3. **Company standards** — acceptable terms, fallbacks, non-negotiables
4. **Signing authority** — who can execute by deal size/type

## Workflow

### 1. Intake
Extract: requester/department, counterparty name/jurisdiction/contact, purpose, direction (mutual, one-way disclosing, one-way receiving), non-standard terms, deadline.

### 2. Route
- Standard mutual, no special terms → auto-generate, send for signature
- Company paper with custom terms → generate draft, flag for review
- Counterparty paper → route to redline review
- Non-standard structure → escalate to legal

### 3. Generate or Review
**Company paper:** populate template → store in vault → approve if needed → send.
**Counterparty paper:** upload to vault → redline review → negotiate if needed.

### 4. Track Execution
Monitor signature status. Send reminders. Log execution date. Store executed copy. Set expiration/renewal reminder.

## Pitfalls
- Check for existing NDAs with the same counterparty before generating new ones
- Governing law affects enforceability of non-solicitation/non-compete provisions
- Agent prepares and tracks — humans sign
- Track expiration for fixed-term NDAs; set review reminders for perpetual ones
