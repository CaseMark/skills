---
name: reconciling-accounts
description: Compares multiple data sources to produce reconciliation reports with break identification and aging analysis. Use when reconciling accounts, identifying breaks, or performing bank reconciliations.
tags:
  - reconciliation
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Financial Reporting
    - Audit
    - Accounting
  document_types:
    - Reconciliation Report
  skill_modes:
    - Reconciliation
---

# Reconciling Accounts

Compares multiple data sources to produce reconciliation reports with break identification and aging analysis.

## Why This Skill Exists

Account reconciliation is the foundation of financial statement integrity. Every balance on the balance sheet must be supported by verifiable detail that ties back to a source of truth — a bank statement, a sub-ledger, a counterparty confirmation, or an amortization schedule. Unreconciled or poorly reconciled accounts are a leading cause of financial restatements, audit findings, and SOX control deficiencies.

This skill exists to enforce a rigorous, repeatable process for:
- Proving that a GL balance is **complete, accurate, and valid** at a point in time.
- Surfacing **breaks** (discrepancies) with categorization and aging so they are investigated — not buried.
- Producing **audit-ready documentation** that satisfies reviewer sign-off and SOX evidence requirements.
- Reducing the close cycle by standardizing reconciliation across account types.

If you cannot reconcile an account, you cannot assert its balance is correct. Period.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before any reconciliation work begins, confirm or collect the following. Do NOT proceed with incomplete intake — mark gaps as `[MISSING]` and escalate.

| Field | Required | Description |
|---|---|---|
| **Reconciliation Type** | Yes | One of: `Bank`, `Intercompany`, `Sub-ledger to GL`, `Balance Sheet Account` |
| **Account Number(s)** | Yes | GL account(s) in scope. Include entity/company code if multi-entity. |
| **Account Name** | Yes | Descriptive name (e.g., "Chase Operating Account", "IC — Entity A to B") |
| **Period End Date** | Yes | The as-of date for the reconciliation (e.g., 2025-12-31) |
| **GL Balance** | Yes | Ending balance per the general ledger at period end |
| **Supporting Source** | Yes | The comparison source: bank statement, sub-ledger, counterparty balance, schedule |
| **Supporting Source Balance** | Yes | Ending balance per the supporting source |
| **Currency** | Yes | Functional currency. Flag if FX translation is involved. |
| **Materiality Threshold** | Yes | Dollar amount below which differences may be written off without investigation |
| **Preparer / Reviewer** | Yes | Names for evidence of segregation of duties |
| **Reconciliation Frequency** | Yes | `Daily`, `Monthly`, `Quarterly` — determines expected cadence |
| **Prior Period Carryforward Items** | If any | Unresolved items from prior reconciliation that should clear this period |

### Frequency Guidelines

| Account Type | Recommended Frequency | Rationale |
|---|---|---|
| Cash / Bank | Daily or at minimum Monthly | High volume, fraud risk, cash management |
| Intercompany | Monthly | Must net to zero at consolidation; timing differences compound |
| Accounts Receivable / Payable | Monthly | Sub-ledger aging must tie to GL |
| Prepaid Expenses | Monthly | Amortization schedules drive balance |
| Accrued Liabilities | Monthly | Estimates require fresh support each period |
| Fixed Assets / Depreciation | Monthly | Roll-forward must reconcile additions, disposals, depreciation |
| Deferred Revenue | Monthly | Revenue recognition schedule drives balance |
| Equity / Less Active BS | Quarterly | Low activity, but must still be formally reconciled |

---

## Workflow

### Step 1: Obtain and Validate GL Balance

- Pull the trial balance or GL detail for the account at the period end date.
- Confirm the balance agrees to the trial balance used for financial statement preparation.
- If the GL detail is a list of transactions, foot the detail and confirm it ties to the ending balance.
- Flag any post-close adjustments that may have been posted after the initial pull.

### Step 2: Obtain Supporting Detail

The supporting source depends on reconciliation type:

| Recon Type | Primary Supporting Source | Secondary Sources |
|---|---|---|
| Bank | Bank statement (PDF or data feed) | Cleared check images, deposit slips, bank fee schedules |
| Intercompany | Counterparty GL detail or confirmation | IC invoice log, netting schedule |
| Sub-ledger to GL | Sub-ledger trial balance or aging | Transaction detail, module reports |
| Balance Sheet Account | Supporting schedule (amortization, roll-forward, listing) | Invoices, contracts, fixed asset register |

