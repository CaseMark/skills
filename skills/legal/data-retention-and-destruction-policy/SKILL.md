---
name: data-retention-and-destruction-policy
description: Drafts a comprehensive law firm Data Retention and Destruction Policy governing client file lifecycles, practice-area retention schedules, secure destruction procedures for paper and electronic records, legal hold protocols, and compliance infrastructure. Addresses ABA Model Rules 1.6 and 1.15, HIPAA, Sarbanes-Oxley, and IRS standards. Use when establishing or updating firm-wide records management frameworks, drafting retention schedules by matter type, or implementing secure destruction procedures across paper and digital systems.
tags:
  - drafting
  - memo
  - regulatory
---

# Data Retention and Destruction Policy

Drafts a law firm records management policy covering retention periods by practice area, secure destruction methods for paper and electronic records, legal hold procedures, and compliance infrastructure.

## Prerequisites

1. **Firm profile** — practice areas, office locations, jurisdictions of licensure
2. **Current systems** — document management platforms, cloud storage, email systems, backup infrastructure
3. **State bar rules** — applicable ethics rules on client files and record retention (jurisdiction-specific)
4. **Existing policies** — information security, conflict procedures, client intake protocols
5. **Vendors** — any certified document destruction services currently used

## Output Structure

### 1. Introduction & Regulatory Framework

State policy purpose and cite applicable authorities:

| Authority | Applicability |
|-----------|--------------|
| ABA Model Rules 1.6, 1.15 | Confidentiality; safekeeping of client property |
| State ethics rules | Jurisdiction-specific retention mandates (controls where more stringent) |
| Sarbanes-Oxley Act | Firms handling securities matters |
| HIPAA | Health law practices |
| IRS / IRC § 6001 | Tax-related work; 7-year documentation standard |

### 2. Scope

**Covered materials:**
- Client matter files (pleadings, correspondence, research, discovery, transactional docs, work product)
- Financial records (trust ledgers, billing, payments, general accounting)
- Intake records (conflict databases, engagement letters, declination letters)
- Electronic records (email, cloud storage, mobile devices, metadata, backup systems)
- Third-party platforms used for document sharing or collaboration

**Exclusions / carve-outs:**
- Original client-owned documents (wills, deeds, stock certificates) → must be returned upon matter close; destruction requires written client authorization
- Transitory communications (scheduling, duplicative courtesy copies) → may be deleted promptly

**Bound parties:** All firm personnel (equity partners, associates, of counsel, paralegals, administrative staff, IT, contract attorneys) and third-party service providers operating under confidentiality agreements.

### 3. Retention Schedule

| Record Category | Minimum Retention | Basis |
|-----------------|-------------------|-------|
| General litigation / transactional files | 6 years post-matter close | Malpractice SOL + margin |
| Estate planning files | Permanent, or until client death + estate admin period + SOL | Latent claim risk post-death |
| Real estate transactions | 7–10 years post-close | Title / environmental latency |
| Corporate formation / governance | Entity lifetime + 7 years post-dissolution | Ongoing relevance |
| Tax return preparation files | 7 years post-filing | IRS extended audit period (6-yr for substantial understatement) |
| Trust account records | 6 years minimum (or state bar rule, whichever is longer) | State ethics rules |
| General firm accounting | 7 years | Tax audit exposure |
| Conflict check / intake records | Duration of firm operation | Ongoing conflicts screening |
| Destruction logs | 3 years | Compliance evidence |

> **Legal Hold Override:** Normal schedules suspend immediately upon reasonable anticipation of litigation, regulatory investigation, or bar disciplinary proceedings. Holds require a written notice identifying scope, reason, and responsible personnel. Retention periods restart from the hold release date, not original matter close.

### 4. Destruction Procedures

**Paper / Physical Documents**
- Cross-cut shredding to ≥ DIN 66399 security level P-4
- On-site firm-controlled shredding OR certified destruction vendor with chain-of-custody certificates and certificates of destruction
- Prohibition: no disposal in regular trash, unsecured recycling, or any method leaving documents intact or reconstructable

**Electronic Records**

| Sensitivity | Required Method |
|-------------|----------------|
| Standard data | Cryptographic erasure / multi-pass overwrite per NIST SP 800-88 |
| Highly sensitive | Degaussing (magnetic media) or physical destruction (shredding, crushing, incineration) |
| SSDs / flash memory | Cryptographic erasure or physical destruction (overwriting is unreliable) |

