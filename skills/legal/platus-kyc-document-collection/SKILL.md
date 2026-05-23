---
name: platus-kyc-document-collection
description: Automate KYC document collection, verification, and compliance workflows for legal transactions and client onboarding
tags:
  - practice: regulatory, corporate
  - document: checklist, policy
  - mode: drafting, analysis
---

# Platus KYC Document Collection

Automated KYC document collection and verification for client onboarding and transactional compliance.

## Prerequisites

- KYC checklist template with jurisdiction-specific requirements
- Secure document intake portal (API or web link)
- Identity verification data source (government databases, third-party KYC providers)
- Compliance policy reference for target jurisdiction

## Workflow

1. Define KYC requirements based on transaction type and jurisdiction
2. Generate client intake portal link with required document checklist
3. Trigger automated collection: clients upload ID, proof of address, corporate docs
4. Validate uploaded documents against checklist (format, completeness, expiration)
5. Cross-reference identity data with verification sources
6. Flag discrepancies or missing documents for manual review
7. Generate compliance summary report with pass/fail status

## Pitfalls

- KYC requirements differ significantly by jurisdiction — don't apply one-size-fits-all checklists
- Document expiration dates matter; expired IDs fail verification even if content is correct
- Corporate structures (LLC, trust, foundation) require layered documentation — entity docs + beneficial owner info
- Privacy laws (GDPR, CCPA) restrict how identity data is stored and processed
- Automated validation catches format issues but not sophisticated document forgery
