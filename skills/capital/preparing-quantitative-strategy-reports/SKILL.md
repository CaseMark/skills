---
name: preparing-quantitative-strategy-reports
description: Structures systematic strategy performance reporting with factor exposure, attribution, and risk analytics for investor communication. Use when preparing quant reports, documenting strategy performance, or presenting systematic strategy results.
tags:
  - preparation
  - quantitative-capital-strategies
  - risk
metadata:
  author: casemark
  practice_areas:
    - Quantitative Investing
    - Systematic Strategies
    - Factor Investing
  document_types:
    - Preparation Document
  skill_modes:
    - Preparation
---
# Preparing Quantitative Strategy Reports

Structures systematic strategy performance reporting with factor exposure, attribution, and risk analytics for investor communication.

## When To Use

- Preparing monthly, quarterly, or annual performance reports for a systematic or factor-based strategy
- Communicating strategy results to LPs, allocators, or investment committees
- Documenting factor exposure changes, attribution breakdowns, or risk regime shifts
- Building tear sheets or strategy updates for due diligence or marketing materials
- Responding to investor requests for detailed quantitative performance analytics

## Inputs To Gather

- **Return series**: Daily or monthly strategy NAV/returns, gross and net of fees, with exact reporting period dates
- **Benchmark data**: Returns for the relevant benchmark(s) (e.g., S&P 500, MSCI World, Russell 2000) over the same period
- **Factor exposure snapshots**: Current and historical loadings on standard factors (market beta, size, value, momentum, quality, low volatility) from the risk model in use [VERIFY factor model provider—Barra, Axioma, internal]
- **Attribution output**: Return attribution by factor, sector, region, or signal grouping from the strategy's attribution engine
- **Risk metrics**: Realized volatility, Sharpe ratio, Sortino ratio, max drawdown, VaR/CVaR at stated confidence level, tracking error vs. benchmark
- **Portfolio characteristics**: Number of holdings, turnover rate, average holding period, concentration metrics (top 10 weight, HHI)
- **Capacity and AUM**: Current strategy AUM, estimated capacity, and any soft/hard close thresholds
- **Fee structure**: Management fee, performance fee, hurdle rate, high-water mark terms for net-of-fee calculations
- **Compliance constraints**: Any regulatory or internal limits on what can be disclosed (e.g., performance advertising rules under SEC Marketing Rule, GIPS compliance status) [VERIFY applicable regulatory regime]

## Workflow

1. **Confirm reporting scope**
   - Lock the reporting period (e.g., Q4 2025, trailing 12 months, since inception)
   - Identify the audience: LP quarterly letter, allocator due diligence deck, internal IC memo
   - Determine which return series to present (gross vs. net, multiple share classes, composite vs. fund-level)

2. **Compile and reconcile performance data**
   - Pull strategy returns from the portfolio management or accounting system
   - Reconcile against the administrator's NAV statements; flag any discrepancies > 1 bp
   - Calculate standard performance statistics: cumulative return, annualized return, annualized volatility, Sharpe, Sortino, max drawdown, drawdown duration, win/loss ratio (monthly)
   - Build performance comparison table against primary and secondary benchmarks

3. **Prepare factor exposure analysis**
   - Extract current factor loadings from the risk model; compare to prior period and inception averages
   - Present factor exposures in a table or time-series chart showing how tilts have evolved
   - Highlight any material shifts in exposure (e.g., beta drift, unintended sector concentration) and provide brief commentary on the cause (signal changes, market regime, rebalance timing)

4. **Build return attribution section**
   - Decompose returns into systematic factor contribution, alpha residual, and trading/implementation costs
   - If multi-signal strategy, attribute performance to individual signals or signal groups
   - Provide sector and/or geographic attribution if relevant to the strategy's investable universe
   - Clearly label the attribution methodology (Brinson-Fachler, factor-based, holdings-based) [VERIFY methodology matches what was disclosed in offering documents]

5. **Document risk analytics**
   - Report realized risk metrics alongside ex-ante risk model estimates; comment on any divergence
   - Include tail risk measures: VaR and CVaR at 95% and 99% confidence, worst N-day drawdown
   - Present correlation to major risk factors and asset classes (equity, rates, credit, commodities, USD)
   - Note any stress test or scenario analysis results if part of standard reporting (e.g., 2020 COVID shock replay, rates +200 bps)

6. **Add portfolio characteristics and operational details**
   - Summarize current portfolio composition: number of longs/shorts, gross/net exposure, sector weights
   - Report turnover, trade count, and implementation shortfall or slippage for the period
   - State current AUM, capacity utilization, and any changes to the strategy's investment process or model

7. **Draft narrative commentary**
   - Write a concise market environment overview (2–3 sentences) relevant to the strategy's factor exposures
   - Explain performance drivers and detractors in plain language tied to the quantitative attribution
   - Address any underperformance directly; avoid vague language—cite specific factors or market conditions
   - Note forward-looking positioning changes only if permissible under compliance guidelines [VERIFY whether forward-looking statements require specific disclaimers]

8. **Apply disclosures and formatting**
   - Include required legal disclaimers: past performance language, fee disclosure, risk warnings
   - If GIPS-compliant, include the GIPS compliance statement and composite disclosures [VERIFY GIPS verification status and composite definition]
   - Add footnotes for any non-standard calculations (e.g., annualization method for periods < 1 year, geometric vs. arithmetic linking)
   - Format tables for readability: consistent decimal places (2 for returns, 2 for ratios), date labels, source citations

## Output

The final report should include:

- **Performance summary table**: Period returns (MTD, QTD, YTD, 1Y, 3Y, 5Y, SI) gross and net, with benchmark comparisons
- **Factor exposure exhibit**: Current loadings vs. historical average, presented as a table or bar chart
- **Attribution breakdown**: Factor, sector, and/or signal attribution for the reporting period
- **Risk dashboard**: Volatility, Sharpe, drawdown, VaR/CVaR, correlation matrix
- **Portfolio snapshot**: Holdings count, exposure levels, turnover, AUM
- **Narrative commentary**: 1–2 pages explaining results in the context of market conditions
- **Disclosures**: Regulatory disclaimers, fee disclosures, GIPS statement if applicable

## Quality Checks

- Returns reconcile to administrator NAV within ±1 bp; any variance is footnoted
- All statistics use the same return series (no mixing gross and net within a single comparison)
- Factor exposures and attribution sum correctly (factor contributions + residual ≈ total return)
- Benchmark selection matches the strategy's stated benchmark in offering documents [VERIFY]
- Sharpe and Sortino ratios use the correct risk-free rate for the reporting period [VERIFY current risk-free rate assumption]
- Annualized figures for periods under one year are either avoided or clearly labeled as annualized with a footnote
- Drawdown calculations use peak-to-trough on a daily (not monthly) basis unless stated otherwise
- All forward-looking language has been reviewed by compliance
- Disclosures match the current regulatory requirements and the fund's most recent offering documents [VERIFY]
- Turnover and slippage figures are consistent with what the execution desk reports
