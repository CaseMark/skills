---
name: analyzing-corporate-restructuring
language: en
description: Evaluates restructuring alternatives with debt-for-equity analysis, 363 sale considerations, and recovery analysis. Use when analyzing restructurings, evaluating Chapter 11 options, or modeling recovery scenarios.
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
# Analyzing Corporate Restructuring

Evaluates restructuring alternatives with debt-for-equity analysis, 363 sale considerations, and recovery analysis.

## When To Use

- Analyzing a distressed company's restructuring options (out-of-court workout vs. Chapter 11 vs. Chapter 7)
- Modeling recovery waterfalls for secured and unsecured creditors
- Evaluating debt-for-equity conversion proposals or exchange offers
- Assessing viability of a Section 363 asset sale vs. plan of reorganization
- Comparing standalone restructuring value to M&A or liquidation alternatives
- Advising creditor committees, DIP lenders, or equity sponsors on restructuring positions

## Inputs To Gather

- **Capital structure**: Full debt schedule with maturities, interest rates, covenants, lien priorities, and intercreditor terms
- **Financial statements**: Trailing 3-year income statements, balance sheets, and cash flow statements
- **Projections**: Management case and independent-case operating forecasts (revenue, EBITDA, capex, working capital)
- **Valuation data**: Comparable company multiples, precedent transactions, and DCF assumptions
- **Claim register**: List of all claims by class, amounts, and priority (administrative, secured, priority unsecured, general unsecured, equity)
- **DIP financing terms**: Facility size, pricing, milestones, carve-outs, and roll-up provisions (if applicable)
- **Key contracts**: Critical executory contracts, unexpired leases, and assumption/rejection analysis
- **Market context**: Industry conditions, asset marketability, and potential buyer universe for 363 sale scenarios

## Workflow

1. **Assess liquidity position** — Build a 13-week cash flow model to determine runway, identify near-term liquidity gaps, and size DIP financing needs. Flag any imminent covenant breaches or maturity walls.

2. **Map the capital structure and claims** — Organize all obligations by seniority: first-lien secured → second-lien secured → mezzanine → unsecured → subordinated → equity. Identify the fulcrum security (the class where value breaks). Note any cross-default, cross-collateralization, or makewhole provisions.

3. **Build the recovery waterfall** — Model enterprise value under low/base/high scenarios. Allocate value top-down through the priority stack. Calculate recovery rates (cents on the dollar) for each claim class. Show the fulcrum security shift across scenarios.

4. **Evaluate restructuring alternatives**:
   - **Out-of-court workout**: Feasible if fewer creditor classes, limited holdout risk, and no need for 363 protections. Model consent thresholds and timeline.
   - **Prepackaged/pre-negotiated Chapter 11**: Appropriate when major creditor support exists but court confirmation is needed for cramdown or contract rejection. Estimate plan confirmation timeline (typically 60–120 days for prepack).
   - **Free-fall Chapter 11**: Required when creditor negotiations stall or significant operational restructuring (lease rejections, workforce reduction) is needed. Model professional fees, DIP costs, and extended timeline risk.
   - **Section 363 sale**: Preferred when going-concern value is maximized through a competitive auction process, stalking horse bid exists, or speed is critical to preserve value. Analyze bid protections (break-up fees, expense reimbursement, overbid increments).
   - **Chapter 7 liquidation**: Benchmark floor value; model orderly vs. forced liquidation values for all asset categories.

5. **Perform debt-for-equity analysis** — For reorganization scenarios, model the pro forma capital structure: new equity allocation to converting creditors, new money investors, and management incentive plan (MIP, typically 10–15% of equity). Calculate implied valuation at various exit multiples and the resulting return to each class.

6. **Compare alternatives on key metrics** — Summarize each path by: estimated total enterprise value, recovery by claim class, timeline to emergence/closing, execution risk, tax implications (COD income, NOL preservation under Section 382 [VERIFY]), and stakeholder alignment.

7. **Stress-test assumptions** — Sensitize outputs to EBITDA margin, exit multiple, discount rate, and timeline delays. Identify breakpoints where the recommended path changes.

## Output

- **Executive summary**: Recommended restructuring path with rationale and key risks
- **Capital structure overview**: Current vs. pro forma debt and equity composition
- **Recovery waterfall table**: Claim class, amount, priority, recovery % under each scenario (low/base/high)
- **Fulcrum security analysis**: Identification of the value-break class with sensitivity ranges
- **Alternative comparison matrix**: Side-by-side evaluation of out-of-court, prepack, free-fall, 363 sale, and liquidation on value, timeline, cost, and risk dimensions
- **Pro forma capitalization**: Post-emergence balance sheet showing new debt, equity ownership, and implied valuation
- **Key assumptions and sensitivities**: Clearly stated inputs with tornado or data-table sensitivity outputs

## Quality Checks

- Confirm the recovery waterfall sums correctly — total distributed value must equal enterprise value less administrative/professional costs
- Verify claim priorities against actual credit agreements and intercreditor terms, not assumed seniority [VERIFY]
- Ensure DIP financing assumptions reflect market-standard terms for the company's size and sector [VERIFY]
- Check that Section 382 NOL limitation analysis uses the correct long-term tax-exempt rate and ownership change thresholds [VERIFY]
- Validate that 363 sale timeline assumptions account for required notice periods, auction procedures, and court scheduling [VERIFY]
- Confirm professional fee estimates are benchmarked to comparable cases by size and complexity
- Cross-check exit multiples against current trading comparables and recent restructuring precedents
- Flag any scenario where administrative claims consume more than 10–15% of estate value as a viability concern
- Ensure all projected financial statements tie (balance sheet balances, cash flow reconciles to change in cash)
