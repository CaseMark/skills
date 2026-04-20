---
name: managing-ehr-implementations
language: en
description: Structures EHR implementation planning with workflow analysis, data migration, and go-live readiness. Use when planning EHR deployments, managing system migrations, or preparing for go-live events.
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

# Managing EHR Implementations

Structures EHR implementation planning with workflow analysis, data migration, and go-live readiness. This skill covers the full lifecycle from vendor selection validation through post-go-live stabilization for certified EHR technology (CEHRT) deployments.

## Why This Skill Exists

EHR implementations are among the highest-risk health IT projects. Failed or poorly managed deployments disrupt clinical workflows, compromise patient safety, trigger ONC certification non-compliance, and can cost organizations $50-200M in total losses. A structured approach covering workflow redesign, data migration integrity, interface validation, and go-live command center operations reduces the risk of deployment failures that directly affect patient care.


EHR implementation failures have well-documented consequences: the 2013 Cedars-Sinai system shutdown due to physician rejection, multiple health systems reporting increased mortality during go-live periods, and organizations spending 2-3x their original budgets on remediation. Success requires treating EHR implementation as a clinical transformation project, not an IT project.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Implementation type** --- New install, system replacement (e.g., Cerner to Epic), module addition, or major version upgrade?
2. **EHR product and version** --- Vendor name, product edition, and ONC certification status (check CHPL listing ID)
3. **Facility scope** --- Number of sites, beds, ambulatory clinics, and departments in scope. Phased or big-bang approach?
4. **Clinical domains** --- Which modules are in scope? (Inpatient, ambulatory, ED, surgery, pharmacy, radiology, lab)
5. **Current state** --- What systems are being replaced? What interfaces exist today? Obtain the current interface inventory
6. **Regulatory drivers** --- Cures Act compliance deadlines, Promoting Interoperability reporting periods, state-specific mandates
7. **Timeline constraints** --- Contractual go-live dates, fiscal year boundaries, seasonal census patterns to avoid
8. **Staffing model** --- Internal team capacity vs. vendor/consultant staffing ratios

### Required Documents

- Vendor statement of work (SOW) and implementation methodology
- Current-state IT system inventory and interface map
- Clinical workflow documentation (top 20 workflows per department)
- Data migration specification and legacy system data dictionary
- ONC Health IT Certification requirements checklist (per 170.315 criteria)
- Organizational change management plan

---

## Step 1 --- Validate Certification and Regulatory Readiness

Before design begins, confirm the EHR meets mandatory requirements:

- Verify the product's ONC CHPL listing covers all required 170.315 certification criteria for your reporting programs (Promoting Interoperability, MIPS)
- Confirm USCDI v4 data class support: Allergies, Assessment/Plan, Care Team, Clinical Notes, Encounter Diagnosis, Immunizations, Laboratory, Medications, Patient Demographics, Problems, Procedures, Vital Signs, Health Insurance, Clinical Tests, Diagnostic Imaging
- Validate FHIR R4 Patient Access API (170.315(g)(10)) compliance for patient-facing apps
- Check information blocking compliance architecture: the system must not prevent, materially discourage, or interfere with EHI access per 45 CFR Part 171

---

## Step 2 --- Conduct Workflow Analysis

For each clinical domain in scope:

1. **Document current state** --- Shadow clinicians through 3-5 representative encounters per workflow. Capture click counts, screen transitions, workarounds, and pain points
2. **Map future state** --- Design target workflows using the EHR's native capabilities. Identify gaps requiring customization vs. workflow adaptation
3. **Identify integration points** --- Where does the workflow depend on external systems (lab instruments, pharmacy dispensing, radiology PACS, blood bank)?
4. **Decision log** --- Record every workflow design decision with rationale, approving clinician, and date. These become the reference for post-go-live optimization
5. **Order set and preference list design** --- Build specialty-specific order sets with clinical content committee review. Validate against current formulary and evidence-based guidelines

6. **Clinical decision support design** --- Map existing CDS rules to the new platform. Prioritize: drug-drug interactions, drug-allergy alerts, evidence-based order sets, and condition-specific best practice alerts. Avoid importing all legacy CDS without review — this is the opportunity to reduce alert fatigue
---

## Step 3 --- Plan Data Migration

Data migration requires its own workstream with dedicated validation:

- **Scope determination** --- Define which data categories migrate: demographics, problem lists, medication lists, allergy lists, historical lab results, documents, appointments, financial balances
- **Mapping specifications** --- Map legacy system fields to EHR target fields. Apply terminology mapping (legacy codes to SNOMED CT, ICD-10-CM, RxNorm) using the mapping-clinical-terminologies skill
- **Extraction and transformation** --- Build ETL pipelines with checksums at every stage. Document transformation rules for data that requires restructuring
- **Validation protocol** --- Define acceptance criteria per data category: 100% match for patient demographics, 99.5% for active medications, 98% for historical results. Run automated row-count and value-distribution comparisons
- **Cutover rehearsal** --- Execute at least two full migration dry runs against production-volume data. Measure elapsed time to confirm the cutover window is achievable

---

## Step 4 --- Interface Build and Testing

Healthcare interfaces are failure-prone and patient-safety-critical:

