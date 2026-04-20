---
name: managing-credit-portfolio-risk
language: en
description: Structures credit portfolio analysis with concentration metrics, correlation assessment, and stress testing. Use when managing credit portfolios, measuring concentration risk, or stress testing credit exposure.
tags:
  - management
  - fixed-income
  - risk
  - portfolio
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
# Managing Credit Portfolio Risk

Structures credit portfolio analysis with concentration metrics, correlation assessment, and stress testing.

## When To Use

- Evaluating credit concentration risk across issuer, sector, geography, or rating bucket
- Running stress tests on credit portfolios under adverse macro or idiosyncratic scenarios
- Assessing default correlation exposure and tail-risk contributions
- Producing periodic credit risk reports for portfolio managers, risk committees, or compliance
- Rebalancing credit allocations in response to rating migration, spread widening, or limit breaches

## Inputs To Gather

- **Holdings data**: Full position list with par/market value, issuer, CUSIP/ISIN, coupon, maturity, seniority, and currency
- **Credit ratings**: Agency ratings (Moody's, S&P, Fitch) and any internal shadow ratings for each position
- **Sector/industry classification**: GICS, BICS, or internal taxonomy mapping each issuer
- **Spread and yield data**: Current OAS, Z-spread, or asset-swap spread by position
- **Recovery rate assumptions**: Expected recovery by seniority tier (secured, senior unsecured, subordinated) [VERIFY against current market consensus]
- **Portfolio limits and guidelines**: IPS concentration limits by issuer, sector, rating, and duration bucket
- **Macro scenario parameters**: Rate shocks, spread-widening assumptions, GDP contraction levels for stress tests
- **Historical default and transition matrices**: Rating migration probabilities over the relevant horizon [VERIFY source vintage and applicability]

## Workflow

1. **Map the portfolio**
   - Aggregate holdings by issuer, sector, rating bucket, maturity band, and geography
   - Calculate notional and market-value weights for each grouping
   - Identify any single-name exposures exceeding guideline thresholds

2. **Measure concentration risk**
   - Compute Herfindahl-Hirschman Index (HHI) at issuer and sector level
   - Calculate top-N issuer exposure (e.g., top 5, top 10) as percentage of portfolio
   - Flag positions where a single issuer or sector exceeds policy limits
   - Assess geographic and currency concentration where applicable

3. **Evaluate credit quality distribution**
   - Build the rating distribution (IG vs. HY split, granular bucket breakdown)
   - Estimate weighted-average credit quality and compare to benchmark
   - Apply rating transition matrices to project 1-year migration probability and expected downgrade loss
   - Identify issuers on negative watch or outlook that may trigger forced selling [VERIFY against current watchlist data]

4. **Assess default correlation and tail risk**
   - Estimate pairwise and sectoral default correlations using factor models or historical co-movement
   - Run portfolio loss distribution (e.g., CreditMetrics, Gaussian copula, or Monte Carlo simulation)
   - Calculate expected loss (EL), unexpected loss (UL), and credit VaR at defined confidence levels (95th, 99th percentile)
   - Quantify contribution-to-risk by issuer and sector to identify outsized tail-risk contributors

5. **Stress test the portfolio**
   - Define scenarios: baseline, moderate stress, severe stress, and idiosyncratic event (single large-issuer default)
   - For each scenario, apply spread shocks, rating downgrades, and default assumptions
   - Compute stressed portfolio market value, P&L impact, and any limit breaches
   - Test liquidity impact: estimate bid-ask widening and potential liquidation cost under stress

6. **Compile risk report and recommendations**
   - Summarize concentration metrics, credit quality trends, and stress test results in a dashboard format
   - Highlight limit breaches, emerging risks (e.g., rising sector correlation, crowded trades), and watch-list names
   - Propose rebalancing actions: reduce overweight sectors, diversify single-name risk, add hedges (CDS, index protection)
   - State assumptions, model limitations, and data freshness

## Output

The deliverable is a **Credit Portfolio Risk Report** containing:

- **Portfolio snapshot table**: Holdings aggregated by issuer, sector, rating, and maturity with market-value weights
- **Concentration dashboard**: HHI scores, top-N exposure, limit utilization vs. guidelines
- **Credit quality summary**: Rating distribution, weighted-average rating, migration risk assessment
- **Loss distribution metrics**: EL, UL, credit VaR with confidence intervals
- **Stress test results matrix**: P&L impact across defined scenarios with limit-breach flags
- **Action items**: Prioritized list of recommended trades, hedges, or limit-adjustment requests

## Quality Checks

- Confirm holdings data reconciles to official book-of-record totals before running analysis
- Verify that all issuers are mapped to a sector and rating — flag any unmapped positions as data gaps
- Cross-check HHI and top-N calculations against an independent source or prior period for consistency
- Ensure stress scenarios cover both systematic (macro) and idiosyncratic (single-name) events
- Validate that recovery rate and default probability assumptions match current market conditions [VERIFY]
- Confirm all limit thresholds reference the current investment policy statement, not outdated guidelines
- Check that model outputs (VaR, expected loss) are within plausible ranges compared to historical realized losses
- Flag any stale pricing (spreads or ratings older than the reporting date) that could distort results
