---
name: tracking-regulatory-changes
description: Monitors regulatory developments with impact assessment, gap analysis, and implementation timeline planning. Use when tracking regulatory changes, assessing compliance gaps, or planning implementation.
tags:
  - monitoring
  - financial-compliance
  - compliance
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Regulatory Compliance
    - Financial Regulation
    - Compliance
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---
# Tracking Regulatory Changes

Monitors regulatory developments with impact assessment, gap analysis, and implementation timeline planning.

## When To Use

- A new rule, amendment, or guidance document has been proposed or finalized by a regulatory body (SEC, CFTC, CFPB, OCC, Fed, FDIC, state regulators, or international equivalents)
- An existing compliance program needs a gap analysis against upcoming requirements
- Leadership needs an impact assessment before a compliance effective date
- The organization must build or update an implementation timeline for one or more regulatory changes
- Periodic regulatory horizon scanning is required (quarterly, semi-annual)

## Inputs To Gather

- **Regulatory source**: Agency name, rule/release number, Federal Register citation or equivalent publication reference
- **Effective and compliance dates**: Proposal date, comment period deadline, final rule date, phased compliance dates [VERIFY against current Federal Register or agency website]
- **Affected business lines**: Products, services, entity types, and customer segments in scope
- **Current compliance posture**: Existing policies, procedures, controls, and prior exam findings relevant to the change
- **Stakeholder map**: Compliance, legal, operations, technology, business line owners, and board/committee reporting lines
- **Risk appetite and materiality thresholds**: What level of gap triggers escalation versus routine remediation

## Workflow

1. **Catalog the change**
   - Record the rule title, issuing agency, citation, and summary of requirements
   - Classify by change type: new requirement, amendment to existing rule, interpretive guidance, enforcement action signaling new expectations, or rescission
   - Tag by regulatory domain: capital/liquidity, consumer protection, BSA/AML, data privacy, market conduct, reporting/disclosure, corporate governance [VERIFY categories against the organization's regulatory taxonomy]

2. **Assess impact**
   - Map each new or modified requirement to affected business processes, systems, and existing controls
   - Rate impact severity: High (material policy/system changes, board approval needed), Medium (procedural updates, training required), Low (minor documentation updates)
   - Identify cross-regulatory overlap — determine whether the change interacts with other pending rules (e.g., a new SEC disclosure rule may also affect PCAOB audit standards)
   - Estimate resource requirements: personnel hours, technology spend, third-party vendor changes

3. **Perform gap analysis**
   - For each requirement, document the current state, the required end state, and the specific gap
   - Distinguish between gaps that need new controls versus enhancements to existing controls
   - Flag areas where current practices exceed the new requirement (potential efficiency gains)
   - Note any ambiguities in the rule text that require interpretation — mark with [VERIFY] and recommend seeking regulatory counsel or submitting a comment/no-action request

4. **Build implementation timeline**
   - Work backward from the compliance effective date, building milestones for: policy drafting, technology changes, testing/validation, training, and go-live
   - Assign owners to each milestone
   - Identify dependencies (e.g., vendor readiness, data migration, parallel regulatory changes with overlapping deadlines)
   - Build in buffer for regulatory delays, exam prep, or internal approval cycles
   - Set interim checkpoints for progress reporting to compliance committee or board

5. **Document and report**
   - Produce the tracking report consolidating catalog entry, impact rating, gap analysis, and timeline
   - Include a dashboard-ready summary: rule name, status (proposed/final/effective), impact rating, implementation % complete, owner, next milestone date
   - Flag items approaching deadline with incomplete remediation as escalation items

## Output

Deliver a **Regulatory Change Tracking Report** containing:

- **Executive summary**: Count of tracked changes, high-impact items, overdue milestones, and upcoming deadlines within the next 90 days
- **Change catalog table**: Rule ID, title, agency, status, effective date, impact rating, assigned owner
- **Detailed impact and gap analysis** (per change): Current-state description, gap description, remediation action items, resource estimate
- **Implementation timeline**: Gantt-style or milestone table with dates, owners, dependencies, and completion status
- **Escalation register**: Items flagged for leadership attention due to high impact, tight timelines, ambiguous requirements, or resource constraints
- **Horizon scan**: Upcoming proposed rules or agency agenda items that may require future tracking

## Quality Checks

- Every tracked change cites a specific regulatory source (Federal Register citation, agency release number, or equivalent) — no unsourced entries
- Effective dates and compliance deadlines are verified against primary sources, not secondary summaries [VERIFY]
- Impact ratings are supported by documented rationale, not assigned arbitrarily
- Gap analysis entries distinguish between confirmed gaps and areas pending further interpretation — the latter are marked [VERIFY]
- Implementation timelines account for dependencies; no milestone is assigned a due date earlier than its predecessor
- Stakeholder owners are named for every action item — no orphan tasks
- The report states its as-of date and the date range of the regulatory scan period
- Jurisdictional scope is explicit (federal, specific states, international) [VERIFY that scope matches the organization's actual regulatory footprint]
