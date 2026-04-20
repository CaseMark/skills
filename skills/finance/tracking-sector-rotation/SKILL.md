---
name: tracking-sector-rotation
language: en
description: Monitors sector performance rotation with factor exposure and macro sensitivity analysis. Use when tracking sector rotation, analyzing factor exposures, or identifying sector trends.
tags:
  - monitoring
  - equity-research
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---
# Tracking Sector Rotation

Monitors sector performance rotation with factor exposure and macro sensitivity analysis.

## When To Use

- Periodic (weekly/monthly) review of GICS sector relative performance to identify leadership transitions
- Evaluating whether current portfolio sector tilts align with observed rotation trends
- Assessing factor crowding risk when multiple sectors share dominant factor exposures
- Screening for early-stage rotation signals triggered by macro regime shifts (rate moves, credit spreads, PMI inflections)
- Preparing sector allocation input for investment committee or portfolio rebalance decisions

## Inputs To Gather

- **Sector return series**: Total return data for each GICS sector (or custom sector schema) over trailing 1W, 1M, 3M, 6M, 12M windows
- **Benchmark weights**: Current sector weights in the reference index (e.g., S&P 500, MSCI World)
- **Factor exposure data**: Sector-level betas or loadings to standard factors — value, momentum, quality, size, volatility, growth
- **Macro indicators**: Recent readings and direction-of-change for key drivers — 10Y yield, USD index, ISM/PMI, credit spreads (IG/HY OAS), oil price, breakeven inflation
- **Fund/portfolio positioning**: Current sector over/underweights relative to benchmark
- **Flow data** (optional): ETF sector fund flows for demand signal confirmation

## Workflow

1. **Build the performance heatmap**
   - Rank sectors by total return across each trailing window (1W through 12M)
   - Compute relative return vs. benchmark for each period
   - Flag sectors where short-term rank diverges sharply from long-term rank (potential rotation inflection)

2. **Identify rotation pattern**
   - Classify the current regime: early-cycle (cyclicals leading), mid-cycle (broadening), late-cycle (defensives firming), or contraction (utilities/staples outperforming)
   - Compare current leadership to the prior period — note which sectors are gaining/losing relative momentum
   - Tag any sector that has moved more than two rank positions in the last month as a "rotation candidate"

3. **Analyze factor exposures**
   - For each sector, report dominant factor tilts (e.g., Technology = high growth + momentum; Financials = high value + rate sensitivity)
   - Identify factor concentration risk: if leading sectors share the same factor (e.g., top 3 sectors all high-momentum), flag crowding concern
   - Note factor regime shifts — e.g., value-over-growth reversal, low-vol premium compression

4. **Map macro sensitivities**
   - For each sector, summarize directional sensitivity to key macro variables:
     - Rising rates: positive for Financials, negative for Utilities/REITs [VERIFY current beta estimates]
     - USD strength: negative for Materials/Energy exporters, mixed for Tech
     - Credit spread widening: negative for Financials/high-leverage sectors
     - PMI expansion: positive for Industrials, Materials, Consumer Discretionary
   - Highlight where macro direction-of-travel supports or contradicts the observed rotation

5. **Assess portfolio implications**
   - Compare current portfolio sector weights against the rotation thesis
   - Identify sectors where the portfolio is positioned against the trend (contrarian risk or opportunity)
   - Flag any sector where position size exceeds 2x benchmark weight as concentration risk

6. **Synthesize and flag**
   - Summarize the rotation narrative in 2-3 sentences (e.g., "Rotation from growth to value/cyclicals, consistent with early PMI recovery and steepening yield curve")
   - List actionable sector calls: overweight, underweight, or watch
   - Mark any data gaps, stale inputs, or conflicting signals with [VERIFY]

## Output

The tracking report should include:

- **Sector performance table**: Returns by period with rank and rank-change columns
- **Rotation signal summary**: Current regime classification, direction of rotation, conviction level (high/medium/low)
- **Factor exposure matrix**: Sector-by-factor grid showing dominant loadings and any crowding flags
- **Macro sensitivity map**: Sector-by-macro-variable directional table with current macro stance noted
- **Portfolio positioning gap**: Table comparing portfolio weights vs. benchmark vs. rotation-implied tilts
- **Action items**: Specific sector over/underweight recommendations with supporting rationale
- **Watch list**: Sectors at inflection points requiring monitoring before action

## Quality Checks

- Confirm all return data is from the same source and uses consistent total-return methodology (not price-only)
- Verify that sector classification (GICS vs. ICB vs. custom) is consistent across performance data and factor models
- Check that macro indicator readings are current (within 1 week for high-frequency data like PMI, within 1 day for rates/spreads)
- Ensure factor exposure data vintage matches the analysis date — stale factor betas from a different regime mislead
- Cross-check rotation signals against sector ETF flow data for confirmation; divergence between price momentum and flows warrants a [VERIFY] flag
- Validate that any regime classification is supported by at least two independent macro indicators, not a single data point
- Confirm portfolio weight data reflects actual current holdings, not model/target weights
