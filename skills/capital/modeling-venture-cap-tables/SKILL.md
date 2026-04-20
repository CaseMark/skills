---
name: modeling-venture-cap-tables
language: en
description: Builds cap table models with round-by-round dilution, ESOP expansion, convertible note conversion, and exit waterfall analysis. Use when modeling cap tables, projecting ownership dilution, or calculating exit proceeds distribution.
tags:
  - modeling
  - venture-capital
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Venture Cap Tables

## When To Use

- Modeling a new priced round (Seed, Series A–D+) to project post-money ownership
- Converting SAFEs or convertible notes into equity at a triggering event
- Expanding or creating an ESOP pool and quantifying dilutive impact on existing holders
- Running exit waterfall scenarios (M&A, IPO, liquidation) to calculate per-share proceeds
- Preparing investor-facing ownership summaries for fundraising or board reporting

## Inputs To Gather

- **Current cap table**: Authorized shares, outstanding common shares by holder, preferred share classes with certificate of incorporation terms (liquidation preference multiple, participation rights, anti-dilution type)
- **ESOP details**: Pool size (authorized vs. issued vs. unallocated), vesting schedules, exercise prices, early-exercise provisions
- **Convertible instruments**: SAFE or note principal, accrued interest, valuation cap, discount rate, conversion trigger, MFN provisions, pro-rata side letters
- **Proposed round terms**: Pre-money valuation, new money invested, investor allocation, price per share, new ESOP pool target (pre- or post-money)
- **Exit assumptions** (if running waterfall): Total exit value range, transaction expenses, escrow/holdback, acceleration triggers for unvested options

Flag any missing instrument with [VERIFY] — an overlooked note or warrant can materially change dilution.

## Workflow

1. **Reconstruct the pre-round cap table**
   - List each holder class: founders (common), employees (options/RSAs), prior investors (preferred series), outstanding warrants, convertible instruments
   - Calculate fully-diluted share count using the treasury-stock method for in-the-money options
   - Confirm authorized-share headroom; flag if a charter amendment is needed [VERIFY]

2. **Model ESOP expansion (if applicable)**
   - Determine whether the new pool is carved from pre-money (founder-dilutive) or post-money (all-shareholder-dilutive)
   - Calculate shares needed: target pool % × post-money fully-diluted shares − existing unallocated pool
   - Show incremental dilution to each holder class

3. **Convert SAFEs and convertible notes**
   - For each instrument, compute the conversion price: lower of (valuation cap / pre-money fully-diluted shares) and (price per share × (1 − discount))
   - Add accrued interest to note principal before dividing by conversion price
   - Apply MFN adjustments if a later SAFE has more favorable terms [VERIFY specific SAFE form version]
   - Sum all conversion shares and add to fully-diluted count before pricing the new round (if pre-money conversion) or after (if post-money SAFE)

4. **Price the new round**
   - Pre-money valuation ÷ fully-diluted shares (including new ESOP and converted instruments) = price per share
   - New shares issued = new investment ÷ price per share
   - Post-money valuation = pre-money + new investment
   - Populate per-holder ownership on a fully-diluted and as-converted basis

5. **Build exit waterfall**
   - Layer 1: Return of liquidation preferences (non-participating preferred gets 1× or stated multiple; participating preferred gets preference + pro-rata)
   - Layer 2: If remaining proceeds exist, allocate pro-rata to common and participating preferred (subject to any cap on participation)
   - Layer 3: Compare conversion value vs. preference value for each preferred series — holders elect the higher payout
   - Model at multiple exit values (e.g., 0.5×, 1×, 2×, 5×, 10× of post-money) to show breakpoints where preferred converts

6. **Sensitivity and scenario analysis**
   - Vary pre-money valuation ±20% and show impact on founder dilution
   - Toggle participation vs. non-participation for latest preferred series
   - Show ESOP pool impact at 10%, 15%, 20% targets
   - If multiple convertible instruments exist, model conversion order impact

## Output

- **Summary ownership table**: Holder name, share class, shares held, % on as-converted fully-diluted basis — both pre-round and post-round columns
- **Conversion schedule**: Each SAFE/note with principal, cap, discount, conversion price, and shares issued
- **ESOP allocation table**: Authorized, issued, unallocated, and new shares created
- **Exit waterfall matrix**: Rows = holder classes, columns = exit value scenarios, cells = gross proceeds per class and per share
- **Key assumptions register**: Every assumed input listed with source or [VERIFY] flag

## Quality Checks

- Ownership percentages must sum to exactly 100% on every basis presented (issued, fully-diluted, as-converted)
- Post-money valuation must equal pre-money valuation + total new money (including converted instruments if priced in)
- Conversion prices must reflect the lower of cap-derived and discount-derived price — check both paths
- Liquidation waterfall total distributed must equal the exit value minus expenses at every scenario point
- Confirm anti-dilution provisions (broad-based weighted average vs. full ratchet) are applied correctly if a down round is modeled [VERIFY governing documents]
- Verify authorized share count supports all modeled issuances; flag if board/stockholder approval is required
- Cross-check option pool shuffle math: new pool shares should make the post-close unallocated pool hit the target percentage, not the gross pool
