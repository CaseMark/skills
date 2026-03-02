---
name: reconciling-medications
description: Reconciles medication lists from multiple sources to produce a unified, verified medication list with discrepancies flagged and resolved. Use when performing admission or discharge medication reconciliation, consolidating pharmacy records, or verifying medication accuracy across care settings.
tags:
  - operations
  - patient-safety
  - medication-management
metadata:
  author: casemark
  practice_areas:
    - Pharmacy
    - Hospital Medicine
  document_types:
    - Medication Reconciliation
  skill_modes:
    - Reconciliation
---

# Reconciling Medications

Produces a single verified medication list from multiple sources.

## Workflow

1. **Collect** all medication lists — patient-reported, pharmacy records, EHR, referring provider
2. **Normalize** — generic names, standardized dosing notation
3. **Compare** across sources — identify matches, additions, omissions, discrepancies
4. **Classify** discrepancies — intentional change vs. error vs. unclear
5. **Resolve** — verify with patient/provider; document resolution
6. **Output** reconciled list with provenance

## Output Template

```markdown
## Medication Reconciliation

### Sources Compared
| Source | Date | Medications Listed |
|--------|------|--------------------|

### Reconciled Medication List
| Medication | Dose | Route | Frequency | Source(s) | Status |
|-----------|------|-------|-----------|-----------|--------|

### Discrepancies Found
| # | Medication | Discrepancy | Source A Says | Source B Says | Resolution |
|---|-----------|-------------|-------------|-------------|------------|

### Unresolved Items (Require Verification)
| Medication | Issue | Action Needed |
|-----------|-------|--------------|

### Duplicate Therapy Check
- [Medications in same therapeutic class]

### High-Alert Medications
- [Anticoagulants, insulins, opioids, etc. flagged for extra verification]
```

## Key Rules

- Patient-reported "nothing changed" is never sufficient — verify against records
- High-alert medications (ISMP list) require extra verification steps
- OTC medications, supplements, and herbals must be included
- PRN medications are frequently missed — ask specifically
- Always document the resolution of each discrepancy, not just the final list
- Allergy list reconciliation should accompany medication reconciliation

For high-alert medication categories, see [references/HIGH-ALERT-MEDS.md](references/HIGH-ALERT-MEDS.md).
