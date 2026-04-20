---
name: analyzing-counterparty-netting-efficiency
language: en
description: Evaluates netting benefits across derivative portfolios with bilateral vs cleared netting, portfolio compression, and capital savings. Use when analyzing netting efficiency, evaluating compression opportunities, or optimizing counterparty exposure.
tags:
  - analysis
  - derivatives-and-structured-products
  - portfolio
metadata:
  author: casemark
  practice_areas:
    - Derivatives
    - Structured Products
    - Hedging
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Counterparty Netting Efficiency

Evaluates netting benefits across derivative portfolios by comparing bilateral vs. cleared netting arrangements, identifying portfolio compression opportunities, and quantifying capital savings from improved netting ratios.

## When To Use

- Assessing gross-to-net exposure ratios across counterparties to identify optimization targets
- Evaluating whether bilateral OTC trades should migrate to central clearing for netting benefit
- Analyzing portfolio compression candidates (e.g., TriOptima, Quantile, LMRKTS cycles)
- Quantifying SA-CCR or IMM capital savings from improved netting set structures
- Preparing for ISDA master agreement renegotiation by modeling netting efficiency under alternative CSA terms
- Reviewing netting enforceability across jurisdictions before consolidating netting sets

## Inputs To Gather

- **Trade-level data**: Notional amounts, mark-to-market values, asset class, maturity profile, and counterparty identifiers for all in-scope positions
- **Netting set definitions**: ISDA master agreement mapping, CSA terms (threshold, MTA, eligible collateral), cleared vs. bilateral designation per trade
- **CCP membership details**: Which CCPs the firm clears through, product eligibility per CCP, and current cleared portfolio composition
- **Regulatory framework**: Whether the firm uses SA-CCR or IMM for counterparty credit risk; applicable leverage ratio and CVA capital requirements [VERIFY]
- **Compression history**: Prior compression cycle results, terminated notional, and any operational constraints on compression eligibility
- **Legal netting opinions**: Jurisdictional enforceability status for each counterparty's netting agreement [VERIFY]

## Workflow

1. **Map netting sets** — Group all trades by legal netting agreement. Identify orphaned trades (no enforceable netting) and trades under multiple CSAs with the same counterparty that could be consolidated.

2. **Calculate gross-to-net ratios** — For each netting set, compute:
   - Gross positive / gross negative MTM
   - Net MTM after close-out netting
   - Netting ratio = 1 − (Net Exposure / Gross Positive Exposure)
   - Flag counterparties with netting ratios below 50% as priority optimization targets

3. **Assess bilateral vs. cleared netting** — For each asset class:
   - Model current bilateral exposure by counterparty
   - Model hypothetical cleared exposure at each eligible CCP (netting across all counterparties in a single CCP netting set)
   - Compare multilateral netting benefit against clearing costs (IM, default fund contribution, CCP fees)
   - Note clearing mandate applicability for each product [VERIFY]

4. **Identify compression candidates** — Screen for:
   - Offsetting or near-offsetting trades within and across counterparties
   - Redundant intermediation chains (A↔B↔C where A↔C is feasible)
   - Trades past economic utility but still consuming line and capital
   - Estimate notional reduction and exposure reduction from compression

5. **Quantify capital impact** — Calculate:
   - SA-CCR EAD before and after netting optimization (replacement cost + PFE with netting factor)
   - RWA reduction from improved netting (using counterparty risk weights)
   - Leverage ratio exposure reduction
   - CVA capital charge reduction from lower EAD [VERIFY — depends on BA-CVA vs. SA-CVA regime]

6. **Model implementation scenarios** — Rank opportunities by:
   - Capital savings (RWA and leverage)
   - Implementation complexity (legal renegotiation, operational lift, counterparty willingness)
   - Ongoing cost (clearing fees, margin funding)
   - Produce a prioritized action plan with estimated timelines

## Output

- **Netting efficiency dashboard**: Per-counterparty and per-netting-set gross-to-net ratios, with trend over prior periods if data available
- **Clearing migration analysis**: Trade populations recommended for clearing, expected multilateral netting benefit, and incremental clearing costs
- **Compression opportunity register**: Candidate trade populations, estimated notional and exposure reduction, next available compression cycle dates
- **Capital impact summary**: Before/after RWA, leverage exposure, and CVA capital with breakdowns by optimization lever (netting consolidation, clearing migration, compression)
- **Implementation roadmap**: Prioritized actions with dependencies, legal/operational prerequisites, and estimated capital release per action

## Quality Checks

- Confirm netting set mappings reconcile to the firm's official ISDA agreement register — no trades should be unassigned
- Verify that netting enforceability has been confirmed by legal opinion for each jurisdiction involved [VERIFY]
- Cross-check SA-CCR calculations against regulatory definitions (supervisory factors, maturity floors, collateral haircuts)
- Ensure compression estimates account for operational constraints (minimum participation thresholds, dealer consent requirements)
- Validate that clearing cost assumptions use current CCP fee schedules and margin models, not stale estimates
- Confirm all MTM values are as-of the same valuation date and use consistent curves
