---
name: medical-billing-audit
description: Audits medical billing records for accuracy, identifies overcharges, duplicate billing, and coding errors. Cross-references against treatment records and fee schedules.
tags:
  - medical-billing
  - audit
  - personal-injury
  - healthcare
---

# Medical Billing Audit

Audits medical bills for accuracy and identifies billing errors.

## Prerequisites

1. **Medical bills** — itemized bills from all providers in vault
2. **Treatment records** — to verify services rendered
3. **Fee schedules** — Medicare rates or usual/customary rates for comparison

## Workflow

### 1. Extract
OCR if needed. Parse: date, CPT/HCPCS code, description, charge. Group by provider/date.

### 2. Verify
Per charge: confirm service was rendered (documented in records), verify code matches service, identify duplicates.

### 3. Compare Rates
Compare against Medicare fee schedule. Flag charges >200% of Medicare. Note charges without standard codes.

### 4. Report
Summary: total billed, issues found, adjusted total. Line-item detail per flag. Categories: duplicates, upcoding, unbundling, no documentation, excessive.

## Pitfalls
- Upcoding is subtle — 99214 vs 99213 is a common inflation tactic
- Unbundling — billing components separately when bundled code exists
- Don't challenge everything — flagging legitimate charges undermines credibility
- In PI cases, lien amount often matters more than billed amount
