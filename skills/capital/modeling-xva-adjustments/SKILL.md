---
name: modeling-xva-adjustments
language: en
description: Calculates comprehensive XVA including CVA, DVA, FVA, KVA, and MVA with portfolio-level analysis and hedging strategies. Use when computing XVA, modeling valuation adjustments, or analyzing funding costs.
tags:
  - modeling
  - derivatives-and-structured-products
  - portfolio
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling XVA Adjustments

## When To Use

- Computing credit valuation adjustment (CVA) or debit valuation adjustment (DVA) for OTC derivative portfolios
- Quantifying funding valuation adjustment (FVA) to reflect treasury funding costs/benefits on uncollateralized or partially collateralized positions
- Estimating capital valuation adjustment (KVA) to allocate regulatory capital costs (SA-CCR, IMM, FRTB) back to individual trades
- Calculating margin valuation adjustment (MVA) for initial margin costs under UMR or CCP requirements
- Performing portfolio-level XVA aggregation with netting set and CSA-aware exposure profiles
- Designing XVA hedging strategies or evaluating incremental XVA on new trades

## Inputs To Gather

- **Trade population**: Trade-level details (notional, maturity, currency, product type) for each netting set
- **CSA / margin terms**: Threshold, minimum transfer amount, independent amount, eligible collateral, rehypothecation rights, variation margin frequency, initial margin model (ISDA SIMM vs. schedule) [VERIFY against actual CSA documents]
- **Counterparty credit data**: CDS spreads or mapped credit curves, recovery rate assumptions, rating/sector if using proxy curves
- **Own-credit data**: Entity CDS spread or internal funding curve for DVA and FVA
- **Market data**: Yield curves, FX rates, volatility surfaces, correlation assumptions for exposure simulation
- **Funding curve**: Internal cost-of-funds curve distinguishing secured vs. unsecured rates; FVA spread = unsecured funding rate − OIS
- **Regulatory parameters**: SA-CCR alpha factor, supervisory risk weights, cost-of-capital rate (typically 8–12%), capital horizon [VERIFY against current Basel III/IV regime applicable to entity]
- **Simulation parameters**: Number of Monte Carlo paths, time grid granularity, diffusion model choice (GBM, local vol, stochastic vol)

## Workflow

1. **Scope & segmentation** — Identify netting sets, confirm CSA terms per netting set, classify trades as collateralized/uncollateralized/partially collateralized. Determine which XVA components are in scope (CVA, DVA, FVA, KVA, MVA).

2. **Exposure simulation** — Run Monte Carlo simulation to generate future portfolio values on a time grid. Compute expected positive exposure (EPE) and expected negative exposure (ENE) profiles per netting set, applying CSA margining logic (threshold, MTA, margin period of risk).

3. **CVA calculation** — Integrate discounted EPE against counterparty default probability:
   - CVA ≈ Σ_t [ DF(t) × EPE(t) × (1 − R_cpty) × ΔPD_cpty(t) ]
   - Use counterparty CDS-implied hazard rates or mapped proxy curves
   - Apply wrong-way risk adjustments where exposure is correlated with counterparty credit quality

4. **DVA calculation** — Mirror CVA using ENE and own default probability:
   - DVA ≈ Σ_t [ DF(t) × ENE(t) × (1 − R_own) × ΔPD_own(t) ]
   - Note DVA accounting treatment varies: IFRS 13 requires DVA in P&L; some desks exclude from pricing [VERIFY entity's DVA policy]

5. **FVA calculation** — Compute funding cost/benefit on expected unsecured exposure:
   - FVA ≈ Σ_t [ EPE(t) × s_fund(t) × Δt ] − Σ_t [ ENE(t) × s_fund(t) × Δt ]
   - Where s_fund is the entity's funding spread over OIS
   - Distinguish FCA (funding cost) from FBA (funding benefit) if reported separately

6. **KVA calculation** — Estimate lifetime cost of regulatory capital:
   - Compute future capital profiles using SA-CCR EAD at each simulation date
   - KVA ≈ Σ_t [ DF(t) × h_capital × RegulatoryCapital(t) × Δt ]
   - h_capital = hurdle rate (cost of equity minus risk-free rate, typically 6–10%)
   - [VERIFY applicable capital framework: SA-CCR vs. IMM; Basel III vs. IV timeline]

7. **MVA calculation** — Quantify cost of funding initial margin over trade life:
   - Project future IM using ISDA SIMM or CCP schedule on simulated portfolios
   - MVA ≈ Σ_t [ DF(t) × E[IM(t)] × s_fund(t) × Δt ]
   - For bilateral trades under UMR, confirm phase-in applicability [VERIFY UMR phase and AANA threshold]

8. **Aggregation & allocation** — Sum components to total XVA per netting set and portfolio-wide. Allocate incremental XVA to individual trades using Euler allocation or stand-alone/incremental decomposition for pricing and desk-level P&L attribution.

9. **Hedging strategy** — Identify primary XVA risk drivers:
   - CVA hedge: Single-name CDS or index CDS (iTraxx/CDX) for spread risk; interest rate swaps for exposure profile
   - FVA hedge: Secured funding or collateral transformation trades
   - Assess hedge effectiveness, basis risk, and cost-of-hedge vs. XVA reduction

10. **Sensitivity & stress testing** — Run bumps on key inputs (credit spreads ±10bp, funding spreads ±5bp, rates ±25bp, correlation shifts) and report XVA Greeks (CS01, IR01, FVA01). Stress-test under adverse scenarios (counterparty downgrade, funding stress, margin call spikes).

## Output

- **XVA summary table**: CVA, DVA, FVA (FCA/FBA split), KVA, MVA per netting set and total portfolio, with base-case values and percentage of notional
- **Exposure profiles**: EPE and ENE time series charts per netting set, with and without collateral
- **Capital profile**: Projected regulatory capital over time under SA-CCR / IMM
- **IM projection**: Expected initial margin trajectory for MVA computation
- **Sensitivity report**: XVA Greeks (CS01, IR01, FVA01, CorrelSens) in tabular format
- **Stress results**: XVA under 3–5 stress scenarios with narrative on key drivers
- **Hedging recommendation**: Instruments, notional sizing, expected hedge ratio, residual risk, and estimated hedge cost
- **Methodology documentation**: Simulation assumptions, model choices, recovery rates, proxy mapping logic, and any overrides

## Quality Checks

- Confirm EPE/ENE profiles converge with sufficient Monte Carlo paths (check standard error < 1% of mean)
- Validate CVA against analytic approximation (e.g., semi-analytic formula for vanilla swaps) as a sanity check
- Ensure FVA sign convention is consistent: positive FVA = cost to the entity for net lending positions
- Verify netting set boundaries match legal documentation (ISDA Master Agreement scope)
- Cross-check CDS-implied default probabilities against rating-implied benchmarks for reasonableness
- Confirm KVA capital calculation matches independently computed SA-CCR EAD for spot date
- Validate that collateral modeling correctly reflects CSA terms (threshold, MTA, rounding, eligible currencies)
- Review incremental XVA for a new trade: should be bounded between stand-alone XVA (upper) and marginal XVA (lower)
- Flag any counterparty without liquid CDS data — proxy mapping methodology must be documented and reviewed
