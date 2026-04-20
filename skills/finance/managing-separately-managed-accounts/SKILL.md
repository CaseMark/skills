---
name: managing-separately-managed-accounts
language: en
description: Structures SMA operations with customization, compliance overlay, and performance composites. Use when managing SMAs, implementing custom portfolios, or maintaining performance composites.
tags:
  - management
  - asset-management
  - compliance
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Separately Managed Accounts

Structures SMA operations including client customization, investment policy compliance overlay, trade execution, and GIPS-compliant performance composites.

## When To Use

- Onboarding a new SMA client and translating their IPS into portfolio rules and restriction schedules
- Implementing or updating model portfolios across multiple SMA sleeves with client-specific overlays
- Running pre-trade and post-trade compliance checks against client guidelines, regulatory limits, and ESG/values-based restrictions
- Building, maintaining, or auditing GIPS-compliant performance composites
- Preparing periodic SMA management reports for clients, consultants, or internal oversight committees
- Rebalancing accounts after cash flows, corporate actions, or model changes while respecting tax-lot and wash-sale constraints

## Inputs To Gather

- **Investment Policy Statement (IPS):** Return objectives, risk tolerance, time horizon, liquidity needs, and any unique circumstances
- **Restriction schedule:** Prohibited securities, sector caps, ESG screens, concentrated-stock constraints, and any legacy/low-basis holdings to preserve
- **Model portfolio(s):** Target weights by security or asset class, acceptable drift bands, and rebalancing triggers
- **Account details:** Custodian, tax status (taxable / tax-deferred / tax-exempt), cost-basis method (specific-lot, FIFO, HIFO), and cash reserve requirement
- **Fee schedule:** Management fee rate, billing frequency (advance/arrears), fee-calculation methodology (average daily balance, quarter-end market value)
- **Composite assignment criteria:** Strategy name, inception date, minimum account size, inclusion/exclusion rules, benchmark index [VERIFY against current GIPS standards edition]
- **Regulatory context:** [VERIFY] Applicable regulations — SEC/state RIA rules, ERISA if retirement assets, UPIA if trust assets

## Workflow

1. **Account Setup & IPS Translation**
   - Map IPS objectives to a model portfolio sleeve or custom blend
   - Encode restriction schedule into the compliance overlay system (prohibited tickers, sector/industry caps, issuer concentration limits, ESG exclusion lists)
   - Set cash reserve target and rebalancing trigger thresholds (percent drift, calendar, or cash-flow driven)
   - Confirm custodian connectivity, trading permissions, and settlement instructions

2. **Portfolio Construction & Trade Generation**
   - Run model-vs-holding comparison to generate target trades
   - Apply compliance overlay pre-trade: check restriction schedule, diversification limits, and wash-sale look-back window [VERIFY wash-sale rule applicability for tax status]
   - Incorporate tax-aware logic: harvest losses where threshold is met, avoid short-term gains, respect holding-period preferences
   - Generate trade blotter with per-account allocation, noting any accounts where full model replication is infeasible (small size, restrictions, or pending cash flows)

3. **Execution & Allocation**
   - Execute block/batch trades where permissible; allocate fills pro-rata or by pre-defined rotation method
   - Document allocation methodology to satisfy SEC fair-allocation requirements [VERIFY broker-dealer vs. RIA allocation rules]
   - Reconcile executed trades against target; flag and resolve breaks same-day

4. **Compliance Overlay — Ongoing Monitoring**
   - Run post-trade compliance check confirming no guideline breaches
   - Monitor accounts daily or per policy cycle for drift beyond tolerance bands, corporate-action-induced breaches, and restriction-list updates
   - When a breach is detected: classify as active (trade-caused) or passive (market-movement); document cure timeline per IPS and regulatory requirements
   - Maintain compliance exception log with breach date, cause, resolution, and responsible party

5. **Performance Measurement & Composite Maintenance**
   - Calculate time-weighted returns (TWR) using daily valuation or Modified Dietz for sub-periods [VERIFY GIPS calculation methodology requirements for current edition]
   - Assign accounts to composites based on documented inclusion criteria; new accounts included after first full measurement period
   - Remove terminated accounts effective the last full measurement period prior to termination
   - Reconcile composite returns to underlying account returns; investigate dispersion outliers
   - Maintain composite history, asset totals, number of accounts, dispersion measure, and benchmark comparison

6. **Client Reporting & Review**
   - Produce periodic management report: holdings, transactions, performance vs. benchmark, attribution summary, compliance confirmation
   - Highlight any restriction-driven tracking difference versus model
   - Include fee calculation detail: gross-of-fee and net-of-fee returns, fee amount debited
   - Flag upcoming action items: rebalancing due, IPS review anniversary, tax-loss harvesting opportunities, or composite reassignment triggers

## Output

A structured SMA management report or operational document containing:

- **Account summary:** Current market value, asset allocation, cash position, and unrealized gain/loss
- **Performance table:** Period returns (QTD, YTD, ITD) gross and net of fees vs. benchmark; annualized returns for periods > 1 year
- **Compliance status:** Pass/fail confirmation against restriction schedule; any open exceptions with cure status
- **Transaction log:** Trades executed in the period with rationale (rebalance, cash flow, tax harvest, model change)
- **Composite snapshot** (if applicable): Composite return, dispersion, number of accounts, total composite assets, benchmark return
- **Action items:** Pending rebalances, IPS review dates, restriction schedule updates, and any items requiring client or committee decision

## Quality Checks

- Confirm restriction schedule is current — cross-reference against the most recent IPS amendment and any interim client instructions
- Verify trade allocation methodology is consistently applied and documented for fair-allocation compliance
- Reconcile composite account count and asset totals to underlying records; resolve discrepancies before publishing
- Validate that gross-of-fee and net-of-fee return calculations use the correct fee rate and billing method
- Ensure wash-sale and tax-lot tracking aligns with the account's cost-basis election at the custodian
- Check that all [VERIFY] items have been resolved for the applicable jurisdiction, tax status, and GIPS edition before finalizing
- Review for stale data: pricing, corporate actions, and restriction lists should reflect T or T-1 at most
