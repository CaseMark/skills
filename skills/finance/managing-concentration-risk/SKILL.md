---
name: managing-concentration-risk
description: Identifies and monitors portfolio concentration across counterparties, sectors, geographies, and instruments. Use when analyzing concentration risk, setting exposure limits, or monitoring concentration breaches.
tags:
  - management
  - risk-management
  - risk
  - portfolio
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
# Managing Concentration Risk

## When To Use

- Evaluating single-name, sector, geographic, or instrument-type exposures against internal limits or regulatory thresholds
- Setting or recalibrating concentration limits for a new portfolio, fund, or business line
- Responding to a limit breach or near-breach event requiring root-cause analysis and remediation
- Preparing board or risk-committee reporting on portfolio diversification posture
- Stress-testing concentration scenarios (e.g., top-5 counterparty default, sector downturn, sovereign event)

## Inputs To Gather

- **Position data**: Current holdings by counterparty, issuer, sector (GICS/ICB), country/region, asset class, and instrument type
- **Exposure metrics**: Gross and net exposures, notional values, mark-to-market, potential future exposure (PFE) where applicable
- **Limit framework**: Existing concentration limits (absolute dollar, percentage of NAV/capital, risk-contribution-based) and any regulatory caps [VERIFY — limits vary by entity type: bank, broker-dealer, insurance company, fund]
- **Correlation and netting data**: Legal netting agreements, collateral held, hedging positions that offset concentration
- **Benchmark or peer data**: Target allocation weights, index composition, or peer-group concentration statistics for comparison
- **Historical breach log**: Prior limit exceedances, waivers granted, and remediation timelines

## Workflow

1. **Map the concentration dimensions**
   - Segment the portfolio across key axes: single-name/counterparty, sector, geography, currency, maturity bucket, instrument type, and rating band
   - Identify connected exposures — aggregate entities under common parent (ultimate-beneficial-owner roll-up) and linked sectors

2. **Compute concentration metrics**
   - Calculate Herfindahl-Hirschman Index (HHI) or equivalent diversification score per dimension
   - Derive top-N exposure shares (e.g., top-1, top-5, top-10 as % of total portfolio or capital)
   - Compute risk-contribution-based concentration using VaR, CVaR, or stress-loss attribution where data supports it
   - Flag any single-name exposure exceeding the large-exposure threshold [VERIFY — e.g., 10% of Tier 1 capital for banks under Basel framework; different for insurance or fund vehicles]

3. **Compare against limits and benchmarks**
   - Map each metric to the applicable internal limit, regulatory cap, or investment-policy guideline
   - Classify status: green (within limit), amber (within warning band, typically 80-90% of limit), red (at or above limit)
   - Where no formal limit exists, benchmark against peer medians or index weights and note the gap

4. **Analyze breaches and near-breaches**
   - For any red or amber status: identify driver (new position, market-move-driven, counterparty upgrade/downgrade, M&A-driven sector reclassification)
   - Determine whether breach is passive (market-driven) or active (trade-driven) — remediation urgency differs
   - Document any existing waivers, temporary limit increases, or approved exception windows

5. **Formulate remediation and monitoring plan**
   - Propose specific actions: position reduction schedule, hedge overlay, limit recalibration, or formal waiver request
   - Set monitoring frequency — daily for active breaches, weekly for amber items, monthly/quarterly for routine review
   - Define escalation path: portfolio manager → CRO → risk committee → board, depending on severity

6. **Produce the concentration risk report**
   - Compile dashboard with heat maps or tables per dimension, trend lines (current vs. prior periods), and limit-utilization gauges
   - Summarize key findings, material breaches, and recommended actions in an executive narrative

## Output

- **Concentration risk dashboard**: Table or heat map showing exposure by dimension, limit, current utilization %, and RAG status
- **Top-N exposure schedule**: Ranked list of largest exposures with counterparty/sector/country, notional, % of portfolio, and limit headroom
- **HHI / diversification scores**: Per-dimension index values with trend vs. prior period
- **Breach register**: Each breach with driver classification, date identified, remediation action, target cure date, and responsible owner
- **Executive summary**: 1-page narrative for risk committee covering material concentrations, limit changes proposed, and forward-looking stress scenarios

## Quality Checks

- Confirm position data is as-of a consistent date and reconciles to official books and records
- Verify ultimate-parent roll-ups are current — stale corporate-hierarchy data inflates or masks concentration
- Cross-check that limit definitions match the approved risk-appetite statement or investment-policy document [VERIFY]
- Ensure gross vs. net exposure treatment is consistent and any netting applied is backed by enforceable legal agreements
- Validate that regulatory concentration thresholds referenced match the applicable jurisdiction and entity charter [VERIFY — Basel large-exposure framework, SEC diversification rules for RICs, Solvency II for insurers]
- Confirm stress scenarios reflect plausible tail events, not just historical replays
- Flag any dimension where data coverage is incomplete (e.g., look-through into fund-of-fund holdings not available) with [VERIFY]
