---
name: managing-foreign-exchange-hedging
language: en
description: Structures FX hedging programs with exposure identification, instrument selection, and hedge effectiveness testing. Use when managing FX risk, designing hedge programs, or testing hedge effectiveness.
tags:
  - management
  - corporate-finance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Corporate Finance
    - Treasury
    - Financial Planning
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Foreign Exchange Hedging

Structures FX hedging programs with exposure identification, instrument selection, and hedge effectiveness testing.

## When To Use

- Designing or restructuring a corporate FX hedging program
- Mapping currency exposures across subsidiaries, supply chains, or revenue streams
- Selecting hedging instruments (forwards, options, cross-currency swaps, NDFs)
- Testing hedge effectiveness under ASC 815 / IFRS 9 / IAS 39 requirements [VERIFY applicable standard]
- Preparing hedge documentation for audit or board review
- Evaluating whether to hedge transaction, translation, or economic exposures

## Inputs To Gather

- **Exposure inventory**: Currency pairs, notional amounts, expected settlement dates, and source (AR/AP, intercompany loans, forecasted revenue, capital expenditures)
- **Financial statements**: Balance sheet and P&L by entity/currency for translation exposure sizing
- **Existing hedge portfolio**: Outstanding contracts, mark-to-market positions, tenor profile, counterparty allocation
- **Risk tolerance parameters**: Board-approved hedge ratios, maximum open exposure limits, VaR or CFaR targets
- **Accounting treatment elections**: Cash flow hedge, fair value hedge, or net investment hedge designations
- **Market data**: Spot rates, forward curves, implied volatility surfaces, basis swap spreads for relevant currency pairs
- **Policy documents**: Current FX risk management policy, delegation of authority matrix, ISDA/CSA terms

## Workflow

1. **Map exposures**
   - Aggregate all FX exposures by currency pair, entity, and time bucket (monthly or quarterly out to 12–24 months)
   - Classify each exposure as transaction (committed or forecasted), translation, or economic
   - Quantify net exposure after natural offsets (e.g., USD revenues against USD costs in the same entity)
   - Flag highly probable forecasted transactions vs. firm commitments — hedge accounting eligibility differs [VERIFY probability thresholds per standard]

2. **Set hedge objectives and ratios**
   - Align hedge ratios with policy bands (e.g., 50–80% of forecasted exposures within 0–6 months, 25–50% for 6–12 months)
   - Define the hedged risk clearly: spot risk only, spot + forward points, or full fair value
   - Determine whether cost-of-hedging components (forward points, time value of options) are excluded from effectiveness testing under IFRS 9 [VERIFY if applicable]

3. **Select instruments**
   - **Forwards/NDFs**: Default for hedging known or highly probable cash flows; match notional and maturity to exposure; consider window forwards for uncertain timing
   - **Options (vanillas, collars, seagulls)**: Use when downside protection is needed but upside participation is desired; evaluate premium cost vs. risk budget
   - **Cross-currency swaps**: Appropriate for long-dated intercompany loans or foreign-currency debt; structure fixed-for-fixed or fixed-for-floating based on liability profile
   - **FX swaps / rollovers**: Manage short-term liquidity mismatches or roll maturing hedges
   - Assess counterparty credit limits and netting agreements before execution

4. **Document hedge relationships**
   - For each designated hedge, prepare formal documentation at inception:
     - Hedging instrument identification (trade ID, terms)
     - Hedged item or transaction description
     - Nature of hedged risk
     - Effectiveness assessment method (dollar-offset, regression, critical-terms-match, hypothetical derivative)
     - Hedge ratio and sources of ineffectiveness
   - Ensure documentation is contemporaneous — retroactive designation is not permitted [VERIFY specific standard requirements]

5. **Test hedge effectiveness**
   - **Prospective testing**: At inception and each reporting date, confirm the hedge is expected to be highly effective
   - **Retrospective testing**: Measure actual offset between hedging instrument and hedged item fair value changes
   - Under ASC 815: 80–125% effectiveness corridor for dollar-offset method; regression requires R-squared ≥ 0.80 and slope between -0.80 and -1.25 [VERIFY current thresholds]
   - Under IFRS 9: No bright-line quantitative threshold — assess economic relationship, credit risk dominance, and hedge ratio alignment
   - Record ineffectiveness in earnings; do not defer ineffective portions through OCI

6. **Monitor and rebalance**
   - Track hedge coverage ratios against policy targets monthly
   - Monitor roll costs, basis risk, and counterparty exposure concentrations
   - Rebalance hedges when exposure forecasts change materially (e.g., lost contract, revised revenue guidance)
   - Under IFRS 9, rebalancing adjusts the hedge ratio without discontinuation; under ASC 815, de-designation and re-designation may be required [VERIFY]

## Output

- **FX exposure map**: Currency-by-currency summary of gross and net exposures with time bucketing
- **Hedge program recommendation**: Instrument selection, notional sizing, tenor laddering, and estimated hedge cost (forward points, option premiums)
- **Hedge documentation package**: Formal designation memos for each hedge relationship
- **Effectiveness testing results**: Prospective and retrospective test outcomes with pass/fail status per reporting period
- **Dashboard metrics**: Hedge coverage ratios, weighted-average hedge rates, unrealized MTM by currency pair, counterparty utilization

## Quality Checks

- Verify that net exposure calculations properly account for intercompany elimination and natural offsets
- Confirm hedge notionals do not exceed forecasted exposure amounts (over-hedging invalidates hedge accounting)
- Ensure all designated hedges have contemporaneous documentation before trade execution
- Validate effectiveness test calculations against independent market data sources
- Check that accounting entries correctly bifurcate effective vs. ineffective portions
- Review counterparty concentration against single-name and aggregate credit limits
- Confirm compliance with applicable accounting standard (ASC 815, IFRS 9, or local GAAP) — mark any jurisdiction-specific variance with [VERIFY]
