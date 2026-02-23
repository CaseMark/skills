---
name: track-deposits
description: Analyzes bank statements and financial records to trace deposits from receipt through disbursement, constructing chronological timelines, transaction matrices, and evidentiary chains of custody. Flags structuring, commingling, trust account violations, and unexplained gaps. Use when tracking deposits, tracing funds, auditing trust accounts, or analyzing bank statements during discovery.
tags:
  - analysis
  - litigation
---

# Forensic Deposit Tracking & Fund Tracing

Traces every dollar from initial deposit through final disbursement, producing a defensible evidentiary record suitable for expert testimony, settlement negotiation, or regulatory proceedings.

## Prerequisites

1. **Bank statements** — all accounts, all relevant periods, no gaps
2. **Transaction registers** — internal ledgers, check registers, reconciliation reports
3. **Supporting documents** — wire confirmations, check images, ACH records, invoices
4. **Governing documents** — retainer agreements, settlement agreements, court orders, fee arrangements
5. **Matter timeline** — key dates (filing, settlement, court-ordered deadlines, statutes of limitation)

## Process

### Phase 1: Deposit Extraction

For every deposit, capture:

| Field | Detail |
|-------|--------|
| Date | Exact date of receipt |
| Amount | To the cent |
| Source/Payor | Identified sender |
| Receiving Account | Account name + number |
| Reference | Check #, wire confirmation, ACH trace, memo line |
| Method | Check, wire, ACH, cash, other |

### Phase 2: Red Flag Screening

Flag deposits matching any pattern:

- [ ] Round-number amounts suggesting structuring
- [ ] Amounts just below $10,000 CTR threshold
- [ ] Unusual timing relative to case events
- [ ] Unexpected or unrelated sources
- [ ] Patterns suggesting commingling of segregated funds
- [ ] Circular transfers indicating potential laundering
- [ ] Deposits without identifiable source documentation

### Phase 3: Forward Tracing

For each deposit, trace funds forward through:

1. **Holding** — static in original account
2. **Internal transfers** — moved between accounts at same institution
3. **External transfers** — wire/ACH to outside accounts
4. **Disbursements** — paid to third parties

Document each disbursement with equal rigor:

| Field | Detail |
|-------|--------|
| Date | Disbursement date + clearing date |
| Payee | Recipient name |
| Amount | Exact amount |
| Method | Check # (cleared date), wire (confirmation #), ACH (transaction ID), cash (supporting docs) |
| Purpose | From memo, invoice, settlement terms, or authorization |
| Authorization | Governing document authorizing payment |

Classify disbursements:
- Client payments
- Third-party payments on client's behalf
- Operating account transfers
- Case expense payments
- Other (specify)

### Phase 4: Lifecycle Timeline

For each deposit, construct:

```
[Deposit Date] → [Holding Period] → [Transfer/Partial Withdrawal] → [Final Disbursement / Current Status]
```

Cross-reference against governing documents to establish authorization and legitimacy.

### Phase 5: Trust Account Compliance Check

- [ ] No commingling of client funds with firm operating funds
- [ ] No use of client funds for firm expenses or other clients
- [ ] Sufficient balances maintained to cover all client obligations
- [ ] Prompt disbursement to entitled recipients
- [ ] Disbursements within authorized amounts and timing
- [ ] No payments to prohibited recipients
- [ ] No violations of court orders or settlement terms

### Phase 6: Gap Analysis

Document separately:

- Deposits with no traceable disbursement
- Disbursements exceeding identified deposits
- Missing statements for any period
- Discrepancies between bank records and internal ledgers
- Timing anomalies relative to limitation periods, contractual deadlines, or court schedules

## Output Format

### Transaction Matrix

Chronological table with columns:

| Deposit Date | Source | Amount | Receiving Acct | Disbursement Date | Payee | Method | Purpose | Source Doc Ref |
|---|---|---|---|---|---|---|---|---|

### Narrative Analysis

1. Overall fund flow summary
2. Significant patterns or anomalies
3. Identified legal violations or concerns
4. Conclusions on record completeness and integrity

### Untraced Funds Report

For each unresolved deposit: amount, efforts made, records needed to complete tracing.

## Guidelines

- Cite every assertion to a specific source document (name, page, transaction line)
- Disclose all record gaps and their impact on conclusions
- Do not speculate beyond what records support — state what additional records would resolve ambiguities
- Structure analysis to anticipate cross-examination questions about fund movement
- Note jurisdiction-specific trust account rules where applicable
- Mark any uncertain statutory or regulatory citations with [VERIFY]
