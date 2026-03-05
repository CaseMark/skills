---
name: analyzing-leveraged-loans
description: Structures leveraged loan analysis with covenant assessment, amendment tracking, and repricing risk. Use when analyzing leveraged loans, reviewing loan covenants, or evaluating loan market dynamics.
tags:
  - analysis
  - fixed-income
  - risk
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Leveraged Loans

Structures leveraged loan analysis covering credit facility terms, covenant packages, amendment activity, repricing risk, and relative value positioning within the broadly syndicated and middle-market loan universe.

## When To Use

- Evaluating a new leveraged loan for purchase or participation in primary syndication
- Reviewing an existing portfolio holding after an amendment, repricing, or credit event
- Comparing covenant packages across issuers or vintages
- Assessing repricing and refinancing risk for floating-rate loan positions
- Analyzing CLO eligibility and secondary market liquidity for a given facility

## Inputs To Gather

- **Credit agreement or term sheet** — full document or summary of key terms (facility size, maturity, spread, OID, floor, call protection)
- **Financial statements** — at least two periods of income statement, balance sheet, and cash flow to compute leverage and coverage metrics
- **Amendment/waiver history** — any consent solicitations, repricings, or covenant modifications since closing
- **Market data** — current bid/ask levels, loan index spreads (e.g., Morningstar LSTA index), and comparable loan pricing
- **Rating agency reports** — facility and corporate family ratings from Moody's/S&P/Fitch, including outlooks
- **Borrower context** — industry, sponsor (if PE-backed), capital structure diagram, and any pending M&A or dividend recap activity

## Workflow

1. **Map the capital structure** — Identify all debt tranches (revolver, TL-A, TL-B, second lien, unsecured), their relative priority, and any structural subordination across entities. Calculate attachment and detachment points for loss-given-default estimation.

2. **Compute credit metrics** — Calculate Total Debt / EBITDA, Secured Debt / EBITDA, Interest Coverage (EBITDA / Cash Interest), and Fixed Charge Coverage. Use both reported EBITDA and an adjusted figure that strips out non-recurring add-backs. Flag add-backs exceeding 20-25% of unadjusted EBITDA as aggressive. [VERIFY] whether the credit agreement uses a trailing, pro forma, or run-rate EBITDA definition.

3. **Analyze the covenant package** — Determine whether the loan is covenant-lite (incurrence-only) or has maintenance covenants. For cov-lite deals, review:
   - Restricted payments and debt incurrence baskets (fixed-dollar vs. ratio-based)
   - Permitted investments and the "Available Amount" builder basket
   - Asset sale sweep percentages and reinvestment periods
   - Change-of-control provisions and portability language
   - J. Crew / Chewy-style trapdoor provisions allowing IP or asset transfers to unrestricted subsidiaries

4. **Assess amendment and repricing history** — Review any amendments since closing: covenant holidays, EBITDA definition changes, basket expansions, maturity extensions, or spread reductions. Evaluate whether amendments were borrower-friendly erosions or neutral technical fixes. Note any "amend-and-extend" transactions and the resulting maturity profile.

5. **Evaluate repricing and call risk** — Check soft-call protection periods (typically 6-12 months at 101). Assess likelihood of repricing given current spread relative to new-issue clearing levels. A loan trading above par with spread significantly above the current market for comparable credits has elevated repricing risk, compressing upside.

6. **Run relative value comparison** — Compare spread, OID, leverage, rating, and sector against a peer set of 5-10 comparable loans. Compute spread-per-turn-of-leverage to normalize value across different capital structures. Assess whether the loan prices to its rating, or if a dislocation exists.

7. **Evaluate CLO and technical factors** — Determine CLO eligibility (CCC bucket limits, minimum spread/coupon tests, weighted average life constraints). Assess whether the borrower is a frequent CLO holding, which supports secondary liquidity. Note upcoming CLO reinvestment period expirations that could reduce demand.

## Output

Produce a structured leveraged loan analysis containing:

- **Executive summary** — One-paragraph investment thesis: buy/hold/sell recommendation with key drivers
- **Capital structure table** — All tranches with size, rate, maturity, and priority
- **Credit metrics dashboard** — Leverage, coverage, and free cash flow metrics over the last 2-4 quarters with trend arrows
- **Covenant scorecard** — Red/yellow/green assessment of key basket and provision quality relative to market norms
- **Amendment timeline** — Chronological list of material amendments with borrower-impact assessment
- **Repricing risk gauge** — Low/medium/high based on call protection status, spread-to-market gap, and borrower credit trajectory
- **Relative value matrix** — Peer comparison table with spread, leverage, rating, and spread-per-turn
- **Risk factors** — Top 3-5 downside catalysts (earnings deterioration, sponsor dividend, sector headwinds, refinancing wall)

## Quality Checks

- Verify that EBITDA adjustments reconcile to the credit agreement's defined add-backs, not management's investor presentation figures
- Confirm leverage calculations use the same netting conventions (gross vs. net of cash) as the covenant definitions
- Cross-check market pricing against at least two sources (e.g., MarketAxess, LSTA/LPC, dealer runs) [VERIFY]
- Ensure amendment analysis references the actual amendment text, not just press coverage or rating agency summaries
- Validate that CLO eligibility assessment reflects current Volcker and risk-retention requirements [VERIFY]
- Flag any situation where the borrower is approaching the outer edge of incurrence baskets, as this may signal future aggressive liability management
