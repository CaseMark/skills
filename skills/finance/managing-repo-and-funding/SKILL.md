---
name: managing-repo-and-funding
language: en
description: Structures repo market analysis with collateral valuation, haircut assessment, and funding cost optimization. Use when managing repo positions, evaluating collateral, or optimizing funding costs.
tags:
  - management
  - fixed-income
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Fixed Income
    - Credit Research
    - Bond Trading
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Repo And Funding

## When To Use

- Evaluating existing repo book positions for collateral adequacy, tenor mismatch, or counterparty concentration
- Assessing haircuts on specific collateral classes (Treasuries, agencies, corporates, ABS/MBS, equities)
- Optimizing overnight vs. term funding costs across bilateral and tri-party channels
- Preparing margin call or substitution analysis when collateral values shift
- Modeling funding ladder scenarios for liquidity stress testing
- Reviewing counterparty credit exposure within the repo portfolio

## Inputs To Gather

- **Position data**: Outstanding repo and reverse-repo balances by counterparty, tenor bucket, and collateral type
- **Collateral schedule**: CUSIP/ISIN-level holdings pledged or received, with current market values and accrued interest
- **Haircut tables**: Applicable haircut percentages by collateral type, credit rating, and remaining maturity — source from FICC/GSD schedules, prime broker margin grids, or internal risk policy [VERIFY: confirm haircut source matches governing agreement — GMRA, MRA, or tri-party schedule]
- **Funding rate benchmarks**: SOFR, Fed Funds effective, tri-party GC rates, and any term SOFR fixings relevant to the book
- **Counterparty limits**: Approved credit lines, concentration caps, and netting eligibility per counterparty
- **Maturity ladder**: Roll dates, open vs. term positions, and any evergreen structures with termination notice periods

## Workflow

1. **Map the repo book**
   - Aggregate positions by collateral type (govts, agencies, IG corporates, HY/unrated, structured)
   - Segment by tenor: overnight/open, 1-week, 1-month, 3-month, term >3 months
   - Tag each trade as bilateral, tri-party (BNY, JPM, etc.), or GCF/FICC-cleared [VERIFY: clearing status and CCP membership]

2. **Assess collateral valuation and haircuts**
   - Mark collateral to current market prices; include accrued interest for coupon-bearing securities
   - Compare applied haircuts against governing schedule — flag any collateral trading below investment grade or approaching downgrade watch
   - Calculate net exposure per counterparty: (collateral market value × (1 − haircut)) − repo principal
   - Identify margin deficit or surplus positions; flag any exceeding the minimum transfer amount (MTA)

3. **Analyze funding costs**
   - Compute weighted-average repo rate across the book, broken out by collateral type and tenor
   - Benchmark against SOFR (overnight), term SOFR (for term trades), and GC composite rates
   - Quantify spread to benchmark: positive spread = funding at a premium; negative = favorable funding
   - Identify "specials" trading meaningfully below GC — note the specific issues and the basis-point spread

4. **Evaluate concentration and rollover risk**
   - Check single-counterparty exposure against credit limits and regulatory large-exposure thresholds [VERIFY: applicable regulatory framework — Basel III, SEC Rule 15c3-1, or internal policy]
   - Assess maturity concentration: what percentage of funding rolls within 1 day, 1 week, 30 days
   - Model a stress scenario where the largest counterparty or collateral class is unavailable — quantify the funding gap

5. **Optimize and recommend**
   - Identify substitution opportunities: swap higher-haircut collateral for lower-haircut eligible securities to free up balance sheet
   - Recommend tenor extension for positions rolling overnight if term funding is available at acceptable spread
   - Flag opportunities to move bilateral trades to cleared (FICC-sponsored) for capital relief
   - Propose counterparty diversification where concentration limits are approaching thresholds

## Output

The final management report should include:

- **Position summary table**: Columns for counterparty, direction (repo/reverse), collateral type, principal, market value, haircut %, net exposure, maturity date, and rate
- **Funding cost dashboard**: Weighted-average rate by collateral bucket vs. benchmark, with trend vs. prior period
- **Haircut adequacy matrix**: Current haircuts vs. policy/schedule requirements, with exceptions highlighted
- **Concentration heat map**: Counterparty and collateral-type exposure as percentage of total book and of approved limits
- **Risk flags**: Margin calls pending, collateral on downgrade watch, tenor mismatches exceeding policy, or positions approaching regulatory thresholds
- **Action items**: Specific substitution, extension, or diversification trades recommended with estimated cost/benefit

## Quality Checks

- Verify all collateral market values are as-of the same pricing snapshot (T or T-1 close) — mixed dates distort haircut adequacy
- Confirm haircut percentages match the operative agreement for each counterparty (GMRA Annex I, MRA Schedule, or tri-party eligibility profile)
- Cross-check repo rates against published SOFR/GC benchmarks for reasonableness — rates deviating >25 bps from GC without a specials explanation warrant review
- Ensure netting is applied only where a valid netting opinion or ISDA/GMRA close-out netting clause exists [VERIFY: netting enforceability per jurisdiction]
- Validate that concentration metrics use correct denominator (total repo book, not total firm assets) unless policy specifies otherwise
- Confirm all open/evergreen positions reflect correct termination notice periods in the maturity ladder
