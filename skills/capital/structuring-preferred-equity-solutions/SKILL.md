---
name: structuring-preferred-equity-solutions
language: en
description: Designs NAV-based and structured preferred equity facilities with overcollateralization, coverage tests, and waterfall mechanics. Use when structuring preferred equity, analyzing NAV lending, or evaluating fund-level leverage.
tags:
  - secondaries-and-gp-led
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Preferred Equity Solutions

## When To Use

- Designing a NAV-based preferred equity facility for a fund, continuation vehicle, or LP portfolio
- Evaluating whether preferred equity or NAV lending better fits a fund's leverage constraints and LPA covenants
- Structuring overcollateralization ratios, coverage tests, and borrowing base mechanics for a preferred equity tranche
- Modeling distribution waterfalls that layer preferred equity ahead of common/residual equity
- Advising GPs on fund-level leverage in GP-led secondary transactions or strip sales
- Analyzing existing preferred equity terms for refinancing, upsizing, or restructuring

## Inputs To Gather

- **Fund/Vehicle Details**: Fund vintage, strategy (buyout, growth, infrastructure, credit), remaining term, NAV as of latest reporting date, number and type of underlying portfolio companies or assets
- **Capital Structure**: Existing debt (subscription lines, NAV facilities, asset-level leverage), unfunded commitments, total committed capital, drawn capital, recycling provisions
- **LPA Constraints**: Maximum fund-level leverage ratio, restrictions on structural subordination, LP consent thresholds, key-person or removal triggers that affect facility continuity
- **Preferred Equity Parameters**: Target preferred equity size (absolute and as % of NAV), target preferred return (coupon/PIK split), maturity or expected duration, call protection periods, make-whole provisions
- **Portfolio Data**: Individual asset NAVs, MOIC and IRR by asset, sector/geography concentration, liquidity profile (expected exit timeline per asset), any impaired or written-down positions
- **Coverage & Collateral Targets**: Desired overcollateralization ratio (e.g., 1.5x–2.5x), loan-to-value ceiling, interest coverage ratio floor, concentration limits (single-asset cap, sector cap)
- **Waterfall Preferences**: Priority of payments (management fees, preferred return, return of preferred capital, GP catch-up, carried interest, residual distributions), whether preferred is participating or non-participating post-return-of-capital

## Workflow

1. **Assess Structural Fit**
   - Compare preferred equity vs. NAV loan: tax treatment, lien considerations, LPA leverage definition scope, impact on fund-level IRR and MOIC reporting
   - Determine whether preferred equity sits at the fund level, a blocker vehicle, or an aggregator SPV
   - Identify whether the instrument is true preferred equity (no creditor remedies) or hybrid (with secured-creditor-like step-in rights) [VERIFY: jurisdiction-specific recharacterization risk]

2. **Build the Borrowing Base / Collateral Pool**
   - Assign eligibility criteria for portfolio assets (e.g., exclude assets below a NAV threshold, exclude assets in litigation, cap single-asset inclusion at 20–25% of pool)
   - Apply advance rates by asset type: performing buyout assets 50–70%, growth/venture 30–50%, real assets 60–75% [VERIFY: adjust advance rates to current market conditions and lender requirements]
   - Calculate initial overcollateralization ratio: Eligible Asset NAV ÷ Preferred Equity Outstanding

3. **Define Coverage Tests & Triggers**
   - **OC Test**: Minimum overcollateralization ratio (typically 1.3x–2.0x); breach triggers a cure period, then cash sweep or forced deleveraging
   - **Interest Coverage Test**: Distributable cash flow ÷ preferred return payments ≥ threshold (e.g., 1.5x)
   - **Concentration Test**: No single asset > X% of collateral pool; no single sector > Y%
   - **NAV Decline Trigger**: If aggregate NAV declines by more than Z% from closing NAV, mandatory prepayment or additional equity contribution required
   - Specify cure mechanics: cash cure, additional collateral pledge, or GP equity injection; define cure period (typically 30–90 days)

4. **Structure the Distribution Waterfall**
   - Tier 1: Operating expenses, management fees, fund-level taxes
   - Tier 2: Preferred return accrual (current-pay cash coupon plus PIK component if applicable)
   - Tier 3: Return of preferred equity capital (with any accrued/unpaid preferred return)
   - Tier 4: GP catch-up to target carried interest percentage
   - Tier 5: Residual split (common equity / LP distributions per LPA terms)
   - Model scenarios: base case, upside (early exits at premium), downside (20–30% NAV decline), and stress (50%+ NAV decline with concentrated losses)

5. **Analyze Fund-Level Impact**
   - Calculate pro forma fund IRR and MOIC with and without preferred equity leverage
   - Quantify breakeven: at what portfolio return does preferred equity become accretive vs. dilutive to common equity holders
   - Assess J-curve impact: does preferred equity accelerate early distributions or deepen the J-curve due to preferred return drag
   - Model GP economics: effect on carried interest waterfall, management fee base, and GP commitment returns

6. **Draft Term Summary**
   - Produce a structured term sheet or summary memo covering: issuer/vehicle, preferred equity size, preferred return rate and payment terms, maturity, call protection, OC and coverage covenants, waterfall, reporting obligations, governance/consent rights, and transfer restrictions

## Output

- **Preferred Equity Structure Memo**: Executive summary of recommended structure, rationale for key terms, and comparison to alternatives (NAV loan, subscription line upsizing)
- **Borrowing Base Schedule**: Table of eligible assets with individual and aggregate advance rates, resulting OC ratio
- **Coverage Test Dashboard**: Summary of each covenant test at closing and under modeled scenarios
- **Waterfall Model Summary**: Distribution waterfall across base, upside, and stress scenarios showing returns to preferred and common equity
- **Fund Impact Analysis**: Side-by-side IRR/MOIC comparison (levered vs. unlevered), breakeven analysis, and GP economics impact

## Quality Checks

- Confirm OC ratio calculations tie to the borrowing base schedule and use consistent NAV figures (same reporting date)
- Verify waterfall mechanics correctly prioritize preferred return and return of capital before any GP catch-up or carried interest
- Ensure coverage test thresholds are market-appropriate for the fund strategy and vintage [VERIFY: benchmark against comparable recent transactions]
- Check that LPA leverage limits are respected when preferred equity is included in the leverage definition [VERIFY: confirm whether the specific LPA treats preferred equity as leverage]
- Validate that concentration limits in the collateral pool are internally consistent (individual caps sum to allow at least 100% portfolio inclusion)
- Stress-test the structure under a severe NAV decline scenario (40–50% drop) and confirm the waterfall and cure mechanics function as intended
- Flag any recharacterization risk where preferred equity could be treated as debt for tax or regulatory purposes [VERIFY: consult tax counsel for jurisdiction-specific analysis]
