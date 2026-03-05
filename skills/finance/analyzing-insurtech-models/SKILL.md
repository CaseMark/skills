---
name: analyzing-insurtech-models
description: Evaluates insurtech business models with distribution innovation, underwriting technology, and claims automation. Use when analyzing insurtech, evaluating digital insurance, or assessing insurance technology.
tags:
  - analysis
  - financial-technology
  - insurance
metadata:
  author: casemark
  practice_areas:
    - Fintech
    - Payments
    - Digital Banking
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Insurtech Models

## When To Use

- Evaluating an insurtech startup's business model for investment, partnership, or competitive analysis
- Assessing the viability of a digital insurance distribution strategy (D2C, embedded, marketplace)
- Analyzing underwriting technology capabilities — ML-based risk scoring, parametric triggers, or real-time data ingestion
- Reviewing claims automation platforms for efficiency, fraud detection, and customer experience impact
- Benchmarking an insurtech's unit economics against traditional carrier or MGA models

## Inputs To Gather

- **Company overview**: Entity name, founding date, funding stage, total capital raised, key investors
- **Business model classification**: Full-stack carrier, MGA/MGU, broker/agent platform, embedded insurance provider, claims-only SaaS, or reinsurance intermediary
- **Product lines**: Coverage types offered (P&C, life, health, specialty), target customer segments (SMB, consumer, enterprise)
- **Technology stack**: Core platform architecture, underwriting engine details, data sources used for risk assessment, claims processing tools
- **Distribution channels**: Direct-to-consumer, B2B2C embedded partnerships, agent/broker network, API-first distribution
- **Financial data**: GWP/NWP, loss ratio, combined ratio, expense ratio, retention rates, LTV/CAC where available
- **Regulatory posture**: Licenses held, states/jurisdictions of operation, carrier partners (if MGA), reinsurance arrangements [VERIFY jurisdiction-specific licensing requirements]

## Workflow

1. **Classify the model type**
   - Determine whether the company operates as a full-stack carrier, MGA/MGU, technology vendor, or hybrid
   - Map the value chain position: product design, underwriting, distribution, servicing, claims, or multi-segment
   - Identify whether risk is retained on-balance-sheet, ceded to carrier partners, or passed through reinsurance

2. **Evaluate distribution innovation**
   - Assess channel strategy: embedded insurance via API partnerships, digital-direct, affinity groups, or platform marketplace
   - Analyze customer acquisition cost relative to traditional brokers (~15-25% commission) and digital benchmarks
   - Review integration depth with distribution partners (API-level, white-label, co-branded)
   - Gauge switching costs and channel lock-in potential

3. **Assess underwriting technology**
   - Identify data sources beyond traditional actuarial inputs (telematics, IoT, satellite imagery, behavioral data, social signals)
   - Evaluate real-time vs. batch underwriting decisioning and bind-time latency
   - Examine adverse selection controls and portfolio composition management
   - Determine whether proprietary algorithms create defensible underwriting advantage or merely automate standard tables
   - Flag parametric or index-based trigger mechanisms if applicable [VERIFY regulatory treatment of parametric products varies by state/country]

4. **Analyze claims automation**
   - Map the claims lifecycle: FNOL intake, triage, investigation, adjustment, payment
   - Quantify automation rate at each stage — straight-through processing percentage for low-complexity claims
   - Evaluate fraud detection capabilities (rules-based, ML-based, network analysis)
   - Assess customer NPS/satisfaction metrics tied to claims experience
   - Review average cycle time vs. industry benchmarks (auto: ~12 days, homeowners: ~15-30 days) [VERIFY benchmarks shift by line and geography]

5. **Stress-test unit economics**
   - Calculate loss ratio trends over 12-36 months; distinguish attritional from catastrophe losses
   - Compute combined ratio and compare to breakeven thresholds (~100% for carriers, ~80-85% for MGAs after ceding commissions)
   - Model LTV/CAC for policyholders, factoring retention rate and cross-sell potential
   - Evaluate expense ratio drivers: technology spend amortization, customer acquisition, regulatory compliance overhead
   - Assess capital efficiency: premium-to-surplus ratio, reinsurance leverage, and risk-based capital adequacy [VERIFY RBC requirements per domicile state]

6. **Identify regulatory and structural risks**
   - Review carrier dependency risk for MGAs (single vs. multi-carrier panel, contract renewal terms)
   - Assess regulatory concentration — number of state licenses, surplus lines vs. admitted market positioning
   - Evaluate data privacy exposure given volume of personal/health/telematics data processed [VERIFY CCPA, state privacy law, and HIPAA applicability depending on line of business]
   - Flag any pending regulatory actions, market conduct exams, or consumer complaints

## Output

Produce an **Insurtech Model Analysis Report** containing:

- **Executive summary**: One-paragraph assessment of model viability, competitive positioning, and key risk/opportunity
- **Model classification table**: Business type, value chain position, risk retention structure, and regulatory status
- **Distribution scorecard**: Channel mix, CAC benchmarks, integration depth, and scalability assessment
- **Underwriting technology assessment**: Data advantage rating, automation level, adverse selection controls
- **Claims capability matrix**: Automation rate by stage, cycle time benchmarks, fraud detection maturity
- **Financial profile**: Loss ratio, combined ratio, expense ratio, LTV/CAC, capital efficiency metrics
- **Risk register**: Top 5 risks ranked by likelihood and impact (regulatory, concentration, technology, capital, competitive)
- **Comparative positioning**: Where the company sits relative to 2-3 named peers or traditional incumbents

## Quality Checks

- All financial ratios are sourced or calculated from stated inputs — no fabricated metrics
- Loss ratio and combined ratio calculations are internally consistent (loss + expense = combined)
- Model classification aligns with actual risk retention structure, not marketing language
- Regulatory status flags carry [VERIFY] where jurisdiction-specific confirmation is needed
- Benchmark comparisons cite the line of business and time period used
- Report distinguishes between confirmed data and analyst inference throughout
- Carrier dependency and reinsurance arrangement risks are addressed for MGA/MGU models
