---
name: structuring-commercial-mortgage-securitization
description: Designs CMBS structures with property-level underwriting, DSCR analysis, and loan-level credit assessment. Use when structuring CMBS deals, underwriting commercial mortgage pools, or analyzing property cash flows.
tags:
  - structured-finance
  - credit
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Commercial Mortgage Securitization

Designs CMBS structures with property-level underwriting, DSCR analysis, and loan-level credit assessment.

## When To Use

- Structuring a new CMBS conduit or single-asset/single-borrower (SASB) transaction
- Underwriting a pool of commercial mortgage loans for securitization
- Evaluating property-level cash flows and debt service coverage across a loan tape
- Assessing credit enhancement levels, subordination, and tranche sizing
- Reviewing an existing CMBS structure for refinancing, B-piece acquisition, or special servicing triggers

## Inputs To Gather

- **Loan tape**: Loan-level data including balance, coupon, maturity, amortization schedule, IO period, prepayment provisions (yield maintenance, defeasance, lockout)
- **Property financials**: Trailing-12-month (T-12) and in-place rent rolls, historical NOI, capital expenditure reserves, tenant improvement/leasing commission budgets
- **Appraisals and valuations**: As-is and as-stabilized appraised values; cap rate assumptions by property type and market
- **Property type and geography**: Office, retail, multifamily, industrial, hospitality, self-storage, or mixed-use; MSA-level market data
- **Borrower/sponsor information**: Track record, net worth, liquidity covenants, carve-out guarantor details
- **Target capital structure**: Desired tranche classes (AAA through B-piece/unrated), anticipated rating agency (KBRA, Fitch, DBRS Morningstar, S&P), credit enhancement targets
- **Deal terms**: Advancing obligations, servicing fee structure (master, primary, special), controlling class rights, risk retention approach (horizontal, vertical, L-shaped) [VERIFY per Dodd-Frank/EU risk retention rules as applicable]

## Workflow

1. **Loan-level underwriting**
   - Calculate debt service coverage ratio (DSCR) using in-place NOI and stressed NOI (apply haircuts for vacancy, management fees, CapEx reserves)
   - Compute loan-to-value (LTV) using appraised value and securitization trust balance
   - Stress-test each loan: apply NOI declines (typically 5-15% depending on property type), cap rate expansion (25-75 bps), and interest rate shocks for floating-rate loans
   - Flag loans with DSCR < 1.25x or LTV > 75% for enhanced scrutiny [VERIFY: rating agency DSCR/LTV thresholds vary by property type and agency methodology]

2. **Property cash flow analysis**
   - Build property-level cash flow models: gross potential rent, vacancy/credit loss, effective gross income, operating expenses, NOI, below-the-line adjustments (TI/LC, CapEx)
   - Apply re-tenanting assumptions for near-term lease expirations (rollover risk)
   - For hospitality: use RevPAR-based projections with seasonal adjustments
   - For retail: analyze tenant sales per square foot, co-tenancy clauses, and anchor tenant credit quality

3. **Pool composition and concentration analysis**
   - Evaluate pool diversity: property type, geographic, sponsor, and single-tenant concentrations
   - Compute Herfindahl score and top-10 loan concentration
   - Identify any pari passu or subordinate companion loan structures (A/B notes, mezzanine debt, preferred equity layers)

4. **Capital structure and tranche sizing**
   - Set credit enhancement levels per tranche based on target ratings and agency loss models
   - Size AAA, AA, A, BBB-, and below-investment-grade classes; determine horizontal risk retention piece
   - Model waterfall mechanics: sequential pay vs. pro rata triggers, principal allocation, loss allocation (reverse sequential), interest shortfall recovery, appraisal reduction amounts (ARA)
   - Define servicer advancing obligations and reimbursement priority

5. **Stress testing and scenario analysis**
   - Run base, downside, and severe scenarios across the pool
   - Model default timing curves (front-loaded vs. back-loaded) with assumed loss severity by property type (typically 30-50% for conduit)
   - Assess tranche breakeven analysis: determine the cumulative loss level at which each tranche experiences principal loss
   - Evaluate weighted-average life (WAL) stability under varying prepayment speeds (0 CPR, pricing speed, 100 CPY)

6. **Documentation and deliverable assembly**
   - Compile loan-level summaries with DSCR, LTV, debt yield, and key risk factors
   - Prepare pool stratification tables (by property type, geography, loan size, maturity, coupon type)
   - Draft capital structure summary with credit enhancement waterfall, anticipated ratings, and pricing benchmarks
   - Note all assumptions, limitations, and items requiring further diligence

## Output

- **Pool summary**: Aggregate metrics — WA DSCR, WA LTV, WA coupon, WA debt yield, total pool balance, number of loans, property type breakdown
- **Loan-level detail**: Individual loan summaries with underwritten NOI, DSCR (as-is and stressed), LTV, property description, and risk flags
- **Capital structure table**: Tranche classes, balances, credit enhancement percentages, anticipated ratings, preliminary spread guidance
- **Waterfall mechanics**: Principal and interest allocation rules, loss allocation, advancing and reimbursement provisions
- **Stress results**: Scenario-based loss projections and tranche-level impact (breakeven default rates, expected loss by tranche)
- **Concentration tables**: Stratification by property type, geography, sponsor, loan size, maturity profile

## Quality Checks

- Confirm all DSCR calculations use consistent NOI definitions (in-place vs. underwritten vs. stressed) and clearly label each
- Verify LTV denominators match the correct valuation basis (appraised, allocated, or securitization value)
- Cross-check pool aggregate balance against the sum of individual loan balances
- Ensure credit enhancement levels align with published rating agency criteria [VERIFY: confirm current methodology documents from each target agency]
- Validate that waterfall mechanics correctly handle interest shortfalls, appraisal reductions, and workout-delayed reimbursement amounts
- Confirm risk retention compliance with applicable regulations [VERIFY: US Dodd-Frank Section 941 vs. EU Securitisation Regulation requirements]
- Flag any data gaps in the loan tape (missing appraisals, stale rent rolls, incomplete environmental reports) with [VERIFY] markers
- Ensure all stressed scenarios use defensible assumptions sourced from market data or agency guidance
