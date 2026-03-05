---
name: managing-trade-operations
description: Structures trade lifecycle management with confirmation, settlement, and exception processing. Use when managing trade operations, processing confirmations, or resolving settlement exceptions.
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
# Managing Trade Operations

## When To Use

- Onboarding a new fund or strategy that requires trade lifecycle setup (confirmation routing, SSI configuration, settlement instructions)
- Investigating and resolving failed or unmatched trades, aged breaks, or settlement exceptions
- Building or reviewing daily trade operations dashboards covering confirmation rates, settlement efficiency, and exception queues
- Preparing trade operations status reports for portfolio managers, compliance, or fund boards
- Evaluating counterparty or broker-dealer operational performance and SLA adherence

## Inputs To Gather

- **Trade blotter / order management export** — executed trades with asset class, counterparty, trade date, settlement date, notional/quantity, price
- **Confirmation status report** — matched, unmatched, alleged, and affirmed counts by counterparty and asset class
- **Settlement instruction database (SSIs)** — standing instructions per counterparty, custodian, and currency
- **Exception / fail log** — open items with aging, root cause codes, and responsible party
- **Custodian and prime broker settlement reports** — projected and actual settlements, cash breaks, position breaks
- **Market calendars** — settlement cycles by jurisdiction and instrument type (T+1, T+2, T+3) [VERIFY: confirm current settlement cycle per market — many markets moved to T+1 in 2024-2025]

## Workflow

1. **Capture trade details at execution**
   - Ingest trades from OMS/EMS into the operations platform
   - Validate required fields: counterparty LEI, ISIN/CUSIP, settlement date, settlement location, currency, SSI references
   - Flag any trades missing mandatory fields for immediate remediation

2. **Confirmation matching**
   - Route electronic confirmations via SWIFT MT300/MT515, CTM, or MarkitWire depending on asset class
   - For OTC derivatives, match economic terms (notional, rate, maturity, payment frequency) against counterparty confirms
   - Escalate unmatched confirmations exceeding T+1 aging threshold to the trade support desk
   - Track affirmation rates — target ≥98% same-day affirmation for equity and fixed income trades

3. **Pre-settlement processing**
   - Verify SSIs are current and match custodian records; flag any SSI mismatches before value date
   - Confirm sufficient inventory or cash for delivery-versus-payment (DvP) and receive-versus-payment (RvP) obligations
   - For FX and cross-currency trades, verify CLS eligibility and netting set membership
   - For repo and securities lending, confirm collateral eligibility and haircut schedules

4. **Settlement execution and monitoring**
   - Monitor real-time settlement status via custodian portals or SWIFT MT548 updates
   - Categorize fails by root cause: counterparty fail, insufficient inventory, SSI mismatch, market-side issue, operational error
   - Calculate fail costs using applicable penalty regimes (e.g., CSDR mandatory buy-in framework in EU markets) [VERIFY: confirm CSDR penalty rates and buy-in rules for relevant jurisdictions]
   - Initiate partial settlement where permitted and economically beneficial

5. **Exception management and resolution**
   - Maintain an exception queue with severity tiers: P1 (>$1M or regulatory impact), P2 (>$100K), P3 (routine)
   - Document root cause, remediation steps, and responsible party for each exception
   - Escalate P1 exceptions to operations management within 2 hours; P2 within same business day
   - Track aging and resolution time — target ≤3 business days average resolution

6. **Reporting and analytics**
   - Produce daily settlement dashboard: settlement rate, fail rate by counterparty, aged exceptions, cash impact of fails
   - Generate weekly counterparty scorecards ranking brokers/dealers by confirmation timeliness, fail rates, and SSI accuracy
   - Report monthly KPIs: straight-through processing (STP) rate, confirmation match rate, average fail duration, exception volumes by category

## Output

- **Daily trade operations report** — confirmation status, settlement projections, open exceptions with aging and severity
- **Exception resolution log** — closed items with root cause analysis, remediation actions, and time-to-resolution
- **Counterparty performance scorecard** — ranking by confirmation speed, fail frequency, SSI accuracy
- **Monthly KPI summary** — STP rate, settlement efficiency, fail cost, exception trends with month-over-month comparison
- **Escalation tracker** — P1/P2 items with current status, owner, and expected resolution date

## Quality Checks

- Confirm all executed trades are captured — reconcile trade count against OMS blotter (zero unaccounted trades)
- Verify SSI data matches custodian records before each settlement cycle
- Ensure exception root cause codes are consistently applied (no catch-all "other" exceeding 10% of exceptions)
- Validate fail cost calculations against the correct penalty regime for each market [VERIFY: penalty rate schedules by CSD]
- Cross-check settlement projections against actual outcomes to measure forecast accuracy
- Confirm all P1 exceptions have documented escalation within the required timeframe
- Review counterparty scorecards for data completeness — no counterparty with >5 trades should be missing from the report
