---
name: analyzing-deal-financing-alternatives
description: Compares financing alternatives including debt, equity, convertibles, and hybrid instruments for transactions. Use when evaluating financing options, comparing capital structure alternatives, or optimizing deal funding.
tags:
  - analysis
  - investment-banking
metadata:
  author: casemark
  practice_areas:
    - Investment Banking
    - Mergers and Acquisitions
    - Corporate Finance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Deal Financing Alternatives

## When To Use

- Evaluating how to fund an M&A transaction, leveraged buyout, or recapitalization
- Comparing debt vs. equity vs. hybrid instruments for a specific deal
- Advising a board or sponsor on optimal capital structure for a proposed transaction
- Stress-testing financing scenarios under different operating assumptions
- Assessing refinancing alternatives for existing capital structures

## Inputs To Gather

- **Deal parameters**: Transaction size, enterprise value, target EBITDA/revenue, expected synergies, and closing timeline
- **Target financials**: Historical and projected income statement, balance sheet, and cash flow (minimum 3 years historical, 5 years projected)
- **Existing capital structure**: Outstanding debt instruments, maturities, covenants, change-of-control provisions, and prepayment penalties
- **Credit profile**: Current and pro forma leverage ratios, credit ratings (actual or estimated), interest coverage, and fixed charge coverage
- **Market conditions**: Current benchmark rates (SOFR, UST curve), recent comparable debt and equity issuances, credit spread environment
- **Sponsor/issuer constraints**: Maximum acceptable leverage, minimum equity ownership, dividend/distribution requirements, rating targets, covenant flexibility needs
- **Tax considerations**: Marginal tax rate, interest deductibility limits (Section 163(j) or equivalent), and jurisdiction-specific rules [VERIFY]

## Workflow

1. **Define the financing need** — Confirm total capital required, uses of proceeds (acquisition price, refinancing, fees, working capital), and any mandatory components (e.g., rollover equity, assumed debt).

2. **Map the instrument universe** — Identify all viable financing instruments for the deal:
   - **Senior secured debt**: Term Loan A/B, revolving credit facility, asset-based lending
   - **Unsecured/subordinated debt**: Senior unsecured notes, mezzanine, second lien
   - **Equity instruments**: Common equity, preferred equity, rollover equity
   - **Hybrid/convertible**: Convertible notes, convertible preferred, PIK toggles, HoldCo PIK
   - **Other**: Seller notes, earnouts with financing characteristics, vendor financing

3. **Build a sources & uses framework** — For each financing alternative (typically 2–4 scenarios), construct a complete sources & uses table. Ensure sources equal uses in every scenario.

4. **Quantify cost of capital for each instrument**:
   - All-in cost of debt (coupon/spread + OID amortization + upfront fees)
   - Cost of equity (implied by comparable company multiples, DCF-derived, or sponsor target IRR)
   - Blended WACC for each scenario
   - Account for tax shield value of deductible interest [VERIFY: confirm 163(j) limitation applies and at what threshold]

5. **Analyze pro forma credit metrics** for each scenario:
   - Total Debt / EBITDA, Senior Debt / EBITDA, Net Debt / EBITDA
   - Interest coverage (EBITDA / Interest), fixed charge coverage
   - Debt paydown trajectory over the projection period
   - Covenant headroom under base and downside cases

6. **Stress-test under downside scenarios** — Apply revenue and EBITDA haircuts (typically –10%, –20%, –30%) and assess:
   - Covenant compliance or breach points
   - Cash flow breakeven and liquidity runway
   - Ability to service mandatory amortization and maturities

7. **Evaluate non-financial factors**:
   - Execution certainty and timeline (committed financing vs. market flex)
   - Governance and control implications (equity dilution, board seats, consent rights)
   - Flexibility for future transactions (restricted payments, additional debt capacity, call protection)
   - Refinancing risk (maturity profile, floating vs. fixed rate exposure)

8. **Score and rank alternatives** — Use a structured comparison matrix weighting: cost of capital, execution risk, covenant flexibility, dilution, and strategic optionality. Clearly state weighting rationale.

## Output

Deliver a financing alternatives analysis memo containing:

- **Executive summary**: Recommended financing structure with 2–3 sentence rationale
- **Sources & uses table**: For each scenario, with clear labeling
- **Side-by-side comparison matrix**: Key metrics across all scenarios (WACC, leverage, coverage, dilution, covenant headroom)
- **Pro forma capitalization table**: Showing each instrument, amount, rate, maturity, and key terms
- **Sensitivity tables**: Credit metrics under base, upside, and downside cases
- **Risk/trade-off discussion**: Concise narrative on execution risk, market risk, and structural considerations for each alternative
- **Recommendation**: Preferred structure with supporting logic and identified risks

## Quality Checks

- Sources equal uses in every scenario — no unexplained gaps
- All-in cost calculations include OID, fees, and floor adjustments, not just stated coupons
- Pro forma leverage and coverage ratios tie to the projected financial model
- Covenant headroom is tested under both base and downside, not base case only
- Dilution calculations reflect fully diluted share counts including convertible instruments and warrants
- Tax shield assumptions are consistent with applicable interest deductibility rules [VERIFY]
- Market data (spreads, rates, comps) references a specific date and source
- No instrument is dismissed without a stated reason; no alternative is recommended without quantitative support
