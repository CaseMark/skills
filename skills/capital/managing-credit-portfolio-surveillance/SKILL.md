---
name: managing-credit-portfolio-surveillance
language: en
description: Monitors credit portfolio health with rating migration tracking, watchlist management, and early warning indicator analysis. Use when conducting portfolio surveillance, managing credit watchlists, or tracking credit migration.
tags:
  - management
  - credit-and-institutional-lending
  - portfolio
  - credit
metadata:
  author: casemark
  practice_areas:
    - Credit Markets
    - Leveraged Lending
    - Direct Lending
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Credit Portfolio Surveillance

Monitors credit portfolio health with rating migration tracking, watchlist management, and early warning indicator analysis.

## When To Use

- Conducting periodic (weekly, monthly, quarterly) portfolio surveillance reviews
- Tracking internal rating migrations and identifying downgrade trends across the book
- Managing credit watchlists and escalating names approaching default or restructuring triggers
- Analyzing early warning indicators (financial covenant headroom erosion, payment delays, sector stress)
- Preparing portfolio health reports for credit committees, investors, or regulators
- Responding to market dislocations or sector-wide credit events requiring rapid portfolio triage

## Inputs To Gather

- **Portfolio data**: Obligor list with current internal ratings, exposure amounts (funded/unfunded), facility types, maturity dates, and spread/pricing
- **Financial statements**: Most recent borrower financials (income statement, balance sheet, cash flow) and compliance certificates
- **Covenant tracking**: Current covenant levels vs. actuals, headroom calculations, and amendment/waiver history
- **Rating history**: Internal rating migration history per obligor (at least trailing 4 quarters)
- **Market data**: CDS spreads, secondary loan trading levels, sector indices, and peer comparisons where available
- **Watchlist**: Current watchlist with entry dates, reasons for inclusion, and assigned action plans
- **External ratings**: Agency ratings (Moody's/S&P/Fitch) and any recent rating actions or outlook changes [VERIFY: confirm data vendor access and permissioned use]

## Workflow

1. **Refresh portfolio snapshot**
   - Pull current exposure data by obligor, facility, and asset class
   - Reconcile against prior period to identify new additions, paydowns, and maturities
   - Flag any data gaps (missing financials, stale ratings) for follow-up

2. **Run rating migration analysis**
   - Compare current internal ratings against prior quarter and prior year
   - Build a migration matrix showing upgrade/downgrade/stable counts and exposure-weighted percentages
   - Identify names with multi-notch downgrades or consecutive-quarter deterioration
   - Cross-reference internal ratings against external agency actions for divergence

3. **Update watchlist**
   - Review existing watchlist names: confirm status, update action items, and remove resolved credits
   - Add new names triggered by: covenant breach or thin headroom (<15%), missed or late payments, rating downgrade below threshold, adverse market signals (widening CDS, trading below 90), or material adverse developments (litigation, management turnover, sector distress)
   - Assign watchlist category (Watch, Concern, Default/Impaired) and responsible analyst
   - Document rationale for each addition or removal

4. **Analyze early warning indicators**
   - Calculate leverage and coverage ratio trends (trailing 4 quarters minimum)
   - Track revenue and EBITDA trajectory vs. underwrite case and budget
   - Monitor liquidity position: revolver availability, cash burn rate, upcoming maturities
   - Assess sector-level signals: peer defaults, commodity price moves, regulatory changes [VERIFY: sector-specific stress indicators vary by industry vertical]
   - Flag concentration risk: single-name, sector, geography, and maturity buckets exceeding policy limits

5. **Prepare surveillance report**
   - Summarize portfolio composition: total commitments, outstandings, weighted-average rating, and yield
   - Present rating migration matrix with period-over-period comparison
   - List watchlist additions, removals, and status changes with brief narratives
   - Highlight top risk themes: sector exposures, concentration breaches, covenant trends
   - Include recommended actions: required reserves, impairment candidates, workout referrals, or limit adjustments

6. **Escalate and coordinate**
   - Route impaired or near-default credits to workout/restructuring team
   - Flag policy limit breaches to risk management for remediation plans
   - Prepare materials for credit committee presentation if thresholds are triggered
   - Distribute surveillance report to portfolio managers, risk officers, and investor reporting teams as applicable

## Output

A credit portfolio surveillance report containing:
- **Portfolio summary table**: Exposure by rating bucket, facility type, sector, and maturity
- **Rating migration matrix**: Period-over-period with notch-level detail and exposure weighting
- **Watchlist**: Current names with category, entry date, key risk factors, and action plan
- **Early warning dashboard**: Flagged obligors with specific trigger indicators and severity
- **Concentration analysis**: Single-name, sector, and geographic exposures vs. policy limits
- **Recommended actions**: Specific next steps per flagged credit (reserve adjustment, amendment request, workout referral, rating review)

## Quality Checks

- Confirm all obligor exposures reconcile to the loan administration system of record
- Verify internal ratings reflect the most recent financial data available (no stale ratings older than one quarter without documented exception)
- Ensure watchlist entries include documented rationale and assigned ownership
- Check migration matrix math: row totals must equal prior-period rating distribution; column totals must equal current-period distribution
- Validate that covenant headroom calculations use the correct defined terms from each credit agreement [VERIFY: defined EBITDA adjustments vary by deal—confirm add-backs and exclusions per agreement]
- Confirm concentration metrics use the policy-defined exposure measure (committed vs. funded vs. risk-weighted) [VERIFY: exposure definition may differ across internal policies]
- Flag any obligor where internal and external ratings diverge by two or more notches for reconciliation review
