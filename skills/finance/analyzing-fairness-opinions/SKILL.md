---
name: analyzing-fairness-opinions
description: Evaluates fairness opinion analyses with valuation methodology review and conclusion assessment. Use when reviewing fairness opinions, analyzing board-level valuations, or evaluating transaction fairness.
tags:
  - analysis
  - investment-banking
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Investment Banking
    - Mergers and Acquisitions
    - Corporate Finance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Fairness Opinions

## When To Use

- Reviewing a fairness opinion issued by an investment bank in connection with a merger, acquisition, going-private transaction, or related-party deal
- Assessing whether the valuation methodologies and assumptions underlying a fairness opinion are reasonable and complete
- Preparing board-level or special committee commentary on a received fairness opinion
- Evaluating potential conflicts of interest or scope limitations in an advisor's opinion
- Benchmarking a fairness opinion against market practice for comparable transactions

## Inputs To Gather

- **Fairness opinion letter** — the formal opinion and any attached presentation or analysis book
- **Transaction summary** — deal structure (cash, stock, mixed), consideration per share, implied premiums, and key terms (collars, earnouts, CVRs)
- **Company financials** — historical income statements, balance sheets, and cash flow statements (minimum 3 years); management projections if available
- **Comparable company and transaction data** — public comps trading multiples and precedent transaction multiples used or potentially omitted by the advisor
- **Engagement letter / fee arrangement** — advisor compensation structure, including any success-based or contingent fees
- **Discounted cash flow inputs** — projection period, terminal value methodology, WACC components, and sensitivity ranges
- **Prior valuations** — any recent 409A valuations, prior M&A bids, or third-party appraisals for cross-reference
- **Market context** — sector index performance and credit spreads around the opinion date to evaluate timing sensitivity

## Workflow

1. **Confirm scope and transaction context**
   - Identify the transaction type (merger of equals, controlling-shareholder buyout, squeeze-out, asset sale)
   - Note the opinion's addressee (board, special committee) and the standard applied ("fair, from a financial point of view" to holders as a class vs. individually)
   - Flag if the opinion covers only financial fairness or also procedural fairness [VERIFY — some opinions are explicitly limited in scope]

2. **Evaluate valuation methodologies employed**
   - Check which standard approaches are used: comparable company analysis, precedent transactions, DCF, LBO analysis, sum-of-the-parts
   - Identify any methodology that was **omitted** — if a DCF was excluded or a premiums-paid analysis was skipped, note the stated rationale and assess reasonableness
   - For each methodology, verify that the selected peer set and transaction comps are defensible (sector, size, geography, timing)

3. **Stress-test key assumptions**
   - **DCF**: Scrutinize the projection source (management vs. consensus vs. advisor-adjusted), discount rate build-up (risk-free rate source, equity risk premium, beta derivation, size premium), and terminal value (perpetuity growth rate vs. exit multiple)
   - **Comps**: Assess whether multiples (EV/EBITDA, EV/Revenue, P/E) are applied to LTM, NTM, or projected metrics — and whether calendarization is consistent
   - **Precedent transactions**: Check vintage of transactions and whether control premiums are appropriately distinguished from synergy-inclusive pricing
   - Run implied sensitivity tables — small changes to WACC or terminal growth rate should not flip the fairness conclusion; if they do, flag the opinion as narrowly supported

4. **Assess the valuation range and conclusion**
   - Map each methodology's implied value range against the deal price
   - Determine whether the deal price falls within, below, or above the composite range
   - Note if the advisor relies on a "reference range" versus a "single point" conclusion and whether the ranges across methodologies converge or diverge materially

5. **Review for conflicts and limitations**
   - Confirm whether the advisor has material relationships with the counterparty (lending, prior advisory, equity ownership)
   - Check for contingent fee structures that incentivize deal completion — a significant success fee relative to the retainer raises conflict concerns [VERIFY — disclosure requirements vary; check SEC proxy/14D-9 filings]
   - Note any express disclaimers (e.g., "we have not independently verified management projections") and assess their materiality

6. **Benchmark against market practice**
   - Compare the number and type of methodologies to opinions in similar-sized transactions
   - Assess whether the opinion meets the expectations set by Delaware case law (e.g., *In re Toys "R" Us*, *In re Del Monte Foods*) for special committee processes [VERIFY — applicable standards depend on jurisdiction and transaction structure]

## Output

Produce a structured memorandum containing:

- **Executive summary** — one-paragraph assessment of whether the opinion is well-supported, narrowly supported, or materially deficient
- **Methodology review table** — for each methodology: approach used, key inputs, implied per-share range, and identified issues
- **Assumptions sensitivity analysis** — key driver sensitivities (WACC +/- 50 bps, terminal growth +/- 50 bps, multiple +/- 0.5x) with resulting value impact
- **Conflict and limitation flags** — itemized list of advisor conflicts, fee structure concerns, and scope carve-outs
- **Omission checklist** — methodologies, comps, or adjustments that were absent and could materially affect the conclusion
- **Overall assessment** — rating of opinion quality (robust / adequate / deficient) with supporting rationale

## Quality Checks

- Every valuation methodology referenced in the opinion is individually assessed — none are accepted at face value
- Implied value ranges are independently reconstructed or verified, not simply restated from the opinion
- Discount rate components are traced to named sources (e.g., Kroll Cost of Capital Guide, Bloomberg beta) and checked for internal consistency
- Comparable company and transaction selections are evaluated for relevance — stale comps (>24 months) or off-sector comps are flagged
- The analysis distinguishes between the advisor's role as opinion provider versus transaction advisor, and notes any dual-role concerns
- All jurisdiction- or regulation-dependent conclusions are marked with [VERIFY]
- Output avoids rendering a legal conclusion on fiduciary duty compliance — frames findings as financial analysis supporting board deliberation
