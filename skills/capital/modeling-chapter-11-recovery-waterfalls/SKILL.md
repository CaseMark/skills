---
name: modeling-chapter-11-recovery-waterfalls
language: en
description: Builds recovery waterfall models with absolute priority, secured vs unsecured claims, and plan of reorganization distribution analysis. Use when modeling bankruptcy recoveries, analyzing claim priorities, or estimating creditor distributions.
tags:
  - modeling
  - distressed-and-restructuring
  - credit
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
# Modeling Chapter 11 Recovery Waterfalls

Builds recovery waterfall models that distribute enterprise value across claim classes following absolute priority, estimating cents-on-the-dollar recovery for each creditor tier under a plan of reorganization or liquidation scenario.

## When To Use

- Estimating creditor recoveries under a proposed Chapter 11 plan of reorganization
- Comparing reorganization vs. Chapter 7 liquidation outcomes (the "best interests" test)
- Pricing distressed debt by modeling recovery at various enterprise value assumptions
- Evaluating the fulcrum security (the class where value breaks)
- Supporting disclosure statement preparation or plan confirmation arguments
- Stress-testing recovery sensitivity to valuation, claim amounts, or priority disputes

## Inputs To Gather

- **Claims register / proof-of-claim summary**: All filed claims by class — secured, priority, general unsecured, subordinated, equity interests. Include disputed or contingent claims with estimated allowed amounts.
- **Collateral valuations**: Appraised or estimated values for each collateral pool securing a secured claim (real property, equipment, receivables, IP). Distinguish between going-concern and orderly-liquidation values.
- **Enterprise or asset value range**: Low / base / high valuation scenarios. Source from DCF, comparable transactions, or liquidation analysis as appropriate.
- **DIP facility and administrative claims**: DIP loan balances, accrued professional fees (debtors' counsel, UCC counsel, financial advisors), U.S. Trustee fees, cure costs.
- **Plan treatment terms**: Any negotiated recoveries, equity tips, gifting structures, or class-skipping provisions in the proposed plan [VERIFY — plan terms are case-specific].
- **Intercompany claims and structural seniority**: Entity-level debt placement if multi-entity debtor group; substantive consolidation status.
- **Executory contract / lease cure amounts**: Assumed or rejected contracts and corresponding cure or rejection damage claims.

## Workflow

1. **Map the priority stack**
   - Order all claims by Bankruptcy Code priority: § 507 priority claims (admin expenses, wage claims, tax claims), then secured claims (to extent of collateral value), general unsecured, subordinated, equity.
   - For secured creditors, bifurcate under § 506(a): secured portion (up to collateral value) and deficiency claim (unsecured).
   - Identify any intercreditor subordination agreements that contractually re-order the statutory waterfall [VERIFY — subordination terms vary by agreement].

2. **Build the waterfall schedule**
   - Row structure: one row per claim class, ordered by priority.
   - Column structure: claim amount | cumulative claims | available value | distribution | recovery %.
   - Distribute available value top-down: each class receives the lesser of its allowed claim or remaining distributable value before the next class is paid.
   - For classes receiving partial recovery, calculate pro-rata distribution across claimants within the class.

3. **Model secured claim recoveries separately**
   - Each secured class waterfall runs against its specific collateral pool, not the general estate.
   - Apply adequate protection payments already made during the case as offsets.
   - If collateral value exceeds the secured claim, the surplus flows back to the general estate.

4. **Run valuation scenarios**
   - Build at least three scenarios (low / base / high enterprise value) to show how recovery shifts across classes.
   - Identify the fulcrum security — the most senior class that receives less than full recovery. This is the class with the greatest negotiating leverage and option value.
   - Calculate breakeven enterprise value for each class to achieve par recovery.

5. **Incorporate plan-specific adjustments**
   - Equity tips or carve-outs negotiated for junior classes despite absolute priority.
   - Convenience class thresholds (small claims paid in full to reduce administrative cost).
   - Rights offerings, backstop commitments, or new-money investment tranches that affect distributable value.
   - Tax attributes (NOLs, § 382 limitations) that affect post-emergence equity value [VERIFY — NOL availability depends on ownership change analysis].

6. **Perform the best-interests test**
   - Build a parallel Chapter 7 liquidation waterfall using orderly-liquidation collateral values and estimated Chapter 7 trustee fees / wind-down costs.
   - Compare class-by-class: each class must receive at least as much under the plan as it would in liquidation.

## Output

- **Recovery waterfall table**: Claim class | Allowed claim amount | Distribution amount | Recovery % — across all scenarios.
- **Fulcrum security identification**: State which class is the fulcrum and at what enterprise value the fulcrum shifts.
- **Sensitivity matrix**: Recovery by class across a range of enterprise values (e.g., $50M increments).
- **Best-interests comparison**: Side-by-side plan vs. liquidation recovery for each class.
- **Key assumptions summary**: Valuation methodology, disputed claim treatment, subordination mechanics, and plan-specific adjustments applied.

## Quality Checks

- Waterfall distributions must sum exactly to total distributable value — no leakage or rounding gaps.
- No junior class receives any distribution while a senior class is impaired (unless an equity tip or gift is explicitly modeled and labeled).
- Secured claim bifurcation matches collateral valuations; deficiency claims flow correctly to the unsecured pool.
- Administrative and priority claims are fully satisfied before any distribution to general unsecured creditors [VERIFY — confirm no § 1129(a)(9) waiver].
- Recovery percentages are bounded 0–100% per class; cross-check that weighted average recovery across all claims equals total distributable value / total allowed claims.
- Scenario outputs move directionally as expected — higher enterprise value should weakly increase recovery for each class.
- All disputed, contingent, or unliquidated claims are flagged with estimated allowed amounts and marked [VERIFY].
