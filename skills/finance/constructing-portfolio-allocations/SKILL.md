---
name: constructing-portfolio-allocations
language: en
description: Builds strategic and tactical asset allocation models with risk-return optimization and constraint management. Use when constructing portfolios, optimizing asset allocation, or building model portfolios.
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
# Constructing Portfolio Allocations

## When To Use

- Building a strategic asset allocation (SAA) for a new portfolio or investment policy statement (IPS)
- Constructing a tactical asset allocation (TAA) overlay to tilt exposures relative to a policy benchmark
- Optimizing an existing portfolio's risk-return profile under updated capital market assumptions
- Creating model portfolios for client risk-profile tiers (e.g., conservative, moderate, aggressive)
- Evaluating allocation trade-offs when adding alternative asset classes or illiquid holdings

## Inputs To Gather

- **Investment objective and time horizon** — total return target, income requirement, liability-matching need, or spending-rate constraint
- **Risk parameters** — maximum drawdown tolerance, volatility budget, tracking-error limit versus benchmark, and any VaR/CVaR constraints
- **Eligible asset classes** — equities (domestic/international/EM), fixed income (duration/credit tiers), real assets, alternatives (PE, hedge funds, real estate, infrastructure), cash equivalents
- **Capital market assumptions (CMAs)** — expected returns, standard deviations, and correlation matrix for each asset class; source and vintage of CMAs [VERIFY: confirm CMA provider and date]
- **Constraints** — regulatory limits (e.g., ERISA prudent-investor, insurance statutory caps), liquidity minimums, ESG/SRI exclusions, concentration caps per asset class or issuer, currency-hedging policy
- **Current portfolio** (if rebalancing) — existing holdings, unrealized gain/loss positions, and transaction-cost estimates
- **Benchmark** — policy benchmark or composite index for performance attribution

## Workflow

1. **Set the allocation framework**
   - Choose methodology: mean-variance optimization (MVO), Black-Litterman, risk-parity, minimum-variance, or liability-driven investing (LDI)
   - For MVO: build the efficient frontier from CMAs; identify the tangency portfolio and the minimum-variance portfolio
   - For Black-Litterman: establish equilibrium returns from market-cap weights, then incorporate the manager's active views with confidence levels
   - For risk-parity: equalize risk contribution across asset classes using marginal risk decomposition

2. **Apply constraints**
   - Encode upper/lower bounds per asset class (e.g., alternatives ≤ 20%, domestic equity 30–60%)
   - Layer in liquidity requirement: ensure sufficient allocation to daily-liquid instruments to meet redemption or spending needs
   - Integrate ESG screens or exclusion lists if mandated by IPS
   - Apply regulatory floors/caps [VERIFY: jurisdiction-specific statutory allocation limits for insurance, pension, or sovereign wealth mandates]

3. **Run optimization and scenario analysis**
   - Generate optimal allocation at target return or target risk level
   - Run sensitivity analysis: stress-test output against ±1–2σ shifts in key CMAs (equity risk premium, credit spreads, inflation)
   - Compare efficient frontier portfolios at multiple risk points to give decision-makers a menu
   - Evaluate corner solutions — if optimizer pushes any asset class to a bound, document why and whether the constraint should be revisited

4. **Construct model portfolio tiers (if applicable)**
   - Map allocations to 3–5 risk-profile tiers aligned with client suitability questionnaires
   - Ensure each tier shows monotonically increasing equity/growth exposure and expected volatility
   - Assign implementation vehicles (index funds, ETFs, active managers, direct holdings) per sleeve

5. **Document rebalancing and governance rules**
   - Define rebalancing triggers: calendar-based (quarterly/annual) vs. threshold-based (±5% drift bands)
   - Specify TAA authority: allowable active tilts, maximum deviation from SAA, and approval process
   - Note tax-aware rebalancing considerations for taxable accounts (harvest losses, avoid short-term gains)

## Output

- **Allocation summary table** — target weights per asset class with permissible ranges
- **Efficient frontier chart** — plotted portfolios with the selected allocation highlighted
- **Risk decomposition** — contribution to total portfolio risk by asset class (marginal and percentage)
- **Scenario/stress-test results** — portfolio return and drawdown under bull, base, and bear CMAs
- **Model portfolio tiers** (if multi-tier) — side-by-side allocation grids with expected return, volatility, Sharpe ratio, and max drawdown estimate per tier
- **Methodology narrative** — rationale for framework choice, key assumptions, and known limitations
- **Rebalancing policy summary** — triggers, bands, and governance authority

## Quality Checks

- Weights sum to 100% across all asset classes in every tier
- No allocation breaches stated upper/lower bounds or regulatory caps
- Expected portfolio return and risk metrics are arithmetically consistent with CMAs and weights
- Correlation and volatility inputs match the stated CMA source and vintage — flag stale data (>12 months old) with [VERIFY]
- Liquidity profile supports stated spending/redemption needs without forced selling of illiquid sleeves
- Sharpe ratio and risk-contribution metrics are reasonable relative to historical ranges for similar portfolios
- Tax-lot and transaction-cost implications are noted for rebalancing recommendations in taxable accounts
- All assumptions and data sources are explicitly cited; no inferred figures presented as confirmed
