---
name: preparing-trading-desk-risk-reports
description: Structures trading desk risk reporting with P&L attribution, position summaries, and limit utilization tracking. Use when preparing desk risk reports, attributing trading P&L, or monitoring position limits.
tags:
  - preparation
  - public-markets-and-trading
  - risk
  - trading
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Preparation Document
  skill_modes:
    - Preparation
---
# Preparing Trading Desk Risk Reports

## When To Use

- End-of-day or intraday risk reporting for a trading desk (equities, fixed income, FX, commodities, derivatives)
- P&L attribution requests from desk heads, risk managers, or front-office management
- Limit utilization monitoring and breach escalation reporting
- Preparing risk summaries for morning risk meetings, CRO briefings, or regulatory snapshots
- Ad hoc position analysis following significant market moves or unusual trading activity

## Inputs To Gather

- **Position data**: Current holdings by instrument, asset class, and strategy book — include notional, quantity, and market value
- **P&L feeds**: Realized P&L, unrealized (mark-to-market) P&L, and any adjustments (e.g., reserve releases, valuation adjustments like XVA)
- **Risk sensitivities**: Greeks (delta, gamma, vega, theta) for options desks; DV01/CS01 for fixed income; beta and factor exposures for equity desks
- **Limit framework**: Approved risk limits (VaR, notional, concentration, stop-loss, Greeks) and current utilization levels
- **Market data**: Relevant benchmarks, index levels, yield curves, implied vol surfaces as of the reporting timestamp
- **Prior-day report**: Previous desk risk report for comparison and trend analysis
- **Desk parameters**: Desk name, reporting currency, books covered, reporting date/time, any desk-specific conventions

## Workflow

1. **Validate source data**
   - Confirm position and P&L feeds are complete for all books in scope
   - Reconcile total P&L to independent sources (finance feed, prime broker statements)
   - Check for stale prices, missing marks, or broken instrument links — flag with [VERIFY] if unresolved

2. **Build position summary**
   - Aggregate positions by asset class, sector/issuer, currency, and strategy book
   - Identify top 10 positions by notional and by risk contribution
   - Highlight new positions entered since prior report and positions closed out
   - Note any concentrated positions exceeding single-name or sector thresholds [VERIFY: confirm desk-specific concentration limits]

3. **Prepare P&L attribution**
   - Break P&L into components: market moves (delta/duration), carry/roll-down, theta/time decay, volatility (vega), new trade P&L, and residual/unexplained
   - For each component, show the contribution in reporting currency and as percentage of total P&L
   - Compare day-over-day and MTD/YTD figures against prior report
   - Flag any unexplained P&L exceeding the desk's materiality threshold — typically >5-10% of total daily P&L [VERIFY: desk-specific materiality policy]

4. **Compile limit utilization**
   - For each risk limit (VaR, stress VaR, notional, Greeks, stop-loss), report: limit amount, current usage, utilization percentage, headroom remaining
   - Color-code or tier utilization: green (<75%), amber (75-90%), red (>90%), breach (>100%)
   - For any amber/red/breach status, include: cause of elevated utilization, whether a temporary limit exception is in place, and proposed remediation or timeline to reduce
   - Track cumulative stop-loss triggers (MTD realized loss vs. stop-loss limit) [VERIFY: stop-loss policy reset frequency — daily, weekly, monthly]

5. **Add risk commentary**
   - Summarize the desk's directional bias and key risk drivers in 3-5 sentences
   - Note upcoming events that may affect the book (earnings, central bank decisions, economic releases, option expirations)
   - Reference any relevant stress test or scenario analysis results if available
   - If VaR back-testing exceptions have occurred recently, note the count and status

6. **Format and finalize**
   - Structure the report with consistent section headings: Executive Summary, Position Overview, P&L Attribution, Limit Utilization, Risk Commentary
   - Use tables for position and limit data; keep narrative sections concise
   - Stamp with as-of date/time, reporting currency, and desk identifier
   - Ensure figures reconcile across sections (e.g., total P&L in attribution matches executive summary)

## Output

A structured trading desk risk report containing:

- **Executive summary**: 3-5 line snapshot of net P&L, largest risk drivers, and limit status
- **Position summary table**: Top positions by notional and risk, with asset class and sector breakdowns
- **P&L attribution table**: Component-level breakdown (delta, carry, theta, vega, new trade, residual) with day, MTD, YTD columns
- **Limit utilization dashboard**: Each limit with usage, headroom, and RAG status
- **Risk commentary**: Narrative on directional exposure, upcoming catalysts, and any escalation items

## Quality Checks

- Total P&L in attribution section ties to executive summary and position-level P&L roll-up (zero tolerance for mismatch)
- All limit figures reference the correct approved limit amount — cross-check against the limit management system or latest limit memo
- No stale or missing marks remain without a [VERIFY] flag
- Unexplained P&L is quantified and does not exceed desk materiality threshold without commentary
- Reporting timestamp and currency are clearly stated and consistent throughout
- Any limit breach or amber status includes an explanation and remediation note
- Greek/sensitivity totals at the desk level equal the sum of book-level components
- Report is ready for distribution by the desk's reporting deadline [VERIFY: confirm specific cutoff time for the desk]
