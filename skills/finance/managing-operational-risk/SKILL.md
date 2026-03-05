---
name: managing-operational-risk
description: Structures operational risk assessment with loss event classification, RCSA, and KRI monitoring. Use when managing operational risk, conducting risk assessments, or tracking key risk indicators.
tags:
  - management
  - risk-management
  - risk
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
# Managing Operational Risk

Structures operational risk assessment with loss event classification, Risk and Control Self-Assessment (RCSA), and Key Risk Indicator (KRI) monitoring for enterprise operational risk programs.

## When To Use

- Building or refreshing an operational risk framework aligned to Basel II/III categories
- Conducting periodic RCSA cycles across business units
- Classifying and analyzing internal loss events or near-misses
- Designing or recalibrating KRI dashboards and escalation thresholds
- Preparing operational risk reporting for board, risk committee, or regulators
- Evaluating residual risk after control changes or process redesigns

## Inputs To Gather

- **Loss event data**: Internal loss history with dates, amounts, business lines, and Basel event-type classifications (internal fraud, external fraud, employment practices, clients/products, damage to physical assets, business disruption, execution/delivery/process management) [VERIFY: confirm whether the organization uses standard Basel categories or a proprietary taxonomy]
- **RCSA inventory**: Current risk register with inherent risk ratings, control descriptions, control effectiveness scores, and residual risk ratings
- **KRI definitions**: Existing indicator catalog with metric definitions, data sources, collection frequency, and threshold levels (green/amber/red)
- **Organizational context**: Business line structure, material processes, outsourcing arrangements, and recent change events (system migrations, restructurings, product launches)
- **Appetite and tolerance statements**: Board-approved operational risk appetite, tolerance limits, and any regulatory capital requirements [VERIFY: check if the firm is subject to standardized approach, basic indicator approach, or AMA/SMA for op-risk capital]
- **Prior audit/exam findings**: Internal audit reports, regulatory examination results, and open remediation items related to operational risk

## Workflow

1. **Scope and segment** — Define assessment boundaries by business line, legal entity, or process. Map each segment to Basel Level 1 and Level 2 event-type categories. Confirm which risk appetite statements apply.

2. **Classify loss events** — For each reported loss or near-miss:
   - Assign Basel event-type category and sub-category
   - Record gross loss, recoveries, and net loss
   - Tag root cause (people, process, systems, external)
   - Flag boundary events with credit, market, or insurance risk
   - Note whether the event is above the reporting threshold [VERIFY: threshold amount varies by institution]

3. **Conduct RCSA** — For each in-scope process or risk:
   - Identify inherent risk using frequency x severity matrix (e.g., 5x5 scale)
   - Document key controls with type (preventive/detective), owner, and automation level
   - Assess control design adequacy and operating effectiveness
   - Calculate residual risk rating; compare to risk appetite
   - Flag any residual risk that exceeds tolerance as requiring action plan

4. **Define and calibrate KRIs** — For each material risk:
   - Select leading indicators (predictive) and lagging indicators (outcome-based)
   - Set thresholds: green (within appetite), amber (approaching tolerance), red (breach)
   - Specify data source, collection frequency, and responsible owner
   - Back-test thresholds against historical loss data where available
   - Document escalation path for amber and red breaches

5. **Aggregate and report** — Compile findings into a management report:
   - Executive summary with top risks, emerging risks, and trend direction
   - Loss event summary by category with period-over-period comparison
   - RCSA heat map showing residual risk concentrations
   - KRI dashboard with current status, trend arrows, and breach count
   - Action item tracker with owners, due dates, and status
   - Capital impact summary if applicable [VERIFY: confirm capital methodology in use]

6. **Review and challenge** — Present to risk committee or designated governance body. Document challenges raised, decisions taken, and any appetite recalibrations agreed.

## Output

A structured operational risk management report containing:

- **Loss event register** with Basel classification, root-cause tags, and net loss figures
- **RCSA summary matrix** showing inherent risk, control effectiveness, and residual risk per process/business line
- **KRI scorecard** with current values, threshold status, trends, and escalation notes
- **Heat map** visualizing residual risk by business line and event category
- **Action plan log** for risks exceeding tolerance, with owners and deadlines
- **Narrative commentary** on risk trends, emerging threats (e.g., cyber, third-party, conduct), and recommended mitigations

## Quality Checks

- Every loss event is assigned exactly one Basel Level 1 event-type category — no unclassified items remain
- RCSA residual risk ratings are mathematically consistent with inherent risk minus documented control effectiveness; no residual rating exceeds inherent rating
- KRI thresholds are calibrated against actual loss experience or documented expert judgment — not set arbitrarily
- All risks rated above appetite have a corresponding action plan with an identified owner and target date
- Boundary events (overlapping credit/market/op-risk) are clearly flagged and allocation methodology is stated [VERIFY: confirm boundary-event treatment policy]
- Report period, data cut-off date, and any known data gaps are explicitly disclosed
- Terminology is consistent with the organization's risk taxonomy and any applicable regulatory framework (Basel, COSO, ISO 31000)
