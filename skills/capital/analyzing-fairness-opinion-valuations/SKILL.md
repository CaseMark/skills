---
name: analyzing-fairness-opinion-valuations
description: Evaluates fairness opinion methodologies across DCF, trading comps, and precedent transactions for board-level decisions. Use when reviewing fairness opinions, preparing board materials, or analyzing transaction fairness.
tags:
  - analysis
  - mergers-and-acquisitions
  - trading
metadata:
  author: casemark
  practice_areas:
    - M&A Advisory
    - Corporate Development
    - Investment Banking
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Fairness Opinion Valuations

## When To Use

- Reviewing a fairness opinion delivered by an investment bank in connection with a merger, acquisition, going-private transaction, or related-party deal
- Preparing board or special committee materials that summarize or critique valuation analyses
- Comparing valuation ranges across methodologies (DCF, comparable companies, precedent transactions) to assess whether an offered price falls within a reasonable band
- Evaluating whether the opinion provider's methodology, assumptions, and data sources are appropriate for the specific transaction context
- Conducting a second-look analysis for litigation support (e.g., appraisal proceedings, duty-of-care challenges)

## Inputs To Gather

- **Fairness opinion letter and supporting presentation** — the full deliverable from the opinion provider, including appendices
- **Transaction terms** — purchase price (per-share or aggregate), consideration mix (cash, stock, earnout), collar or walk-away provisions
- **Target company financials** — historical income statements, balance sheets, and cash flow statements (3–5 years); management projections if available
- **Comparable company set used** — tickers, selection rationale, trading multiples applied (EV/EBITDA, EV/Revenue, P/E)
- **Precedent transaction set used** — deal list, multiples paid, premiums to unaffected price
- **DCF assumptions** — projection period, terminal value approach (perpetuity growth vs. exit multiple), WACC components (beta, equity risk premium, cost of debt, capital structure)
- **Engagement letter / fee structure** — whether the advisor's fee is contingent on deal completion (potential conflict indicator)
- **Market context** — index levels, sector performance, and volatility environment at valuation date

## Workflow

1. **Map the valuation summary** — Extract the implied per-share or enterprise value range from each methodology. Build a consolidated "football field" chart showing how ranges overlap relative to the offer price.

2. **Assess the DCF analysis**
   - Verify that projections are management-sourced or, if banker-adjusted, that adjustments are disclosed and justified.
   - Check the discount rate build-up: confirm beta source (raw vs. adjusted, peer median vs. target-specific), equity risk premium vintage, size premium inclusion, and debt cost assumptions. [VERIFY] whether the WACC falls within a defensible range for the target's industry and risk profile.
   - Evaluate terminal value: for perpetuity-growth models, confirm the long-term growth rate relative to GDP and industry norms; for exit-multiple models, confirm the multiple is anchored to a supportable comp set.
   - Test sensitivity tables — do the presented ranges capture reasonable bull/bear scenarios, or are they artificially narrow?

3. **Evaluate trading comparables**
   - Review peer selection criteria (SIC/GICS codes, revenue size, margin profile, growth rate, geographic mix). Flag any inclusions or exclusions that appear to skew the range.
   - Confirm which multiples are used and whether they are calculated on a trailing, forward, or calendarized basis. Note the reference date.
   - Check for outlier treatment — was any comp excluded or adjusted, and is the rationale transparent?

4. **Evaluate precedent transactions**
   - Confirm that deals are relevant by vintage (typically within 3–5 years), sector alignment, and transaction type (strategic vs. financial sponsor).
   - Distinguish between announced and completed transactions; note any deals that were later terminated.
   - Assess whether premiums paid are measured against unaffected share prices and whether appropriate look-back periods (1-day, 30-day VWAP) are used.

5. **Identify conflicts and process issues**
   - Determine whether the opinion provider also served as a financing source, had prior advisory relationships, or earns a success fee. These do not invalidate the opinion but must be weighed.
   - Check whether a special committee retained independent advisors separately from company management.

6. **Synthesize and opine**
   - Summarize where the offer price sits relative to each methodology's range (below midpoint, at midpoint, above midpoint).
   - Highlight any methodology whose range does not capture the offer price — this is a red flag requiring explanation.
   - Identify the key swing assumptions that, if adjusted, would move the valuation range materially.

## Output

Produce a structured analysis memo containing:

- **Executive summary** — one-paragraph conclusion on whether the valuation work supports the fairness determination, with caveats
- **Methodology comparison table** — columns for each valuation approach, rows for implied low/mid/high value, offer price marked
- **DCF deep-dive** — discount rate build-up table, projection summary, terminal value analysis, sensitivity matrix critique
- **Comps and precedents critique** — peer/deal selection assessment, multiple range analysis, outlier flags
- **Conflict and process flags** — fee structure, dual roles, committee independence observations
- **Key assumptions sensitivity** — the 3–5 assumptions with the largest impact on valuation range, with directional commentary
- **[VERIFY] items** — consolidated list of data points or assumptions requiring independent confirmation

## Quality Checks

- Every valuation range cited traces to a specific page or exhibit in the source opinion
- Discount rate components are individually sourced and cross-checked against market data providers (Bloomberg, Kroll/Duff & Phelps Cost of Capital Navigator) [VERIFY]
- Comparable company and precedent transaction sets are tested for cherry-picking — omissions of obvious peers are flagged
- Sensitivity ranges are wide enough to capture realistic downside/upside scenarios; artificially tight ranges are called out
- Conflict disclosures from the engagement letter are reflected in the process flags section
- The analysis avoids rendering a legal conclusion on "fairness" — it evaluates the financial methodology, not the legal standard of review (entire fairness, business judgment rule) [VERIFY] applicable standard based on jurisdiction and transaction type
