---
name: managing-health-data-exchange
language: en
description: Structures health information exchange with HL7 FHIR, C-CDA, and interoperability requirements. Use when managing data exchange, implementing FHIR APIs, or ensuring interoperability.
tags:
  - management
  - health-informatics
metadata:
  author: casemark
  practice_areas:
    - Health Informatics
    - Health IT
    - Clinical Informatics
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Health Data Exchange

Structures health information exchange using HL7 FHIR R4, C-CDA, and legacy HL7 v2 messaging to meet Cures Act interoperability mandates. This skill covers technical implementation, participant onboarding, TEFCA alignment, and operational monitoring of data exchange channels.

## Why This Skill Exists

The 21st Century Cures Act and ONC's information blocking rules (45 CFR Part 171) require that health IT systems exchange electronic health information without unreasonable barriers. Organizations face regulatory penalties, reputational risk, and clinical quality gaps when data exchange fails. Simultaneously, the transition from point-to-point HL7 v2 interfaces to RESTful FHIR APIs and TEFCA-based nationwide exchange introduces architectural complexity that requires disciplined management.


The transition from legacy point-to-point HL7 v2 interfaces to modern FHIR-based APIs and TEFCA-mediated nationwide exchange represents the most significant architectural shift in health IT interoperability since the adoption of HL7 v2 in the 1990s. Organizations must manage this transition while maintaining operational continuity for existing interfaces and meeting evolving regulatory timelines.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Exchange use case** --- What clinical or operational need drives this exchange? (Care transitions, referral management, public health reporting, payer data exchange, patient access)
2. **Participants** --- Which organizations or systems are involved? List sending and receiving parties with their EHR/HIS platform and version
3. **Data scope** --- What USCDI data classes and elements are required? Reference USCDI v4 categories explicitly
4. **Exchange pattern** --- Push (sender-initiated), pull (query-response), or subscription (event-driven)? Batch or real-time?
5. **Standards in use** --- HL7 v2 (specify message types: ADT, ORM, ORU, MDM), C-CDA (specify document types: CCD, Referral Note, Discharge Summary), FHIR R4 (specify resources and operations)
6. **TEFCA participation** --- Is either party a TEFCA Qualified Health Information Network (QHIN) participant? Which TEFCA exchange purpose applies?
7. **Regulatory obligations** --- Promoting Interoperability, information blocking compliance, state consent management requirements

### Required Documents

- Interface specification or implementation guide (HL7 v2 conformance profile, C-CDA template constraints, FHIR IG)
- Network connectivity requirements (VPN, TLS mutual auth, DIRECT messaging)
- USCDI v4 data element checklist for the exchange scope
- Data use agreement (DUA) or business associate agreement (BAA) between parties
- Patient consent policy documentation (especially for behavioral health, substance use, HIV data under 42 CFR Part 2)

---

## Step 1 --- Assess Current Exchange Architecture

Map the existing data exchange landscape:

- **Interface inventory** --- Document every active interface: source system, destination system, message type, transport protocol, message volume (daily average), and error rate
- **Standards gap analysis** --- Identify where legacy HL7 v2 interfaces could be migrated to FHIR R4. Prioritize by: (a) regulatory requirement (patient access APIs must be FHIR), (b) maintenance burden, (c) data quality issues
- **Connectivity topology** --- Map hub-and-spoke vs. point-to-point vs. HIE-mediated connections. Identify single points of failure
- **FHIR endpoint catalog** --- Inventory existing FHIR servers, their capability statements, supported resources, and authentication methods

- **TEFCA readiness assessment** --- Evaluate organizational readiness for TEFCA participation: identity proofing infrastructure, master patient index capabilities, FHIR endpoint maturity, consent management for sensitive data categories, and operational capacity to respond to TEFCA queries from external QHINs
---

## Step 2 --- Design the Exchange Specification

For each exchange channel, produce a technical specification:

- **FHIR implementation** --- Define the FHIR resources required (Patient, Condition, MedicationRequest, Observation, DocumentReference, Encounter), required vs. optional elements, search parameters, and _include/_revinclude chains
- **C-CDA document exchange** --- Specify template conformance (C-CDA R2.1 with USCDI companion guide extensions), required sections (Allergies, Medications, Problems, Results, Procedures), and null-flavor handling rules
- **HL7 v2 messaging** --- Define segment-level specifications: MSH (sending/receiving facility, message type, version), PID (patient identifiers, MRN crosswalk), OBX (result segments with LOINC codes and units)
- **Patient matching** --- Specify the matching algorithm: deterministic (MRN, SSN last-4 + DOB + name) or probabilistic (weighted scoring). Define match threshold, possible-match threshold, and no-match handling
- **Consent enforcement** --- For sensitive data categories (42 CFR Part 2 substance use, state behavioral health laws), define the consent-checking mechanism: pre-exchange consent query, consent directive in the payload, or consent management service

- **Bulk FHIR export** --- For large-scale data exchange (payer access, research, public health), implement FHIR Bulk Data Access (Flat FHIR) per the SMART Backend Services specification. Define access controls, rate limiting, and audit logging for bulk export operations
---

## Step 3 --- Implement Security and Trust

Data exchange requires layered security:

- **Transport security** --- TLS 1.2 minimum for all connections. Mutual TLS (mTLS) for FHIR server-to-server communication. DIRECT messaging for secure email-based exchange
- **Authentication and authorization** --- SMART on FHIR OAuth 2.0 for patient-facing and EHR-launch apps. SMART Backend Services (client_credentials grant with signed JWT assertions) for system-to-system exchange
- **Identity proofing** --- Validate participant organization identity through TEFCA QHIN credentialing, DirectTrust accreditation, or manual verification
- **Audit logging** --- Log every exchange event: timestamp, sender, recipient, patient identifier, data elements exchanged, success/failure, and user identity. Retain logs per HIPAA requirements (minimum 6 years)
- **Breach notification readiness** --- Define the escalation path if exchanged PHI is exposed. Integrate with the organization's HIPAA breach notification process

