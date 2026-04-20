---
name: conducting-reg-ab-compliance
language: en
description: Structures Regulation AB II compliance with asset-level data requirements, servicer reporting, and shelf registration eligibility. Use when ensuring Reg AB compliance, preparing ABS reporting, or structuring shelf eligibility.
tags:
  - process
  - structured-finance
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Reg Ab Compliance

Structures Regulation AB II compliance with asset-level data requirements, servicer reporting, and shelf registration eligibility.

## When To Use

- Preparing or reviewing asset-level data filings on EDGAR (Form ABS-EE)
- Evaluating shelf registration eligibility under Rule 415 for ABS offerings
- Structuring servicer reporting obligations and compliance certifications
- Conducting pre-offering diligence on Reg AB II data field completeness
- Reviewing ongoing periodic reporting (Form 10-D, Form 10-K) for ABS issuers
- Assessing whether a new asset class or pool structure triggers additional Reg AB requirements

## Inputs To Gather

- **Asset class designation** — RMBS, CMBS, CLO, auto ABS, credit card ABS, equipment ABS, etc., as each triggers a distinct Schedule AL field set [VERIFY: confirm applicable Schedule AL for the specific asset class]
- **Shelf registration statement** (Form SF-3) and any pending amendments
- **Prospectus and prospectus supplement** with waterfall descriptions and pool-level data
- **Servicer compliance certifications** (annual and event-driven)
- **Historical Form ABS-EE filings** for the issuing entity, if any
- **Transaction agreements** — PSA, servicing agreement, indenture, administration agreement
- **Third-party due diligence reports** (Rule 15Ga-2 findings letters)
- **CEO certification** of disclosure under Exchange Act Rule 13a-14(d)/15d-14(d)

## Workflow

### 1. Determine Shelf Eligibility (Form SF-3)

- Confirm the depositor has filed all required Exchange Act reports for at least 12 months [VERIFY: check for any SEC no-action relief modifying this timeline]
- Verify that prior ABS offerings by the same depositor included compliant transaction-level and asset-level data
- Confirm the depositor has not been an unregistered shell company within the preceding 12 calendar months
- Check that the depositor satisfies the timely filing requirement — no delinquent 10-D or 10-K filings
- Flag any prior SEC comment letters on the depositor's shelf or periodic filings that remain unresolved

### 2. Map Asset-Level Data Fields (Schedule AL)

- Identify the correct Schedule AL template for the asset class (e.g., Schedule AL-1 for RMBS, Schedule AL-2 for CMBS)
- Map each required field to the available data in the servicer's system or loan tape
- Flag fields with missing, unavailable, or non-conforming data — document whether omission is permitted under the "not applicable" or "no data" response codes
- For CLO/CDO structures, determine whether the SEC treats the asset class as requiring asset-level reporting or whether relief applies [VERIFY: current SEC guidance on CLO asset-level data requirements]
- Validate XML tagging per EDGAR technical specifications for Form ABS-EE submission

### 3. Review Servicer Reporting Obligations

- Confirm the servicing agreement requires delivery of a servicer compliance statement (Item 1122 of Reg AB)
- Verify the platform servicer, master servicer, and any sub-servicers each provide a separate Item 1122 assessment
- Check that an independent registered public accounting firm has provided an attestation report under Item 1122(b)
- Confirm servicer event-of-default triggers align with Reg AB reporting deadlines
- Review the servicing criteria applicable to each servicer role (cash collection, investor remittance, pool performance reporting, investor communication)

### 4. Validate Periodic Reporting

- **Form 10-D (distribution report):** Confirm filing within 15 days after each distribution date; verify pool performance data, waterfall allocations, trigger test results, and any servicer advances are accurately disclosed
- **Form 10-K (annual report):** Confirm inclusion of servicer compliance statements, attestation reports, and updated asset-level data; verify CEO certification
- **Form 8-K / Form ABS-15G:** Confirm timely filing of material event notices (e.g., early amortization triggers, servicer replacements, credit enhancement draws)
- Review third-party due diligence findings letter filings under Rule 15Ga-2 for any unresolved scope limitations

### 5. Assess Third-Party Due Diligence Compliance

- Confirm that any third-party diligence provider has furnished a findings letter to the issuer and filed Form ABS-15G on EDGAR
- Verify the prospectus discloses the scope, criteria, and findings of the third-party review
- Check whether the diligence scope covers a statistically valid sample or the full pool, and that the methodology is disclosed

## Output

- **Reg AB II Compliance Checklist** — field-by-field assessment of Schedule AL completeness with gap flags
- **Shelf Eligibility Memo** — confirming or identifying deficiencies in Form SF-3 eligibility criteria
- **Servicer Reporting Matrix** — mapping each servicer's obligations under Items 1121/1122, with attestation status
- **Periodic Filing Tracker** — status of 10-D, 10-K, 8-K, and ABS-EE filings with upcoming deadlines
- **Remediation Log** — list of data gaps, non-conformances, and recommended corrective actions with responsible parties

## Quality Checks

- Every Schedule AL field must be accounted for — no silent omissions; use "N/A — field not applicable to [asset class]" or "DATA GAP — [field name] unavailable from servicer" for each missing item
- Cross-reference waterfall descriptions in the prospectus against the distribution report (10-D) to confirm consistency
- Verify all filing deadlines against the actual transaction calendar, not generic SEC deadlines [VERIFY: confirm any filing extensions or COVID-era relief still in effect]
- Confirm that CEO certifications reference the correct Exchange Act rule (13a-14(d) or 15d-14(d), not the generic Sarbanes-Oxley certifications)
- Flag any reliance on SEC no-action letters, staff guidance, or exemptive orders and confirm they remain current
- Mark all jurisdiction- or regulation-dependent points with [VERIFY] for attorney review before filing