OS deletion and recycle bin emptying are **not** sufficient — original data remains forensically recoverable.

**Scope of electronic destruction** must include: local workstations, network file servers, cloud storage, email servers, mobile devices, backup systems (all generations), and removable media (USB drives, external drives).

**Device retirement:** All devices leaving firm control must undergo complete sanitization or physical destruction before transfer. Factory resets and reformatting are insufficient.

**Client notification before destruction:**
- Provide written notice to client when closed matter becomes eligible for destruction
- Allow reasonable retrieval period; document client authorization or non-response
- Maintain authorization records

**Destruction log (required for every destruction event):**

| Field | Required Entry |
|-------|---------------|
| Date | Date destruction performed |
| Description | Record category, matter identifier |
| Method | Shredding, cryptographic erasure, physical destruction, etc. |
| Personnel | Name(s) of staff who performed or supervised |

### 5. Responsibilities

| Role | Core Duties |
|------|-------------|
| Records Management Officer / Compliance Partner | Policy administration, exception authorization, legal hold coordination, audit oversight, regulatory monitoring |
| Supervising Attorneys | Annual file review, retention period authorization, special-circumstance determinations, legal hold initiation |
| IT Personnel | Configure automated retention flags in DMS, implement secure deletion, encrypt stored data, verify backup inclusion/exclusion per policy |
| Administrative Staff | Execute physical destruction, maintain destruction logs, coordinate client file notifications, track retention schedules by matter |

### 6. Training Requirements

- **New hire:** Policy overview, confidentiality obligations, proper records handling, consequences of non-compliance
- **Annual refresher:** Policy updates, audit findings, evolving best practices
- **Records management personnel:** Technical electronic destruction, legal hold procedures, documentation requirements
- All training documented with signed acknowledgments retained in personnel files

### 7. Compliance & Auditing

**Annual internal audit:**
- Sample of closed files → verify timely destruction after period expiration
- Destruction log completeness and accuracy
- Attempt data recovery on supposedly destroyed electronic records
- Legal hold documentation review

**Quarterly legal hold review:**
- Confirm triggering event remains active
- Narrow scope where possible to reduce burden
- Release promptly upon resolution; document release in writing and notify all affected personnel

**Vendor oversight (annual):**
- Review certifications, liability insurance, security protocols, personnel background checks
- Periodic on-site inspection of destruction facilities where feasible
- Contracts must include: confidentiality obligations, security requirements, indemnification provisions

**Incident reporting:** All personnel must immediately report violations, breaches, or unauthorized access to the Compliance Officer. Firm will not retaliate against good-faith reporters. Incidents trigger: root cause investigation, client notification assessment, regulatory reporting assessment, corrective measures.

### 8. Policy Maintenance

- **Annual review:** Records Management Officer + firm leadership; document findings and any schedule adjustments
- **Interim review triggers:** statutory or ethics rule changes, new technology adoption, significant data breach
- **Amendments:** Approved by firm management → communicated to all personnel within 30 days (email with read receipt or mandatory training) → incorporated into new-hire and annual training
- **Version control:** Maintain version history with effective dates, description of substantive changes, and approval documentation

## Guidelines

- **State bar rules control:** Where state ethics rules impose longer retention than this schedule, the state rule governs — [VERIFY] applicable state minimum for trust account records (commonly 5–7 years; varies by jurisdiction)
- **[VERIFY]** Applicable malpractice statute of limitations and discovery rule before setting retention period floors; adjust schedule if jurisdiction exceeds 6-year baseline
- **No indefinite retention:** Retaining data beyond policy periods without documented justification increases breach exposure without corresponding legal benefit
- **Metadata:** Electronic destruction must address embedded metadata, not just visible document content
- **Cloud/SaaS:** Confirm contractual rights to permanently delete data; obtain vendor deletion certifications as part of destruction documentation
- **Backups:** Destruction protocols must explicitly include all backup generations; omitting backups leaves supposedly destroyed data fully recoverable
- **Malpractice defense carve-out:** Consider allowing attorneys to flag specific closed matters for extended retention where facts suggest heightened malpractice exposure; require written justification and Records Management Officer approval
