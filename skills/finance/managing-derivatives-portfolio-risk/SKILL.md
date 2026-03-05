---
name: managing-derivatives-portfolio-risk
description: Structures derivatives portfolio risk with Greek sensitivities, scenario analysis, and hedging strategies. Use when managing derivatives risk, analyzing Greek exposures, or designing hedge strategies.
tags:
  - management
  - quantitative-finance
  - risk
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Derivatives Portfolio Risk

Structures derivatives portfolio risk reporting around Greek sensitivities, scenario analysis, and hedging strategies for options, swaps, and structured products portfolios.

## When To Use

- Producing a periodic (daily/weekly) derivatives risk report for portfolio managers or risk committees
- Analyzing aggregate Greek exposures (delta, gamma, vega, theta, rho) across a multi-asset derivatives book
- Designing or evaluating hedge overlays to neutralize specific risk dimensions
- Running stress/scenario analysis on a derivatives portfolio ahead of major events (earnings, FOMC, expiry clusters)
- Assessing P&L attribution driven by Greeks versus residual/unexplained moves

## Inputs To Gather

- **Position data**: Instrument type (vanilla options, exotics, swaps, swaptions, structured notes), underlier, notional, strike/barrier levels, expiry dates, and direction (long/short)
- **Market data snapshot**: Spot/forward prices, implied volatility surfaces, yield curves, dividend schedules, correlation matrices
- **Greek sensitivities**: Position-level and portfolio-level delta, gamma, vega, theta, rho; cross-Greeks (vanna, volga/vomma, charm) where material
- **Risk limits**: Approved thresholds for each Greek at desk, strategy, and portfolio level
- **Scenario definitions**: Standard shocks (e.g., underlier +/- 5%, 10%; vol +/- 5 vols; rate +/- 25 bps, 50 bps) and event-specific scenarios
- **Hedge instruments available**: Liquid hedging vehicles, cost constraints, execution limits
- **Pricing model details**: Model type (Black-Scholes, local vol, stochastic vol, SABR) and key calibration parameters [VERIFY model governance and approved model list per desk policy]

## Workflow

1. **Aggregate Greek exposures**
   - Roll up position-level Greeks to strategy, asset class, and portfolio level
   - Distinguish linear Greeks (delta, rho) from convexity Greeks (gamma, vanna) and volatility Greeks (vega, volga)
   - Identify concentrations: large single-name exposures, expiry clusters, strike pinning risk

2. **Assess limit utilization**
   - Compare each Greek against approved risk limits at every aggregation level
   - Flag breaches and near-breaches (e.g., >80% utilization) with breach magnitude and duration
   - Note any temporary limit extensions or waivers in effect [VERIFY current limit framework with risk management]

3. **Run scenario and stress analysis**
   - Apply standard shock grids: underlier moves vs. vol moves (delta-vega matrix), rate curve shifts
   - Run named scenarios: flash crash, vol spike, curve inversion, liquidity freeze
   - Compute portfolio P&L impact under each scenario, decomposed by Greek contribution
   - Highlight non-linear payoff cliffs — areas where small additional moves cause disproportionate losses (negative gamma pockets, barrier proximity)

4. **Design or evaluate hedging strategy**
   - Identify the dominant risk dimension to hedge first (typically the largest limit breach or highest scenario loss driver)
   - Propose hedge trades with instrument, size, and expected Greek offset
   - Estimate hedge cost: premium outlay, carry (theta drag), bid-ask slippage, margin impact
   - Assess residual risk post-hedge — confirm no new secondary exposures introduced (e.g., hedging vega with options adds gamma)
   - For cross-asset books, evaluate correlation-based hedges and note basis risk [VERIFY correlation assumptions against recent realized data]

5. **Compile risk report**
   - Present a Greek summary table (portfolio-level and by strategy/asset class)
   - Include scenario P&L heatmap (underlier shock x vol shock matrix)
   - Show limit utilization dashboard with traffic-light indicators
   - Summarize recommended hedging actions with cost/benefit analysis
   - Note key risk themes: upcoming expiries, illiquid positions, model risk concerns

## Output

A derivatives portfolio risk report containing:

- **Greek exposure summary**: Table showing delta, gamma, vega, theta, rho (and material cross-Greeks) at portfolio and sub-portfolio level, with units clearly stated (e.g., delta in equivalent shares or notional, gamma in dollar-gamma per 1% move, vega in P&L per 1 vol point)
- **Limit utilization dashboard**: Current exposure vs. limit for each Greek, with breach flags
- **Scenario analysis grid**: P&L estimates under defined stress scenarios with Greek-level decomposition
- **Hedging recommendations**: Specific trades, expected cost, and projected post-hedge risk profile
- **Risk commentary**: Narrative highlighting top 3-5 risk themes, action items, and escalation points

## Quality Checks

- Greeks are internally consistent: delta-hedged portfolio should show near-zero delta; gamma sign should align with option position direction (long options = long gamma)
- Scenario P&L results cross-check against Greek approximations (first-order delta*dS + second-order 0.5*gamma*dS^2 should approximate scenario results for moderate moves)
- Hedge notionals are realistic relative to market liquidity — flag any hedge that exceeds 10% of average daily volume in the instrument [VERIFY liquidity thresholds per asset class]
- No stale market data: confirm all vol surfaces and curves are from the same valuation timestamp
- Verify that exotic positions use the correct pricing model and that Greeks are bumped numerically (not analytically) where closed-form Greeks are unreliable [VERIFY model validation status]
- Report units and sign conventions are consistent throughout (e.g., long vega is positive, theta decay is negative for long options)
- All limit breaches have corresponding action items or documented risk acceptance
