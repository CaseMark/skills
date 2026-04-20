---
name: analyzing-secondary-transactions
language: en
description: Evaluates secondary market transactions with NAV assessment, discount/premium analysis, and portfolio evaluation. Use when analyzing secondary deals, pricing LP interests, or evaluating GP-led secondaries.
tags:
  - analysis
  - private-equity
  - portfolio
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Venture Capital
    - Growth Equity
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Secondary Transactions

Evaluates secondary market transactions including LP interest sales, GP-led continuation vehicles, strip sales, and preferred equity secondaries. Covers NAV assessment, discount/premium calibration, portfolio-level evaluation, and deal structuring considerations.

## When To Use

- Pricing an LP interest in a PE/VC/growth equity fund for sale or purchase on the secondary market
- Evaluating a GP-led secondary (single-asset continuation, multi-asset roll-up, tender offer)
- Assessing a portfolio of fund interests for a bulk secondary bid
- Benchmarking a proposed discount or premium against comparable transactions
- Reviewing a secondary fund's pipeline or existing portfolio for valuation reasonableness

## Inputs To Gather

- **Fund information**: Fund name, vintage year, strategy, GP track record, fund size, fund term and remaining life
- **NAV data**: Most recent reported NAV, NAV date, valuation methodology (mark-to-market vs. mark-to-model), audited vs. unaudited status
- **Cash flow history**: Called capital, distributions to date, remaining unfunded commitments, DPI and TVPI as reported
- **Portfolio details**: Underlying company list, sector mix, revenue/EBITDA multiples where available, holding periods, exit pipeline
- **Deal terms**: Proposed price (as % of NAV), deferred consideration or earnout structures, stapled commitment requirements, transfer restrictions or ROFR provisions
- **Market context**: Recent comparable secondary transactions, broker quotes, secondary market volume and pricing trends [VERIFY current market data against recent broker reports such as Greenhill, Jefferies, Lazard]

## Workflow

1. **Validate NAV quality**
   - Determine NAV staleness (months since last reported NAV; adjust if >3 months)
   - Assess valuation methodology rigor — identify any marks based on cost, round-to-round, or third-party appraisals
   - Flag concentrated positions (>20% of NAV in a single asset) as higher-risk marks
   - Check for pending write-downs, known exits since NAV date, or capital calls that shift the reference point

2. **Compute adjusted NAV**
   - Roll forward NAV for known interim events: distributions received, capital called, announced exits or write-downs
   - Apply sector or comparable-company multiple adjustments where public market equivalents have moved materially since the NAV date
   - Produce a base-case adjusted NAV and a stress-case adjusted NAV (e.g., 10–20% haircut on unrealized marks)

3. **Analyze discount/premium**
   - Express the bid price as a percentage of reported NAV and adjusted NAV
   - Benchmark against comparable secondary transactions by vintage, strategy, quartile ranking, and remaining fund life
   - Decompose the discount into components: illiquidity discount, J-curve risk (early vintage), GP quality premium/discount, portfolio concentration risk, unfunded commitment liability
   - For GP-led transactions, evaluate the implied valuation against recent third-party marks and comparable exit multiples

4. **Evaluate portfolio quality**
   - Categorize underlying assets by maturity stage (early, growth, mature, exit-ready)
   - Assess sector diversification and single-name concentration risk
   - Review exit visibility: identify assets with clear near-term exit pathways (IPO pipeline, announced M&A) vs. long-duration holds
   - For VC-heavy portfolios, apply power-law return assumptions and stress-test top holdings

5. **Assess deal structure and terms**
   - Quantify unfunded commitment exposure and expected call schedule — model net cash flow profile
   - Evaluate transfer restrictions: ROFR timelines, LP Advisory Committee consent requirements, GP consent [VERIFY against fund LPA]
   - Analyze stapled commitment provisions (new primary commitment required alongside secondary purchase)
   - For GP-led deals, review alignment terms: GP rollover percentage, management fee reset, carry crystallization

6. **Model returns**
   - Build a base-case, upside, and downside scenario for net IRR and net MOIC from entry price
   - Key assumptions: holding period to full liquidation, distribution pacing, remaining value creation
   - Sensitivity analysis on entry price (discount to NAV) vs. exit multiple vs. hold period
   - Compare projected returns against the buyer's target return hurdle

## Output

Produce a structured analysis report with these sections:

- **Executive Summary**: Deal overview, recommended bid range (as % of NAV), key risk factors, go/no-go recommendation
- **NAV Assessment**: Reported vs. adjusted NAV, quality of marks, staleness adjustment
- **Discount/Premium Analysis**: Proposed pricing vs. benchmarks, discount decomposition
- **Portfolio Review**: Asset-level summary table, concentration metrics, exit pipeline assessment
- **Cash Flow & Return Model**: Projected net IRR and MOIC under base/upside/downside scenarios, sensitivity tables
- **Deal Structure Notes**: Transfer mechanics, unfunded exposure, stapled commitments, key LPA provisions
- **Risk Factors**: Top 3–5 risks with mitigation considerations

## Quality Checks

- Confirmed NAV date and adjusted for interim events — never price off a stale, unadjusted NAV
- Discount benchmarking uses transactions within a comparable vintage, strategy, and time window (ideally trailing 12 months)
- Return model assumptions are internally consistent (e.g., distribution pacing aligns with portfolio maturity)
- Unfunded commitment liability is fully reflected in the total cost basis and return calculations
- All GP consent, ROFR, and transfer restriction provisions are flagged [VERIFY against specific fund LPA terms]
- Stapled commitment terms are modeled as a separate cash outflow, not blended into the secondary pricing
- Assumptions clearly labeled; uncertain data points marked with [VERIFY]
