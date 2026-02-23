---
name: dd-form-254
description: Drafts DD Form 254 Contract Security Classification Specifications for government contracts involving classified information. Covers contract/entity identification, classification determinations, safeguarding protocols, personnel clearance requirements, and certification blocks per NISPOM and DCSA regulations. Use when preparing security classification specs for prime contractors, subcontractors, SAP/SCI access, or facility clearance documentation.
tags:
  - agreement
  - drafting
  - regulatory
---

# DD Form 254 — Contract Security Classification Specification

Drafts a complete DD Form 254 establishing security classification requirements and safeguarding procedures for classified government contracts.

## Prerequisites

1. **Prime contract award document** — full contract number including modification suffixes
2. **Contractor SAM registration** — legal business name, CAGE code, facility address (building/suite)
3. **Subcontractor details** (if applicable) — legal name, CAGE code, facility address, scope of classified work
4. **Statement of work / specifications** — to determine highest classification level required
5. **Applicable Security Classification Guides (SCGs)** — guide numbers, titles, issuing authority, dates
6. **Government certifying official info** — name, title, org designation, office symbol, phone, email
7. **Contractor FSO info** — name, title, phone, email

## Output Structure

Draft the DD Form 254 following the official DCSA block structure. Each section below corresponds to the form's required content areas.

### 1. Contract & Entity Identification

| Field | Requirement |
|---|---|
| Prime contract number | Exact alphanumeric match to award document (include all dashes, mod suffixes) |
| Prime contractor name | Legal name per SAM registration — no DBAs or abbreviations |
| Facility address | Physical location of classified work, including building/suite numbers; must match DCSA facility clearance records |
| CAGE code | Links contract to facility security clearance |
| Subcontractors | For each: legal name, CAGE code, address, relationship to prime, scope of classified work, whether separate DD 254 required |

### 2. Security Classification Determinations

Analyze all contract requirements to determine the highest classification level (Confidential / Secret / Top Secret) for both government-furnished and contractor-generated information.

**Classification narrative must specify:**
- Categories of classified information (technical data, intel, COMSEC, weapons specs, crypto, etc.)
- Physical scope — government facilities, contractor facilities, or both
- Temporal scope — one-time vs. ongoing access
- Special access categories (identify each explicitly):

| Category | Additional Requirements |
|---|---|
| SAP | Program-specific briefings, indoctrination |
| SCI | SSBI/Tier 5 investigation, SCI access approval |
| RD / FRD | DOE classification guides |
| NATO / Foreign Government | Classification level equivalencies, separate specification |

- Reference each applicable SCG by number, title, issuing authority, and date

### 3. Safeguarding & Handling Protocols

**Storage:**
- Specify GSA-approved container class (Class 5 / Class 6) per classification level
- Identify secure room / vault requirements
- SCIF requirements for SCI

**Transmission & Transport:**

| Method | When Authorized | Requirements |
|---|---|---|
| Electronic (encrypted) | Approved systems only | Specify system/encryption standard |
| Hand-carry | Between cleared facilities | Chain-of-custody documentation |
| Defense Courier Service | TS or higher / special categories | DCS procedures |
| Authorized courier | As specified | Packaging, marking, receipting |

**Destruction:**
- Approved methods per classification level and media type
- Witnessed destruction requirements
- Destruction certificates and recordkeeping

**Physical Security Infrastructure:**
- Intrusion detection systems (IDS)
- Access control systems
- Security-in-depth measures

**Derivative Classification (if contractor generates classified info):**
- Classification authority designation
- Applicable SCGs
- Portion marking requirements: (U), (C), (S), (TS)
- Overall document marking
- Declassification instructions

### 4. Personnel Security Clearance Requirements

| Element | Detail |
|---|---|
| Clearance levels needed | Breakdown by position: Confidential / Secret / Top Secret |
| Additional access | SCI, SAP, or other specialized access requirements |
| Estimated headcount | By clearance level and access type |
| Citizenship requirements | U.S. citizen / LPR / Limited Access Authorization (LAA) eligibility |
| Interim clearances | Conditions for interim Secret or TS; access limitations while interim |
| Pre-access requirements | NDAs, security briefings, specialized training |
| Enhanced screening | CI-scope polygraph or enhanced screening if applicable |

### 5. Certification & Acknowledgment

**Government Certifying Official Block:**
- Full name, title, org designation, office symbol, phone, email
- Certification statement: official has reviewed contract requirements, determined classification levels, identified all categories of classified information, and verified accuracy of specifications
- Signature and date lines

**Contractor Acknowledgment Block:**
- FSO or designated representative: full name, title, FSO designation, phone, email
- Acknowledgment statement: contractor has received DD Form 254, understands requirements, and commits to implementing all safeguarding measures
- Signature and date lines

### 6. Document Markings

Apply to the DD Form 254 itself:
- Overall classification marking = highest level discussed in the document
- Portion markings on each section: (U), (C), (S), (TS)
- Classification authority block
- Declassification instructions
- Dissemination controls (NOFORN, etc.) as applicable

## Guidelines

- **Exact match required** — contract numbers, CAGE codes, and legal names must be character-perfect; discrepancies cause clearance processing delays
- **No ambiguity** — every requirement must be actionable by contractor FSO without clarification
- **Traceability** — every security requirement must trace to NISPOM, DCSA directives, DoD instructions, or IC directives; cite specific chapters/sections
- **Subcontractor flow-down** — determine whether each sub needs its own DD 254 or operates under the prime's security umbrella based on scope of classified access
- **SCG currency** — verify all referenced Security Classification Guides are current editions
- **NISPOM compliance** — 32 CFR Part 117 (NISPOM) governs all requirements [VERIFY current CFR citation]
- **Mark [VERIFY] on any SCG number, NISPOM section, or regulatory citation not confirmed against source documents**
