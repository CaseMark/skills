---
name: reviewing-kyc-documentation
description: Evaluates customer identification and verification documentation against CIP/CDD/EDD requirements. Use when reviewing KYC files, validating customer identification, or assessing customer risk.
tags:
  - review
  - financial-compliance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Regulatory Compliance
    - Financial Regulation
    - Compliance
  document_types:
    - Review Report
  skill_modes:
    - Review
    - Analysis
---
# Reviewing KYC Documentation

Evaluates customer identification and verification documentation against Customer Identification Program (CIP), Customer Due Diligence (CDD), and Enhanced Due Diligence (EDD) requirements to determine whether a KYC file is complete, accurate, and risk-appropriate.

## When To Use

- Reviewing a new customer onboarding file before account opening approval
- Periodic re-review of existing customer KYC files (annual, trigger-based, or risk-cycle)
- Assessing whether a customer risk rating change requires EDD uplift
- Auditing a portfolio of KYC files for regulatory exam readiness
- Evaluating remediation files flagged by compliance monitoring

## Inputs To Gather

- **Customer identification documents**: government-issued ID (passport, driver's license, national ID), articles of incorporation, certificate of formation, or trust instrument for entities
- **Verification records**: documentary vs. non-documentary verification method used; third-party verification results (e.g., LexisNexis, World-Check, Dow Jones)
- **Beneficial ownership declaration**: ownership structure chart, UBO identification form, percentage thresholds applied [VERIFY: 25% threshold under CDD Rule; jurisdiction may differ]
- **Risk rating worksheet**: initial and current risk score, scoring methodology, risk factors applied
- **Source of funds / source of wealth documentation**: bank statements, tax returns, business financials, or self-certification
- **Screening results**: OFAC/SDN, PEP databases, adverse media, sanctions lists — with date of last screening
- **Account activity profile**: expected transaction types, volumes, jurisdictions, and any deviations flagged post-opening
- **Prior review notes**: previous findings, remediation status, outstanding deficiencies

## Workflow

1. **Confirm file completeness** — Check that all required CIP elements are present for the customer type:
   - Individuals: name, date of birth, address, government ID number [VERIFY: specific ID requirements vary by jurisdiction]
   - Legal entities: legal name, formation jurisdiction, principal place of business, EIN/TIN, formation documents
   - Trusts/other structures: trust agreement, trustee identification, beneficiary information where required

2. **Validate identification and verification** — Assess whether:
   - Documentary verification uses unexpired, legible, government-issued documents
   - Non-documentary methods (database checks, credit bureau, references) are adequately documented
   - Discrepancies between ID documents and application data are noted and resolved
   - For entities: verify legal existence through formation documents or registry searches

3. **Assess beneficial ownership compliance** — Confirm:
   - All individuals owning 25% or more are identified with full CIP-level information [VERIFY: threshold per CDD Final Rule; some jurisdictions use 10% or 20%]
   - A single individual is identified as having significant management control
   - Ownership structure is diagrammed for multi-layered entities
   - Nominee/bearer share arrangements are flagged and investigated

4. **Evaluate risk rating** — Review the assigned risk level against:
   - Customer type (individual, corporate, PEP, MSB, NBFI, charity/NPO)
   - Geographic risk (FATF high-risk jurisdictions, sanctioned countries, tax havens)
   - Product/service risk (correspondent banking, private banking, trade finance, virtual assets)
   - Transaction risk (expected volume, cash intensity, cross-border activity)
   - Confirm the risk rating methodology matches institutional policy and that the score is correctly calculated

5. **Review EDD where applicable** — For high-risk customers, verify:
   - Source of wealth and source of funds are independently documented (not just self-declared)
   - Senior management approval for relationship establishment or continuation is on file
   - Enhanced monitoring parameters are defined (transaction thresholds, review frequency)
   - Negative news and PEP screening performed at closer intervals

6. **Check screening and ongoing monitoring** — Confirm:
   - OFAC/sanctions screening was run at onboarding and is current
   - PEP screening covers the customer and all beneficial owners
   - Adverse media screening is documented with disposition of hits
   - Screening is re-run at each periodic review and upon trigger events

7. **Classify findings** — Assign severity to each deficiency:
   - **Critical**: missing CIP element, unresolved sanctions hit, no beneficial ownership on file
   - **Major**: expired identification document, risk rating inconsistent with profile, EDD not performed for high-risk customer
   - **Minor**: formatting gaps, outdated contact information, missing secondary documentation

## Output

Produce a structured KYC review report containing:

- **File summary**: customer name, account number, customer type, risk rating, review date, reviewer
- **Completeness checklist**: pass/fail for each CIP, CDD, and EDD element
- **Findings table**: finding description, severity (Critical/Major/Minor), regulatory reference, evidence citation
- **Remediation recommendations**: specific corrective action for each finding, responsible party, deadline
- **Overall assessment**: file status recommendation — Satisfactory, Conditional (with remediation required), or Unsatisfactory (escalation required)
- **Escalation flags**: any findings requiring SAR consideration, account restriction, or senior management review

## Quality Checks

- Every finding cites a specific regulatory requirement or internal policy section (e.g., 31 CFR 1020.220, BSA/AML Manual Section X) [VERIFY: cite institution-specific policy references]
- Beneficial ownership analysis accounts for all layers of the ownership chain, not just the first tier
- Risk rating review confirms arithmetic accuracy and that all applicable risk factors were scored
- Screening results include date stamps — reject any screening older than the institution's policy window [VERIFY: typical policy is 30-90 days; confirm institutional standard]
- No finding is marked "Minor" if it would independently constitute a regulatory violation
- Flag any assumption or unverifiable data point with [VERIFY] rather than presenting it as confirmed
- If the file involves a jurisdiction, product, or customer type outside the reviewer's expertise, escalate to specialized compliance staff
