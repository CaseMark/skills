---
name: modeling-securities-lending-dynamics
language: en
description: Analyzes securities lending market with borrow cost, short interest dynamics, and fail-to-deliver monitoring. Use when analyzing lending markets, tracking borrow costs, or evaluating short selling dynamics.
tags:
  - modeling
  - public-markets-and-trading
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Securities Lending Dynamics

## When To Use

- Estimating borrow cost trajectories for hard-to-borrow securities or crowded shorts
- Monitoring short interest buildup and days-to-cover ratios ahead of catalysts (earnings, lockup expiries, index rebalances)
- Tracking fail-to-deliver (FTD) patterns to flag potential locate/recall risk
- Evaluating lending revenue opportunity for beneficial owners or prime brokerage desks
- Stress-testing short portfolios for borrow-cost squeeze scenarios

## Inputs To Gather

- **Lending data**: Current borrow rates (GC vs. specials), utilization percentages, lendable supply, and on-loan quantities — sourced from agent lenders, DataLend/IHS Markit, or prime broker reports
- **Short interest**: Exchange-reported short interest, days-to-cover, and short-as-percentage-of-float; note reporting lag [VERIFY settlement cycle T+1/T+2 by jurisdiction]
- **FTD data**: SEC or equivalent regulator FTD files; aggregate by security and compute rolling FTD rates as percentage of volume
- **Market microstructure**: Average daily volume, float size, institutional ownership concentration, and ETF creation/redemption activity affecting locate supply
- **Event calendar**: Dividend record dates (manufacturing risk), proxy record dates, index reconstitution dates, lockup expiry schedules, and corporate action timelines
- **Fee benchmarks**: General collateral (GC) rate, fed funds / overnight rate for rebate calculations, and any negotiated rate floors in existing lending agreements

## Workflow

1. **Map the lending supply stack**
   - Aggregate lendable inventory across agent lenders, custody banks, and ETF providers
   - Compute utilization rate (on-loan ÷ lendable supply) and flag securities above 80% utilization as elevated-risk
   - Identify concentration: if top 3 lenders hold >50% of supply, mark recall risk as high

2. **Model borrow cost dynamics**
   - Classify each security: GC (<50 bps fee), warm (50–200 bps), or special/hard-to-borrow (>200 bps)
   - Build a rate curve using current indicative rate, 30-day trailing average, and peak rate over 90 days
   - For specials, model cost as a function of utilization rate, short interest velocity (Δ SI / Δt), and days to next catalyst
   - Apply dividend-adjusted cost: on ex-date, manufactured dividend payment shifts effective borrow cost — model gross vs. net rebate impact [VERIFY withholding tax treatment by domicile]

3. **Analyze short interest dynamics**
   - Compute days-to-cover = short interest ÷ trailing 20-day ADV
   - Track SI velocity: rising SI with stable supply → upward rate pressure; rising SI with expanding supply → rate may hold
   - Flag squeeze conditions: days-to-cover >7, utilization >90%, and rising borrow rate simultaneously
   - Cross-reference with options market: high put open interest or elevated skew may indicate synthetic short positioning not captured in SI data

4. **Monitor fail-to-deliver patterns**
   - Pull FTD data and compute rolling 10-day FTD rate as percentage of ADV
   - Sustained FTDs above 0.5% of float trigger Reg SHO threshold list inclusion [VERIFY close-out timelines per Reg SHO Rule 204 vs. local equivalent]
   - Correlate FTD spikes with borrow rate movements — persistent FTDs with flat rates may indicate operational fails rather than locate scarcity
   - Model forced buy-in probability based on FTD age and broker close-out policies

5. **Scenario and stress testing**
   - **Recall scenario**: Model P&L impact if 25% / 50% / 100% of position is recalled with forced buy-in at ask + spread premium
   - **Rate spike scenario**: Apply 2x and 5x current borrow rate to compute annualized carry cost drag on short alpha
   - **Squeeze scenario**: Simulate price path where 10–20% of SI covers over 3 days against constrained supply — compute slippage and total cost of exit
   - **Dividend event**: Calculate manufactured dividend liability and compare against rebate income for dividend-capture lending strategies

## Output

- **Borrow Cost Dashboard**: Security-level table with current rate, 30/90-day range, utilization, SI %, days-to-cover, and FTD rate
- **Risk Flags Summary**: List of securities crossing thresholds (utilization >80%, DTC >7, FTD >0.5% float, rate in top decile of 90-day range)
- **Cost Projection**: Forward 30/60/90-day borrow cost estimate per position with confidence bands based on historical volatility of lending rates
- **Scenario Matrix**: P&L impact table for recall, rate spike, and squeeze scenarios by position
- **Lending Revenue Estimate** (if beneficial owner context): Projected fee income by security with utilization-weighted expected duration on loan

## Quality Checks

- Verify utilization and SI data are from the same reporting date — stale mismatches distort DTC and rate projections
- Confirm borrow rates distinguish between indicative quotes and executable rates; flag any rate sourced from a single counterparty
- Ensure FTD calculations use the correct denominator (shares outstanding vs. float vs. ADV) and state which is used
- Cross-check that rebate calculations correctly net the benchmark rate against the lending fee [VERIFY GC rate benchmark: fed funds, SOFR, or ESTR depending on currency]
- Validate that squeeze stress tests use realistic volume participation rates (typically 10–25% of ADV for orderly cover, higher for forced buy-ins)
- Confirm manufactured dividend costs reflect actual tax treaty rates and not just statutory withholding [VERIFY]
