---
name: nda-intake-automation
description: Automates end-to-end NDA processing from initial intake request through drafting, review, negotiation, and execution tracking. Handles both company-paper and counterparty-paper NDAs with appropriate workflows. Use when scaling NDA processing, reducing turnaround time on routine confidentiality agreements, or building self-service NDA portals.
tags:
  - nda
  - intake
  - automation
  - contracts
---

# NDA Intake Automation

Processes NDAs end-to-end from intake request through execution.

## Prerequisites

1. **NDA request** — who needs it, counterparty details, purpose, type (mutual vs. one-way)
2. **NDA templates** — approved mutual and one-way NDA templates in vault
3. **Company standards** — acceptable terms, fallback positions, non-negotiable clauses
4. **Signing authority** — who can execute NDAs by deal size/type

## Workflow

### 1. Intake

Extract from request:
- Requester and department
- Counterparty name, jurisdiction, contact
- Purpose of disclosure
- Direction: mutual, one-way (disclosing), one-way (receiving)
- Any non-standard terms requested
- Deadline

### 2. Route by Type

| Scenario | Action |
|---|---|
| Standard mutual NDA, no special terms | Auto-generate from template, send for signature |
| Company-paper with custom terms | Generate draft, flag custom terms for review |
| Counterparty paper | Route to redline review workflow |
| Non-standard structure | Escalate to legal team |

### 3. Generate or Review

**Company paper:** Populate template with deal parameters → store draft in vault → route for approval if needed → send to counterparty.

**Counterparty paper:** Upload to vault → run contract redline review → generate response markup → enter negotiation workflow if needed.

### 4. Track Execution

- Monitor signature status
- Send reminders at configurable intervals
- Log execution date and store fully executed copy in vault
- Set calendar reminder for expiration/renewal

## Pitfalls

- **Check for existing NDAs** — search vault before generating a new one; there may be a current NDA with the same counterparty
- **Jurisdiction matters** — governing law selection affects enforceability of non-solicitation and non-compete provisions often bundled in NDAs
- **Don't auto-execute** — even routine NDAs need human signature; the agent prepares and tracks, humans sign
- **Track expiration** — NDAs with fixed terms need renewal tracking; perpetual NDAs need periodic review reminders
