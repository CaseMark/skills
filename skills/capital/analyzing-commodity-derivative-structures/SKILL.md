---
name: analyzing-commodity-derivative-structures
language: en
description: Evaluates commodity swaps, options, and exotic structures with seasonality, convenience yield, and storage cost analysis. Use when pricing commodity derivatives, analyzing energy structures, or evaluating commodity hedging.
tags:
  - analysis
  - derivatives-and-structured-products
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Commodity Derivative Structures

Evaluates commodity swaps, options, and exotic structures with seasonality, convenience yield, and storage cost analysis.

## When To Use

- Pricing or re-pricing commodity swaps (fixed-for-floating, basis swaps, calendar spreads)
- Valuing commodity options — vanillas, Asian (average-price), spread options, barrier/knock-in/knock-out structures
- Analyzing energy or agricultural hedging programs for mark-to-market, hedge effectiveness, or P&L attribution
- Evaluating exotic structures such as crack spread options, heat-rate options, swing/take-or-pay contracts, or accumulator/decumulator notes
- Reviewing term sheets or trade confirmations for commodity-linked structured products
- Assessing convenience yield, contango/backwardation dynamics, and storage cost implications on forward curves

## Inputs To Gather

- **Underlying commodity and market**: crude oil (WTI/Brent), natural gas (Henry Hub/TTF), power (PJM/ERCOT), metals (LME), agricultural (CBOT), etc.
- **Forward/futures curve**: full-term structure with settlement dates; source and as-of date
- **Contract specifications**: notional quantity, unit (bbl, MMBtu, MWh, mt), tenor, settlement type (physical vs. financial), pricing index
- **Structure details**: strike(s), barrier levels, averaging period, exercise style (European/American/Bermudan), optionality (caps, floors, collars, swaptions)
- **Volatility surface**: at-the-money vols, skew/smile data, seasonality adjustments; source and vintage
- **Interest rate curve**: relevant discount curve for NPV calculations
- **Storage and carry costs**: warehousing, insurance, financing, shrinkage/spoilage rates [VERIFY — varies by commodity and delivery point]
- **Historical spot/basis data**: for backtesting, seasonality calibration, and convenience yield estimation
- **Hedge accounting context** (if applicable): designation method (fair value vs. cash flow), effectiveness testing standard (ASC 815 / IFRS 9) [VERIFY]

## Workflow

1. **Map the structure** — Decompose the trade into component legs: swaps, options, and any embedded optionality. Identify payoff formulas and confirm whether settlement is physical or cash.

2. **Build/validate the forward curve** — Verify the futures term structure. Check for seasonal patterns (e.g., winter/summer spreads in natural gas, harvest cycles in grains). Note whether the curve is in contango or backwardation and the implied roll yield.

3. **Estimate convenience yield and cost of carry** — Calculate implied convenience yield from the forward curve using:
   - `F(t,T) = S(t) × e^{(r + u − y)(T−t)}`
   - where `r` = risk-free rate, `u` = storage cost rate, `y` = convenience yield
   - Flag any negative convenience yields or anomalous carry spreads for review.

4. **Calibrate volatility** — Select the appropriate volatility surface. For energy structures, apply seasonal volatility adjustments (e.g., winter gas vol premiums). For Asian options, compute the effective variance reduction from the averaging mechanism. For spread options, estimate correlation between the two underlyings.

5. **Price component instruments**:
   - **Swaps**: discount each fixed-vs-floating cashflow leg using the forward curve and discount curve; report NPV for each leg and the net.
   - **Vanilla options**: use Black-76 (futures-settled) or Garman-Kohlhagen (FX-commodity hybrids) as appropriate.
   - **Asian options**: apply Turnbull-Wakeman or geometric approximation; specify averaging type (arithmetic vs. geometric) and frequency.
   - **Barrier/exotic options**: use Monte Carlo simulation or finite-difference PDE methods; document number of paths, time steps, and convergence checks.
   - **Spread options**: apply Kirk's approximation or two-factor Monte Carlo with calibrated correlation.

6. **Compute Greeks and sensitivities** — Report delta (per unit underlying), gamma, vega (per 1 vol point), theta (per day), and rho. For spread structures, include cross-gamma and correlation sensitivity. For calendar structures, break out Greeks by delivery month.

7. **Run scenario and stress analysis** — Test P&L impact under:
   - Parallel curve shifts (±10%, ±25%)
   - Curve shape changes (steepening, flattening, seasonal spike)
   - Volatility shocks (±5 vol points)
   - Correlation breakdown scenarios (for spread/basket structures)
   - Storage cost or convenience yield shifts

8. **Assess hedge effectiveness** (if applicable) — Calculate prospective and retrospective effectiveness using dollar-offset or regression methods per the applicable accounting standard. Flag if the hedge ratio falls outside the 80–125% corridor or fails the "highly effective" threshold. [VERIFY — effectiveness thresholds depend on ASC 815 vs. IFRS 9 designation]

9. **Compile findings** — Summarize pricing, risk metrics, scenario results, and any structural concerns (e.g., gap risk at barriers, liquidity risk in off-peak months, basis risk between hedge instrument and underlying exposure).

## Output

- **Structure Summary**: trade description, component decomposition, key contract terms
- **Pricing Table**: NPV by leg, total structure value, mid-market price vs. indicative dealer quote (if available)
- **Greeks Dashboard**: delta, gamma, vega, theta, rho — broken out by delivery period for calendar structures
- **Forward Curve & Carry Analysis**: chart or table showing forward curve shape, implied convenience yield, and storage cost assumptions
- **Scenario Matrix**: P&L under defined stress scenarios, with identification of the most adverse case
- **Hedge Effectiveness Summary** (if applicable): effectiveness ratio, cumulative ineffectiveness, any risks to designation
- **Risk Flags**: liquidity concerns, model risk notes (e.g., smile extrapolation, correlation instability), and basis risk warnings

## Quality Checks

- Verify forward curve data is current (within 1 business day for liquid markets) and sourced from a recognized provider (ICE, CME, Platts, Argus)
- Confirm volatility surface vintage matches the curve date; flag stale vol inputs
- For Monte Carlo valuations, verify convergence: standard error of price estimate should be < 1% of the value
- Cross-check swap NPVs against Bloomberg SWPM or equivalent where possible
- Ensure convenience yield estimates are consistent with observable storage rates and are not negative without explanation
- Validate that Greeks sum correctly across component legs to the total structure level
- For hedge accounting analysis, confirm the designated hedge ratio matches the actual hedging relationship and that critical terms are documented [VERIFY]
- Mark all jurisdiction- or regulation-dependent conclusions with [VERIFY]
