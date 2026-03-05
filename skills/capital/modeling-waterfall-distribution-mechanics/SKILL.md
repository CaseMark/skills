---
name: modeling-waterfall-distribution-mechanics
description: Builds distribution waterfall models with European vs American style carry, preferred return accrual, and GP clawback calculation. Use when modeling distribution waterfalls, comparing carry structures, or calculating LP distributions.
tags:
  - modeling
  - fund-formation-and-structuring
metadata:
  author: casemark
  practice_areas:
    - Fund Formation
    - Fund Structuring
    - Partnership Law
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Waterfall Distribution Mechanics

## When To Use

- Modeling LP/GP economics for a new fund's LPA negotiation
- Comparing European (whole-fund) vs. American (deal-by-deal) carry structures
- Calculating preferred return accrual and catch-up splits under specific fund terms
- Projecting GP clawback exposure under downside scenarios
- Auditing an existing waterfall model against LPA language
- Preparing distribution examples for investor side letters or advisory committee presentations

## Inputs To Gather

- **Fund terms from LPA/term sheet**: committed capital, GP commitment percentage, management fee rate and basis (committed vs. invested), preferred return rate (compounding convention — annual, quarterly, continuous), carry percentage, catch-up split ratio
- **Waterfall structure type**: European (whole-fund) or American (deal-by-deal), or hybrid
- **Catch-up provisions**: full catch-up (100/0) vs. partial (e.g., 80/20), and whether catch-up is capped
- **Return of capital definition**: whether return of capital includes recycled proceeds, management fee offsets, or only invested capital [VERIFY against LPA Section on Distributions]
- **Clawback terms**: GP clawback trigger, tax gross-up treatment, escrow/holdback percentage, timing of true-up (interim vs. final liquidation)
- **Cash flow projections**: investment amounts by period, projected realization proceeds and timing, interim income (dividends, interest)
- **Fee economics**: management fee schedule (step-down timing), organizational expenses cap, fee offsets from portfolio company monitoring/transaction fees

## Workflow

1. **Map the waterfall tiers from the LPA**
   - Tier 1: Return of capital (confirm whether this means contributed capital, invested capital, or contributed capital plus allocable fees/expenses) [VERIFY]
   - Tier 2: Preferred return accrual — calculate on unreturned capital at the stated rate; confirm compounding convention and day-count basis
   - Tier 3: GP catch-up — model the split (commonly 100% to GP until GP has received its carry share of all cumulative profits, or a partial catch-up ratio)
   - Tier 4: Carried interest split (typically 80/20 LP/GP after catch-up is satisfied)
   - Note: Some LPAs include additional tiers (e.g., super-carry above a second hurdle). Capture any non-standard tiers explicitly.

2. **Build the period-by-period cash flow model**
   - For **European style**: aggregate all contributions and distributions across the fund life; carry is only calculated and distributed after all invested capital plus preferred return is returned to LPs on a cumulative, whole-fund basis
   - For **American style**: calculate carry on each realized investment independently; track a running "loss account" or "netting mechanism" where losses on prior deals reduce carry on subsequent deals [VERIFY netting terms in LPA]
   - Track cumulative contributions, cumulative distributions, unreturned capital balance, and accrued preferred return balance at each period

3. **Model the preferred return accrual**
   - Compound at the LPA-specified rate on unreturned capital
   - Reduce the accrual balance as distributions are applied (confirm order of application: return of capital first, then preferred return, or blended)
   - For quarterly compounding on an 8% annual hurdle: apply 2% per quarter to the unreturned capital balance

4. **Calculate catch-up distributions**
   - After LPs have received return of capital plus preferred return, GP receives catch-up distributions
   - Full catch-up: 100% of next distributions flow to GP until GP's cumulative carry equals its carried interest percentage of total profits
   - Partial catch-up (e.g., 80/20): distributions split 80% GP / 20% LP until the same threshold is met
   - Formula check: at the catch-up completion point, GP's cumulative distributions should equal (carry %) x (total cumulative profits)

5. **Model GP clawback exposure**
   - For American-style waterfalls: after each distribution, calculate the hypothetical position as if the fund liquidated at that moment
   - Clawback = amount by which GP's cumulative carry exceeds what it would have earned under a whole-fund calculation
   - Apply any escrow/holdback (commonly 20-50% of carry distributions held back) [VERIFY holdback percentage]
   - Model tax gross-up if applicable — GP clawback is typically net of taxes deemed paid on prior carry distributions

6. **Run scenario and sensitivity analysis**
   - Base case, upside (+20% proceeds), and downside (-30% proceeds) on realization values
   - Vary realization timing (early exits vs. extended holds) to show impact on preferred return accrual
   - Compare European vs. American outcomes on identical cash flows to quantify the economic difference
   - Stress-test clawback exposure under loss-last scenarios (profitable deals exit first, losers remain)

## Output

- **Waterfall summary table**: period-by-period rows showing contributions, distributions, LP share, GP share, preferred return balance, and cumulative multiples (TVPI, DPI, RVPI)
- **Carry comparison schedule**: side-by-side European vs. American carry under base-case projections (if both structures are being evaluated)
- **GP clawback analysis**: maximum clawback exposure by period, net of escrow/holdback, with tax gross-up impact
- **Sensitivity matrix**: net carry to GP and net multiple to LPs across 3-5 scenarios
- **Assumptions register**: all inputs, compounding conventions, and LPA section references documented in a single tab/section

## Quality Checks

- **Reconciliation**: total distributions to LP + total distributions to GP must equal total fund proceeds in every period
- **Preferred return verification**: at the point carry begins, confirm LPs have received exactly their contributed capital plus compounded preferred return
- **Catch-up math**: at catch-up completion, verify GP cumulative carry = (carry %) x (cumulative distributions - cumulative contributions)
- **Clawback floor**: GP clawback should never exceed cumulative carry distributions received (net of tax gross-up)
- **Cross-check**: run the model with a single investment returning exactly 1.0x to confirm zero carry is paid
- **LPA conformance**: every formula and tier boundary should trace to a specific LPA section — flag any ambiguity with [VERIFY]
