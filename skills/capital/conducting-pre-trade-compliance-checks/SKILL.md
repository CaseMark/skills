---
name: conducting-pre-trade-compliance-checks
description: Structures pre-trade compliance with restricted list screening, position limits, and regulatory constraint verification. Use when running pre-trade compliance, screening restricted securities, or verifying trading limits.
tags:
  - process
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
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Pre Trade Compliance Checks

Structures pre-trade compliance workflows covering restricted list screening, position and concentration limit verification, and regulatory constraint checks before order submission.

## When To Use

- Before submitting any order to verify the trade does not violate firm or regulatory constraints
- When onboarding a new security or counterparty to confirm it is not on a restricted or watch list
- When a trader or PM requests a compliance greenlight on a proposed position change
- During periodic review of standing orders or strategy-level allocations against updated restricted lists
- When market conditions or corporate events (e.g., MNPI receipt, blackout periods) trigger re-screening

## Inputs To Gather

- **Proposed trade details**: security identifier (CUSIP/ISIN/ticker), side (buy/sell/short), notional or share quantity, order type, account/fund
- **Restricted and watch lists**: firm restricted list, issuer-level watch list, MNPI-flagged names, sanctions lists (OFAC SDN, EU consolidated list) [VERIFY applicable sanctions regimes]
- **Current portfolio positions**: existing holdings in the security and correlated instruments across all accounts
- **Position and concentration limits**: regulatory limits (e.g., 13D/13G 5% beneficial ownership threshold, Reg SHO locate requirements), fund mandate limits, internal risk limits, single-issuer concentration caps [VERIFY fund-specific or strategy-specific thresholds]
- **Regulatory calendars**: blackout windows, quiet periods, earnings-related trading restrictions
- **Client or account restrictions**: IPS constraints, ESG exclusion lists, sector/country prohibitions

## Workflow

1. **Identify the trade and account context**
   - Confirm security identifier, direction, size, and target account
   - Determine whether the account is discretionary, advisory, or proprietary — each may carry different compliance rules

2. **Screen against restricted and watch lists**
   - Check the security and its issuer against the firm restricted list and any MNPI-flagged names
   - Screen the counterparty (if OTC) and the issuer against OFAC SDN, sectoral sanctions, and any jurisdiction-specific denied-party lists [VERIFY which sanctions programs apply]
   - If the security is on the watch list (not restricted), flag for enhanced monitoring but do not auto-block
   - Document the list version/date used for screening

3. **Verify position and ownership limits**
   - Calculate the pro-forma position (current holdings + proposed trade) across all accounts under common control
   - Check against regulatory ownership thresholds: 5% beneficial ownership (13D/13G), 10% short-swing profit (Section 16), exchange position limits [VERIFY exchange-specific limits for derivatives]
   - Confirm the trade does not breach fund-level concentration limits (single issuer, sector, geography, liquidity bucket)

4. **Check short-sale and locate compliance**
   - For short sales, confirm a valid locate has been obtained per Reg SHO Rule 203(b) [VERIFY if the security is on the threshold list or is hard-to-borrow]
   - Verify the security is not subject to an active short-sale circuit breaker (Rule 201 alternative uptick)

5. **Validate against trading window and blackout restrictions**
   - Confirm the firm is not in a blackout or quiet period for the issuer
   - Cross-check personal trading pre-clearance if the order is from a covered person under the firm's Code of Ethics

6. **Apply account-level and mandate restrictions**
   - Verify the trade is consistent with the investment policy statement, prospectus limits, or client guidelines
   - Screen against ESG exclusion lists and sector/country prohibitions if applicable

7. **Record the compliance determination**
   - Stamp the order with a compliance pass/fail/conditional result and timestamp
   - If conditional, specify the remediation needed (e.g., reduce size below threshold, obtain locate confirmation)
   - Archive the screening evidence for audit trail purposes

## Output

- **Compliance determination**: clear pass, fail (with blocking reason), or conditional approval with required remediation steps
- **Screening log**: list of each check performed, data sources used, list versions/dates, and result per check
- **Flagged items**: any watch-list hits, near-limit warnings, or items requiring enhanced monitoring
- **Exception escalation memo** (if needed): narrative explaining the issue, relevant rule or policy, and recommended resolution for compliance officer review

## Quality Checks

- Confirm all security identifiers were resolved correctly — ticker aliases and class shares can cause false negatives
- Verify restricted list and sanctions list versions are current (stale lists are a common audit finding)
- Ensure pro-forma position calculations include all accounts under common beneficial ownership, not just the requesting account
- Cross-check that the compliance timestamp precedes the order submission timestamp in the audit trail
- For any [VERIFY] items, confirm resolution before releasing the order — do not default to pass on unresolved flags
- Escalate to the Chief Compliance Officer when a proposed trade is within 80% of a hard regulatory threshold or involves a watch-list name with active MNPI concerns
