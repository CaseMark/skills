---
name: managing-best-execution-compliance
description: Structures best execution monitoring with venue analysis, systematic internalization assessment, and regulatory compliance documentation. Use when managing best execution, documenting execution decisions, or conducting venue analysis.
tags:
  - management
  - public-markets-and-trading
  - compliance
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Trading
    - Market Making
    - Execution
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Best Execution Compliance

Structures best execution monitoring with venue analysis, systematic internalization assessment, and regulatory compliance documentation.

## When To Use

- Conducting periodic best execution reviews (quarterly, annual, or ad hoc)
- Evaluating execution venue performance and routing decisions
- Assessing systematic internalizer (SI) obligations and thresholds
- Responding to regulatory inquiries on order execution quality
- Onboarding new execution venues or broker-dealers
- Documenting rationale for execution arrangements after material changes (new asset classes, venue outages, market structure shifts)

## Inputs To Gather

- **Order flow data**: Volume, notional value, and order types by asset class, venue, and time period
- **Execution quality metrics**: Fill rates, price improvement/disimprovement, effective spread vs. quoted spread, latency, and market impact
- **Venue fee schedules**: Maker/taker fees, rebates, tiered pricing, and payment-for-order-flow (PFOF) arrangements
- **Regulatory framework**: Applicable regime — MiFID II RTS 27/28 reports, SEC Rule 606, FINRA 5310, or equivalent [VERIFY jurisdiction-specific requirements]
- **Prior review reports**: Previous best execution committee minutes, exception logs, and remediation items
- **Client classification**: Retail vs. professional vs. eligible counterparty breakdown, as execution factors weighting differs by client type
- **Benchmark selection**: Reference prices used (arrival price, VWAP, TWAP, midpoint, close)

## Workflow

1. **Define review scope**
   - Specify asset classes (equities, fixed income, FX, listed derivatives, OTC derivatives)
   - Set review period and confirm data completeness across all venues
   - Identify any venue outages, market disruptions, or corporate actions that affected execution during the period

2. **Aggregate and validate execution data**
   - Pull execution reports from OMS/EMS and venue-provided RTS 27-equivalent data
   - Reconcile order counts and notional values against internal records
   - Flag data gaps or mismatches — mark unresolved items with [VERIFY]

3. **Conduct venue analysis**
   - Rank venues by execution quality factors: price, cost, speed, likelihood of execution, settlement reliability
   - Weight factors according to client type and order characteristics (size, urgency, instrument liquidity)
   - Compare venue performance against the prior period and against peer venues
   - Identify venues where quality has materially deteriorated and document root cause

4. **Assess systematic internalization**
   - Calculate SI threshold metrics: frequency, systematic basis, and substantial scale for each instrument class [VERIFY thresholds per current ESMA or local regulator guidance]
   - Determine whether the firm triggers SI status for any instrument
   - If SI status applies, confirm pre-trade transparency and quote obligations are met

5. **Evaluate conflicts of interest**
   - Review PFOF arrangements, affiliated venue routing, and soft-dollar benefits
   - Confirm that conflicts are disclosed and do not compromise execution quality
   - Document any instances where conflict mitigation controls were triggered

6. **Document execution decisions**
   - Record the rationale for venue selection, routing logic changes, and any deviations from standard execution policy
   - Note exceptions where execution fell outside acceptable parameters and the remedial action taken
   - Prepare committee-ready summary with recommendations (add venues, remove underperformers, adjust routing weights)

7. **Produce regulatory deliverables**
   - Generate required disclosures: RTS 28 top-five venue reports, SEC Rule 606 order routing reports, or equivalent [VERIFY applicable filings]
   - Ensure disclosures are published within regulatory deadlines
   - Archive supporting data with audit trail for the mandated retention period [VERIFY retention period — typically 5–7 years]

## Output

- **Best Execution Review Report**: Period-over-period venue scorecards, factor-weighted rankings, exception summary, SI threshold status, and conflict-of-interest review
- **Regulatory Disclosure Package**: Formatted RTS 28 / Rule 606 reports or equivalent, ready for publication or filing
- **Action Items Log**: Specific remediation tasks with owners, deadlines, and escalation triggers
- **Committee Minutes Template**: Pre-populated agenda, findings, and resolution language for the best execution committee

## Quality Checks

- All execution quality metrics tie back to source OMS/EMS data — no manual overrides without documented justification
- Venue rankings reflect the correct factor weightings for each client category
- SI threshold calculations use current regulatory parameters, not stale figures — mark [VERIFY] if parameter source is older than 6 months
- Conflicts-of-interest section addresses every affiliated venue and PFOF arrangement in scope
- Regulatory filings match the format and content requirements of the applicable jurisdiction
- Prior-period exceptions are tracked to closure — open items carried forward with updated status
- Report language avoids conclusory compliance statements; instead, states factual findings and flags items requiring further review
