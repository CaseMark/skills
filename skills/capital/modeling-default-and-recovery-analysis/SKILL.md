---
name: modeling-default-and-recovery-analysis
language: en
description: Builds default probability and recovery rate models with industry data, structural analysis, and loss-given-default estimation. Use when modeling credit losses, estimating recovery values, or analyzing default scenarios.
tags:
  - modeling
  - credit-and-institutional-lending
  - credit
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Default And Recovery Analysis

Builds default probability and recovery rate models incorporating structural credit analysis, industry default statistics, and loss-given-default (LGD) estimation for leveraged lending, direct lending, and broad credit market portfolios.

## When To Use

- Underwriting a new leveraged loan or direct lending facility and need to size expected credit losses
- Constructing or updating a portfolio-level reserve model (CECL, IFRS 9, or internal economic capital)
- Stress-testing a credit book under adverse macro scenarios (recession, sector dislocation)
- Evaluating recovery assumptions for a restructuring, workout, or distressed debt investment
- Pricing credit risk on a single-name or portfolio basis for CLO warehousing or syndication

## Inputs To Gather

- **Obligor financials**: Latest and trailing 3-year income statement, balance sheet, cash flow statement; management projections if available
- **Capital structure detail**: Secured/unsecured tranches, lien priority, intercreditor terms, guarantor coverage, collateral descriptions and appraisals
- **Industry default data**: Moody's, S&P, or Fitch trailing default and recovery rate studies for the relevant sector and rating cohort [VERIFY available vintage]
- **Macro scenario parameters**: GDP growth, unemployment, interest rate path, sector-specific stress drivers (e.g., commodity prices for E&P)
- **Collateral valuations**: Appraisals, liquidation analyses, or orderly-sale estimates for tangible and intangible assets
- **Loan documentation**: Credit agreement covenants, waterfall mechanics, cure rights, and any subordination or turnover provisions

## Workflow

1. **Establish default probability (PD) framework**
   - Select methodology: through-the-cycle rating mapping, point-in-time scorecard, or structural (Merton-style) model
   - For rating-mapped PD: assign internal rating, map to agency cohort default rates, adjust for borrower-specific factors (leverage, coverage, liquidity)
   - For scorecard PD: populate financial and qualitative inputs, calibrate to historical default frequency in the relevant portfolio segment
   - For structural PD: estimate asset value and volatility, compute distance-to-default, convert to PD using empirical mapping
   - Document which base data vintage and methodology variant is used [VERIFY agency data vintage year]

2. **Model recovery rates and LGD**
   - Determine recovery approach: discounted collateral liquidation, comparable workout recovery, or statistical LGD model
   - **Collateral-based recovery**: apply haircuts by asset class (A/R 80-85%, inventory 50-70%, equipment 40-60%, real estate 60-75%, IP/intangibles 0-30%) [VERIFY haircuts against lender's internal policy]
   - **Workout-based recovery**: reference industry recovery rate studies segmented by seniority (first lien secured ~65-80%, second lien ~30-50%, unsecured ~20-40%) [VERIFY against current agency data]
   - Layer in administrative costs (legal, advisory, trustee fees — typically 3-8% of claim) and time-value discount (recovery period assumption 12-24 months for senior secured, 18-36 months for junior)
   - Compute LGD = 1 − Recovery Rate for each tranche

3. **Calculate expected and unexpected loss**
   - Expected Loss (EL) = PD × LGD × Exposure at Default (EAD)
   - For revolving facilities, estimate EAD using credit conversion factors on undrawn commitments (typically 50-75% drawdown at default) [VERIFY against internal or regulatory CCF]
   - Aggregate EL across tranches and obligors for portfolio-level reserve estimation
   - Compute unexpected loss at target confidence interval (99.5% or 99.9%) using single-factor Vasicek or Monte Carlo portfolio simulation for economic capital purposes

4. **Run stress and sensitivity scenarios**
   - Base case, downside (mild recession), and severe stress (deep recession / sector collapse)
   - Vary key inputs: PD multiplier (1.5x–3x base), recovery rate haircut (−10 to −25 pp), correlation assumption (+5 to +15 pp)
   - Test covenant trip scenarios: model EBITDA decline needed to breach financial maintenance covenants and trigger default
   - Capture non-linear effects (e.g., recovery cliff if enterprise value drops below senior secured claims)

5. **Compile model output and documentation**
   - Summary table: PD, LGD, EL, and stress-case loss for each tranche
   - Sensitivity tornado chart showing which inputs most affect loss estimates
   - Methodology narrative covering model choice rationale, data sources, and key judgment calls
   - Limitations disclosure: data gaps, model assumptions that may not hold, sectors or structures outside calibration range

## Output

- **Default probability schedule**: Point-in-time and cumulative PD by year (1Y, 3Y, 5Y, life-of-loan)
- **Recovery waterfall**: Collateral-by-collateral or tranche-by-tranche recovery with haircuts, costs, and net recovery rate
- **LGD and EL summary**: Per-tranche and total facility expected loss in dollars and basis points
- **Stress scenario matrix**: Loss outcomes across base, downside, and severe cases
- **Assumption register**: Every material assumption flagged with source, rationale, and [VERIFY] tag where jurisdiction- or policy-dependent

## Quality Checks

- PD estimates cross-referenced against at least one external benchmark (agency transition matrix, market-implied default probability from CDS spreads if available)
- Recovery assumptions validated against empirical studies for matching seniority, sector, and jurisdiction [VERIFY governing law — US vs. UK vs. other restructuring regimes affect recovery timing and magnitude]
- EL as percentage of commitment tested for reasonableness against historical portfolio loss experience
- Stress PDs do not exceed 100%; recovery rates do not go negative; loss outputs are monotonically ordered across stress severity
- All hard-coded inputs clearly labeled and separated from calculated cells; no circular references without iterative solve documentation
- Model reviewed for consistency between PD horizon, recovery timing, and discount rate assumptions
