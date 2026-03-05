---
name: analyzing-commitment-pacing-models
description: Builds LP commitment pacing with deployment curves, distribution assumptions, and NAV projection for portfolio planning. Use when modeling commitment pacing, projecting LP cash flows, or planning new fund allocations.
tags:
  - analysis
  - investor-relations-and-lp-reporting
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Commitment Pacing Models

## When To Use

- Modeling forward commitment schedules against an LP's allocation targets and liquidity constraints
- Projecting net cash flows (capital calls minus distributions) across existing and prospective fund commitments
- Evaluating whether a new fund commitment fits within the LP's pacing plan without breaching allocation bands
- Building NAV build-up and runoff projections for board or investment committee reporting
- Stress-testing a portfolio under accelerated drawdown or delayed distribution scenarios

## Inputs To Gather

- **Existing portfolio data**: Fund name, vintage year, commitment size, unfunded balance, current NAV, cumulative contributions and distributions, TVPI/DPI to date
- **Target allocation parameters**: Total portfolio AUM, private markets allocation target (% and $), allowable over/under-commitment band, asset class sub-targets (buyout, venture, real assets, credit, etc.)
- **Deployment curve assumptions**: Expected drawdown pace by strategy type (e.g., buyout typically 20-25% Y1, 25-30% Y2, 20-25% Y3; venture more front-loaded on commitments but slower on calls) [VERIFY against GP-provided schedules when available]
- **Distribution assumptions**: Expected distribution timing by strategy — DPI ramp typically begins Y4-Y5 for buyout, Y5-Y7 for venture; recycling provisions if applicable
- **Prospective commitments**: Candidate funds with expected closing dates, commitment sizes, and strategy classifications
- **Macro/liquidity inputs**: Denominator effect sensitivity (public equity return assumptions), LP cash reserve requirements, any hard liquidity constraints (e.g., pension benefit payments)

## Workflow

1. **Map existing portfolio obligations**
   - Catalog all active fund commitments with unfunded balances
   - Assign each fund a deployment curve based on strategy type, vintage, and GP-reported pacing guidance
   - Project remaining capital calls by quarter/year for each existing fund

2. **Model distribution expectations**
   - Apply strategy-appropriate distribution curves to each fund based on age and current DPI
   - Adjust for market environment — compressed exit markets warrant haircuts to near-term distribution projections
   - Separate recycled capital from true distributions where fund terms permit recycling

3. **Build net cash flow projection**
   - Aggregate projected capital calls and distributions across the portfolio by period
   - Calculate net cash flow position (distributions minus calls) per period
   - Identify peak unfunded exposure and years of maximum net cash outflow

4. **Layer in prospective commitments**
   - Add candidate fund commitments at expected closing dates
   - Apply deployment curves for new funds and recalculate aggregate cash flows
   - Test whether new commitments push unfunded ratios or allocation percentages beyond policy bands

5. **Project NAV trajectory**
   - Use contributions, distributions, and assumed growth rates to project NAV by period
   - Calculate projected allocation as a percentage of total portfolio AUM (apply assumed public equity growth to denominator)
   - Flag periods where allocation breaches upper or lower policy bands

6. **Run scenarios and stress tests**
   - **Accelerated drawdown**: GPs call capital 30-50% faster than baseline — test liquidity adequacy
   - **Distribution drought**: Distributions delayed 12-18 months — assess cash reserve sufficiency
   - **Denominator shock**: Public equity drawdown of 20-30% — measure allocation overshoot
   - **Commitment acceleration**: What if the LP adds 1-2 additional commitments beyond plan?

7. **Derive pacing recommendation**
   - Calculate annual commitment budget that keeps allocation within target bands across scenarios
   - Recommend commitment cadence (number and size of funds per year) by strategy
   - Identify vintage year gaps or concentration risks in the existing portfolio

## Output

- **Commitment pacing schedule**: Year-by-year recommended commitment amounts by strategy, with cumulative totals
- **Net cash flow projection**: Periodic (quarterly or annual) table showing projected calls, distributions, and net position
- **NAV and allocation forecast**: Projected NAV trajectory and allocation percentage against target bands, with denominator sensitivity
- **Scenario comparison table**: Side-by-side view of base case, accelerated drawdown, distribution drought, and denominator shock outcomes
- **Key risk flags**: Periods of peak negative cash flow, allocation band breaches, vintage concentration, or liquidity shortfalls
- **Assumption register**: Explicit listing of all deployment curves, distribution assumptions, growth rates, and their sources

## Quality Checks

- Verify that unfunded commitment totals reconcile to GP capital account statements or the LP's portfolio management system
- Confirm deployment curve assumptions reflect actual GP call behavior — compare projected vs. historical call patterns for seasoned funds [VERIFY with GP quarterly reports]
- Ensure distribution assumptions distinguish between return of capital and gains, as tax treatment and reinvestment decisions differ
- Check that denominator assumptions for public portfolio growth are internally consistent with the LP's broader asset allocation model
- Validate that over-commitment ratios remain within investment policy statement limits across all scenarios, not just the base case
- Confirm that the pacing model accounts for follow-on fund commitments to existing GP relationships, not just new relationships
- Flag any fund where the GP has discretion to extend the investment period or fund term, as this shifts call/distribution timing [VERIFY fund LPA terms]
