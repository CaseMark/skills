---
name: building-equity-valuation-models
language: en
description: Constructs DCF, comparable company, and precedent transaction valuation models with sensitivity analysis. Use when valuing public companies, building financial models, or estimating fair value ranges.
tags:
  - modeling
  - equity-research
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Model
  skill_modes:
    - Modeling
---
# Building Equity Valuation Models

## When To Use

- Estimating intrinsic or fair value of a public or private equity security
- Building or auditing a DCF, comparable company analysis (comps), or precedent transaction analysis
- Preparing valuation support for investment memos, pitch books, or fairness opinions
- Running sensitivity/scenario analysis around key value drivers
- Cross-checking a single-method valuation with a multi-method "football field" range

## Inputs To Gather

- **Company financials**: Most recent 10-K/10-Q or annual report — revenue, EBITDA, EBIT, net income, capex, D&A, working capital line items (minimum 3 years historical)
- **Forward estimates**: Consensus sell-side estimates or management guidance for revenue and earnings (2–3 years forward)
- **Capital structure**: Total debt, cash & equivalents, diluted share count (including options/RSUs via treasury stock method), preferred equity, minority interests
- **Comparable universe**: 5–10 peer companies with sector, size, growth, and margin similarity; confirm tickers and fiscal year ends
- **Precedent transactions**: Relevant M&A deals in the sector over the trailing 3–5 years with disclosed deal multiples
- **Discount rate inputs**: Risk-free rate [VERIFY current yield on 10-year sovereign], equity risk premium, levered/unlevered beta source, cost of debt, target capital structure for WACC
- **Terminal value assumptions**: Long-term growth rate or exit multiple, and rationale for each

## Workflow

### 1. Construct the DCF Model

- Project unlevered free cash flow (UFCF) for 5–10 years: Revenue → EBIT → NOPAT → add back D&A → subtract capex and changes in net working capital
- Calculate WACC: weight cost of equity (CAPM) and after-tax cost of debt by target capital structure [VERIFY tax rate assumptions per jurisdiction]
- Compute terminal value using both the perpetuity growth method (Gordon Growth) and the exit multiple method; present both
- Discount projected UFCF and terminal value to present; sum to get enterprise value
- Bridge to equity value: Enterprise Value − Net Debt − Minority Interests − Preferred + Associates/JV value → Equity Value ÷ Diluted Shares = Implied Price Per Share

### 2. Build Comparable Company Analysis

- Select peer set; document selection criteria (sector, geography, size, growth profile)
- Pull trailing and forward multiples: EV/Revenue, EV/EBITDA, EV/EBIT, P/E, P/FCF
- Calculate mean, median, and interquartile range; flag and discuss outliers
- Apply selected multiple range to subject company's corresponding metric to derive implied valuation range
- Adjust for company-specific premiums/discounts (growth differential, margin profile, risk factors)

### 3. Build Precedent Transaction Analysis

- Identify 8–15 comparable transactions; document deal date, buyer/seller, deal value, and strategic rationale
- Extract transaction multiples: EV/Revenue, EV/EBITDA at announcement and at LTM pre-deal
- Note control premiums paid (deal price vs. unaffected share price)
- Apply relevant multiple range to subject company metrics; clearly separate "as-is" value from "with-control-premium" value
- Flag stale transactions (>3 years old) and note market-environment differences [VERIFY macro conditions at deal close]

### 4. Sensitivity & Scenario Analysis

- **DCF sensitivities**: Build two-way data tables on (a) WACC vs. terminal growth rate and (b) WACC vs. exit multiple — display implied share price ranges
- **Comps sensitivities**: Show valuation at 25th, 50th, and 75th percentile multiples
- **Scenario overlay**: Define base, bull, and bear cases with explicit assumption changes (revenue growth, margin expansion/compression, multiple re-rating); summarize each scenario's implied value

### 5. Synthesize the Valuation Range

- Present a "football field" chart or table showing the implied price range from each methodology side by side
- Identify the central tendency across methods and highlight where methodologies converge or diverge
- State a recommended fair value range (not a point estimate) with confidence weighting by methodology

## Output

Deliver a structured valuation model containing:

- **Assumptions page**: Every key input listed, sourced, and dated; [VERIFY] tags on any assumed or estimated inputs
- **DCF tab**: Full UFCF build, WACC calculation, terminal value (both methods), bridge to equity value
- **Comps tab**: Peer summary table with multiples, statistical summary, implied valuation
- **Precedents tab**: Transaction summary, multiple ranges, implied valuation
- **Sensitivity tables**: Two-way tables for DCF; percentile tables for comps/precedents
- **Summary page**: Football field visualization, fair value range, key risks to the valuation thesis
- All figures clearly labeled with units, currency, and fiscal period

## Quality Checks

- Verify UFCF build ties back to source financials — check that Revenue → EBIT → NOPAT → UFCF reconciles
- Confirm WACC components are internally consistent (beta source matches peer set; debt cost matches credit profile)
- Ensure terminal value does not exceed 70–75% of total enterprise value; if it does, extend the explicit forecast period or revisit growth assumptions
- Validate that the equity bridge accounts for all claims ahead of common equity (convertibles, preferred, minority interests)
- Cross-check implied valuation multiples from DCF against comps range — significant divergence requires explanation
- Confirm diluted share count uses treasury stock method and reflects latest filing [VERIFY share count date]
- Review all [VERIFY] tags before finalizing; no unresolved tags in the delivered output
