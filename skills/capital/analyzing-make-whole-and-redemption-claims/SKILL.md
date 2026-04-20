---
name: analyzing-make-whole-and-redemption-claims
language: en
description: Evaluates make-whole premium claims in bankruptcy with contract interpretation, present value disputes, and secured status analysis. Use when analyzing make-whole claims, evaluating redemption disputes, or assessing premium recovery.
tags:
  - analysis
  - distressed-and-restructuring
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Make Whole And Redemption Claims

## When To Use

- Evaluating whether a make-whole premium is enforceable against a debtor in bankruptcy
- Assessing the allowed amount and secured/unsecured status of a redemption or prepayment claim
- Analyzing indenture or credit agreement language governing optional vs. mandatory redemption, acceleration, and no-call provisions
- Advising distressed debt investors on recovery expectations tied to make-whole premiums
- Preparing or responding to objections to proofs of claim asserting make-whole amounts

## Inputs To Gather

- **Indenture or credit agreement** — full executed version including all supplements and amendments; focus on redemption, prepayment, default, acceleration, and remedies provisions
- **Proof of claim** filed by the noteholder or trustee, including the asserted make-whole calculation
- **Make-whole calculation details** — discount rate used, reference Treasury yield, remaining coupon schedule, reinvestment assumptions, and resulting premium amount
- **Petition date and acceleration timeline** — date of bankruptcy filing, whether acceleration occurred pre- or post-petition, and any cure or reinstatement
- **Governing law** — state law governing the indenture (typically New York) [VERIFY]
- **Relevant court rulings** in the jurisdiction — prior orders in the case addressing make-whole or acceleration issues
- **Capital structure summary** — seniority, collateral coverage, and whether the claiming party holds a secured or unsecured position

## Workflow

1. **Parse the operative provisions**
   - Identify the make-whole or prepayment premium clause — locate the defined term (e.g., "Applicable Premium," "Make-Whole Amount," "Yield Maintenance Premium")
   - Determine whether the premium triggers on voluntary prepayment only or also on acceleration, bankruptcy filing, or automatic maturity
   - Check for integration with the default/remedies section — does acceleration eliminate the premium entitlement, or does the contract preserve it post-acceleration?

2. **Analyze the acceleration question**
   - Determine whether automatic acceleration upon bankruptcy filing (ipso facto clause) is enforceable under §365(e)/§541 [VERIFY]
   - Assess whether acceleration effectively renders the notes due at par, eliminating the call premium — the core issue in *U.S. Bank v. South Side House* (Energy Future Holdings), *Momentive*, and *Ultra Petroleum* lines of authority [VERIFY — check current circuit splits]
   - If the debtor seeks to de-accelerate or reinstate under §1124, evaluate whether reinstatement restores the make-whole obligation

3. **Evaluate contract interpretation under governing law**
   - Apply New York contract interpretation principles (or applicable state law) [VERIFY]: unambiguous language enforced as written; ambiguity construed against the drafter
   - Identify whether the make-whole clause expressly survives acceleration — clauses drafted post-*Momentive* often include explicit "acceleration shall not reduce" language
   - Assess whether the premium constitutes liquidated damages or an unenforceable penalty under state law

4. **Calculate the claimed amount**
   - Verify the discount rate — typically the Treasury rate plus a spread; confirm the referenced maturity and date for the Treasury yield
   - Recalculate the present value of remaining scheduled payments minus the principal amount to verify the asserted premium
   - Check whether the calculation uses the petition date, acceleration date, or another measurement date
   - Flag any discrepancies between the claimed amount and your independent calculation

5. **Determine secured vs. unsecured status**
   - If the claimant is a secured creditor, assess whether the make-whole premium is part of the secured claim under §506(b) — allowed only if the creditor is oversecured and the premium qualifies as "reasonable fees, costs, or charges" provided for in the agreement [VERIFY]
   - For undersecured creditors, the make-whole premium is treated as unsecured
   - Evaluate collateral value relative to total claim including the premium

6. **Assess plan treatment and recovery impact**
   - Model recovery scenarios with and without the make-whole premium allowed
   - Analyze whether the plan proposes reinstatement (§1124) vs. cramdown — reinstatement requires curing defaults and may preserve make-whole obligations
   - Consider the impact on unsecured creditor recoveries if the premium is allowed as a secured or priority claim

## Output

Produce an analysis report containing:

- **Executive summary** — state whether the make-whole claim is likely enforceable, the estimated allowed amount, and its probable classification (secured/unsecured)
- **Contract interpretation analysis** — key provisions quoted with analysis of ambiguity, drafting intent, and governing law application
- **Acceleration and trigger analysis** — whether acceleration extinguishes or preserves the premium under applicable case law
- **Calculation verification** — independent recalculation vs. claimed amount, noting any variances
- **Secured status assessment** — collateral coverage analysis and §506(b) eligibility
- **Recovery sensitivity** — impact on distributions under different plan scenarios
- **Risk factors** — identify jurisdictional uncertainty, pending appeals, or conflicting authority

## Quality Checks

- Confirm every contract provision cited is quoted verbatim from the actual agreement, not paraphrased
- Verify the discount rate and Treasury yield against publicly available data for the referenced date
- Cross-check the mathematical accuracy of the present-value calculation
- Ensure the analysis addresses the current circuit split on post-acceleration make-whole enforceability [VERIFY — *Momentive* vs. *Ultra Petroleum* vs. *Energy Future Holdings* current status]
- Flag any provisions that are ambiguous or where courts have reached conflicting results with [VERIFY]
- Confirm that the secured/unsecured classification accounts for actual collateral valuations, not assumed values
