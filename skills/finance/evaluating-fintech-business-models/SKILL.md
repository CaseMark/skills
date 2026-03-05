---
name: evaluating-fintech-business-models
description: Structures fintech company analysis with unit economics, customer acquisition, and regulatory moat assessment. Use when evaluating fintech companies, analyzing unit economics, or assessing fintech business models.
tags:
  - analysis
  - financial-technology
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Fintech
    - Payments
    - Digital Banking
  document_types:
    - Evaluation Report
  skill_modes:
    - Analysis
    - Assessment
---
# Evaluating Fintech Business Models

Structures fintech company analysis with unit economics, customer acquisition, and regulatory moat assessment.

## When To Use

- Evaluating a fintech company for investment, acquisition, or partnership
- Comparing business model viability across fintech verticals (payments, lending, neobanking, insurance, wealth management)
- Assessing whether a fintech's unit economics support long-term profitability
- Analyzing regulatory positioning and charter/license strategy as competitive moat
- Diligencing fintech targets in M&A or venture contexts

## Inputs To Gather

- **Company fundamentals**: Revenue model type (interchange, SaaS, spread-based, transaction fee, lead-gen), target customer segment (consumer, SMB, enterprise, embedded B2B2C), geography
- **Financial data**: Revenue, gross margin, net revenue retention, take rate or spread, operating expenses by category, burn rate and runway
- **Unit economics**: Customer acquisition cost (CAC), lifetime value (LTV), payback period, contribution margin per customer or per transaction
- **Growth metrics**: Monthly/annual active users, transaction volume, deposit growth, cohort retention curves, net dollar retention
- **Regulatory posture**: Licenses held vs. sponsor bank/partner dependencies, pending applications, compliance infrastructure maturity [VERIFY jurisdiction-specific license requirements]
- **Competitive context**: Direct competitors, incumbent bank positioning, open banking / API ecosystem dynamics

## Workflow

1. **Classify the business model**
   - Identify primary revenue mechanism: interchange/fees, net interest margin, subscription/SaaS, marketplace/platform, or hybrid
   - Map the value chain position: originator, distributor, infrastructure/rails, or aggregator
   - Determine whether the company owns the customer relationship directly or operates as embedded fintech (B2B2C)

2. **Analyze unit economics**
   - Calculate fully-loaded CAC including paid acquisition, referral costs, onboarding friction costs, and fraud losses at sign-up
   - Compute LTV using revenue per customer, gross margin, and observed or modeled churn rates; stress-test with cohort degradation
   - Derive LTV:CAC ratio and CAC payback period; flag if payback exceeds 18 months for consumer or 24 months for SMB
   - For lending models: break down net interest margin, provision for credit losses, and charge-off rates by vintage; assess whether credit performance holds across economic cycles
   - For payments models: compute net take rate after interchange, network fees, and processor costs; evaluate volume sensitivity and pricing power

3. **Assess customer acquisition and retention**
   - Evaluate channel mix: organic vs. paid, viral/referral mechanics, embedded distribution partnerships
   - Review cohort retention curves at 3, 6, 12, and 24 months; identify whether engagement deepens or flatlines after onboarding
   - For multi-product companies: measure cross-sell attach rates and revenue per user expansion over time
   - Assess switching costs and deposit/balance stickiness as natural retention levers

4. **Evaluate regulatory moat and risk**
   - Inventory licenses and charters held directly (state money transmitter licenses, banking charter, broker-dealer, insurance) vs. rented through sponsor banks or partners [VERIFY state-by-state and federal requirements]
   - Assess sponsor bank dependency risk: concentration, contract renewal terms, regulatory scrutiny on the sponsor
   - Evaluate compliance infrastructure: BSA/AML program maturity, KYC/KYB processes, complaint rates, examination history [VERIFY applicable regulations by charter type]
   - Score regulatory moat: companies with direct charters or multi-license portfolios have higher barriers to replication
   - Flag pending regulatory changes that could expand or constrain the business (e.g., open banking mandates, interchange caps, earned wage access rules) [VERIFY current regulatory proposals]

5. **Benchmark and synthesize**
   - Compare key metrics against public fintech comps and relevant benchmarks by vertical
   - Identify the 2-3 metrics most critical to this specific model's viability (e.g., net take rate for payments, NIM + charge-offs for lending, NRR for SaaS)
   - Assess scalability: does the cost structure improve with volume, or do compliance/servicing costs scale linearly?
   - Summarize structural advantages and vulnerabilities

## Output

Produce a structured evaluation report containing:

- **Executive summary**: One-paragraph model classification, key thesis, and overall assessment (attractive / mixed / unattractive)
- **Business model overview**: Revenue model, value chain position, customer segment, and competitive positioning
- **Unit economics scorecard**: Table with CAC, LTV, LTV:CAC, payback period, gross margin, contribution margin; flag metrics outside healthy ranges
- **Growth and retention analysis**: Cohort curves, channel mix, cross-sell dynamics, and net revenue retention
- **Regulatory assessment**: License inventory, sponsor bank risk, compliance maturity rating, and regulatory change exposure
- **Benchmark comparison**: Side-by-side with 3-5 comparable companies on key metrics
- **Risk factors**: Itemized list of model-specific risks (credit, regulatory, concentration, competitive)
- **Key questions for management**: 5-10 targeted diligence questions surfaced by the analysis

## Quality Checks

- Verify that LTV calculations use observed churn data or clearly state modeled assumptions; never present projected LTV as proven
- Confirm take rate or spread calculations net out all pass-through costs (interchange, network fees, credit losses)
- Ensure regulatory license inventory is current and jurisdiction-specific; mark any unverified items with [VERIFY]
- Check that cohort data covers sufficient time horizons (minimum 12 months for consumer, 24 months for lending)
- Validate that benchmark comparisons use companies of comparable stage, geography, and vertical
- Flag any metrics derived from management projections vs. audited/reported data
- Confirm the analysis addresses the specific fintech vertical's key risk: credit risk for lenders, fraud risk for payments, regulatory risk for banking, and basis risk for embedded finance
