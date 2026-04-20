---
name: managing-alternative-fund-operations
language: en
description: Structures operational processes for hedge fund, PE, and real estate fund specific workflows. Use when managing alternative fund ops, processing capital calls, or handling commitment tracking.
tags:
  - management
  - fund-operations
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Alternative Fund Operations

Structures operational processes for hedge fund, PE, and real estate fund specific workflows including capital call processing, commitment tracking, distribution waterfalls, and NAV reporting.

## When To Use

- Processing or reviewing capital call notices and funding schedules
- Tracking LP commitments, drawdowns, and unfunded obligations
- Structuring distribution waterfall calculations (return of capital, preferred return, catch-up, carried interest splits)
- Preparing or auditing NAV packages and investor statements
- Managing fund-level cash flow reconciliation across investment vehicles
- Coordinating subscription/redemption processing for open-ended funds
- Building operational checklists for fund launches, closings, or wind-downs

## Inputs To Gather

- **Fund structure**: Vehicle type (LP/LLC, offshore feeder, master-feeder, parallel fund), domicile, and governing documents (LPA/OA)
- **Investor data**: LP commitment schedule, contribution history, ownership percentages, side letter terms
- **Capital activity**: Pending capital calls, distribution notices, recycling provisions, recall rights
- **Waterfall terms**: Preferred return rate/hurdle, GP catch-up percentage, carry split, clawback provisions, deal-by-deal vs. whole-fund economics
- **NAV inputs**: Portfolio valuations (Level 1/2/3), accrued fees, fund expenses, pending trades
- **Compliance parameters**: Concentration limits, borrowing caps, investment period status, key-person provisions [VERIFY against LPA]
- **Timeline**: Reporting period end date, capital call due date, distribution record date

## Workflow

1. **Classify the fund type and operational context**
   - Determine if hedge fund (open-ended, NAV-based), PE/VC (closed-end, commitment-based), or real estate fund (hybrid)
   - Identify the specific operational process: capital call, distribution, NAV calc, investor onboarding, or period-end reporting
   - Confirm governing document references (LPA sections, side letter carve-outs)

2. **Validate source data and investor records**
   - Reconcile LP commitment balances: total commitment minus cumulative contributions plus any recalled amounts
   - Confirm pro-rata shares and any equalization adjustments for subsequent closings
   - Cross-check side letter provisions that modify default economics (fee discounts, co-invest rights, MFN triggers) [VERIFY]
   - Flag stale valuations or missing marks on illiquid positions

3. **Execute the operational process**
   - *Capital calls*: Calculate each LP's pro-rata share, apply management fee and organizational expense allocations, generate call notice with wire instructions and funding deadline
   - *Distributions*: Run waterfall tiers — (i) return of contributed capital, (ii) preferred return accrual, (iii) GP catch-up, (iv) residual carry/profit split — applying the correct compounding method [VERIFY: compounded vs. simple preferred return per LPA]
   - *NAV reporting*: Aggregate portfolio marks, accrue management fees and incentive fees/carried interest, deduct fund-level expenses, compute per-unit/per-share NAV
   - *Redemptions (open-ended)*: Apply notice period, gate provisions, and holdback percentages; calculate redemption NAV with any illiquid pocket adjustments

4. **Reconcile and cross-check**
   - Tie cash movements to bank statements and custodian records
   - Verify that cumulative drawdowns do not exceed commitment amounts
   - Confirm incentive fee/carry crystallization frequency and high-water mark resets
   - Reconcile investor-level capital accounts to fund-level totals

5. **Produce reporting deliverables**
   - Generate investor capital account statements showing beginning balance, contributions, distributions, allocation of gains/losses, ending balance
   - Prepare fund-level management report with AUM summary, investment activity, fee calculations, and liquidity position
   - Document any exceptions, overrides, or manual adjustments with rationale

## Output

- **Capital call notice**: LP-by-LP funding amounts, due date, wire instructions, purpose of call (investment, fees, expenses)
- **Distribution notice**: Waterfall tier breakdown per LP, tax withholding notes, payment method
- **NAV package**: Fund-level and investor-level NAV, performance summary (IRR, TVPI, DPI, RVPI for closed-end; time-weighted return for open-end), fee accruals
- **Capital account statement**: Full activity detail per LP for the reporting period
- **Operational checklist**: Task-by-task tracker for fund events (closing, capital call cycle, year-end)

## Quality Checks

- All LP pro-rata calculations sum to 100% (or the correct aggregate commitment)
- Waterfall distributions respect tier sequencing — no carry leakage before preferred return is fully satisfied
- Management fee basis matches LPA terms (committed capital during investment period, invested capital thereafter) [VERIFY]
- Incentive fee/carry calculations correctly apply high-water mark or loss carryforward provisions
- Cash reconciliation ties to zero variance against bank/custodian records
- Equalization interest on subsequent closing LPs is calculated and allocated correctly
- Side letter fee discounts and MFN elections are reflected in individual LP allocations [VERIFY]
- All currency conversions use the FX rate source and timing specified in fund documents
- Redemption gate calculations use the correct denominator (fund-level vs. investor-level NAV)
