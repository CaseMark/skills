---
name: managing-fund-accounting
description: Structures fund accounting processes with trade recording, income allocation, and financial statement preparation. Use when managing fund books, recording investment transactions, or preparing fund financials.
tags:
  - management
  - fund-operations
  - investment
  - accounting
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Fund Accounting

Structures fund accounting processes with trade recording, income allocation, and financial statement preparation.

## When To Use

- Setting up or reviewing the books for an investment fund (hedge fund, PE fund, venture fund, real estate fund)
- Recording trades, capital activity, or corporate actions across portfolio positions
- Allocating income, expenses, gains, and losses to investor capital accounts
- Preparing fund-level financial statements (NAV statements, statements of operations, capital account statements)
- Reconciling fund records against custodian, prime broker, and administrator data
- Responding to auditor requests for fund accounting workpapers

## Inputs To Gather

- **Fund structure**: fund type (open-end, closed-end, master-feeder, fund-of-funds), domicile, fiscal year-end, and base currency
- **Partnership/operating agreement**: allocation methodology (pro-rata, layered/new-issue, lot-based), management fee and incentive fee terms, hurdle rates, clawback provisions, side pocket treatment [VERIFY specific waterfall mechanics against LPA]
- **Trade data**: executed trades with settlement dates, trade confirmations, and broker allocations
- **Capital activity**: subscription/redemption notices, capital call and distribution notices, transfer records
- **Corporate actions**: dividends, splits, mergers, spin-offs, tender offers affecting portfolio holdings
- **Valuation inputs**: pricing sources hierarchy (exchange close, dealer marks, third-party vendors, fair value committee determinations) [VERIFY fund valuation policy]
- **Prior period data**: prior NAV, prior capital account balances, beginning-of-period trial balance, and open lot inventory

## Workflow

1. **Establish chart of accounts and accounting policies**
   - Confirm trade-date vs. settlement-date accounting per the fund's governing documents [VERIFY]
   - Map security types to appropriate asset/liability accounts (long positions, short positions, derivatives, repos)
   - Set up multi-currency ledger if fund holds non-base-currency assets; define FX rate sources and revaluation frequency

2. **Record investment transactions**
   - Book executed trades: cost basis (including commissions and SEC fees), settlement obligations, accrued interest for fixed income
   - Process corporate actions: adjust lot-level cost basis for stock splits, record dividend income (distinguish ordinary vs. qualified vs. return of capital)
   - Record derivative activity: premium payments, margin flows, daily mark-to-market for futures, periodic resets for swaps

3. **Perform daily/periodic valuations**
   - Apply pricing hierarchy: exchange-traded closes first, then dealer marks, then fair value estimates
   - Calculate unrealized gain/loss by lot against cost basis
   - Compute fund-level NAV: total assets minus total liabilities
   - For open-end funds, derive per-share/per-unit NAV for subscription and redemption pricing

4. **Allocate income and expenses to partners/shareholders**
   - Calculate management fees (typically on beginning-of-period or average NAV) per the fee schedule
   - Calculate incentive fees/performance allocations, applying high-water marks, hurdle rates, and crystallization frequencies [VERIFY waterfall terms against LPA]
   - Allocate net investment income, realized gains/losses, and unrealized gains/losses across capital accounts using the fund's specified methodology
   - Handle new-issue eligibility restrictions (FINRA Rules 5130/5131) for applicable investors [VERIFY investor eligibility designations]

5. **Process capital activity**
   - Record subscriptions at applicable NAV with any equalization adjustments
   - Process redemptions: calculate redemption proceeds, apply any holdback reserves, verify lock-up and gate provisions
   - For PE/VC funds: record capital calls against unfunded commitments, process distributions (return of capital vs. profit distributions per the waterfall)

6. **Reconcile across counterparties**
   - Reconcile cash balances to custodian and prime broker statements daily
   - Reconcile portfolio positions (quantities and market values) to custodian/PB records
   - Reconcile capital accounts to administrator records (if external administrator is used)
   - Investigate and resolve all breaks before finalizing the period

7. **Prepare financial statements and reporting**
   - Generate NAV statement with position-level detail
   - Prepare statement of operations (investment income, expenses, realized/unrealized gains)
   - Prepare statement of changes in partners' capital / statement of changes in net assets
   - Produce individual investor capital account statements with beginning balance, contributions, withdrawals, allocated P&L, and ending balance
   - Compile supporting schedules: fee calculations, lot-level realized gain/loss, FX gain/loss, expense allocation

## Output

- **Trial balance** with all fund-level accounts reconciled and balanced
- **NAV package**: NAV statement, statement of operations, statement of changes in net assets/partners' capital
- **Investor capital account statements** with full activity detail for the period
- **Reconciliation summaries**: cash, position, and capital account reconciliations with break resolution notes
- **Supporting workpapers**: fee calculations, allocation schedules, pricing exception reports, corporate action processing logs
- **Audit-ready documentation**: organized by financial statement line item with source references

## Quality Checks

- NAV ties to the sum of all investor capital accounts (zero residual)
- Total allocated income/expense/gain/loss across all investors equals fund-level totals (allocation proof)
- Cash reconciliation shows zero unexplained breaks against custodian/PB statements
- Position reconciliation shows zero quantity or valuation breaks (or all breaks documented with resolution status)
- Management fee and incentive fee calculations independently verified against LPA terms
- All fair-valued positions documented with methodology and approval per the fund's valuation policy
- Realized gain/loss on dispositions ties to lot-level cost basis records
- FX revaluation gains/losses properly segregated from investment gains/losses
- New-issue allocation restrictions correctly applied to restricted investors [VERIFY against current FINRA guidance]
- Financial statements prepared in accordance with applicable GAAP (US GAAP or IFRS) and reviewed for consistency with prior periods [VERIFY applicable reporting framework]
