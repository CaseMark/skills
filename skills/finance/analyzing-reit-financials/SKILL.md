---
name: analyzing-reit-financials
language: en
description: Evaluates REIT financial performance with FFO, AFFO, NAV, and leverage metrics. Use when analyzing REITs, calculating FFO/AFFO, or comparing REIT valuations.
tags:
  - analysis
  - real-estate-finance
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Real Estate Finance
    - REIT Analysis
    - Property Investment
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing REIT Financials

## When To Use

- Evaluating a REIT's operating performance for investment or lending decisions
- Calculating FFO, AFFO, or NAV from 10-K/10-Q filings or supplemental data packages
- Comparing REIT valuations across peers within the same property sector
- Assessing leverage, coverage ratios, and distribution sustainability
- Preparing underwriting memos or investment committee summaries for REIT-backed transactions

## Inputs To Gather

- **Financial statements**: Income statement, balance sheet, cash flow statement (at least 2–3 periods for trend analysis)
- **Supplemental operating data**: Same-store NOI, occupancy rates, lease expirations, tenant concentration
- **Capitalization details**: Share count (diluted), OP units, preferred equity, convertible instruments
- **Debt schedule**: Outstanding balances, maturities, interest rates, secured vs. unsecured split, credit facility availability
- **Distribution history**: Dividend per share, payout ratio, DRIP participation
- **Peer set**: 3–5 comparable REITs by property type, geography, and market cap for relative valuation
- **Market data**: Current share price, trading volume, analyst consensus estimates

## Workflow

1. **Calculate FFO**
   - Start with GAAP net income attributable to common shareholders
   - Add back real estate depreciation and amortization
   - Remove gains/losses on property sales and impairments
   - Adjust for unconsolidated JV interests (proportionate share)
   - Express as FFO per diluted share/unit

2. **Calculate AFFO (CAD/FAD)**
   - Begin with FFO
   - Subtract recurring capital expenditures (maintenance capex, tenant improvements, leasing commissions)
   - Adjust for straight-line rent and above/below-market lease amortization
   - Add back non-cash compensation expense
   - Express as AFFO per diluted share/unit and compute AFFO payout ratio (dividends ÷ AFFO)

3. **Estimate Net Asset Value (NAV)**
   - Capitalize stabilized NOI by property segment using appropriate cap rates [VERIFY cap rate sources — broker surveys, transaction comps, or appraised values]
   - Add value of development pipeline, land bank, and other tangible assets at estimated fair value
   - Add cash and receivables; subtract total debt, preferred equity, and other liabilities at face or fair value
   - Divide by fully diluted share/unit count to arrive at NAV per share
   - Compare current share price to NAV: premium/(discount) = (Price − NAV) ÷ NAV

4. **Assess Leverage and Coverage**
   - **Debt-to-Gross Assets**: Total debt ÷ (total assets + accumulated depreciation)
   - **Net Debt / EBITDA**: (Total debt − cash) ÷ trailing EBITDA (target typically 5.0×–7.0× depending on sector) [VERIFY sector-specific thresholds]
   - **Fixed Charge Coverage**: Adjusted EBITDA ÷ (interest expense + preferred dividends + secured debt amortization); minimum 1.5× is common benchmark
   - **Secured Debt Ratio**: Secured debt ÷ total assets; most investment-grade REITs target < 40%
   - **Debt Maturity Profile**: Flag any single-year maturity exceeding 15–20% of total debt

5. **Peer Comparison**
   - Assemble a table with: P/FFO, P/AFFO, premium/discount to NAV, dividend yield, same-store NOI growth, leverage metrics
   - Rank subject REIT within peer group on each metric
   - Note any structural differences affecting comparability (e.g., external vs. internal management, JV-heavy structures, development exposure)

6. **Distribution Sustainability**
   - AFFO payout ratio above 90% signals limited retained cash flow cushion
   - Review trend in AFFO per share vs. dividend per share over 3+ years
   - Check whether distributions are funded by asset sales, debt draws, or equity issuance rather than operating cash flow

## Output

Produce a structured analysis report containing:

- **Executive Summary**: One-paragraph investment thesis with bull/bear case and key conclusion
- **FFO / AFFO Bridge**: Tabular reconciliation from GAAP net income to FFO to AFFO with per-share figures
- **NAV Summary**: Segment-level NOI and cap rate assumptions, NAV per share, and premium/discount
- **Leverage Dashboard**: Key ratios with traffic-light indicators (green/yellow/red relative to sector norms)
- **Peer Comp Table**: Side-by-side metrics for subject and comparable REITs
- **Risk Factors**: Tenant concentration, lease rollover exposure, floating-rate debt percentage, geographic concentration
- **Appendix**: Detailed assumptions, data sources, and any items marked [VERIFY]

## Quality Checks

- FFO reconciliation must tie back to the GAAP income statement line by line — any unexplained delta should be flagged
- Confirm diluted share count includes OP units, vested RSUs, and in-the-money convertibles
- Verify cap rates used for NAV are sourced and dated; stale cap rates can materially distort NAV
- AFFO maintenance capex should reflect actual recurring spend, not management's normalized guidance, unless justified
- Ensure leverage ratios use consistent definitions (e.g., gross vs. net debt, GAAP vs. pro forma EBITDA)
- Cross-check dividend yield calculation against most recent declared distribution and current price
- Mark any metric that relies on management-reported non-GAAP adjustments with [VERIFY] for independent confirmation
