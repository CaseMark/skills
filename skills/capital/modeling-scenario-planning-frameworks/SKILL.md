---
name: modeling-scenario-planning-frameworks
language: en
description: Builds corporate scenario planning models with macro assumption sets, strategic response options, and contingency plan development. Use when building scenario frameworks, planning strategic responses, or developing contingency strategies.
tags:
  - modeling
  - capital-allocation-and-corporate-strategy
metadata:
  author: casemark
  practice_areas:
    - Corporate Strategy
    - Capital Allocation
    - Shareholder Value
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Scenario Planning Frameworks

## When To Use

- Board or C-suite requests a structured view of how the business performs under different macro environments (recession, rate shifts, commodity shocks, regulatory change)
- Capital allocation decisions require stress-testing across multiple futures before committing spend
- Strategic planning cycle needs formalized upside / base / downside cases with linked operational responses
- M&A or divestiture evaluation where acquirer must model target performance under divergent assumptions
- Investor or lender presentations that require transparent scenario disclosure with quantified impact ranges

## Inputs To Gather

- **Macro assumption set**: GDP growth, inflation, interest rates, FX rates, commodity prices, unemployment — sourced from consensus forecasts, internal economics team, or management guidance [VERIFY sources and vintage dates]
- **Company financials**: 3–5 years of historicals (revenue, COGS, SG&A, capex, working capital, debt schedule) plus latest budget/forecast
- **Strategic levers**: list of management actions available per scenario (headcount freeze, capex deferral, pricing pass-through, product launch acceleration, share repurchase suspension)
- **Scenario definitions**: typically 3–5 named scenarios (e.g., Soft Landing, Stagflation, Deep Recession, Rapid Recovery) with narrative descriptions of the macro path
- **KPI thresholds**: board-approved triggers or guardrails (e.g., net leverage > 3.5×, liquidity < $200M, dividend coverage < 1.2×) that activate contingency responses
- **Time horizon**: usually 3–5 years; confirm whether quarterly or annual granularity is needed

## Workflow

1. **Anchor the base case** — Map current consensus or management forecast into the model as the base scenario. Tie every revenue and cost line to at least one macro driver so assumptions are traceable.

2. **Define scenario narratives** — Write a 2–3 sentence narrative for each scenario describing the macro path, timing, and severity. Ensure scenarios span a realistic range — avoid clustering around the base case.

3. **Build the macro-to-P&L transmission map** — For each scenario, specify how macro variables flow into financials:
   - Revenue: volume sensitivity to GDP, pricing sensitivity to inflation/FX
   - COGS: input cost linkage to commodities, labor cost linkage to wage inflation
   - Interest expense: floating-rate debt repricing under rate scenarios
   - Capex: discretionary vs. maintenance split and deferral rules
   - Working capital: DSO/DIO/DPO shifts under stress

4. **Layer strategic response options** — For each downside scenario, attach specific management actions with quantified P&L and cash flow impact:
   - Hiring freeze: estimated savings = open headcount × avg loaded cost × months
   - Capex deferral: identify discretionary projects and deferral timeline
   - Pricing actions: pass-through rate × revenue base × elasticity adjustment
   - Portfolio actions: divestiture proceeds, restructuring charges

5. **Calculate key outputs per scenario** — Revenue, EBITDA, free cash flow, net debt, leverage ratio, liquidity, dividend coverage, ROIC. Present in a side-by-side comparison table.

6. **Set contingency triggers** — Map KPI thresholds to specific response packages. Example: if trailing net leverage exceeds 3.0× for two consecutive quarters, activate Package A (capex freeze + dividend cut). [VERIFY thresholds against existing credit agreement covenants and board policies]

7. **Run sensitivity overlays** — Within each scenario, flex the 2–3 most uncertain assumptions ±10–20% to show output ranges. Present as tornado charts on EBITDA and FCF.

8. **Stress-test liquidity** — For downside scenarios, build a monthly cash flow waterfall showing whether the company can fund operations, debt service, and minimum capex without drawing on revolving credit or raising capital.

## Output

Deliver a scenario planning package containing:

- **Scenario summary table**: one-page matrix showing macro assumptions, financial outcomes (revenue, EBITDA, FCF, leverage), and probability-weighted expected values across all scenarios
- **Detailed financial schedules**: full P&L, cash flow, and balance sheet projections per scenario at the agreed granularity
- **Strategic response menu**: table mapping each contingency trigger to its response package, estimated financial impact, and implementation timeline
- **Sensitivity tornado charts**: for EBITDA and FCF under each scenario, showing which assumptions drive the widest variance
- **Liquidity bridge**: monthly cash waterfall for downside scenarios showing headroom against credit facilities and covenant limits
- **Narrative memo**: 1–2 page executive summary describing key findings, highest-risk scenarios, and recommended pre-positioning actions

## Quality Checks

- Every financial output must trace back to a named macro assumption — no orphan line items
- Scenario ranges should be meaningfully differentiated; if upside and downside EBITDA differ by less than 15%, challenge whether scenarios are sufficiently distinct
- Verify that strategic response savings do not double-count (e.g., headcount freeze savings should not also appear in a separate SG&A reduction line)
- Confirm leverage and liquidity calculations use the correct debt definitions matching credit agreement terms [VERIFY]
- Probability weights across scenarios must sum to 100%; confirm weights reflect management or board view, not model-builder opinion
- Cross-check base case projections against sell-side consensus or prior management guidance to flag material deviations
- Ensure contingency triggers reference the same KPI definitions used in covenant compliance reporting [VERIFY]
