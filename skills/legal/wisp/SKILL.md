---
name: wisp
description: Drafts a comprehensive Written Information Security Program (WISP) compliant with Massachusetts 201 CMR 17.00 and supplementary frameworks (GDPR, CCPA, HIPAA, GLBA, PCI-DSS). Produces a complete, board-ready regulatory document covering coordinator designation, risk assessment, administrative/technical/physical safeguards, employee training, incident response with breach notification timelines, and third-party vendor oversight. Use when an organization owns, licenses, stores, or maintains personal information of Massachusetts residents and needs a standalone compliance artifact for regulatory examination or executive approval.
tags:
  - drafting
  - memo
  - regulatory
  - research
---

# Written Information Security Program (WISP)

Drafts a 201 CMR 17.00-compliant WISP that satisfies regulatory examination and functions as an operational security blueprint.

## Prerequisites

1. **Organization profile** — legal name, industry, jurisdictions of operation, number of employees
2. **Data inventory** — types of personal information collected, storage locations, transmission methods, access roles
3. **Existing security materials** — current policies, prior WISP versions, risk assessments, security audit reports, incident logs
4. **Vendor list** — third-party service providers with access to personal information
5. **Coordinator identity** — designated WISP coordinator name/title, or confirmation none exists
6. **Supplemental frameworks** — any applicable laws beyond MA (GDPR, CCPA, HIPAA, GLBA, PCI-DSS)

## Output Structure

Produce a formally numbered regulatory document with table of contents, definitions section, body sections below, and appendices as needed.

### Section 1 — Executive Summary & Program Purpose

| Field | Content |
|---|---|
| Effective Date | [DATE] |
| Version | [N] |
| Governing Regulation | 201 CMR 17.00; [additional frameworks] |
| Scope | Personal information of MA residents owned, licensed, stored, or maintained by [Org] |
| Commitment Statement | One-paragraph executive commitment to administrative, technical, and physical safeguards |

### Section 2 — WISP Coordinator Designation

- Name, title, department, direct contact
- Authority: implements, supervises, and maintains the program
- Reporting line to executive leadership, IT, and legal counsel
- If no coordinator exists: recommend qualifications and insert placeholder language flagged `[ACTION REQUIRED]`

### Section 3 — Risk Assessment Framework

- Methodology for identifying foreseeable internal and external risks across the data lifecycle (collection → destruction)
- Risk matrix: likelihood × impact categorization
- Scope: employee access, system vulnerabilities, physical gaps, third-party exposure
- Reassessment schedule (at minimum: annually and after material organizational change)
- If prior assessments are available: incorporate specific findings and mitigation status

### Section 4 — Security Safeguards

**4A — Administrative**
- Access control and least-privilege policies
- Pre-employment background checks
- Disciplinary procedures for policy violations
- Termination/offboarding protocols (credential revocation, device return)

**4B — Technical**

| Control | Standard |
|---|---|
| Encryption at rest | AES-256 or equivalent |
| Encryption in transit | TLS 1.2+ |
| Authentication | MFA for systems containing personal information |
| Patch management | Critical patches within [N] days |
| Monitoring | Log retention, anomaly alerting |
| Secure disposal | NIST SP 800-88 media sanitization [VERIFY] |

**4C — Physical**
- Facility access controls (badge, visitor logs)
- Workstation lock/screen-lock policies
- Clean desk requirements
- Environmental controls (fire suppression, flood protection)
- Mobile device encryption and remote-wipe capability

### Section 5 — Employee Training Program

| Element | Detail |
|---|---|
| Frequency | Annual + new-hire onboarding |
| Delivery | [In-person / LMS / vendor platform] |
| Topics | Data handling, password hygiene, phishing/social engineering, incident reporting, clean desk |
| Role-specific | Elevated training for employees with broad personal-information access |
| Documentation | Completion records retained for [N] years |
| Non-compliance | Disciplinary consequences per HR policy |

### Section 6 — Monitoring, Review & Program Maintenance

- Ongoing monitoring of safeguards with defined metrics
- Annual security audit schedule; penetration testing cadence
- Trigger-based WISP reviews: new technology, new threats, regulatory changes, organizational restructuring
- Post-incident review process feeding continuous improvement

### Section 7 — Incident Response & Breach Notification

**Response Phases:** Detection → Containment → Investigation → Remediation → Notification → Post-Mortem

| Notification Obligation | Trigger | Timeline |
|---|---|---|
| Affected individuals | Unauthorized acquisition of personal information | Expeditiously / as soon as reasonably possible |
| MA Attorney General | Same as above | Same timeframe |
| MA Director of Consumer Affairs and Business Regulation | Same as above | Same timeframe |

- Incident response team: roles, escalation path, decision authority for breach determination
- Evidence preservation requirements
- Coordination protocol: legal counsel, law enforcement, PR
- Template notification language in Appendix
- Incident log retention requirements

### Section 8 — Third-Party Service Provider Oversight

- Vendor risk assessment prior to engagement (data access scope, security posture)
- Required contractual provisions: data protection obligations, audit rights, breach notification duties (timeline ≤ [N] hours), liability
- Ongoing monitoring: annual vendor security reviews or after material vendor change
- Approved vendor register maintained by WISP Coordinator

## Guidelines

- **Cite 201 CMR 17.00 section numbers** throughout each corresponding safeguard section
- **Flag all [VERIFY]** citations before finalizing — statutory amendments or agency guidance may affect compliance obligations
- **Multi-jurisdiction orgs**: layer GDPR Article 32, CCPA § 1798.150, HIPAA Security Rule 45 CFR Part 164, or GLBA Safeguards Rule as applicable; note conflicts requiring legal resolution
- **Do not over-specify technology**: reference standards (AES-256, TLS 1.2+) rather than specific vendor products to avoid making the WISP operationally brittle
- **Flag gaps**: any section where organizational information is unavailable should be marked `[ACTION REQUIRED — provide details for compliance]`
- **Tone**: formal regulatory language accessible to both technical and non-technical readers; suitable for board presentation and regulatory examiner review
