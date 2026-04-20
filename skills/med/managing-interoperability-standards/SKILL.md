---
name: managing-interoperability-standards
language: en
description: Tracks and implements healthcare interoperability standards (ONC, TEFCA, Information Blocking). Use when ensuring interoperability compliance, implementing TEFCA, or managing information blocking rules.
tags:
  - management
  - health-informatics
  - compliance
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

# Managing Interoperability Standards

Tracks and implements healthcare interoperability standards including ONC Health IT Certification, TEFCA, Cures Act information blocking rules, USCDI, and HL7 FHIR implementation guides. This skill covers regulatory compliance assessment, implementation planning, and ongoing standards monitoring for health IT systems.

## Why This Skill Exists

Healthcare interoperability is mandated by federal law (21st Century Cures Act) and enforced by ONC and HHS-OIG. Organizations that fail to comply face information blocking penalties (up to $1M per violation for health IT developers), loss of CMS incentive payments, and operational isolation from the evolving nationwide health data exchange infrastructure (TEFCA). The standards landscape is complex and evolving: USCDI versions update annually, FHIR implementation guides mature through ballot cycles, TEFCA onboarding requirements expand, and ONC rulemaking introduces new certification criteria. This skill provides a structured approach to tracking, interpreting, and implementing these requirements.


The regulatory velocity is accelerating: USCDI versions update annually with expanding data class requirements, CMS interoperability rules now extend to payers (Prior Authorization Rule, CMS-0057-F), TEFCA is transitioning from pilot to operational nationwide exchange, and HL7 FHIR implementation guides are maturing through ballot cycles at increasing speed. Organizations that do not maintain active standards tracking fall behind compliance requirements.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Organization type** --- Healthcare provider, health IT developer, health information exchange (HIE), payer, public health agency? This determines which interoperability obligations apply
2. **Certified EHR technology** --- Which CEHRT products are in use? CHPL listing IDs and certified versions
3. **Current interoperability posture** --- What FHIR APIs are deployed? What HIEs does the organization participate in? What HL7 v2 interfaces are in production?
4. **TEFCA status** --- Is the organization connected to a TEFCA QHIN? In evaluation? Not yet considering?
5. **Regulatory reporting programs** --- Which CMS programs require interoperability compliance? (Promoting Interoperability, MIPS, Medicare Advantage, Medicaid Managed Care)
6. **Known compliance gaps** --- Are there existing information blocking concerns, ONC certification deficiencies, or interoperability failures?
7. **Upcoming milestones** --- What regulatory deadlines or contract requirements are approaching?

### Required Documents

- ONC CHPL listing for all certified health IT products in use
- Current FHIR endpoint directory registration
- Information blocking compliance self-assessment
- TEFCA participation evaluation or QHIN connection documentation
- USCDI v4 data class implementation inventory
- HL7 FHIR implementation guide compliance matrix

---

## Step 1 --- Map Regulatory Requirements

Build a comprehensive requirements inventory:

- **Cures Act information blocking (45 CFR Part 171)** --- Eight exceptions define when an actor may restrict EHI access without constituting information blocking: Privacy, Security, Infeasibility, Health IT Performance, Content and Manner, Fees, Licensing, and TEFCA Manner. Document which exceptions the organization invokes and the supporting justification for each
- **ONC certification criteria (45 CFR Part 170.315)** --- Map each certified module against the applicable criteria: (a) Data Category (patient demographics, CPOE, CDS), (b) Care Settings, (c) API criteria (g)(10) for patient access, (d) Electronic prescribing, (e) Public health reporting
- **USCDI requirements** --- Inventory USCDI v4 data classes and elements against system capability: which data classes are captured in structured form? Which are available via FHIR API? Which have gaps? Flag new data classes added in v4 (e.g., Health Insurance Information, Facility Information)
- **TEFCA Common Agreement** --- If pursuing TEFCA participation, map organizational capabilities against QHIN technical requirements: identity proofing, record location, query routing, security requirements, and exchange purposes (Treatment, Payment, Healthcare Operations, Public Health, Individual Access, Government Benefits Determination)
- **State-specific requirements** --- Identify state laws that impose additional interoperability obligations or restrictions (state consent management, state HIE participation mandates, state-specific data sharing rules)

- **CMS Payer Interoperability requirements** --- Map compliance with CMS Prior Authorization Rule (CMS-0057-F) requirements: Patient Access API, Provider Access API, Payer-to-Payer data exchange, and Prior Authorization API. These apply to Medicare Advantage, Medicaid, and CHIP managed care plans
---

