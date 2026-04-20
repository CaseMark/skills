---
name: conducting-structured-finance-surveillance
language: en
description: Monitors structured product performance with collateral deterioration triggers, coverage test tracking, and credit migration analysis. Use when conducting ABS surveillance, monitoring CLO performance, or tracking structured product credit.
tags:
  - process
  - structured-finance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Structured Finance Surveillance

## When To Use

- Periodic (monthly/quarterly) monitoring of ABS, MBS, CLO, or CDO performance against origination assumptions
- Evaluating whether collateral pool deterioration is approaching or breaching indenture triggers
- Tracking overcollateralization (OC) and interest coverage (IC) test compliance across tranches
- Assessing credit migration within a collateral pool (upgrades, downgrades, defaults, recovery rates)
- Preparing surveillance summaries for portfolio managers, rating agencies, or risk committees
- Responding to market stress events that may accelerate structured product deterioration

## Inputs To Gather

- **Trustee reports** — most recent and prior periods for trend analysis (remittance reports, monthly servicer reports)
- **Deal documents** — indenture/pooling and servicing agreement (PSA) with trigger definitions, waterfall priority, and event-of-default thresholds
- **Collateral tape** — loan-level or asset-level data with current balances, delinquency status, credit ratings, and loss severity
- **Coverage test levels** — current OC and IC ratios versus trigger thresholds for each tranche
- **Rating agency actions** — recent rating changes on underlying collateral or tranche ratings
- **Market data** — relevant index spreads (e.g., CLOIE, ABX), discount margins, and comparable deal pricing
- **Historical performance data** — vintage curves for delinquency, default, prepayment (CPR/CDR/severity)

## Workflow

1. **Establish surveillance baseline**
   - Confirm deal structure: tranche stack, subordination levels, credit enhancement mechanisms (excess spread, reserve accounts, OC)
   - Map trigger definitions from the indenture — identify OC/IC trigger levels, reinvestment period end date, and event-of-default thresholds
   - Note any structural features: turbo amortization, payment-in-kind toggles, ramp-up provisions (CLOs), clean-up call thresholds

2. **Analyze collateral pool performance**
   - Calculate period-over-period changes in pool factor, weighted average coupon (WAC), weighted average life (WAL), and weighted average rating factor (WARF)
   - Stratify delinquency buckets (30/60/90+ DPD) and compare to prior periods and original expectations
   - For CLOs: assess CCC-bucket concentration (typically >7.5% triggers OC haircut), identify assets trading below par, flag defaulted or credit-risk obligations [VERIFY: specific CCC threshold per deal indenture]
   - For ABS/MBS: track cumulative net loss (CNL) against vintage loss curves and original rating agency base/stress scenarios
   - Compute constant default rate (CDR), constant prepayment rate (CPR), and loss severity trends

3. **Run coverage test compliance**
   - Calculate current OC ratio: (collateral par or market value) / (tranche par outstanding) for each trigger level
   - Calculate current IC ratio: (interest collections) / (interest due on covered tranches)
   - Compare to trigger thresholds — flag any breach or cushion below 50 bps of trigger
   - If triggers are breached: trace waterfall consequences (diversion of interest proceeds, accelerated principal paydown to senior tranches, cessation of reinvestment)
   - Track cure trajectory — is the breach worsening, stable, or recovering?

4. **Assess credit migration**
   - Tally rating upgrades vs. downgrades in the collateral pool since last review
   - Compute WARF drift and compare to maximum permitted WARF [VERIFY: deal-specific WARF covenant]
   - Identify sector or obligor concentration shifts — flag single-obligor or single-industry exposure exceeding indenture limits
   - For CLOs: review trading activity (purchases/sales) and assess whether the collateral manager is defensively rotating or reaching for yield

5. **Evaluate structural protections**
   - Assess remaining credit enhancement as a percentage of current pool balance
   - Calculate excess spread trends — declining excess spread is an early warning signal
   - Review reserve account balances relative to required levels
   - For amortizing deals: check whether paydown priority has shifted (sequential vs. pro-rata) due to trigger events

6. **Compile surveillance output**
   - Produce a structured surveillance summary (see Output section)
   - Flag any action items: watchlist additions, trigger breaches requiring escalation, recommended position changes
   - Compare current performance to original underwriting thesis — note where assumptions have diverged materially

## Output

The surveillance report should include:

- **Deal summary header** — deal name, asset class, originator/manager, closing date, current pool factor
- **Coverage test dashboard** — table showing each tranche's OC/IC ratio, trigger level, cushion, and pass/fail status
- **Collateral performance snapshot** — delinquency stratification, CDR/CPR/severity, WARF, CCC bucket %, and period-over-period trends
- **Credit migration table** — count and notional of upgrades, downgrades, defaults, and recoveries since last report
- **Trigger watch section** — any tests within 100 bps of breach, with projected trajectory under base and stress scenarios
- **Structural commentary** — credit enhancement adequacy, excess spread trend, waterfall implications of any current trigger breaches
- **Action items and recommendations** — watchlist changes, escalation flags, suggested portfolio actions (hold/reduce/exit)

## Quality Checks

- Verify that OC/IC calculations match the trustee report — reconcile any discrepancies before publishing
- Confirm trigger thresholds are sourced from the actual indenture, not from memory or generic assumptions [VERIFY]
- Validate that collateral tape totals (par balance, number of assets) tie to the trustee report
- Cross-check WARF calculations using the applicable rating agency methodology (Moody's vs. S&P vs. Fitch scales differ) [VERIFY: which agency methodology governs per indenture]
- Ensure delinquency and default definitions match the PSA/indenture (e.g., payment default vs. bankruptcy default vs. distressed exchange)
- Flag any data gaps — missing servicer reports, stale collateral tapes, or unrated assets — rather than assuming values
- Confirm that all period-over-period comparisons use consistent reporting dates and methodologies
