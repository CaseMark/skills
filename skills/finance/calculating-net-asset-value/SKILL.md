---
name: calculating-net-asset-value
language: en
description: Structures NAV calculation with security pricing, accruals, expense allocation, and reconciliation. Use when calculating fund NAV, pricing portfolios, or reconciling NAV components.
tags:
  - analysis
  - fund-operations
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Calculation Worksheet
  skill_modes:
    - Calculation
---
# Calculating Net Asset Value

Structures NAV calculation with security pricing, accruals, expense allocation, and reconciliation for open-end funds, closed-end funds, hedge funds, and other pooled investment vehicles.

## When To Use

- Calculating daily, weekly, or monthly NAV for a fund
- Pricing a portfolio for investor subscriptions or redemptions
- Reconciling NAV components against administrator or custodian records
- Investigating NAV breaks or pricing discrepancies
- Preparing NAV packages for board reporting or audit support

## Inputs To Gather

- **Portfolio holdings**: Complete position file with security identifiers (CUSIP, ISIN, SEDOL), quantities, and trade date vs. settlement date status
- **Security prices**: Closing market prices, bid/ask spreads, or fair-value marks; identify pricing source hierarchy (primary exchange, composite, pricing vendor, broker quotes, internal model)
- **Cash and cash equivalents**: Bank balances, money market positions, margin balances, collateral held/posted
- **Accrued income**: Interest accruals (coupon income, amortization/accretion on fixed income), declared dividends receivable, securities lending fee accruals
- **Accrued expenses**: Management fees, performance/incentive fees, administration fees, custody fees, legal/audit accruals, borrowing costs, other fund-level expenses
- **Corporate actions**: Pending or ex-date adjustments (splits, dividends, mergers, spin-offs, rights offerings)
- **Subscriptions/redemptions**: Pending capital activity and any equalization adjustments
- **FX rates**: Spot rates for multi-currency portfolios; identify rate source and cut-off time

## Workflow

1. **Validate position data** — Reconcile the position file against custodian records and trade blotter. Confirm all executed trades are captured. Flag any unmatched positions or pending settlements that affect NAV-date holdings.

2. **Price securities** — Apply the pricing source hierarchy per the fund's valuation policy. For each holding:
   - Listed equities/bonds: use closing price from designated exchange or composite
   - OTC derivatives: use counterparty valuations, independent pricing service, or internal model; document inputs (curves, vols, spreads)
   - Illiquid/hard-to-value: apply fair-value procedures per ASC 820 / IFRS 13 hierarchy (Level 1 → 2 → 3) [VERIFY: confirm applicable accounting standard]
   - Flag stale prices (no update > threshold days) and securities with wide bid-ask spreads for pricing committee review

3. **Calculate gross asset value** — Multiply each position quantity by its NAV-date price. Convert foreign-currency positions using the designated FX rate. Sum all holdings plus cash balances plus accrued income receivable.

4. **Accrue and allocate expenses** — Compute each expense line item on the applicable accrual basis (daily, monthly, quarterly). For performance/incentive fees, calculate based on the fund's high-water mark or hurdle rate methodology [VERIFY: confirm fee terms from fund documents]. Apply investor-level equalization or series accounting where required.

5. **Compute NAV** — Net Asset Value = Gross Assets − Total Accrued Liabilities. Derive per-share/per-unit NAV by dividing by shares/units outstanding (adjusted for any pending subscriptions or redemptions effective on the NAV date).

6. **Reconcile and cross-check**:
   - Compare calculated NAV to administrator's independent NAV; investigate any variance exceeding the fund's tolerance threshold (typically 5–10 bps)
   - Verify daily NAV movement is directionally consistent with benchmark/index performance and known portfolio activity
   - Check per-share NAV change against prior-day NAV for reasonableness
   - Reconcile cash balances to bank/custodian statements

7. **Resolve NAV breaks** — For variances outside tolerance, isolate the break by component (pricing, positions, cash, accruals, shares outstanding). Document root cause and adjustment. Escalate to pricing committee or fund controller if break exceeds materiality threshold.

## Output

Produce a **NAV Calculation Worksheet** containing:

- **NAV summary**: Total gross assets, total liabilities, net assets, shares/units outstanding, per-share/per-unit NAV, NAV date
- **Holdings detail**: Security-level market values with pricing source attribution
- **Accrual schedules**: Line-item breakdown of income accruals and expense accruals
- **Reconciliation summary**: Side-by-side comparison with administrator/custodian values, variance amounts and percentages
- **NAV movement analysis**: Day-over-day (or period-over-period) NAV change decomposed into market movement, income, expenses, and capital activity
- **Exception log**: Stale prices, fair-valued positions, unreconciled items, and any [VERIFY] flags

## Quality Checks

- All positions in the portfolio are accounted for — no orphaned or missing holdings
- Pricing sources are documented and consistent with the fund's valuation policy
- Expense accruals tie to the fund's offering documents, side letters, and board-approved budgets
- FX rates are sourced consistently and applied at the correct cut-off time
- Shares/units outstanding reflect all effective subscriptions and redemptions
- NAV variance vs. independent administrator is within stated tolerance
- Fair-valued securities include documented rationale and Level classification [VERIFY: ASC 820 or IFRS 13 as applicable]
- Calculation is reproducible — another fund accountant can trace every input to its source
