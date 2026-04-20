---
name: structuring-revolving-credit-facilities
language: en
description: Designs revolver structures with commitment amounts, borrowing base mechanics, letter of credit sub-facilities, and pricing grids. Use when structuring revolvers, designing borrowing bases, or analyzing liquidity facilities.
tags:
  - debt-capital-markets
  - credit
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Revolving Credit Facilities

## When To Use

- Structuring a new revolving credit facility for an investment-grade or leveraged borrower
- Designing or recalibrating a borrowing base for asset-based lending (ABL) revolvers
- Adding or sizing letter of credit (LC) sub-facilities and swingline sub-limits
- Building pricing grids tied to leverage ratios, credit ratings, or borrowing base utilization
- Evaluating an existing revolver for refinancing, upsizing, or covenant amendment

## Inputs To Gather

- **Borrower profile**: Industry, credit rating (if any), capital structure, and historical financial statements (minimum 3 years of income statement, balance sheet, cash flow)
- **Liquidity needs**: Seasonal working capital swings, peak-to-trough cash usage, capex cadence, and acquisition pipeline
- **Collateral data** (for ABL structures): Accounts receivable aging schedule, inventory breakdown by category, eligible vs. ineligible asset detail, appraisal reports
- **Existing debt**: Outstanding term loans, bonds, other revolving facilities, intercreditor arrangements
- **LC requirements**: Standby vs. commercial LC needs, typical tenor, historical draw frequency, beneficiary requirements
- **Target terms**: Desired commitment size, maturity, accordion feature size, currency of borrowing, multi-tranche considerations
- **Market context**: Comparable recent revolver transactions, current SOFR/base rate levels, and agent bank feedback [VERIFY current benchmark rate conventions in the relevant market]

## Workflow

1. **Assess liquidity requirement**
   - Model the borrower's monthly or weekly cash flow to identify peak borrowing need
   - Add a liquidity buffer (typically 15–25% above peak need) to set the target commitment amount
   - Determine whether a single-tranche or multi-tranche structure best fits (e.g., separate domestic and multicurrency tranches)

2. **Select facility type and borrowing base mechanics**
   - For investment-grade borrowers: unsecured revolver with leverage-based pricing grid
   - For leveraged/sub-investment-grade borrowers: secured revolver, often with borrowing base
   - For ABL revolvers, define eligible collateral categories and advance rates:
     - Eligible receivables: typically 80–85% advance rate [VERIFY standard advance rates for borrower's industry]
     - Eligible inventory: typically 50–70% for finished goods, lower for raw materials/WIP
     - Set concentration limits, dilution reserves, and availability blocks
   - Specify borrowing base certificate delivery frequency (monthly, bi-weekly, or triggered by utilization threshold)

3. **Size sub-facilities**
   - **LC sub-facility**: Size based on historical and projected LC issuance; typically 10–30% of total commitment
   - **Swingline sub-limit**: Size for same-day funding needs; typically 5–15% of total commitment
   - Confirm that sub-facility limits nest within the aggregate commitment (not additive)

4. **Build the pricing grid**
   - Investment-grade revolvers: grid steps typically keyed to S&P/Moody's corporate rating or total leverage ratio
   - Leveraged revolvers: grid typically keyed to first lien net leverage or total net leverage ratio
   - Define applicable margin (SOFR spread), commitment fee on undrawn amounts, LC participation fee, and fronting fee
   - Typical grid has 4–6 pricing levels with 12.5–25 bps steps between levels
   - Specify step-up pricing for utilization exceeding defined thresholds (e.g., >50% utilization adds 12.5 bps)

5. **Define key structural terms**
   - Maturity: typically 5 years for investment-grade; 5 years (with springing maturity 91 days ahead of any term loan maturity) for leveraged
   - Accordion / incremental facility capacity: define cap (fixed dollar amount, percentage of EBITDA, or ratio-based)
   - Springing financial covenant: specify trigger (e.g., revolver utilization >35% triggers a maximum leverage test) [VERIFY market-standard springing thresholds for the credit tier]
   - Mandatory prepayment and commitment reduction triggers
   - Cash dominion / account control provisions for ABL structures

6. **Prepare the structuring memo**
   - Consolidate all sizing, pricing, and structural decisions into a single deliverable
   - Include sensitivity tables showing availability under stress scenarios (e.g., 10–20% collateral value decline for ABL)
   - Benchmark against 3–5 comparable transactions with commitment size, pricing, and covenant data

## Output

The deliverable is a **Revolver Structuring Report** containing:

- **Executive summary**: Recommended commitment amount, facility type, and key economic terms
- **Liquidity analysis**: Cash flow model supporting the commitment size with peak/trough utilization projections
- **Borrowing base schedule** (if ABL): Eligible collateral, advance rates, reserves, and calculated availability
- **Sub-facility sizing**: LC sub-limit and swingline sub-limit with supporting rationale
- **Pricing grid**: Full margin grid with applicable rate benchmark, commitment fee schedule, and LC fee structure
- **Structural term sheet**: Maturity, accordion mechanics, financial covenants, springing triggers, and mandatory prepayment terms
- **Comparable transactions table**: Benchmarking data from recent market deals
- **Stress / sensitivity analysis**: Availability and covenant headroom under downside scenarios

## Quality Checks

- Commitment amount is supported by documented cash flow analysis, not round-number estimation
- Borrowing base advance rates and reserves are consistent with the borrower's industry and collateral quality
- Pricing grid levels are internally consistent (no inversions) and benchmarked against comparable deals
- Sub-facility limits are nested correctly within the total commitment
- Springing covenant triggers and financial maintenance tests are specified with exact thresholds
- All jurisdiction-dependent assumptions (benchmark rate, regulatory capital treatment, withholding tax) are marked [VERIFY]
- Accordion and incremental capacity caps are defined with both a dollar amount and a ratio-based incurrence test
- Stress scenarios test at least a moderate downside (e.g., 15–20% revenue decline) and a severe downside case
