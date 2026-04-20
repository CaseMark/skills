---
name: managing-clinical-data-quality
language: en
description: Structures data quality management with query resolution, source data verification, and audit trails. Use when managing clinical data quality, resolving data queries, or conducting SDV.
tags:
  - management
  - clinical-research
  - clinical
  - audit
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Biostatistics
    - Regulatory Affairs
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Clinical Data Quality

## Why This Skill Exists

Clinical data quality directly determines whether a study produces reliable evidence for regulatory decision-making. FDA 21 CFR 11 and ICH-GCP E6(R2) Section 5.5 require that data be attributable, legible, contemporaneous, original, and accurate (ALCOA+ principles). A single data-integrity failure — fabricated data, unchecked discrepancies, or broken audit trails — can invalidate an entire dataset and trigger regulatory action. This skill provides the operational framework for data quality management (DQM) across the clinical data lifecycle, from CRF design through database lock.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What electronic data capture (EDC) system is used (Medidata Rave, Oracle InForm, Veeva Vault CDMS, REDCap)?
2. What external data sources feed into the clinical database (central lab, ePRO, ECG, imaging, IWRS/IRT, PK)?
3. What is the data management plan (DMP) version and status?
4. What CDISC standards apply (CDASH for CRF design, SDTM for datasets, ADaM for analysis)?
5. What is the current data query rate and resolution timeline?
6. What source data verification (SDV) approach is specified in the monitoring plan?
7. What medical coding dictionaries are used (MedDRA version for AEs, WHO Drug Dictionary for medications)?
8. Are there data review committee (DRC) or medical-monitor review requirements?
9. What is the database-lock timeline and what are the pre-lock activities?
10. Have data-transfer agreements (DTAs) been executed with all external data vendors?

### Required Source Documents
- Data Management Plan (DMP)
- CRF completion guidelines
- Edit-check specifications (validation rules)
- Data Transfer Agreements with external vendors
- Medical coding conventions document
- SAE reconciliation plan
- Database lock checklist
- Monitoring plan (SDV and SDR specifications)
- 21 CFR Part 11 compliance documentation for the EDC system

---

## Step 1 — Design CRFs Following CDASH Standards

Build case report forms that facilitate clean data entry:

1. **CDASH compliance**: Map each CRF field to the CDISC CDASH Implementation Guide standard; ensure domain-variable-name consistency from CRF to SDTM
2. **Field-level specifications**: Data type (numeric, text, date, coded list), valid ranges, mandatory vs. optional, display format
3. **Skip logic**: Program conditional branching so irrelevant fields are hidden (e.g., pregnancy questions hidden for male participants)
4. **Real-time edit checks**: Implement at data-entry time to catch errors immediately:
   - Range checks (lab values within physiologically plausible range)
   - Consistency checks (death date cannot precede enrollment date)
   - Conditional checks (if pregnant=yes, pregnancy outcome fields become mandatory)
   - Cross-form checks (AE onset date must fall within study-participation dates)
5. **Annotation**: Annotate the blank CRF with SDTM domain and variable mappings for regulatory submission (CSR Appendix 16.2)
6. **UAT (User Acceptance Testing)**: Test all CRF pages, edit checks, and skip logic before first site activation; document test scenarios and results

---

## Step 2 — Implement Edit-Check Specifications

Design and validate the programmatic data-cleaning rules:

### Edit-Check Categories
1. **Hard checks (errors)**: Prevent illogical data entry (e.g., systolic BP < diastolic BP, visit date before birth date). Data cannot be saved until corrected.
2. **Soft checks (warnings)**: Flag unusual but possible values (e.g., age >90, weight >150 kg). Data can be saved with acknowledgment.
3. **Cross-domain checks**: Compare data across CRF modules (AE dates vs. treatment dates, lab values vs. AE reporting, concomitant medications vs. medical history)
4. **External-data checks**: Compare EDC entries with central lab transfers, IWRS randomization data, ePRO data

### Documentation Requirements
- Each edit check documented with: check ID, description, logic statement, CRF fields involved, severity (hard/soft), action (auto-query, block entry, flag for review)
- Edit-check specifications reviewed and signed off by data management, biostatistics, and clinical operations
- Version-controlled and updated with each protocol amendment

---

## Step 3 — Manage Data Queries

Implement a systematic query-resolution workflow:

### Query Lifecycle
1. **Generation**: System-generated (from edit checks) or manual (from data review by CRA, medical monitor, or data manager)
2. **Issuance**: Query sent to site with clear description of the discrepancy and required action
3. **Response**: Site investigates source documents and provides a response with corrective data or explanation
4. **Resolution**: Data manager reviews the response; if satisfactory, closes the query; if not, re-queries
5. **Closure**: Query closed with final status (data corrected, confirmed as correct, source-verified)

### Query Metrics
- Track open-query count by site, query age (days open), query type (system vs. manual), response time
- Benchmark: <5% open-query rate; average resolution time <14 days
- Sites with persistently high query rates or slow resolution trigger enhanced monitoring or retraining

### Query Quality
- Queries must be specific and actionable — "Please verify" is insufficient; provide the exact discrepancy and the expected correction
- Avoid duplicate or trivial queries that create site fatigue and reduce response quality
- Batch queries where possible to reduce site workload

---

## Step 4 — Conduct Source Data Verification and Review

Implement the SDV/SDR strategy from the monitoring plan:

