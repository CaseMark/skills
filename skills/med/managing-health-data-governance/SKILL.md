---
name: managing-health-data-governance
language: en
description: Structures health data governance programs with stewardship roles, policies, and data quality standards. Use when establishing data governance, defining data stewardship, or managing data policies.
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

# Managing Health Data Governance

Structures health data governance programs with stewardship roles, data classification policies, lifecycle management, and quality standards. This skill covers governance framework design, policy creation, stewardship role definition, and operational monitoring for health data assets across EHR, claims, research, and analytics environments.

## Why This Skill Exists

Health data governance is the organizational framework that ensures data is accurate, secure, available, and used appropriately. Without governance, organizations face: inconsistent data definitions across departments (one team's "active patient" differs from another's), uncontrolled data proliferation (PHI in unsecured spreadsheets), regulatory non-compliance (HIPAA, Cures Act, state privacy laws), unreliable analytics (decisions based on conflicting data sources), and inability to respond to data requests (no one knows where data lives or who owns it). Governance provides the policies, roles, and processes that make data a managed organizational asset rather than an uncontrolled liability.


Healthcare data governance has become more urgent with the proliferation of data uses beyond clinical care: AI/ML model training, population health analytics, research data sharing, payer data exchange, and patient-generated health data. Each new data use introduces governance requirements that must be addressed within a coherent framework rather than ad hoc.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Governance scope** --- Which data domains are in scope? (Clinical EHR data, claims/financial data, research data, operational data, patient-generated data, genomic data)
2. **Organizational structure** --- What governance bodies exist? (Data governance council, clinical informatics committee, privacy/compliance committee, research data committee)
3. **Regulatory drivers** --- Which regulations require data governance? (HIPAA Privacy/Security Rules, 42 CFR Part 2, Cures Act information blocking, state privacy laws, GDPR for international operations, Common Rule for research)
4. **Current state** --- Is there an existing governance program, or is this a new initiative? What policies exist today?
5. **Pain points** --- What data problems are driving governance investment? (Data quality issues, audit findings, security incidents, analytics inconsistencies, regulatory non-compliance)
6. **Technology landscape** --- What systems hold governed data? (EHR, data warehouse, analytics platforms, research databases, HIE connections, cloud storage)
7. **Executive sponsorship** --- Who is the executive sponsor? Governance without executive authority fails

### Required Documents

- Organizational data system inventory (all systems containing patient/health data)
- Current data-related policies (data access, data retention, data sharing, acceptable use)
- Regulatory compliance assessment (HIPAA risk assessment, ONC certification documentation)
- Previous audit findings related to data management
- Organizational chart for IT, compliance, clinical informatics, and research functions
- Data breach/incident history (last 3 years)

---

## Step 1 --- Establish the Governance Framework

Define the structure that will sustain governance:

- **Governance council charter** --- Define the council's authority, scope, membership, meeting cadence, and decision-making process. Include: CMIO or CNIO (clinical authority), CIO/CISO (technology authority), Privacy Officer (compliance authority), CFO representative (financial data), Research Director (research data)
- **Decision rights matrix** --- For each data domain, define who can: create data definitions, approve data access, authorize data sharing, retire data assets, approve exceptions to policies. Use a RACI matrix (Responsible, Accountable, Consulted, Informed)
- **Data stewardship roles** --- Assign data stewards for each domain: clinical data steward (typically clinical informaticist), financial data steward, research data steward, operational data steward. Stewards are accountable for data quality and policy compliance within their domain
- **Policy hierarchy** --- Define the relationship between enterprise policies, domain-specific standards, and operational procedures. Enterprise policy: "All PHI must be encrypted at rest." Domain standard: "EHR database encryption uses AES-256." Operational procedure: "DBA enables TDE on all production databases"

- **AI/ML data governance** --- Define governance policies specifically for AI/ML data use: training data curation standards, de-identification requirements for model development, bias assessment requirements for training datasets, data provenance tracking, and governance review for datasets used in AI development or validation
---

## Step 2 --- Classify Data Assets

Build a data asset inventory with classification:

