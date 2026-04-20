---
name: modeling-bond-valuations
language: en
description: Calculates bond pricing with duration, convexity, OAS, and Z-spread analysis. Use when pricing bonds, calculating risk metrics, or evaluating relative value.
tags:
  - modeling
  - fixed-income
  - risk
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Bond Valuations

## When To Use

- Pricing a bond (fixed-rate, floating-rate, zero-coupon, callable, putable, or amortizing) from first principles or relative to benchmarks
- Calculating duration (Macaulay, modified, effective) and convexity for portfolio risk management
- Computing OAS or Z-spread to evaluate credit-adjusted relative value versus comparable issues
- Running scenario/shock analysis on rate moves, curve shifts, or credit migration
- Comparing bonds across sectors or maturities on a spread basis for trade idea generation

## Inputs To Gather

- **Bond terms**: CUSIP/ISIN, coupon rate, coupon frequency, maturity date, day-count convention (30/360, ACT/ACT, ACT/360), par value, settlement date
- **Embedded options**: Call/put schedule with dates and strike prices; make-whole spread if applicable
- **Benchmark curve**: Treasury par/spot/forward curve or swap curve (source and as-of date)
- **Credit inputs**: Credit rating, sector, issuer spread history, comparable issue spreads
- **Market data**: Current market price or yield, accrued interest, repo rate (for carry analysis)
- **Volatility assumption**: Interest rate vol model or surface if pricing options (e.g., lognormal OAS model vol in bps)

## Workflow

1. **Build the cash flow schedule**
   - Map coupon dates using the stated frequency and day-count convention
   - For amortizing bonds, construct the principal repayment schedule
   - For floaters, project coupon resets from the forward curve plus quoted spread

2. **Bootstrap or source the discount curve**
   - Use Treasury spot rates (strip curve) or swap zero rates as the risk-free benchmark
   - Interpolate intermediate maturities via cubic spline or piecewise linear methods
   - Document curve source, snapshot date/time, and interpolation method

3. **Compute base valuation**
   - **Price from yield**: Discount each cash flow at the bond's YTM; sum present values; add accrued interest for dirty price
   - **Z-spread**: Solve iteratively for the constant spread over the spot curve that equates discounted cash flows to the observed market price
   - **OAS (for bonds with optionality)**: Use a binomial or Monte Carlo interest rate model; calibrate the tree/sim to the benchmark curve and vol surface; solve for the spread that prices the bond to market after accounting for embedded option exercise [VERIFY: confirm vol model and calibration parameters match firm convention]

4. **Calculate risk metrics**
   - **Modified duration**: −(1/P) × dP/dy, computed analytically or via a ±1 bp parallel shift
   - **Effective duration** (for callable/putable): Use the OAS model to reprice under ±25–50 bp parallel curve shifts; ED = (P₋ − P₊) / (2 × P₀ × Δy)
   - **Convexity**: (P₋ + P₊ − 2P₀) / (P₀ × Δy²), using the same shift size
   - **Key-rate durations**: Shift individual tenor points (2y, 5y, 10y, 30y) by ±25 bp, holding others constant; report sensitivity at each node
   - **DV01 / BPV**: Dollar change per $1 million face for a 1 bp yield change

5. **Run relative value and scenario analysis**
   - Compare OAS or Z-spread to sector medians, rating-tier comps, and issuer's own curve
   - Stress-test with parallel shifts (±50, ±100, ±200 bp), curve steepening/flattening (2s10s ±50 bp), and credit spread widening (+50, +100 bp)
   - Compute carry and roll-down over 1m/3m/6m horizons using forward rates
   - Flag rich/cheap signals: current spread vs. 6-month and 12-month historical range

6. **Validate outputs**
   - Cross-check computed price against Bloomberg/vendor price (tolerance ≤ 1/32 for Treasuries, ≤ ¼ point for corporates)
   - Verify duration and convexity fall within expected ranges for the bond's tenor and coupon
   - Confirm OAS is positive for investment-grade issues and directionally consistent with credit tier
   - Sense-check carry/roll-down against the shape of the forward curve

## Output

Deliver a structured valuation summary containing:

- **Bond identification**: Issuer, CUSIP/ISIN, coupon, maturity, call features
- **Pricing table**: Clean price, dirty price, accrued interest, YTM, YTW (yield-to-worst for callables)
- **Spread metrics**: Z-spread, OAS, G-spread, I-spread (where applicable)
- **Risk metrics**: Modified/effective duration, convexity, DV01, key-rate duration profile
- **Relative value**: Spread vs. comps table, historical spread percentile, rich/cheap assessment
- **Scenario matrix**: Price and spread impact under each stress scenario
- **Carry/roll-down**: Projected total return components over stated horizons
- **Assumptions log**: Curve source, vol model, day-count, settlement, interpolation method

## Quality Checks

- Confirm day-count convention matches the bond's market standard (e.g., 30/360 for US corporates, ACT/ACT for Treasuries) [VERIFY]
- Ensure settlement date reflects T+1 or T+2 convention per market [VERIFY]
- Validate that the yield-to-worst is computed across all call dates, not just the first
- Check that OAS model calibration reprices on-the-run benchmarks to within 0.5 bp
- Verify accrued interest calculation matches the ex-dividend convention for the market
- Confirm that key-rate duration contributions sum approximately to effective duration
- Flag any negative OAS on investment-grade bonds as a potential data or model error
- Mark all externally sourced vol assumptions and spread comps with retrieval dates
