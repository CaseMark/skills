---
name: data-processing-addendum
description: Drafts a GDPR-compliant Data Processing Addendum (DPA) establishing binding obligations between data controllers and processors under Article 28 GDPR. Extracts party details, processing scope, and service terms from uploaded documents. Produces a complete, execution-ready DPA with all mandatory Article 28(3) elements and four standard schedules. Use when supplementing a service agreement with data protection terms, negotiating processor contracts, or achieving GDPR Article 28 compliance for EU data processing relationships.
tags:
  - agreement
  - drafting
  - regulatory
---

# GDPR Data Processing Addendum (DPA)

Drafts an Article 28-compliant DPA as a standalone addendum to an underlying service agreement, covering all mandatory processor obligations and four execution-ready schedules.

## Prerequisites

1. **Underlying service agreement** — governing law, notice clauses, effective date, termination provisions
2. **Party details** — full legal names, registered addresses, company registration numbers, DPO contact info for both controller and processor
3. **Processing description** — subject matter, duration, nature/purpose of processing, types of personal data, categories of data subjects (if special category data under Art. 9 is involved, flag explicitly)
4. **Sub-processor list** — existing sub-processors with names, locations, and processing activities
5. **Security posture** — existing certifications (ISO 27001, SOC 2), policies, or audit reports
6. **Transfer mechanisms** — any existing SCCs, BCRs, adequacy decisions, or transfer impact assessments if EEA transfers are involved

## Output Structure

Produce a numbered, cross-referenced legal document with recitals, operative provisions, signature block, and four schedules. Follow the section structure below.

---

### Section 1 — Parties & Relationship to Main Agreement

| Element | Drafting requirement |
|---|---|
| Party identification | Full legal name, address, registration number, DPO details for each party |
| Hierarchy | DPA prevails over main agreement on data protection matters |
| Effective date | Specify; note retroactive application if processing already underway |
| Integration clause | DPA forms integral part of main agreement |

---

### Section 2 — Processing Details (→ Schedule B)

Draft Schedule B simultaneously; cross-reference here.

- **Subject matter & duration**: Tied to service agreement term; include renewal/termination triggers
- **Nature & purpose**: Enumerate specific operations (collection, storage, analysis, transmission, deletion); confirm processing is limited to what is necessary and proportionate
- **Personal data types**: Distinguish ordinary vs. special category (Art. 9); list each category
- **Data subject categories**: Employees, customers, end-users, children (flag if Art. 8 applies), etc.

---

### Section 3 — Processor Instructions & Restrictions

Mandatory Art. 28(3)(a) elements:

- [ ] Process only on documented controller instructions; specify initial instruction scope via this DPA and main agreement
- [ ] Procedure for issuing additional/modified instructions (form, acknowledgment timeframe)
- [ ] Processor must immediately notify controller if any instruction violates GDPR or Member State law
- [ ] If legal obligation requires processing beyond instructions, processor notifies controller before processing unless prohibited on public-interest grounds

---

### Section 4 — Security of Processing (Art. 32) (→ Schedule C)

Draft Schedule C simultaneously; cross-reference here. Security measures must address risk of accidental/unlawful destruction, loss, alteration, unauthorized disclosure, or access.

Minimum domains to address in Schedule C:

| Domain | Examples |
|---|---|
| Pseudonymization & encryption | At-rest and in-transit; key management |
| Confidentiality & integrity | Access controls, least-privilege, logging |
| Availability & resilience | Redundancy, disaster recovery, RTO/RPO |
| Testing & evaluation | Penetration testing cadence, vulnerability management |
| Personnel | Confidentiality obligations or statutory duty for all authorized personnel |

Reference existing certifications (ISO 27001, SOC 2 Type II, TISAX) as baseline evidence where available.

---

### Section 5 — Sub-processor Engagement (Art. 28(2), 28(4)) (→ Schedule A)

- [ ] General written authorization granted (preferred) OR specific authorization required per sub-processor
- [ ] 30-day advance notice of additions/replacements (adjustable); controller may object on reasonable grounds
- [ ] Objection consequences: processor proposes alternative OR controller may terminate relevant services without penalty
- [ ] Sub-processors bound by contract imposing equivalent obligations (Art. 28(4))
- [ ] Processor remains fully liable for sub-processor performance
- [ ] Maintain current Schedule A: sub-processor name, location, processing activity

---

### Section 6 — Data Subject Rights Assistance (Art. 12–23)

- [ ] Processor implements technical/organizational measures to support controller's response to: access (Art. 15), rectification (Art. 16), erasure (Art. 17), restriction (Art. 18), portability (Art. 20), objection (Art. 21)
- [ ] Upon receiving any direct data subject request: notify controller within **48 hours**; do not respond without controller's documented instruction
- [ ] Cost allocation for resource-intensive requests: address consistently with main agreement fee schedule

