---
name: analyzing-alpha-signal-decay
description: Evaluates signal half-life, turnover implications, and capacity constraints for systematic alpha factors. Use when analyzing signal persistence, evaluating factor decay, or estimating strategy capacity.
tags:
  - analysis
  - quantitative-capital-strategies
metadata:
  author: casemark
  practice_areas:
    - Quantitative Investing
    - Systematic Strategies
    - Factor Investing
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Alpha Signal Decay

## When To Use

- Evaluating whether an alpha signal retains predictive power across different holding periods
- Determining optimal rebalance frequency by measuring how quickly signal strength deteriorates
- Estimating strategy capacity limits before market impact erodes expected returns
- Comparing decay profiles across candidate factors during signal selection or portfolio construction
- Assessing whether a live signal has degraded relative to its backtested decay curve (alpha erosion monitoring)

## Inputs To Gather

- **Signal return series**: Period-by-period returns for portfolios sorted by the signal (e.g., decile or quintile long/short spreads)
- **Holding-period returns matrix**: Returns measured at 1-day, 5-day, 10-day, 21-day, 63-day, and 126-day forward windows
- **Turnover data**: Portfolio turnover rate at each rebalance frequency; round-trip transaction cost estimate (bps)
- **Universe and dates**: Investable universe definition, backtest start/end dates, any regime breaks or structural changes
- **AUM or notional size**: Current or projected strategy size for capacity analysis
- **Market impact model parameters**: Participation rate assumptions, ADV percentiles, spread estimates [VERIFY — impact model choice varies by asset class and execution venue]

## Workflow

1. **Construct the decay curve**
   - Compute the information coefficient (IC) or long/short spread return at each forward horizon (1d through 126d)
   - Plot IC vs. holding period; fit an exponential decay model IC(t) = IC₀ · e^(−λt) to estimate the decay constant λ
   - Derive the signal half-life: t½ = ln(2) / λ
   - Report confidence intervals around half-life using bootstrapped IC series

2. **Assess turnover cost breakeven**
   - Calculate implied turnover at each rebalance frequency from the signal's rank-change rate
   - Multiply turnover by estimated round-trip cost to get the cost drag per period
   - Identify the breakeven rebalance frequency where gross alpha minus cost drag is maximized
   - Flag if optimal rebalance is faster than operationally feasible settlement or execution cycles [VERIFY — settlement cycles differ by market and instrument type]

3. **Estimate capacity constraints**
   - For each rebalance, estimate total dollars traded per period
   - Apply market impact model (e.g., square-root impact: cost ∝ √(participation rate)) to compute expected slippage at increasing AUM levels
   - Find the AUM level where net-of-impact alpha falls below a minimum threshold (e.g., 0 bps or a target Sharpe hurdle)
   - Produce a capacity curve: net alpha vs. AUM

4. **Diagnose decay regime and crowding risk**
   - Compare decay profile across sub-periods (pre/post publication, different volatility regimes)
   - Check if half-life has shortened over time — an indicator of signal crowding or information diffusion
   - Cross-reference with short-interest, ETF flow, or factor-crowding proxies if available
   - Note any structural breaks where decay accelerated (new data vendors, regulatory changes, competing strategy launches)

5. **Synthesize findings into actionable recommendations**
   - Recommend hold period and rebalance cadence consistent with the decay profile
   - State capacity ceiling with assumptions made explicit
   - Identify risk: if half-life is near or below the cost-breakeven horizon, flag the signal as capacity-constrained or potentially non-viable at scale
   - Suggest mitigants (partial rebalancing, execution algorithm tuning, blending with slower-decay signals)

## Output

The deliverable is a structured **Signal Decay Analysis Report** containing:

- **Signal summary table**: signal name, universe, backtest period, IC₀, half-life, decay constant
- **Decay curve chart**: IC or spread return vs. forward horizon with fitted exponential overlay
- **Turnover-cost analysis**: table of rebalance frequency vs. gross alpha, cost drag, and net alpha
- **Capacity curve**: net alpha vs. AUM chart with annotated capacity ceiling
- **Regime comparison**: sub-period half-lives and any crowding indicators
- **Recommendation**: optimal rebalance cadence, maximum deployable AUM, and risk flags

## Quality Checks

- Verify that IC calculations use point-in-time data with no lookahead bias in signal construction
- Confirm transaction cost assumptions reflect realistic execution for the asset class and AUM level [VERIFY — cost estimates should be calibrated to actual fills or TCA data where available]
- Ensure half-life estimate is stable across bootstrap samples; flag if confidence interval spans more than 2× the point estimate
- Check that capacity estimate accounts for correlated liquidation risk (other funds trading the same signal)
- Validate that decay curve uses non-overlapping or bias-adjusted overlapping returns to avoid autocorrelation inflation
- Cross-check turnover calculations against actual portfolio rebalance logs if the signal is already in production
