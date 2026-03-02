---
name: reconciling-accounts
description: Reconciles financial accounts across multiple data sources, identifying breaks, aging unresolved items, and producing exception reports with root cause analysis. Use when performing daily cash reconciliation, month-end account reconciliation, or investigating balance discrepancies.
tags:
  - operations
  - accounting
  - reconciliation
metadata:
  author: casemark
  practice_areas:
    - Accounting
    - Operations
  document_types:
    - Reconciliation Report
  skill_modes:
    - Reconciliation
---

# Reconciling Accounts

Produces structured reconciliation reports from multiple data sources.

## Workflow

1. **Import** data sources — GL, bank statements, custodian reports, sub-ledgers
2. **Match** transactions — automated matching on key fields
3. **Identify** breaks — unmatched items, amount differences, timing differences
4. **Classify** breaks — timing (will self-clear) vs. real (needs investigation)
5. **Age** outstanding items — track days unresolved
6. **Investigate** root causes for recurring or large breaks

## Output Template

```markdown
## Account Reconciliation: [Account Name] — [Date]

### Summary
| Metric | Value |
|--------|-------|
| Source A Balance | |
| Source B Balance | |
| Difference | |
| Matched Items | [Count / Amount] |
| Unmatched Items | [Count / Amount] |

### Reconciliation
| Category | Amount |
|----------|--------|
| Source A Balance | |
| + Items in A not in B | |
| - Items in B not in A | |
| = Source B Balance | |

### Unmatched Items
| Date | Reference | Description | Source | Amount | Age (Days) | Category |
|------|-----------|-------------|--------|--------|-----------|----------|

### Aging Summary
| Age Bucket | Count | Amount |
|-----------|-------|--------|
| 0-3 days | | |
| 4-7 days | | |
| 8-30 days | | |
| 31-60 days | | |
| 60+ days | | |

### Root Cause Analysis (for items >30 days)
| Item | Root Cause | Responsible Party | Resolution Plan |
|------|-----------|-------------------|----------------|

### Certification
Prepared by: ___ | Reviewed by: ___ | Date: ___
```

## Key Rules

- Timing differences (float, processing lag) are expected — classify them, don't investigate them
- Stale items (>30 days) require escalation and root cause analysis
- Three-way reconciliation for custody accounts (books vs. custodian vs. counterparty)
- Dollar thresholds for investigation should be documented in policy
- Reconciliation must be performed by someone independent of transaction processing
- Month-end: all material reconciling items must be cleared or explained

For matching algorithms and tolerance rules, see [references/RECONCILIATION-RULES.md](references/RECONCILIATION-RULES.md).
