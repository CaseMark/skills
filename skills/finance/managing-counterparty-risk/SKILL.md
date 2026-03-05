---
name: managing-counterparty-risk
description: Structures counterparty credit risk assessment with exposure calculation and mitigation monitoring. Use when assessing counterparty risk, calculating potential future exposure, or managing collateral.
tags:
  - management
  - risk-management
  - risk
  - credit
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Counterparty Risk

## When To Use

- Onboarding a new derivatives, lending, or repo counterparty and setting initial credit limits
- Periodic (quarterly/annual) review of existing counterparty exposures against approved limits
- Calculating potential future exposure (PFE) or credit valuation adjustment (CVA) for a portfolio
- Evaluating collateral adequacy after a credit event, rating downgrade, or material market move
- Preparing counterparty risk reports for risk committees, regulators, or senior management
- Assessing netting and close-out enforceability under ISDA or equivalent master agreements

## Inputs To Gather

- **Counterparty profile**: Legal entity name, LEI, corporate structure, domicile, sovereign rating
- **Credit assessment data**: External ratings (S&P, Moody's, Fitch), internal scorecard results, CDS spreads, financial statements (most recent 2-3 periods)
- **Exposure data**: Trade-level mark-to-market by product (derivatives, repo, securities lending, loans), notional amounts, maturity profiles
- **Netting & collateral documentation**: ISDA master agreement status, CSA/VM-CSA terms (thresholds, minimum transfer amounts, eligible collateral, haircuts), netting opinion coverage [VERIFY jurisdiction-specific enforceability]
- **Limit framework**: Approved credit limits by exposure type (current exposure, PFE, settlement risk), tenor buckets, and any sub-limits by product or desk
- **Regulatory parameters**: SA-CCR or IMM methodology inputs, risk weights, CVA capital charge requirements [VERIFY applicable framework: Basel III / Basel IV / local implementation]

## Workflow

1. **Profile the counterparty**
   - Confirm legal entity, group hierarchy, and ultimate parent
   - Map to internal rating grade using scorecard or external rating mapping
   - Determine probability of default (PD) and loss given default (LGD) assumptions
   - Flag any wrong-way risk — correlation between counterparty creditworthiness and exposure direction

2. **Calculate exposure metrics**
   - Compute current exposure (CE): aggregate positive MTM after legally enforceable netting
   - Estimate potential future exposure (PFE) at defined confidence interval (typically 95th or 97.5th percentile) across relevant time horizons (1-day, 10-day, 1-year, life-of-trade)
   - Derive expected exposure (EE) and expected positive exposure (EPE) profiles for CVA pricing
   - For SA-CCR: compute replacement cost (RC) and PFE add-on by asset class (interest rate, FX, credit, equity, commodity) [VERIFY regulatory multipliers and supervisory factors]

3. **Assess collateral and mitigation**
   - Verify CSA terms: threshold, independent amount, minimum transfer amount, frequency of margin calls
   - Calculate net unsecured exposure after applying collateral (cash, government bonds, other eligible assets with appropriate haircuts)
   - Review initial margin (IM) adequacy for cleared vs. bilateral trades
   - Evaluate guarantees, credit insurance, or CDS hedges and their effectiveness
   - Confirm netting opinion validity for counterparty jurisdiction [VERIFY local netting enforceability]

4. **Test against limits and triggers**
   - Compare CE, PFE, and settlement exposure against approved counterparty limits
   - Identify limit breaches, near-breaches (e.g., >80% utilization), and tenor concentrations
   - Check for credit event triggers: rating downgrade clauses, additional termination events (ATEs), cross-default provisions
   - Run stress scenarios: counterparty default under adverse market conditions, jump-to-default, simultaneous collateral devaluation

5. **Compile risk report and recommendations**
   - Summarize exposure profile with trend analysis (current vs. prior period)
   - Present limit utilization dashboard by counterparty, product, and tenor
   - Highlight watch-list counterparties and escalation items
   - Recommend actions: limit adjustments, additional collateral calls, trade compression or novation, hedging via CDS

## Output

The counterparty risk report should contain:

- **Executive summary**: Top 10 exposures, aggregate portfolio PFE, notable changes since last review
- **Individual counterparty cards**: Rating, PD/LGD, CE/PFE, limit utilization, collateral coverage ratio, wrong-way risk flag
- **Exposure analytics**: Breakdown by asset class, maturity bucket, and netting set; concentration metrics (Herfindahl index or top-N share)
- **Stress test results**: Impact of defined scenarios on exposure and collateral values
- **Action items**: Specific limit changes, margin call recommendations, documentation remediation (e.g., outstanding netting opinions or CSA amendments)
- **Regulatory capital impact**: SA-CCR EAD or IMM exposure, CVA capital charge delta [VERIFY capital framework in effect]

## Quality Checks

- Verify that netting is applied only where a valid, current netting opinion exists for the relevant jurisdiction
- Confirm PFE model parameters (volatilities, correlations, confidence level) are consistent with approved methodology
- Cross-check MTM values against independent valuation sources (front-office vs. risk system reconciliation)
- Ensure haircuts on collateral reflect current market conditions and regulatory minimums
- Validate that wrong-way risk exposures are separately identified and not netted against general exposure
- Confirm all limit breaches have documented escalation and remediation timelines
- Check that rating downgrade trigger analysis reflects current CSA/ISDA terms, not stale documentation
