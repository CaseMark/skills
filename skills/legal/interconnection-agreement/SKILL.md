---
name: interconnection-agreement
description: >-
  Drafts U.S. telecommunications Interconnection Agreements (ICAs) compliant
  with the Communications Act, FCC rules, and state commission requirements,
  covering POIs, technical specs, traffic classification, reciprocal
  compensation, access charges, LNP, E911, billing, and dispute resolution.
  Use when drafting or revising an interconnection agreement, ICA, Section
  251/252 negotiation, POI/transport terms, ILEC/CLEC arrangements, VoIP
  interconnection, SS7/SIP signaling, or telecom regulatory filings. Trigger
  keywords: interconnection agreement, ICA, Section 251, Section 252, FCC,
  ILEC, CLEC, POI, reciprocal compensation, access charges, LNP, E911, SS7,
  SIP, ATIS.
tags:
  - agreement
  - drafting
  - regulatory
---

# Interconnection Agreement

Draft a complete ICA suitable for execution and (if required) state PUC filing.

## Prerequisites

1. **Party identities and authorizations**
Legal name, entity type, state of organization, principal address, FCC FRN, state certificates/licensure, carrier classification (ILEC/CLEC/CMRS/VoIP/other).
2. **Interconnection scope**
Geographic scope, traffic types, desired POIs, interconnection method (direct/indirect), anticipated volumes.
3. **Technical inputs**
Network diagrams, switch locations, interface standards, signaling method (SS7/SIP), LNP/CNAM/E911 requirements.
4. **Commercial inputs**
Rate elements, billing format, payment terms, existing tariffs or commission orders.
5. **Regulatory posture**
Section 252 status, filing jurisdiction(s), any prior ICA or arbitration history.

## Output Structure / Process

**Agreement Skeleton**

| Section | Required Content |
| --- | --- |
| Title + Effective Date | “Interconnection Agreement” and execution/approval effective date clause. |
| Parties + Recitals | Full legal names, carrier types, FRNs, statutory basis (47 U.S.C. § 251/252) [VERIFY]. |
| Definitions | See Definitions Table. |
| Interconnection | POI details, transport/trunking, technical specs, signaling, testing. |
| Traffic Classification | Local, intraLATA, interLATA, wireless, VoIP definitions and billing treatment. |
| Numbering + Databases | LNP procedures, CNAM, routing, NPAC access. |
| E911 | PSAP routing, ANI/ALI responsibilities, priority handling. |
| Performance | KPIs (ASR/NER/PND), thresholds, remediation. |
| Rates + Billing | Rate tables, invoices, records, audits, disputes. |
| Term + Termination | Initial term, renewal, termination for cause/convenience, transition. |
| Dispute Resolution | Tiered process and regulatory vs commercial paths. |
| Regulatory Compliance | FCC/state law, filing/approval mechanics, change-in-law. |
| Standard Terms | Confidentiality, indemnity, limitation of liability, force majeure, notices, assignment. |
| Signatures | Authorized signatories, optional notary, e-signatures. |

**Definitions Table (populate precisely)**

| Term | Definition Requirements |
| --- | --- |
| Point of Interconnection (POI) | Physical address and logical demarcation, meet-point vs end office vs tandem, interface standard (DS-1/DS-3/OC-x/Ethernet). |
| Local Traffic | Origination/termination within local calling area; cite tariff/PUC designation. |
| IntraLATA Toll | Within LATA, outside local calling area. |
| InterLATA | Crosses LATA boundary. |
| Wireless Traffic | CMRS-originated/terminated; treatment basis and classification method. |
| VoIP Traffic | IP-enabled voice; jurisdictional treatment and interim compensation. |
| UNEs / Interconnection Facilities | Distinguish Section 251(c)(3) vs 251(c)(2) [VERIFY]. |
| Transport / Tandem Switching / End Office | Technical definitions tied to network topology. |
| Busy Hour / CCS / MOU / PIU/PLU | Measurement and apportionment terms. |
| Reciprocal Compensation | Section 251(b)(5) obligation [VERIFY]. |

**Technical Specifications Checklist**

- [ ] POI inventory: address, floor/bay/cage, equipment IDs.
- [ ] Trunking: one-way/two-way, initial capacity, augmentation thresholds.
- [ ] Signaling: SS7 point codes or SIP profile + headers.
- [ ] Testing: ATIS/TIA protocols, acceptance criteria.
- [ ] Forecasts: cadence and format for traffic projections.
- [ ] Performance reporting: ASR/NER/PND metrics and remedies.

**Rate and Billing Tables**

**A. Reciprocal Compensation**

| Traffic Type | Rate | Symmetric/Asymmetric | Jurisdictional Basis |
| --- | --- | --- | --- |

**B. Transport / Tandem / Entrance Facilities**

| Element | NRC | MRC | Order Interval | Notes |
| --- | --- | --- | --- | --- |

**C. Access Charges**

| Traffic Type | Tariff/Rate Reference | Conditions |
| --- | --- | --- |

**Billing Workflow**

1. Invoice timing and format (EMR/EDI/CSV).
2. Records retention duration and audit rights.
3. Dispute window, notice requirements, and payment of undisputed amounts.

**Dispute Resolution Ladder**

| Stage | Timeframe | Scope |
| --- | --- | --- |
| Operational Negotiation | X business days | Technical/billing issues. |
| Executive Escalation | X days | Unresolved operational disputes. |
| Mediation | X days | Non-binding commercial disputes. |
| Regulatory Complaint | As needed | Section 251/252 compliance, rates, traffic classification. |
| Arbitration | Final step | Purely commercial contract disputes. |

**Regulatory Filing Clause**

- Filing deadline after execution: [VERIFY].
- Effective date: execution vs PUC approval vs filing.
- If PUC rejects a provision, amendment process and interim performance.

## Guidelines

- Do not invent rates, POIs, FRNs, or regulatory approvals; use placeholders if missing.
- Tie traffic classification to specific jurisdictional rules and tariffs; flag VoIP treatment uncertainty.
- Use defined terms consistently and ensure cross-references are accurate.
- Cite federal framework: Communications Act §§ 251-252 and FCC rules in 47 C.F.R. Part 51 [VERIFY].
- Include “continue to perform” during disputes to avoid service disruption.
- If state-specific PUC rules are known, add a jurisdiction addendum; otherwise include a state-law non-preemption clause.
- Add exhibits for POIs, technical specs, and rate tables when the agreement exceeds 10 pages.
