---
name: analyzing-municipal-bonds
description: Evaluates municipal credit with revenue source analysis, tax considerations, and state/local economic assessment. Use when analyzing municipal bonds, evaluating GO vs revenue bonds, or assessing muni credit.
tags:
  - analysis
  - fixed-income
  - credit
  - tax
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Municipal Bonds

## When To Use

- Evaluating creditworthiness of a general obligation (GO) or revenue bond issuer
- Comparing muni bond offerings across issuers, sectors, or maturities
- Assessing tax-equivalent yield advantage for a specific investor tax bracket
- Reviewing an existing muni position for credit deterioration or upgrade potential
- Analyzing a new issue's official statement (OS) for credit and structural risks

## Inputs To Gather

- **Bond identifiers**: CUSIP, issuer name, series, maturity date, coupon, par amount
- **Bond type**: GO (limited or unlimited tax), revenue (specify pledged source — water/sewer, toll, hospital, airport, tax increment, etc.), conduit, or hybrid
- **Official statement / offering document**: Legal provisions, flow of funds, rate covenant, additional bonds test, debt service reserve fund details
- **Financial statements**: Issuer's CAFR or audited financials (2–3 most recent years)
- **Rating agency reports**: Moody's, S&P, Fitch — current ratings plus any outlook/watch actions
- **Economic and demographic data**: Population trends, employment base, median household income, top taxpayers/employers, assessed valuation history
- **Investor profile** (if computing tax-equivalent yield): Marginal federal rate, state rate, AMT status, state of residence vs. issuer state [VERIFY]

## Workflow

1. **Classify the bond structure**
   - Determine GO vs. revenue; identify the specific pledged revenue stream or taxing authority
   - Note any credit enhancement: bond insurance (AGMC, Assured Guaranty, Build America Mutual), state credit enhancement programs, or letters of credit
   - Flag variable-rate demand obligations (VRDOs), tender option bonds, or other structures that introduce liquidity/remarketing risk

2. **Analyze the revenue/tax base**
   - *GO bonds*: Review assessed valuation trends, tax levy capacity, levy limits [VERIFY state-specific caps — e.g., Prop 13 in CA, PTELL in IL], collection rates, and top-10 taxpayer concentration
   - *Revenue bonds*: Evaluate the pledged revenue history (3–5 years), debt service coverage ratio (DSCR), rate covenant minimum (typically 1.10×–1.25× for utilities), additional bonds test, and flow-of-funds waterfall (gross vs. net pledge)
   - Identify single-source or concentration risk in the revenue stream

3. **Assess issuer financial health**
   - Review general fund balance as a percentage of expenditures (target: ≥15% unrestricted)
   - Check pension and OPEB funded ratios and annual required contributions as a share of the budget [VERIFY — GASB 67/68 and 74/75 reporting standards apply]
   - Evaluate debt burden: debt per capita, debt as % of assessed valuation, overlapping debt from other taxing jurisdictions
   - Note any history of draws on reserves, interfund borrowing, or budget deficits

4. **Evaluate economic and demographic fundamentals**
   - Population growth or decline trajectory
   - Employment diversity — flag dependence on a single employer or industry
   - Median household income relative to state and national benchmarks
   - Infrastructure condition and capital improvement plan adequacy

5. **Compute tax-equivalent yield and relative value**
   - Tax-equivalent yield = muni yield ÷ (1 − marginal tax rate); layer in state tax benefit if applicable [VERIFY — confirm whether the bond is subject to state tax in the investor's state; de minimis rules for secondary market discount bonds]
   - Compare spread to AAA MMD or Refinitiv muni benchmark curve at the relevant maturity point
   - Assess muni/Treasury ratio in context of historical range for the credit tier and maturity

6. **Review legal and structural provisions**
   - Call features: optional, mandatory sinking fund, extraordinary (e.g., catastrophe or eminent domain)
   - Bankruptcy eligibility: municipalities may file Chapter 9 in states that authorize it [VERIFY — only about half of US states authorize Chapter 9 filing]
   - Security pledge enforceability and any legislative risk to the pledged source

## Output

Produce a **Municipal Bond Credit Analysis** containing:

- **Summary**: Issuer, bond type, par amount, coupon, maturity, rating(s), and one-paragraph credit opinion
- **Revenue/Tax Base Assessment**: Key metrics (DSCR, AV trends, collection rates) with 3-year trend table
- **Financial Profile**: Fund balance ratios, pension/OPEB exposure, debt burden metrics
- **Economic Overview**: Population, income, employment data with directional indicators
- **Relative Value**: Tax-equivalent yield, spread to benchmark, muni/Treasury ratio
- **Risk Factors**: Bullet list of material risks (concentration, pension burden, legal constraints, call risk)
- **Recommendation**: Buy / hold / sell or underweight / market-weight / overweight with rationale

## Quality Checks

- All DSCR and coverage calculations tie back to audited revenue and debt service figures — no estimated numbers without [VERIFY] tag
- Tax-equivalent yield computation explicitly states the assumed tax rate(s) and whether AMT applies
- Pension and OPEB figures reference the most recent actuarial valuation date; flag if valuation is more than 2 years old
- Overlapping debt calculation includes all taxing jurisdictions (school districts, special districts, county)
- Rating agency actions within the last 12 months are captured; note any divergence between agencies
- State-specific legal provisions (tax caps, filing authorizations, appropriation risk for lease-backed debt) are marked [VERIFY] where jurisdictional variation exists
