---
name: modeling-counterparty-credit-exposure
description: Calculates potential future exposure and CVA with simulation-based approaches and netting agreement analysis. Use when modeling counterparty exposure, calculating CVA/DVA, or assessing counterparty risk.
tags:
  - modeling
  - derivatives-and-structured-products
  - risk
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
# Modeling Counterparty Credit Exposure

## When To Use

- Calculating potential future exposure (PFE) profiles for OTC derivative portfolios
- Computing credit valuation adjustment (CVA) and debit valuation adjustment (DVA) for pricing or accounting (ASC 820 / IFRS 13)
- Assessing counterparty credit limits and concentration risk across netting sets
- Evaluating the impact of collateral agreements (CSAs) on exposure profiles
- Stress-testing counterparty exposure under adverse market scenarios
- Supporting regulatory capital calculations under SA-CCR or IMM [VERIFY: applicable regulatory framework]

## Inputs To Gather

- **Trade population**: Full list of trades per counterparty, including notional, trade date, maturity, currency, and product type (IRS, CDS, FX forwards, equity options, etc.)
- **Netting agreements**: ISDA Master Agreement status, netting set definitions, and any close-out netting enforceability opinions [VERIFY: jurisdiction-specific enforceability]
- **Collateral terms**: CSA parameters — threshold, minimum transfer amount (MTA), independent amount, eligible collateral types, rehypothecation rights, margin period of risk (MPR)
- **Market data**: Yield curves, volatility surfaces, FX spot rates, credit spreads (CDS or bond-implied), correlation assumptions
- **Counterparty credit data**: Credit ratings, CDS spreads (or proxy spreads), probability of default (PD) term structures, loss given default (LGD) assumptions
- **Own credit data**: Entity CDS spreads or proxy for DVA calculation
- **Simulation parameters**: Number of Monte Carlo paths, time grid granularity, confidence level for PFE (typically 95th or 97.5th percentile), simulation horizon

## Workflow

1. **Map netting sets and collateral**
   - Group trades by legal netting agreement; confirm enforceability per jurisdiction
   - Parse CSA terms: thresholds, MTAs, MPR, eligible collateral haircuts
   - Identify wrong-way risk exposures (counterparty credit quality correlated with exposure)

2. **Calibrate market models**
   - Select diffusion processes per risk factor (e.g., Hull-White for rates, GBM or local vol for equities/FX, reduced-form for credit)
   - Calibrate to current market data; document calibration targets and fit quality
   - Set correlation matrix across risk factors — use historical estimation with appropriate lookback window

3. **Run Monte Carlo simulation**
   - Simulate joint evolution of all risk factors across the time grid
   - Reprice each trade at each time step on each path (use analytic approximations or regression-based methods like Longstaff-Schwartz for early-exercise products)
   - Aggregate to netting-set level, apply close-out netting: net exposure = max(0, sum of MTMs within netting set)

4. **Apply collateral dynamics**
   - Model collateral calls with MPR lag (typically 10–20 business days for bilateral, 5 for cleared)
   - Apply thresholds, MTAs, and independent amounts per CSA
   - Compute collateralized exposure at each time step: E(t) = max(0, net MTM − collateral held)

5. **Calculate exposure metrics**
   - **Expected Exposure (EE)**: Mean of positive exposures across paths at each time step
   - **Potential Future Exposure (PFE)**: Quantile of exposure distribution (95th/97.5th percentile) at each time step
   - **Expected Positive Exposure (EPE)**: Time-weighted average of EE over the profile
   - **Peak PFE**: Maximum PFE across the time grid
   - **Effective EPE**: Non-decreasing transformation of EPE for regulatory purposes

6. **Compute CVA and DVA**
   - CVA = integral of discounted EE × counterparty default probability × LGD over the exposure horizon
   - DVA = integral of discounted ENE (expected negative exposure) × own default probability × LGD
   - Use counterparty CDS spreads for market-implied PD; use rating-based PD for accounting if required [VERIFY: CVA methodology — market-implied vs. historical PD per firm policy]
   - Consider bilateral CVA (BCVA = CVA − DVA) and FVA if required

7. **Stress test and validate**
   - Run exposure profiles under stressed market scenarios (rate shocks, spread widening, FX moves)
   - Test sensitivity to correlation assumptions, number of simulation paths, and time-grid density
   - Compare model PFE against add-on based methods (SA-CCR) as a reasonableness check
   - Back-test exposure predictions against realized MTMs where historical data is available

## Output

- **Exposure profile report**: Time-series charts of EE, PFE (with confidence level), and peak PFE per netting set and counterparty
- **CVA/DVA summary**: Unilateral CVA, DVA, and bilateral CVA per counterparty with breakdown by netting set
- **Collateral impact analysis**: Comparison of uncollateralized vs. collateralized exposure profiles showing CSA benefit
- **Sensitivity tables**: CVA sensitivity to credit spread moves (CS01), interest rate shifts, and correlation changes
- **Wrong-way risk flags**: Identification of netting sets where exposure and counterparty default are positively correlated
- **Methodology documentation**: Model choices, calibration details, simulation parameters, and all assumptions

## Quality Checks

- Verify that netting-set groupings match legal documentation — incorrect netting inflates or deflates exposure
- Confirm collateral parameters (thresholds, MTA, MPR) are sourced from actual CSA terms, not defaults
- Check that the number of Monte Carlo paths produces stable results (re-run with doubled paths; PFE should not shift materially)
- Validate that EE converges to zero as trades approach maturity
- Ensure PFE at the 95th percentile exceeds EE at every time step — if not, check for simulation errors
- Cross-check CVA magnitude against market benchmarks: CVA as basis points of notional should be plausible given counterparty spread level
- Confirm discount curves and credit curves are as-of the same valuation date
- Flag any trades with missing market data or valuation failures — do not silently drop them from the simulation
- Mark all jurisdiction-dependent assumptions (netting enforceability, MPR regulatory minimums, capital framework) with [VERIFY]
