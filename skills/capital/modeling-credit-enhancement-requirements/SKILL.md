---
name: modeling-credit-enhancement-requirements
language: en
description: Calculates required credit enhancement levels with loss modeling, attachment/detachment points, and rating agency methodology. Use when sizing credit enhancement, modeling loss scenarios, or determining tranche subordination.
tags:
  - modeling
  - structured-finance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Credit Enhancement Requirements

## When To Use

- Sizing subordination levels for new ABS, MBS, or CLO issuances
- Determining attachment and detachment points for rated tranches
- Stress-testing existing credit enhancement against revised loss assumptions
- Responding to rating agency feedback on proposed capital structures
- Evaluating whether overcollateralization, excess spread, or reserve accounts provide sufficient protection at target rating levels

## Inputs To Gather

- **Collateral pool data**: loan-level tape with balances, rates, LTVs, FICOs, seasoning, geographic concentration, and obligor industry (CLO)
- **Historical performance**: static pool loss curves, delinquency roll rates, prepayment speeds, recovery rates and recovery lag by vintage
- **Target rating levels**: desired ratings per tranche (e.g., AAA/Aaa senior, BBB/Baa2 mezz)
- **Rating agency methodology**: applicable criteria document and version (e.g., S&P LEVELS model for RMBS, Moody's CDOROM for CLO, Fitch multiples approach for ABS) [VERIFY methodology version is current]
- **Deal structural features**: waterfall priority, interest/principal payment mechanics, triggers (OC tests, delinquency triggers), turbo provisions, liquidity facilities
- **Market benchmarks**: comparable deal credit enhancement levels by asset class and rating tier

## Workflow

1. **Analyze the collateral pool**
   - Stratify the pool by key risk drivers (LTV bands, FICO buckets, geographic/industry concentration)
   - Compute weighted-average collateral characteristics
   - Identify tail-risk concentrations (single obligor, single geography, vintage clustering)

2. **Build the base-case loss model**
   - Select loss methodology: frequency × severity, loss curve extrapolation, or transition-matrix approach depending on asset class
   - Calibrate default frequency using historical static pool data; apply seasoning and vintage adjustments
   - Set loss severity assumptions using historical recovery data, haircut for liquidation lag and costs
   - For CLO: model using Monte Carlo simulation with correlated default (asset correlation by industry pair)
   - For RMBS: apply loan-level loss model with HPI stress overlays [VERIFY applicable HPI stress scenarios per agency]

3. **Determine stressed loss scenarios by rating level**
   - Apply rating-agency-specific stress multiples to base-case losses (e.g., Fitch AAAsf typically 4–5× base case for prime auto ABS) [VERIFY current multiples per asset class]
   - For S&P LEVELS-based analysis: run the LEVELS model to produce break-even loss levels per rating category
   - For Moody's: compute expected loss and Moody's idealized loss rate mapping to target rating
   - Layer in timing stress: front-loaded vs. back-loaded loss curves and their impact on excess spread availability

4. **Size credit enhancement components**
   - **Subordination**: set attachment point for each tranche so that stressed cumulative losses at target rating do not breach the tranche
   - **Overcollateralization (OC)**: size initial OC and OC floor; model OC build-up from excess spread over time
   - **Excess spread**: project net WAC minus cost of funds minus servicing fees; stress for rising defaults and prepayments reducing gross WAC
   - **Reserve account**: size funded reserve (typically 0.25%–1.0% of initial pool balance); determine draw and replenishment mechanics
   - **External enhancement**: size any LOC, surety bond, or guaranty if applicable; note counterparty rating dependency [VERIFY counterparty minimum rating requirements]

5. **Set attachment and detachment points**
   - Map total required credit enhancement to tranche subordination percentages
   - Confirm each tranche detachment point equals the next senior tranche attachment point (no gaps)
   - Validate that the equity/first-loss piece absorbs expected losses plus a margin before impacting rated notes

6. **Run sensitivity and stress analysis**
   - Vary default rate (±25%, ±50%), severity (±10 pp), prepayment speed (0.5× to 2× base CPR/CDR), and recovery lag
   - Test trigger breaches: at what loss level do OC or IC triggers divert cash from junior to senior tranches
   - Run break-even analysis: determine the maximum cumulative default rate each tranche survives at par
   - For CLO: test WARF migration, CCC bucket concentration, and par erosion scenarios

7. **Document and present**
   - Summarize base-case and stressed loss assumptions with sources
   - Present credit enhancement waterfall showing each component's contribution
   - Include tranche-level break-even table and sensitivity matrix
   - Flag any areas where enhancement levels are tight relative to comparable deals

## Output

- **Credit enhancement summary table**: tranche name, rating, attachment %, detachment %, total CE %, CE composition (subordination + OC + excess spread + reserve)
- **Loss model outputs**: base-case cumulative loss, stressed losses by rating tier, loss timing curves
- **Sensitivity matrix**: tranche survival under varied default, severity, prepayment, and recovery assumptions
- **Break-even analysis**: maximum default rate each tranche absorbs before principal impairment
- **Structural waterfall diagram**: priority of payments with trigger levels annotated
- **Comparables benchmarking**: CE levels vs. recent comparable issuances

## Quality Checks

- Confirm attachment/detachment points are contiguous and sum correctly to 100% of the capital structure
- Verify that AAA/Aaa CE exceeds the stressed loss at the corresponding rating level with adequate cushion
- Cross-check CE levels against at least 3 comparable recent deals in the same asset class [VERIFY deal comps are within 12 months]
- Validate that excess spread projections account for collateral WAC compression from prepayments and defaults
- Ensure loss model inputs tie to auditable source data (servicer reports, trustee reports, static pool supplements)
- Confirm trigger levels are internally consistent with waterfall mechanics (OC trigger should breach before IC trigger in a stress)
- Review whether the model handles reinvestment period mechanics correctly (CLO) or amortization profiles (ABS/RMBS)
- Flag any credit enhancement level below the minimum observed in comparable rated transactions