### Source Data Verification (SDV)
- Compare EDC data against source documents (medical records, lab printouts, participant diaries)
- Under RBQM, SDV is targeted to critical data: primary endpoint data, key safety data (SAEs, deaths), eligibility criteria, informed consent dates
- 100% SDV is no longer the default — risk-based SDV rates (e.g., 20% SDV for low-risk data, 100% SDV for critical data)
- Document SDV findings and report site-level data-quality metrics

### Source Data Review (SDR)
- Review source documents for completeness, consistency, and GCP compliance
- Verify that source documents support the data entered in the CRF
- Assess whether the data are contemporaneous (entered at the time of the event, not retrospectively reconstructed)
- Identify potential fraud indicators: identical data patterns, improbable consistency, missing source documents

### ALCOA+ Compliance Assessment
- **Attributable**: Can identify who recorded the data and when
- **Legible**: Data are readable and permanent
- **Contemporaneous**: Recorded at the time of the activity
- **Original**: First-recorded data (or certified copy)
- **Accurate**: Data correctly represent the observation
- **+Complete**: All required data points are present
- **+Consistent**: Data are consistent across sources and timepoints
- **+Enduring**: Data stored on durable media with appropriate retention
- **+Available**: Data accessible for review throughout the required retention period

---

## Step 5 — Manage External Data Integration

Coordinate data transfers from external vendors:

1. **Data Transfer Agreement (DTA)**: Define file format (SAS, CSV, XML), transfer frequency, naming conventions, delivery method (sFTP, API), and reconciliation procedures
2. **Central laboratory data**: Receive and load lab results; run edit checks against EDC-entered data; reconcile discrepancies (lab accession numbers, dates, participant IDs)
3. **IWRS/IRT data**: Randomization and dispensing data; reconcile with EDC treatment-assignment and IP-accountability records
4. **ePRO data**: Electronic patient-reported outcome data; validate transmission integrity and mapping to SDTM domains
5. **ECG/imaging data**: Central-read results; reconcile with site-entered assessments
6. **SAE reconciliation**: Reconcile SAE data between the safety database (Argus, AriSGlobal) and the clinical database; resolve any discrepancies before database lock

---

## Step 6 — Execute Database Lock

Perform systematic pre-lock activities:

### Pre-Lock Checklist
1. [ ] All data queries are resolved and closed (zero open queries)
2. [ ] External data transfers are complete and reconciled
3. [ ] Medical coding (MedDRA, WHO Drug) is complete and consistent
4. [ ] SAE reconciliation is complete (zero discrepancies)
5. [ ] Protocol deviation log is finalized
6. [ ] Analysis-population assignment is complete (ITT, PP, safety designations)
7. [ ] Blind review of data is complete (medical review, statistical review)
8. [ ] Edit-check programs have been run on the final dataset
9. [ ] SDTM datasets are generated and validated (Pinnacle 21 / OpenCST)
10. [ ] Data management report is drafted

### Lock Procedure
1. Announce soft lock (no further data entry; final queries issued)
2. Complete final QC and issue a database-lock memo
3. Execute hard lock (database frozen; audit trail records lock event)
4. Generate final datasets (SDTM, ADaM)
5. Distribute datasets to biostatistics for analysis
6. Any post-lock changes require formal unlock request, documentation, and re-lock

---

## Checkpoint B — Data Quality Review

1. [ ] CRF design follows CDASH standards with annotated SDTM mappings
2. [ ] Edit checks are documented, tested, and version-controlled
3. [ ] Query resolution rate is within benchmarks (<5% open, <14-day average resolution)
4. [ ] SDV/SDR findings are documented and site-level metrics are tracked
5. [ ] All external data sources are reconciled with the clinical database
6. [ ] ALCOA+ principles are demonstrated for critical data elements
7. [ ] Medical coding is complete and dictionary versions are documented
8. [ ] SAE reconciliation shows zero discrepancies
9. [ ] Pre-database-lock checklist items are all complete
10. [ ] SDTM datasets pass Pinnacle 21 validation with no critical errors

---

## Quality Audit

- [ ] EDC system has documented 21 CFR Part 11 compliance (audit trail, electronic signatures, access controls)
- [ ] All edit checks have been validated (tested against known correct and known incorrect data)
- [ ] No source-document fabrication indicators identified during SDV/SDR
- [ ] Query text is specific and actionable (no vague "please verify" queries)
- [ ] External-data reconciliation logs are complete for all vendors
- [ ] Database-lock memo is signed by data management lead, biostatistics lead, and medical monitor
- [ ] Post-lock dataset changes (if any) are documented with justification and re-lock memo
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. Data quality is built into the process, not inspected in after the fact — invest in CRF design, edit checks, and site training upfront
2. ALCOA+ principles are non-negotiable — every data point must meet these criteria
3. Risk-based SDV is the current standard per ICH-GCP E6(R2) — 100% SDV is neither required nor efficient
4. Query fatigue is real — write clear, necessary queries; batch where possible; avoid trivial queries that dilute site attention
5. External-data reconciliation must be completed before database lock — post-lock reconciliation is operationally disruptive and raises data-integrity questions
6. SDTM datasets must pass validation (Pinnacle 21) before submission to regulators — submission-critical errors must be resolved
7. Database lock is irreversible in principle — any post-lock change requires senior approval, documentation, and re-validation
8. Fraud detection is a monitoring responsibility — apply statistical and pattern-based methods (CSDA, central monitoring) to identify anomalous data
9. Mark any data-integrity concern that requires investigation with [VERIFY] for quality-assurance and medical-monitor escalation
10. This skill produces data-management frameworks — final database-lock authorization requires data management lead, biostatistics lead, and medical-monitor sign-off
