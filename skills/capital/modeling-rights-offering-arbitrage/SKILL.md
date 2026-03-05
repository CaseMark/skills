---
name: modeling-rights-offering-arbitrage
description: Analyzes rights offering dynamics with theoretical ex-rights price, subscription premium, and nil-paid value calculation. Use when evaluating rights offerings, modeling TERP, or analyzing subscription arbitrage.
tags:
  - modeling
  - activist-and-event-driven-investing
metadata:
  author: casemark
  practice_areas:
    - Activist Investing
    - Event-Driven Strategy
    - Special Situations
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Rights Offering Arbitrage

## When To Use

- Issuer announces a rights offering and you need to model the theoretical ex-rights price (TERP) to evaluate fair value impact
- Evaluating whether nil-paid rights are mispriced relative to the subscription price and cum-rights share price
- Sizing an arbitrage position by comparing the market price of nil-paid rights to their theoretical value
- Assessing dilution impact on existing shareholders who do not exercise
- Analyzing an activist's strategy where a rights offering is used as a defensive or offensive capital structure tool
- Modeling oversubscription privilege economics and backstop commitment fees

## Inputs To Gather

- **Cum-rights share price** — last traded price before the ex-rights date (or current price if pre-ex-date)
- **Subscription price** — the price at which new shares can be purchased under the offering
- **Rights ratio** — number of existing shares required to subscribe for one new share (e.g., 4:1 means 4 old shares yield 1 right to buy 1 new share)
- **Total shares outstanding** (pre-offering) and **new shares to be issued**
- **Gross offering proceeds** and any **backstop/standby fees**
- **Key dates** — record date, ex-rights date, subscription period, oversubscription deadline, closing date
- **Oversubscription terms** — whether oversubscription privilege exists, any pro-rata allocation mechanics
- **Market data** — nil-paid rights trading price (if rights are renounceable and listed), sector comps, short borrow availability
- **Issuer-specific context** — reason for offering (deleveraging, acquisition financing, regulatory capital), any concurrent transactions

## Workflow

1. **Calculate TERP**
   - TERP = (Cum-rights price × Existing shares + Subscription price × New shares) / (Existing shares + New shares)
   - Express TERP discount to cum-rights price as a percentage

2. **Derive theoretical nil-paid rights value**
   - Theoretical value per right = (Cum-rights price − Subscription price) / (Rights ratio + 1)
   - Alternative: TERP − Subscription price (value of one right when one right is needed per new share)
   - Confirm which formula applies based on the specific rights ratio structure

3. **Assess subscription premium / discount**
   - Compare the subscription price to TERP — a deeper discount incentivizes take-up
   - Flag if discount is unusually shallow (<10%) as this increases non-exercise risk and rights value volatility

4. **Model arbitrage P&L scenarios**
   - **Fully hedged arbitrage**: Buy nil-paid rights, subscribe for shares, short sell equivalent shares at TERP or market price; P&L = market price of rights vs. theoretical value minus borrow cost, execution slippage, and fees
   - **Unhedged participation**: Subscribe and hold — model upside/downside to TERP under bull/bear share price scenarios
   - **Rights sale**: Sell nil-paid rights in the market — compare to theoretical value and factor in liquidity discount

5. **Run dilution and ownership analysis**
   - Model post-offering ownership for participating vs. non-participating shareholders
   - Calculate wealth transfer from non-exercising to exercising shareholders
   - If an activist holds a disclosed stake, model their post-offering ownership under full exercise, partial exercise, and oversubscription scenarios

6. **Sensitivity analysis**
   - Vary cum-rights share price (±5%, ±10%, ±20%) and recalculate TERP, nil-paid value, and arbitrage P&L
   - Vary take-up rate (70%, 85%, 100%) to assess oversubscription allocation and backstop exposure
   - Stress-test borrow cost assumptions for the short leg of the hedge

7. **Timeline and execution risk**
   - Map key dates to identify the subscription window and settlement lag
   - Flag jurisdictional restrictions on rights trading or short selling [VERIFY]
   - Note any regulatory approvals required before closing (e.g., antitrust, banking regulator capital approval) [VERIFY]

## Output

- **TERP summary table**: Cum-rights price, subscription price, rights ratio, TERP, TERP discount %, theoretical nil-paid value
- **Arbitrage P&L matrix**: Scenarios across share price movements and take-up rates, showing gross and net P&L per share/right
- **Dilution waterfall**: Pre- and post-offering share counts, ownership percentages for key holders, and wealth transfer to/from non-exercisers
- **Key dates timeline**: Record date through settlement, with trading windows for nil-paid rights
- **Risk flags**: Liquidity of nil-paid rights market, borrow availability for hedging, regulatory or jurisdictional constraints, backstop counterparty risk

## Quality Checks

- Confirm TERP is between the subscription price and cum-rights price — if not, recheck inputs
- Verify nil-paid rights value is positive; a negative value implies subscription price exceeds cum-rights price (a deeply distressed scenario requiring separate analysis)
- Cross-check total offering proceeds = subscription price × new shares issued
- Ensure dilution math reconciles: new shares / (existing + new) = dilution percentage
- Validate that arbitrage P&L accounts for all friction costs (borrow, commissions, FX if cross-listed)
- If nil-paid rights are trading, compare theoretical value to market price and explain any material divergence (liquidity premium, time value, hedging demand)
- Mark any jurisdiction-specific tax treatment of rights (e.g., CGT treatment of nil-paid rights sales) with [VERIFY]
