---
name: analyzing-mezzanine-and-subordinated-debt
language: en
description: Evaluates mezzanine structures with PIK toggle, equity kickers, and intercreditor subordination mechanics. Use when analyzing mezzanine financing, comparing subordinated debt terms, or modeling layered capital structures.
tags:
  - analysis
  - debt-capital-markets
  - credit
metadata:
  author: casemark
  practice_areas:
    - DCM
    - Leveraged Finance
    - Debt Origination
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Mezzanine And Subordinated Debt

Evaluates mezzanine structures with PIK toggle, equity kickers, and intercreditor subordination mechanics for layered capital structures.

## When To Use

- Analyzing a proposed mezzanine financing term sheet against borrower economics and senior lender constraints
- Comparing subordinated debt structures across multiple lender proposals
- Modeling blended cost of capital across senior/mezzanine/equity tranches
- Reviewing intercreditor agreement terms for subordination mechanics and standstill provisions
- Assessing equity kicker dilution impact (warrants, conversion features, co-invest rights)
- Evaluating PIK toggle economics and cash flow implications under stress scenarios

## Inputs To Gather

- **Term sheet or credit agreement** for the mezzanine/subordinated tranche
- **Senior credit facility terms** — advance rates, covenants, permitted debt baskets, intercreditor requirements
- **Company financials** — historical and projected EBITDA, cash flow statements, existing debt schedule
- **Capital structure summary** — all tranches with amounts, rates, maturity, and priority
- **Intercreditor agreement** (if executed or in draft) — subordination type, standstill periods, turnover provisions, cure rights
- **Equity kicker documentation** — warrant coverage percentage, strike price, conversion ratios, anti-dilution protections
- **PIK terms** — PIK rate vs. cash pay rate, toggle conditions, PIK compounding frequency, PIK caps if any

## Workflow

1. **Map the capital structure** — Build a sources-and-uses table showing each tranche's position in the priority waterfall. Identify total leverage, senior leverage, and mezzanine leverage multiples (Senior Debt / EBITDA, Total Debt / EBITDA). Flag any leverage levels outside market norms for the sector [VERIFY against current market benchmarks].

2. **Analyze coupon and yield economics**
   - Break down the mezzanine return into components: cash coupon, PIK accrual, upfront fees (OID), and equity kicker value
   - Calculate all-in yield to maturity and IRR under base case and PIK-toggle scenarios
   - Model PIK accrual growth: confirm compounding mechanics (simple vs. compound, quarterly vs. semi-annual) and compute accreted balance at maturity
   - Compare blended cost of the mezzanine tranche against market clearing rates [VERIFY current mezz market spreads for comparable credit quality]

3. **Evaluate PIK toggle mechanics**
   - Identify toggle triggers — is the PIK election borrower-optional, tied to a leverage or coverage ratio test, or mandatory under certain conditions?
   - Model cash flow under full-cash-pay, full-PIK, and partial-PIK scenarios
   - Calculate the maximum PIK balance at maturity and its impact on total leverage and refinancing risk
   - Assess whether PIK compounding creates a maturity cliff that exceeds projected enterprise value

4. **Assess equity kicker dilution and value**
   - For warrants: calculate warrant coverage as a percentage of fully diluted equity, determine strike price relative to entry equity value, and model dilution at exit across multiple MOIC scenarios (1.0x–3.0x)
   - For conversion features: map conversion price, conversion ratio, and forced-conversion triggers; model as-converted ownership
   - Estimate equity kicker value using Black-Scholes or scenario-based methods and add to total yield analysis
   - Review anti-dilution protections (full ratchet vs. weighted average) and participation rights

5. **Review intercreditor and subordination terms**
   - Classify subordination type: contractual subordination (payment waterfall) vs. structural subordination (holding-company debt) vs. lien subordination (second-lien)
   - Identify standstill period duration — how long must the mezzanine lender wait after a senior default before exercising remedies? (Market range: 90–180 days [VERIFY])
   - Review turnover and blockage provisions: under what conditions are mezzanine payments blocked, and for how long?
   - Check for mezzanine lender cure rights — ability to cure senior defaults and step into borrower's position
   - Assess buyout rights — can the mezzanine lender purchase the senior debt at par?
   - Evaluate permitted actions during standstill (e.g., acceleration allowed but no enforcement)

6. **Stress-test the structure**
   - Run downside scenarios: revenue decline of 10%, 20%, 30% from base case
   - Test fixed charge coverage ratio (FCCR) and interest coverage under each scenario
   - Identify the EBITDA level at which the borrower breaches mezzanine covenants vs. senior covenants
   - Assess recovery waterfall in a hypothetical liquidation — estimate recovery rates for each tranche based on asset coverage

7. **Benchmark against alternatives**
   - Compare mezzanine terms to: second-lien term loans, unitranche facilities, preferred equity, and direct lending options
   - Evaluate total cost of capital impact — would a different structure produce lower WACC or better covenant flexibility?
   - Note structural trade-offs (e.g., unitranche simplicity vs. mezzanine flexibility on PIK)

## Output

Produce an analysis report containing:

- **Capital Structure Summary Table** — Each tranche with amount, rate (cash/PIK), maturity, leverage multiple, and priority ranking
- **Mezzanine Economics Summary** — Cash coupon, PIK rate, OID, equity kicker value, all-in IRR under base and PIK scenarios
- **PIK Accrual Schedule** — Period-by-period PIK balance growth through maturity
- **Equity Kicker Dilution Table** — Dilution at exit across multiple valuation scenarios
- **Intercreditor Terms Matrix** — Key provisions mapped: subordination type, standstill period, blockage terms, cure rights, buyout rights
- **Stress Test Results** — Coverage ratios and recovery estimates under base, downside, and severe downside cases
- **Key Risks and Considerations** — Refinancing risk from PIK accrual, covenant cushion analysis, structural vulnerabilities
- **Comparison to Alternatives** — Side-by-side of mezzanine vs. competing structures on cost, flexibility, and complexity

## Quality Checks

- Verify that all-in yield calculation includes every return component (cash, PIK, fees, equity kicker) — omitting any one will materially understate true cost
- Confirm PIK compounding mechanics match the actual term sheet language (simple interest vs. compound, frequency)
- Ensure intercreditor analysis distinguishes between payment subordination and lien subordination — conflating them misrepresents lender rights
- Validate that stress scenarios use internally consistent assumptions (e.g., revenue decline should flow through to EBITDA with appropriate margin compression)
- Check that equity kicker dilution is calculated on a fully diluted basis including all outstanding options, warrants, and convertible instruments
- Confirm leverage multiples use the same EBITDA definition (adjusted vs. unadjusted) across all tranches for comparability
- Flag any terms that deviate materially from market standards with [VERIFY] and note the deviation
