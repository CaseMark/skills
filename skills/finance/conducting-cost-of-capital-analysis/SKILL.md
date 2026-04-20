---
name: conducting-cost-of-capital-analysis
language: en
description: Calculates WACC components with equity risk premium, beta estimation, and debt cost measurement. Use when calculating cost of capital, estimating WACC, or analyzing discount rates.
tags:
  - process
  - corporate-finance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Corporate Finance
    - Treasury
    - Financial Planning
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Cost Of Capital Analysis

Calculates WACC components with equity risk premium, beta estimation, and debt cost measurement.

## When To Use

- Setting a discount rate for DCF valuations or capital budgeting decisions
- Evaluating whether a project or acquisition clears the firm's required return
- Benchmarking divisional hurdle rates against the corporate WACC
- Preparing investor presentations or board materials that require a transparent cost-of-capital build-up
- Reassessing WACC after a material change in capital structure, credit rating, or market conditions

## Inputs To Gather

- **Capital structure**: Current market-value weights of equity, debt, preferred stock, and any hybrid instruments (convertibles, mezzanine)
- **Equity inputs**: Current share price, shares outstanding, selected risk-free rate, equity risk premium (ERP) source and vintage, raw/adjusted beta, and any size or company-specific risk premium
- **Debt inputs**: Outstanding debt instruments with coupon/yield, credit spread, and weighted-average maturity; marginal corporate tax rate [VERIFY — tax rate varies by jurisdiction and entity type]
- **Preferred stock inputs**: Dividend rate, par value, and current market price (if applicable)
- **Peer/comparable data**: Comparable-company betas (levered and unlevered), capital structures, and credit profiles for cross-check
- **Purpose context**: Valuation date, reporting currency, and whether the rate will be applied to nominal vs. real cash flows

## Workflow

1. **Determine capital structure weights**
   - Use market values, not book values, for equity and debt
   - For private companies, estimate equity value iteratively or use comparable-company structures
   - Include all interest-bearing obligations; exclude operating liabilities (accounts payable, accrued expenses)

2. **Estimate cost of equity (Ke)**
   - Select a risk-free rate matched to the cash-flow duration (typically 10-year or 20-year government bond yield) [VERIFY — currency and sovereign bond selection]
   - Choose an ERP source (Duff & Phelps/Kroll, Damodaran, Bloomberg) and document the vintage year
   - Estimate beta:
     - Gather 2–5 year weekly or monthly returns for comparable public companies
     - Unlever each peer beta using Hamada or Harris-Pringle formula
     - Take the median unlevered beta and relever to the subject company's target capital structure
   - Apply size premium and company-specific risk premium where justified (document rationale)
   - Ke = Risk-Free Rate + (Beta x ERP) + Size Premium + Company-Specific Premium

3. **Estimate cost of debt (Kd)**
   - Use the yield-to-maturity on existing traded debt, or the synthetic rating approach (credit spread over risk-free rate) if debt is not publicly traded
   - Weight each tranche by market value
   - After-tax Kd = Weighted-average pre-tax cost of debt x (1 − marginal tax rate)

4. **Estimate cost of preferred stock (Kp)** (if applicable)
   - Kp = Annual preferred dividend / Current market price of preferred

5. **Calculate WACC**
   - WACC = (We x Ke) + (Wd x Kd after-tax) + (Wp x Kp)
   - Round to the nearest 25 basis points for presentation unless precision is required

6. **Sensitivity and cross-checks**
   - Run a sensitivity table varying beta (±0.10–0.20) and ERP (±50–100 bps)
   - Compare result to industry WACC benchmarks and implied cost of capital from market multiples
   - If the WACC seems outside a reasonable range for the industry, revisit assumptions before finalizing

## Output

- **WACC summary table**: Each component (Ke, Kd, Kp), its weight, and the blended WACC
- **Detailed build-up schedule**: Risk-free rate, ERP, beta derivation, size/specific premia, debt cost derivation
- **Assumptions register**: Every input assumption listed with its source and date
- **Sensitivity matrix**: WACC under alternative beta and ERP scenarios
- **Narrative summary** (2–3 paragraphs): Explain the key drivers, any unusual adjustments, and how the rate compares to prior periods or peers

## Quality Checks

- Market-value weights sum to 100%
- Beta is derived from comparable companies and relevered — not simply pulled from a single data provider without adjustment
- Risk-free rate currency matches the cash-flow currency
- ERP source and vintage are explicitly cited; do not mix ERP sources across analyses
- After-tax cost of debt does not exceed cost of equity (flag if it does — likely a data error or distressed-credit situation)
- Sensitivity range is wide enough to capture plausible scenarios but not so wide as to be unhelpful
- All jurisdiction-dependent inputs (tax rate, sovereign bond choice, regulatory capital requirements) are marked [VERIFY]
- Final WACC is sanity-checked against published industry cost-of-capital data (e.g., Kroll Cost of Capital Navigator, Damodaran sector data)
