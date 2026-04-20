---
name: preparing-venture-exit-analyses
language: en
description: Evaluates exit scenarios including IPO, M&A, secondary sale, and recapitalization with timing and return analysis. Use when planning exits, comparing exit routes, or modeling exit outcomes for portfolio companies.
tags:
  - preparation
  - venture-capital
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Preparation Document
  skill_modes:
    - Preparation
---
# Preparing Venture Exit Analyses

Evaluates exit scenarios — IPO, strategic M&A, secondary sale, and recapitalization — with timing, return multiples, and stakeholder impact analysis for venture-backed portfolio companies.

## When To Use

- Fund is approaching end-of-life and GP must evaluate liquidity paths for remaining portfolio
- Portfolio company hits inflection point (revenue milestone, market shift, inbound acquisition interest)
- LP requests updated exit outlook or MOIC/IRR projections for specific holdings
- Comparing strategic sale vs. IPO readiness vs. continuation fund or secondary transaction
- Board-level discussion on exit timing and route selection

## Inputs To Gather

- **Cap table**: Current ownership breakdown including all preferred series, common, options/warrants, SAFEs, and convertible notes with conversion terms
- **Liquidation preferences**: Participating vs. non-participating, caps, seniority/pari passu stacking order
- **Financial data**: Trailing 12-month revenue, EBITDA/burn, growth rate, gross margin, net retention (for SaaS)
- **Comparable transactions**: Recent M&A deals and IPO valuations in the company's sector and stage
- **Fund parameters**: Fund vintage, remaining term, carry structure, GP commitment, current MOIC/IRR across the fund
- **Company-specific factors**: IP portfolio, key customer concentration, regulatory exposure, management team retention risk
- **Market conditions**: Current IPO window status, sector M&A appetite, interest rate environment, public comp multiples

## Workflow

1. **Build the waterfall model**
   - Map the full cap table with all preference stacks and conversion triggers
   - Model liquidation waterfall at multiple exit valuations (e.g., 0.5x, 1x, 2x, 4x, 8x current post-money)
   - Calculate per-share proceeds for each stakeholder class at each valuation tier
   - Identify conversion break-even points where preferred holders benefit from converting to common

2. **Model each exit scenario**
   - **IPO**: Estimate offering price range using public comps, apply typical IPO discount (15-25%), model lock-up period impact, underwriter fees (6-7%), and secondary offering timeline. Assess S-1 readiness (audited financials, SOX compliance, board composition) [VERIFY: current IPO window and SEC processing times]
   - **Strategic M&A**: Identify likely acquirer categories (strategic vs. financial), model purchase price using relevant multiples (EV/Revenue, EV/EBITDA), account for earnout structures, escrow holdbacks (typically 10-15%), and rep & warranty insurance. Factor in deal timeline (3-6 months typical)
   - **Secondary sale**: Model GP-led secondary, LP-led secondary, or direct secondary at current fair market value with typical discounts (5-20% depending on liquidity and information access). Consider continuation fund structure if applicable
   - **Recapitalization**: Model dividend recap or structured recap scenarios, assess debt capacity, and calculate impact on remaining equity upside

3. **Calculate return metrics for each scenario**
   - Gross and net MOIC for the fund's position in each exit path
   - Gross and net IRR (time-weighted, accounting for entry date and projected exit date)
   - DPI contribution to overall fund returns
   - Sensitivity analysis: show returns across a valuation range (+/- 30% from base case)

4. **Assess timing and execution risk**
   - Rank scenarios by probability-weighted expected return
   - Map execution requirements and timeline for each path (e.g., IPO = 6-12 months prep, M&A = 3-6 months)
   - Identify key risks: market window, management alignment, regulatory approvals, buyer financing contingencies
   - Flag drag-along / tag-along rights or consent thresholds that affect execution [VERIFY: governing documents and shareholder agreement provisions]

5. **Prepare the comparative analysis**
   - Side-by-side comparison table: exit route, valuation range, net proceeds to fund, MOIC, IRR, timeline, probability, key risks
   - Recommendation with supporting rationale tied to fund lifecycle and LP expectations
   - Sensitivity matrix showing how returns change with valuation and timing shifts

## Output

The exit analysis document should contain:

- **Executive summary**: Recommended exit path with headline return metrics and timeline
- **Cap table and waterfall**: Visual waterfall showing proceeds distribution at target valuation for each scenario
- **Scenario detail sheets**: One section per exit route with valuation methodology, return calculations, execution steps, and risk factors
- **Comparative matrix**: Side-by-side table with all scenarios ranked by probability-weighted return
- **Sensitivity analysis**: Grid showing MOIC/IRR across valuation and timing assumptions
- **Action items**: Concrete next steps to advance the recommended exit path (e.g., engage banker, begin S-1 drafting, solicit IOIs)

## Quality Checks

- Waterfall math reconciles — total proceeds distributed equals total exit value minus fees/expenses at every tier
- Liquidation preferences are correctly stacked and participation caps are properly modeled
- IRR calculations use actual investment dates, not approximations
- Comparable transactions are recent (within 18 months), relevant by sector/stage, and sourced from verifiable databases [VERIFY: comp data currency]
- All tax implications flagged but not computed (QSBS eligibility, long-term vs. short-term gains, state-level considerations noted for specialist review) [VERIFY: current QSBS thresholds and holding period requirements]
- Anti-dilution provisions and option pool impacts are reflected in share counts
- Management carve-out or retention bonus assumptions are stated explicitly if included in M&A scenarios
- Document clearly labels base case vs. upside vs. downside assumptions throughout
