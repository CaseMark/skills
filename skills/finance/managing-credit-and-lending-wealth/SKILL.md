---
name: managing-credit-and-lending-wealth
language: en
description: Structures wealth-based lending analysis with securities-backed, real estate, and art lending evaluation. Use when evaluating wealth lending, analyzing pledge portfolios, or structuring high-net-worth credit.
tags:
  - management
  - wealth-management
  - portfolio
  - credit
metadata:
  author: casemark
  practice_areas:
    - Wealth Management
    - Private Banking
    - Financial Planning
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Credit And Lending Wealth

Structures wealth-based lending analysis with securities-backed, real estate, and art lending evaluation.

## When To Use

- Evaluating a securities-backed lending (SBL) facility against a client's investment portfolio
- Structuring or reviewing a real estate credit line secured by residential or commercial holdings
- Analyzing art-backed or specialty-asset lending proposals
- Comparing credit facilities across private banks for a high-net-worth or ultra-high-net-worth client
- Assessing overall leverage exposure across a client's total balance sheet
- Reviewing covenant compliance or margin call triggers on existing pledge arrangements

## Inputs To Gather

- **Client profile**: Net worth tier, liquidity needs, income sources, tax residency, risk tolerance
- **Portfolio data**: Holdings by asset class (equities, fixed income, alternatives, real estate, collectibles), custodian details, concentration levels
- **Existing credit facilities**: Lender, facility type, outstanding balance, rate structure, maturity, covenants, cross-collateralization terms
- **Proposed facility terms**: Loan-to-value (LTV) ratios offered, advance rates by collateral type, rate benchmarks (SOFR spread, prime), draw period, amortization schedule
- **Collateral documentation**: Appraisals (real estate, art), UCC filings, pledge agreements, custodial control agreements
- **Purpose of borrowing**: Liquidity bridge, asset acquisition, tax planning, estate planning, concentration management

## Workflow

1. **Map the collateral universe**
   - Categorize pledgeable assets: marginable securities, restricted/control stock, real estate equity, art/collectibles, private fund interests
   - Note assets excluded from borrowing base (e.g., illiquid alternatives, below-threshold positions)
   - Flag concentration risk — single-stock positions above 10% of portfolio require separate advance-rate treatment [VERIFY: lender-specific thresholds vary]

2. **Calculate borrowing capacity**
   - Apply lender advance rates by asset class (typical ranges: 50-95% for investment-grade bonds, 50-70% for diversified equities, 40-60% for real estate, 0-50% for art) [VERIFY: rates are lender- and market-dependent]
   - Compute aggregate borrowing base across all eligible collateral
   - Stress-test borrowing base under a 20-30% portfolio decline to identify margin call exposure

3. **Evaluate facility structure and terms**
   - Compare interest rate structures: floating (SOFR + spread) vs. fixed-rate tranches
   - Review commitment vs. uncommitted facilities — committed lines provide certainty but carry unused-line fees
   - Assess covenant package: minimum portfolio value, diversification requirements, reporting obligations
   - Identify cross-default and cross-collateralization clauses across multiple facilities

4. **Analyze risk and downside scenarios**
   - Model margin maintenance triggers: at what portfolio decline does a margin call occur?
   - Evaluate forced-liquidation risk and its tax consequences (especially for concentrated or low-basis positions)
   - Consider interest rate sensitivity on floating-rate facilities
   - Review Regulation U and Regulation T implications for purpose vs. non-purpose loans [VERIFY: applies to U.S.-based lending; other jurisdictions have separate margin regulations]

5. **Assess strategic fit**
   - Compare cost of borrowing vs. cost of liquidating (capital gains tax, loss of upside, portfolio disruption)
   - Evaluate whether leverage aligns with estate planning objectives (e.g., borrowing against assets rather than selling to defer step-up in basis)
   - Consider coordination with existing lines — avoid over-leveraging the same collateral pool
   - Review interest deductibility under current tax rules [VERIFY: IRC Section 163(j) and investment interest limitations]

6. **Compile recommendations**
   - Summarize optimal facility structure, recommended lender(s), and collateral allocation
   - Present side-by-side comparison if evaluating multiple lender proposals
   - Outline action items: documentation required, timeline, approval steps

## Output

Produce a **Credit & Lending Analysis Report** containing:

- **Executive summary**: Recommended facility structure, total borrowing capacity, and key risks in 3-5 sentences
- **Collateral schedule**: Table of pledgeable assets with asset class, market value, advance rate, and borrowing base contribution
- **Facility comparison matrix** (if multiple proposals): Rate, LTV, commitment type, fees, covenants side-by-side
- **Stress-test results**: Borrowing base under baseline, moderate stress (-20%), and severe stress (-40%) scenarios with margin call trigger points
- **Risk register**: Concentration risk, margin call exposure, tax consequences of forced liquidation, interest rate sensitivity
- **Recommendations and next steps**: Facility selection rationale, documentation checklist, estimated timeline to close

## Quality Checks

- Advance rates used match the specific lender's current schedule — do not default to generic industry averages without noting the source
- Borrowing base math is internally consistent (sum of individual asset contributions equals stated total)
- Stress-test assumptions are clearly stated and realistic (use actual historical drawdown data where available)
- Tax implications of forced liquidation are flagged, including estimated capital gains exposure on low-basis positions
- All jurisdiction- or lender-dependent figures are marked with [VERIFY]
- Cross-collateralization and cross-default risks are identified if the client has multiple facilities
- Report distinguishes between purpose loans (subject to margin regulation) and non-purpose loans
- Recommendations align with the client's stated liquidity needs and risk tolerance — do not recommend maximum leverage by default
