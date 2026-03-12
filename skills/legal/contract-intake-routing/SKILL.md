---
name: contract-intake-routing
description: >-
  Classifies incoming contract requests by type, risk level, and complexity,
  then routes them to the appropriate approval workflow. Enables business teams
  to self-serve low-risk agreements while escalating complex deals to legal.
  Use when building or optimizing a legal intake process.
tags:
  - corporate
  - checklist
  - analysis
---

# Contract Intake Routing

Triages incoming contract requests and routes them through the correct approval path based on contract type, value, and risk profile.

## Prerequisites

- Contract request details (type, counterparty, estimated value, business owner)
- Organization's contract type taxonomy and risk thresholds
- Defined approval workflows per contract category

## Workflow

### 1. Classify Contract Type

Determine the contract category: NDA, MSA, SOW, SaaS subscription, vendor agreement, employment agreement, partnership, amendment, or renewal. Map to the organization's taxonomy.

### 2. Assess Risk Tier

Score the request against risk factors: contract value, counterparty type (enterprise/SMB/government), data handling requirements, regulatory implications, non-standard terms requested, and jurisdiction complexity. Assign Low/Medium/High risk tier.

### 3. Route to Workflow

- **Low risk + standard template**: Auto-generate from template, route to business owner for execution. No legal review needed.
- **Medium risk**: Generate from template with legal review checkpoint. Route to assigned counsel.
- **High risk or non-standard**: Full legal review. Route to senior counsel with complete context package.

### 4. Generate Context Package

For routed contracts, compile: request summary, counterparty background, relevant precedent contracts, applicable playbook positions, and flagged risk factors.

### 5. Track and Report

Log every request with: submission date, classification, assigned workflow, current status, and time-to-completion. Generate weekly throughput reports.

## Pitfalls

- Routing all contracts through legal review regardless of risk wastes counsel time
- Allowing self-serve on contract types that require jurisdiction-specific modifications
- Not updating routing rules when organizational risk thresholds change
