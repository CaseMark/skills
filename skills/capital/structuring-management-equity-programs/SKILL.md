---
name: structuring-management-equity-programs
language: en
description: Designs management incentive structures with rollover equity, option pools, ratchets, and vesting schedules aligned to value creation. Use when structuring management incentives, designing co-invest programs, or aligning management economics.
tags:
  - private-equity
metadata:
  author: casemark
  practice_areas:
    - Private Equity
    - Leveraged Buyouts
    - Growth Equity
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Management Equity Programs

Designs management incentive structures combining rollover equity, option pools, ratchets, and vesting schedules to align management economics with sponsor value creation targets across buyout, growth equity, and recapitalization transactions.

## When To Use

- Structuring the management equity package at close of a new PE acquisition
- Designing co-investment or rollover programs for incumbent management teams
- Building option pools or profits interest plans for post-close incentive alignment
- Evaluating ratchet or hurdle-based equity structures tied to sponsor return thresholds
- Resetting or refreshing management equity grants at recap, dividend recap, or add-on events
- Benchmarking management ownership percentages and dilution across comparable deals

## Inputs To Gather

- **Deal economics**: Enterprise value, equity contribution, leverage profile, and sponsor target returns (gross/net IRR, MOIC)
- **Management team roster**: Identify participants by tier (CEO, C-suite, VP-level, key contributors) with current compensation data
- **Rollover details**: Amount of seller equity rolling, tax basis, rollover as percentage of management net proceeds
- **Option pool sizing**: Target fully diluted pool (typically 10-20% for buyouts), strike price methodology (FMV, book, or nominal), and 409A/tax considerations [VERIFY]
- **Vesting terms**: Time-based schedule (3-5 year cliff/ratable), performance-based triggers (EBITDA milestones, revenue gates, exit multiples)
- **Ratchet/hurdle structure**: Sponsor MOIC or IRR thresholds that unlock incremental management equity (e.g., 5% at 2.0x, scaling to 10% at 3.0x+)
- **Governance constraints**: Existing LLC agreement or stockholders agreement provisions, tag/drag rights, transfer restrictions
- **Tax structuring preferences**: Profits interests vs. stock options vs. restricted stock; 83(b) election timing [VERIFY based on jurisdiction and entity type]

## Workflow

1. **Map sponsor return targets to management allocation**
   - Model equity waterfall at multiple exit scenarios (1.5x, 2.0x, 2.5x, 3.0x+ MOIC)
   - Size total management pool as percentage of fully diluted equity at each return level
   - Determine split between rollover equity, time-vested options, and performance-vested equity

2. **Structure rollover equity**
   - Calculate rollover amount as percentage of management pre-tax proceeds at close
   - Confirm rollover parity (same class/terms as sponsor equity) vs. subordinated rollover
   - Address tax treatment: tax-free rollover via 368 reorganization, Section 351 contribution, or taxable sale/reinvestment [VERIFY]

3. **Design option pool and strike methodology**
   - Set pool size and reserve unallocated grants for future hires (typically 15-25% of pool)
   - Determine strike price: FMV at close (standard for ISOs), nominal/par value for profits interests, or book value
   - Model dilution impact on sponsor returns at each exit scenario
   - Draft allocation table by participant tier with individual grant sizes

4. **Build vesting schedule**
   - Time-based component: Define cliff period (typically 1 year), ratable vesting (monthly or annual over 3-5 years), and acceleration triggers (change of control, termination without cause)
   - Performance-based component: Tie tranches to measurable milestones — EBITDA targets, revenue thresholds, or integration milestones for platform builds
   - Leaver provisions: Classify good leaver vs. bad leaver with corresponding repurchase terms (FMV vs. cost vs. forfeiture)

5. **Configure ratchet/hurdle mechanics**
   - Define sponsor return thresholds (MOIC-based or IRR-based) that unlock incremental equity
   - Model ratchet economics: additional equity percentage earned at each hurdle tier
   - Specify measurement timing — exit-only vs. mark-to-market at interim events (dividend recaps, partial exits)
   - Address anti-dilution and catch-up provisions

6. **Run sensitivity analysis**
   - Produce management payout tables across exit multiples (1.0x through 4.0x+) and hold periods (3, 5, 7 years)
   - Compare management effective ownership on a fully diluted, fully vested basis at each scenario
   - Benchmark total management economics against market data for comparable transactions by deal size, sector, and strategy

7. **Document structure and flag open items**
   - Summarize recommended structure with clear rationale for each design choice
   - Identify items requiring legal drafting (option plan, grant agreements, LLC amendments)
   - Flag tax and securities law issues needing specialist review

## Output

- **Management Equity Summary**: One-page overview of structure — pool size, rollover terms, vesting schedule, ratchet thresholds, and participant allocations
- **Equity Waterfall Model**: Scenario table showing management payouts at multiple exit MOIC levels (per-participant and aggregate)
- **Allocation Table**: Participant-level breakdown by equity instrument type, grant size, vesting schedule, and estimated value at base-case exit
- **Sensitivity Matrix**: Management effective ownership and dollar payouts across a range of exit values and hold periods
- **Open Items List**: Tax, legal, and governance issues flagged for specialist review with recommended next steps

## Quality Checks

- Waterfall math reconciles — total equity distributed equals 100% of equity value at each exit scenario
- Management pool percentage falls within market range for deal type (typically 8-15% for large buyouts, 15-25% for growth equity) [VERIFY against current market benchmarks]
- Rollover amount is realistic relative to management net proceeds and personal liquidity needs
- Vesting schedule complies with Section 409A requirements for deferred compensation [VERIFY]
- Ratchet thresholds align with sponsor underwritten returns — management earns meaningfully more only when sponsor achieves target+ returns
- Tax treatment of each equity instrument is consistent with entity type (C-corp vs. LLC/partnership) and confirmed with tax counsel
- Leaver provisions are enforceable under applicable state law [VERIFY based on jurisdiction]
- All assumptions (exit multiple, hold period, EBITDA growth) are explicitly stated, not embedded silently in calculations
