---
name: sam-reps-certs
description: Drafts Representations and Certifications documents for SAM.gov federal contractor registration, covering entity identification, UEI, NAICS codes, business size determinations, socioeconomic category eligibility, FAR compliance representations, and integrity certifications under penalty of perjury. Use when registering entities in SAM.gov, updating annual registrations, or preparing government contracting eligibility documents.
tags:
  - agreement
  - drafting
  - regulatory
---

# SAM.gov Representations and Certifications

Drafts the mandatory Representations and Certifications document for SAM.gov registration and federal contracting eligibility.

## Prerequisites

1. **Entity legal name** — plus any DBA names
2. **UEI** (replaced DUNS in April 2022) and **TIN**
3. **CAGE code** if previously assigned
4. **Primary and secondary NAICS codes** with applicable SBA size standards
5. **Organizational structure** — corporation, LLC, partnership, sole proprietorship, etc.
6. **State of incorporation/organization**, fiscal year end, congressional district
7. **Ownership and affiliation data** — percentages, parent/subsidiary relationships per 13 CFR 121.103
8. **Socioeconomic certifications** — SBA certification numbers for any claimed status
9. **Revenue or employee count** for size standard determination under primary NAICS
10. **Authorized signatory** with binding authority for the entity

## Output Structure

### Section 1: Header and Purpose

| Field | Content |
|-------|---------|
| Title | "Representations and Certifications — SAM.gov Registration" |
| Entity | Full legal name |
| Date of submission | [DATE] |
| Validity | One year from submission; material changes updated within 60 days |
| Penalty notice | Made under penalty of perjury per 18 U.S.C. § 1001 |

### Section 2: Entity Identification

Populate all required SAM.gov fields:

| Field | Source |
|-------|--------|
| Legal business name | Client |
| DBA name(s) | Client |
| Physical address | Client |
| Mailing address | Client (if different) |
| UEI | Client |
| TIN | Client |
| CAGE code | Client or "To be assigned" |
| Primary NAICS | Client |
| Secondary NAICS | Client |
| Organizational structure | Client |
| State of incorporation | Client |
| Fiscal year end | Client |
| Congressional district | Client |

### Section 3: Business Size and Socioeconomic Representations

For each category, state status and factual basis:

| Category | FAR/SBA Reference | Required Support |
|----------|-------------------|------------------|
| Small business | SBA size standard for primary NAICS | Revenue or employee count |
| Small disadvantaged business | 13 CFR 124 | SBA 8(a) cert number if applicable |
| Women-owned small business | FAR 52.219-29 | Ownership % + WOSB cert |
| Economically disadvantaged WOSB | FAR 52.219-30 | EDWOSB cert |
| Veteran-owned small business | 38 U.S.C. § 8127 | VA CVE verification |
| Service-disabled veteran-owned | FAR 52.219-27 | VA CVE verification + disability documentation |
| HUBZone | 13 CFR 126 | SBA HUBZone cert + principal office location |

Include affiliation analysis under 13 CFR 121.103 — list all parent companies, subsidiaries, and affiliates that factor into size determination.

### Section 4: FAR Compliance Representations

Number each representation sequentially. Include FAR clause citation and entity's status (Compliant / Not Applicable / Explanation Attached).

| Representation | FAR Clause | Key Requirement |
|---------------|------------|-----------------|
| Telecom/video surveillance equipment | FAR 52.204-26 | No covered equipment per NDAA § 889 |
| Tax delinquency | 26 U.S.C. § 7122 | No unpaid federal tax liability |
| Felony conviction | FAR 9-10.2 | No felony conviction within 24 months |
| State sponsors of terrorism | FAR 52.225-13 | No business relationships |
| Equal opportunity | FAR 52.222-22 | Compliance certified |
| E-Verify | FAR 52.222-54 | Enrolled and participating |
| Davis-Bacon Act | FAR 52.222-6 | If construction — compliance confirmed |
| Service Contract Act | FAR 52.222-41 | If services — compliance confirmed |

### Section 5: Integrity and Compliance Certifications

Draft formal certifications for each:

- [ ] Not presently debarred, suspended, proposed for debarment, declared ineligible, or voluntarily excluded
- [ ] No fraud conviction or civil judgment in connection with a public transaction within prior 3 years
- [ ] Compliance with Title VI (Civil Rights Act), Title IX (Education Amendments), Section 504 (Rehabilitation Act), Age Discrimination Act
- [ ] Drug-Free Workplace Act of 1988 compliance
- [ ] Lobbying restrictions per 31 U.S.C. § 1352 — Byrd Anti-Lobbying Amendment
- [ ] Environmental compliance certifications
- [ ] For contracts >$10M: tax obligations under IRC § 6050M [VERIFY] and no business relationships with terrorist organizations

### Section 6: Attestation and Signature Block

```
ATTESTATION

I, [NAME], [TITLE], hereby certify under penalty of perjury that the
foregoing representations and certifications are current, accurate, and
complete to the best of my knowledge and belief. I understand that false
statements may result in criminal prosecution under 18 U.S.C. § 1001,
civil penalties, and suspension or debarment from federal contracting.

I acknowledge the obligation to update these representations within
60 days of any material change affecting eligibility or accuracy.

_________________________     _________________________
Signature                     Date

Name:    [PRINTED NAME]
Title:   [TITLE]
Email:   [EMAIL]
Phone:   [PHONE]

Electronic signatures accepted per ESIGN Act; must comply with
SAM.gov authentication requirements.
```

## Guidelines

- **Annual renewal**: SAM.gov registrations expire after one year — flag renewal dates
- **60-day update rule**: Any material change to representations must be updated within 60 days
- **Verify all FAR citations** against current FAR at acquisition.gov before submission
- **Cross-reference SAM.gov requirements** published by GSA — field requirements change periodically
- **Affiliation analysis is critical**: Understating affiliations is a common basis for False Claims Act liability
- **Do not guess socioeconomic status**: Each claimed category must be supported by formal SBA certification or verifiable facts
- **Penalty of perjury**: Remind client that all statements carry criminal liability — signatory must have actual knowledge
- **Format output** to match SAM.gov portal organizational structure with sequential numbering
