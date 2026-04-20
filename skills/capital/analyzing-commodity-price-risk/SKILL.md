---
name: analyzing-commodity-price-risk
language: en
description: Evaluates commodity price exposure with forward curve analysis, hedging strategies, and break-even price sensitivity. Use when analyzing commodity risk, designing hedging programs, or stress testing price assumptions.
tags:
  - analysis
  - real-assets-and-natural-resources
  - risk
metadata:
  author: casemark
  practice_areas:
    - Natural Resources
    - Energy Capital
    - Commodity Investment
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Commodity Price Risk

Evaluates commodity price exposure with forward curve analysis, hedging strategies, and break-even price sensitivity.

## When To Use

- Assessing a portfolio's or project's exposure to commodity price movements (crude oil, natural gas, metals, agricultural products)
- Designing or reviewing a hedging program for a producer, refiner, or offtaker
- Stress testing price assumptions in investment underwriting or reserve-based lending
- Evaluating forward curve shape (contango vs. backwardation) and its impact on roll yield and storage economics
- Benchmarking realized vs. budgeted commodity prices for variance analysis

## Inputs To Gather

- **Commodity exposure profile**: volumes, commodity type(s), production/consumption schedule, contract tenors
- **Current and historical spot prices**: at minimum 3–5 years of price history for the relevant benchmark (e.g., WTI, Henry Hub, LME Copper)
- **Forward/futures curve data**: exchange-settled strip prices across relevant tenors
- **Existing hedge book**: instruments in place (swaps, collars, puts, three-way structures), notional volumes, strike prices, expiration dates
- **Break-even economics**: all-in sustaining cost, lifting cost, or full-cycle cost per unit of production [VERIFY against operator's cost model]
- **Counterparty and credit terms**: ISDA status, margin/collateral requirements, hedge line availability
- **Regulatory or covenant constraints**: any hedging ratio limits from lenders or board-approved risk policy [VERIFY applicable policy]

## Workflow

1. **Map the exposure**: Quantify gross unhedged volume by commodity, time period, and delivery point. Identify basis risk between the production/consumption location and the benchmark index.

2. **Analyze the forward curve**: Pull current futures strip and compare to trailing 3-year and 5-year averages. Note whether the curve is in contango or backwardation and assess implications for hedge timing and roll costs.

3. **Evaluate existing hedges**: Overlay the current hedge book on the exposure profile. Calculate the percentage hedged by quarter, the weighted-average hedge price, and the mark-to-market value of outstanding positions.

4. **Run price scenarios**:
   - **Base case**: strip pricing as of analysis date
   - **Downside**: price decline of 25–40% sustained over 12 months (calibrate to historical drawdowns)
   - **Upside**: price rally of 20–30% (to quantify opportunity cost of hedges)
   - **Stress case**: a tail event (e.g., 2008 or 2020 crude collapse) applied to the current portfolio
   - For each scenario, compute revenue impact, debt service coverage, and covenant compliance.

5. **Assess break-even sensitivity**: Determine the commodity price at which the project or portfolio hits cash-flow breakeven, debt service breakeven, and economic breakeven (including return hurdle). Flag any scenario where price falls below breakeven for more than two consecutive quarters.

6. **Recommend hedging strategy**: Based on risk tolerance, cost of hedging, and forward curve shape, recommend an instrument mix:
   - **Swaps** for certainty of cash flow (fixed price, full participation lock)
   - **Costless collars** for floor protection with upside participation
   - **Put options** for downside protection while retaining full upside (premium cost required)
   - **Three-way collars** to reduce or eliminate premium by selling a deeper put
   - Specify recommended hedge ratios by tenor (e.g., 75% of PDP production for 12 months, 50% for months 13–24) [VERIFY against lender or board policy constraints]

7. **Document basis risk**: If the production point differs from the hedge benchmark, quantify historical basis differential volatility and recommend basis swaps or location differentials if material.

## Output

Produce a **Commodity Price Risk Report** containing:

- **Executive summary**: one-paragraph overview of net exposure, key risk, and recommended action
- **Exposure map table**: gross and net (post-hedge) volumes by commodity, quarter, and delivery point
- **Forward curve chart**: current strip vs. historical averages with break-even price overlaid
- **Scenario analysis table**: revenue, EBITDA, and DSCR under base, downside, upside, and stress cases
- **Break-even waterfall**: chart showing all-in cost buildup per unit vs. current strip price
- **Hedge recommendation summary**: instrument type, notional volume, tenor, indicative pricing, and estimated cost/premium
- **Risk register**: residual risks (basis risk, volumetric risk, counterparty credit, liquidity risk) with severity rating

## Quality Checks

- Confirm that forward curve data is sourced from a recognized exchange or broker dealer and is dated within 2 business days of analysis
- Verify that hedge ratios do not exceed any covenant or policy ceiling [VERIFY]
- Ensure break-even costs are consistent with the operator's most recent cost report or reserve report
- Check that scenario magnitudes are calibrated to actual historical drawdowns, not arbitrary round numbers
- Validate that mark-to-market calculations use consistent valuation methodology (mid-market vs. bid/ask)
- Confirm that basis differential assumptions reflect the correct delivery point and index pairing
- Flag any commodity where liquidity in the futures market is thin beyond the recommended hedge tenor
