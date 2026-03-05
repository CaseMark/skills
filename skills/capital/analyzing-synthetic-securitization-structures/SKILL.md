---
name: analyzing-synthetic-securitization-structures
description: Evaluates synthetic CDO and CRT structures with credit default swap mechanics and funded/unfunded tranche analysis. Use when analyzing synthetic structures, evaluating credit risk transfer, or modeling CDS-based securitizations.
tags:
  - analysis
  - structured-finance
  - risk
  - credit
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Synthetic Securitization Structures

## When To Use

- Evaluating a synthetic CDO (collateralized debt obligation) where credit risk is transferred via credit default swaps rather than true sale of assets
- Analyzing credit risk transfer (CRT) programs such as Fannie Mae Connecticut Avenue Securities (CAS) or Freddie Mac Structured Agency Credit Risk (STACR)
- Reviewing funded vs. unfunded tranche mechanics in a bespoke or managed synthetic structure
- Assessing counterparty exposure, collateral posting requirements, and credit event definitions in CDS-based securitizations
- Comparing synthetic structures against cash equivalents for capital relief, regulatory treatment, or risk retention purposes

## Inputs To Gather

- **Structure term sheet or offering circular** — tranche definitions, attachment/detachment points, notional amounts, coupon mechanics
- **Reference portfolio details** — obligor count, sector/geographic concentration, weighted-average rating, weighted-average life
- **CDS confirmation or ISDA schedule** — credit event definitions (bankruptcy, failure to pay, restructuring), settlement method (physical vs. cash vs. auction), materiality thresholds
- **Collateral account terms** — eligible investments, haircut schedules, rehypothecation rights, substitution triggers
- **Waterfall mechanics** — interest and principal priority of payments, loss allocation sequence, write-down/write-up mechanics
- **Counterparty information** — protection buyer/seller ratings, replacement triggers, collateral posting thresholds under CSA [VERIFY against specific CSA terms]

## Workflow

1. **Map the structure diagram**
   - Identify the protection buyer (originator/sponsor) and protection seller (SPV or direct counterparty)
   - Classify each tranche: super-senior (typically unfunded CDS wrap), mezzanine (funded or unfunded), first-loss/equity
   - Note whether the SPV is bankruptcy-remote and whether funded tranches issue credit-linked notes (CLNs)

2. **Analyze credit event mechanics**
   - Confirm which ISDA credit events apply — standard corporate CDS vs. sovereign vs. LCDS for loans [VERIFY: 2003 vs. 2014 ISDA definitions]
   - Assess whether restructuring is included (Modified Restructuring, Mod-Mod-R, or Old-R) and how it affects loss allocation
   - Determine settlement method: cash settlement with dealer poll/auction, physical settlement, or fixed recovery

3. **Evaluate funded vs. unfunded tranches**
   - For funded tranches: review CLN terms, collateral account eligible investments, and mark-to-market triggers
   - For unfunded tranches: assess counterparty credit quality, collateral posting obligations, and replacement language
   - Calculate the effective cost of protection across funded (coupon = SOFR + spread) vs. unfunded (CDS premium only) tranches

4. **Model loss allocation and waterfall**
   - Map attachment and detachment points for each tranche to determine subordination levels
   - Stress-test reference portfolio using base, adverse, and severely adverse scenarios (e.g., 2x–5x historical default rates)
   - Assess expected loss, probability of tranche impairment, and implied ratings at each stress level
   - Identify any write-down/write-up mechanics — are losses allocated on a mark-to-market or realized-loss basis?

5. **Assess counterparty and basis risk**
   - Evaluate protection buyer default risk — what happens to the SPV and noteholders if the originator fails to pay premiums?
   - Review collateral account risk: can principal be impaired by eligible investment losses?
   - Identify basis risk between CDS reference obligations and actual portfolio (naming mismatch, maturity mismatch, currency mismatch)

6. **Review regulatory and capital treatment**
   - Determine whether the structure achieves significant risk transfer (SRT) under applicable capital framework [VERIFY: Basel III/IV, CRR2 Article 244–245 for EU, US agency rules for CRT]
   - Assess risk retention compliance — does the originator retain a material net economic interest? [VERIFY: EU Securitisation Regulation Article 6, US Dodd-Frank Section 941]
   - Evaluate accounting treatment: does the synthetic transfer achieve off-balance-sheet treatment or only capital relief?

## Output

Produce a structured analysis report containing:

- **Structure Summary** — diagram or table showing parties, tranche stack (super-senior through equity), notional amounts, attachment/detachment points, funded/unfunded status
- **CDS Mechanics Summary** — credit events, settlement method, reference obligation characteristics, maturity profile
- **Tranche-Level Analysis** — for each tranche: subordination, expected loss, implied rating, coupon/premium, key risks
- **Stress Testing Results** — portfolio loss scenarios mapped to tranche impairment thresholds, with probability-weighted outcomes
- **Counterparty Risk Assessment** — exposure quantification for unfunded tranches, collateral adequacy for funded tranches
- **Regulatory/Capital Treatment** — SRT eligibility conclusion, risk retention status, accounting impact
- **Key Risks and Mitigants** — basis risk, counterparty risk, collateral risk, documentation gaps, with recommended mitigants

## Quality Checks

- Confirm all attachment/detachment points sum correctly across the capital structure and match the total reference portfolio notional
- Verify that credit event definitions in the CDS confirmation are consistent with the offering circular/term sheet
- Cross-check loss allocation waterfall against both the indenture and the CDS documentation for any conflicts
- Ensure stress scenarios are calibrated to the reference portfolio's asset class (corporate, RMBS, CMBS, leveraged loans) — do not apply generic assumptions
- Validate that regulatory capital conclusions cite the correct jurisdictional framework [VERIFY]
- Flag any mismatch between the CDS reference portfolio and the originator's actual retained portfolio
- Confirm collateral account eligible investment criteria are sufficiently conservative relative to tranche ratings