---

## Step 4 --- Onboard Exchange Partners

Structured partner onboarding prevents production failures:

1. **Legal/compliance review** --- Execute DUA/BAA. Confirm both parties' information blocking compliance posture
2. **Technical connectivity** --- Establish network connectivity (VPN tunnels, firewall rules, certificate exchange)
3. **Testing progression** --- Connectivity test (can systems reach each other), message validation test (do messages parse correctly), clinical scenario test (do realistic clinical scenarios produce correct data), volume test (peak-load simulation)
4. **Go-live criteria** --- Define message acceptance rate threshold (> 99.5%), maximum acceptable latency, and error handling procedures before activating production exchange
5. **Monitoring handoff** --- Establish ongoing monitoring responsibilities and escalation contacts for both parties

- **Consent management architecture** --- For organizations exchanging sensitive data (42 CFR Part 2 substance use, state behavioral health, HIV, genetic data), implement a consent management service that: stores granular patient consent directives, evaluates consent at query time, enforces consent restrictions in real-time, and logs all consent-based access decisions for audit
---

## Step 5 --- Monitor and Optimize

Ongoing operational management:

- **Dashboard metrics** --- Message volume (hourly, daily, weekly trends), error rate by error type (parse failure, patient match failure, timeout, authentication failure), latency (p50, p95, p99), and queue depth
- **Error triage protocol** --- Categorize errors: (a) transient (retry automatically), (b) data quality (requires source system fix), (c) configuration (requires interface team action), (d) systemic (requires architecture change)
- **FHIR API performance** --- Monitor FHIR server response times, concurrent connection counts, and resource utilization. FHIR queries returning > 200 resources should use pagination
- **Reconciliation** --- Weekly automated reconciliation of sent vs. received message counts between partners. Investigate discrepancies > 0.1%
- **Standards version management** --- Track upcoming HL7 ballot cycles, FHIR version updates (R4 to R4B to R5), and USCDI version changes that affect exchange content requirements

- **Migration planning (v2 to FHIR)** --- For legacy HL7 v2 interfaces targeted for FHIR migration, develop a phased migration plan: inventory current v2 interfaces by message type and criticality, map v2 segments to equivalent FHIR resources, implement dual-stack (v2 and FHIR in parallel) during transition, validate FHIR output against v2 baseline, and decommission v2 only after successful FHIR validation
---

## Checkpoint B --- Exchange Operations Review

Before declaring the exchange channel production-ready:

- [ ] Technical specification is complete and approved by both parties
- [ ] All testing stages are passed with documented evidence
- [ ] Patient matching accuracy meets organizational threshold
- [ ] Consent management is validated for sensitive data categories
- [ ] Security controls (TLS, OAuth, audit logging) are verified
- [ ] Monitoring dashboards are operational with alerting configured
- [ ] Error handling and escalation procedures are documented
- [ ] DUA/BAA is executed and on file

- [ ] TEFCA readiness assessment is completed with gap remediation plan
- [ ] Consent management is validated for all sensitive data categories in the exchange
- [ ] Migration plan from v2 to FHIR is documented for legacy interfaces
---

## Quality Audit

- [ ] USCDI v4 data elements required for the use case are confirmed in the exchange payload
- [ ] FHIR resources validate against the applicable implementation guide (US Core, Da Vinci, CARIN)
- [ ] C-CDA documents pass validation against C-CDA R2.1 schema and Schematron rules
- [ ] Information blocking exceptions (45 CFR Part 171) are documented if any data is excluded from exchange
- [ ] Patient matching false-positive and false-negative rates are measured and within tolerance
- [ ] Transport security meets HIPAA technical safeguard requirements
- [ ] Audit logs capture all required exchange metadata
- [ ] Exchange volume meets or exceeds projected clinical workflow demand
- [ ] Partner onboarding documentation is archived for compliance audit

- [ ] FHIR Bulk Data Access is configured with appropriate access controls and rate limiting
- [ ] Consent management service enforces patient consent directives for sensitive data categories
- [ ] v2-to-FHIR migration plan includes dual-stack validation and rollback capability
- [ ] TEFCA Common Agreement technical requirements are mapped against organizational capabilities
---

## Guidelines

- Treat information blocking compliance as a default posture: exchange all EHI unless a specific Cures Act exception (privacy, security, infeasibility, health IT performance, content/manner, fees, licensing) applies and is documented
- Use US Core FHIR profiles as the baseline for all FHIR exchange. Do not invent custom profiles when US Core covers the use case
- For C-CDA, validate every document against the ONC reference validator before sending. Invalid C-CDAs that fail at the receiving system create clinical gaps
- Never rely solely on MRN for patient matching across organizations. MRNs are facility-specific and collide across systems
- Monitor HL7 v2 interface engines (Rhapsody, Mirth Connect, Cloverleaf) for message queue buildup. A growing queue is an early warning of downstream system issues
- When onboarding TEFCA exchange, follow the Common Agreement technical requirements for QHIN-to-QHIN query and message delivery
- Design for failure: every exchange channel needs a documented degradation mode (store-and-forward, manual fax fallback) for when electronic exchange is unavailable
- Re-assess exchange architecture annually against evolving USCDI versions and ONC rulemaking

- FHIR is the future standard but HL7 v2 is the present reality. Plan for 5-10 years of coexistence. Migration must be incremental and risk-managed, not a big-bang replacement
- Consent management for sensitive data is the hardest interoperability problem in healthcare. Technical solutions exist but organizational policy, patient communication, and legal compliance must be aligned before implementation