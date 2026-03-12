---
name: contract-draft-from-template
description: Drafts contracts by populating approved template terms with deal-specific information. Handles variable substitution, clause selection based on deal parameters, and generates review-ready drafts. Use when automating contract generation, building self-service contracting portals, or scaling legal document production.
tags:
  - contracts
  - drafting
  - automation
---

# Contract Draft from Template

Generates contract drafts by combining approved templates with deal-specific parameters.

## Prerequisites

1. **Approved template** — the base contract template with placeholder fields, stored in vault
2. **Deal parameters** — counterparty name, effective date, term length, governing law, deal-specific terms
3. **Clause library** — optional alternative clauses for conditional inclusion (e.g., different IP assignment clauses by deal type)
4. **Approval matrix** — which template versions are current and approved for use

## Workflow

### 1. Select Template

Match the request to the correct template based on:
- Contract type (NDA, MSA, SaaS agreement, consulting, employment)
- Counterparty type (vendor, customer, partner)
- Jurisdiction and governing law requirements
- Deal size thresholds that trigger different template versions

### 2. Populate Variables

Standard fields to extract and fill:

| Variable | Source |
|---|---|
| Party names & addresses | Requester input or CRM |
| Effective date | Deal timeline |
| Term & renewal | Deal parameters |
| Governing law & venue | Jurisdiction rules |
| Payment terms | Finance/deal terms |
| Liability cap | Deal size × company policy |

### 3. Conditional Clauses

Select or omit clauses based on deal parameters:
- Include IP assignment clause only for development agreements
- Add data processing addendum if counterparty handles personal data
- Include non-compete only where enforceable by jurisdiction
- Adjust indemnification scope based on deal risk tier

### 4. Generate & Store

- Produce clean draft in standard format (Word/PDF)
- Store in vault with metadata: template version, deal parameters used, generation timestamp
- Flag any fields that couldn't be auto-populated for human review

## Pitfalls

- **Never use stale templates** — always pull the current approved version from vault at generation time
- **Mark unfilled fields** — use `[TO BE COMPLETED]` for any field that couldn't be populated, never leave blanks
- **Don't auto-select jurisdiction** — if governing law isn't specified in the request, flag for human decision
- **Version tracking** — record which template version was used; if the template updates mid-negotiation, flag the discrepancy
