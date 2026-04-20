---
name: modeling-project-finance-structures
language: en
description: Builds project finance models with construction period draws, operational cash flows, DSCR covenants, and sculpted debt repayment. Use when modeling project finance, calculating debt service coverage, or structuring project lending.
tags:
  - modeling
  - infrastructure-and-project-finance
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Project Finance Structures

## When To Use

- Modeling a non-recourse or limited-recourse project financing (power plants, toll roads, LNG terminals, renewables, PPP/PFI concessions)
- Sizing senior debt tranches against projected cash flows and DSCR / LLCR covenants
- Structuring construction-period draws, equity contributions, and IDC capitalization
- Evaluating sculpted vs. level debt repayment profiles
- Running sensitivities for lender presentations, credit committee packages, or investment committee memos
- Assessing refinancing scenarios or mini-perm bullet structures

## Inputs To Gather

- **Project parameters**: capacity/throughput, construction timeline (months), COD target, concession term or asset useful life
- **Capital cost budget**: EPC contract price, owner's costs, contingency, development fees, financing fees, interest during construction
- **Revenue assumptions**: offtake/PPA price and escalation, availability/capacity factor, merchant price curves if applicable [VERIFY contracted vs. merchant split]
- **Operating cost assumptions**: fixed O&M, variable O&M, fuel/feedstock costs, insurance, land lease, management fees, major maintenance reserve schedule
- **Tax inputs**: depreciation method and schedule (MACRS, straight-line), tax rate, ITC/PTC eligibility [VERIFY jurisdiction-specific incentives], tax equity structure if relevant
- **Debt terms**: tenor, pricing (margin + base rate), commitment fee, upfront fees, DSCR lock-up and default levels, cash sweep percentage, DSRA sizing (typically 6-month debt service), maintenance capex reserve
- **Equity return targets**: target levered IRR, minimum cash-on-cash yield, distribution waterfall tiers if multiple equity classes

## Workflow

1. **Set up the timeline and flags**
   - Define semi-annual or quarterly periods from financial close through debt maturity and concession end
   - Create binary flags for construction, ramp-up, operations, and tail periods
   - Map construction draw schedule against EPC milestone payments

2. **Build the construction-period waterfall**
   - Model equity contributions and debt draws pro rata or equity-first per the term sheet
   - Capitalize interest during construction (IDC) and commitment fees into the loan balance
   - Track cumulative uses and sources; confirm total sources = total uses at COD

3. **Model operating revenue**
   - Calculate gross revenue from contracted offtake quantities × price × escalation
   - Apply availability/curtailment deductions
   - If merchant exposure exists, layer in price scenarios (base, low, high)

4. **Model operating expenses and taxes**
   - Project fixed and variable O&M with escalation indices
   - Build depreciation schedule and compute taxable income
   - Apply NOL carryforwards if early-year losses exist; compute cash taxes payable [VERIFY NOL rules per jurisdiction]

5. **Calculate Cash Flow Available for Debt Service (CFADS)**
   - CFADS = Revenue − Opex − Cash Taxes − Working Capital Changes − Maintenance Capex Reserve Contributions
   - Confirm CFADS excludes financing items (interest, principal, distributions)

6. **Size and sculpt debt repayment**
   - For sculpted repayment: solve each period's principal so that DSCR = target (e.g., 1.35×) across all periods
   - For level repayment: calculate annuity-based debt service; verify DSCR remains above minimum covenant (e.g., 1.20×)
   - Compute LLCR (NPV of CFADS over remaining debt life ÷ outstanding debt) and confirm ≥ lender threshold (typically 1.20×–1.30×)
   - Size DSRA funding requirement and model periodic top-ups/releases

7. **Build the equity distribution waterfall**
   - Apply lock-up DSCR test: if trailing/forward DSCR < lock-up level, trap cash
   - Calculate distributions after debt service, reserve funding, and cash sweep (if applicable)
   - Compute levered equity IRR and cash-on-cash multiples (MOIC)

8. **Run sensitivities and scenarios**
   - Single-variable: construction delay (+3/+6 months), cost overrun (+10%/+20%), revenue shortfall (−10%/−20%), interest rate stress (+100/+200 bps)
   - Breakeven analysis: find the revenue level or cost level where DSCR = 1.00×
   - Downside scenario: combine construction delay + cost overrun + low revenue; confirm covenant compliance or identify cash shortfall

## Output

- **Summary page**: project IRR, equity IRR, MOIC, average DSCR, minimum DSCR, LLCR at COD, maximum gearing, payback period
- **Sources & uses table**: construction period and permanent capital structure
- **Annual/semi-annual cash flow statement**: revenue through distributions, with CFADS and DSCR clearly shown per period
- **Debt schedule**: draws, repayments (sculpted or level), outstanding balance, interest, fees, DSRA balance
- **Sensitivity tables**: tornado chart inputs with equity IRR and min DSCR as outputs
- **Assumptions log**: every input with source reference, date, and [VERIFY] flags for unconfirmed items

## Quality Checks

- Sources = Uses in construction waterfall (zero variance)
- DSCR never drops below covenant default level in base case; identify periods where DSCR is within 0.10× of lock-up
- LLCR ≥ threshold at every calculation date
- Cash balance never goes negative in any period under base case
- Sum of all debt draws = committed facility amount; no over-draw
- Equity IRR circular reference resolved (use macro iteration or copy-paste values approach)
- Tax depreciation fully absorbed within concession/useful life; no phantom deductions after asset is fully depreciated
- Escalation indices applied consistently across revenue and cost lines [VERIFY index source and base year]
- Model balances: closing cash = opening cash + net cash flow in every period
