---
name: analyzing-life-insurance-products
description: Evaluates life insurance product structures with cash value analysis, cost comparisons, and suitability assessment. Use when analyzing life products, comparing insurance costs, or assessing product suitability.
tags:
  - analysis
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Life Insurance Products

Evaluates life insurance product structures including term, whole life, universal life (UL), indexed UL, and variable UL, with cash value projections, cost-of-insurance analysis, and suitability assessment relative to client objectives.

## When To Use

- Comparing product structures across carriers or product types for a specific client profile
- Evaluating in-force policy performance against original illustrations
- Assessing cash value accumulation efficiency and cost-of-insurance trends
- Reviewing product suitability for estate planning, income replacement, or wealth transfer
- Analyzing policy replacement proposals (1035 exchange scenarios)
- Auditing illustration assumptions (credited rates, persistency, lapse risk)

## Inputs To Gather

- **Policy documents**: Illustration ledgers, in-force summaries, policy contracts, riders
- **Client profile**: Age, health classification (preferred/standard/rated), gender, tobacco status, state of issue
- **Objective**: Death benefit need, cash accumulation target, premium budget, planning horizon
- **Existing coverage**: Current policies, surrender values, outstanding loans, cost basis
- **Carrier data**: Financial strength ratings (AM Best, S&P, Moody's), general account allocation, crediting rate history
- **Benchmarks**: Comparable products or industry cost indices (e.g., Belth method, surrender cost index, net payment cost index)

## Workflow

1. **Classify the product type** — Identify whether term, whole life, UL, IUL, VUL, or hybrid (e.g., life/LTC combo). Note guaranteed vs. non-guaranteed elements and the general account vs. separate account structure.

2. **Extract cost-of-insurance (COI) charges** — Pull COI rates from the contract or illustration. Compare current COI charges against guaranteed maximums. Flag products where current rates are close to guaranteed ceilings. [VERIFY] COI rate schedules vary by carrier and may be subject to periodic adjustment.

3. **Analyze cash value projections** — Run or review illustrations at multiple crediting rate assumptions:
   - Guaranteed minimum rate
   - Current declared/credited rate
   - Midpoint scenario
   - For IUL: floor, cap, participation rate, and historical back-tested returns
   - Identify the crossover year where cash value exceeds cumulative premiums

4. **Evaluate premium structure** — Determine whether the product is funded at target, minimum, or maximum non-MEC levels. Assess MEC risk under IRC §7702A. Calculate the spread between minimum premium to maintain coverage and the planned premium.

5. **Compare costs across products** — Use standardized cost indices:
   - **Surrender cost index**: Net cost per $1,000 of coverage if policy is surrendered at benchmark durations (10, 20, 30 years)
   - **Net payment cost index**: Net cost per $1,000 if held to death at benchmark durations
   - **Belth yearly rate of return method**: Isolates the implied cost of insurance per year
   - Normalize for differences in death benefit design (level vs. increasing)

6. **Assess suitability** — Match product features against client needs:
   - Income replacement → level term or guaranteed UL with secondary guarantees
   - Estate liquidity → survivorship (second-to-die) whole life or guaranteed UL
   - Cash accumulation → overfunded IUL or VUL (assess cap/floor trade-offs)
   - Business succession → key person term or whole life with split-dollar arrangement
   - [VERIFY] State-specific suitability requirements and replacement regulations (e.g., NAIC Model Replacement Regulation)

7. **Review carrier financial strength** — Confirm AM Best rating (A or better typical threshold), surplus growth, RBC ratio, and general account investment quality. For products with long-duration guarantees, carrier stability is critical.

8. **Flag risks and assumptions** — Document sensitivity to interest rate changes, COI increases, policy loan arbitrage assumptions, and lapse-supported pricing. Identify any illustration assumptions that diverge from historical norms.

## Output

Structure the analysis report with:

- **Executive summary**: Product recommendation or comparison verdict in 2-3 sentences
- **Product comparison table**: Side-by-side matrix of premiums, death benefits, cash values at years 10/20/30, cost indices, and carrier ratings
- **Cash value projection chart**: Guaranteed vs. current vs. midpoint scenarios over the planning horizon
- **COI analysis**: Current vs. guaranteed rate trajectory with breakeven assessment
- **Suitability finding**: How each product aligns with stated client objectives
- **Risk factors**: Interest rate sensitivity, carrier risk, lapse risk, MEC risk
- **Recommendation**: Preferred product with rationale, or conditions under which each option is superior

## Quality Checks

- Verify all illustration ledger values tie to the carrier-provided documents — do not interpolate missing years
- Confirm premium mode (annual/semi/quarterly/monthly) is consistent across comparisons
- Ensure cost indices use the same benchmark durations and discount rates
- Validate that non-guaranteed elements are clearly labeled and separated from guarantees
- Check that MEC status is correctly determined under IRC §7702A seven-pay test
- Confirm carrier ratings are current (ratings change; mark with [VERIFY] if older than 12 months)
- Flag any illustration that assumes crediting rates materially above the carrier's 10-year historical average
- Note all state-specific regulatory requirements that may affect replacement or suitability determinations [VERIFY]
