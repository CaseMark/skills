---
name: e-discovery-protocol-agreement
description: Drafts a court-ready ESI Protocol Agreement governing electronically stored information exchange in U.S. federal litigation. Enforces FRCP 26(f)/34 compliance, FRE 502(d) clawback protections, TAR/predictive coding methodology, privilege log protocols, and technically precise production format specifications. Use when drafting e-discovery stipulations, ESI protocols, meet-and-confer agreements, or joint discovery plans during the discovery phase of commercial litigation.
tags:
  - agreement
  - drafting
  - litigation
---

# E-Discovery Protocol Agreement

Drafts a litigation-ready ESI Protocol Agreement establishing search methodology, production formats, privilege procedures, and clawback protections for U.S. commercial litigation.

## Prerequisites

1. **Court caption** — court name, case number, full party names, assigned judge
2. **Case materials** — meet-and-confer correspondence, prior ESI orders, existing discovery requests
3. **Custodian list** — names and roles of key custodians per party
4. **ESI sources** — email platforms, DMS, collaboration tools, mobile devices, cloud storage
5. **Search terms** — agreed Boolean/proximity terms, or parameters for TAR methodology
6. **Date ranges** — preservation trigger date and production date range
7. **Production specs** — native vs. TIFF, agreed metadata fields (if pre-negotiated)

## Output Structure

### 1. Caption & Recitals
- Full court caption mirroring prior filings; all counsel of record
- Rule 26(f) conference date; good-faith cooperation statement
- Rule 26(b)(1) proportionality commitment

### 2. Preservation

| Element | Content |
|---|---|
| Trigger date | Date preservation obligations arose |
| Key custodians | Name, title, party affiliation |
| ESI sources in scope | Email, DMS, shared drives, mobile, cloud, collaboration tools |
| Excluded sources | Basis for exclusion under FRCP 26(b)(2)(B) (burden/inaccessibility) |
| Litigation hold | Confirmation holds issued; IT contact identified per party |

### 3. Search Methodology

**Option A — Keyword Search**
- Search terms listed in **Exhibit A** with Boolean connectors and proximity operators
- Custodian-specific application vs. across-the-board — specify which
- Iterative refinement process; meet-and-confer obligation on hit count reports

**Option B — Technology-Assisted Review (TAR/Predictive Coding)**
- Platform and vendor identification
- Seed set composition and training protocol
- QC metrics: elusion rate, recall/precision targets
- Validation via statistical sampling; disclosure obligations to opposing counsel

### 4. Production Format

| Document Type | Format | Notes |
|---|---|---|
| Standard documents | TIFF (Group IV) + extracted text + load file | Unitized per document |
| Native-required | Native + TIFF slip-sheet placeholder | Spreadsheets, audio, video, CAD |
| Email | TIFF or native (per agreement) | Threading preserved |
| Databases | Field-level export per meet-and-confer | TBD by data type |

**Required Metadata Fields:**
`BegBates`, `EndBates`, `BegAttach`, `EndAttach`, `Custodian`, `FilePath`, `FileName`, `FileExt`, `FileSize`, `DateCreated`, `DateModified`, `DateSent`, `DateReceived`, `Author`, `To`, `CC`, `BCC`, `Subject`, `MD5Hash`, `Confidentiality`

### 5. Deduplication
- Global (cross-custodian) or custodian-level — specify which
- Hash-value method (MD5 or SHA-1)
- All custodians reflected in metadata for de-duped documents

### 6. Privilege Log

| Field | Required |
|---|---|
| Bates range (if redacted) | Yes |
| Date | Yes |
| Author / Sender | Yes |
| Recipients (To/CC/BCC) | Yes |
| Document type | Yes |
| Privilege basis | Yes |
| Subject (non-revealing description) | Yes |

- Deadline: [X] days after each rolling production or [fixed date]
- Categorical logs permitted for: [e.g., post-litigation-hold attorney-client communications]
- Sampling/statistical extrapolation provisions: include if volume warrants

### 7. FRE 502(d) Clawback

Agreement constitutes a **court order under FRE 502(d)** upon approval — inadvertent production waives neither privilege nor work-product protection in this or any other proceeding.

**Procedure:**
1. Producing party notifies in writing within [X] days of discovering inadvertent production
2. Receiving party ceases review, sequesters materials, and returns/destroys within [X] days
3. No copies retained; receiving party may challenge designation by motion (burden on producing party)

### 8. Additional Provisions (as applicable)

- **Cost allocation** — for inaccessible/legacy sources under Rule 26(b)(2)(B)
- **PII/confidentiality** — handling protocol for sensitive personal data
- **Forensic imaging** — chain of custody and imaging protocol if device forensics required
- **IT/custodian depositions** — 30(b)(6) topics re: ESI systems, if anticipated
- **Dispute resolution** — expedited meet-and-confer → magistrate referral → motion practice

### 9. Proposed Court Order
- Signature blocks for all counsel of record
- Signature line for judge incorporating FRE 502(d) protections
- Case number and proposed order title formatted for docketing

## Guidelines

- Reference current **Sedona Conference Principles** [VERIFY current edition] as interpretive backdrop where appropriate
- All technical specs must be implementable by IT vendors and forensic consultants without further clarification
- No placeholder brackets in final output — resolve all gaps from uploaded case materials or flag explicitly for attorney input before filing
- Include rolling production schedule and volume estimates if disclosed in meet-and-confer materials
- For state court matters, cross-check against applicable state e-discovery rules — not all states track FRCP
- Maintain neutral, cooperative tone throughout — this is a joint stipulation, not adversarial pleading
