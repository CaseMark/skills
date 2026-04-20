---
name: managing-capital-structure
language: en
description: Analyzes optimal capital structure with WACC minimization, rating implications, and financing alternatives. Use when optimizing capital structure, analyzing debt capacity, or evaluating leverage targets.
tags:
  - management
  - corporate-finance
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
# Managing Capital Structure

## When To Use

- Evaluating whether to increase or decrease leverage (e.g., post-acquisition, recapitalization, or dividend policy change)
- Setting or revising a target debt-to-equity or debt-to-EBITDA range
- Assessing debt capacity ahead of a financing event (bond issuance, term loan, revolver draw)
- Responding to a credit rating agency review or downgrade watch
- Comparing financing alternatives (senior secured vs. unsecured, fixed vs. floating, bank vs. capital markets)
- Board or CFO request for a capital structure optimization memo

## Inputs To Gather

- **Financial statements**: Trailing 3 years of income statement, balance sheet, and cash flow statement
- **Existing debt schedule**: Instrument type, principal outstanding, maturity, coupon/rate, covenants, call provisions
- **EBITDA and free cash flow projections**: Base case plus downside scenario (minimum 3-year forecast)
- **Peer/comp set**: 5-10 comparable companies with public capital structure data
- **Credit rating details**: Current rating, agency commentary, key ratio thresholds for the target rating category [VERIFY against latest agency methodology]
- **Cost of equity inputs**: Beta, risk-free rate, equity risk premium, and any company-specific adjustments
- **Strategic context**: Planned M&A, capex programs, shareholder return commitments, or covenant headroom concerns

## Workflow

1. **Profile current capital structure**
   - Map all outstanding debt by seniority, maturity, rate type, and currency
   - Calculate current leverage ratios: Net Debt/EBITDA, Debt/Total Capital, Interest Coverage (EBITDA/Interest), FFO/Debt
   - Identify upcoming maturities and refinancing windows

2. **Benchmark against peers**
   - Pull comparable company leverage, coverage, and cost-of-debt metrics
   - Note median, 25th, and 75th percentile ranges
   - Flag where the company sits relative to peers on each metric

3. **Estimate WACC across leverage scenarios**
   - Build a WACC sensitivity table with 3-5 leverage increments (e.g., 1.0x to 4.0x Net Debt/EBITDA)
   - For each increment, estimate: pre-tax cost of debt (spread curve), after-tax cost of debt, relevered beta and cost of equity, blended WACC
   - Identify the leverage range that minimizes WACC — this is the theoretical optimum
   - Note that the WACC curve flattens in the middle range; precision beyond 10-20 bps is false accuracy

4. **Assess credit rating implications**
   - Map each leverage scenario to rating agency ratio thresholds (S&P, Moody's, Fitch as applicable) [VERIFY thresholds — agencies update methodologies periodically]
   - Identify the leverage ceiling that preserves the target rating
   - Stress-test: apply a revenue decline of 10-20% and check whether coverage ratios breach downgrade triggers

5. **Evaluate financing alternatives**
   - For the recommended leverage target, identify instrument options:
     - Revolving credit facility (liquidity buffer, undrawn commitment fees)
     - Term loan A/B (amortization profile, spread, flex terms)
     - Investment-grade or high-yield bonds (tenor, call schedule, covenant package)
     - Convertible notes, hybrid/subordinated instruments (equity credit treatment by rating agencies)
   - Compare all-in cost, covenant flexibility, execution certainty, and maturity profile
   - Consider fixed vs. floating mix and hedging requirements

6. **Formulate recommendation**
   - State recommended target leverage range (not a single point — use a band, e.g., 2.0x-2.5x Net Debt/EBITDA)
   - Specify instrument mix and sequencing (e.g., "refinance 2027 notes with new 10-year bond; maintain $500M undrawn revolver")
   - Quantify impact: change in WACC, incremental interest expense, effect on EPS, rating outcome
   - Define guardrails: maximum leverage before management action triggers (e.g., suspend buybacks above 3.0x)

## Output

The deliverable is a **Capital Structure Optimization Report** containing:

- **Executive summary**: Current state, recommended target range, key rationale (1 page)
- **Current capital structure profile**: Debt stack table with terms, maturity wall chart
- **Peer benchmarking**: Comparative leverage and coverage table
- **WACC analysis**: Sensitivity table showing WACC across leverage scenarios, chart of WACC curve
- **Rating impact matrix**: Leverage scenarios mapped to projected rating outcomes with stress-test overlay
- **Financing alternatives comparison**: Side-by-side table of instrument options with cost, terms, and trade-offs
- **Recommendation and action plan**: Target range, instrument selection, execution timeline, and governance triggers

## Quality Checks

- All leverage and coverage ratios are calculated consistently (same EBITDA definition — confirm whether adjustments include stock-based comp, restructuring charges, etc.)
- Peer set is genuinely comparable (similar industry, scale, geography, business model)
- Cost of debt estimates reflect current market spreads, not historical coupon rates on existing debt
- WACC analysis uses after-tax cost of debt with the correct marginal tax rate [VERIFY jurisdiction-specific rate]
- Rating thresholds are sourced from current agency criteria documents, not outdated references
- Stress scenario assumptions are disclosed and realistic (not worst-case-only or best-case-only)
- Recommendation includes a clear action trigger framework, not just a static target
- All projections and market data carry a stated as-of date