- **Data catalog** --- Inventory all data assets: system name, data owner, data steward, data classification level, retention period, backup frequency, access control mechanism. Include both structured (databases, data warehouses) and unstructured (clinical documents, scanned records, images)
- **Classification scheme** --- Apply a multi-tier classification: (1) Restricted (PHI, PII, substance use records under 42 CFR Part 2, genetic data), (2) Confidential (business-sensitive data, financial data, personnel data), (3) Internal (general operational data), (4) Public (published quality data, directory information)
- **PHI inventory** --- Specifically identify all locations where PHI resides: production EHR, data warehouse, analytics platforms, reporting tools, research databases, backup systems, test environments, user workstations, mobile devices, cloud services, third-party systems
- **Data lineage** --- For critical data elements (patient identity, diagnosis codes, medication lists, financial balances), document the lineage: source of creation, transformation steps, systems of record, downstream consumers
- **Minimum necessary mapping** --- For each data consumer (department, role, application), document which data elements are accessed and validate that access is limited to the minimum necessary per HIPAA

---

## Step 3 --- Develop Core Policies

Write the governance policies that operationalize the framework:

- **Data access policy** --- Define role-based access control principles, access request and approval workflow, access review cadence (minimum annual per HIPAA), and break-the-glass procedures for emergency access
- **Data quality policy** --- Define quality dimensions (completeness, accuracy, consistency, timeliness), measurement methodology, acceptable thresholds by data classification, and remediation escalation procedures
- **Data retention and disposal** --- Define retention periods by data type aligned with regulatory requirements: medical records (state-specific, typically 7-10 years adult, 7 years past age of majority for minors), billing records (7 years per IRS), research data (per IRB/funding agency requirements). Define secure disposal methods
- **Data sharing and use agreements** --- Standardize templates for BAAs, DUAs, and data sharing agreements. Define approval workflow for external data sharing including legal, compliance, and governance council review
- **Master data management** --- Establish golden record policies for key entities: patient identity (MPI governance), provider identity (NPI-based), location/facility, payer/plan. Define merge/unmerge procedures for duplicate records

- **Consent management policy** --- Define organizational policy for patient consent related to data use: clinical care (implied consent), quality improvement (authorized without individual consent per 45 CFR 164.506), research (IRB-approved consent or waiver per Common Rule), commercial/secondary use (requires explicit patient authorization under HIPAA), and AI/ML training (policy-dependent, evolving regulatory landscape)
---

## Step 4 --- Implement Operational Controls

Convert policies into enforceable controls:

- **Access control implementation** --- Configure role-based access in EHR and data warehouse systems aligned with the data access policy. Implement automated access provisioning/deprovisioning tied to HR onboarding/offboarding
- **Audit monitoring** --- Implement automated monitoring for: unusual access patterns (high volume record access, access outside assigned department, access to VIP records), data export to removable media, bulk data downloads, and break-the-glass events
- **Data quality dashboards** --- Deploy automated DQ monitoring for critical data elements: patient demographics completeness, diagnosis code validity, medication list currency, lab result timeliness. Alert data stewards when quality metrics fall below thresholds
- **Policy exception management** --- Establish a formal exception process: request, justification, risk assessment, time-limited approval, documentation, and re-evaluation at expiration
- **Training program** --- Mandatory annual data governance training for all workforce members who access health data. Role-specific training for data stewards, analysts, and IT staff

- **De-identification governance** --- Establish de-identification standards and oversight: approved de-identification methods (Safe Harbor, Expert Determination), re-identification risk assessment procedures, governance review required before releasing de-identified datasets, and monitoring for re-identification attempts or breaches
---

## Step 5 --- Monitor and Mature

Ongoing governance requires continuous improvement:

