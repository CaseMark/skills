---
name: modeling-tax-attribute-preservation
language: en
description: Analyzes NOL and tax attribute preservation strategies under Section 382 limitations in ownership change scenarios. Use when modeling tax attribute preservation, analyzing 382 limitations, or structuring ownership change thresholds.
tags:
  - modeling
  - distressed-and-restructuring
  - tax
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Financial Model
  skill_modes:
    - Modeling
    - Forecasting
---
# Modeling Tax Attribute Preservation

## When To Use

- Evaluating whether a proposed transaction (debt-for-equity swap, rights offering, plan of reorganization) triggers an "ownership change" under IRC §382
- Quantifying the annual §382 limitation on post-change NOL and credit utilization
- Comparing restructuring alternatives by their net tax-attribute value after §382 haircuts
- Advising on shareholder threshold management to avoid or defer an ownership change
- Modeling the incremental value of a §382(l)(5) bankruptcy exception versus §382(l)(6) election

## Inputs To Gather

- **NOL and credit schedule**: Federal and state NOL carryforward balances by vintage year, expiration dates, and any built-in loss/gain positions (NUBIL/NUBIG) [VERIFY state-specific NOL rules and carryforward periods]
- **Equity capitalization table**: All 5%+ shareholders (direct and constructive under §382 attribution rules), option pools, convertible instruments, and warrant holders with strike prices
- **Transaction terms**: Proposed equity issuance amounts, conversion ratios, exchange mechanics, and closing timeline
- **Company value inputs**: Current equity market cap or agreed enterprise value, long-term tax-exempt rate published by IRS for the month of the ownership change [VERIFY current applicable federal rate]
- **Historical ownership shifts**: Rolling 3-year testing period log of 5%+ shareholder percentage-point increases
- **Built-in gain/loss data**: Fair market value versus tax basis of assets at the change date to determine NUBIG or NUBIL status under the §1374 approach or the §338 approach [VERIFY which recognition period method applies]

## Workflow

1. **Map the ownership change test**
   - Identify all 5%+ shareholders under the constructive ownership and aggregation rules of Treas. Reg. §1.382-2T
   - Build a rolling 3-year testing-period schedule tracking each 5%+ shareholder's lowest and current percentage
   - Sum percentage-point increases; flag if aggregate exceeds or approaches the 50-point threshold

2. **Calculate the §382 annual limitation**
   - Multiply the loss corporation's equity value immediately before the ownership change by the applicable long-term tax-exempt rate
   - Adjust for any recognized built-in gains during the 5-year recognition period (increases the limitation) or built-in losses (subject to the limitation)
   - Apply the continuity-of-business-enterprise (COBE) requirement — if not met for 2 years post-change, limitation drops to zero [VERIFY COBE fact pattern]

3. **Model the bankruptcy exceptions**
   - §382(l)(5): If the loss corporation is in a Title 11 case and historic shareholders/qualified creditors own ≥50% post-change, no annual limitation applies — but NOLs are reduced by interest deductions on converted debt for the 3 prior tax years, and a second ownership change within 2 years zeroes remaining NOLs
   - §382(l)(6): Standard limitation applies but equity value is measured post-restructuring (typically higher), which may yield a larger annual cap
   - Compare net present value of usable NOLs under each path over the carryforward horizon

4. **Build the NOL utilization forecast**
   - Layer the §382 cap over projected taxable income by year
   - Apply vintage-year expiration dates — oldest NOLs used first (FIFO)
   - Incorporate state-level §382-equivalent limitations where applicable [VERIFY state conformity — e.g., California limits NOL usage independently]
   - Discount the tax savings at an appropriate after-tax rate to derive the net present value of preserved attributes

5. **Run scenario and sensitivity analysis**
   - Vary equity value ±10–20% to show limitation sensitivity
   - Model alternative transaction structures (partial conversion, staged closings) to test whether ownership change can be avoided
   - Test threshold management strategies: transfer restrictions, poison pills, §382 rights plans, or shareholder caps
   - Compare outcomes with and without NUBIG/NUBIL adjustments

6. **Compile deliverable**
   - Summary table: NOL balance, annual §382 cap, usable NOLs by year, NPV of tax savings
   - Scenario comparison matrix (l)(5) vs. (l)(6) vs. no ownership change
   - Key assumptions log with [VERIFY] flags for all rate, valuation, and jurisdictional inputs

## Output

- **§382 Limitation Model** (Excel-ready table or structured output): annual cap, cumulative usage, expiration waste, and NPV of tax shield under base and alternative cases
- **Ownership Change Testing Schedule**: 3-year rolling shareholder log showing whether the 50-point threshold is breached
- **Scenario Comparison Summary**: Side-by-side of (l)(5), (l)(6), and non-change structures with NPV differential
- **Assumption and Risk Register**: All inputs, sources, and [VERIFY] items requiring confirmation

## Quality Checks

- Confirm that the long-term tax-exempt rate used matches the IRS-published rate for the correct month [VERIFY]
- Validate that constructive ownership attribution (family, entity, option) rules are applied consistently across the shareholder schedule
- Ensure NOL vintage ordering follows FIFO and that expiration dates align with the applicable carryforward period (20-year pre-2018, indefinite post-TCJA with 80% taxable income cap) [VERIFY which NOL vintage rules apply to each tranche]
- Cross-check that NUBIG/NUBIL classification uses the correct measurement method and that recognition-period items are properly included or excluded
- Verify that the model handles a second ownership change correctly — §382 cap is the lesser of the new and old limitations
- Flag any state where §382 conformity is partial or nonexistent so state-level modeling is adjusted accordingly