## Step 2 --- Assess Current Compliance

Evaluate the gap between requirements and current state:

- **FHIR API compliance** --- Test the Patient Access API (g)(10) endpoint: Does it support all USCDI data classes via US Core FHIR R4 profiles? Does it implement SMART on FHIR OAuth 2.0 correctly? Is it registered in the national FHIR endpoint directory?
- **Information blocking self-assessment** --- For each known instance where EHI is not freely available, determine: Is a valid exception invoked? Is the exception applied consistently and not as a pretext? Is the exception documented with the required specificity? Common problem areas: clinical note release delays, data sharing fees, refusal to support third-party app connections
- **C-CDA quality** --- Validate C-CDA documents generated by the system against the ONC C-CDA Scorecard. Score across: completeness (all required sections present), conformance (valid template IDs, correct code systems), content (coded data rather than free text in coded sections), and vocabulary (valid SNOMED CT, LOINC, RxNorm codes)
- **TEFCA readiness** --- If pursuing TEFCA, assess against the QHIN Technical Framework: endpoint connectivity, identity management infrastructure, master patient index capabilities, query/response message handling, and audit trail requirements
- **Public health reporting** --- Verify electronic case reporting (eCR), electronic lab reporting (ELR), syndromic surveillance, and immunization registry reporting capabilities against current requirements

---

## Step 3 --- Build the Implementation Roadmap

Prioritize and schedule compliance activities:

- **Critical compliance gaps** --- Address immediately: active information blocking (e.g., blocking third-party app connections, withholding clinical notes), certification deficiencies that affect CMS program participation, and gaps that create patient safety risks
- **Regulatory deadline alignment** --- Map gaps to enforcement timelines: CMS Promoting Interoperability reporting periods, ONC certification compliance dates, TEFCA onboarding milestones, USCDI version adoption deadlines
- **Technical workstreams** --- Organize implementation by technical domain: FHIR API development/configuration, C-CDA generation improvement, terminology mapping updates, identity management infrastructure, security and consent management
- **Resource requirements** --- Estimate effort for each gap: EHR vendor configuration (low effort, vendor-dependent timeline), interface development (moderate effort), infrastructure build (high effort), policy/process changes (variable effort, high stakeholder coordination)
- **Dependency mapping** --- Identify sequencing dependencies: USCDI data capture must precede FHIR API support for those data elements; identity management must precede TEFCA participation; terminology mapping must precede C-CDA quality improvement

- **Implementation guide compliance matrix** --- For each active FHIR implementation guide, maintain a compliance matrix documenting: IG name and version, required profiles, conformance level for each profile (full, partial, planned), testing status, and known gaps with remediation timeline
---

## Step 4 --- Implement Standards

Execute the implementation work:

- **FHIR API configuration** --- Configure or develop FHIR R4 endpoints supporting US Core profiles for all USCDI data classes. Implement SMART on FHIR authorization (EHR launch, standalone launch, backend services). Register endpoints in the national FHIR endpoint directory
- **USCDI data capture** --- For USCDI data elements not currently captured in structured form, implement structured data capture in clinical workflows: SDOH screening (using LOINC-coded instruments), sexual orientation/gender identity (SOGI data per USCDI v4), health insurance information, clinical tests
- **C-CDA improvement** --- Address C-CDA Scorecard findings: improve code coverage in coded sections, add missing sections, correct vocabulary bindings, ensure template conformance. Target: all C-CDA documents score > 80% on the ONC Scorecard
- **Information blocking remediation** --- For each identified information blocking instance: remove the barrier, document the change, or formally invoke a valid exception with complete justification
- **TEFCA onboarding** --- Execute TEFCA participation through a QHIN: complete the QHIN Application, implement technical connectivity, pass conformance testing, and establish operational procedures for query handling and response

---

## Step 5 --- Monitor and Maintain Compliance

Interoperability compliance is ongoing:

- **Standards tracking** --- Monitor: ONC rulemaking (Federal Register notifications), HL7 ballot cycles (new FHIR IGs and updates), USCDI version releases (annual), TEFCA Common Agreement amendments, and CMS program rule changes
- **FHIR API monitoring** --- Track API usage metrics: request volume, error rates, response times, unique app connections, patient authorization grants/revocations. Monitor for availability SLA compliance
- **C-CDA quality tracking** --- Periodically re-score C-CDA output against the ONC Scorecard. Track trends by document type and generating provider
- **Information blocking incident management** --- Establish a process for identifying and remediating potential information blocking: intake mechanism for complaints, investigation procedure, remediation tracking, and reporting to compliance
- **Annual compliance review** --- Conduct an annual interoperability compliance assessment covering: ONC certification currency, USCDI version adoption, information blocking posture, TEFCA participation status, and public health reporting capabilities

