---
name: analyzing-correlation-trading
description: Structures correlation analysis with index vs. tranche pricing and correlation skew assessment. Use when analyzing correlation products, pricing tranches, or evaluating dispersion trades.
tags:
  - analysis
  - quantitative-finance
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
# Analyzing Correlation Trading

## When To Use

- Pricing or relative-value assessment of synthetic CDO tranches (equity, mezzanine, senior)
- Evaluating index vs. single-name basis (e.g., CDX.NA.IG/HY vs. constituent CDS)
- Analyzing correlation skew across the capital structure of a credit index
- Structuring or assessing dispersion trades (long index protection / short single-name protection, or vice versa)
- Reviewing implied correlation surfaces for mark-to-market or risk reporting
- Stress-testing a correlation book against regime shifts (crisis spikes, mean-reversion)

## Inputs To Gather

- **Index data**: Current and historical spreads for the relevant index (CDX, iTraxx) and series/roll
- **Tranche quotes**: Mid-market prices or upfronts for standard tranches (e.g., 0-3%, 3-7%, 7-15%, 15-30%, 30-100% for CDX.IG)
- **Single-name CDS spreads**: Constituent spreads, recovery rate assumptions, and any jump-to-default premia
- **Implied correlation levels**: Base correlations or compound correlations per tranche from dealer runs or internal models
- **Historical realized correlation**: Pairwise or average asset-correlation estimates from equity proxies or CDS co-movements over chosen lookback windows
- **Model parameters**: Copula type (Gaussian, Student-t, Marshall-Olkin), number of simulation paths, granularity of loss distribution [VERIFY: confirm model convention used by the desk]
- **Market context**: Recent credit events, index rolls, on-the-run vs. off-the-run dynamics, funding/repo costs

## Workflow

1. **Reconstruct the base correlation curve**
   - Compute compound correlation for each tranche using the standard Gaussian copula and quoted tranche spreads/upfronts
   - Convert to base correlation by bootstrapping from equity tranche up through super-senior
   - Flag any non-monotonicity in the base correlation curve — this indicates arbitrage or stale quotes

2. **Assess correlation skew**
   - Compare current base correlation levels to 3-month, 6-month, and 1-year historical ranges
   - Identify whether equity tranche implied correlation is rich or cheap relative to mezzanine/senior
   - Note skew steepness: a flat skew suggests low differentiation between subordination levels; a steep skew signals tail-risk repricing

3. **Index vs. intrinsics analysis**
   - Calculate the theoretical index spread from the sum of single-name constituents weighted by notional
   - Compute the index basis (market index spread minus intrinsic spread)
   - A persistently negative basis (index trading tight to intrinsics) may indicate correlation supply; a positive basis suggests demand for index protection or single-name tightening

4. **Dispersion trade evaluation**
   - Define the trade structure: long index vs. short basket of single names (or reverse), specifying delta-neutral notionals
   - Estimate P&L sensitivity to parallel spread moves (DV01), idiosyncratic spread moves, and correlation changes (CR01)
   - Model carry and roll-down under stable-spread scenarios
   - Stress-test against historical episodes: 2008 credit crisis, 2011 European sovereign stress, 2020 COVID dislocation [VERIFY: update with most recent relevant stress period]

5. **Risk decomposition**
   - Break total tranche risk into spread risk (CS01), default risk (jump-to-default), and correlation risk (CR01)
   - Quantify gamma/convexity for equity and thin mezzanine tranches — these exhibit significant non-linearity
   - Assess vega exposure if using stochastic-correlation or stochastic-recovery extensions

6. **Compile findings and relative-value view**
   - Summarize whether the current skew environment favors long or short correlation positioning
   - Provide specific trade recommendations with entry levels, target P&L, stop-loss thresholds, and horizon
   - Note key risks: credit event clustering, sudden correlation spikes, liquidity withdrawal in off-the-run series

## Output

- **Correlation Surface Summary**: Table of base correlations by tranche detachment with historical percentile ranks
- **Skew Analysis**: Chart-ready data showing current vs. historical skew with commentary on regime
- **Index Basis Report**: Intrinsic vs. market spread, basis time series, and drivers
- **Dispersion Trade P&L Profile**: Scenario table with carry, spread, default, and correlation P&L columns
- **Risk Dashboard**: CS01, CR01, JTD, and gamma by tranche or position
- **Trade Recommendation**: Directional view with rationale, sizing, and risk limits

## Quality Checks

- Base correlation curve must be monotonically increasing from equity to super-senior — if not, investigate quote staleness or interpolation error
- Sum of tranche expected losses must equal the index expected loss (no-arbitrage constraint)
- CR01 signs must be internally consistent: long equity tranche = long correlation; long senior tranche = short correlation
- Verify recovery rate assumptions match market convention (typically 40% for IG, 25-30% for HY) [VERIFY: confirm current market standard]
- Confirm index series and roll date — mixing on-the-run and off-the-run quotes invalidates basis calculations
- Stress scenarios should include at least one idiosyncratic (single-name blowup) and one systemic (market-wide spread widening) event
- All implied correlations should fall within [0, 1]; values near boundaries indicate model breakdown or extreme market conditions requiring manual review
