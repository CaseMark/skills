---
name: managing-loan-underwriting-real-estate
language: en
description: Structures commercial real estate loan underwriting with DSCR, LTV, and debt yield analysis. Use when underwriting CRE loans, calculating coverage ratios, or evaluating loan terms.
tags:
  - management
  - real-estate-finance
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Loan Underwriting Real Estate

Structures commercial real estate loan underwriting with DSCR, LTV, and debt yield analysis for commercial property debt transactions.

## When To Use

- Underwriting a new CRE loan (acquisition, refinance, or construction-to-perm)
- Evaluating loan sizing across multiple coverage metrics (DSCR, LTV, debt yield)
- Comparing term sheet proposals from multiple lenders
- Stress-testing loan structures under varying NOI, cap rate, or interest rate scenarios
- Preparing credit committee or investment committee loan packages
- Assessing REIT-level portfolio leverage and covenant compliance

## Inputs To Gather

- **Property financials**: Trailing-12-month (T-12) operating statements, rent roll with lease expiration schedule, historical occupancy data
- **Appraisal or valuation**: Recent appraisal, broker opinion of value, or internal underwritten value with cap rate basis
- **Loan terms**: Proposed loan amount, interest rate (fixed/floating + spread), amortization period, maturity, IO period if any, prepayment provisions
- **Borrower information**: Sponsor track record, net worth and liquidity, guaranty structure (recourse vs. non-recourse with carve-outs)
- **Market data**: Submarket vacancy, comparable rental rates, recent sales comps for cap rate benchmarking
- **Third-party reports**: Environmental (Phase I/II), property condition report, seismic (if applicable), survey, title [VERIFY: lender-specific report requirements vary]

## Workflow

1. **Build the NOI waterfall**
   - Start from gross potential rent, subtract vacancy/credit loss, add other income
   - Deduct operating expenses line-by-line (management fee, R&M, insurance, taxes, utilities, common area)
   - Arrive at in-place NOI, then build an underwritten NOI adjusting for lease-up, rent bumps, and normalized expenses
   - Clearly label in-place vs. stabilized vs. stressed NOI figures

2. **Calculate core coverage metrics**
   - **DSCR** = Underwritten NOI ÷ Annual Debt Service. Minimum thresholds: 1.20x–1.25x typical for stabilized; 1.30x+ for transitional or single-tenant [VERIFY: lender-specific DSCR floors]
   - **LTV** = Loan Amount ÷ Appraised Value. Senior loans typically capped at 65%–75% [VERIFY: product-specific LTV limits]
   - **Debt Yield** = Underwritten NOI ÷ Loan Amount. Minimum 8%–10% for most CRE lenders; acts as a rate-independent sizing check

3. **Size the loan using the binding constraint**
   - Calculate maximum loan proceeds under each metric independently
   - The binding constraint (lowest proceeds) governs final loan sizing
   - Document which metric is the binding constraint and the gap to the next constraint

4. **Stress test the structure**
   - Interest rate stress: model +100bps and +200bps rate increases on floating-rate loans
   - NOI stress: model 10%–20% NOI decline and recalculate DSCR
   - Cap rate stress: model 50–100bps cap rate expansion and recalculate LTV
   - Identify breakeven occupancy and breakeven rental rate for debt service coverage

5. **Evaluate loan structure and terms**
   - Compare IO period impact on amortizing vs. IO DSCR
   - Assess prepayment provisions (yield maintenance, defeasance, step-down) against hold period
   - Review recourse carve-outs (bad boy guarantees) and their scope
   - Flag any cash management triggers (hard vs. soft lockbox, cash sweep thresholds)

6. **Compile the underwriting package**
   - Loan sizing summary table showing proceeds under each metric
   - Sources and uses of funds
   - Sensitivity tables (rate, NOI, cap rate scenarios)
   - Borrower/sponsor summary and guarantor financial capacity
   - Risk factors and mitigants narrative

## Output

A structured loan underwriting report containing:

- **Loan sizing summary**: Maximum proceeds by DSCR, LTV, and debt yield with the binding constraint identified
- **NOI waterfall**: Gross-to-net income build with clear in-place vs. underwritten adjustments
- **Coverage metrics table**: DSCR (IO and amortizing), LTV, debt yield at base case and stress scenarios
- **Sensitivity matrix**: NOI decline × interest rate increase grid showing resulting DSCR
- **Sources & uses**: Total project cost, equity requirement, and loan-to-cost
- **Risk summary**: Key risks (lease rollover concentration, market softness, sponsor experience) with mitigants
- **Term comparison** (if multiple proposals): Side-by-side lender term sheets with net proceeds, all-in cost, and flexibility ranked

## Quality Checks

- NOI underwriting ties back to the rent roll and T-12 with all adjustments documented
- Debt service calculation matches the stated rate, amortization, and IO period precisely
- All three coverage metrics (DSCR, LTV, debt yield) are computed and the binding constraint is correctly identified
- Stress scenarios use clearly stated assumptions and show metric movement directionally
- Vacancy assumption is justified relative to submarket data, not assumed at a flat percentage without support
- Management fee is underwritten consistently (market standard or actual, whichever is higher) [VERIFY: lender underwriting convention]
- Reserves (TI/LC, capex, ground rent if applicable) are included in the cash flow before debt service where required by the lender
- No circular references between stabilized value assumptions and loan sizing
- Sponsor financial capacity (net worth ≥ loan amount, liquidity ≥ 10% of loan) is verified against lender requirements [VERIFY: specific lender thresholds]