- **Interoperability maturity model** --- Assess organizational maturity using a staged model: Stage 1 (basic HL7 v2 interfaces, C-CDA exchange), Stage 2 (FHIR APIs operational with US Core compliance), Stage 3 (SMART on FHIR app ecosystem, TEFCA participation), Stage 4 (FHIR-native architecture, real-time data exchange, advanced IGs). Use the maturity assessment to prioritize investments
---

## Checkpoint B --- Compliance Review

Before attesting to interoperability compliance:

- [ ] All ONC certification criteria applicable to the organization are met and documented
- [ ] USCDI v4 data classes are supported in structured data capture and FHIR API access
- [ ] Patient Access API (g)(10) is operational with SMART on FHIR authorization
- [ ] Information blocking assessment identifies no unresolved violations
- [ ] C-CDA documents validate against current standards with acceptable quality scores
- [ ] TEFCA participation status is documented (connected, in-progress, or planned with timeline)
- [ ] Public health reporting capabilities meet current requirements
- [ ] Staff responsible for interoperability are trained on current standards

- [ ] CMS payer interoperability requirements are mapped and compliance status documented
- [ ] FHIR implementation guide compliance matrix is current for all active IGs
- [ ] Organizational interoperability maturity has been assessed with improvement roadmap
---

## Quality Audit

- [ ] ONC CHPL certification listings are current for all health IT products
- [ ] FHIR API endpoints are registered in the national directory and are accessible
- [ ] USCDI implementation inventory is current and version-aligned
- [ ] Information blocking exceptions are individually documented with specific justification
- [ ] C-CDA Scorecard results meet organizational quality targets
- [ ] TEFCA readiness assessment is complete (or participation is active)
- [ ] Regulatory monitoring process is operational with defined responsible parties
- [ ] Annual compliance review is scheduled and has executive sponsorship
- [ ] Standards implementation roadmap is maintained with progress tracking

- [ ] CMS payer interoperability rule compliance is tracked with implementation timeline
- [ ] FHIR IG compliance matrix covers all applicable implementation guides with testing evidence
- [ ] Interoperability maturity assessment has been completed within the last 12 months
- [ ] Regulatory change monitoring process captures ONC, CMS, and HL7 developments within 30 days
---

## Guidelines

- Information blocking is the default regulatory concern. Assume that any restriction on EHI access requires formal exception justification unless clearly exempt. "We have always done it this way" is not a valid exception
- USCDI is a floor, not a ceiling. The standard defines minimum required data classes, but organizations should exchange all available EHI per Cures Act requirements
- Test FHIR APIs from the patient and app developer perspective, not just from the EHR administrator perspective. If a patient cannot successfully connect a third-party app and retrieve their data, the implementation is non-compliant regardless of technical correctness
- Track the HL7 FHIR ballot cycle for implementation guides that will become required (US Core version updates, Da Vinci IGs for payer-provider exchange, CARIN for consumer-directed exchange). Early adoption avoids compliance scrambles
- TEFCA participation is becoming a competitive necessity, not just a regulatory option. Organizations not connected through a QHIN will be excluded from nationwide data exchange as TEFCA adoption grows
- State laws create a patchwork of additional requirements. Maintain a state-by-state compliance matrix for consent management, data sharing, and reporting obligations
- Public health reporting (eCR, ELR, syndromic surveillance) is an interoperability obligation that is often managed separately from clinical interoperability. Ensure it is included in the overall interoperability program
- Vendor management is critical: EHR vendors control much of the FHIR API and C-CDA generation capability. Maintain contractual leverage for timely standards updates and configuration support

- Interoperability compliance is now a competitive differentiator, not just a regulatory requirement. Organizations with mature FHIR APIs and TEFCA connectivity can participate in data-driven care models that non-compliant organizations are excluded from
- The CMS Prior Authorization Rule (CMS-0057-F) represents the most significant payer interoperability mandate since HIPAA transactions. Organizations serving Medicare Advantage and Medicaid populations must begin implementation planning immediately