---
name: managing-fund-distributions
description: Structures fund distribution processes with allocation methodology, tax lot selection, and distribution notice preparation. Use when processing distributions, allocating fund income, or preparing distribution notices.
tags:
  - management
  - fund-operations
  - tax
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Fund Distributions

Structures fund distribution processes including allocation methodology, tax lot selection, distribution waterfall execution, and investor notice preparation for open-end funds, closed-end funds, and private fund vehicles.

## When To Use

- Processing periodic (monthly, quarterly, annual) income or capital gains distributions
- Allocating distributable income across share classes or investor capital accounts
- Selecting tax lots for in-kind or cash distributions
- Preparing distribution notices, reinvestment confirmations, or K-1 supporting schedules
- Reconciling distribution amounts against NAV, fund accounting records, and custodian statements
- Executing waterfall distributions for private equity or real estate fund vehicles

## Inputs To Gather

- **Fund structure**: Open-end mutual fund, closed-end fund, LP/LLC private fund, or interval fund
- **Distribution type**: Ordinary income, short-term capital gains, long-term capital gains, return of capital, or hybrid
- **Distribution frequency and record/ex/pay dates**: Confirm calendar and any board-declared amounts
- **Share class or investor details**: Class-level expense ratios, equalization method, investor capital accounts and commitment amounts
- **Tax lot inventory**: Current holdings with cost basis, acquisition dates, and holding period status
- **Waterfall terms** (private funds): Preferred return hurdle, GP catch-up, carried interest split, clawback provisions
- **Reinvestment elections**: DRIP participation rates, reinvestment NAV pricing conventions
- **Governing documents**: Prospectus, LPA/operating agreement, distribution policy resolutions

## Workflow

1. **Determine distributable amount**
   - Pull net investment income (NII), realized gains/losses, and undistributed balances from fund accounting
   - Deduct fund-level expenses allocated to the period
   - For private funds, calculate available cash after reserves, management fees, and fund expenses
   - Cross-check against excise tax distribution requirements (calendar-year 98% test for RICs) [VERIFY: confirm fund's fiscal year-end and excise tax election status]

2. **Classify income components**
   - Separate ordinary income, qualified dividend income (QDI), short-term gains, long-term gains, Section 199A dividends, and return of capital
   - For tax-exempt funds, identify exempt-interest dividends and AMT preference items [VERIFY: state-specific tax treatment varies]
   - Apply equalization accounting if the fund uses that method to prevent dilution from shareholder activity

3. **Select tax lots (if distributing securities or optimizing character)**
   - Apply the fund's stated tax lot identification method (FIFO, specific identification, highest-cost, average-cost for RICs)
   - Evaluate wash sale implications on lots sold within 30-day windows
   - Document lot selections with acquisition date, cost basis, and holding period for audit trail

4. **Allocate across share classes or investor accounts**
   - **Mutual funds**: Allocate per-share distribution amounts by class, adjusting for class-specific expense differentials
   - **Private funds**: Run the waterfall — preferred return accrual, return of contributed capital, GP catch-up layer, then residual profit split per carried interest terms
   - For LP waterfalls, calculate on a deal-by-deal or whole-fund basis per LPA terms [VERIFY: confirm waterfall methodology specified in governing docs]
   - Apply any side letter economics (fee discounts, co-invest offsets) before final allocation

5. **Prepare distribution notices**
   - Draft investor distribution notice including: record date, ex-date, pay date, per-share or per-unit amounts by income category, reinvestment price, and net cash payable
   - For private funds, include capital account statement showing beginning balance, contributions, distributions (current), ending balance, and unrealized carry
   - Attach tax character estimates with disclaimer that final characterization follows year-end audit

6. **Execute and reconcile**
   - Transmit payment instructions to custodian/transfer agent with CUSIP, pay date, and DTC eligibility details
   - Process DRIP reinvestments at the applicable NAV or market price
   - Reconcile distributed amounts against NAV drop on ex-date (NAV should decline by per-share distribution amount)
   - Verify custodian cash movements match expected totals within T+1

## Output

- **Distribution summary report**: Per-share/per-unit amounts by income category and share class
- **Waterfall schedule** (private funds): Step-by-step calculation from available cash through each tier to final GP/LP split
- **Tax lot selection log**: Identified lots with basis, dates, and gain/loss character
- **Investor distribution notice**: Ready-to-send notice with all required dates, amounts, and reinvestment details
- **Reconciliation worksheet**: NAV impact analysis, custodian cash match, and DRIP share issuance confirmation
- **Equalization schedule** (if applicable): Per-share equalization debits/credits by class

## Quality Checks

- Confirm total distribution amount ties to board resolution or GP authorization [VERIFY: check approval documentation]
- Verify per-share amounts multiplied by shares outstanding equal the aggregate distribution to the penny
- Validate that income character percentages sum to 100% and align with fund accounting trial balance
- For private funds, confirm waterfall output matches a manual spot-check of at least one investor's allocation
- Check that return-of-capital components do not exceed any investor's tax basis (flag if they do, as this triggers gain recognition)
- Ensure ex-date NAV adjustment is accurate and consistent with distribution amount
- Confirm all reinvestment shares are issued at the correct NAV and reflected in shareholder records
- Cross-reference distribution calendar against prospectus/LPA commitments and regulatory deadlines (excise tax safe harbor, RIC qualification tests)
