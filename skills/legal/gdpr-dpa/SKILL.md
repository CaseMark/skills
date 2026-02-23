---
name: gdpr-dpa
description: >-
  Drafts GDPR-compliant Data Processing Addenda that implement Article 28
  controller-processor obligations, align with a service agreement, and
  specify processing details, security, sub-processor controls, breach notice,
  audits, and deletion terms. Use when drafting or updating a DPA, vendor GDPR
  addendum, controller-processor agreement, or SCC-adjacent data protection
  addendum; trigger keywords: DPA, data processing addendum, GDPR, Article 28,
  controller, processor, sub-processor, data transfer, SCC, breach
  notification.
tags:
  - agreement
  - drafting
  - regulatory
---

# GDPR Data Processing Addendum (DPA)

Produce an Article 28-compliant DPA with schedules ready for execution.

## Prerequisites

1. Legal names, registered addresses, and registration numbers for Controller and Processor.
2. Underlying agreement name/date and order forms or SOWs.
3. Processing description: subject matter, duration, nature, purpose, and processing operations.
4. Data inventory: categories of data subjects, personal data types, special categories (Art 9) or criminal data (Art 10).
5. Processing locations, transfer map, and intended transfer mechanism (adequacy, SCCs, BCRs, or Art 49 derogation).
6. Security baseline: existing certifications, policies, and technical/organizational measures.
7. Sub-processor list and approval model (general vs specific authorization) with objection window.
8. Incident response SLAs and audit preferences.
9. Termination requirements: return/deletion formats, timelines, retention/backup constraints.

## Output Structure / Process

1. Draft header, recitals, effective date, and order of precedence with the main agreement.
2. Define terms using GDPR language: Controller, Processor, Personal Data, Processing, Sub-processor, Data Protection Laws, Personal Data Breach, Services.
3. Insert Article 28(3) core obligations using the checklist below.
4. Add security (Art 32), breach notification (Arts 33-34), and assistance (Arts 32-36) clauses.
5. Add sub-processor governance (Art 28(2), 28(4)) and liability for sub-processors.
6. Add audit and compliance evidence options (Arts 28(3)(h), 40, 42).
7. Add international transfer terms (Art 46 SCCs, Art 47 BCRs, Art 49 derogations) if data leaves the EEA.
8. Add termination, return, and deletion obligations plus backup handling.
9. Attach schedules A-D and populate from input; mark missing data as Required.

**Article 28(3) Mandatory Clause Checklist**

| GDPR basis | Clause heading | Required content |
| --- | --- | --- |
| Art 28(3)(a) | Instructions | Process only on documented Controller instructions; notify if instruction violates law. |
| Art 28(3)(b) | Confidentiality | Ensure authorized personnel are bound by confidentiality. |
| Art 28(3)(c) | Security | Implement appropriate technical and organizational measures per Art 32. |
| Art 28(3)(d) | Sub-processors | No sub-processing without authorization; flow-down equivalent obligations. |
| Art 28(3)(e) | Data subject rights | Assist Controller with requests under Chapter III. |
| Art 28(3)(f) | Assistance | Assist with Art 32-36 obligations, including DPIA and prior consultation. |
| Art 28(3)(g) | Return/Deletion | Return or delete personal data at end of services; certify. |
| Art 28(3)(h) | Audits/Info | Make information available; allow and contribute to audits. |

**Decision Points Table**

| Decision | Options | Input needed |
| --- | --- | --- |
| Sub-processor authorization | General or specific | Controller policy, objection window |
| Audit model | On-site, remote, third-party, certification | Controller vendor policy, existing reports |
| Breach notice SLA | 24h / 48h / other | Risk tolerance, incident playbooks |
| Data return format | CSV, JSON, native export | System compatibility |
| Transfer mechanism | Adequacy, SCCs, BCRs, Art 49 | Data flows and locations |

**Schedule Templates**

```markdown
Schedule A - Approved Sub-processors
| Name | Location | Processing Activity | Authorization Type | Change Notice Period |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | General/Specific | 30 days |

Schedule B - Description of Processing
| Field | Details |
| --- | --- |
| Subject matter | |
| Duration | |
| Nature of processing | |
| Purpose | |
| Processing operations | |
| Categories of data subjects | |
| Categories of personal data | |
| Special categories (Art 9) | |
| Criminal data (Art 10) | |
| Processing locations | |

Schedule C - Technical and Organizational Measures
| Domain | Measures |
| --- | --- |
| Access control | |
| Encryption/pseudonymization | |
| Logging/monitoring | |
| Availability/resilience | |
| Incident response | |
| Testing/evaluation | |
| Physical security | |

Schedule D - Audit/Certification Evidence
| Evidence | Date | Scope | Link/Reference |
| --- | --- | --- | --- |
| ISO 27001 | | | |
| SOC 2 Type II | | | |
```

## Guidelines

- Align with the governing service agreement and include an order-of-precedence clause for data protection terms.
- Do not promise absolute security; use “appropriate” measures per Art 32 and tie to risk profile.
- If special categories or children’s data are involved, add heightened safeguards and stricter access controls.
- If any non-EEA transfer occurs, specify the mechanism and attach SCCs or equivalent; flag missing transfer basis as a blocker.
- Keep schedules consistent with the DPA text and ensure sub-processor lists are current.
- Mark any uncertain legal citations with `[VERIFY]`.
