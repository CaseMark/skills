---
name: analyzing-distressed-credit-situations
language: en
description: Evaluates distressed debt opportunities with recovery analysis, liquidity assessment, and potential restructuring outcomes. Use when screening distressed situations, analyzing stressed credits, or evaluating workout scenarios.
tags:
  - analysis
  - distressed-and-restructuring
  - credit
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Distressed Credit Situations

Evaluates distressed debt opportunities by combining capital structure analysis, liquidity runway assessment, recovery waterfall modeling, and restructuring path evaluation to produce actionable investment or advisory recommendations.

## When To Use

- Screening a new distressed or stressed credit for potential investment
- Evaluating recovery prospects across tranches in an overleveraged capital structure
- Assessing whether a borrower is heading toward an out-of-court workout, exchange offer, or Chapter 11 filing
- Comparing restructuring outcomes (e.g., amend-and-extend vs. debt-for-equity swap vs. Section 363 sale)
- Updating a thesis when a credit event occurs (missed coupon, covenant breach, ratings downgrade, liquidity draw)

## Inputs To Gather

- **Capital structure**: All funded debt tranches with principal amounts, interest rates (fixed/floating), maturities, call protection, and intercreditor terms
- **Financial statements**: Trailing 2–3 years of income statement, balance sheet, and cash flow statement; management projections if available
- **Credit documents**: Credit agreement or indenture excerpts — focus on covenants, subordination, change-of-control provisions, and cross-default triggers
- **Market data**: Current trading levels for each tranche (price, YTW, spread), CDS levels if available, and comparable distressed transactions
- **Operational context**: Industry dynamics, competitive position, management track record, pending litigation, regulatory exposure
- **Catalyst timeline**: Upcoming maturities, debt service payments, covenant test dates, or known negotiation milestones

## Workflow

1. **Map the capital structure**
   - Build a tranche-by-tranche table: instrument, seniority, face amount, coupon, maturity, current price, accrued and PIK balances
   - Identify secured vs. unsecured, first lien vs. second lien, and any structural subordination across legal entities
   - Calculate total leverage, secured leverage, and interest coverage on LTM and projected EBITDA

2. **Assess liquidity runway**
   - Build a 13-week (or 26-week) cash flow projection if near-term liquidity is the primary concern
   - Identify minimum cash needed to operate (payroll, critical vendors, insurance, regulatory minimums)
   - Determine revolver availability (net of borrowing base constraints, springing covenants, or blocked conditions)
   - Estimate runway to a liquidity wall — the date cash is exhausted absent intervention

3. **Perform recovery analysis**
   - Estimate enterprise value under multiple scenarios: going-concern (EBITDA multiple), liquidation (asset-by-asset), and sale (comparable transaction multiples)
   - Apply the priority waterfall: administrative claims → DIP facility → first lien secured → second lien → unsecured → subordinated → equity
   - Calculate recovery rate per tranche under each scenario; express as cents on the dollar
   - Sensitivity-test key assumptions: EBITDA level (±10–20%), valuation multiple (±0.5–1.0x), and liquidation discount rates

4. **Evaluate restructuring paths**
   - **Amend-and-extend / repricing**: Feasible if the business is fundamentally viable but faces a near-term maturity wall; requires lender consent thresholds [VERIFY consent thresholds in credit agreement]
   - **Exchange offer / liability management**: Assess uptake likelihood, holdout risk, and whether existing docs permit open-market purchases or below-par buybacks
   - **Out-of-court workout**: Viable when creditor classes are few and aligned; faster and cheaper but requires near-unanimous consent
   - **Chapter 11 filing**: Consider when out-of-court fails, when Section 363 sale maximizes value, or when cramdown is needed to bind dissenting classes [VERIFY jurisdiction-specific filing considerations]
   - **Liquidation (Chapter 7)**: Benchmark for creditors — if liquidation recovery exceeds reorganization value, Chapter 7 is the rational outcome

5. **Synthesize investment or advisory thesis**
   - State the recommended position (long/short/avoid) or advisory recommendation with conviction level
   - Identify the fulcrum security — the tranche where value breaks in the waterfall
   - Articulate upside, base, and downside scenarios with associated recovery ranges
   - Flag key risks: litigation overhang, fraudulent-conveyance exposure, intercreditor disputes, regulatory blocks
   - Define catalysts and timeline for value realization or further deterioration

## Output

Produce a structured distressed credit analysis containing:

- **Executive summary**: One-paragraph situation overview, current trading levels, and primary recommendation
- **Capital structure table**: Tranche detail with face value, price, implied recovery, and yield metrics
- **Liquidity analysis**: Cash runway estimate with key assumptions and trigger dates
- **Recovery waterfall**: Scenario-based recovery by tranche (going-concern, liquidation, sale)
- **Restructuring path assessment**: Comparison matrix of restructuring alternatives with feasibility, timeline, and likely recovery by class
- **Risk factors and catalysts**: Prioritized list of upside/downside drivers with monitoring triggers
- **Appendix**: Sensitivity tables, comparable transaction data, and covenant compliance summary

## Quality Checks

- Verify that the capital structure sums correctly and that no tranches are missing (cross-check against 10-K/10-Q filings or offering memoranda)
- Confirm that the recovery waterfall respects documented priority of claims — do not assume equitable subordination or recharacterization without basis
- Ensure liquidity projections use defensible assumptions; mark management-provided forecasts distinctly from independent estimates
- Validate valuation multiples against actual comparable transactions, not generic industry averages
- Flag any data point sourced from a single unverified source with [VERIFY]
- Confirm that covenant thresholds, cure periods, and cross-default triggers are drawn from the actual credit documents, not summaries [VERIFY against executed agreements]
- Stress-test that the recommendation holds under the downside scenario, not just the base case
