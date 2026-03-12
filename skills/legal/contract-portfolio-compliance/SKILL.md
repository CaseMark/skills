---
name: contract-portfolio-compliance
description: Analyzes entire contract portfolios against regulatory requirements or policy standards. Identifies non-compliant terms across hundreds of contracts and prioritizes remediation. Use when conducting portfolio-wide compliance sweeps, regulatory change impact assessments, or contract standardization initiatives.
tags:
  - compliance
  - contracts
  - portfolio-analysis
---

# Contract Portfolio Compliance

Scans contract portfolios for compliance with regulatory requirements or internal standards.

## Prerequisites

1. **Contract portfolio** — all active contracts uploaded to vault
2. **Compliance standard** — the specific regulation, policy, or standard to check against (e.g., GDPR data processing requirements, new regulatory mandate, updated company policy)
3. **Remediation authority** — who can approve contract amendments or waivers

## Workflow

### 1. Define Compliance Criteria

- Translate the regulation/policy into specific contractual requirements
- Example: GDPR → need data processing addendum, sub-processor controls, breach notification clause, data deletion rights
- Create a checklist of required, recommended, and prohibited terms

### 2. Bulk Contract Analysis

For each contract in the portfolio:
- Check for presence/absence of required clauses
- Flag prohibited terms
- Score compliance: compliant, partially compliant, non-compliant
- Extract relevant clause text for review

### 3. Prioritize Remediation

| Priority | Criteria |
|---|---|
| Urgent | High-value contracts with prohibited terms or missing critical clauses |
| High | Contracts up for renewal soon — fix during renewal |
| Medium | Partially compliant — minor updates needed |
| Low | Low-value or soon-expiring contracts |

### 4. Produce Compliance Report

- Portfolio dashboard: % compliant by category
- Non-compliant contracts list with specific gaps
- Remediation plan with recommended actions per contract
- Template amendment language for common fixes

## Pitfalls

- **Don't boil the ocean** — prioritize by contract value and risk, not alphabetical order
- **Grandfathering** — some regulations exempt existing contracts; check transition provisions
- **Amendment vs. new agreement** — sometimes it's cheaper to wait for renewal than force an amendment
- **Track remediation** — a compliance report without follow-through is just documentation of failure
