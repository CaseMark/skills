---
name: managing-corporate-actions
description: Processes corporate action events with election management, entitlement calculation, and position adjustment. Use when managing corporate actions, processing dividends, or handling stock splits.
tags:
  - management
  - fund-operations
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
# Managing Corporate Actions

Processes corporate action events — dividends, stock splits, mergers, tender offers, rights issues, spin-offs, and reorganizations — through the full lifecycle from announcement to settlement and position reconciliation.

## When To Use

- A SWIFT MT564/MT566 or ISO 20022 corporate action notification arrives from a custodian or data vendor (Bloomberg CACT, ICE, SIX)
- A fund holds positions affected by a mandatory, mandatory-with-choice, or voluntary corporate action
- Election deadlines are approaching and investment teams need decision summaries
- Post-event position or cash reconciliation shows breaks tied to a corporate action
- NAV production requires entitlement accrual or ex-date adjustments

## Inputs To Gather

- **Event notification**: SWIFT message, custodian notice, or vendor feed with event type, ISIN/CUSIP, record date, ex-date, pay date, and election deadline
- **Position data**: Holdings as of record date (and ex-date if different) across all accounts, share classes, and sleeves
- **Election options**: For voluntary/choice events — option descriptions, default election, tax implications per option, and any proration terms
- **Prior corporate action history**: Previous events on same security to detect chaining (e.g., split followed by dividend)
- **Tax lot and cost basis detail**: Needed for return-of-capital dividends, spin-offs, and reorganizations that require cost basis reallocation
- **Standing instructions**: Client or fund-level default elections, cash vs. reinvestment preferences, and any DRIP enrollment status

## Workflow

1. **Capture & Classify Event**
   - Parse notification and classify by ISO 15022 event type (DVCA, SPLF, MRGR, TEND, RHTS, EXOF, etc.)
   - Determine mandatory vs. voluntary vs. mandatory-with-choice
   - Log key dates: announcement, ex-date, record date, election deadline, payment/effective date
   - Cross-reference against vendor data to confirm terms; flag discrepancies with [VERIFY]

2. **Calculate Entitlements**
   - Pull record-date positions for all affected accounts
   - Apply event terms: ratio for splits, rate per share for dividends, exchange ratio for mergers
   - Handle fractional shares per fund policy (round down and cash-in-lieu, or full shares)
   - For dividends: distinguish between ordinary income, qualified, return of capital, and capital gains components [VERIFY against issuer's Section 19(a) notice or equivalent]
   - Compute gross and net amounts, applying applicable withholding tax rates by jurisdiction [VERIFY treaty rates per investor domicile]

3. **Manage Elections (Voluntary/Choice Events)**
   - Prepare election summary showing each option with projected economic impact
   - Distribute to portfolio managers with deadline clearly noted (include custodian's internal deadline, which is typically 1-2 business days before issuer deadline)
   - Collect elections; apply standing instructions where no active election is received
   - Submit elections to custodian; confirm receipt and capture confirmation reference
   - Track oversubscription or proration risk on tender offers

4. **Process Position Adjustments**
   - On ex-date: adjust positions for splits, reverse splits, and rights distributions
   - On pay date: book cash entries for dividends; settle share deliveries for stock dividends and mergers
   - For reorganizations and spin-offs: reallocate cost basis using issuer-published allocation factors [VERIFY allocation percentages from issuer 8937 filing or equivalent]
   - Update tax lots with new cost basis, acquisition dates (carryover vs. new), and holding period assignments
   - Post accounting entries: accrued income reversal, realized gain/loss (if applicable), receivable/payable creation

5. **Reconcile & Close**
   - Reconcile positions and cash against custodian statements post-settlement
   - Investigate and resolve breaks — common causes: timing differences, fractional share rounding, withholding rate mismatches, missed elections
   - Confirm NAV impact is correctly reflected for affected valuation dates
   - Archive event documentation: original notice, election records, custodian confirmations, reconciliation sign-off

## Output

- **Event Processing Summary**: Event type, security identifier, key dates, terms applied, and current lifecycle status (announced / pending election / ex-date passed / settled / closed)
- **Entitlement Schedule**: Per-account breakdown of gross entitlement, withholding, net amount, fractional share treatment, and cost basis adjustments
- **Election Tracker**: Option descriptions, elections submitted, confirmation references, and deadline compliance status
- **Reconciliation Report**: Position and cash comparison (book vs. custodian) with break analysis and resolution notes
- **Exception Log**: Any items requiring manual review — unmatched positions, missing tax forms, disputed terms, or unconfirmed elections

## Quality Checks

- Entitlement calculations tie back to official event terms (rate x position = entitlement, within rounding tolerance)
- All elections were submitted before custodian deadline; any missed deadlines are escalated immediately
- Cost basis reallocations use issuer-published factors, not estimates [VERIFY source document]
- Withholding tax rates match treaty schedules for each investor jurisdiction [VERIFY]
- Post-settlement positions reconcile to custodian within zero tolerance for shares and defined cash tolerance
- NAV impact is reviewed: ex-date price adjustment, accrual reversal, and pay-date cash receipt are all reflected on correct valuation dates
- No duplicate processing — confirm each event ID is processed exactly once across systems