---

### Section 7 — Personal Data Breach Notification (Art. 33–34)

- [ ] Notify controller **without undue delay, maximum 24 hours** after processor becomes aware of breach (adjust based on data sensitivity)
- [ ] Definition: Art. 4(12) — accidental or unlawful destruction, loss, alteration, unauthorized disclosure of or access to personal data

Minimum notification content:

| Field | Required detail |
|---|---|
| Nature of breach | Categories and approximate number of data subjects and records affected |
| Contact point | Processor DPO or designated contact name and details |
| Likely consequences | Risk assessment |
| Measures taken/proposed | Mitigation and remediation steps |

- [ ] Cooperate with controller on investigation, Art. 33/34 supervisory authority notification, and data subject communications
- [ ] Preserve all breach evidence; maintain incident log

---

### Section 8 — Compliance Assistance (Art. 32–36)

- [ ] Assist controller with Art. 32 security obligations
- [ ] Assist with DPIAs (Art. 35) — provide processing records, risk data, technical specs
- [ ] Assist with prior supervisory authority consultation (Art. 36) where required
- [ ] Provide all information necessary to demonstrate Art. 28 compliance
- [ ] Allow for and contribute to audits (see Section 9)

---

### Section 9 — Audits & Inspections

| Parameter | Standard position |
|---|---|
| Advance notice | 30 days (routine); shorter for cause (post-incident, regulatory inquiry) |
| Frequency | Once per year unless cause exists |
| Auditor | Controller's internal team or independent third party (with confidentiality undertaking) |
| Remote/virtual audits | Expressly permitted |
| Alternative evidence | Art. 42 certification, Art. 40 code of conduct, SOC 2 Type II, ISO 27001 reports — accepted where current and comprehensive |
| Cost allocation | Controller bears routine audit costs; processor bears remediation and follow-up audit costs for identified non-compliance |
| Remediation | Specified timeline; escalation mechanism; controller right to suspend processing or terminate for material breach |

---

### Section 10 — Data Return & Deletion

- [ ] At controller's election upon termination/expiry: return data in structured, machine-readable format **OR** securely delete using cryptographic erasure or physical destruction
- [ ] Written certification of completion within **30 days** (standard) / **60 days** (complex multi-system environments)
- [ ] Exception: processor may retain copies required by EU/Member State law (tax, employment, regulatory) — retained data must be: isolated from operational systems; subject to confidentiality; not used for any service delivery purpose
- [ ] Backups: immediate deletion may be infeasible — require isolation, exclusion from restoration except as legally required, deletion per standard backup rotation schedule (document specific schedule)

---

### Section 11 — General Provisions

- [ ] **Definitions**: Incorporate GDPR Art. 4 definitions; add processing-specific defined terms
- [ ] **Governing law**: Must be compatible with GDPR territorial scope (Art. 3); do not undermine data subject rights under Chapter III
- [ ] **International transfers**: If personal data transferred outside EEA, incorporate applicable mechanism — SCCs (Art. 46(2)(c)), BCRs (Art. 47), or adequacy decision (Art. 45); reference transfer impact assessment if required post-*Schrems II*
- [ ] **Amendments**: Written agreement of both parties; process for regulatory-driven updates
- [ ] **Dispute resolution**: Escalation → mediation → litigation/arbitration per governing law

---

### Schedules

| Schedule | Contents |
|---|---|
| **A** | Approved sub-processors: name, registered address, location of processing, processing activity |
| **B** | Processing description: subject matter, duration, nature/purpose, personal data types, data subject categories |
| **C** | Technical and organizational security measures (detail by domain per Section 4) |
| **D** | Existing certifications, audit reports, and compliance documentation |

Flag any schedule where source documents lack sufficient detail; note required information for parties to complete before execution.

---

## Guidelines

- **Art. 28(3) is mandatory** — all eight enumerated elements must appear; omission creates regulatory exposure (fines up to €20M or 4% of global annual turnover)
- **Special category data** (Art. 9): if present, heighten security requirements and explicitly address in Schedule B and C
- **Children's data**: if data subjects include minors, flag Art. 8 and national implementing provisions
- **Jurisdiction**: GDPR applies by Art. 3 territorial scope regardless of processor's location; ensure governing law clause does not conflict
- **SCCs post-*Schrems II*** [VERIFY current EC SCC templates effective June 2021 and EDPB Recommendations 01/2020 on supplementary measures]
- **Do not** include provisions allowing processor to use personal data for its own purposes — this converts processor to controller
- **Do not** grant open-ended sub-processor authorization without at minimum change-notification and objection rights
- **Consistency**: All cost allocation, notice, and termination provisions must be reconciled with the underlying service agreement before execution
