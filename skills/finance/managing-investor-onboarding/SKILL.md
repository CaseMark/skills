---
name: managing-investor-onboarding
description: Structures investor onboarding with subscription documentation, AML/KYC, and suitability verification. Use when onboarding investors, processing subscriptions, or managing investor documentation.
tags:
  - management
  - fund-operations
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
# Managing Investor Onboarding

Structures investor onboarding with subscription documentation, AML/KYC, and suitability verification.

## When To Use

- Onboarding a new limited partner or investor into a private fund (PE, VC, hedge fund, real estate fund)
- Processing subscription documents for an initial or subsequent closing
- Coordinating AML/KYC verification and accreditation checks before capital acceptance
- Managing re-documentation for existing investors after fund restructuring or regulatory changes
- Tracking investor documentation status across multiple closings

## Inputs To Gather

- **Fund documents**: PPM/offering memorandum, LPA/operating agreement, subscription agreement template, side letter terms (if any)
- **Investor information**: Full legal name, entity type (individual, trust, corporation, pension, sovereign wealth, ERISA plan), jurisdiction of formation, tax ID/EIN
- **KYC/AML materials**: Government-issued ID (individuals), certificate of incorporation/formation, beneficial ownership declaration, OFAC/sanctions screening results, source-of-funds documentation
- **Accreditation/suitability**: Accredited investor questionnaire or qualified purchaser certification, investor suitability questionnaire, investment experience and risk tolerance documentation
- **Tax forms**: W-9 (U.S. persons), W-8BEN or W-8BEN-E (non-U.S. persons), FATCA/CRS self-certification [VERIFY: form requirements vary by fund domicile and investor jurisdiction]
- **Banking details**: Wire instructions for capital call funding, distribution payment instructions

## Workflow

1. **Pre-screening**
   - Confirm investor meets fund eligibility criteria (accredited investor, qualified purchaser, qualified client, or other applicable standard) [VERIFY: threshold definitions per SEC rules and fund-specific requirements]
   - Run preliminary OFAC/SDN list screening and adverse media check on investor and beneficial owners
   - Identify whether the investor is subject to ERISA, Bank Holding Company Act, or other regulatory overlays that impose additional fund-level obligations

2. **Subscription package assembly**
   - Prepare subscription agreement pre-populated with fund-specific terms (management fee, carried interest, commitment amount)
   - Attach investor questionnaire covering: accreditation status, qualified purchaser representations, ERISA status, tax status, beneficial ownership
   - Include applicable tax forms and banking/wire instruction templates
   - If side letter has been negotiated, cross-reference side letter terms against subscription agreement for consistency

3. **AML/KYC verification**
   - Collect and verify identity documents for all beneficial owners holding 25%+ (or applicable threshold) [VERIFY: beneficial ownership threshold varies — FinCEN CDD Rule uses 25%, some jurisdictions use 10%]
   - Validate entity formation documents (certificate of incorporation, trust agreement, partnership agreement)
   - Complete enhanced due diligence (EDD) for PEPs, high-risk jurisdictions, or complex ownership structures
   - Document all screening results with timestamps; flag any hits for compliance officer review

4. **Document review and execution**
   - Review completed subscription documents for: signature completeness, consistency between commitment amount and fund minimums, correct entity name across all forms
   - Verify tax form validity (correct form type for entity/jurisdiction, current revision date, proper certifications signed)
   - Confirm capital call funding source matches declared source-of-funds
   - Obtain countersignature from general partner or fund manager

5. **Investor record setup**
   - Create investor record in fund administration system with: legal name, commitment amount, closing date, fee terms, side letter provisions
   - Assign investor to correct share class or series
   - Set up capital account with opening balance and commitment tracking
   - Configure distribution waterfall allocation per LPA terms and any side letter modifications
   - Store all onboarding documents in investor file with retention tagging

6. **Closing coordination**
   - Confirm all investors in the closing have complete documentation packages
   - Prepare closing memorandum listing: investors accepted, aggregate commitments, any conditions or exceptions
   - Issue capital call notice for initial funding (if applicable at closing)
   - Distribute welcome packet with fund contact information, reporting schedule, and portal access credentials

## Output

- **Onboarding status tracker**: Investor-by-investor matrix showing document receipt status, KYC clearance, accreditation verification, tax form status, and overall readiness for closing
- **Exception log**: List of incomplete items, pending verifications, or flagged issues requiring follow-up (e.g., expired ID, missing beneficial owner disclosure, OFAC near-match)
- **Closing memorandum**: Summary of accepted investors, commitment amounts, closing date, and any conditions or carve-outs
- **Investor file checklist**: Confirmation that all required documents are collected, verified, and stored per fund document retention policy

## Quality Checks

- Every beneficial owner identified and screened — no gaps in the ownership chain
- Subscription agreement commitment amount matches the investor's stated commitment and meets fund minimum [VERIFY: check for any side letter fee or minimum commitment modifications]
- Tax forms match investor entity type and jurisdiction (W-9 for U.S. taxpayers, correct W-8 series for non-U.S.)
- OFAC/sanctions screening is current (not stale) — run within 30 days of closing or per fund compliance policy
- ERISA investor percentage tracked against fund's ERISA threshold (typically 25% of plan assets) [VERIFY: confirm fund-specific ERISA tolerance and whether VCOC/REOC exemption applies]
- All documents executed with authorized signatories — verify signatory authority against entity formation documents or board resolutions
- Side letter terms properly reflected in fund admin system setup (fee discounts, co-invest rights, reporting obligations)
- No investor accepted without completed KYC clearance — zero exceptions without documented compliance officer approval
