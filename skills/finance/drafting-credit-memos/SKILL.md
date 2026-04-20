---
name: drafting-credit-memos
language: en
description: Creates structured credit memos with borrower analysis, risk assessment, and recommendation justification. Use when writing credit memos, documenting credit decisions, or presenting credit recommendations.
tags:
  - drafting
  - fixed-income
  - risk
  - credit
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Draft Document
  skill_modes:
    - Drafting
---
# Drafting Credit Memos

## When To Use

- Recommending a new bond purchase, loan participation, or credit facility for a portfolio or credit committee
- Documenting the rationale for increasing, reducing, or maintaining an existing credit exposure
- Presenting a credit opinion on a new issuer or counterparty for internal approval
- Refreshing an annual or semi-annual credit review on a held position
- Supporting a rating change recommendation (upgrade, downgrade, or watch placement)

## Inputs To Gather

- **Issuer/borrower identity**: Legal name, ticker, CUSIP/ISIN, sector classification (GICS or internal taxonomy)
- **Financial statements**: Minimum three years of audited financials plus latest interim period; confirm GAAP vs. IFRS basis
- **Capital structure detail**: Debt schedule with maturities, coupon rates, seniority, covenants, and guarantor structure
- **Market data**: Current spread levels (OAS, Z-spread, or CDS), comparable issuer spreads, recent price action
- **Rating agency views**: Moody's/S&P/Fitch ratings, outlooks, and most recent rating action commentary
- **Industry context**: Sector fundamentals, competitive positioning, key risk drivers (commodity exposure, regulatory, cyclicality)
- **Transaction specifics** (if new issue): Proposed terms, use of proceeds, pricing guidance, syndicate structure
- **Portfolio context**: Current exposure, concentration limits, mandate guidelines, and any investment policy constraints [VERIFY]

## Workflow

1. **Confirm scope and recommendation direction**
   - Clarify whether memo is for new investment, annual review, or event-driven reassessment
   - Identify the target audience (credit committee, portfolio manager, trading desk)
   - Determine recommendation type: Buy / Hold / Sell / Avoid, with size and tenor guidance

2. **Build the issuer profile**
   - Summarize business description: revenue mix, geographic footprint, market position
   - Identify the 3-5 key credit drivers (e.g., leverage trajectory, margin stability, asset quality, liquidity, management track record)
   - Note ownership structure and any parent/subsidiary support or structural subordination

3. **Conduct financial analysis**
   - Compute and trend core credit metrics: Debt/EBITDA, Interest Coverage (EBITDA/Interest), FFO/Debt, FCF generation
   - Adjust for off-balance-sheet obligations, operating leases (if pre-IFRS 16 comparisons needed), and non-recurring items — flag each adjustment explicitly
   - Stress-test metrics under a downside scenario (revenue decline of X%, margin compression of Y bps) and identify the break-even deterioration level
   - Compare metrics against rating agency medians for the assigned rating category [VERIFY agency-specific methodology]

4. **Assess capital structure and recovery**
   - Map the priority-of-claims waterfall: secured → senior unsecured → subordinated → equity
   - Estimate recovery prospects by tranche using enterprise value or asset-based approach
   - Flag covenant protections or weaknesses (incurrence vs. maintenance tests, restricted payments baskets, change-of-control provisions)

5. **Evaluate relative value**
   - Compare spread to sector peers at similar rating, maturity, and seniority
   - Assess whether current spread compensates for identified risks vs. comparables
   - Note any technical factors: index eligibility, supply/demand dynamics, event catalysts

6. **Formulate recommendation**
   - State recommendation clearly: action (Buy/Hold/Sell), notional size, target spread or price, and investment horizon
   - Summarize supporting thesis in 2-3 sentences
   - List key risks to the recommendation and monitoring triggers (e.g., leverage exceeding 4.5x, downgrade to below-IG)

7. **Draft the memo**
   - Use the output structure below
   - Write in direct, declarative style — lead each section with the conclusion, then support with data
   - Mark any unverified data points with [VERIFY]

## Output

Structure the credit memo with these sections:

1. **Executive Summary** — Recommendation, issuer name, rating, key metric snapshot, and 2-3 sentence thesis
2. **Issuer Overview** — Business description, revenue breakdown, competitive position, ownership
3. **Industry & Macro Context** — Sector trends, regulatory environment, cyclical positioning
4. **Financial Analysis** — Historical and projected metrics table, adjustment notes, stress scenario results
5. **Capital Structure & Recovery** — Debt maturity profile, priority waterfall, covenant summary
6. **Relative Value** — Spread comparison table vs. peers, technical factors
7. **Risk Factors** — Ranked list of 3-5 material risks with severity assessment
8. **Recommendation & Monitoring** — Actionable conclusion, position sizing rationale, triggers for review
9. **Appendix** — Detailed financial tables, source list, rating history

## Quality Checks

- All credit metrics tie back to sourced financials; no computed ratio is left without its inputs shown
- Recommendation is internally consistent — risk factors do not contradict the thesis without explicit acknowledgment
- Covenant analysis references actual indenture or credit agreement language, not summaries [VERIFY document availability]
- Peer comparison uses issuers of genuinely comparable credit profile (same sector, similar rating band, comparable maturity)
- Stress scenario assumptions are stated and plausible, not arbitrary round-number shocks
- Spread and pricing data carry timestamps — stale data is flagged
- Portfolio limit compliance is confirmed against current mandate or IPS guidelines [VERIFY specific fund constraints]
- No rating agency content is reproduced verbatim beyond fair-use thresholds; paraphrase and cite
