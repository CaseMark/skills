---
name: managing-dodd-frank-reporting
language: en
description: Structures Dodd-Frank derivatives reporting with trade reporting, position limits, and SEF compliance. Use when managing DFA reporting, submitting trade reports, or ensuring SEF compliance.
tags:
  - management
  - quantitative-finance
  - compliance
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
# Managing Dodd Frank Reporting

Structures Dodd-Frank derivatives reporting with trade reporting, position limits, and SEF compliance.

## When To Use

- Onboarding a new swap dealer or major swap participant to CFTC reporting obligations
- Setting up or auditing trade reporting flows to a Swap Data Repository (SDR)
- Evaluating position limit compliance for physical commodity and economically equivalent swaps
- Ensuring execution on a Swap Execution Facility (SEF) for mandated products
- Preparing for CFTC examinations or responding to deficiency findings
- Transitioning to updated reporting rules (e.g., CFTC Rewrite — Parts 43, 45, and 49 amendments)

## Inputs To Gather

- **Entity classification**: Swap dealer (SD), major swap participant (MSP), financial end-user, or non-financial end-user — determines reporting hierarchy and obligations
- **Product scope**: Asset classes covered (rates, credit, FX, equity, commodities) and specific swap categories
- **SDR relationships**: Which SDRs the firm reports to (e.g., DTCC DDR, ICE Trade Vault, CME SDR) and connectivity method (FpML, CSV, API)
- **Unique Swap Identifier (USI) / Unique Transaction Identifier (UTI)**: Generation methodology and who is the reporting counterparty
- **Position data**: Current open interest by commodity reference contract, including all-months-combined and single-month positions
- **SEF execution records**: Which products are subject to the made-available-to-trade (MAT) determination [VERIFY current MAT product list]
- **Existing compliance gaps**: Prior exam findings, SDR rejection logs, late-reporting metrics

## Workflow

1. **Map reporting obligations by entity and product**
   - Determine reporting counterparty hierarchy (SD > MSP > financial end-user > non-financial end-user)
   - Classify each swap by asset class, cleared vs. uncleared, and whether it is a "publicly reportable swap transaction" under Part 43
   - Identify real-time public reporting vs. regulatory reporting requirements

2. **Validate SDR connectivity and data fields**
   - Confirm all CFTC-required data elements are captured at trade inception (counterparty IDs via LEI, product taxonomy via UPI, valuation data, collateral and margin fields)
   - Verify USI/UTI generation logic and uniqueness controls
   - Test lifecycle event reporting: amendments, novations, terminations, compressions, and portfolio-level valuations
   - [VERIFY] Confirm compliance with current CFTC technical specifications (schema version, field formats, and validation rules)

3. **Assess position limit compliance**
   - Map positions against CFTC federal position limits for the 25 core referenced contracts [VERIFY current contract list and limit levels]
   - Apply netting rules: aggregate positions across related accounts and affiliated entities
   - Document any bona fide hedging exemptions — confirm each meets the enumerated hedging categories under CFTC Rule 150.1
   - Track exchange-set spot-month position limits separately from federal limits
   - Establish pre-trade and intraday position monitoring with automated alerts at threshold levels (e.g., 80%, 90%, 100% of limits)

4. **Confirm SEF execution compliance**
   - Identify all swaps subject to the trade execution requirement (MAT-determined products must execute on a SEF or DCM)
   - Review execution methods: order book, request-for-quote (RFQ) with minimum participant requirements, or block trade exception
   - Verify block trade thresholds and time delays for public reporting [VERIFY current block sizes by product]
   - Ensure pre-trade and post-trade transparency obligations are met

5. **Build reporting controls and exception management**
   - Establish T+1 (or applicable) reporting SLAs with escalation for late or rejected submissions
   - Create reconciliation process: compare internal books and records against SDR-held data at least quarterly
   - Implement error-correction workflows for resubmissions and backloading
   - Document all inter-affiliate swaps and confirm whether the inter-affiliate exemption from clearing/SEF execution applies [VERIFY current no-action relief status]

6. **Compile management report**
   - Summarize reporting volumes by asset class, SDR, and submission status (accepted, rejected, pending)
   - Present position limit utilization dashboard across all monitored contracts
   - Flag open compliance items, remediation timelines, and upcoming regulatory deadlines
   - Include trend analysis on rejection rates, late-reporting incidents, and reconciliation breaks

## Output

- **Dodd-Frank Reporting Status Report** covering:
  - Entity-level obligation matrix (who reports what, to which SDR, under which Part)
  - SDR data quality scorecard (field completeness, rejection rates, timeliness)
  - Position limit utilization summary by core referenced contract
  - SEF execution compliance log with any block trade elections
  - Open items register with owners, deadlines, and risk ratings
  - Recommendations for process or technology improvements

## Quality Checks

- Confirm every reportable swap has a valid LEI for both counterparties — reject submissions with missing or lapsed LEIs
- Verify USI/UTI uniqueness; no duplicates across the reporting population
- Cross-check position limit calculations against independent source (clearing house reports, prime broker statements)
- Validate that all lifecycle events (amendments, partial terminations) are reported within required timeframes
- Ensure real-time public dissemination data has been properly masked for block trades and large notional off-facility swaps
- [VERIFY] Confirm all reporting aligns with the most recent CFTC staff advisories, no-action letters, and rule amendments — Dodd-Frank reporting rules are subject to ongoing revisions
- Flag any product where clearing mandate, SEF execution mandate, or position limit applicability is uncertain for senior compliance review
