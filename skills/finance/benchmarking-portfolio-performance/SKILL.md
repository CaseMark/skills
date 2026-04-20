---
name: benchmarking-portfolio-performance
language: en
description: Conducts portfolio performance measurement with benchmark comparison, attribution, and risk-adjusted metrics. Use when measuring portfolio performance, calculating Sharpe/Sortino ratios, or conducting performance attribution.
tags:
  - asset-management
  - risk
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Portfolio Management
    - Asset Management
    - Wealth Management
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Benchmarking Portfolio Performance

## When To Use

- Evaluating portfolio returns against a stated benchmark over a defined period
- Preparing quarterly or annual performance reports for clients, investment committees, or fund boards
- Diagnosing sources of outperformance or underperformance through return attribution
- Comparing risk-adjusted returns across managers, strategies, or asset classes
- Responding to consultant or RFP performance data requests

## Inputs To Gather

- **Portfolio holdings and weights** — position-level data with market values at period start/end and at each rebalance date
- **Return series** — time-weighted or money-weighted returns at the frequency required (daily, monthly, quarterly)
- **Benchmark selection** — confirm the primary benchmark index (e.g., S&P 500, Bloomberg Aggregate, MSCI ACWI) and any secondary or blended benchmarks; document the rationale for benchmark choice
- **Risk-free rate** — specify the proxy used (e.g., 3-month T-bill, SOFR) and the matching period [VERIFY: confirm rate source and vintage]
- **Cash flow data** — contributions, withdrawals, and their timing (required for money-weighted / IRR calculations)
- **Evaluation period and frequency** — trailing periods (1Y, 3Y, 5Y, inception) and sub-periods for attribution windows
- **Fee schedule** — gross vs. net return basis; confirm whether management fees, performance fees, and transaction costs are included or excluded

## Workflow

1. **Validate data integrity**
   - Reconcile portfolio market values to custodian or accounting records
   - Confirm benchmark return series source (index provider, data vendor) and check for stale or restated data
   - Verify that return calculation methodology (time-weighted vs. money-weighted) matches the reporting standard (GIPS, client IMA) [VERIFY: applicable reporting standard]

2. **Calculate core return metrics**
   - Compute cumulative and annualized returns for each evaluation period
   - Calculate excess return (portfolio return minus benchmark return) on both arithmetic and geometric bases
   - If cash flows are material, compute money-weighted return (IRR) alongside time-weighted return and note the divergence

3. **Compute risk-adjusted metrics**
   - **Sharpe Ratio** — (Rp − Rf) / σp; use matching return and risk-free rate frequency, then annualize
   - **Sortino Ratio** — (Rp − Rf) / downside deviation; define the minimum acceptable return (MAR) threshold used
   - **Information Ratio** — excess return / tracking error; interpret in context of the strategy's active risk budget
   - **Treynor Ratio** — (Rp − Rf) / βp; note the benchmark used for beta estimation
   - **Maximum Drawdown** — peak-to-trough decline and recovery period
   - **Calmar Ratio** — annualized return / maximum drawdown (useful for alternative strategies)

4. **Perform return attribution**
   - **Brinson-Fachler decomposition** — allocation effect, selection effect, and interaction effect at the sector/asset-class level
   - For fixed income, use duration-based or key-rate attribution as appropriate
   - For multi-asset or multi-manager portfolios, decompose at the sleeve/manager level before drilling into sectors
   - Cumulative attribution should be linked across sub-periods using a geometric or logarithmic linking method (avoid simple arithmetic summation over multi-period windows)

5. **Contextualize and compare**
   - Rank portfolio metrics against peer universe (e.g., eVestment, Morningstar category) where data is available
   - Assess whether tracking error, beta, and active share are consistent with the stated investment mandate
   - Highlight any style drift, benchmark mismatch, or concentration risk revealed by the attribution

6. **Compile the performance report**
   - Structure output with an executive summary, return table, risk statistics table, attribution charts, and commentary
   - State all assumptions: return calculation method, fee basis, benchmark selection rationale, risk-free rate source
   - Flag any data gaps, estimation methods, or periods with non-standard treatment

## Output

The deliverable is a **Portfolio Performance Report** containing:

- **Executive Summary** — headline return, excess return, and one-line attribution takeaway
- **Return Table** — portfolio vs. benchmark returns across trailing periods, gross and net
- **Risk Statistics Table** — Sharpe, Sortino, Information Ratio, Treynor, max drawdown, tracking error, beta, alpha
- **Attribution Analysis** — sector/factor-level allocation and selection effects with linked multi-period results
- **Peer Comparison** — percentile rankings where universe data is available
- **Commentary** — narrative explaining key drivers, any anomalies, and forward-looking positioning context
- **Appendix** — data sources, methodology notes, and definitions of all metrics used

## Quality Checks

- Confirm that portfolio and benchmark return series cover identical date ranges with no missing periods
- Verify arithmetic: cumulative return from sub-period returns should reconcile to the reported total return within rounding tolerance
- Ensure Sharpe/Sortino ratios use consistent annualization (do not annualize the ratio from monthly figures by multiplying by √12 if the inputs are already annualized)
- Check that attribution effects sum to total excess return for each period; investigate residuals exceeding ±5 bps
- Validate that gross-to-net return spread is consistent with the disclosed fee schedule
- Confirm benchmark is appropriate for the mandate — a small-cap value portfolio benchmarked to the S&P 500 should be flagged [VERIFY: benchmark suitability per IMA/IPS]
- Review for GIPS compliance if the firm claims GIPS adherence [VERIFY: GIPS composite requirements]
