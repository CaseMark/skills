---
name: modeling-prepayment-and-default-scenarios
description: Builds CPR/CDR/severity vectors with scenario analysis across interest rate and economic environments. Use when modeling prepayment behavior, projecting default scenarios, or stress testing pool performance.
tags:
  - modeling
  - structured-finance
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
# Modeling Prepayment And Default Scenarios

Builds CPR/CDR/severity vectors with scenario analysis across interest rate and economic environments for ABS, MBS, and CLO pools.

## When To Use

- Projecting cash flows on a securitization tranche under multiple prepayment and default paths
- Stress testing pool performance for rating agency submissions or internal risk review
- Building base/upside/downside vectors for deal pricing or ongoing surveillance
- Evaluating how rate shifts, unemployment changes, or HPA movements alter bond returns
- Comparing model output to agency benchmarks (e.g., Moody's Idealized CDR curves, S&P LEVELS)

## Inputs To Gather

- **Pool tape**: loan-level data including balance, coupon, LTV, FICO/credit score, seasoning, geography, loan purpose, occupancy type
- **Collateral type**: RMBS (agency/non-agency), auto ABS, student loan ABS, CLO, CMBS, or other — each drives model selection
- **Rate environment assumptions**: current benchmark curve (SOFR/Treasury), forward curve, and any shocked curves (+/- 100, 200, 300 bps)
- **Macro scenarios**: baseline, mild stress, severe stress — specify unemployment rate, HPI path, GDP growth as applicable
- **Historical performance data**: prior remittance reports, delinquency rolls, loss/recovery history for the deal or comparable deals
- **Structural features**: lockout periods, prepayment penalties, call provisions, clean-up calls, step-down triggers
- **Target output granularity**: monthly vs. quarterly vectors; single-path vs. matrix of scenarios

## Workflow

1. **Classify collateral and select model framework**
   - RMBS: use PSA-based CPR ramp or econometric prepayment model (turnover + refinance incentive + burnout + seasoning)
   - Auto/consumer ABS: use ABS speed ramp (absolute prepayment speed or monthly payment rate)
   - CLO: model voluntary and involuntary prepayments separately; apply CDR based on rating cohort and industry mix
   - CMBS: apply balloon risk, voluntary defeasance/yield maintenance, and involuntary default vectors
   - [VERIFY] Confirm whether the deal uses single monthly mortality (SMM) or annualized CPR convention

2. **Build CPR vectors**
   - Construct a base-case CPR curve reflecting current rate incentive, seasoning, and borrower characteristics
   - Layer refinance incentive function: map WAC-to-market-rate spread against historical S-curves for the collateral type
   - Apply burnout adjustment: reduce refi sensitivity for pools with extended exposure to in-the-money conditions
   - Apply seasoning ramp: new-origination pools follow a ramp to steady-state CPR (e.g., 30-month PSA ramp for RMBS)
   - Generate shocked vectors: shift rate environment and recalculate incentive-driven CPR for each scenario

3. **Build CDR and severity vectors**
   - Specify baseline CDR curve: use historical roll-rate analysis (current → 30 → 60 → 90 → default) or rating agency benchmarks
   - Apply macro overlays: increase CDR under stress scenarios by mapping unemployment and HPI shocks to default frequency multipliers
   - Set loss severity assumptions by collateral type:
     - RMBS: 30-50% severity typical; vary by LTV band and state foreclosure timeline [VERIFY]
     - Auto ABS: 40-60% severity on defaulted units; adjust for used vs. new, recovery lag
     - CLO: recovery rates by seniority (senior secured ~70%, second lien ~40%, unsecured ~25%) [VERIFY]
   - Construct timing vectors: distribute defaults and recoveries across months with appropriate lag (typically 12-24 months from default to liquidation for RMBS)

4. **Assemble scenario matrix**
   - Define at minimum three scenarios: base, upside (low default / high prepay), downside (high default / low prepay)
   - For each scenario, pair a CPR vector with a CDR vector and a severity assumption
   - Optionally add a rating agency stress case using prescribed vectors (e.g., Fitch Deerfield, Moody's MILAN)
   - Run each scenario through the deal waterfall to produce tranche-level cash flows, WAL, yield, and principal window

5. **Validate and calibrate**
   - Back-test base-case vectors against 6-12 months of actual deal performance (if seasoned)
   - Compare model CPR to market-implied prepayment speeds from TBA or specified pool pricing
   - Check CDR reasonableness against Moody's sector-level default studies or S&P transition matrices
   - Verify that scenario dispersion is wide enough to capture 1-in-25-year and 1-in-100-year stress events for risk purposes

## Output

- **Scenario summary table**: for each scenario, display CPR (annualized), CDR (annualized), loss severity, resulting WAL, yield to maturity, and principal payment window
- **Monthly vector schedules**: time-series of SMM, MDR (monthly default rate), and recovery amounts for each scenario
- **Tranche impact analysis**: show how each tranche (AAA through equity) performs under each scenario — expected loss, credit enhancement erosion, trigger breaches
- **Sensitivity heat map**: matrix showing tranche yield or WAL as a function of CPR (rows) x CDR (columns)
- **Key assumptions log**: document every assumed input — rate curves, macro variables, model parameters, data cutoff date

## Quality Checks

- Confirm CPR vectors are internally consistent: SMM × 12 annualization should reconcile with stated CPR
- Ensure CDR + CPR does not exceed 100% of performing balance in any period
- Verify severity assumptions reflect post-foreclosure costs (legal, REO maintenance, broker fees) not just collateral value haircuts
- Cross-check base-case WAL against Bloomberg or Intex model output for the same deal [VERIFY]
- Confirm that stressed scenarios produce credit enhancement shortfalls at the appropriate rating level
- Flag any input marked [VERIFY] before delivering final output — do not present unconfirmed assumptions as given
- Validate that recovery lag timing is realistic for the jurisdiction and collateral type (judicial vs. non-judicial foreclosure states produce materially different timelines)
