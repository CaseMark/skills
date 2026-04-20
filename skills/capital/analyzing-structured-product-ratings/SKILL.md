---
name: analyzing-structured-product-ratings
language: en
description: Evaluates rating agency methodology application with loss model inputs, correlation assumptions, and tranche-level credit assessment. Use when analyzing structured product ratings, comparing agency methodologies, or assessing rating sensitivity.
tags:
  - analysis
  - structured-finance
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
# Analyzing Structured Product Ratings

Evaluates rating agency methodology application with loss model inputs, correlation assumptions, and tranche-level credit assessment across ABS, MBS, CLO, and other securitized products.

## When To Use

- Reviewing a new-issue presale report or rating letter to understand tranche-level credit support
- Comparing Moody's, S&P, Fitch, or DBRS/Kroll methodologies on the same transaction
- Assessing whether a rating action (upgrade, downgrade, watch placement) is consistent with stated methodology
- Evaluating sensitivity of ratings to changes in default, recovery, or correlation assumptions
- Preparing investment committee memos that incorporate third-party rating analysis
- Reviewing surveillance reports for deteriorating collateral performance vs. original rating assumptions

## Inputs To Gather

- **Rating reports**: Presale/new-issue reports, rating letters, surveillance updates, and methodology publications from each relevant agency
- **Deal documents**: Offering memorandum/circular, waterfall structure, priority of payments, trigger definitions, and reserve fund mechanics
- **Collateral data**: Pool stratification tables (FICO/DSCR/LTV distributions for MBS; industry/rating/recovery for CLOs; obligor concentration for ABS), historical vintage performance data
- **Loss model inputs**: Base-case default rate, default timing curve, recovery rate, recovery lag, prepayment speed (CPR/CDR for MBS; CPR for auto/student loan ABS)
- **Structural features**: Credit enhancement levels (subordination, OC, excess spread), tranche thickness, amortization schedule, reinvestment period (CLOs), step-down triggers
- **Correlation assumptions**: Inter-sector and intra-sector asset correlation matrices, geographic concentration adjustments [VERIFY: agency-specific correlation frameworks differ materially]

## Workflow

1. **Map the capital structure** — Diagram tranche seniority, attachment/detachment points, and credit enhancement (CE) levels. Calculate initial CE as a percentage of the pool balance for each rated tranche.

2. **Identify applicable methodology** — Determine which agency criteria apply. Key frameworks include:
   - Moody's: Idealized expected loss tables, Cdp (correlated default probability), MILAN CE for RMBS, CLO Monitor/WARF for CLOs
   - S&P: CDO Evaluator (Monte Carlo), LEVELS for RMBS, SROC (scenario-based rating on capital) for CLOs under surveillance
   - Fitch: Portfolio Credit Model (PCM), ResiGlobal for RMBS, asset-specific default models
   - DBRS/Kroll: KBRA CLO methodology, DBRS master trust criteria [VERIFY: confirm current methodology version dates]

3. **Analyze loss model inputs** — For each agency:
   - Extract base-case and stressed default/loss assumptions
   - Compare assumed severity/recovery rates against historical realized performance for the asset class
   - Evaluate prepayment and default timing vectors and their impact on excess spread capture
   - Identify whether the agency uses a deterministic scenario ladder or stochastic (Monte Carlo) simulation

4. **Assess correlation and concentration** — Review how each agency models:
   - Asset correlation (flat vs. sector-based matrices)
   - Obligor/geographic/industry concentration penalties
   - Large obligor tests (Moody's Binomial Expansion Technique vs. S&P supplemental tests)
   - Impact of correlation assumptions on tail-risk scenarios at senior vs. mezzanine tranche levels

5. **Evaluate structural protections** — Map agency-specific treatment of:
   - Cash flow waterfall priorities (pre- vs. post-acceleration)
   - OC/IC trigger mechanics and cure provisions
   - Liquidity facilities, reserve funds, and guaranteed investment contracts
   - Counterparty risk (swap provider, servicer, account bank) and replacement triggers [VERIFY: counterparty criteria vary by agency and jurisdiction]

6. **Run sensitivity analysis** — Stress key variables independently and in combination:
   - Default rate: +25%, +50%, +100% of base case
   - Recovery rate: –10pp, –20pp from base assumption
   - Correlation: increase by 5–10pp across sectors
   - Prepayment speed: 0.5x and 2.0x base CPR
   - Document which tranches experience notch changes under each scenario

7. **Compare cross-agency outcomes** — Build a comparison matrix showing:
   - Rating assigned by each agency per tranche
   - Key divergence drivers (e.g., differing recovery assumptions, correlation treatment, or structural credit given for excess spread)
   - Identify split ratings and explain the methodological basis for divergence

## Output

Produce a structured rating analysis report containing:

- **Executive summary**: Transaction overview, agencies involved, rating snapshot, and key findings (1–2 paragraphs)
- **Capital structure table**: Tranche name, size, rating by each agency, CE level, attachment/detachment points
- **Methodology comparison matrix**: Side-by-side comparison of loss assumptions, correlation inputs, structural credit, and stress scenarios per agency
- **Sensitivity grid**: Table showing rating impact of stressed defaults, recoveries, correlations, and prepayments by tranche
- **Key risk factors**: Concentration risks, structural weaknesses, servicer/counterparty dependencies, and triggers approaching breach
- **Split rating commentary**: Explanation of any rating divergences between agencies, with identification of the analytical driver
- **Surveillance flags**: Collateral performance metrics to monitor (delinquency trends, cumulative loss curves vs. original projections, OC/IC test cushion)

## Quality Checks

- Confirm all referenced methodology publications are current versions — agencies frequently update criteria [VERIFY: check publication dates against agency websites]
- Verify that CE calculations match offering document definitions (some deals define CE net of defaulted assets, others gross)
- Cross-check that loss model inputs extracted from presale reports are internally consistent (e.g., default rate × severity = expected loss)
- Ensure sensitivity analysis covers the full rated spectrum — senior tranches may be insensitive to moderate stresses but mezzanine tranches may be highly sensitive
- Confirm that waterfall modeling accounts for all payment dates, not just a single snapshot
- Flag any reliance on manager/servicer discretion (e.g., CLO reinvestment flexibility, workout assumptions) as a qualitative risk factor
- Validate that counterparty rating triggers are consistent with agency counterparty criteria for the relevant jurisdiction