- **Governance metrics** --- Track: policy compliance rates, data quality trend scores, access review completion rates, policy exception volume and aging, data incident counts, time-to-resolution for data quality issues
- **Maturity assessment** --- Annually assess governance maturity using a recognized framework (CMMI Data Management Maturity Model, Stanford Medicine Data Governance Maturity). Score across dimensions: awareness, formalization, management, optimization
- **Regulatory change management** --- Monitor regulatory changes that affect data governance: new HIPAA guidance, ONC rulemaking, state privacy laws, CMS data sharing requirements. Update policies within 90 days of effective dates
- **Incident review** --- Conduct root cause analysis for every data governance incident (unauthorized access, data quality failure affecting patient care, breach). Feed findings back into policy and control improvements
- **Stakeholder engagement** --- Quarterly governance council meetings with standing agenda: policy compliance report, DQ dashboard review, incident review, new policy proposals, regulatory update

- **Data governance for emerging data types** --- Extend governance to cover: patient-generated health data (wearables, patient-reported outcomes), genomic data (GINA requirements, return of results policies), social determinants of health data (sensitivity, consent, sharing restrictions), and AI-generated data (ambient documentation, clinical predictions, NLP-extracted findings)
---

## Checkpoint B --- Governance Program Review

Before declaring the governance program operational:

- [ ] Governance council charter is approved by executive leadership
- [ ] Decision rights matrix covers all data domains in scope
- [ ] Data stewards are assigned and have accepted accountability
- [ ] Data classification is applied to all inventoried data assets
- [ ] Core policies (access, quality, retention, sharing) are approved and published
- [ ] Operational controls are implemented for access monitoring and DQ measurement
- [ ] Training program is deployed with completion tracking
- [ ] Governance metrics are defined with baseline measurements

- [ ] AI/ML data governance policies are defined and integrated with the governance framework
- [ ] Consent management policy covers all data use categories (clinical, QI, research, commercial, AI)
- [ ] De-identification governance is operational with risk assessment procedures
---

## Quality Audit

- [ ] Governance framework aligns with a recognized standard (DAMA-DMBOK, CMMI DMM)
- [ ] Data classification scheme covers HIPAA PHI, 42 CFR Part 2, and state-specific sensitive data categories
- [ ] Retention policies comply with state medical record retention laws and federal requirements
- [ ] Access control implementation matches the documented access policy
- [ ] Audit monitoring covers HIPAA-required access logging and review
- [ ] Data quality metrics are measured and trended for all critical data elements
- [ ] Policy exception process is documented with time-limited approvals
- [ ] Governance council meeting minutes are archived with decision documentation
- [ ] Annual maturity assessment is completed with improvement plan

- [ ] AI/ML training data governance requirements are documented and enforced
- [ ] Consent management covers emerging data use cases (AI training, commercial use, payer exchange)
- [ ] De-identification methods are validated and re-identification risk is periodically assessed
- [ ] Governance framework extends to emerging data types (patient-generated, genomic, SDOH, AI-generated)
---

## Guidelines

- Governance is a business function, not an IT function. IT implements controls, but clinical and operational leadership must own data definitions, quality standards, and access decisions
- Start with the data domains that have the highest regulatory exposure and the most pressing quality problems. Do not attempt to govern all data simultaneously
- Policy without enforcement is theater. Every policy must have a corresponding control, monitoring mechanism, and consequence for non-compliance
- Data stewards must have sufficient authority and dedicated time for stewardship activities. A steward role assigned to someone with no time allocation will fail
- Master Patient Index governance is the most critical and most neglected governance activity. Duplicate and overlapping patient records corrupt every downstream use of clinical data
- Information blocking rules under the Cures Act create a governance tension: you must share data broadly while also controlling access appropriately. Resolve this by defaulting to sharing with documented exceptions, not defaulting to restriction with requested access
- Governance of de-identified and limited datasets is often overlooked. Re-identification risk exists even for Safe Harbor de-identified data; govern accordingly
- Treat data governance incidents (unauthorized access, quality failures) with the same rigor as patient safety events: report, investigate, remediate, and prevent recurrence

- AI/ML training data is a governance frontier. Organizations that allow AI vendors to train models on their patient data without governance oversight are ceding control over how their patients' information is used. Contractual clarity on data rights, model ownership, and training data governance is essential
- Data governance must evolve from a compliance function to a strategic function. Organizations with mature data governance can unlock data value (research partnerships, analytics, AI development) that organizations with poor governance cannot safely pursue