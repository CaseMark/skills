---
name: structuring-risk-retention-compliance
description: Designs risk retention structures meeting US and EU requirements with vertical, horizontal, and L-shaped retention options. Use when structuring risk retention, analyzing sponsor retention alternatives, or ensuring regulatory compliance.
tags:
  - structured-finance
  - compliance
  - regulatory
  - risk
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Risk Retention Compliance

Designs risk retention structures meeting US and EU requirements with vertical, horizontal, and L-shaped retention options.

## When To Use

- Structuring a new securitization (CLO, RMBS, CMBS, ABS, CRE-CLO) and selecting the retention form
- Evaluating whether a sponsor, originator, or majority-owned affiliate qualifies as the retaining party
- Comparing US Regulation RR (17 CFR Part 246) retention options against EU Securitisation Regulation (EU 2017/2402, Articles 6-8) requirements
- Assessing whether an exemption applies (e.g., Qualified Residential Mortgages, qualifying CRE loans, ABCP conduit exemptions)
- Reviewing an existing retention structure for ongoing compliance after portfolio changes or refinancing

## Inputs To Gather

- **Transaction type**: CLO, RMBS, CMBS, consumer ABS, ABCP, or other; open-market vs. balance-sheet
- **Jurisdictional scope**: US-only, EU-only, or dual-compliance (cross-border placement)
- **Sponsor / originator identity**: Entity holding the retention interest; ownership chain to confirm majority-owned affiliate status if applicable
- **Capital structure**: Tranche sizes, credit enhancement levels, par amount of the securitized pool
- **Asset pool characteristics**: Asset class, weighted-average credit quality, delinquency/default data, QRM/QCRE eligibility indicators
- **Retention preference**: Vertical (pro-rata slice), horizontal (first-loss piece), L-shaped (combination), or originator retention under EU rules
- **Hedging and transfer restrictions**: Any planned hedging of credit risk on retained positions; transfer timing constraints
- **Fair value data**: Third-party or model-based fair value of the horizontal residual interest at closing [VERIFY]

## Workflow

1. **Classify the transaction and identify the applicable rule set**
   - Determine whether US Reg RR, EU Securitisation Regulation, or both apply based on investor base and placement jurisdiction
   - Identify the "securitizer" (US) or "originator/sponsor/original lender" (EU) responsible for retention
   - Confirm the retaining entity satisfies the definition — trace ownership for majority-owned affiliates [VERIFY]

2. **Calculate the minimum retention amount**
   - **US Reg RR**: 5% of the aggregate fair value of all ABS interests issued, calculated at closing
   - **EU Article 6**: 5% material net economic interest, measured on an ongoing basis (not just at closing)
   - For dual-compliance deals, compute both and apply the more restrictive measurement methodology

3. **Select and structure the retention form**
   - **Vertical strip (US Option A / EU Article 6(3)(a))**: Retain not less than 5% of each class of ABS interests issued. Simplest to implement; retainer bears losses proportionally across the capital structure
   - **Horizontal residual interest (US Option B / EU Article 6(3)(d))**: Retain a first-loss position equal to at least 5% of fair value. Concentrates risk; requires fair value determination of the residual [VERIFY fair value methodology]
   - **L-shaped (US Option C)**: Combination of vertical and horizontal where the sum of the two components equals or exceeds 5%. Provides flexibility to calibrate first-loss exposure versus pro-rata risk
   - **EU originator retention (Article 6(3)(c))**: Randomly selected exposures retained on originator balance sheet — not available under US rules; relevant for ABCP and trade-receivable deals
   - **Seller's interest (US revolving pool option / EU Article 6(3)(e))**: Originator retains the seller's interest in a revolving master trust. Applicable to credit card and auto-loan securitizations

4. **Evaluate exemptions and safe harbors**
   - QRM exemption (US): If 100% of pool assets are Qualified Residential Mortgages, full exemption from retention [VERIFY QRM criteria against current CFPB/OCC definition]
   - Qualifying CRE loan exemption (US): Reduced or eliminated retention for loans meeting LTV, DSCR, and amortization thresholds
   - ABCP conduit exemption (US): Available if the conduit sponsor provides full liquidity support
   - EU exemptions: STS (Simple, Transparent, and Standardised) designation does not eliminate the 5% requirement but may alter disclosure obligations [VERIFY STS eligibility under current EBA technical standards]

5. **Document hedging and transfer restrictions**
   - US: The retaining party may not hedge or transfer the credit risk of the retained interest for the life of the transaction (with narrow exceptions for interest rate and currency hedging)
   - EU: Similar prohibition — no credit risk mitigation, short selling, or hedging of the retained interest. Ongoing compliance monitoring required
   - Flag any proposed hedge overlay for legal review to confirm it does not constitute impermissible credit risk transfer

6. **Address ongoing compliance monitoring**
   - EU requires continuous maintenance of the net economic interest — not merely at closing. Build a periodic recalculation mechanism for amortizing or revolving pools
   - US is generally a closing-date test, but any transfer or restructuring of the retained interest triggers re-evaluation
   - Confirm disclosure obligations to investors: US Rule 17g-5 / Reg AB II requirements; EU Article 7 transparency templates

## Output

Produce a **Risk Retention Compliance Memo** containing:

- **Retention structure summary**: Form selected (vertical / horizontal / L-shaped / other), retaining entity, and calculated retention amount with supporting math
- **Regulatory basis**: Specific statutory and regulatory citations (Reg RR section, EU Securitisation Regulation article)
- **Exemption analysis**: Whether any exemption applies, with criteria-by-criteria confirmation or shortfall identification
- **Hedging and transfer restriction schedule**: Permitted and prohibited actions for the retaining party over the life of the deal
- **Ongoing compliance obligations**: Monitoring cadence, recalculation triggers, and disclosure requirements
- **Risk factors / open items**: Any unresolved questions marked [VERIFY], assumptions requiring sponsor confirmation, or items requiring external counsel sign-off

## Quality Checks

- Retention percentage calculation cross-checked against both the par-based and fair-value-based methodologies where applicable
- Retaining entity eligibility verified through ownership chain analysis — not assumed from deal documents alone
- Dual-compliance deals confirm the structure satisfies both US and EU requirements simultaneously, not just the home jurisdiction
- All exemption claims supported by asset-level data or portfolio-level certifications, not summary representations
- Hedging restriction analysis reviewed against the specific retained interest (not the sponsor's broader portfolio)
- Every jurisdiction-dependent or regulation-dependent assertion tagged with [VERIFY] where the applicable rule may have been amended after the model's knowledge cutoff
