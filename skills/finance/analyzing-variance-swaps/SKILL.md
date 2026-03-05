---
name: analyzing-variance-swaps
description: Structures variance and volatility swap pricing with realized/implied vol analysis and hedging. Use when pricing variance swaps, analyzing vol risk premium, or hedging volatility exposure.
tags:
  - analysis
  - quantitative-finance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Variance Swaps

## When To Use

- Pricing a new variance or volatility swap trade (long or short variance)
- Evaluating the variance risk premium (VRP) to determine if selling/buying variance is attractive
- Hedging a portfolio's volatility exposure via variance swaps rather than vanilla options
- Marking existing variance swap positions to market
- Analyzing realized vs. implied volatility divergence for a specific underlier
- Structuring capped or conditional variance swaps to limit tail exposure

## Inputs To Gather

- **Underlier details**: Ticker, asset class (equity index, single stock, FX, commodity), spot price
- **Contract terms**: Variance notional (vega notional), strike volatility (Kvol), maturity date, observation frequency (daily close-to-close vs. intraday), day count convention, market disruption provisions
- **Implied volatility surface**: Full strike/expiry grid from listed options; at minimum the ATM term structure and 25-delta skew at the relevant tenor
- **Realized volatility history**: Close-to-close log returns for the underlier over trailing windows matching the swap tenor (30d, 60d, 90d, etc.) plus a longer lookback (1y, 3y) for context
- **Hedging context**: Existing portfolio Greeks (vega, gamma, vanna, volga) if the swap is intended as a hedge
- **Cap/floor provisions**: Whether the swap includes a cap on realized variance (common for single-name swaps to limit short-variance blowup risk)

## Workflow

1. **Compute fair variance strike**
   - Replicate the variance swap payoff using the strip of OTM puts and calls weighted by 1/K² across all available strikes [VERIFY: confirm available strike range covers at least 2 standard deviations from ATM to avoid truncation bias]
   - Apply the standard replication integral: K²_var = (2/T) × [∫ (P(K)/K²) dK + ∫ (C(K)/K²) dK], discretized over the listed option chain
   - Adjust for discrete monitoring: apply the Broadie-Jain or similar correction factor for daily vs. continuous sampling
   - Convert between variance strike (K²_var) and volatility strike (Kvol = √K²_var) as needed

2. **Assess the variance risk premium**
   - Compare the fair variance strike to trailing realized volatility at the matching tenor
   - Calculate the historical VRP: VRP = implied variance − realized variance, expressed in vol points
   - Contextualize the current VRP percentile within the historical distribution (where does today's VRP sit in the 1y/3y/5y range?)
   - If VRP is wide relative to history, selling variance is relatively attractive; if compressed, buying variance or staying flat may be preferred

3. **Analyze convexity and P&L profile**
   - Variance swaps pay on variance (σ²), not volatility — model the nonlinear P&L: Settlement = Notional_var × (σ²_realized − K²_var)
   - Translate variance notional to vega notional for intuition: Vega_notional = Var_notional × 2 × Kvol
   - Stress-test P&L under realized vol scenarios: Kvol ± 5 pts, Kvol ± 10 pts, and a 2008/2020-style tail event
   - For capped variance swaps, model the payoff truncation and quantify the cap's value (difference between uncapped and capped fair strike)

4. **Evaluate hedging and Greeks**
   - Delta: variance swaps are initially delta-neutral but accumulate dollar-gamma exposure; quantify the gamma P&L per 1% underlier move
   - Vega/volga: compute sensitivity to parallel shifts and curvature changes in the vol surface
   - If hedging an existing book, show the net portfolio Greeks before and after adding the variance swap position
   - Identify residual risks: gap risk (overnight jumps not captured by close-to-close), correlation risk (for basket variance swaps), and dividend risk (for equity underliers)

5. **Mark-to-market existing positions**
   - For seasoned swaps, split value into accrued variance (locked in from observations already passed) and residual variance (implied by options for the remaining tenor)
   - MTM = Notional_var × [(T_elapsed/T_total) × σ²_realized_so_far + (T_remaining/T_total) × K²_var_implied_remaining − K²_var_original], discounted at the risk-free rate
   - Report unrealized P&L and current delta/gamma exposure

## Output

The analysis report should include:

- **Trade summary table**: Underlier, notional (variance and vega), strike (variance and vol), tenor, cap (if any), observation convention
- **Fair value analysis**: Replication-derived fair strike vs. quoted dealer strike, with the implied bid-offer in vol points
- **VRP assessment**: Current VRP level, historical percentile, and directional view (rich/fair/cheap)
- **P&L scenario matrix**: Grid of settlement values across a range of realized vol outcomes (e.g., 10%, 15%, 20%, 25%, 30%, 40%) showing payoff in currency terms
- **Greeks summary**: Vega notional, dollar gamma, volga, and any residual exposures
- **Hedging recommendation**: Whether the swap achieves the intended hedge objective, with net Greeks after overlay
- **Risk flags**: Tail risk under extreme scenarios, truncation bias warnings, liquidity considerations for the replicating strip

## Quality Checks

- Confirm the replication integral uses a sufficiently wide strike range; flag if the lowest put strike is above 70% of spot or the highest call strike is below 130% of spot [VERIFY: adjust thresholds based on underlier — single stocks need wider wings than indices]
- Verify the variance notional / vega notional conversion is consistent: Vega_notional = Var_notional × 2 × Kvol
- Cross-check the fair strike against dealer quotes or CBOE VIX methodology (for S&P 500 underlier) to validate the replication
- Ensure realized vol calculations use log returns (ln(S_t/S_{t-1})), not simple returns, and apply the correct annualization factor (typically √252 for daily data) [VERIFY: confirm trading day convention for the specific market]
- For capped variance swaps, verify the cap level is stated in variance terms (not vol terms) and the P&L payoff correctly reflects the truncation
- Confirm day count and observation frequency match the ISDA variance swap confirmation terms
- Flag any market disruption days (exchange holidays, trading halts) and confirm the contractual treatment (omit vs. carry forward)
