---
name: modeling-event-driven-trading-analysis
language: en
description: Analyzes event-driven opportunities with catalyst identification, pricing efficiency assessment, and risk/reward evaluation. Use when analyzing event-driven situations, evaluating catalysts, or assessing event timing.
tags:
  - modeling
  - public-markets-and-trading
  - risk
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Event Driven Trading Analysis

## When To Use

- Evaluating M&A arbitrage spreads (merger arb, tender offers, spin-offs)
- Analyzing corporate actions as catalysts (earnings, restructurings, dividend changes, share buybacks)
- Assessing regulatory or legal event outcomes (FDA decisions, antitrust rulings, litigation verdicts)
- Pricing event-driven situations where a discrete catalyst will resolve pricing uncertainty within a known timeframe
- Screening for mispriced optionality around scheduled or anticipated corporate/macro events

## Inputs To Gather

- **Event specification**: Type of event, expected date or date range, involved entities, and deal/event terms
- **Security data**: Current price, implied volatility, options chain (if applicable), historical price action around prior similar events, short interest, borrow cost
- **Deal/event terms**: Consideration offered (cash, stock, mixed), conditions precedent, regulatory approvals required, breakup/termination fees [VERIFY deal terms against latest proxy/filing]
- **Comparable precedents**: Historical completion rates for similar event types, typical timeline from announcement to close, historical spread behavior
- **Market microstructure**: Liquidity profile, bid-ask spreads, average daily volume, institutional ownership concentration
- **Risk factors**: Identified deal/event risks—antitrust, financing contingencies, shareholder vote thresholds, MAC clauses

## Workflow

1. **Classify the event type and define the scenario tree**
   - Identify the primary catalyst (e.g., merger close, FDA approval, earnings surprise)
   - Map discrete outcomes: success/close, failure/break, modified terms, delayed timeline
   - Assign initial probability estimates to each branch based on precedent data

2. **Establish pricing under each scenario**
   - For M&A: calculate deal-close value (offer price adjusted for proration, collar, CVR), break price (standalone or re-rate target)
   - For binary events (FDA, litigation): estimate upside and downside price targets using comps, DCF, or historical event-day moves
   - For earnings/guidance: model beat/miss/inline scenarios with magnitude estimates anchored to consensus dispersion

3. **Compute expected value and spread analysis**
   - Calculate probability-weighted expected return across scenarios
   - Annualize the gross spread for time-value comparison: `Annualized Return = (Gross Spread / Current Price) × (365 / Days to Close)`
   - Compare annualized return to cost of capital, financing costs, and borrow costs for short legs

4. **Assess risk/reward asymmetry**
   - Calculate downside-to-upside ratio: `D/U = |Break Loss| / |Deal Gain|`
   - Determine implied probability of completion priced into the current spread: `Implied Prob = Downside / (Downside + Upside)`
   - Compare implied probability to your estimated probability—identify edge or lack thereof

5. **Model timing and carry dynamics**
   - Estimate timeline to resolution with confidence intervals
   - Calculate carry cost: financing, borrow fees, dividend differentials, opportunity cost
   - Stress-test returns under delayed-close scenarios (e.g., +30, +60, +90 days)

6. **Run sensitivity analysis**
   - Vary completion probability (±10–20%) and observe impact on expected return
   - Vary break price (±5–15% from base case) to capture valuation uncertainty
   - Test portfolio-level impact if running multiple event positions simultaneously

7. **Construct position sizing and hedging framework**
   - Size based on Kelly criterion or fractional-Kelly given confidence level
   - Identify hedging instruments: put spreads for downside, index hedges for systematic risk, pairs for sector exposure
   - Define stop-loss triggers tied to fundamental milestones (e.g., regulatory objection, financing withdrawal) rather than arbitrary price levels

## Output

- **Event summary table**: Event type, key dates, involved parties, current spread, implied probability
- **Scenario matrix**: Each outcome branch with probability, target price, return, and annualized return
- **Expected value calculation**: Probability-weighted return, edge vs. implied market pricing
- **Risk metrics**: Downside/upside ratio, max loss, carry cost per month, breakeven hold period
- **Sensitivity tables**: Return sensitivity to probability changes, break-price changes, and timeline delays
- **Position recommendation**: Suggested sizing, entry levels, hedge structure, and catalyst-driven exit triggers

## Quality Checks

- Implied probability derived from the spread must be internally consistent with the scenario prices used
- Annualized returns must account for actual expected days-to-close, not just announced target date
- Break price estimates should be supported by at least two independent methods (comps, pre-announcement price, DCF)
- Verify all deal terms against the most recent SEC filing or equivalent disclosure [VERIFY]
- Confirm borrow availability and cost for any short legs before finalizing the model [VERIFY]
- Cross-check event timeline against regulatory calendars (e.g., HSR waiting periods, FDA PDUFA dates) [VERIFY]
- Flag any position where gross spread is less than 2× estimated carry cost as marginal
- Ensure scenario probabilities sum to 100% and no outcome branch is omitted
