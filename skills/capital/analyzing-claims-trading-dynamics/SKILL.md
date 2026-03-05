---
name: analyzing-claims-trading-dynamics
description: Evaluates claims trading market with trading levels, holder identification, and blocking position analysis. Use when analyzing claims markets, tracking distressed debt trading, or evaluating ad hoc group dynamics.
tags:
  - analysis
  - distressed-and-restructuring
  - trading
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
# Analyzing Claims Trading Dynamics

## When To Use

- Mapping the secondary market for claims against a debtor in or approaching Chapter 11
- Identifying whether an ad hoc group or single holder is building a blocking position in a particular class
- Evaluating trading levels to assess market-implied recovery expectations
- Preparing for plan negotiations by understanding creditor composition shifts
- Advising a potential claims purchaser on entry pricing, liquidity, and positional risk

## Inputs To Gather

- **Claims register / transfer ledger**: Court-filed Rule 3001 claims and any Rule 3001(e) notices of transfer
- **Trading desk color / broker runs**: Bid/ask levels, volume indications, and recent prints for traded claims or debt tranches
- **Debtor's schedules and statement of financial affairs**: Scheduled claim amounts per creditor, disputed vs. undisputed
- **Capital structure and intercreditor documents**: Priorities, subordination, adequate protection terms
- **Ad hoc group disclosures**: Rule 2019 statements showing members, economic interests, and acquisition dates/prices
- **Plan or term sheet (if filed)**: Proposed treatment by class and any toggle/election mechanisms
- **Relevant docket entries**: Objections to claims, estimation motions, DIP financing orders affecting recoveries

## Workflow

1. **Build the claims universe**
   - Compile all filed proofs of claim by class (secured, priority, general unsecured, intercompany, equity interests)
   - Cross-reference with debtor's schedules to flag unliquidated, contingent, or disputed claims
   - Note aggregate face amount per class and the one-third-in-amount blocking threshold [VERIFY: confirm blocking threshold under applicable plan — some plans use two-thirds in amount plus majority in number per §1126(c)]

2. **Map holder positions**
   - Track Rule 3001(e) transfer notices to identify claims buyers and the chain of ownership
   - Parse Rule 2019 disclosures for ad hoc group membership, acquisition dates, and cost basis ranges
   - Flag any single holder or coordinated group approaching or exceeding the blocking position threshold in any class

3. **Assess trading levels and liquidity**
   - Record recent bid/ask spreads and executed trade prices (cents on the dollar)
   - Calculate implied recovery at current trading levels versus proposed plan distributions
   - Note market depth: Is trading thin (occasional BWIC/OWIC) or active with regular two-way flow?
   - Identify divergence between trading levels across tranches, which may signal differing recovery expectations or information asymmetry

4. **Analyze blocking position dynamics**
   - Determine if any party holds or is assembling a blocking position in a class needed for confirmation
   - Evaluate whether the blocking holder's economic incentives align with or oppose the debtor's plan strategy
   - Consider whether the debtor has a cram-down path under §1129(b) if a class rejects, and assess the fair-and-equitable / unfair-discrimination standards applicable [VERIFY: jurisdiction-specific cram-down precedent]

5. **Evaluate strategic implications**
   - Assess how claims migration affects negotiation leverage among the debtor, committee, and major holders
   - Identify potential gift or settlement structures that might unlock support from blocking holders
   - Flag any claims that are subject to pending objections, estimation, or subordination motions — these affect both trading value and voting power

6. **Synthesize findings**
   - Produce a claims map showing position sizes, holder identities (where public), and trading levels
   - Summarize blocking position risk per class
   - Highlight key uncertainties that could shift the trading or voting landscape

## Output

- **Claims Trading Summary**: Table of claim classes with aggregate face amounts, number of holders, and current trading levels (bid/ask/last trade)
- **Holder Position Map**: Identification of material holders per class, including known ad hoc group members, with position sizes as a percentage of class
- **Blocking Position Analysis**: Per-class assessment of whether any holder or group has or is approaching a blocking position, with strategic commentary on likely negotiation posture
- **Recovery Implied by Market**: Comparison of trading-level-implied recoveries against plan-proposed recoveries, with commentary on spread drivers
- **Risk Flags**: List of pending claim objections, estimation motions, or equitable subordination actions that could alter the landscape

## Quality Checks

- Confirm all Rule 3001(e) transfers referenced are from the official docket — do not rely on broker hearsay for ownership data
- Verify blocking threshold math against the specific plan's classification structure and §1126(c)/(d) requirements
- Cross-check trading levels against at least two independent sources (broker runs, pricing services) where available
- Flag any holder whose position may trigger HSR, beneficial ownership, or securities law disclosure obligations [VERIFY: applicable reporting thresholds under Hart-Scott-Rodino and Exchange Act §13(d)]
- Mark all cost-basis and implied-recovery figures as estimates unless sourced from confirmed trade confirmations
- Note where the analysis depends on assumptions about claim allowance amounts for disputed or unliquidated claims
