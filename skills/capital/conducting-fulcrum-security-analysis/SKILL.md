---
name: conducting-fulcrum-security-analysis
language: en
description: Identifies fulcrum securities in distressed capital structures with enterprise value allocation and recovery sensitivity analysis. Use when analyzing fulcrum securities, estimating recovery ranges, or determining value breaks.
tags:
  - process
  - distressed-and-restructuring
metadata:
  author: casemark
  practice_areas:
    - Restructuring
    - Distressed Investing
    - Turnaround
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Fulcrum Security Analysis

Identifies the tranche in a distressed capital structure where enterprise value breaks — the fulcrum security — and models recovery rates across valuation scenarios. The fulcrum security is the most senior class of claims that is impaired (receives less than full recovery), making it the tranche that controls restructuring negotiations and typically converts to equity.

## When To Use

- Evaluating distressed debt or loan positions for potential investment
- Preparing for restructuring negotiations to identify which creditor class holds leverage
- Building a plan of reorganization and allocating enterprise value to claimants
- Stress-testing recovery waterfalls under competing valuation assumptions
- Advising debtors or creditor committees on zone-of-insolvency dynamics

## Inputs To Gather

- **Capital structure detail**: All tranches of debt (revolvers, term loans, bonds, mezzanine, preferred) with face amounts, accrued interest, make-whole or call premiums, and priority/lien status
- **Enterprise value estimates**: At least a base, downside, and upside TEV derived from DCF, comparable transactions, or trading multiples [VERIFY: confirm valuation methodology accepted by stakeholders]
- **Priority and intercreditor terms**: Waterfall mechanics, subordination agreements, adequate protection provisions, priming lien rights
- **Administrative and priority claims**: DIP facility payoff, professional fees, priority tax claims, cure costs for assumed executory contracts
- **Cash and non-operating assets**: Unrestricted cash, value of non-core assets available for distribution outside the operating TEV

## Workflow

1. **Map the capital structure waterfall**
   - List all claims in strict priority order: administrative/DIP, secured (by lien priority and collateral), unsecured, subordinated, preferred equity, common equity
   - Include accrued and default interest where contractually owed [VERIFY: whether post-petition interest accrues depends on solvent/insolvent debtor status under applicable law]
   - Note any structural subordination (holdco vs. opco claims) and cross-guarantees

2. **Establish enterprise value range**
   - Define at least three TEV scenarios (low, base, high) with supporting assumptions
   - Deduct administrative/priority claims and DIP payoffs from TEV to arrive at distributable value
   - If collateral-specific analysis is needed (e.g., first-lien vs. second-lien on different asset pools), break out asset-level values separately

3. **Allocate value through the waterfall**
   - For each TEV scenario, pay claims top-down in priority order until distributable value is exhausted
   - The tranche where value runs out mid-class is the fulcrum security
   - Calculate recovery rate for each tranche: (value allocated to tranche) / (allowed claim amount)

4. **Build the recovery sensitivity table**
   - Rows: each claim tranche in priority order
   - Columns: TEV scenarios (and optionally intermediate values)
   - Cells: recovery percentage (0%–100%) per tranche per scenario
   - Highlight the fulcrum row — this is where recovery shifts from 100% to partial

5. **Identify fulcrum shift points**
   - Determine the TEV breakpoints where the fulcrum migrates from one tranche to another
   - Example: "At TEV below $350M, the fulcrum shifts from second-lien notes to first-lien term loan"
   - Map these breakpoints to key valuation drivers (revenue growth, EBITDA margin, multiple) to show what operational assumptions move the fulcrum

6. **Assess negotiation and investment implications**
   - The fulcrum class typically receives the equity in a reorganized entity — size the implied equity stake
   - Evaluate whether current trading prices of the fulcrum tranche reflect the modeled recovery range
   - Note which creditor constituencies sit above (likely to push for lower TEV to maximize control) vs. below (likely to argue for higher TEV to receive some recovery)

## Output

- **Capital structure summary table**: Tranche, face amount, priority rank, collateral description
- **Recovery waterfall matrix**: Recovery percentages across TEV scenarios for every tranche
- **Fulcrum identification statement**: "Under the base case TEV of $X, the fulcrum security is [tranche], with an estimated recovery of Y%"
- **Sensitivity chart**: TEV on the x-axis, recovery rate on the y-axis, with lines for each tranche showing where value breaks
- **Breakpoint summary**: TEV thresholds at which the fulcrum migrates between tranches
- **Key assumptions and limitations**: Valuation methodology, treatment of disputed claims, intercompany issues

## Quality Checks

- Confirm that total distributions across all tranches equal distributable value (no value leakage or double-counting)
- Verify that no junior tranche shows recovery while a senior tranche is impaired — this violates absolute priority [VERIFY: applicable jurisdiction's treatment of absolute priority rule and any gift/carve-out exceptions]
- Cross-check TEV assumptions against publicly available comps, trading levels, or advisor valuations
- Ensure accrued interest, fees, and make-whole claims are included or explicitly excluded with reasoning
- Validate that DIP and administrative claims are deducted before secured creditor distributions
- Flag any pending intercreditor disputes, equitable subordination claims, or avoidance actions that could alter the waterfall [VERIFY: status of any ongoing adversary proceedings]