### Step 3: Standardize and Match

- Normalize date formats, reference numbers, and amount signs across sources.
- Perform matching on one or more keys: `reference/check number`, `amount`, `date`, `description`.
- Exact matches clear automatically. Partial matches (amount match, date mismatch) require manual review.
- Document the matching methodology used.

### Step 4: Identify and Categorize Breaks

Every unmatched item is a **reconciling item**. Categorize each one:

| Category | Code | Description | Examples |
|---|---|---|---|
| Timing Difference | `TIMING` | Transaction recorded in one source but not yet in the other; expected to clear | Outstanding checks, deposits in transit, IC entries posted in different periods |
| Error — Source A | `ERR-A` | Mistake in the GL requiring correction | Duplicate posting, wrong amount, misclassification |
| Error — Source B | `ERR-B` | Mistake in the supporting source | Bank error, counterparty mis-posting |
| Missing Entry | `MISSING` | Transaction exists in one source with no corresponding entry in the other | Unrecorded bank fees, interest, NSF items, unbooked IC charges |
| Cut-off | `CUTOFF` | Transaction recorded in the wrong period | Revenue/expense recognized before or after the correct period |
| FX Translation | `FX` | Difference caused by exchange rate variance | Remeasurement differences on foreign-currency-denominated balances |
| Immaterial Write-off | `WOFF` | Difference within materiality threshold; no investigation required | Rounding, penny differences, small bank fees |

### Step 5: Age the Reconciling Items

Every reconciling item gets an age bucket based on how long it has remained unresolved:

| Aging Bucket | Days Outstanding | Required Action |
|---|---|---|
| **Current** | 0–30 days | Monitor. Expected to clear next period. |
| **Aged** | 31–90 days | Investigate. Document reason for delay. Escalate if no clear resolution path. |
| **Stale** | >90 days | **Mandatory investigation.** Likely requires a journal entry, write-off, or management decision. Flag for controller review. |

Stale items on a reconciliation are a red flag. If an item has sat unresolved for 90+ days, the reconciliation is not complete — it is a tracker with an open item list.

### Step 6: Resolve and Document

For each reconciling item, document the resolution or proposed action:

- **Timing items**: Note expected clearing date. If a timing item has been "timing" for >60 days, reclassify to `MISSING` or `ERR`.
- **Errors**: Prepare a correcting journal entry (JE) with supporting detail. Include the JE number once posted.
- **Missing entries**: Prepare the booking entry. For bank items (fees, interest), batch into a single JE if immaterial individually.
- **Write-offs**: Document the amount, the threshold used, and approval. Write-offs should be posted as a JE, not simply ignored.

### Step 7: Prove Out the Reconciliation

The reconciliation must **foot and cross-foot**. The standard proof:

```
GL Balance (per books)                         $XXX,XXX.XX
  Add: Items in supporting source, not in GL   $XX,XXX.XX
  Less: Items in GL, not in supporting source  ($X,XXX.XX)
                                               ───────────
Adjusted GL Balance                            $XXX,XXX.XX

Supporting Source Balance                      $XXX,XXX.XX
  Add: Items in GL, not in supporting source   $X,XXX.XX
  Less: Items in supporting source, not in GL  ($XX,XXX.XX)
                                               ───────────
Adjusted Supporting Source Balance              $XXX,XXX.XX

Difference                                     $0.00
```

If the difference is not zero, the reconciliation is not complete.

---

## Output Templates

### Reconciliation Summary Header

```
ACCOUNT RECONCILIATION
Account:        [Number] — [Name]
Entity:         [Company Code / Entity Name]
Period:         [Month-End Date]
Currency:       [CCY]
Prepared by:    [Name]           Date: [Date]
Reviewed by:    [Name]           Date: [Date]
Status:         [Reconciled / Open Items Remaining]
```

### Reconciling Items Table

See `references/RECONCILIATION-TEMPLATE.md` for the standardized table format.

### Summary Metrics (include at bottom of every reconciliation)

