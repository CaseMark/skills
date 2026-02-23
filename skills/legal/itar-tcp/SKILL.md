---
name: itar-tcp
description: Drafts ITAR Technology Control Plans (TCPs) for organizations handling USML defense articles and technical data under 22 CFR Parts 120-130. Covers DDTC registration, classification/inventory, access controls, deemed export prevention, secure handling, training programs, audit frameworks, and incident response with voluntary self-disclosure procedures. Use when creating or updating export control compliance plans, technology control plans, ITAR compliance programs, or DDTC submission documents.
tags:
  - drafting
  - memo
  - regulatory
  - research
---

# ITAR Technology Control Plan (TCP)

Drafts a comprehensive Technology Control Plan serving as the organization's binding compliance framework for managing defense articles, technical data, and defense services under ITAR (22 CFR Parts 120-130), suitable for DDTC submission and internal implementation.

## Prerequisites

1. **DDTC registration status** — current registration, export licenses, or agreements
2. **USML categories** — applicable categories under 22 CFR §121.1 for the organization's controlled items
3. **Defense contracts/programs** — contract numbers, program names, government customers
4. **Empowered official** — identity of designee under 22 CFR §120.25
5. **Facility information** — locations, IT infrastructure, workforce composition (including foreign nationals)
6. **Prior compliance history** — audit findings, violations, voluntary disclosures

## Research Phase

Before drafting, extract from available documents:

| Information | Source |
|---|---|
| DDTC registration & license numbers | Organizational records |
| USML categories & controlled items | Contract SOWs, commodity jurisdiction determinations |
| Facility layouts & controlled areas | Security plans, floor plans |
| Foreign national employees | HR records (triggers deemed export analysis) |
| Existing policies & procedures | Current compliance documentation |
| Prior violations or VSD history | Enforcement records, corrective actions |

## Output Structure

Draft the TCP with these sections in order:

### 1. Executive Summary & Legal Foundation

- State TCP as binding compliance instrument under ITAR
- Cite controlling definitions:
  - **Export**: 22 CFR §120.10 — includes release to foreign persons in the U.S.
  - **Defense article**: 22 CFR §120.17
  - **Technical data**: 22 CFR §120.33 — information for design, development, production, manufacture, assembly, operation, repair, testing, maintenance, or modification of defense articles
- List applicable USML categories with concrete descriptions of controlled items
- State penalties: civil up to $1,184,165/violation (22 CFR §127.1) [VERIFY current amount], criminal imprisonment under AECA, debarment
- Declare universal applicability: employees, contractors, consultants, visitors

### 2. Scope & Jurisdictional Boundaries

Define with specificity:
- [ ] Defense programs, contracts, and product lines (with contract numbers)
- [ ] Physical locations: facilities, labs, offices, storage, remote/field sites
- [ ] Work-from-home and temporary site coverage
- [ ] Personnel categories: routine access, project-specific, contractors, visitors, third-party service providers
- [ ] Collaborative arrangements: teaming agreements, JVs, TAAs, MLAs
- [ ] Exclusions: public domain (22 CFR §120.11), EAR-controlled items, CJ determinations

### 3. Classification & Inventory Management

**Classification process:**
1. Evaluate items against USML category descriptions (22 CFR §121.1)
2. For uncertain items: prepare CJ request to DDTC under 22 CFR §120.4
3. Apply interim controls pending CJ determination
4. Assign qualified personnel for classification decisions with review process

**Inventory must track:**

| Item Type | Required Details |
|---|---|
| Hardware | Components, assemblies, USML classification |
| Technical documents | Drawings, specs, design files — with version control |
| Software/source code | Specially designed for defense applications |
| Manufacturing processes | Proprietary techniques, tooling |
| Test data | Performance specs, operational parameters |

**Marking requirement:** All controlled items must bear:
> "ITAR CONTROLLED — Export of this information to foreign persons is prohibited without prior approval from the U.S. Department of State."

### 4. Access Controls & U.S. Person Verification

**U.S. Person definition (22 CFR §120.62):**
- U.S. citizens
- Lawful permanent residents (Form I-551)
- Persons granted asylum, refugee status, or TPS
- Excludes all other foreign nationals regardless of visa or work authorization

**Verification:** Examine original documentation (passport, green card) before granting access.

**Physical controls:**
- Electronic badge systems restricting controlled areas to verified U.S. persons
- Locked storage with authorized-personnel-only access
- Visitor protocols: advance approval, escort, area sanitization before foreign national visits
- Clean desk policy for controlled materials

**Cybersecurity controls:**
- Network segmentation isolating ITAR systems
- Multi-factor authentication
- FIPS-compliant encryption for data at rest and in transit
- Prohibit personal devices, removable media, consumer cloud storage

**Deemed export prevention (22 CFR §120.54):**
- Release of controlled data to a foreign person in the U.S. = export to their country of nationality
- Sanitize workspaces, cover/remove materials, restrict discussions when foreign persons present
- Any necessary disclosure to foreign persons requires prior authorization (TAA under 22 CFR §124, DSP-5, or other DDTC approval)

