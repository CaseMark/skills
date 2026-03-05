---
name: analyzing-mortgage-backed-securities
description: Evaluates MBS structures with prepayment modeling (CPR/CDR), collateral analysis, and tranche-level credit risk assessment. Use when analyzing MBS, modeling prepayment scenarios, or evaluating residential mortgage pools.
tags:
  - analysis
  - structured-finance
  - risk
  - credit
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Mortgage Backed Securities

Evaluates MBS structures with prepayment modeling (CPR/CDR), collateral analysis, and tranche-level credit risk assessment.

## When To Use

- Analyzing agency (Ginnie Mae, Fannie Mae, Freddie Mac) or non-agency RMBS deals
- Modeling prepayment and default scenarios on residential mortgage collateral pools
- Evaluating tranche-level credit enhancement, subordination, and cash flow waterfall mechanics
- Comparing MBS tranches for relative value across spread, WAL, and convexity profiles
- Assessing seasoned pools for re-REMIC structuring or secondary market trading
- Reviewing offering documents, prospectus supplements, or trustee reports for deal-level risk

## Inputs To Gather

- **Deal documents**: Prospectus supplement, pooling and servicing agreement (PSA), trustee reports
- **Collateral tape**: Loan-level data including FICO, LTV, DTI, loan age, geography, occupancy type, documentation level
- **Pool statistics**: Current balance, WAC, WAM, WALA, average loan size, delinquency buckets (30/60/90+), REO pipeline
- **Structure details**: Tranche map (senior/mezzanine/subordinate), credit enhancement levels, OC/XS triggers, step-down dates
- **Prepayment and default assumptions**: Base-case CPR, CDR, loss severity, recovery lag; stress scenarios if applicable
- **Market context**: Current mortgage rates, refi incentive, HPA trends, [VERIFY] agency guarantee status and program eligibility
- **Rating agency criteria**: Applicable S&P, Moody's, Fitch, or DBRS loss/stress frameworks if rating-dependent analysis

## Workflow

1. **Map the deal structure**
   - Identify all tranches: senior (A classes), mezzanine (M classes), subordinate (B classes), IO strips, residual
   - Document the cash flow waterfall: sequential vs. pro-rata pay periods, trigger events (delinquency/loss triggers), clean-up call provisions
   - Record credit enhancement: subordination percentages, overcollateralization targets, excess spread capture mechanisms

2. **Profile the collateral pool**
   - Stratify loans by vintage, FICO band, LTV bucket, geography (state/MSA concentration), loan purpose (purchase/refi/cash-out), and property type
   - Identify adverse selection risks: high LTV concentrations, low-doc loans, investor properties, geographic clustering
   - Calculate weighted-average characteristics and compare against benchmark pools for the same vintage/program

3. **Model prepayment scenarios**
   - Set base-case CPR using historical analogs (e.g., seasoned conventional 30yr at current coupon spread to market)
   - Run sensitivity across CPR vectors: slow (e.g., 6 CPR), base (e.g., 15 CPR), fast (e.g., 35 CPR), and ramp scenarios (PSA multiples)
   - For each scenario, compute WAL, yield, spread to benchmark, and effective duration for each tranche
   - Assess negative convexity exposure on premium-priced tranches and extension risk on discount tranches

4. **Model default and loss scenarios**
   - Set base-case CDR and loss severity using collateral characteristics and historical performance curves
   - Run stress scenarios: 2x CDR, elevated severity (e.g., 40%–60% on non-agency), delayed recovery timelines
   - Determine tranche-level loss absorption: at what CDR/severity combination does each tranche experience principal write-down
   - Evaluate trigger mechanics — will delinquency or cumulative-loss triggers divert cash flow from subordinate tranches

5. **Assess credit enhancement adequacy**
   - Compare current subordination levels to original levels and to rating-agency loss benchmarks
   - Evaluate OC build/release mechanics and whether excess spread is sufficient to maintain targets under stress
   - For seasoned deals, assess whether step-down conditions have been met and whether senior tranches benefit from de-leveraging
   - [VERIFY] Check for any amendments, modifications, or servicer advances that may affect collateral performance

6. **Synthesize relative value and risk conclusions**
   - Rank tranches by spread per unit of WAL risk, credit risk, and convexity exposure
   - Flag tranches with asymmetric risk profiles (e.g., thin mezzanine with cliff risk, IO strips with high prepay sensitivity)
   - Compare to similar deals in the market for relative value context
   - Identify key monitoring triggers: delinquency thresholds, cumulative loss benchmarks, servicer performance metrics

## Output

Produce a structured MBS analysis report containing:

- **Deal overview**: Issuer, shelf program, closing date, original/current balance, servicer(s), trustee
- **Collateral summary**: Pool composition table with stratifications, weighted-average metrics, delinquency and loss performance to date
- **Structure summary**: Tranche map with current balances, coupons, credit enhancement levels, and priority of payments description
- **Prepayment analysis**: Table of WAL, yield, and spread across CPR scenarios for each evaluated tranche
- **Credit analysis**: Loss absorption capacity by tranche, stress-test results, trigger proximity assessment
- **Relative value assessment**: Spread comparison to benchmark deals, convexity-adjusted return analysis
- **Risk flags and monitoring points**: Concentration risks, servicer concerns, trigger events approaching thresholds
- **Appendix**: Key assumptions, data sources, model methodology notes

## Quality Checks

- Verify that all tranche balances sum to total deal balance and that waterfall logic is internally consistent
- Confirm CPR/CDR assumptions are sourced from stated methodology, not arbitrary — cite historical analogs or agency benchmarks
- Ensure loss severity assumptions match collateral type (e.g., non-agency subprime vs. agency conforming have materially different severities)
- Cross-check credit enhancement percentages against trustee reports, not just offering documents, for seasoned deals
- [VERIFY] Rating agency criteria versions used — S&P, Moody's, and Fitch periodically update RMBS loss frameworks
- [VERIFY] Regulatory considerations: risk retention rules (Reg RR), QM/ATR status of underlying loans, Volcker Rule implications for trading book holdings
- Flag any data gaps in the collateral tape (missing FICO, undisclosed LTV) and note their impact on model reliability
- Mark all forward-looking projections as estimates subject to rate, HPA, and macroeconomic assumptions
