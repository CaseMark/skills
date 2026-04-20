---
name: modeling-debt-maturity-profiles
language: en
description: Structures debt maturity analysis with refinancing risk, market access assumptions, and liability management opportunities. Use when analyzing maturity walls, planning refinancing, or optimizing debt tenor.
tags:
  - modeling
  - debt-capital-markets
  - risk
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Debt Maturity Profiles

## When To Use

- Analyzing a borrower's maturity wall to quantify near-term refinancing exposure
- Planning a liability management exercise (tender, exchange, or extension)
- Stress-testing refinancing capacity under adverse market conditions
- Comparing debt tenor strategies for new issuance or acquisition financing
- Preparing credit committee or investor materials showing debt runway

## Inputs To Gather

- **Debt schedule**: Instrument-level detail — facility name, tranche type (TL, revolver, bond, convertible), original principal, outstanding balance, maturity date, coupon/spread, amortization schedule, call protection or make-whole provisions
- **Credit agreement terms**: Mandatory prepayment provisions, springing maturities, accordion capacity, extension options, change-of-control puts
- **Financial projections**: EBITDA, FCF, and cash balance forecasts over the maturity horizon (minimum 5 years, ideally matching the longest-dated tranche)
- **Capital structure context**: Total leverage, secured leverage, interest coverage, any maintenance or incurrence covenants that gate refinancing capacity
- **Market assumptions**: Current benchmark rates (SOFR curve, Treasury curve), indicative new-issue spreads by rating and tranche type, market access windows [VERIFY — spreads are point-in-time]

## Workflow

1. **Build the maturity schedule**
   - Map every debt instrument to its contractual maturity date, capturing bullet maturities and scheduled amortization separately
   - Flag springing maturities (e.g., term loan springing 91 days ahead of unsecured notes) — these override contractual dates
   - Include revolver expiration alongside funded maturities; note undrawn capacity

2. **Construct the maturity wall visualization**
   - Produce a time-bucketed chart (quarterly or annual) showing aggregate maturities by instrument type
   - Overlay secured vs. unsecured segmentation and fixed vs. floating split
   - Highlight concentration risk: any single year exceeding 30–40% of total debt signals elevated refinancing risk

3. **Layer in refinancing assumptions**
   - For each maturing tranche, define a refinancing scenario: repay from cash, refinance at market, extend via amendment, or tender/exchange
   - Apply forward curve rates plus credit spread assumptions to estimate new coupon cost [VERIFY — confirm current spread indications with syndicate desk]
   - Model refinancing proceeds net of OID, fees, and any call premiums
   - If mandatory prepayment sweeps reduce outstanding balances before maturity, reflect those cash flows

4. **Run the pro forma debt profile**
   - Output a year-by-year schedule showing: beginning balance, scheduled amortization, refinancing activity, ending balance, weighted average maturity (WAM), and weighted average cost of debt (WACD)
   - Calculate WAM before and after proposed transactions to quantify tenor extension
   - Compute annual interest expense under base-case and stressed rate scenarios

5. **Stress-test refinancing risk**
   - **Market closure scenario**: Assume no capital markets access for 12–18 months — does the borrower have sufficient liquidity (cash + revolver) to address near-term maturities?
   - **Spread widening**: Shock credit spreads by +150–300 bps and re-run interest expense and coverage ratios
   - **Downgrade scenario**: Model one-notch downgrade impact on pricing grids and covenant headroom
   - Identify the "refinancing cliff" — the earliest date at which maturities exceed available liquidity under stress

6. **Evaluate liability management alternatives**
   - Compare NPV of early redemption (at make-whole or first call) vs. open-market repurchase vs. exchange offer
   - For exchange offers, model the accounting treatment (modification vs. extinguishment) and its P&L impact [VERIFY — consult accounting guidance for specific instrument terms]
   - Size any new money component needed to incentivize participation

## Output

- **Maturity profile summary table**: Instrument, outstanding balance, maturity date, coupon, secured/unsecured, fixed/floating
- **Maturity wall chart**: Time-bucketed visual with segmentation by seniority and rate type
- **Pro forma schedule**: Year-by-year beginning balance → amortization → refinancing → ending balance, with WAM and WACD
- **Stress scenario dashboard**: Coverage ratios and liquidity runway under base, spread-widening, and market-closure cases
- **Liability management comparison**: Side-by-side economics of redemption, repurchase, and exchange alternatives (where applicable)

## Quality Checks

- Ending balances in the maturity schedule must tie to the total debt figure on the balance sheet — reconcile any discrepancies from unamortized OID, deferred financing costs, or fair-value adjustments
- Confirm springing maturity triggers are correctly coded (verify the exact look-back period and outstanding threshold from the credit agreement)
- WAM and WACD calculations should be balance-weighted, not count-weighted
- Stress scenarios must reflect actual covenant definitions (e.g., whether EBITDA is LTM or annualized, whether add-backs apply) [VERIFY — pull covenant definitions from governing documents]
- Cross-check new-issue spread assumptions against recent comparable transactions and syndicate color
- Ensure call protection and make-whole mechanics are accurately reflected — early redemption costs can materially change the economics of liability management options
