---
name: managing-fund-compliance-monitoring
description: Structures investment compliance testing with guideline monitoring and breach reporting. Use when monitoring investment guidelines, testing compliance, or reporting breaches.
tags:
  - management
  - fund-operations
  - compliance
  - investment
metadata:
  author: casemark
  practice_areas:
    - Fund Administration
    - Investment Operations
    - Fund Accounting
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Fund Compliance Monitoring

Structures investment compliance testing with guideline monitoring and breach reporting.

## When To Use

- Setting up or reviewing pre-trade and post-trade compliance testing frameworks
- Monitoring portfolio holdings against investment policy statement (IPS) guidelines, prospectus limits, or regulatory constraints
- Investigating and documenting guideline breaches (active or passive)
- Producing periodic compliance status reports for fund boards, trustees, or regulators
- Onboarding a new fund or strategy into the compliance monitoring system
- Responding to regulatory inquiries about investment guideline adherence

## Inputs To Gather

- **Investment guidelines source**: IPS, prospectus, side letters, board resolutions, or regulatory orders defining permissible investments, concentration limits, and prohibited holdings
- **Portfolio data**: Current holdings, NAV, sector/geography/asset-class breakdowns, counterparty exposures, liquidity profiles
- **Guideline parameter schedule**: Specific quantitative limits (e.g., max 5% single issuer, max 25% sector, min credit rating BBB-) and qualitative restrictions (e.g., no tobacco, no sanctioned entities)
- **Prior breach log**: History of past breaches, remediation actions taken, and cure deadlines
- **Testing frequency**: Daily, weekly, monthly — per guideline category
- **Escalation contacts**: Portfolio manager, CCO, fund board representative, external compliance counsel

## Workflow

1. **Map guidelines to testable rules**
   - Parse each investment guideline into a discrete, testable compliance rule (e.g., "single-issuer equity exposure ≤ 5% of NAV")
   - Classify each rule by type: concentration limit, asset-class restriction, credit quality floor, liquidity requirement, leverage cap, prohibited investment, diversification test
   - Note whether each rule applies pre-trade, post-trade, or both
   - Flag any guideline language that is ambiguous or requires interpretation [VERIFY with fund counsel]

2. **Configure monitoring parameters**
   - Set quantitative thresholds with hard limits and warning bands (e.g., hard limit 5%, warning at 4.5%)
   - Define the NAV denominator and valuation methodology for percentage-based tests [VERIFY — some guidelines use gross assets, others use net assets]
   - Establish look-through requirements for fund-of-funds, ETF holdings, or derivative exposures
   - Specify cure periods for passive breaches caused by market movements vs. active breaches from trades

3. **Run compliance tests**
   - Execute each mapped rule against current portfolio data
   - For pre-trade tests: validate proposed trades against guidelines before execution
   - For post-trade tests: scan end-of-day holdings against all applicable rules
   - Record pass/fail status, current value vs. limit, and margin to breach for each test
   - Apply look-through analysis where required for underlying exposures

4. **Detect and classify breaches**
   - Identify any rule where the current exposure exceeds the hard limit
   - Classify each breach: **active** (caused by a new trade) vs. **passive** (caused by market movement, redemptions, or corporate actions)
   - Determine severity: technical/de minimis vs. material
   - Check whether the breach falls within a defined cure period or requires immediate remediation
   - Cross-reference against prior breach log for repeat patterns

5. **Escalate and remediate**
   - Notify the portfolio manager immediately for active breaches
   - Escalate to the CCO per the fund's breach escalation matrix
   - Document proposed remediation plan with target cure date
   - For passive breaches within cure period, monitor daily until resolved
   - If remediation requires trading, confirm the corrective trade itself does not trigger a new breach

6. **Report**
   - Produce compliance status report covering all tested guidelines, pass/fail results, and open breaches
   - Include breach detail section: date detected, classification, current exposure vs. limit, remediation status, expected cure date
   - Summarize trends: new breaches this period, cured breaches, aging breaches, repeat breaches
   - Note any guideline changes, new fund onboardings, or parameter updates since last report
   - Append attestation language for board or trustee sign-off [VERIFY — attestation format varies by jurisdiction and fund structure]

## Output

The compliance monitoring report should include:

- **Dashboard summary**: Total rules tested, pass count, warning count, breach count
- **Breach register**: Each open breach with classification, severity, exposure detail, cure deadline, and remediation owner
- **Guideline-by-guideline results**: Tabular view of every tested rule showing current value, limit, headroom, and status
- **Trend analysis**: Period-over-period breach counts, time-to-cure metrics, repeat-breach flags
- **Action items**: Outstanding remediation tasks with owners and deadlines
- **Regulatory disclosure notes**: Any breaches that may trigger regulatory reporting obligations [VERIFY — reporting thresholds and timelines vary by regulator: SEC, FCA, CSSF, MAS, etc.]

## Quality Checks

- Confirm all investment guidelines from the governing documents are mapped to testable rules — no gaps
- Verify portfolio data is as-of the correct date and reconciles to the fund administrator's records
- Validate that percentage calculations use the correct denominator (gross vs. net assets) per each guideline's terms
- Check that look-through analysis is applied consistently for pooled vehicles and derivatives
- Ensure active vs. passive breach classification is accurate — misclassification affects cure period eligibility
- Confirm escalation timelines were met per the fund's compliance manual
- Review breach descriptions for completeness: a third party should be able to understand the breach without additional context
- Cross-check that remediation actions do not themselves create new compliance issues
