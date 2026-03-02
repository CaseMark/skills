---
name: processing-trade-settlements
description: Structures trade settlement workflows with instruction verification, break identification, counterparty matching, and exception management for securities transactions. Use when managing trade settlements, investigating settlement breaks, or auditing settlement processes.
tags:
  - operations
  - trading
  - settlements
metadata:
  author: casemark
  practice_areas:
    - Operations
    - Trading
  document_types:
    - Settlement Report
  skill_modes:
    - Processing
---

# Processing Trade Settlements

Manages the trade-to-settlement lifecycle.

## Workflow

1. **Capture** trade details — security, quantity, price, counterparty, settlement date
2. **Validate** instructions — SSI (Standard Settlement Instructions) verification
3. **Match** — confirm counterparty agreement on terms
4. **Monitor** — track through settlement cycle (T+1/T+2)
5. **Resolve** breaks — identify and escalate discrepancies
6. **Confirm** settlement — verify delivery vs. payment

## Output Template

```markdown
## Settlement Status Report

### Trade Summary
| Field | Value |
|-------|-------|
| Trade Date | |
| Settlement Date | |
| Security | [CUSIP/ISIN] |
| Side | [Buy/Sell] |
| Quantity | |
| Price | |
| Amount | |
| Counterparty | |
| Broker | |

### Settlement Instructions
| Field | Our Instructions | Counterparty Instructions | Match? |
|-------|-----------------|--------------------------|--------|

### Status: [Matched / Unmatched / Settled / Failed]

### Breaks (if any)
| Field | Our Record | Counterparty Record | Difference |
|-------|-----------|-------------------|------------|

### Resolution Actions
| # | Action | Owner | Status | Deadline |
|---|--------|-------|--------|----------|

### Aging
| Age (Days) | Status |
|-----------|--------|
```

## Key Rules

- T+1 settlement (US equities as of May 2024) — urgency is high
- Matching must cover: security, quantity, price, settlement date, delivery instructions
- DK (Don't Know) trades: counterparty doesn't recognize the trade — escalate immediately
- Failed settlements incur costs and regulatory reporting requirements (SEC Rule 204)
- Corporate actions (dividends, splits) during settlement period need special handling
- Cross-border settlements: time zones and cut-off times are critical
