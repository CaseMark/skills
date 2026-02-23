---
name: fda-device-registration
description: Drafts FDA Establishment Registration and Device Listing documents compliant with 21 CFR Part 807 for medical device manufacturers. Structures filings with establishment details, owner/operator information, device inventories, compliance certifications, and signature blocks using current FDA forms. Use for initial registrations, annual renewals, listing updates, or foreign establishment filings with US agent designations.
tags:
  - drafting
  - memo
  - regulatory
  - research
---

# FDA Establishment Registration & Device Listing

Drafts a complete 21 CFR Part 807 registration and device listing document suitable for FDA submission.

## Prerequisites

1. **Establishment details** — legal name, FEI number, physical/mailing addresses, business activities
2. **Owner/operator information** — legal names, titles, contact details, signature authority
3. **Device inventory** — product codes, classifications, intended uses, listing numbers, 510(k) numbers
4. **US agent info** (foreign establishments only) — name, address, phone, email
5. **Prior submissions** — previous registration numbers, listing numbers, any pending 510(k)s

## Output Structure

### Document Header

| Field | Content |
|-------|---------|
| Title | Establishment Registration and Device Listing |
| Regulatory basis | 21 CFR Part 807 |
| FDA Form | 2830 (or current equivalent — confirm version at FDA.gov) |
| Preparation date | [Date] |
| Filing type | Initial / Annual Renewal / Update |

### Section 1: Establishment Information

- Legal owner name (must match corporate records)
- FEI number
- Physical address and mailing address (if different)
- Phone, fax, email
- Business activities — use FDA-recognized terms:
  - Manufacturer, Contract Manufacturer, Repackager/Relabeler, Specification Developer, Reprocessor of Single-Use Devices, Foreign Manufacturer, Sterilizer, Component Manufacturer

### Section 2: Owner/Operator Details

For each responsible party:
- Full legal name and title
- Signature authority designation
- Contact information
- Confirmation of legal authority to bind establishment

### Section 3: Device Listing

For each device, provide:

| Field | Requirement |
|-------|-------------|
| Device name | Common/trade name |
| FDA product code | 3-letter code from FDA classification database |
| Classification | Class I, II, or III |
| Intended use | Technical description aligned with labeling |
| Listing number | If previously assigned |
| 510(k) number | If applicable |
| Predicate device | If applicable |
| Exempt from premarket? | Yes/No with regulatory citation |

### Section 4: Compliance & Certifications

Include statements covering:

- [ ] Adherence to 21 CFR Part 807 registration requirements
- [ ] QSR compliance (21 CFR Part 820) where applicable
- [ ] Accurate representation of device classifications
- [ ] US agent designation (foreign establishments — 21 CFR 807.40)
- [ ] Any claimed exemptions with specific regulatory citations and justifications
- [ ] MDR reporting obligations acknowledged (21 CFR Part 803)

### Section 5: Foreign Establishment Requirements

If applicable, document the US Agent:
- Agent name, company, address, phone, email
- Written agreement confirmation per 21 CFR 807.40(c)

### Section 6: Signatures & Attestations

Signature block must include:
- Printed name, title, date, signature line
- Attestation language: accuracy/completeness of information, acknowledgment of 18 U.S.C. § 1001 (false statements), authority to bind establishment
- Owner/operator signature required; additional signatories as needed

## Guidelines

- **Terminology**: Use only FDA-recognized activity descriptions and product codes — do not paraphrase
- **FEI consistency**: Verify FEI number matches FURLS (FDA Unified Registration and Listing System) records
- **Annual renewal**: Registration must be renewed between October 1 and December 31 each year
- **Listing updates**: Submit within 30 days of any change in device commercial distribution status
- **Cross-reference**: All device classifications must match the current FDA Product Classification Database
- **Format**: Structure output to mirror FDA Form 2830 field order for ease of transfer to electronic submission
- **Do not fabricate** product codes, FEI numbers, or 510(k) numbers — flag missing data with `[REQUIRED — obtain from client]`
- **Mark uncertain citations** with `[VERIFY]` — particularly any guidance document references that may have been superseded
