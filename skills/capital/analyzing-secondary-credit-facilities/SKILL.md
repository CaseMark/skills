---
name: analyzing-secondary-credit-facilities
description: Evaluates secondary-focused credit facilities with leverage terms, borrowing base mechanics, and portfolio pledging requirements. Use when analyzing secondary lending, structuring portfolio leverage, or evaluating fund finance options.
tags:
  - analysis
  - secondaries-and-gp-led
  - portfolio
  - credit
metadata:
  author: casemark
  practice_areas:
    - Secondaries
    - GP-Led Transactions
    - LP Portfolio Management
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Secondary Credit Facilities

Evaluates secondary-focused credit facilities with leverage terms, borrowing base mechanics, and portfolio pledging requirements.

## When To Use

- Reviewing a credit facility extended to a secondary fund or GP-led continuation vehicle
- Comparing leverage terms across competing lender proposals for a secondary portfolio acquisition
- Assessing borrowing base eligibility criteria and advance rates against a pledged LP interest portfolio
- Evaluating covenant packages, margin ratchets, and default triggers specific to secondary fund finance
- Structuring or re-sizing a facility ahead of a portfolio closing or capital call bridge

## Inputs To Gather

- **Credit agreement or term sheet** — full facility documentation including schedules and exhibits
- **Borrowing base certificate (template or recent)** — shows eligible collateral, advance rates, and concentration limits
- **Portfolio summary** — list of pledged LP interests or GP-led assets with NAV, vintage, strategy, and distribution history
- **Fund-level financials** — borrower's AUM, unfunded commitments, liquidity, and existing indebtedness
- **Lender proposal or commitment letter** — if pre-closing, captures indicative terms for comparison
- **Side letters or LP consent requirements** — any restrictions on pledge, transfer, or encumbrance of LP interests [VERIFY whether underlying LPAs restrict pledging]

## Workflow

1. **Map facility structure** — Identify the borrower entity, guarantors, pledged collateral pool, and lender syndicate. Confirm whether the facility is a subscription line (capital-call backed), NAV facility (asset-backed), or hybrid. Note the committed amount, accordion features, and maturity date.

2. **Analyze borrowing base mechanics**
   - List each category of eligible collateral (direct secondaries, GP-led interests, co-investments, deferred purchase price receivables)
   - Record advance rates per asset type — typical ranges: 40–65% for diversified secondary portfolios, 30–50% for concentrated GP-led positions [VERIFY current market advance rates with lender data]
   - Identify concentration limits (single-fund cap, single-GP cap, vintage limits, strategy limits)
   - Check for NAV decline triggers that force mandatory prepayment or borrowing base redetermination (common threshold: 15–25% NAV decline over a trailing period)

3. **Evaluate leverage and pricing terms**
   - Calculate headline leverage (facility size / NAV of pledged portfolio) and effective leverage (drawn amount / adjusted borrowing base)
   - Record interest rate structure: base rate (SOFR, prime) + applicable margin, floor rate, and any margin ratchet tied to utilization or LTV
   - Note commitment fees on undrawn amounts (typical: 25–50 bps), upfront fees, and arrangement fees
   - Compare all-in cost of leverage to expected portfolio IRR spread — flag if net spread is thin relative to risk

4. **Review covenant package**
   - **Financial covenants**: minimum NAV, maximum LTV ratio, minimum liquidity / cash-on-hand, distribution coverage ratio
   - **Portfolio covenants**: concentration limits, restrictions on asset dispositions or substitutions, required diversification metrics
   - **Reporting covenants**: frequency and detail of borrowing base certificates, quarterly NAV reports, audited financials
   - **Negative covenants**: restrictions on additional indebtedness, liens, affiliate transactions, change of control provisions
   - Flag any springing covenants or step-downs triggered by utilization thresholds

5. **Assess collateral and pledge mechanics**
   - Confirm perfection requirements — UCC filings on LP interests, account control agreements, notice to underlying GPs [VERIFY jurisdiction-specific perfection requirements for LP interest pledges]
   - Check whether underlying LPAs permit pledging and whether LP or GP consent is required
   - Identify "defaulting LP" provisions in underlying fund agreements that could impair collateral value
   - Review substitution and release mechanics — can the borrower swap pledged interests without lender consent?

6. **Stress-test the facility**
   - Model borrowing base under a 20% and 40% NAV decline scenario — determine available headroom
   - Assess cash sweep and mandatory prepayment triggers under stress
   - Evaluate concentration risk: if the largest 3–5 positions are marked down, does the base breach minimums?
   - Consider distribution timing risk — if underlying fund distributions slow, can the borrower service the facility?

7. **Benchmark against market terms**
   - Compare advance rates, pricing, and covenants to recent secondary credit facility precedents
   - Note whether terms reflect the portfolio's quality (vintage diversification, GP quality, strategy mix) or are off-market
   - Identify negotiation leverage points — areas where the borrower may push for improved terms

## Output

Produce a structured analysis report containing:

- **Facility Overview Table** — borrower, lender(s), committed amount, maturity, facility type, key dates
- **Borrowing Base Summary** — eligible collateral categories, advance rates, concentration limits, current availability
- **Pricing and Fee Schedule** — margin, base rate, floors, commitment fees, all-in cost estimate
- **Covenant Matrix** — each covenant with threshold, current compliance status, and headroom
- **Stress Scenario Results** — borrowing base availability under 20% and 40% NAV decline, margin call or prepayment triggers
- **Key Findings and Risks** — top 3–5 risks (concentration, NAV volatility, LP consent gaps, liquidity mismatch)
- **Recommendations** — specific negotiation points or structural modifications to improve borrower position

## Quality Checks

- Verify that advance rates and concentration limits are correctly extracted from the borrowing base schedule — cross-reference against the credit agreement definitions section
- Confirm that all pledged LP interests are actually eligible under the facility's inclusion/exclusion criteria
- Ensure NAV figures used are from the most recent reporting period and note any lag (typically 60–90 days)
- Check that covenant compliance calculations match the methodology specified in the credit agreement (e.g., whether NAV is gross or net of recallable distributions)
- Validate that stress scenarios use internally consistent assumptions (e.g., correlated declines across similar vintage/strategy positions)
- Flag any [VERIFY] items where jurisdiction-specific rules, LP consent requirements, or current market benchmarks need confirmation
