---
name: contract-template-generator
description: >-
  Creates standardized contract templates with configurable variables, conditional
  clauses, and pre-approved fallback positions. Enables business teams to
  generate compliant first drafts without legal involvement for routine
  agreements. Use when building or updating an organization's template library.
tags:
  - transactional
  - agreement
  - drafting
---

# Contract Template Generator

Builds parameterized contract templates that allow non-legal teams to generate compliant first drafts for routine agreements.

## Prerequisites

- Organization's standard terms and preferred positions
- Contract type specifications (NDA, MSA, SOW, SaaS, vendor agreement)
- Approved clause variants and fallback positions
- Variable fields (counterparty name, term length, value thresholds)

## Workflow

### 1. Define Template Scope

Specify the contract type, typical use case, and target user (sales, procurement, HR). Identify which terms are fixed (non-negotiable), which are variable (user-selected from approved options), and which are conditional (included based on deal parameters).

### 2. Draft Core Provisions

Write each clause with the organization's preferred position as the default. For variable provisions, define the option set: e.g., governing law choices limited to approved jurisdictions, liability caps as a formula tied to contract value.

### 3. Build Conditional Logic

Define conditions that trigger clause inclusion: indemnification scope expands when contract value exceeds threshold, data processing addendum included when personal data is involved, export compliance clause added for international deals.

### 4. Create Variable Fields

Mark each configurable element: counterparty name, effective date, term length, renewal terms, fee structure, and jurisdiction. Define validation rules (e.g., term cannot exceed 36 months without legal approval).

### 5. Add Guardrails

Build escalation triggers: if the user selects a non-standard option or the deal exceeds defined thresholds, the template routes to legal review instead of generating a final document.

## Pitfalls

- Making too many fields variable, creating templates that produce inconsistent agreements
- Not updating templates when organizational standards or applicable law changes
- Allowing users to override conditional clauses that exist for regulatory compliance
