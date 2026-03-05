---
name: managing-fixed-income-attribution
description: Structures fixed income performance attribution across duration, credit, and sector allocation effects. Use when attributing fixed income returns, analyzing portfolio performance, or decomposing return drivers.
tags:
  - management
  - fixed-income
  - portfolio
  - credit
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Fixed Income Attribution

Decomposes fixed income portfolio returns into constituent effects — duration/yield curve, credit spread, sector allocation, and security selection — to explain performance versus a benchmark and identify repeatable alpha sources.

## When To Use

- Preparing monthly or quarterly performance attribution reports for investment committees or clients
- Diagnosing why a fixed income portfolio outperformed or underperformed its benchmark
- Evaluating portfolio manager skill across interest rate positioning, credit selection, and sector rotation
- Supporting compliance reviews that require transparent return decomposition
- Feeding attribution results into risk budgeting or allocation rebalancing decisions

## Inputs To Gather

- **Portfolio holdings** with market values, durations, spreads, and sector classifications at period start and end
- **Benchmark composition** (e.g., Bloomberg US Aggregate, ICE BofA indices) with matching granularity
- **Return series** — total return, price return, and income return for both portfolio and benchmark
- **Yield curve data** — par/spot/forward curves at period start and end (Treasury + swap if applicable)
- **Spread data** — OAS or Z-spread by sector and rating bucket at period start and end
- **Transaction log** — trades executed during the period (for intra-period rebalancing effects)
- **Attribution methodology selection** — Campisi, Brinson-Fachler adapted for fixed income, or factor-based [VERIFY methodology approved by the firm's performance team]

## Workflow

1. **Validate inputs and align classifications**
   - Confirm holdings data reconciles to custodian/accounting NAV
   - Map portfolio and benchmark securities to consistent sector/rating/maturity buckets
   - Verify curve and spread data timestamps match the attribution period boundaries
   - Flag any securities missing key analytics (duration, OAS) and determine proxy approach

2. **Decompose benchmark return into systematic effects**
   - **Income effect**: accrued coupon and pull-to-par for the period
   - **Treasury/yield curve effect**: return attributable to changes in the risk-free curve (shift, twist, butterfly)
   - **Spread effect**: return from aggregate spread changes across the benchmark
   - **Residual**: convexity, roll-down, and any model noise

3. **Compute portfolio-level effects and differentials**
   - Calculate the same return components for the portfolio
   - Derive active return = portfolio total return − benchmark total return
   - Attribute active return across:
     - **Duration/curve positioning**: over/underweight duration and curve placement vs. benchmark
     - **Credit spread allocation**: sector and rating bucket spread bets
     - **Security selection**: bond-level excess return within each bucket after removing systematic factors
     - **Trading/timing**: impact of intra-period transactions vs. buy-and-hold assumption

4. **Reconcile and cross-check**
   - Sum of all attribution effects must reconcile to total active return within an acceptable tolerance (typically ≤ 2 bps)
   - If residual exceeds tolerance, investigate: missing cash effect, FX overlay, derivative overlay not captured, or sector mapping mismatches
   - Compare results against prior-period attribution to detect sign flips or anomalous magnitudes

5. **Synthesize narrative and reporting**
   - Rank effects by absolute contribution to active return
   - Provide plain-language explanation of the top 3 drivers (positive and negative)
   - Highlight any one-off or non-repeatable effects (e.g., a single distressed bond rally)
   - Present results in standardized table format with period-over-period comparison

## Output

- **Attribution summary table**: rows for each effect (income, curve, spread, selection, trading), columns for portfolio return, benchmark return, and active contribution
- **Sector/rating drill-down**: attribution broken out by BICS or GICS sector and by rating tier (AAA, AA, A, BBB, HY if applicable)
- **Curve positioning exhibit**: visual or tabular comparison of portfolio vs. benchmark key-rate duration profile
- **Narrative commentary**: 1–2 paragraph executive summary suitable for client letters or IC memos
- **Reconciliation footnote**: residual amount and explanation if material

## Quality Checks

- Total active return reconciles to the sum of attribution effects within ±2 bps
- Income effect is positive and directionally consistent with portfolio yield vs. benchmark yield
- Duration effect sign matches the direction of rate moves relative to portfolio's duration overweight/underweight
- Spread effect sign aligns with portfolio's credit beta positioning and actual spread movement direction
- No single "residual" or "other" bucket exceeds 20% of total active return without documented explanation
- Sector classifications are consistent between portfolio and benchmark (no mismatches inflating allocation effects)
- [VERIFY] Attribution methodology matches the firm's GIPS-compliant performance presentation standards
- [VERIFY] Return calculations use the pricing source and day-count conventions specified in the IPS or client agreement
- [VERIFY] Derivative overlays (futures, swaps, CDS) are correctly mapped to their economic exposure buckets rather than reported as a single line item
