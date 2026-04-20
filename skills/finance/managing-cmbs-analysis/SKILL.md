---
name: managing-cmbs-analysis
language: en
description: Evaluates CMBS structures with loan-level analysis, subordination assessment, and special servicing monitoring. Use when analyzing CMBS deals, reviewing loan pools, or monitoring CMBS performance.
tags:
  - management
  - real-estate-finance
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing CMBS Analysis

Evaluates CMBS structures with loan-level analysis, subordination assessment, and special servicing monitoring.

## When To Use

- Analyzing a new CMBS issuance or secondary market deal for acquisition or surveillance
- Reviewing loan-pool composition, concentration risk, and collateral quality
- Assessing credit enhancement levels and subordination adequacy across tranches
- Monitoring specially serviced loans, watchlist credits, or workout outcomes
- Preparing periodic CMBS portfolio performance reports for investors or asset managers
- Evaluating B-piece or mezzanine tranche risk in conduit, single-borrower, or CRE CLO deals

## Inputs To Gather

- **Deal documents**: Prospectus supplement, pooling and servicing agreement (PSA), offering circular
- **Loan-level data**: Loan tape with property type, location, balance, DLTV, DSCR, maturity date, rate type, and IO period details
- **Tranche structure**: Capital stack showing class designations, credit enhancement percentages, coupon rates, and expected maturities
- **Servicer reports**: Monthly trustee/remittance reports, watchlist reports, specially serviced loan updates
- **Property-level financials**: NOI, occupancy, rent rolls, cap rate comps for top-10 or top-20 loans
- **Rating agency presales**: Moody's, DBRS Morningstar, Fitch, or KBRA presale reports with loss expectations
- **Market data**: CMBX index levels, spread benchmarks, delinquency rate trends by vintage and property type

## Workflow

1. **Map the capital structure**
   - Chart each tranche: class, original/current balance, credit enhancement, coupon, WAL, and rating
   - Identify the credit-risk transfer point (where losses attach) for the target tranche
   - Note any interest-only classes, rake bonds, or companion classes with distinct risk profiles

2. **Analyze the loan pool**
   - Calculate pool-level metrics: weighted-average DSCR, DLTV, coupon, remaining term, and IO percentage
   - Assess concentration risk by property type, geography, single-borrower exposure, and loan size (top-10 loan %)
   - Flag loans with DSCR < 1.20x, DLTV > 70%, near-term maturities (< 24 months), or upcoming IO-to-amortizing transitions
   - Review underwriting assumptions vs. in-place financials — identify aggressive NOI or cap rate inputs [VERIFY]

3. **Evaluate subordination and credit enhancement**
   - Compare credit enhancement levels to rating agency expected loss estimates
   - Stress-test subordination under adverse scenarios (e.g., 20% NOI decline, 150bp cap rate expansion)
   - Benchmark CE levels against comparable vintage deals and current spread pricing
   - Assess whether defeasance, prepayment, or amortization has increased CE since issuance

4. **Monitor special servicing and watchlist**
   - Track loans transferred to special servicing: transfer date, reason, current workout status, appraised value
   - Categorize workout strategies: modification, extension, foreclosure/REO, DPO, or note sale
   - Calculate realized and projected losses on resolved and pending dispositions
   - Review watchlist triggers: declining occupancy, tenant rollover, DSCR deterioration, environmental/structural issues
   - Track cumulative loss rate vs. original deal loss projections and rating agency scenarios

5. **Assess ongoing deal performance**
   - Compare current delinquency rates (30/60/90+/FC/REO) against benchmark indices and prior periods
   - Evaluate cash flow waterfall mechanics: sequential vs. pro-rata pay, trigger events, and reserve fund levels [VERIFY against PSA]
   - Note any appraisal reductions, interest shortfalls (ASER), or principal writedowns affecting target tranches
   - Review servicer advancing obligations and any advancing facility constraints

6. **Synthesize findings and report**
   - Compile tranche-level risk assessment with key metrics dashboard
   - Highlight material risks: concentration, maturity wall, declining collateral quality, servicer performance
   - Provide loss-adjusted yield analysis for target tranches under base and stress scenarios
   - Recommend hold/sell/increase position with supporting rationale

## Output

- **Deal summary table**: Tranche map with current balances, CE levels, ratings, and spreads
- **Loan pool analysis**: Pool composition breakdown with concentration charts and flagged risk loans
- **Special servicing report**: Status of all specially serviced and watchlist loans with loss estimates
- **Performance dashboard**: Delinquency trends, loss rates, and CE migration since issuance
- **Risk assessment narrative**: Material findings, stress scenario outcomes, and actionable recommendations
- **Data gaps log**: Items requiring updated servicer data, property financials, or third-party verification

## Quality Checks

- Confirm all loan-level data ties to the most recent trustee report date — flag stale data older than 60 days
- Verify credit enhancement calculations match trustee factor files, not just prospectus-level originals
- Cross-check DSCR and DLTV figures against both servicer-reported and independently calculated values
- Ensure loss projections account for advancing, liquidation expenses, and special servicing fees
- Validate that waterfall mechanics and trigger tests reflect the governing PSA terms [VERIFY]
- Confirm property type and geographic classifications align with standard CRE taxonomy (office, retail, multifamily, industrial, hospitality, self-storage, mixed-use)
- Flag any discrepancies between rating agency reports and servicer data on the same loans