| Metric | Value |
|---|---|
| GL Balance | $XXX |
| Supporting Source Balance | $XXX |
| Gross Reconciling Items | $XXX |
| Net Reconciling Difference | $0.00 |
| Count of Open Items | N |
| Stale Items (>90 days) | N |
| Largest Single Reconciling Item | $XXX |
| Materiality Threshold | $XXX |
| Items Exceeding Threshold | N |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Before finalizing any reconciliation output, verify:

- [ ] **Proof**: Adjusted GL balance equals adjusted supporting source balance (difference = $0.00)
- [ ] **Completeness**: All transactions in both sources are accounted for — matched or listed as reconciling items
- [ ] **Categorization**: Every reconciling item has a category code (`TIMING`, `ERR-A`, `ERR-B`, `MISSING`, `CUTOFF`, `FX`, `WOFF`)
- [ ] **Aging**: Every reconciling item has an aging bucket and days outstanding
- [ ] **Action items**: Every non-timing item has a proposed resolution with an owner and due date
- [ ] **Carryforward check**: Prior period items are tracked — cleared items removed, persistent items re-aged
- [ ] **Materiality**: Items below threshold are documented as write-offs, not silently dropped
- [ ] **Journal entries**: All correcting/booking entries are identified with JE numbers (or marked `[PENDING]`)
- [ ] **Reviewer sign-off**: Reconciliation includes preparer and reviewer fields; reviewer has a basis to assess completeness
- [ ] **No stale items without explanation**: Any item >90 days has a documented investigation note

---

## Quality Audit

### SOX Control Considerations

Account reconciliation is typically a **key control** in a SOX environment. The following must be evidenced:

| Control Attribute | What to Document |
|---|---|
| **Timeliness** | Reconciliation completed within X business days of period end (per policy) |
| **Completeness** | All in-scope accounts reconciled; none skipped |
| **Accuracy** | Reconciliation foots to zero or differences are explained |
| **Evidence of Review** | Independent reviewer sign-off with date; reviewer is not the preparer |
| **Investigation** | Stale and material items have documented follow-up |
| **Resolution** | Correcting entries posted and referenced |

### Common Deficiency Patterns

Flag these in quality review — they indicate a reconciliation that looks complete but is not:

1. **"Timing" items that never clear** — If an outstanding check has been outstanding for 6 months, it is not timing. Investigate for stale-dated checks, escheatment requirements, or recording errors.
2. **Plugged differences** — A single line labeled "Other" or "Miscellaneous" that forces the recon to zero. Every reconciling item must be individually identified.
3. **Stale support** — Using a bank statement from a different date than the GL balance, or a sub-ledger run at a different time. Sources must be as-of the same point in time.
4. **Missing prior-period roll** — The reconciliation does not track items from last month. You cannot assess whether aged items are growing or shrinking.
5. **No materiality framework** — Write-offs without a stated threshold, or investigation of penny differences while ignoring a large unresolved item.

### Reconciliation-Type-Specific Checks

**Bank Reconciliation**
- Outstanding checks >180 days: check escheatment laws by jurisdiction
- Deposits in transit >3 business days: investigate; may indicate fictitious revenue (kiting)
- Bank fees/interest: confirm booked monthly; do not let accumulate
- NSF / returned items: confirm AR was re-debited or follow-up initiated

**Intercompany**
- Net IC balance across all entities must equal zero at consolidation
- Bilateral confirmation: both sides agree on the balance
- Timing differences must have a clear posting date on the counterparty side
- Eliminate in consolidation only after both sides are reconciled

**Sub-ledger to GL**
- Sub-ledger total must tie to GL control account exactly
- If a difference exists, it usually means a journal entry was posted directly to the GL control account bypassing the sub-ledger — this is a control weakness

**Balance Sheet Account (Schedule-Based)**
- Roll-forward: Opening balance + additions – reductions = Ending balance = GL balance
- Prepaid: Amortization schedule must tie; check for fully amortized items still on the schedule
- Accruals: Each accrual must have a basis (invoice, estimate, contract term); stale accruals indicate over-accrual
- Fixed assets: Agree to fixed asset register; check for ghost assets

---

## Reference Files

| File | Description |
|---|---|
| `references/RECONCILIATION-TEMPLATE.md` | Standardized reconciling items table, proof format, and summary metrics template |
