---
name: analyzing-health-insurance-plans
description: Evaluates health insurance plan structures with actuarial value, network analysis, and cost projection. Use when analyzing health plans, comparing coverage, or projecting healthcare costs.
tags:
  - analysis
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Health Insurance Plans

## When To Use

- Comparing multiple health insurance plan options (employer group, individual market, or Medicare Advantage)
- Evaluating actuarial value and metal-tier classification accuracy
- Projecting out-of-pocket costs under different utilization scenarios
- Assessing network adequacy for a specific population or geographic area
- Reviewing plan design changes for renewal or repricing cycles
- Analyzing reinsurance attachment points and stop-loss adequacy relative to plan exposure

## Inputs To Gather

- **Plan documents**: Summary of Benefits and Coverage (SBC), Schedule of Benefits, Certificate of Coverage, Evidence of Coverage
- **Rate filings**: Premium rates by tier (single, employee+spouse, family), age-banding tables if applicable
- **Network data**: Provider directory or network ID, in-network vs. out-of-network reimbursement schedules, any tiered or narrow network designations
- **Claims history** (if available): Aggregate paid claims, large-claimant data, utilization rates by service category
- **Census data**: Member demographics, enrollment counts by tier, geographic distribution
- **Formulary**: Drug tier structure, prior authorization requirements, specialty drug handling
- **Reinsurance/stop-loss terms**: Specific and aggregate attachment points, lasering exclusions, contract period (paid vs. incurred basis)
- **Comparison context**: Benchmark plans, prior-year plan design, or competing carrier quotes

## Workflow

1. **Classify the plan structure**
   - Identify plan type: HMO, PPO, EPO, POS, HDHP/HSA-eligible, or hybrid
   - Confirm metal tier (Bronze/Silver/Gold/Platinum) or equivalent actuarial value band
   - Note any non-standard design features: reference-based pricing, direct primary care carve-outs, or centers-of-excellence requirements

2. **Calculate actuarial value**
   - Map cost-sharing parameters: deductible, coinsurance, copays, out-of-pocket maximum (OOPM)
   - Apply standard continuance tables or the CMS AV Calculator methodology to estimate the plan's share of total allowed costs [VERIFY: confirm which AV calculator version or methodology is required for the filing year]
   - Flag deviations from de minimis AV ranges for the stated metal tier (±2 percentage points under ACA rules) [VERIFY: state-specific AV requirements may differ]

3. **Analyze network adequacy**
   - Check provider-to-member ratios for primary care, specialty, and facility categories against applicable state or CMS standards [VERIFY: network adequacy standards vary by state and market segment]
   - Identify geographic access gaps using drive-time/distance thresholds
   - Assess out-of-network exposure: balance billing protections, surprise billing act applicability, reference pricing methodology

4. **Project member cost exposure**
   - Model total cost of care under low, moderate, and high utilization scenarios
   - Calculate effective member cost share: premiums + expected out-of-pocket spend per scenario
   - Compare across plans using equivalent annual cost metrics (premium + expected OOP at each utilization level)
   - For HDHP plans, factor in HSA/HRA employer contributions and tax-advantage value

5. **Evaluate pharmacy benefits**
   - Map formulary tiers and typical member cost for high-utilization drug categories
   - Identify specialty drug exposure and accumulator/maximizer program impact on OOPM
   - Note step therapy, prior authorization, and quantity limit protocols

6. **Assess risk transfer and reinsurance**
   - Review specific stop-loss attachment points relative to historical large-claimant frequency
   - Evaluate aggregate stop-loss corridor and expected claims variability
   - Flag any lasered members or excluded conditions and quantify retained risk
   - For self-funded plans, assess claims-fund adequacy and IBNR reserves

7. **Compile comparative analysis**
   - Build side-by-side comparison matrix covering: premiums, cost sharing, AV, network breadth, pharmacy, and risk transfer
   - Rank plans on total effective cost, network quality, and financial risk exposure
   - Highlight material trade-offs (e.g., lower premium but narrow network, high deductible offset by HSA funding)

## Output

- **Plan Analysis Summary**: One-page overview with plan classification, AV calculation result, and key cost metrics
- **Cost Projection Table**: Low/moderate/high utilization scenario modeling with annual premium + OOP totals per plan
- **Network Adequacy Assessment**: Provider ratio analysis, geographic access findings, and out-of-network risk notes
- **Pharmacy Benefit Summary**: Formulary tier structure, specialty drug exposure, and accumulator program flags
- **Reinsurance/Stop-Loss Review** (if applicable): Attachment point adequacy, retained risk quantification, and lasering impact
- **Comparative Matrix**: Side-by-side plan ranking with trade-off commentary
- **Flagged Items**: Any data gaps, assumptions made, or items requiring [VERIFY] follow-up

## Quality Checks

- Confirm all cost-sharing parameters (deductible, coinsurance, copay, OOPM) are captured for both in-network and out-of-network tiers
- Verify AV calculations use the correct methodology and plan year assumptions
- Ensure utilization scenarios reflect realistic claims distributions (not just arbitrary multiples)
- Check that premium comparisons use consistent contribution assumptions (gross vs. net of employer subsidy)
- Validate network data is current — provider directories can be 60–90 days stale
- Confirm reinsurance terms match the contract period and claims basis (paid vs. incurred)
- Flag any state-mandated benefit requirements that could affect plan design comparability [VERIFY: essential health benefit benchmark varies by state]
- Mark all jurisdiction-dependent regulatory references with [VERIFY]
