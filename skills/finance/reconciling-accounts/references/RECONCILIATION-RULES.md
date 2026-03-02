# Reconciliation Matching Rules and Tolerances

## Matching Strategies

### Exact Match
Match on: exact amount + exact date + exact reference number
- **Use when**: Matching internal GL to bank transactions where reference numbers are captured
- **Match rate**: Typically 60-80% of transactions

### Amount Match (with date tolerance)
Match on: exact amount + date within ±3 business days
- **Use when**: No common reference number; timing differences expected
- **Match rate**: Adds 10-15% to match rate

### Fuzzy Amount Match
Match on: amount within tolerance band + date within window
- **Use when**: Rounding differences, FX conversion, fee variations
- **Tolerance**: Typically ±$0.01 to ±$1.00 (policy-defined)

### One-to-Many Match
Match one transaction against multiple offsetting transactions
- **Use when**: Batched deposits, settlement netting, split payments
- **Example**: One bank deposit = sum of 5 individual receivable payments

### Many-to-Many Match
Match groups of transactions on both sides
- **Use when**: Complex netting, intercompany settlements
- **Requires**: Manual review after initial algorithm

## Tolerance Thresholds by Account Type

| Account Type | Amount Tolerance | Date Tolerance | Auto-Clear? |
|-------------|-----------------|---------------|-------------|
| Cash/Bank | $0.00 | ±3 business days | Yes (timing only) |
| Brokerage/Custody | $0.01 | ±1 business day | Yes if within tolerance |
| Intercompany | $0.00 | ±5 business days | No — always review |
| Accounts Receivable | $1.00 | ±10 business days | Yes if within tolerance |
| Fixed Assets | $0.00 | N/A | No — always review |
| Payroll | $0.05 | ±1 business day | Yes if within tolerance |

## Break Classification

| Type | Definition | Expected Resolution | Aging Alert |
|------|-----------|-------------------|-------------|
| **Timing** | Transaction in one system, not yet in other | Self-clears within settlement cycle | 5 business days |
| **Amount** | Same transaction, different amounts | Investigation required | 3 business days |
| **Missing** | Transaction in one system, absent in other | Research/journal entry | 3 business days |
| **Duplicate** | Same transaction recorded twice | Reversal entry | 1 business day |
| **Mispost** | Correct amount, wrong account | Reclassification entry | 3 business days |

## Escalation Matrix

| Break Age | Break Size | Action |
|----------|-----------|--------|
| 0-3 days | Any | Standard research |
| 4-7 days | < $1,000 | Team lead review |
| 4-7 days | > $1,000 | Manager review |
| 8-30 days | < $10,000 | Manager + root cause analysis |
| 8-30 days | > $10,000 | Director review + action plan |
| 31+ days | Any | CFO/Controller visibility; include in month-end commentary |

## Month-End Reconciliation Requirements

| Requirement | Standard |
|-------------|---------|
| Completion deadline | T+5 business days after month-end |
| Preparer/reviewer segregation | Required — different individuals |
| Documentation | Every reconciling item must have description, source, expected resolution |
| Certification | Signed by preparer and reviewer with date |
| Stale item threshold | Items > 30 days require written explanation |
| Materiality for investigation | Any individual item > $500 or aggregate > $5,000 (adjust per policy) |

## Common Root Causes

| Root Cause | Prevention |
|-----------|-----------|
| Manual entry errors | Automate transaction feeds |
| Timing (settlement lag) | Document expected settlement dates |
| FX conversion differences | Agree on rate source and timing |
| Fee/commission discrepancies | Reconcile fee schedules quarterly |
| Intercompany imbalances | Daily intercompany matching |
| System interface failures | Monitor automated feed completions |
