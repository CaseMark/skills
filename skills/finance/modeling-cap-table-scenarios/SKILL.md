---
name: modeling-cap-table-scenarios
description: Builds cap table models with round-by-round dilution, option pool, and exit waterfall analysis. Use when modeling cap tables, calculating ownership dilution, or projecting exit proceeds.
tags:
  - modeling
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Venture Capital
    - Growth Equity
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Cap Table Scenarios

Builds cap table models with round-by-round dilution, option pool, and exit waterfall analysis.

## When To Use

- Modeling ownership stakes across multiple financing rounds (Seed through Series D+)
- Calculating fully-diluted ownership including option pools, warrants, and convertible instruments
- Projecting exit waterfall proceeds under varying valuation scenarios
- Evaluating the dilutive impact of a proposed new round on existing shareholders
- Comparing term sheet offers by modeling their downstream cap table effects
- Assessing option pool sufficiency for hiring plans between rounds

## Inputs To Gather

- **Founding equity**: Shares issued to each founder, any vesting schedules or repurchase rights
- **Prior round details**: For each completed round — pre-money valuation, amount raised, price per share, share class, liquidation preference (multiple and participation), anti-dilution provisions [VERIFY exact preference terms from charter/COI]
- **Convertible instruments**: Outstanding SAFEs, convertible notes — principal, interest rate, maturity, valuation cap, discount rate, conversion triggers
- **Option pool**: Authorized pool size, shares granted, shares exercised, shares available; strike prices by grant vintage
- **Warrants**: Outstanding warrants with exercise price, expiration, and share class on exercise
- **Proposed round terms**: Pre-money valuation, round size, new option pool expansion (pre- or post-money), liquidation preference, participation cap, pay-to-play provisions
- **Exit assumptions**: Target exit valuation range, expected timing, transaction type (M&A vs. IPO)

## Workflow

1. **Build the pre-round cap table**
   - List all share classes (Common, Series Seed, Series A, etc.) with shares outstanding
   - Convert all outstanding convertible instruments at their applicable terms — apply valuation caps, discounts, and accrued interest [VERIFY conversion mechanics against each instrument's specific terms]
   - Include the current option pool (granted + available) in fully-diluted share count
   - Confirm the fully-diluted share count reconciles to the company's transfer agent or legal records

2. **Model the proposed round**
   - Calculate new shares issued: round size / price per share
   - If option pool expansion is required, determine whether the pool increase is pre-money (dilutes existing holders) or post-money (dilutes all including new investors)
   - Compute post-round fully-diluted shares and each holder's ownership percentage
   - Apply any anti-dilution adjustments to prior preferred rounds if the new round is a down round [VERIFY anti-dilution formula — broad-based weighted average vs. full ratchet]

3. **Construct the exit waterfall**
   - Define exit valuation scenarios (e.g., 0.5x, 1x, 2x, 3x, 5x, 10x of last post-money)
   - Apply liquidation preferences in seniority order — standard is last-in-first-out unless pari passu [VERIFY stacking order from charter documents]
   - For participating preferred: distribute remaining proceeds pro rata after preference recovery, applying any participation caps
   - For non-participating preferred: compare preference payout against as-converted common payout; holders take the higher amount
   - Allocate remaining proceeds to common and as-converted preferred pro rata
   - Calculate per-share proceeds and total dollar returns for each shareholder group at each exit level

4. **Run sensitivity analysis**
   - Vary pre-money valuation (+/- 20-30%) and show impact on founder dilution
   - Test different option pool sizes (e.g., 10%, 15%, 20% post-money)
   - Model participation vs. non-participation terms at various exit levels to identify the crossover point
   - If convertible instruments are present, show ownership impact at different cap/discount conversion scenarios

5. **Produce summary outputs**
   - Ownership summary table: each holder's shares, percentage (basic and fully-diluted), dollar value at proposed valuation
   - Round-by-round dilution waterfall showing cumulative dilution per founder/investor group
   - Exit proceeds table across valuation scenarios for each share class
   - Key metrics: effective price per share for each round, total capital raised, implied step-up multiples

## Output

Deliver a structured cap table model containing:

- **Ownership Table**: Shareholder name/group, share class, shares held, % ownership (basic), % ownership (fully-diluted), implied value at current round price
- **Dilution Waterfall**: Round-by-round view showing each financing event's dilutive impact on prior holders
- **Exit Waterfall Matrix**: Rows = shareholder groups, columns = exit valuation scenarios, cells = dollar proceeds and multiple on invested capital (MOIC)
- **Sensitivity Tables**: Key variable toggles (valuation, pool size, participation) with resulting ownership/proceeds changes
- **Assumptions Log**: Every assumption explicitly stated with source or [VERIFY] tag

Format numeric outputs with consistent precision (shares as whole numbers, percentages to two decimal places, dollar amounts to nearest dollar). Use clear column headers and group rows by share class.

## Quality Checks

- Fully-diluted shares across all holders sum to total authorized + issued shares — no orphaned or double-counted shares
- Ownership percentages sum to exactly 100.00% in each scenario
- Exit waterfall proceeds at each valuation level sum to the total exit value (no leakage)
- Liquidation preferences are applied in correct priority order and do not exceed total exit value at low valuations
- Convertible instrument conversions match the specific terms of each note/SAFE — do not apply a blanket conversion formula across instruments with different caps or discounts
- Anti-dilution adjustments are only triggered when the new round price is below the applicable threshold [VERIFY trigger prices per series]
- Option pool arithmetic: granted + exercised + available = total pool authorized
- Cross-check post-money valuation = pre-money + new money, and price per share = pre-money / pre-round fully-diluted shares (including any pool expansion)
