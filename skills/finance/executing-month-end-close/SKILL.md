---
name: executing-month-end-close
description: Structures month-end close procedures with journal entry preparation, reconciliation, and variance analysis. Use when performing month-end close, preparing close checklists, or analyzing period variances.
tags:
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Financial Reporting
    - Audit
    - Accounting
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Executing Month End Close

Structures month-end close procedures with journal entry preparation, reconciliation, and variance analysis.

## When To Use

- Performing or reviewing a monthly accounting close cycle
- Building or refining a close checklist with task owners and deadlines
- Preparing standard and adjusting journal entries for period cutoff
- Reconciling balance sheet accounts (cash, AR, AP, prepaids, accruals, fixed assets, debt)
- Analyzing period-over-period variances and budget-to-actual deviations
- Generating a close package for controller or CFO sign-off

## Inputs To Gather

- **Trial balance** — current-period and prior-period (or budget) for comparison
- **Sub-ledger detail** — AR aging, AP aging, fixed-asset register, loan amortization schedules
- **Bank statements** — all operating, payroll, and investment accounts for the period
- **Revenue support** — billing reports, deferred revenue schedules, contract milestones
- **Expense accrual inputs** — purchase orders received-not-invoiced, payroll calendars, benefit invoices
- **Intercompany activity** — IC transaction logs and elimination entries if multi-entity
- **Prior-period reconciliations** — to carry forward open items and verify clearing
- **Close calendar** — target dates, task owners, and dependency sequencing
- **Materiality threshold** — the amount below which variances are deemed immaterial [VERIFY against entity's accounting policy]

## Workflow

### 1. Pre-Close Preparation (Days 1-2)

- Confirm all sub-ledger postings (AR, AP, payroll, inventory) are complete for the period
- Verify cutoff: ensure revenue and expenses are recorded in the correct period
  - Check ship dates vs. invoice dates for revenue recognition
  - Confirm goods/services received by period end for expense accruals
- Run preliminary trial balance and scan for obvious anomalies (negative balances, misclassified accounts)
- Distribute close checklist with task assignments and deadlines

### 2. Journal Entry Preparation (Days 2-4)

- **Standard recurring entries**: depreciation, amortization, straight-line rent, prepaid expense release, loan interest accrual
- **Adjusting entries**: accrued expenses (utilities, professional fees, bonuses), deferred revenue adjustments, inventory reserves, bad-debt provision
- **Reclassification entries**: correct mispostings, reallocate shared costs, reclassify current portion of long-term debt
- **Intercompany entries**: post IC charges, confirm matching balances, prepare elimination entries [VERIFY elimination method — automatic vs. manual per ERP setup]
- For each journal entry, document: account codes, amounts, description/business purpose, supporting calculation or source document reference

### 3. Account Reconciliation (Days 3-5)

For every balance sheet account, prepare or review a reconciliation:

- **Cash & equivalents** — bank reconciliation; identify and age outstanding checks and deposits in transit
- **Accounts receivable** — tie sub-ledger to GL; review aging buckets; assess allowance for doubtful accounts
- **Prepaids & other assets** — verify amortization schedules; confirm remaining balances are supportable
- **Fixed assets** — reconcile additions, disposals, and depreciation to the FA register; confirm CIP items
- **Accounts payable** — tie sub-ledger to GL; confirm completeness against receiving reports
- **Accrued liabilities** — validate each accrual with source documentation or reasonable estimate
- **Debt** — reconcile to lender statements; confirm principal, interest, and covenant calculations
- **Equity** — roll forward from prior period; confirm any issuances, repurchases, or dividend entries

Flag any reconciling items older than 60 days or above materiality for controller review.

### 4. Variance Analysis (Days 4-6)

- Compute month-over-month and budget-to-actual variances for all P&L line items
- Investigate variances exceeding the materiality threshold or ±10% of budget (whichever is lower) [VERIFY threshold per company policy]
- Categorize root causes: timing differences, volume/price changes, one-time items, accrual true-ups, errors
- Prepare variance commentary for each significant line item — state cause, quantify impact, note whether recurring or non-recurring
- Summarize top 5-10 variances in an executive narrative

### 5. Close Package Assembly (Days 5-7)

- Compile the following for management review:
  - Final trial balance
  - Income statement and balance sheet (comparative)
  - Cash flow summary (if required monthly)
  - Reconciliation binder or index with status (complete / open items)
  - Variance analysis with commentary
  - Journal entry log with approval status
  - Open items list requiring follow-up in next period
- Obtain required sign-offs (preparer, reviewer, controller/CFO)
- Lock the period in the ERP/GL system after final approval

## Output

Deliver a structured close package containing:

- **Close checklist** — all tasks with status, owner, completion date
- **Journal entry schedule** — each entry with account, amount, description, and supporting reference
- **Reconciliation summaries** — one page per account showing GL balance, supporting balance, and reconciling items
- **Variance report** — table of significant variances with cause, amount, and recurring/non-recurring flag
- **Executive summary** — narrative highlighting key financial results, unusual items, and open issues

## Quality Checks

- All balance sheet accounts are reconciled; no account has an unexplained difference above materiality
- Journal entries balance (total debits = total credits) and have documented support
- Revenue and expense cutoff is verified — no material items recorded in the wrong period
- Intercompany balances net to zero after eliminations
- Variance explanations are specific and quantified — no generic "timing" without dollar amounts
- Close checklist shows 100% task completion before period lock
- [VERIFY] Accounting standards applied (US GAAP, IFRS, or other) are consistent with prior periods
- [VERIFY] Any changes in estimates or accounting policies are disclosed and approved
- Reconciling items carried forward from prior months are resolved or have documented justification for remaining open
