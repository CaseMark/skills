---
name: modeling-revenue-forecasts
description: Builds bottom-up revenue models from segment-level drivers with assumption documentation. Use when forecasting revenue, modeling growth drivers, or building segment-level projections.
tags:
  - modeling
  - equity-research
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Revenue Forecasts

## When To Use

- Building bottom-up revenue projections from segment-level volume and pricing drivers
- Forecasting revenue for equity research initiation, earnings preview, or model updates
- Translating management guidance and KPIs into quantified segment assumptions
- Stress-testing revenue scenarios for investment committee or portfolio review
- Bridging historical reported revenue to forward estimates after an M&A event, divestiture, or segment reclassification

## Inputs To Gather

- **Historical financials**: Minimum 8–12 quarters of segment-level revenue (10-K/10-Q or equivalent filings) [VERIFY filing currency and fiscal year-end]
- **Segment definitions**: Current reporting segments, any recent reclassifications, and inter-segment eliminations
- **Volume drivers**: Units shipped, subscribers, MAUs, transactions, beds occupied, same-store counts — whatever the natural unit for each segment
- **Price/mix drivers**: ASP trends, ARPU, contract renewals, price escalators, FX rates for international segments
- **Management guidance**: Most recent earnings call commentary, investor day targets, and any quantified KPIs
- **Industry/macro data**: TAM estimates, market growth rates, competitive share data, and relevant macro indicators (GDP, CPI, housing starts, etc.) [VERIFY source vintage]
- **Consensus context** (optional): Street estimates for comparison and sanity-checking

## Workflow

1. **Map the segment structure**
   - List each reporting segment and sub-segment with its most recent annual and quarterly revenue
   - Note inter-segment eliminations and reconcile to consolidated revenue
   - Flag any segment changes in the lookback period; restate historicals on a comparable basis where possible

2. **Decompose each segment into drivers**
   - Identify the primary quantity × price formula (e.g., subscribers × ARPU, units × ASP, same-store sales + new store contribution)
   - For each driver, pull historical values and compute trailing growth rates, seasonality indices, and trend lines
   - Separate organic growth from acquired/divested revenue contributions

3. **Set forward assumptions**
   - For each driver, define base-case, upside, and downside assumptions with a one-line rationale
   - Anchor assumptions to at least one verifiable reference: management guidance, industry data, or historical trend
   - Mark any assumption lacking direct support with [VERIFY]
   - Apply FX assumptions consistently across international segments [VERIFY spot vs. forward rates]

4. **Build the model**
   - Construct a quarterly build-up: volume × price per segment, rolling up to consolidated revenue
   - Include a seasonality adjustment layer using historical seasonal indices
   - Add a bridge table showing Y/Y revenue change decomposed into volume, price/mix, FX, and M&A contributions
   - Carry the model forward for the explicit forecast period (typically 2–5 years for equity research)

5. **Validate and stress-test**
   - Compare model output against consensus and management guidance ranges; investigate deviations > 2%
   - Run sensitivity tables on the two or three highest-impact drivers (e.g., ±100 bps on volume growth, ±5% on ASP)
   - Check implied margins and growth rates for internal consistency with COGS and opex models if available
   - Verify that quarterly cadence produces a sensible annual total (no rounding drift)

6. **Document assumptions and output**
   - Produce an assumptions table listing each driver, its historical value, forward assumption, and source/rationale
   - Summarize key risks to the forecast (customer concentration, contract renewals, regulatory changes) [VERIFY sector-specific risks]
   - State model limitations: segments not decomposed, drivers treated as exogenous, and data gaps

## Output

- **Revenue build-up table**: Quarterly and annual segment revenue with driver-level detail
- **Y/Y bridge**: Volume / price / mix / FX / M&A contribution waterfall
- **Assumptions register**: Driver, historical baseline, forecast value, rationale, and source for each assumption
- **Sensitivity matrix**: Revenue impact from varying the top 2–3 drivers across base / bull / bear
- **Narrative summary**: 1–2 paragraphs describing the revenue trajectory, key inflection points, and primary forecast risks

## Quality Checks

- All historical segment revenues reconcile to reported consolidated totals within rounding tolerance
- Every forward assumption has an explicit rationale — no "assumed flat" without justification
- Seasonal patterns in the quarterly build-up match historical indices (Q1 vs. Q4 weighting, etc.)
- Sensitivity ranges are symmetric and plausible; extreme cases do not produce negative revenue for stable segments
- FX assumptions are applied consistently and disclosed [VERIFY base currency and translation method]
- Any data point sourced from third-party research or management commentary is cited with date and document
- [VERIFY] markers remain on any assumption the analyst has not independently corroborated