### 5. Secure Handling, Storage & Transmission

**Physical materials:** Locked cabinets/cages in controlled areas, alarmed rooms for sensitive items, check-in/check-out inventory system.

**Electronic data:**
- AES-256 encryption (or equivalent) for all controlled data
- Prohibit transmission via standard commercial email
- Use approved secure file transfer with end-to-end encryption
- Verify recipient U.S. person status and need-to-know before any transmission

**Records retention:** 5 years per 22 CFR §122.5.

**Destruction:** Shredding, degaussing, or approved sanitization methods.

**International travel:**
- DSP-73 temporary export license required before traveling with controlled materials
- ATA Carnets for temporary export of defense articles
- No remote access from foreign countries without specific authorization
- VPN with strong encryption required for all remote access

### 6. Training Program

**Initial training** — required before any access to controlled materials.
**Refresher** — annually at minimum.

**Core curriculum:**

| Topic | Audience |
|---|---|
| ITAR fundamentals & organizational applicability | All personnel |
| Defense article/technical data identification | All personnel |
| Deemed export rules & foreign person restrictions | All personnel |
| TCP requirements & individual responsibilities | All personnel |
| Violation consequences (civil/criminal) | All personnel |
| Reporting procedures | All personnel |

**Role-specific training:**

| Role | Additional Training |
|---|---|
| Empowered official | 22 CFR §120.25 duties |
| Export compliance officers | Licensing procedures, regulatory interpretation |
| Security personnel | Access control implementation, incident response |
| Engineering/technical staff | Technical data controls, deemed export prevention |
| HR personnel | Foreign national screening, eligibility verification |
| IT staff | Cybersecurity for controlled networks |
| Shipping/receiving | Export documentation, restricted party screening |

**Documentation required:** Attendance records, signed acknowledgments, competency assessments, materials with version control.

### 7. Monitoring & Audit Framework

**Annual audit scope:**
- [ ] Access control systems and logs
- [ ] Training records and personnel screening
- [ ] Export authorizations and licensing compliance
- [ ] Technical data transfer and disclosure records
- [ ] Foreign visitor logs and escort procedures
- [ ] IT security controls and system configurations

**Triggered audits:** Organizational changes, new programs/USML categories, incidents/near-misses, regulatory changes.

**Audit methodology:** Log review, records examination, export documentation validation, physical/electronic storage inspection, personnel interviews.

**KPIs:**
- Incident count and severity trends
- Audit finding closure timeliness
- Training completion rates and scores
- U.S. person verification currency percentage
- License application/renewal timeliness

### 8. Incident Response & Violation Management

**Reportable incidents:**
- Unauthorized foreign person access to controlled areas/information
- Inadvertent exports or deemed exports without authorization
- Missing or unaccounted controlled items/data
- Cybersecurity breaches affecting ITAR systems
- Unmarked controlled data found in unrestricted areas

**Response sequence:**
1. **Contain** — revoke access, secure materials, isolate systems
2. **Preserve evidence** — access logs, communications, witness statements; maintain chain of custody
3. **Assess scope** — what data/articles, USML categories, who accessed, nationality, duration
4. **Report internally** — empowered official, compliance officer, legal counsel, senior management
5. **Voluntary self-disclosure** — consider 22 CFR §127.12 notification to DDTC Office of Defense Trade Controls Compliance for mitigation credit
6. **Root cause analysis** — procedure gaps, training deficiency, human error, systemic failure
7. **Corrective action** — address deficiencies, update TCP, revise training

VSD should be coordinated between empowered official and legal counsel; submit promptly to maximize mitigation.

### 9. Governance & Continuous Improvement

- **Oversight:** Empowered official (22 CFR §120.25), day-to-day by export compliance officer
- **Annual review** encompassing: regulatory changes, USML amendments, incident trends, audit findings, organizational changes, personnel feedback
- **Interim review triggers:** New programs/USML categories, restructuring/M&A, key personnel changes, new IT systems, government audit findings
- **Version control:** All revisions documented, approved by senior management and empowered official, communicated to affected personnel
- **Records:** Maintain all TCP versions, approval dates, distribution lists, review documentation

### 10. Document Format Requirements

- Table of contents with numbered sections/subsections
- Appendices: forms, checklists, reference guides
- Signature blocks: empowered official, CEO/senior executive
- Effective date and distribution/acknowledgment process
- Professional formatting with regulatory citations
- Flag any information gaps with placeholder language and recommendations for obtaining missing data

## Guidelines

- All regulatory citations must be verified against current CFR — mark uncertain citations with [VERIFY]
- Tailor to the organization's specific USML categories, programs, and facility configurations — avoid generic boilerplate
- Penalty amounts change; verify current civil penalty maximums under 22 CFR §127.1
- The TCP must be suitable for DDTC submission, senior management review, and operational implementation simultaneously
- Coordinate with legal counsel on privilege protections during incident investigations
- Address both physical and electronic controls — modern TCPs must robustly cover cybersecurity
- Foreign national workforce composition drives the scope of deemed export controls; assess thoroughly
