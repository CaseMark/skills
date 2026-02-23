---
name: auth-packet-summary
description: Generates a structured authorization packet summary for personal injury cases, validating execution of retainer agreements, HIPAA releases, insurance authorizations, and employment record releases. Confirms signatures, dates, completeness, and compliance to trigger the investigation phase. Use when reviewing client onboarding documents, verifying authorization forms, checking HIPAA compliance, or confirming record release authorizations before discovery.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Authorization Packet Summary

Validates and summarizes the four essential client authorization forms in a personal injury matter, confirming the firm's legal authority to request third-party records.

## Prerequisites

1. **Uploaded case documents** — all client-signed authorization forms available in the matter
2. **Case identifiers** — client full legal name, case/matter number
3. **Firm style guide** — letterhead, fonts, margin specs for PDF output

## Required Authorization Forms

| # | Form | Purpose |
|---|------|---------|
| 1 | Retainer Fee Agreement | Establishes attorney-client relationship and fee structure |
| 2 | HIPAA Medical Record Release | Authorizes healthcare providers to disclose PHI |
| 3 | Insurance Communication Authorization | Permits contact with carriers and access to claims files |
| 4 | Wage & Employment Record Release | Allows firm to obtain employment history, wage records, personnel files |

## Process

### Step 1: Locate and Extract

Search all uploaded case documents for each of the four authorization forms. For each form, extract:

- Client full legal name (as it appears on the form)
- Case number / matter ID
- Execution date
- Categories of records authorized
- Temporal limitations on scope
- Named entities / providers
- Witness signatures and notarization (if applicable per jurisdiction)

### Step 2: Validate Each Form

Assign one status per form:

| Status | Meaning |
|--------|---------|
| **Complete and Valid** | All required elements present — signatures, dates, scope, mandatory fields |
| **Received but Deficient** | Form present but missing required elements (specify exactly what) |
| **Not Received** | Form absent from case file |

Check each form for:
- [ ] Client signature present and legible
- [ ] Date fully completed
- [ ] All mandatory fields filled (name, DOB, case matter, scope)
- [ ] Witness/notarization present if required by state law
- [ ] No expiration issues under applicable privacy regulations

### Step 3: Cross-Reference

Compare extracted data across all four forms for consistency in:
- Client name spelling
- Case/matter number
- Dates and date ranges
- Flag and document all discrepancies

### Step 4: Compile Authorization Checklist

Produce a table with these columns:

| Authorization Type | Status | Execution Date | Authorized Entities | Scope Limitations | Notes / Deficiencies |
|--------------------|--------|----------------|--------------------|--------------------|---------------------|
| Retainer Fee Agreement | | | | | |
| HIPAA Medical Record Release | | | | | |
| Insurance Communication Auth | | | | | |
| Wage & Employment Record Release | | | | | |

For deficient or missing forms, specify the exact corrective action (e.g., "Missing client signature on page 2" or "Must identify all employers for relevant period").

### Step 5: Draft Narrative Summary

Write a formal memorandum containing:

1. **Status statement** — As of [date], confirm whether all authorizations are complete or identify outstanding items
2. **Per-form scope summary** — Brief description of each authorization's scope, noting temporal or entity-specific limitations
3. **Issues** — Name discrepancies, missing witness signatures, approaching expirations
4. **Conclusion** — Either:
   - "Investigation phase may commence; firm is authorized to request records from all identified entities within scope of client consent," OR
   - "Corrective actions required before record requests may proceed" with specifics and responsible party

Tone: formal, definitive, suitable as permanent case file record.

## Output Documents

1. **Authorization Checklist** — structured table for case management system reference
2. **PDF Memorandum** — formal memo with:
   - Firm letterhead
   - Serif body text, 11–12pt, 1-inch margins
   - Header: case ID, client name, date, subject line "Authorization Packet Summary"
   - Body: narrative summary
   - Footer: page numbers, `ATTORNEY-CLIENT PRIVILEGED AND CONFIDENTIAL`, `ATTORNEY WORK PRODUCT`
   - Signature/approval lines per firm policy

## Guidelines

- Never mark a form "Complete and Valid" unless every required element is confirmed present
- Note all scope limitations prominently — staff requesting records must know the boundaries of consent
- If any form is deficient or missing, do **not** authorize commencement of record requests
- Resolve name-spelling discrepancies by reference to the original document; flag for correction
- Handle all output as privileged and confidential; transmit only via secure channels
- This summary may be reviewed by ethics committees, bar authorities, or malpractice carriers — accuracy and completeness are non-negotiable
- Jurisdiction-specific witnessing or notarization requirements vary by state; flag any uncertainty
