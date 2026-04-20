---
name: conducting-collateral-pool-analysis
language: en
description: Assesses underlying asset pools with stratification, concentration analysis, historical performance, and credit quality distribution. Use when analyzing collateral pools, stratifying asset characteristics, or evaluating pool quality.
tags:
  - process
  - structured-finance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Collateral Pool Analysis

## When To Use

- Evaluating an asset pool backing a new securitization (ABS, RMBS, CMBS, CLO, or bespoke structured notes)
- Performing periodic surveillance on an existing deal's collateral
- Comparing multiple pool cuts during warehouse accumulation or ramp-up
- Assessing eligibility criteria compliance for a proposed asset addition or substitution
- Supporting rating agency presentations, investor due diligence, or regulatory examinations

## Inputs To Gather

- **Pool tape / loan-level data file** — the asset-by-asset schedule with fields such as obligor, balance, rate, maturity, origination date, geography, industry/property type, credit score or rating, LTV/DSCR, delinquency status
- **Eligibility criteria and concentration limits** from the indenture, pooling & servicing agreement, or warehouse facility terms
- **Historical performance data** — static pool loss curves, delinquency rolls, prepayment speeds, recovery rates for comparable vintages
- **Deal structure details** — target pool size, overcollateralization levels, advance rates, and any reinvestment or replenishment provisions
- **Third-party reports** (if available) — appraisals, BPOs, credit reports, servicer commentary

## Workflow

1. **Validate the pool tape**
   - Confirm record count, total balance, and field completeness against summary statistics provided by the originator
   - Identify and flag missing, stale, or inconsistent data (e.g., maturity dates before origination dates, negative balances, duplicate loan IDs)
   - Reconcile the tape to any prior cut date if performing a delta analysis

2. **Stratify the pool across key dimensions**
   - For each asset class, stratify by the material risk drivers:
     - *Consumer ABS*: FICO band, original term, seasoning, geographic state, loan-to-value
     - *RMBS*: LTV, DTI, documentation type, occupancy status, property type, origination channel
     - *CMBS*: property type, DSCR bucket, LTV, geographic MSA, lease rollover year
     - *CLO*: Moody's/S&P industry code, rating bucket, spread, maturity, first-lien vs. second-lien
   - Present stratification tables showing count, aggregate balance, weighted-average coupon/spread, and percentage of pool for each bucket

3. **Assess concentration risk**
   - Calculate single-obligor, top-5, and top-10 obligor concentrations by outstanding balance
   - Evaluate geographic concentration (state, MSA, or country depending on asset class)
   - Check industry or property-type concentration against deal limits
   - Flag any breach or near-breach of indenture concentration limits [VERIFY against deal documents]

4. **Analyze credit quality distribution**
   - Map credit scores, internal ratings, or external ratings to a standardized scale
   - Compute weighted-average credit quality metrics (WA FICO, WA rating factor, WA DSCR)
   - Identify tail-risk exposures — bottom decile by credit quality — and quantify their share of the pool
   - Compare current distribution to the pool as of the closing date to detect migration

5. **Review historical performance benchmarks**
   - Overlay the pool's vintage against static pool loss curves from comparable originator cohorts
   - Analyze delinquency transition matrices (current → 30 → 60 → 90 → charge-off roll rates)
   - Calculate cumulative default rate, cumulative loss rate, and loss severity to date
   - Evaluate prepayment behavior (CPR, CDR, ABS) relative to pricing assumptions
   - Note any performance divergence from base-case or rating-agency stress scenarios

6. **Test eligibility and portfolio quality tests**
   - Re-run each eligibility criterion from the governing documents against every asset in the tape
   - Identify any ineligible assets and quantify their balance
   - Run portfolio-level quality tests (e.g., WA spread test, diversity score, WA recovery rate test for CLOs; WA LTV and WA DSCR for CMBS) [VERIFY specific tests per deal]
   - Document pass/fail status and available cushion for each test

7. **Synthesize findings into a pool quality opinion**
   - Summarize strengths (e.g., high WA FICO, geographic diversification, seasoned performance)
   - Highlight weaknesses and risk concentrations with quantified exposure
   - Compare the pool to prior deal vintages or market benchmarks
   - Recommend any remedial actions (asset substitution, concentration limit waiver requests, structural credit enhancement adjustments)

## Output

Produce a structured collateral pool analysis report containing:

- **Executive summary** — one-paragraph pool quality assessment with key metrics (pool balance, asset count, WA coupon, WA credit metric, WA remaining term, top concentration)
- **Stratification tables** — formatted tables for each key dimension with count, balance, WA stats, and pool share
- **Concentration analysis** — obligor, geographic, and sector/property-type heat maps or ranked tables with limit compliance status
- **Credit quality snapshot** — distribution chart or table with migration commentary
- **Performance benchmarking** — vintage curve comparisons and roll-rate summaries
- **Eligibility and portfolio test results** — pass/fail matrix with cushion amounts
- **Risk flags and recommendations** — itemized list of concerns ranked by materiality

## Quality Checks

- All balances in stratification tables sum to the total pool balance (zero reconciliation difference)
- Weighted-average calculations are balance-weighted, not simple averages
- Concentration percentages sum to 100% within each stratification dimension
- Every eligibility criterion from the deal documents is tested — none omitted [VERIFY completeness against indenture/PSA]
- Historical performance comparisons use matched seasoning periods (not mismatched time windows)
- Any data gaps or assumptions are explicitly noted with [VERIFY] markers
- Currency, day-count, and rate conventions are consistent across all calculations
- Output distinguishes between hard breaches (ineligibility) and soft breaches (portfolio test failures with cure periods)
