---
name: managing-redemption-processing
description: Structures redemption processing with NAV calculation, gate provisions, and liquidity management. Use when processing redemptions, managing liquidity, or applying gate provisions.
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
# Managing Redemption Processing

## When To Use

- Processing investor redemption requests (full or partial) against fund NAV
- Evaluating whether gate provisions or suspension clauses should be triggered
- Managing liquidity across redemption windows (monthly, quarterly, annual)
- Coordinating redemption queues when aggregate requests exceed available liquidity
- Calculating and applying redemption fees, holdbacks, or side-pocket adjustments
- Preparing redemption settlement reports for fund administrators and investors

## Inputs To Gather

- **Redemption request details**: Investor name/ID, requested amount or percentage, submission date, redemption date elected
- **Fund governing documents**: LPA/PPM provisions on notice periods, lock-up terms, gate thresholds, and suspension rights
- **NAV data**: Most recent official NAV, estimated NAV if final NAV is pending, NAV calculation methodology (monthly/quarterly)
- **Liquidity profile**: Cash on hand, near-term maturities, liquid vs. illiquid asset breakdown, credit facility availability
- **Aggregate redemption queue**: Total pending redemptions for the same period from all investors
- **Fee schedule**: Early redemption fees, redemption charges, performance fee crystallization impact
- **Side-pocket allocations**: Investor-level side-pocket balances and any restrictions on redemption of side-pocketed assets
- **Tax lot and equalization data**: Investor-level equalization credits/debits and tax withholding requirements [VERIFY — jurisdiction-specific]

## Workflow

1. **Validate redemption requests**
   - Confirm each request was submitted within the required notice period (typically 30–90 days) [VERIFY against fund docs]
   - Verify investor eligibility: check lock-up expiration, any contractual restrictions, ERISA or regulatory holds
   - Confirm the redemption date aligns with permitted redemption windows per the fund's offering documents

2. **Calculate preliminary redemption amounts**
   - Apply the most recent NAV per share/unit to the investor's capital account
   - Adjust for accrued management fees, performance fees (including high-water mark and crystallization), and equalization amounts
   - Deduct any applicable early redemption fees or charges
   - Identify side-pocket balances — exclude side-pocketed assets from the redeemable amount unless side-pocket liquidation is available

3. **Assess aggregate liquidity and gate thresholds**
   - Sum all redemption requests for the period and compare against fund-level and investor-level gate limits (e.g., 25% fund-level gate, 10% investor-level cap per quarter) [VERIFY gate percentages per fund docs]
   - If aggregate requests exceed the gate, apply pro-rata allocation across all redeeming investors
   - Determine whether illiquid asset levels or market conditions warrant invoking suspension provisions
   - If gates are triggered, prepare gate notification letters citing the specific LPA/PPM provision

4. **Execute redemption settlement**
   - Calculate final redemption proceeds once official NAV is struck
   - Determine holdback amount (typically 5–10% of redemption proceeds) retained pending annual audit and final NAV adjustments [VERIFY holdback percentage]
   - Process wire transfers for the non-holdback portion within the settlement window (commonly T+30 to T+60 from redemption date)
   - Record capital account reduction and update the investor's ownership percentage in the fund's books

5. **Handle holdback release and true-up**
   - After the fund's annual audit is finalized, recalculate the investor's final redemption amount based on audited NAV
   - Release or claw back holdback amounts based on the true-up calculation
   - Issue final redemption statement with audited figures and tax reporting information (K-1 or equivalent) [VERIFY — tax form varies by jurisdiction and fund structure]

6. **Update records and report**
   - Update the capital account ledger, partnership allocations, and investor register
   - Notify the fund administrator and transfer agent of completed redemptions
   - Prepare redemption summary report for GP/investment committee review showing: total requests received, amounts processed, gates applied, holdback balances, and remaining investor queue

## Output

- **Redemption processing schedule**: Timeline showing notice receipt, NAV determination date, settlement date, and holdback release date for each investor
- **Gate analysis memo**: If applicable, calculation showing aggregate requests vs. gate threshold, pro-rata allocation, and carry-forward queue
- **Investor redemption statements**: Per-investor breakdown of NAV applied, fees deducted, holdback retained, and net proceeds wired
- **Liquidity impact summary**: Pre- and post-redemption cash position, impact on fund's liquid/illiquid asset ratio, and any credit facility drawdown required
- **Capital account reconciliation**: Updated investor capital accounts reflecting processed redemptions

## Quality Checks

- Confirm all redemption requests were received within the contractual notice window — late requests must be deferred to the next period
- Verify NAV used for redemption is the official, administrator-confirmed NAV (not an internal estimate) before final settlement
- Cross-check gate calculations against the exact LPA/PPM language — gate percentages, measurement periods, and carve-outs vary by fund
- Ensure holdback percentages and release timelines match governing documents; flag any deviation with [VERIFY]
- Validate that side-pocket balances are excluded from redemption proceeds unless a specific side-pocket liquidation event has occurred
- Confirm wire instructions match the investor's most recent authenticated banking details (AML/KYC refresh if stale)
- Reconcile total redemption outflows against the fund's cash ledger — settlement should not create an overdraft without GP approval of a credit facility draw
- Verify tax withholding obligations are met before wire release [VERIFY — withholding requirements vary by investor domicile and fund jurisdiction]
