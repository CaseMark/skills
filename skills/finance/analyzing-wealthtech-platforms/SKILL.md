---
name: analyzing-wealthtech-platforms
language: en
description: Evaluates wealth management technology with robo-advisory models, digital planning, and fee analysis. Use when analyzing wealthtech, evaluating robo-advisors, or assessing digital wealth platforms.
tags:
  - analysis
  - financial-technology
metadata:
  author: casemark
  practice_areas:
    - Fintech
    - Payments
    - Digital Banking
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Wealthtech Platforms

Evaluates wealth management technology platforms across robo-advisory capabilities, digital financial planning tools, fee structures, and regulatory compliance posture to produce actionable investment-technology assessments.

## When To Use

- Evaluating a robo-advisor or digital wealth platform for adoption, partnership, or competitive benchmarking
- Comparing multiple wealthtech solutions across advisory models, fee schedules, and feature sets
- Assessing a platform's suitability for a specific client segment (retail, HNW, institutional)
- Reviewing technology stack, API integrations, and custodial architecture of a digital wealth offering
- Analyzing fee transparency, revenue model, and total cost of ownership for end investors

## Inputs To Gather

- **Platform identifiers**: Name, parent company, founding year, AUM (if public), target client segment
- **Advisory model details**: Algorithm-driven allocation methodology, human-advisor overlay availability, hybrid model structure
- **Fee schedule**: Management fees, fund expense ratios, trading costs, account minimums, tiered pricing breakpoints
- **Product & feature set**: Account types supported (taxable, IRA, 401k, trust), tax-loss harvesting, direct indexing, ESG screening, goal-based planning tools, cash management
- **Technology architecture**: Custodian(s), rebalancing engine, API/open-banking integrations, mobile/web capabilities, data security certifications (SOC 2, ISO 27001)
- **Regulatory status**: SEC/FINRA registration, fiduciary standard, state-level requirements [VERIFY jurisdiction-specific registration obligations]
- **Performance data**: Historical returns by model portfolio (if disclosed), benchmark comparisons, risk-adjusted metrics (Sharpe, Sortino)
- **Competitive context**: Direct competitors, market positioning, differentiators claimed vs. substantiated

## Workflow

1. **Define scope** — Confirm whether the analysis covers a single platform deep-dive, a head-to-head comparison, or a market landscape scan. Identify the intended audience (investor, advisor, institutional buyer, regulator).

2. **Catalog the advisory model** — Document the portfolio construction methodology: MPT-based optimization, Black-Litterman, risk-parity, or proprietary algorithm. Note whether the platform acts as a registered investment adviser (RIA) or operates under a broker-dealer model. Flag whether fiduciary duty applies. [VERIFY SEC/state RIA registration status]

3. **Decompose the fee structure** — Break total investor cost into layers:
   - Platform management fee (basis points on AUM)
   - Underlying fund expense ratios (weighted average)
   - Trading/transaction costs, spread costs
   - Account maintenance, transfer, or closure fees
   - Premium tier or human-advisor surcharges
   - Calculate an all-in blended cost for a representative portfolio size ($10K, $100K, $1M).

4. **Evaluate feature depth** — Score capabilities against a standard checklist:
   - Tax optimization (tax-loss harvesting frequency, direct indexing threshold, asset location across account types)
   - Financial planning tools (goal tracking, Monte Carlo projections, retirement income modeling)
   - Cash management (sweep rates, FDIC coverage structure, linked checking/savings)
   - ESG/SRI integration (screening methodology, third-party ratings used, greenwashing risk)
   - Reporting and client experience (performance attribution, consolidated view, mobile UX quality)

5. **Assess technology and custody** — Identify the custodian(s), evaluate rebalancing trigger logic (threshold-based, calendar-based, cash-flow-based), and review API ecosystem for advisor or institutional integrations. Note data security posture and regulatory technology (regtech) capabilities.

6. **Benchmark against competitors** — Position the platform on key dimensions: cost, feature breadth, minimum investment, target demographic, and performance track record. Use a standardized comparison matrix.

7. **Identify risks and limitations** — Flag concentration risk in underlying funds, conflicts of interest (proprietary fund usage, payment for order flow), regulatory gaps, and technology vendor dependencies.

8. **Synthesize findings** — Produce the analysis report with a clear recommendation framework or scoring summary.

## Output

The deliverable is a structured **Wealthtech Platform Analysis Report** containing:

- **Executive summary**: Platform positioning, key strengths, primary concerns, overall assessment
- **Advisory model overview**: Methodology, fiduciary status, human-advisor availability
- **Fee analysis table**: Layered cost breakdown with all-in blended rate at multiple AUM tiers
- **Feature scorecard**: Rated capability matrix across tax optimization, planning, cash management, ESG, and UX
- **Technology & custody profile**: Architecture summary, custodian details, security certifications
- **Competitive positioning matrix**: Side-by-side comparison on cost, features, minimums, and target segment
- **Risk flags**: Conflicts of interest, regulatory considerations, technology dependencies
- **Recommendation or rating**: Suitability assessment for the defined use case, with conditions or caveats

## Quality Checks

- All fee figures are sourced from current published schedules or ADV Part 2A filings — mark outdated or unverifiable figures with [VERIFY]
- Fiduciary status and registration claims are cross-referenced against SEC IAPD or FINRA BrokerCheck [VERIFY registration details]
- Performance claims use net-of-fee returns with stated benchmarks and time periods; gross-of-fee figures are flagged
- Comparison matrices use identical metrics and time periods across all platforms evaluated
- Conflicts of interest (proprietary funds, revenue sharing, PFOF) are explicitly disclosed in the analysis
- Regulatory obligations are noted as jurisdiction-dependent where applicable [VERIFY state-level RIA requirements, non-US regulatory regimes]
- AUM and market data carry a stated "as of" date; stale data beyond 90 days is flagged
