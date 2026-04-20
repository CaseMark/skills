---
name: managing-middle-office-operations
language: en
description: Structures middle office functions with trade matching, position reconciliation, and P&L verification. Use when managing middle office, reconciling positions, or verifying P&L calculations.
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
# Managing Middle Office Operations

Structures middle office functions with trade matching, position reconciliation, and P&L verification.

## When To Use

- Standing up or restructuring a fund's middle office function (trade support, portfolio accounting, risk oversight)
- Investigating trade breaks, position mismatches, or NAV discrepancies
- Building or reviewing daily/monthly reconciliation workflows across custodians, prime brokers, and fund administrators
- Verifying realized and unrealized P&L calculations against official books and records
- Preparing middle office status reports for portfolio managers, COOs, or compliance

## Inputs To Gather

- **Trade blotter / OMS extract** — executed trades for the period with order IDs, counterparties, quantities, prices, commissions, and settlement dates
- **Custodian/PB position statements** — end-of-day or end-of-period holdings from each custodian or prime broker
- **Internal portfolio accounting records** — positions and cash balances from the fund's book-of-record system
- **Corporate action notices** — dividends, splits, mergers, tender offers affecting held positions
- **Pricing sources** — vendor feeds (Bloomberg, Refinitiv) and any override/fair-value marks from the valuation committee
- **Prior reconciliation exception log** — outstanding breaks carried forward from the last cycle
- **Fund governing documents** — LPA/OA provisions on valuation methodology, fee waterfalls, and reporting obligations [VERIFY fund-specific terms]

## Workflow

### 1. Trade Capture & Matching

- Import trade blotter from OMS; match each trade against broker confirmations on trade date (T+0)
- Confirm economic terms: security identifier (CUSIP/ISIN/SEDOL), side, quantity, price, currency, settlement date, commission/fees
- Flag unmatched or partially matched trades as breaks; classify by type (price break, quantity break, missing confirmation)
- Escalate unresolved breaks older than T+1 for listed securities or T+2 for OTC/derivatives [VERIFY settlement conventions by asset class and jurisdiction]

### 2. Position Reconciliation

- Pull end-of-day positions from (a) internal books, (b) custodian/PB statements, and (c) fund administrator records
- Run three-way reconciliation: internal vs. custodian vs. administrator
- Identify quantity breaks, settlement-date vs. trade-date differences, and pending-settlement items
- Reconcile cash balances including accrued interest, margin balances, and collateral postings
- Document each break with root cause (failed settlement, late booking, corporate action timing, FX conversion)
- Resolve or age breaks per the fund's tolerance thresholds (e.g., <$100 auto-clear, >$100 requires sign-off) [VERIFY materiality thresholds]

### 3. Corporate Action Processing

- Monitor announced corporate actions for all held positions; cross-reference against custodian/PB notifications
- Classify as mandatory (dividends, splits) or voluntary (tenders, rights offerings) and route voluntary actions for PM decision by election deadline
- Verify ex-date, record-date, and pay-date processing in the portfolio accounting system
- Confirm post-action position and cost-basis adjustments

### 4. P&L Verification

- Calculate daily/period P&L by component: realized gains/losses, unrealized mark-to-market, income (dividends, interest, premiums), and financing costs
- Cross-check pricing inputs against approved sources; flag stale prices (>1 day old for liquid securities, >5 days for illiquid) [VERIFY staleness policy]
- Reconcile P&L between the internal system and the fund administrator's independent calculation
- Investigate material variances (typically >0.5 bps of NAV); trace to specific positions or pricing differences [VERIFY variance tolerance]
- Verify FX rate sources and conversion timing for multi-currency portfolios

### 5. Exception Management & Reporting

- Maintain an exception log with: break ID, date identified, asset/account, break amount, root cause, owner, aging, resolution status
- Produce daily middle office dashboard showing: trade match rate, open position breaks by age bucket, P&L variance summary, pending corporate actions
- Escalate aged or material exceptions per defined SLA (e.g., >3 days unresolved → ops manager, >5 days → COO) [VERIFY escalation matrix]
- Prepare month-end summary for inclusion in the fund administrator's NAV package

## Output

The deliverable is a **Middle Office Status Report** containing:

- **Trade matching summary** — match rate, open breaks with aging, resolution notes
- **Position reconciliation results** — three-way recon status by account, outstanding breaks with root cause
- **P&L reconciliation** — internal vs. administrator P&L, variance analysis by position and component
- **Corporate action log** — actions processed, elections made, pending items
- **Exception dashboard** — all open items, owners, SLA status, escalation flags
- **Recommendations** — process improvements, system issues, staffing or workflow adjustments

## Quality Checks

- Every trade in the blotter has a corresponding broker confirmation or is flagged as an open break
- Three-way position recon covers 100% of accounts; no account is silently excluded
- P&L variance between internal books and administrator is within the fund's stated tolerance [VERIFY]
- All voluntary corporate actions have documented PM elections before the deadline
- Stale or overridden prices are individually justified and approved per the valuation policy
- Exception log has no items missing an assigned owner or aging date
- Report terminology is consistent (e.g., "break" vs. "discrepancy" — pick one and use throughout)
- All dollar amounts and share counts tie back to source extracts; no manual hardcodes without audit trail
