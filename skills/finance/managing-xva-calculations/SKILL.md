---
name: managing-xva-calculations
language: en
description: Structures CVA, DVA, FVA, and KVA calculation with methodology selection and counterparty exposure modeling. Use when calculating XVA, pricing counterparty credit risk, or analyzing funding valuation adjustments.
tags:
  - management
  - quantitative-finance
  - risk
  - credit
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Quantitative Analysis
    - Structured Products
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing XVA Calculations

Structures CVA, DVA, FVA, and KVA calculation with methodology selection and counterparty exposure modeling.

## When To Use

- Pricing or re-pricing OTC derivatives where counterparty credit risk adjustments are material
- Computing desk-level or portfolio-level XVA charges for P&L attribution
- Selecting or validating methodology choices (SA-CCR vs. IMM, analytic vs. Monte Carlo)
- Reconciling front-office XVA with risk-neutral CVA/DVA reported to finance
- Responding to model validation or audit queries on XVA assumptions
- Assessing incremental XVA impact for new trades, novations, or collateral restructuring

## Inputs To Gather

- **Trade population**: Netting set definitions, CSA/ISDA terms, collateral thresholds, minimum transfer amounts, margin frequency
- **Market data**: Yield curves, credit spreads (CDS or mapped proxies), FX/equity/commodity vols, correlation matrices
- **Counterparty data**: Credit ratings, PD term structures, LGD assumptions, wrong-way risk indicators
- **Funding curves**: Treasury funding spreads, secured vs. unsecured funding basis, internal FTP rates
- **Capital parameters**: RWA methodology (SA-CCR or IMM), cost-of-capital rate, regulatory alpha multiplier [VERIFY — jurisdiction-specific]
- **Collateral terms**: Eligible collateral types, haircut schedules, rehypothecation rights, variation margin vs. initial margin treatment
- **Simulation parameters**: Number of Monte Carlo paths, time grid granularity, diffusion model choices, close-out period assumption

## Workflow

1. **Define netting and margining structure**
   - Map trades to legal netting sets under enforceable ISDA/CSA agreements
   - Confirm collateral terms: threshold, MTA, rounding, independent amounts
   - Identify any one-way CSAs, break clauses, or optionality affecting exposure profiles
   - Flag netting opinions that are missing or expired [VERIFY — enforceability by jurisdiction]

2. **Generate exposure profiles**
   - Select simulation approach: full Monte Carlo revaluation, regression-based (e.g., Longstaff-Schwartz for American-style features), or analytic approximation for vanilla books
   - Define time grid — finer near term (weekly to 1Y), coarser long term (quarterly/annual beyond 5Y)
   - Simulate risk factor paths under risk-neutral measure for pricing, real-world measure if needed for KVA/regulatory
   - Compute per-path, per-time-step MtM; apply netting and collateral modeling to produce Expected Exposure (EE), Expected Positive Exposure (EPE), and Expected Negative Exposure (ENE)
   - Derive Potential Future Exposure (PFE) at required quantiles (typically 95th or 97.5th)

3. **Compute individual XVA components**
   - **CVA**: Integrate discounted EPE against counterparty default probability and LGD. For Basel III SA-CVA, apply prescribed risk weights and correlation parameters [VERIFY — SA-CVA vs. BA-CVA eligibility under local regulation]
   - **DVA**: Mirror calculation using ENE and own-default probability. Determine whether DVA is recognized in regulatory capital vs. only in accounting P&L [VERIFY — prudential treatment varies by jurisdiction]
   - **FVA**: Decompose into Funding Benefit Adjustment (FBA) on negative exposure and Funding Cost Adjustment (FCA) on positive exposure. Apply unsecured funding spread net of collateral offsets. Address controversy: ensure FVA is not double-counting DVA
   - **ColVA**: Calculate cost/benefit of posting collateral — opportunity cost of segregated IM, carry on rehypothecable VM
   - **KVA**: Estimate lifetime cost of regulatory capital (RWA × cost-of-capital rate) discounted over the portfolio's expected life. Requires forward projection of capital under chosen methodology (SA-CCR alpha factor = 1.4 unless internal model approved)
   - **MVA**: Compute cost of posting initial margin under UMR/cleared margin rules; project IM using ISDA SIMM or CCP schedule

4. **Aggregate and attribute**
   - Roll up netting-set-level XVA to counterparty, desk, business line, and firm-wide totals
   - Perform incremental XVA analysis: marginal contribution of individual trades to portfolio-level CVA/FVA
   - Calculate XVA sensitivities (CS01, IR delta, vega) for hedging desk consumption
   - Reconcile front-office XVA (risk-neutral, continuous) with accounting CVA (fair-value, quarterly) and regulatory CVA capital charge

5. **Report and escalate**
   - Produce XVA P&L explain: decompose period-over-period changes into market risk, credit migration, new trades, trade maturity/settlement, and methodology changes
   - Flag counterparties where CVA exceeds materiality thresholds or PFE breaches credit limits
   - Identify wrong-way risk concentrations (e.g., FX derivatives with EM sovereign counterparties)
   - Document all model choices, overrides, and proxy mappings for audit trail

## Output

- **XVA summary table**: CVA, DVA, FVA (FCA + FBA), ColVA, KVA, MVA by netting set and counterparty, with total portfolio XVA
- **Exposure profile charts**: EPE, ENE, and PFE term structures per netting set
- **P&L attribution**: Period-over-period XVA movement broken into risk drivers
- **Sensitivity report**: CS01, IR01, and vega for CVA hedging
- **Methodology memo**: Simulation parameters, model choices, proxy mappings, and known limitations
- **Exception log**: Counterparties with material wrong-way risk, missing netting opinions, or stale credit data

## Quality Checks

- Confirm netting set definitions match signed ISDA/CSA documentation — mismatched netting inflates or deflates exposure
- Validate that EPE converges with increasing Monte Carlo paths (run convergence test; target coefficient of variation < 2% on portfolio CVA)
- Cross-check CVA against market-implied CDS spreads × EPE as a sanity benchmark
- Verify FVA does not double-count DVA — if both are reported, confirm the exposure legs are correctly separated
- Ensure KVA capital projection is consistent with the regulatory methodology actually approved for the entity [VERIFY — IMM vs. SA-CCR status]
- Reconcile sum of incremental XVAs to standalone portfolio XVA (non-linearity is expected but should be documented)
- Confirm collateral modeling reflects actual operational margin call frequency, not just contractual terms
- Review proxy credit spread mappings — ensure sector/region/rating proxies are reasonable and documented