- **Interface inventory** --- List every inbound and outbound interface with message type (HL7 v2 ADT, ORM, ORU, MDM; FHIR R4 resources), transport (MLLP, SFTP, REST), and sending/receiving system
- **Build sequence** --- Prioritize interfaces by go-live criticality: ADT feeds first, then orders/results, then ancillary
- **Testing stages** --- Unit test (message parse), integration test (end-to-end with partner system), volume test (peak hour simulation), failover test (what happens when the interface engine is down?)
- **Validation criteria** --- Message acceptance rate > 99.9%, no orphaned orders, no duplicate results, correct patient matching on MRN crosswalk
- **HL7 FHIR considerations** --- For systems using SMART on FHIR apps, validate OAuth 2.0 scopes, token lifecycle, and patient-context launch parameters

- **FHIR API readiness** --- Validate FHIR R4 Patient Access API (170.315(g)(10)) functionality before go-live: SMART on FHIR app launch, patient authorization flow, data scope completeness per USCDI v4, and third-party app registration process
---

## Step 5 --- Training and Change Management

- **Role-based training plans** --- Build training curricula by clinical role (physician, nurse, pharmacist, registration, billing) with minimum hours per role
- **Credential-for-access policy** --- No user gets production access without training completion certification
- **Super user network** --- Recruit and train 1 super user per 10 end users per department. Super users complete 2x the standard training hours
- **Simulation environments** --- Provide training environments with realistic patient data (de-identified). Physicians must complete at least 5 simulated encounters before go-live
- **Communication cadence** --- Weekly stakeholder updates starting 12 weeks pre-go-live; daily updates starting 2 weeks pre-go-live

---

## Step 6 --- Go-Live Readiness and Command Center

The final 30 days before go-live follow a structured checklist:

- **Readiness assessment scoring** --- Score each department on a Red/Yellow/Green matrix across: training completion, workflow sign-off, interface testing, data migration validation, downtime procedures
- **Go/No-Go decision gate** --- All departments must be Yellow or Green. Any Red triggers executive escalation and potential delay
- **Command center structure** --- Staff a physical and virtual command center with: EHR vendor analysts, interface engineers, clinical informaticists, pharmacy, nursing leadership, and IT operations
- **At-the-elbow support** --- Deploy super users and vendor support staff to every clinical unit for the first 72 hours minimum
- **Issue tracking and triage** --- Use a severity classification: P1 (patient safety risk, system down), P2 (workflow blocked), P3 (inconvenience, workaround available), P4 (enhancement request). P1 response time < 15 minutes
- **Downtime procedures** --- Validate paper-based backup procedures. Conduct at least one unannounced downtime drill pre-go-live

- **Post-go-live optimization roadmap** --- Before go-live, establish the optimization backlog and prioritization framework. Items deferred during build should be tracked with estimated implementation dates and responsible owners
---

## Checkpoint B --- Post-Go-Live Stabilization Review

Within 30 days of go-live, validate:

- [ ] All P1 and P2 issues from command center are resolved or have approved workarounds
- [ ] Interface message volumes match pre-go-live baselines (+/- 10%)
- [ ] Promoting Interoperability measures are generating data (CEHRT reporting)
- [ ] Patient portal (ONC 170.315(e)(1)) is accessible and patients can view USCDI data
- [ ] Clinical documentation time-to-completion is within 20% of pre-go-live baseline
- [ ] No outstanding data migration discrepancies in active patient records
- [ ] Super user support schedule is transitioned to ongoing optimization team

- [ ] FHIR Patient Access API is functional and registered in the national endpoint directory
- [ ] CDS alert volume is baselined and alert fatigue monitoring is active
- [ ] Post-go-live optimization backlog is prioritized with target implementation dates
---

## Quality Audit

- [ ] ONC certification criteria coverage is documented and verified against CHPL
- [ ] All clinical workflows have signed-off future-state documentation
- [ ] Data migration validation report shows acceptance criteria met for all data categories
- [ ] Interface testing results are archived with pass/fail evidence
- [ ] Training completion rates meet minimum thresholds by role
- [ ] Go/No-Go decision is formally documented with sign-off
- [ ] Command center issue log is complete with resolution status for every ticket
- [ ] Post-go-live stabilization metrics are baselined for ongoing optimization

- [ ] CDS rules have been reviewed and rationalized during implementation (not bulk-imported from legacy)
- [ ] FHIR API testing confirms USCDI v4 data class availability via US Core profiles
- [ ] Post-go-live optimization governance structure is defined with clinical informatics oversight
- [ ] Downtime drill results are documented with identified gaps addressed before go-live
---

## Guidelines

- Never skip the migration dry-run. Production data volumes expose timing and transformation issues that test datasets cannot
- Treat interface testing as a patient safety activity, not an IT checklist item. A dropped lab result or duplicated medication order can cause direct patient harm
- Resist scope creep during build: enhancements identified during workflow design go to a post-go-live optimization backlog, not the implementation timeline
- Ensure Cures Act information blocking compliance is validated before go-live, not after. The EHR must support patient access to all EHI without special effort
- Maintain a clinical decision register linking every build decision to the responsible clinician. This prevents post-go-live disputes about "who approved this workflow"
- Plan for a 15-25% productivity dip in the first 4-6 weeks post-go-live. Communicate this expectation to clinical and financial leadership upfront
- Archive all implementation artifacts (SOW, design documents, testing evidence, training records) for ONC audit readiness

- CDS rationalization during implementation is a once-in-a-decade opportunity. Do not import hundreds of legacy alerts into the new system without clinical review. Start with evidence-based, high-impact alerts and add incrementally based on clinical need
- Post-go-live, establish a standing clinical informatics optimization team (not a project team). EHR optimization is continuous and requires dedicated resources beyond the implementation project closeout