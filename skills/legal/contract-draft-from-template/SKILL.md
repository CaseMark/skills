---
name: contract-draft-from-template
description: Drafts contracts by populating approved template terms with deal-specific information. Handles variable substitution, clause selection, and generates review-ready drafts.
tags:
  - contracts
  - drafting
  - automation
---

# Contract Draft from Template

Generates contract drafts by combining approved templates with deal-specific parameters.

## Prerequisites

1. **Approved template** — base contract with placeholder fields, stored in vault
2. **Deal parameters** — counterparty, effective date, term, governing law, deal-specific terms
3. **Clause library** — alternative clauses for conditional inclusion
4. **Approval matrix** — which template versions are current and approved

## Workflow

### 1. Select Template
Match request to correct template by: contract type, counterparty type, jurisdiction, deal size.

### 2. Populate Variables
Fill: party names/addresses, effective date, term/renewal, governing law, payment terms, liability cap.

### 3. Conditional Clauses
- Include IP assignment only for development agreements
- Add DPA if counterparty handles personal data
- Include non-compete only where enforceable by jurisdiction
- Adjust indemnification by deal risk tier

### 4. Generate and Store
Produce clean draft. Store in vault with metadata: template version, parameters used, timestamp. Flag unfilled fields with `[TO BE COMPLETED]`.

## Pitfalls
- Always pull current approved template version — never use cached copies
- Mark unfilled fields explicitly — never leave blanks
- Don't auto-select governing law if not specified — flag for human decision
- Record which template version was used for audit trail
