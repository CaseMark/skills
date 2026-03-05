---
name: managing-stablecoin-analysis
description: Structures stablecoin evaluation with reserve backing, redemption mechanics, and regulatory classification. Use when analyzing stablecoins, evaluating reserve adequacy, or assessing stablecoin risk.
tags:
  - management
  - financial-technology
  - regulatory
  - risk
metadata:
  author: casemark
  practice_areas:
    - Fintech
    - Payments
    - Digital Banking
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Stablecoin Analysis

Structures stablecoin evaluation covering reserve composition, peg stability mechanisms, redemption infrastructure, and regulatory classification to produce actionable risk assessments for treasury, compliance, and portfolio teams.

## When To Use

- Evaluating a stablecoin for treasury holdings, payment rails, or collateral eligibility
- Conducting due diligence on a stablecoin issuer for partnership or integration
- Assessing reserve adequacy after an attestation report or audit disclosure
- Comparing stablecoins for settlement, lending, or liquidity pool deployment
- Reviewing regulatory exposure when a jurisdiction proposes or enacts stablecoin legislation

## Inputs To Gather

- **Stablecoin identifier**: token name, ticker, chain(s) deployed on, smart contract addresses
- **Issuer details**: legal entity, jurisdiction of incorporation, licensing status
- **Reserve disclosures**: latest attestation or audit report, reserve composition breakdown, custodian identities
- **Redemption terms**: minimum redemption amount, processing windows, fees, KYC/AML gating
- **Market data**: circulating supply, 24h volume, peg deviation history (30/90/365-day), secondary market liquidity depth
- **Regulatory filings**: any money transmitter licenses, e-money authorizations, or pending enforcement actions [VERIFY jurisdiction-specific registrations]
- **Smart contract details**: minting/burning mechanism, blacklist/freeze functions, upgrade proxy pattern, audit reports

## Workflow

1. **Classify the stablecoin model**
   - Fiat-collateralized (e.g., bank deposits, T-bills, money market funds)
   - Crypto-collateralized (e.g., over-collateralized vaults, liquidation mechanisms)
   - Algorithmic / hybrid (e.g., seigniorage, rebase, fractional-reserve)
   - Commodity-backed (e.g., gold, oil reserves)
   - Classification drives which risk factors dominate the analysis

2. **Analyze reserve composition and adequacy**
   - Map each reserve asset class to its credit quality, duration, and liquidity profile
   - Calculate weighted-average maturity and mark-to-market risk under stress scenarios (e.g., 100 bps rate shock)
   - Verify whether reserves equal or exceed circulating supply at par
   - Check attestation cadence (monthly vs. quarterly) and whether performed by a reputable accounting firm [VERIFY attestation firm independence and methodology]
   - For crypto-collateralized: assess collateralization ratios, liquidation thresholds, and oracle dependencies

3. **Evaluate peg stability mechanics**
   - Review historical peg deviations: frequency, magnitude, and recovery time
   - Identify primary arbitrage loop that restores peg (mint/redeem vs. market maker vs. algorithmic)
   - Stress-test: what happens if $500M redeems in 24 hours? Is reserve liquidity sufficient?
   - For algorithmic models: analyze reflexivity risk and death-spiral scenarios

4. **Assess redemption infrastructure**
   - Map the full redemption path: on-chain burn → issuer processing → fiat settlement
   - Identify gates, delays, minimum thresholds, and fee structures
   - Evaluate whether retail and institutional users have equal redemption access
   - Check for blacklist/freeze capabilities and under what conditions they are exercised

5. **Evaluate regulatory and legal risk**
   - Classify under applicable frameworks: US (state MTL, potential federal stablecoin legislation), EU (MiCA e-money token vs. asset-referenced token), UK (FCA regulated stablecoin) [VERIFY current status of pending legislation]
   - Assess issuer's licensing posture and any enforcement history
   - Review bankruptcy remoteness of reserve assets—are they held in trust, segregated, or commingled?
   - Identify sanctions compliance capabilities (OFAC screening, address blacklisting)

6. **Score and synthesize**
   - Assign risk ratings across dimensions: reserve quality, peg stability, redemption reliability, regulatory standing, smart contract risk
   - Produce a composite risk tier (e.g., Tier 1 / Tier 2 / Tier 3 or traffic-light rating)
   - Identify key monitoring triggers that would change the rating (e.g., missed attestation, peg deviation >50 bps for >4 hours, regulatory action)

## Output

The deliverable is a **Stablecoin Analysis Report** containing:

- **Executive summary**: stablecoin name, model type, composite risk rating, and one-paragraph recommendation
- **Reserve analysis table**: asset class | allocation % | credit quality | liquidity | weighted duration
- **Peg stability chart summary**: 30/90/365-day max deviation, average deviation, recovery statistics
- **Redemption mechanics matrix**: channel, minimum, fees, settlement time, KYC requirements
- **Regulatory status dashboard**: jurisdiction | license type | status | expiry/renewal date
- **Smart contract risk summary**: audit firm(s), findings severity, upgrade mechanism, admin key controls
- **Risk rating scorecard**: dimension-by-dimension scores with brief rationale
- **Monitoring triggers and escalation criteria**: specific thresholds that warrant re-review or position reduction

## Quality Checks

- Reserve figures reconcile to the most recent attestation or on-chain proof-of-reserves; flag any discrepancy
- Circulating supply cross-referenced between on-chain data and issuer disclosures
- Peg deviation data sourced from at least two independent market data providers
- All regulatory classifications verified against current (not proposed) law—mark pending legislation with [VERIFY]
- Redemption terms confirmed from issuer's current terms of service, not third-party summaries
- Smart contract addresses verified against issuer's official documentation
- No stale data: attestation reports older than 90 days flagged; market data no older than 24 hours
- Report explicitly states what is outside scope (e.g., tax treatment, accounting classification under GAAP/IFRS)
