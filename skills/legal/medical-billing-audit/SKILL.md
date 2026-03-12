---
name: medical-billing-audit
description: Audits medical billing records for accuracy, identifies overcharges, duplicate billing, and coding errors. Cross-references charges against treatment records and standard fee schedules. Use when reviewing medical bills for personal injury litigation, insurance disputes, or healthcare compliance.
tags:
  - medical-billing
  - audit
  - personal-injury
  - healthcare
---

# Medical Billing Audit

Audits medical bills for accuracy and identifies billing errors or overcharges.

## Prerequisites

1. **Medical bills** — itemized bills from all providers, uploaded to vault
2. **Treatment records** — corresponding medical records to verify services were rendered
3. **Fee schedules** — Medicare/Medicaid rates or jurisdictional usual and customary rates for comparison

## Workflow

### 1. Extract and Organize Bills

- OCR bills if needed
- Parse line items: date, CPT/HCPCS code, description, charge amount
- Group by provider and date of service

### 2. Cross-Reference with Records

For each billed service:
- Verify the service was actually rendered (documented in treatment records)
- Check that the billing code matches the service described
- Identify duplicate charges for the same service

### 3. Rate Comparison

- Compare charges against Medicare fee schedule for the geographic area
- Flag charges exceeding 200% of Medicare rates as potential overcharges
- Note any charges without standard billing codes

### 4. Produce Audit Report

- Summary: total billed, total issues found, adjusted total
- Line-item detail for each flagged charge with reason
- Categories: duplicates, upcoding, unbundling, no supporting documentation, excessive charges
- Store in vault linked to the matter

## Pitfalls

- **Upcoding is subtle** — a provider billing 99214 (moderate visit) vs. 99213 (low visit) is a common inflation tactic
- **Unbundling** — billing components separately when a bundled code exists inflates totals
- **Don't challenge everything** — flagging legitimate charges alongside real errors undermines credibility
- **Lien amounts matter** — in PI cases, the lien amount (not billed amount) is often what matters for damages
