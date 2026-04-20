---
name: structuring-smart-beta-product-design
language: en
description: Designs systematic investment products with transparent methodology, rebalancing rules, and index construction specifications. Use when designing smart beta products, creating index methodologies, or structuring systematic funds.
tags:
  - quantitative-capital-strategies
  - investment
metadata:
  author: casemark
  practice_areas:
    - Quantitative Investing
    - Systematic Strategies
    - Factor Investing
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Smart Beta Product Design

Designs systematic investment products with transparent methodology, rebalancing rules, and index construction specifications.

## When To Use

- Designing a new smart beta ETF, index fund, or systematic strategy product
- Drafting an index methodology document for a calculation agent or index provider
- Defining factor exposures, weighting schemes, and reconstitution rules for a rules-based portfolio
- Evaluating whether an existing smart beta product's methodology is robust, investable, and differentiable
- Preparing product design materials for internal investment committee or external index advisory board review

## Inputs To Gather

- **Investment objective**: Target factor(s) (value, momentum, quality, low volatility, size, dividend yield, multi-factor blend), return/risk goals, and benchmark reference
- **Eligible universe**: Starting universe (e.g., Russell 1000, MSCI ACWI, S&P 500), market cap floors, liquidity minimums (median daily traded value), and country/sector constraints
- **Weighting scheme preference**: Market-cap weighted, equal-weighted, factor-score tilted, risk-parity, maximum diversification, or optimization-based (min variance, max Sharpe)
- **Rebalancing parameters**: Frequency (quarterly, semi-annual, annual), buffer/banding rules to control turnover, and rebalance effective dates
- **Capacity and tradability constraints**: Target AUM, maximum single-name weight, sector/country caps, ADV participation rate limits
- **Regulatory and wrapper context**: Product vehicle (ETF, mutual fund, separate account, index license), listing exchange, and relevant regulatory regime [VERIFY]
- **Backtesting data**: Historical factor returns, constituent-level price/fundamental data, and transaction cost assumptions

## Workflow

1. **Define the factor thesis and objective**
   - Specify target factor(s) with academic or empirical grounding (cite seminal papers where relevant: Fama-French, Asness, Novy-Marx, etc.)
   - Articulate the economic rationale — behavioral, structural, or risk-based explanation for the premium
   - State whether the product targets pure factor exposure, blended multi-factor, or factor timing

2. **Construct the eligible universe and screening rules**
   - Start from a recognized parent index or custom universe definition
   - Apply liquidity screens: minimum market cap, median daily volume, listing history (e.g., 12-month trading history)
   - Apply exclusionary screens if required (ESG, controversial weapons, sanctioned entities) [VERIFY regulatory/client-specific exclusions]

3. **Design the stock selection and scoring methodology**
   - Define factor signals with precise variable definitions (e.g., "book-to-price using most recent fiscal year-end book value divided by current market cap")
   - Specify composite scoring for multi-factor: z-score normalization, rank-based scoring, or percentile blending
   - Set selection thresholds: top quintile, top tercile, or continuous tilt with no hard cutoff
   - Address sector neutrality vs. sector-agnostic selection — document the trade-off between factor purity and sector concentration

4. **Specify the weighting scheme**
   - For factor-tilt weighting: define tilt function (linear, exponential, capped)
   - For optimization-based: state objective function, constraints (max weight, turnover budget, tracking error band), and covariance estimator
   - For equal-weight or fundamental-weight: document rationale and rebalancing drift tolerance
   - Apply hard caps: single-name max (typically 5%), sector max (typically benchmark +/- 5-10%), country limits

5. **Set rebalancing and reconstitution rules**
   - Reconstitution: full re-screening and re-ranking of the universe (typically semi-annual or annual)
   - Rebalancing: resetting weights to target (typically quarterly)
   - Buffer rules: existing constituents retained if within X% of selection threshold to reduce unnecessary turnover
   - Corporate actions handling: mergers, delistings, spin-offs, IPO eligibility waiting periods
   - Estimate turnover: one-way annual turnover target (smart beta typically 20-60%)

6. **Run backtest and stress analysis**
   - Simulate historical performance net of estimated transaction costs (commission + spread + market impact)
   - Report: annualized return, volatility, Sharpe ratio, max drawdown, and factor exposure (regression betas to standard factors)
   - Compare against cap-weighted benchmark and simple equal-weight alternative
   - Stress test across regimes: factor drawdown periods (e.g., value underperformance 2018-2020), liquidity crises, rising rate environments
   - Flag any period of data mining concern — out-of-sample validation or sub-period consistency checks

7. **Draft the index methodology document**
   - Produce a formal methodology covering: objective, universe, selection, weighting, rebalancing, corporate actions, calculation methodology (price return vs. total return vs. net total return), and governance
   - Include a numerical worked example showing how a hypothetical stock moves through screening, scoring, and weighting
   - Specify the index calculation agent and dissemination frequency if applicable

## Output

Deliver a **Smart Beta Product Design Report** containing:

- **Executive summary**: Factor thesis, target exposure, expected characteristics (tracking error to benchmark, turnover, number of holdings)
- **Methodology specification**: Complete, replicable rules covering universe, selection, weighting, and rebalancing — written so a third-party calculation agent could independently reconstruct the index
- **Backtest results**: Performance table, risk statistics, factor attribution, turnover analysis, and capacity estimate
- **Implementation considerations**: Preferred vehicle, estimated expense ratio range, licensing requirements, and competitive positioning vs. existing products
- **Appendix**: Detailed variable definitions, data sources, and corporate action handling rules

## Quality Checks

- **Replicability**: Could an independent party reconstruct the index from the methodology document alone, with no oral clarification? Every rule must be unambiguous
- **Investability**: Verify that capacity constraints are realistic — check that median constituent ADV supports target AUM at reasonable participation rates (typically <10% of ADV)
- **Turnover discipline**: Confirm buffer/banding rules are in place; one-way turnover should be justified relative to expected factor alpha net of costs
- **Factor purity**: Run regression of backtest returns against standard factor models (Fama-French 5-factor + momentum) — confirm intended factor loadings are significant and unintended exposures are controlled
- **Robustness**: Check that results are not driven by a narrow time period, a few outlier stocks, or look-ahead bias in signal construction
- **Regulatory alignment**: Confirm the methodology meets requirements for the chosen wrapper — diversification rules (e.g., RIC diversification tests for US ETFs/mutual funds [VERIFY]), index eligibility for UCITS if EU-listed [VERIFY], and any exchange-specific listing standards
- **No [VERIFY] items left unresolved** before final delivery to investment committee or index advisory board
