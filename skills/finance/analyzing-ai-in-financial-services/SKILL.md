---
name: analyzing-ai-in-financial-services
description: Evaluates AI/ML applications in financial services with model governance, bias assessment, and regulatory considerations. Use when analyzing AI in finance, evaluating ML models, or assessing AI governance.
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
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing AI In Financial Services

## When To Use

- Evaluating an AI/ML model deployed or proposed for credit decisioning, fraud detection, AML/KYC, trading, or customer-facing automation
- Assessing model risk management (MRM) posture against SR 11-7, OCC 2011-12, or equivalent guidance [VERIFY jurisdiction-specific MRM guidance]
- Reviewing algorithmic bias and fair-lending implications for underwriting or pricing models
- Analyzing vendor-supplied AI tools (e.g., BaaS scoring engines, conversational AI for digital banking)
- Preparing for regulatory examination or audit of AI/ML systems in a financial institution

## Inputs To Gather

- **Model documentation**: model cards, technical specifications, training data descriptions, feature lists
- **Performance metrics**: accuracy, precision/recall, AUC-ROC, stability metrics (PSI), back-testing results
- **Governance artifacts**: model inventory entry, validation reports, change-management logs, approval records
- **Bias/fairness data**: disparate impact ratios across protected classes, HMDA or ECOA-relevant statistics [VERIFY applicable fair-lending statutes by jurisdiction]
- **Regulatory context**: institution charter type (bank, credit union, non-bank lender), applicable supervisory framework, any open MRAs or consent orders
- **Use-case scope**: specific business function the AI serves (e.g., real-time fraud scoring, deposit pricing, chatbot servicing)

## Workflow

1. **Define scope and materiality**
   - Classify the model by risk tier (critical, high, medium, low) based on financial exposure, customer impact, and regulatory sensitivity
   - Confirm whether the model is first-party built, vendor-supplied, or open-source derived — governance expectations differ for each

2. **Assess model governance framework**
   - Map the institution's MRM program against SR 11-7 three-lines-of-defense structure [VERIFY if institution falls under OCC, Fed, or state regulator]
   - Check for documented model owner, independent validation function, and escalation procedures
   - Verify model inventory completeness — flag any shadow models or undocumented deployments

3. **Evaluate technical soundness**
   - Review feature selection for proxies of protected characteristics (e.g., zip code as race proxy in credit models)
   - Examine training data vintage, representativeness, and label quality
   - Assess explainability: can adverse-action reasons be generated per ECOA/Reg B requirements? [VERIFY if adverse-action notice obligations apply]
   - Check for concept drift monitoring and automated retraining triggers

4. **Conduct bias and fairness analysis**
   - Calculate disparate impact ratios for lending/pricing models across race, sex, age, and other protected classes
   - Apply appropriate fairness metrics (demographic parity, equalized odds, predictive parity) based on use case
   - Identify whether pre-processing, in-processing, or post-processing debiasing techniques are employed
   - Flag any model where disparate impact exceeds the four-fifths threshold without documented business justification

5. **Map regulatory and compliance exposure**
   - Cross-reference against CFPB guidance on automated decisioning and adverse-action notices
   - For payment/digital-banking AI, evaluate PCI-DSS data handling, BSA/AML transaction-monitoring adequacy [VERIFY PCI scope for specific deployment]
   - Assess third-party risk management (TPRM) obligations if model is vendor-supplied (OCC 2013-29 / updated interagency guidance)
   - Note any state-specific AI laws (e.g., Colorado AI Act, NYC Local Law 144 for automated employment decisions) [VERIFY state/local AI legislation applicability]

6. **Synthesize findings and risk-rate**
   - Assign overall risk rating with supporting rationale
   - Prioritize findings by severity: critical (immediate remediation), high (next exam cycle), moderate (roadmap), low (enhancement)
   - Identify compensating controls that mitigate identified gaps

## Output

Produce an **AI/ML Model Analysis Report** containing:

- **Executive summary**: model name, use case, risk tier, overall assessment (acceptable / acceptable with conditions / unacceptable)
- **Governance assessment**: MRM program maturity, validation independence, inventory accuracy
- **Technical evaluation**: model performance, explainability, drift monitoring, data quality
- **Bias and fairness findings**: disparate impact results, fairness metrics, debiasing controls
- **Regulatory exposure map**: applicable regulations, compliance gaps, pending enforcement trends
- **Remediation roadmap**: prioritized findings with owners, timelines, and success criteria
- **Appendices**: data tables, metric calculations, regulatory cross-reference matrix

## Quality Checks

- Every finding cites a specific regulatory provision, guidance document, or industry standard (SR 11-7, ECOA, CFPB circulars)
- Disparate impact calculations include methodology notes and confidence intervals
- Vendor-supplied models are assessed under both MRM and TPRM frameworks — do not evaluate under only one
- All jurisdiction-dependent conclusions are tagged with [VERIFY] for reviewer confirmation
- Adverse-action explainability is tested with sample outputs, not just documented as "supported"
- Report distinguishes between model risk (technical) and compliance risk (regulatory) — do not conflate the two
