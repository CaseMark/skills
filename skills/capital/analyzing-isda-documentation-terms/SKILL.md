---
name: analyzing-isda-documentation-terms
language: en
description: Evaluates ISDA Master Agreement provisions with close-out netting, termination events, and credit support annexes. Use when reviewing ISDA terms, analyzing CSA provisions, or assessing documentation risk.
tags:
  - analysis
  - derivatives-and-structured-products
  - risk
  - credit
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
# Analyzing Isda Documentation Terms

Evaluates ISDA Master Agreement provisions with close-out netting, termination events, and credit support annexes.

## When To Use

- Reviewing an ISDA Master Agreement (1992 or 2002 form) before execution or amendment
- Assessing Credit Support Annex (CSA) terms for margin adequacy, eligible collateral, and valuation mechanics
- Evaluating close-out netting enforceability across jurisdictions for a new counterparty relationship
- Comparing documentation terms across a portfolio of ISDA agreements for consistency or risk concentration
- Analyzing Additional Termination Events (ATEs), cross-default thresholds, or bespoke schedule provisions
- Pre-trade documentation risk assessment for a new product type or counterparty entity

## Inputs To Gather

- **ISDA Master Agreement**: Identify form year (1992 vs. 2002) and the full Schedule with Part 1–5 elections
- **Credit Support Annex/Deed**: CSA type (English law title-transfer vs. New York law pledge), including any regulatory VM/IM annexes (2016 VM CSA, 2018 IM CSA)
- **Counterparty Information**: Entity type (bank, fund, sovereign, corporate, SPV), jurisdiction of incorporation, netting opinion coverage status
- **Transaction Scope**: Product types traded or contemplated (rates, FX, credit, equity, commodities) and notional range
- **Existing Amendments**: Any side letters, amendment agreements, or protocol adherences (e.g., ISDA 2020 IBOR Fallbacks Protocol)
- **Internal Credit Policies**: Firm-specific thresholds, approved collateral schedules, and risk appetite parameters

## Workflow

1. **Identify Agreement Architecture**
   - Confirm Master Agreement form year and governing law election
   - Map the Schedule elections: specified entities, specified transactions, cross-default/cross-acceleration triggers, credit event upon merger provisions
   - Note whether the agreement uses Section 6(e) Market Quotation/Loss (1992) or Close-out Amount (2002) methodology

2. **Analyze Termination & Default Provisions**
   - Review Events of Default: confirm Threshold Amounts for cross-default, Specified Indebtedness definitions, cure periods
   - Evaluate Additional Termination Events: NAV decline triggers, ratings downgrades, key-person clauses, change-of-control provisions
   - Check Automatic Early Termination applicability — required in certain jurisdictions for netting enforceability [VERIFY: jurisdiction-specific netting opinion requirements]
   - Assess designation rights for Affected Party vs. Defaulting Party and any asymmetry

3. **Evaluate Close-Out Netting**
   - Confirm whether ISDA netting opinions cover the counterparty's jurisdiction of incorporation and relevant insolvency regime
   - For multi-branch structures, verify netting across branches and Multibranch Party elections in Part 4
   - Identify any carve-outs from single-agreement netting (e.g., separate Transactions excluded from close-out)
   - Flag jurisdictions where netting enforceability is qualified or absent [VERIFY: current ISDA netting opinion status for counterparty jurisdiction]

4. **Review Credit Support Annex Terms**
   - Map collateral framework: Independent Amounts, Threshold, Minimum Transfer Amount, Rounding
   - Catalog Eligible Collateral and applicable haircuts/valuation percentages — compare against internal collateral policy
   - Check Valuation Date frequency, Notification Time, and dispute resolution mechanics
   - For regulatory margin annexes: confirm compliance with IM/VM requirements, custodian arrangements, and eligible collateral under applicable rules [VERIFY: phase-in timing for initial margin requirements based on AANA]
   - Assess rehypothecation rights (English law CSA) vs. pledge structure limitations (New York law CSA)

5. **Flag Documentation Risk**
   - Identify asymmetric provisions favoring one party (one-way ATEs, asymmetric thresholds, unilateral amendment rights)
   - Highlight missing or incomplete elections (blank Schedule fields, undefined Specified Entities)
   - Note outdated fallback provisions (e.g., pre-IBOR transition language without protocol adherence)
   - Assess consistency between ISDA terms and any related GMRA, GMSLA, or prime brokerage documentation

## Output

Structure the analysis report with:

- **Executive Summary**: Counterparty name, agreement form year, governing law, and top 3–5 documentation risks ranked by severity
- **Provision-by-Provision Analysis**: Table or structured list covering each key election with current terms, market-standard benchmark, and risk rating (Low / Medium / High)
- **Close-Out Netting Assessment**: Enforceability status with jurisdiction-specific notes and any conditions or qualifications
- **CSA Terms Summary**: Collateral matrix showing eligible assets, haircuts, thresholds, and MTA for each party; regulatory compliance status
- **Risk Flags & Recommendations**: Prioritized list of issues with recommended remediation actions (renegotiation points, protocol adherence, amendment drafting)
- **Open Items**: Any provisions requiring [VERIFY] confirmation, missing documents, or pending netting opinion updates

## Quality Checks

- Confirm all Schedule Part 1–5 elections are addressed — no blank or ambiguous fields left unanalyzed
- Verify form year is correctly identified (1992 Loss/Market Quotation vs. 2002 Close-out Amount methodology)
- Cross-check that CSA haircuts and eligible collateral align with current regulatory requirements for VM/IM
- Ensure netting opinion coverage is current (within 12–18 months) and matches the counterparty's actual jurisdiction
- Validate that cross-default Threshold Amounts are consistent with the counterparty's credit profile and outstanding indebtedness
- Confirm any referenced protocols or amendments are accurately reflected in the analysis
- Flag any provision where jurisdiction-specific rules override standard ISDA terms with [VERIFY] markers
