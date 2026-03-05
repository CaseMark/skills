---
name: analyzing-commodity-markets
description: Structures commodity market analysis with supply/demand balances, inventory dynamics, and price driver attribution. Use when analyzing commodities, evaluating supply/demand, or forecasting commodity prices.
tags:
  - analysis
  - economic-analysis
metadata:
  author: casemark
  practice_areas:
    - Economic Research
    - Macroeconomics
    - Policy Analysis
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Commodity Markets

Structures commodity market analysis with supply/demand balances, inventory dynamics, and price driver attribution.

## When To Use

- Building a supply/demand balance for a specific commodity (e.g., crude oil, copper, wheat, natural gas)
- Attributing recent price moves to fundamental, technical, or macro drivers
- Evaluating inventory dynamics — draws, builds, days-of-supply coverage
- Assessing the impact of policy changes (tariffs, export bans, sanctions, subsidies) on commodity flows
- Comparing forward curve structure (contango/backwardation) against physical market signals
- Preparing commodity-focused sections of macro research notes or investment committee materials

## Inputs To Gather

- **Commodity and timeframe**: Specific commodity (or commodity complex) and the analysis horizon (spot, quarterly, annual)
- **Production data**: Global and regional output figures, capacity utilization, rig counts, planted acreage, or mine throughput as applicable
- **Consumption/demand data**: Sectoral demand breakdown (industrial, transport, power generation, feed/food), regional demand estimates
- **Inventory levels**: Exchange-reported stocks (LME, COMEX, SHFE), commercial and strategic reserve levels, floating storage or in-transit volumes
- **Price series**: Spot, front-month futures, and relevant spreads (crack spreads, crush margins, locational basis)
- **Policy/event context**: Sanctions, OPEC+ decisions, weather events, trade policy shifts, regulatory changes [VERIFY current policy status]
- **Forward curve and positioning**: Futures term structure, CFTC/COT managed-money positioning, options open interest

## Workflow

1. **Define scope and commodity taxonomy**
   - Identify whether the analysis covers a single commodity, a complex (e.g., energy, base metals, agriculture), or a cross-commodity theme
   - Set the time horizon: near-term (spot to 3 months), medium-term (1–4 quarters), or structural (multi-year)

2. **Construct the supply/demand balance**
   - Build a table with production, consumption, net trade, and implied stock change by period
   - Separate known data periods from forecast periods; label forecasts clearly
   - Identify the marginal source of supply (swing producer, marginal cost curve position)
   - Note any supply disruptions, maintenance schedules, or ramp-ups in new capacity [VERIFY production figures against latest reporting agency data — EIA, IEA, USDA, ICSG, etc.]

3. **Analyze inventory dynamics**
   - Calculate days-of-supply coverage (inventories / daily consumption)
   - Compare current stocks to 5-year seasonal range and identify whether levels are above, below, or within normal bands
   - Assess visible vs. estimated invisible inventories (e.g., Chinese bonded warehouse stocks, floating storage)
   - Note rate of change — whether stocks are drawing or building, and at what pace relative to seasonal norms

4. **Attribute price drivers**
   - Decompose recent price action into categories:
     - **Fundamental**: supply outage, demand surprise, inventory report
     - **Macro**: USD moves, rate expectations, GDP revisions, risk appetite
     - **Technical/positioning**: speculative positioning extremes, options expiry, trend-following signals
     - **Policy/geopolitical**: sanctions, tariffs, weather, conflict disruption
   - Rank drivers by estimated magnitude of price impact

5. **Evaluate forward curve structure**
   - Characterize the curve as contango, backwardation, or flat and note the degree ($/unit, % annualized)
   - Interpret the curve signal: backwardation typically signals tight physical markets; contango suggests ample supply or weak spot demand
   - Compare curve shape to inventory trajectory — divergences may flag mispricing or hidden stock shifts

6. **Assess risks and scenarios**
   - Identify the top 2–3 upside and downside risks to the base case balance
   - Quantify scenario impact where possible (e.g., "loss of 1 mb/d Libyan supply would shift the balance to a 0.5 mb/d deficit")
   - Flag binary event risks (elections, OPEC meetings, crop reports) and their timing

## Output

Structure the deliverable as:

- **Executive summary**: 3–5 sentence overview of the commodity's current state, balance trajectory, and price view
- **Supply/demand balance table**: Quarterly or annual, with production, consumption, stock change, and price assumptions
- **Inventory analysis**: Current levels, seasonal context, days-of-supply, trajectory
- **Price driver attribution**: Ranked list of factors moving the market, with directional impact
- **Forward curve commentary**: Structure description, interpretation, and any notable spread trades
- **Risk matrix**: Upside/downside scenarios with estimated probability and price impact
- **Key data releases calendar**: Upcoming reports that could shift the view (e.g., EIA weekly, USDA WASDE, OPEC MOMR)

## Quality Checks

- Supply/demand balance must arithmetically reconcile (production - consumption = stock change +/- net trade adjustments)
- All data sources and vintages are cited; no undated or unsourced figures
- Forecast assumptions are separated from reported actuals and clearly labeled
- Inventory comparisons use consistent units (barrels, tonnes, bushels) and seasonal adjustment methodology
- Price driver attribution avoids circular reasoning (don't attribute a price rise solely to "buying pressure" without identifying the catalyst)
- Forward curve analysis references actual curve data rather than generic statements
- [VERIFY] any referenced government policy, sanction, or trade restriction against current status — these change frequently
- [VERIFY] production quotas (OPEC+, mining country export limits) against most recent official announcements
