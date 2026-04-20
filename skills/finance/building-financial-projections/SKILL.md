---
name: building-financial-projections
language: en
description: Constructs integrated three-statement financial models with scenario analysis and assumption documentation. Use when building financial models, projecting financial statements, or creating forecast scenarios.
tags:
  - modeling
  - corporate-finance
metadata:
  author: casemark
  practice_areas:
    - Corporate Finance
    - Treasury
    - Financial Planning
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Financial Projections

## When To Use

- Building an integrated income statement, balance sheet, and cash flow projection for a company or business unit
- Forecasting financial performance for budgeting, fundraising, M&A due diligence, or strategic planning
- Creating scenario analysis (base/upside/downside) to stress-test key business drivers
- Developing projections to support debt covenants, credit applications, or board presentations
- Modeling treasury cash flow forecasts for liquidity planning

## Inputs To Gather

- **Historical financials**: 3–5 years of audited or management-prepared income statements, balance sheets, and cash flow statements
- **Revenue drivers**: unit volumes, pricing, contract backlog, market growth rates, customer counts, or segment breakdowns
- **Cost structure**: fixed vs. variable cost split, COGS composition, headcount plans, capex schedule
- **Working capital detail**: DSO, DIO, DPO historical trends and any known changes (e.g., new payment terms)
- **Capital structure**: existing debt schedule (maturity, rate, amortization), planned issuances or repayments, equity raise assumptions
- **Tax assumptions**: effective tax rate, NOL carryforwards, known rate changes [VERIFY jurisdiction-specific rates]
- **Management guidance or budget**: any internal targets, board-approved plans, or strategic initiatives that affect projections
- **Macro assumptions**: inflation rates, FX rates, interest rate curves if relevant

## Workflow

1. **Normalize historicals**
   - Restate financials to remove one-time or non-recurring items (restructuring charges, litigation settlements, asset impairments)
   - Reconcile income statement to balance sheet to cash flow — confirm net income flows through, capex ties to PP&E roll-forward, debt ties to interest expense
   - Calculate historical KPIs: revenue growth, gross margin, EBITDA margin, DSO/DIO/DPO, capex-to-revenue, effective tax rate

2. **Define projection architecture**
   - Set forecast horizon (typically 3–5 years for operating models, 5–10 for infrastructure/project finance)
   - Choose revenue build methodology: top-down (market size × share), bottom-up (units × price), or hybrid
   - Establish an assumptions table as a single consolidated input panel — all key drivers in one place, color-coded (blue for inputs, black for formulas)

3. **Build the income statement**
   - Project revenue by segment or product line using identified drivers
   - Forecast COGS using gross margin assumptions or unit cost buildup
   - Model opex line-by-line: SG&A (headcount × fully loaded cost), R&D (as % of revenue or specific program budgets), D&A (from PP&E roll-forward)
   - Calculate EBIT, apply interest from debt schedule, compute pre-tax income, apply tax rate, arrive at net income

4. **Build the balance sheet**
   - Roll forward each asset and liability line: PP&E (beginning + capex − D&A − disposals), intangibles, goodwill
   - Project working capital using days-based assumptions: AR = revenue × (DSO/365), inventory = COGS × (DIO/365), AP = COGS × (DPO/365)
   - Model debt schedule: beginning balance + draws − repayments = ending balance; compute interest expense from average balances × rate
   - Equity: beginning + net income − dividends + issuances = ending; retained earnings must reconcile

5. **Build the cash flow statement**
   - Start from net income, add back D&A and non-cash items
   - Calculate changes in working capital from balance sheet deltas
   - Investing: capex, acquisitions, asset sales
   - Financing: debt proceeds/repayments, equity issuances, dividends, share repurchases
   - Ending cash = beginning cash + operating + investing + financing; this must tie to the balance sheet cash line

6. **Integrate and balance-check**
   - Confirm the balance sheet balances (assets = liabilities + equity) in every projection period
   - Verify the cash flow statement reconciles beginning to ending cash on the balance sheet
   - Add a revolver or cash sweep mechanism if modeling a credit facility (auto-draws to cover shortfalls, auto-repays from excess cash)

7. **Run scenario analysis**
   - Define base, upside, and downside cases with clearly stated assumption differences (e.g., base: 5% revenue growth; downside: flat revenue + 200bp margin compression)
   - Use a scenario toggle or data table to switch between cases
   - Sensitize 2–3 key variables (revenue growth, margin, capex) and present output ranges for EBITDA, free cash flow, net debt/EBITDA

8. **Document assumptions and limitations**
   - Create an assumptions summary page listing every driver, its value, and its source (management guidance, broker consensus, historical average, analyst estimate)
   - Flag any assumption without a verifiable source as [VERIFY]
   - Note model limitations: what is excluded (e.g., potential M&A, FX translation effects, pension liabilities)

## Output

- **Integrated three-statement model** with clearly separated input assumptions, calculations, and outputs
- **Assumptions summary** with source attribution for each driver
- **Scenario comparison table** showing key metrics (revenue, EBITDA, FCF, net debt, leverage ratio) across base/upside/downside
- **Sensitivity tables** on 2–3 critical variables
- **Balance check flags** confirming the model balances in all periods and scenarios

## Quality Checks

- Balance sheet balances in every period (zero-tolerance; assets = liabilities + equity)
- Cash flow statement ending cash ties to balance sheet cash in every period
- Interest expense is consistent with average debt balance × stated rate
- D&A expense ties to PP&E roll-forward schedule
- Working capital changes on cash flow statement match balance sheet period-over-period deltas
- Revenue and cost growth rates are within reasonable ranges relative to historicals and industry benchmarks
- Tax rate applied is consistent with disclosed effective rate [VERIFY for jurisdiction changes, NOL utilization, or rate sunset provisions]
- All hard-coded assumptions are isolated in the input panel — no buried constants in formula cells
- Scenario toggle produces materially different outputs; if base and downside are nearly identical, assumptions may be too narrow
