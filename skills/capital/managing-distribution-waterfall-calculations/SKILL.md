---
name: managing-distribution-waterfall-calculations
language: en
description: Executes distribution calculations through partnership waterfall with preferred return, GP catch-up, and carried interest allocation. Use when calculating distributions, processing waterfall mechanics, or determining carry payments.
tags:
  - management
  - investor-relations-and-lp-reporting
metadata:
  author: casemark
  practice_areas:
    - Investor Relations
    - LP Reporting
    - Fund Administration
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Distribution Waterfall Calculations

Executes distribution calculations through partnership waterfall with preferred return, GP catch-up, and carried interest allocation.

## When To Use

- Processing a realization event (asset sale, refinancing proceeds, dividend recap) that triggers LP/GP distributions
- Running quarterly or annual waterfall calculations for investor reporting
- Modeling prospective distributions for a pending exit
- Reconciling prior distributions against cumulative waterfall tiers
- Responding to LP inquiries about carry accrual or distribution allocations

## Inputs To Gather

- **LPA waterfall provisions** — exact tier structure, preferred return rate, catch-up percentage, carry split, and any clawback or giveback language [VERIFY against the specific fund's LPA]
- **Capital account data** — each LP's committed capital, contributed capital, and unfunded commitments
- **Prior distribution history** — cumulative distributions by partner, broken out by return of capital vs. profit
- **Current distributable amount** — net proceeds available after transaction costs, reserves, and GP-level holdbacks
- **Preferred return parameters** — rate (e.g., 8% IRR or 8% cumulative compounded), compounding frequency, accrual start date (funding date vs. commitment date) [VERIFY compounding convention]
- **GP commitment details** — GP co-invest amount and whether GP participates pro rata through the waterfall or only at the carry tier
- **Reserve and holdback amounts** — tax withholding, escrow holdbacks, contingency reserves

## Workflow

1. **Validate capital accounts**
   - Confirm each partner's contributed capital, prior distributions (ROCR vs. profit), and net funded amount
   - Reconcile against the fund administrator's records; flag any discrepancies as [VERIFY]

2. **Determine distributable proceeds**
   - Start with gross realization proceeds
   - Deduct transaction expenses, organizational expense recoupment (if applicable), and management fee offsets
   - Set aside approved reserves (escrow, tax withholding, contingency)
   - Resulting figure = net distributable amount

3. **Run Tier 1 — Return of Capital**
   - Allocate distributions to LPs (and GP co-invest) until each partner has received cumulative distributions equal to their contributed capital
   - Track remaining distributable amount after Tier 1 is satisfied

4. **Run Tier 2 — Preferred Return**
   - Calculate accrued preferred return for each partner based on LPA terms (IRR-based or cumulative compounded)
   - For IRR-based waterfalls: solve for the distribution amount that brings each partner's IRR to the hurdle rate on contributed capital, netting prior profit distributions
   - For cumulative-compounded waterfalls: compute accrued preferred on outstanding capital balances from each drawdown date, less prior preferred distributions
   - Allocate available proceeds to satisfy accrued preferred; if insufficient, allocate pro rata among partners based on their respective unpaid preferred amounts

5. **Run Tier 3 — GP Catch-Up**
   - After preferred return is fully satisfied, allocate proceeds to the GP until the GP has received its stated share (commonly 20%) of all cumulative profits distributed (Tiers 2 + 3 combined)
   - Determine if catch-up is 100% to GP or a blended split (e.g., 80/20) [VERIFY catch-up formula in LPA]
   - If distributable amount is insufficient to complete catch-up, allocate the entire remaining amount to the GP per LPA terms

6. **Run Tier 4 — Carried Interest Split**
   - Allocate remaining proceeds according to the stated profit split (e.g., 80% LP / 20% GP carry)
   - Apply any tiered carry structure if applicable (e.g., carry increases to 25% above a second hurdle) [VERIFY whether multi-tier carry applies]

7. **Allocate across individual partners**
   - Distribute LP-level amounts pro rata based on each LP's share of aggregate LP commitments (or contributed capital, per LPA)
   - Apply any LP-specific side letter economics (fee discounts, carry reductions, co-invest offsets) [VERIFY side letter terms]

8. **Reconcile and cross-check**
   - Confirm total distributions across all partners equals the net distributable amount
   - Verify cumulative waterfall position: which tiers are fully satisfied, partially satisfied, or unsatisfied
   - Run a reverse check — compute implied net IRR and equity multiple for LPs to validate reasonableness

## Output

- **Distribution waterfall schedule** — tier-by-tier allocation table showing current-period and cumulative amounts per tier
- **Partner-level distribution notice** — each partner's allocated distribution broken into return of capital and profit components
- **Carry calculation summary** — GP carried interest earned in the current period, cumulative carry to date, and any carry reserve or clawback exposure
- **Waterfall status tracker** — current position in the waterfall (e.g., "Tier 2: Preferred Return — 62% satisfied") with remaining amounts to clear each tier
- **Tax character breakdown** — allocation of distributions by tax character (capital gain vs. ordinary income) if tax data is available [VERIFY with fund tax advisor]

## Quality Checks

- All partner distributions sum exactly to the net distributable amount (zero residual)
- Preferred return calculations use the correct compounding convention and day-count basis per the LPA
- GP catch-up allocation does not exceed the amount required to reach the stated carry percentage of total profits
- Prior distributions are correctly credited against each waterfall tier before applying current proceeds
- Side letter adjustments are applied only to the affected LP and do not alter aggregate economics for other partners
- Clawback exposure is flagged if cumulative GP carry exceeds what a whole-fund lookback would produce [VERIFY clawback methodology]
- Distribution amounts reconcile with the fund administrator's independent calculation before release
