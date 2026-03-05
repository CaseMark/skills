---
name: analyzing-covenant-packages
description: Evaluates financial and incurrence covenant packages with headroom analysis, definition review, and covenant-lite comparison. Use when analyzing loan covenants, negotiating covenant levels, or assessing borrower flexibility.
tags:
  - analysis
  - debt-capital-markets
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
# Analyzing Covenant Packages

## When To Use

- Reviewing a credit agreement or term sheet to assess borrower flexibility and lender protections
- Comparing covenant packages across competing deal proposals or precedent transactions
- Calculating headroom on maintenance covenants against projected financials
- Evaluating a covenant-lite structure versus a traditional maintenance-covenant package
- Advising on covenant negotiation strategy for new issuances, amendments, or refinancings

## Inputs To Gather

- **Credit agreement or term sheet** — full covenant section including definitions
- **Financial model or projections** — at minimum: revenue, EBITDA, total debt, capex, interest expense, and cash flow forecasts over the covenant testing horizon
- **Borrower's historical financials** — trailing 4–8 quarters of actuals for trend context
- **Precedent deal comps** — covenant packages from comparable credits (same sector, rating, leverage profile)
- **EBITDA definition details** — addbacks schedule, pro forma adjustment language, run-rate cost savings caps
- **Basket and builder schedules** — restricted payments, permitted investments, permitted debt capacity

## Workflow

1. **Map the covenant architecture**
   - Classify each covenant as maintenance (tested periodically) or incurrence (tested at transaction)
   - List all financial covenants: leverage ratio, interest coverage, fixed charge coverage, minimum EBITDA, capex limits, etc.
   - Identify testing frequency, cure rights, and equity cure mechanics if present

2. **Deconstruct EBITDA and key definitions**
   - Parse the Consolidated EBITDA definition for addback categories: restructuring charges, non-cash items, transaction costs, run-rate synergies, pro forma cost savings
   - Flag any uncapped or loosely capped addbacks — note the percentage-of-EBITDA cap (commonly 15–25%) or absence thereof [VERIFY against specific agreement]
   - Compare the definition against LMA/LSTA standard forms to identify borrower-favorable deviations

3. **Calculate covenant headroom**
   - For each maintenance covenant, compute the ratio using both reported EBITDA and adjusted EBITDA (stripping discretionary addbacks)
   - Project headroom quarter-by-quarter against the financial model: headroom = (covenant threshold − projected ratio) / covenant threshold
   - Stress-test headroom under downside scenarios (e.g., 10%, 20%, 30% EBITDA decline) to identify the quarter of first breach
   - If equity cure exists, quantify the cure amount needed per scenario

4. **Analyze negative covenants and baskets**
   - Map restricted payments capacity: fixed baskets, builder baskets (typically 50% of cumulative consolidated net income), available amount mechanics
   - Assess permitted debt capacity: ratio-based incurrence tests, fixed-dollar carveouts, incremental facility terms (MFN protections, maturity constraints, inside maturity limits)
   - Review permitted investments, asset sale reinvestment periods, and J-crew / Chewy-style trapdoor provisions for unrestricted subsidiary transfers

5. **Benchmark against covenant-lite and precedent deals**
   - Score the package on a maintenance-to-cov-lite spectrum: full maintenance → springing revolver only → pure incurrence
   - Compare individual covenant levels, EBITDA definition breadth, and basket sizes to 3–5 precedent transactions
   - Note any sunset provisions, portability features, or MFN step-downs

6. **Assess overall borrower flexibility vs. lender protection**
   - Summarize where the package sits relative to market: tight, market, or aggressive
   - Identify the covenants or definitions most likely to be negotiation flashpoints
   - Flag provisions that could enable value leakage or structural subordination

## Output

- **Covenant summary table** — each covenant with type, threshold, current level, and projected headroom by quarter
- **EBITDA definition markup** — addback categories with capped/uncapped status and comparison to standard forms
- **Headroom analysis** — base case and stress scenario projections showing quarters-to-breach
- **Basket capacity schedule** — restricted payments, permitted debt, and permitted investments with current available amounts
- **Covenant-lite comparison matrix** — side-by-side against 3–5 precedent deals on key dimensions
- **Negotiation risk flags** — ranked list of provisions requiring attention, with suggested market-based counterpositions

## Quality Checks

- Confirm all ratio calculations use the agreement's specific definitions (not generic textbook formulas) — numerator and denominator components must match the credit agreement
- Verify that EBITDA addback analysis accounts for interaction effects (e.g., capped addbacks applied before or after other adjustments) [VERIFY]
- Cross-check headroom projections against the financial model's own covenant compliance tab if available
- Ensure basket analysis reflects all builder basket components, including contribution debt and excluded contribution carveouts
- Validate that precedent comps are genuinely comparable: same credit rating band, similar leverage, same broad sector, and originated within relevant market window [VERIFY vintage within 12–18 months]
- Flag any provisions where jurisdiction-specific law affects enforceability (e.g., fraudulent conveyance limitations on upstream guarantees, local law restrictions on security packages) [VERIFY by jurisdiction]
