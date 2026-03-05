---
name: managing-good-clinical-practice
description: Applies GCP/ICH principles to clinical research operations with compliance monitoring. Use when ensuring GCP compliance, training on ICH guidelines, or auditing research practices.
tags:
  - management
  - clinical-research
  - compliance
  - clinical
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

# Managing Good Clinical Practice

## Why This Skill Exists

Good Clinical Practice (GCP) is the international ethical and scientific quality standard for designing, conducting, recording, and reporting clinical trials. ICH-GCP E6(R2) — adopted by FDA (21 CFR Parts 11, 50, 54, 56, 312, 314), EMA, PMDA, and 50+ regulatory authorities — establishes the minimum requirements that protect participant rights, ensure data integrity, and enable regulatory acceptance of trial results. GCP violations are the leading cause of FDA warning letters to clinical investigators and can render entire datasets unreliable. This skill provides the operational framework for implementing, monitoring, and auditing GCP compliance across a clinical research program.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What is the scope of the GCP assessment (single study, site, sponsor program, institutional research portfolio)?
2. What regulatory framework applies (FDA, EMA, PMDA, multiple jurisdictions)?
3. Is this a prospective GCP implementation or a retrospective compliance audit?
4. What is the current GCP training status of study personnel?
5. Are there existing GCP-related findings (FDA 483s, warning letters, IRB audit findings, sponsor monitoring findings)?
6. What type of monitoring is in place (on-site, centralized, risk-based, hybrid)?
7. Is there an existing quality management system (QMS) with SOPs?
8. What electronic systems are used (EDC, ePRO, CTMS, IWRS/IRT)?
9. Are there any active corrective/preventive action (CAPA) plans?
10. What is the timeline for any upcoming regulatory inspection?

### Required Source Documents
- ICH-GCP E6(R2) guideline (current consolidated version)
- Applicable CFR sections (21 CFR 11, 50, 54, 56, 312, 314)
- Site/sponsor SOPs for GCP operations
- Training records for all study personnel
- Monitoring reports (visit reports, centralized monitoring outputs)
- Previous audit reports and CAPA documentation
- FDA Form 483 observations and warning letters (if applicable)
- Delegation of Authority Logs for active studies
- Regulatory binder/Trial Master File index

---

## Step 1 — Map the 13 ICH-GCP Principles

ICH-GCP E6(R2) Section 2 establishes 13 foundational principles. Assess compliance against each:

1. **Ethical conduct**: Research conducted in accordance with the Declaration of Helsinki and consistent with GCP and applicable regulatory requirements
2. **Risk-benefit**: Foreseeable risks and inconveniences weighed against anticipated benefit; a trial should be initiated only if anticipated benefits justify the risks
3. **Participant rights**: Rights, safety, and well-being of trial participants prevail over interests of science and society
4. **Nonclinical and clinical information**: Adequate to support the proposed clinical trial
5. **Scientific soundness**: Scientifically sound and described in a clear, detailed protocol
6. **Protocol compliance**: Conducted in compliance with the protocol that has received prior IRB/IEC approval
7. **Medical care**: Qualified physician responsible for trial-related medical decisions
8. **Qualified personnel**: Each individual involved is qualified by education, training, and experience
9. **Informed consent**: Freely given informed consent before participation
10. **Recording and reporting**: All clinical trial information recorded, handled, and stored to allow accurate reporting, interpretation, and verification
11. **Confidentiality**: Participant confidentiality maintained per applicable privacy requirements
12. **GMP manufacturing**: Investigational products manufactured, handled, and stored per GMP and used per approved protocol
13. **Quality systems**: Systems with procedures ensuring quality of every aspect of the trial

---

## Step 2 — Implement Risk-Based Quality Management

ICH-GCP E6(R2) Section 5.0 introduced the requirement for risk-based quality management (RBQM):

### Risk Identification
1. Identify critical processes and data (those that directly affect participant safety, data integrity, and regulatory decision-making)
2. Conduct a risk assessment for each critical process: likelihood of error × impact of error × detectability
3. Use structured tools: Failure Mode and Effects Analysis (FMEA), risk-assessment matrices, or process mapping

### Risk Control
1. Implement risk-mitigation measures proportionate to risk level
2. Design quality tolerance limits (QTLs) for key risk indicators (KRIs)
3. Define action thresholds: when KRIs exceed QTLs, trigger predefined responses (query, monitoring visit, CAPA)

### Risk Communication
1. Communicate identified risks and mitigation strategies to all stakeholders
2. Include risk-management outputs in monitoring plans, training, and sponsor oversight
3. Document risk decisions in the Quality Management Plan

### Risk Review
1. Review the RBQM plan at defined intervals (minimum annually or after significant events)
2. Adjust risk assessments based on accumulating data
3. Document lessons learned and update for future studies

---

## Step 3 — Establish the Trial Master File (TMF)

The TMF is the documentary evidence of GCP compliance per ICH-GCP E6(R2) Section 8:

### Essential Documents — Before Trial Commencement
- Investigator's Brochure (current version with distribution log)
- Signed protocol and amendments
- IRB/IEC approval letters with approved consent forms
- Regulatory authority authorization (IND, CTA)
- Insurance documentation (where required)
- Signed investigator agreements (FDA Form 1572 for US sites)
- Financial disclosure forms (21 CFR 54)
- Normal laboratory value ranges and lab certifications
- Study personnel CVs and medical licenses
- Delegation of Authority Log

### Essential Documents — During Trial Conduct
- Signed informed consent forms for each participant
- Source documents and certified copies
- CRF pages (or EDC audit trails)
- Monitoring visit reports
- Correspondence between investigator and sponsor/IRB
- SAE reports and IND Safety Reports
- Protocol deviation logs
- Shipping records for investigational product
- IP accountability logs

### Essential Documents — After Trial Completion
- Final participant disposition
- Study close-out monitoring report
- Drug accountability records (destruction or return)
- Final IRB/IEC notification
- Clinical study report (or reference to)
- Audit certificates (if audited)

Implement TMF Reference Model (DIA TMF Reference Model v3.3) for electronic TMF organization.

---

## Step 4 — Conduct GCP Training Program

Design and maintain a compliant training program:

1. **Initial GCP training**: All study personnel must complete GCP training before participating in trial activities; CITI GCP, TransCelerate GCP, or equivalent
2. **Protocol-specific training**: Training on the specific protocol, procedures, and EDC system; document with sign-off sheets and dates
3. **Refresher training**: GCP certification renewal per institutional policy (typically every 2-3 years; FDA does not specify frequency but expects current knowledge)
4. **Specialized training**: Role-specific training for consent obtainers, data entry personnel, laboratory staff, pharmacy staff
5. **Documentation**: Maintain training logs in the regulatory binder and TMF; include trainer qualifications, date, topic, and attendee signatures
6. **New-team-member onboarding**: Training must be completed before the new member performs any trial-related duties; update Delegation Log simultaneously

---

## Step 5 — Implement Monitoring Per RBQM

Design the monitoring strategy per ICH-GCP E6(R2) Sections 5.18 and 5.20:

### Centralized Monitoring (primary method under RBQM)
- Statistical surveillance of clinical data for patterns, outliers, and anomalies
- KRI dashboards: enrollment rate, protocol deviation rate, AE reporting rate, query rate, consent-to-randomization time
- Cross-site comparison to identify underperforming or atypical sites
- Automated edit checks and data-driven monitoring triggers

### On-Site Monitoring (targeted based on risk)
- Source data verification (SDV) limited to critical data points (primary endpoint, key safety data, consent verification)
- Source data review (SDR) for process compliance
- Regulatory binder review
- IP accountability audit
- Interview with site personnel to assess understanding and compliance

### Remote Monitoring
- Electronic access to site systems (EDC, ePRO, IWRS)
- Telephone/video-conference review of site processes
- Document review via secure file transfer

Document the monitoring plan and justify the approach based on the risk assessment from Step 2.

---

## Step 6 — Manage Protocol Deviations

Implement a deviation-management system:

1. **Classification**: Important (affects participant safety, data integrity, or rights) vs. minor; use ICH-GCP E6(R2) definition and sponsor criteria
2. **Detection**: Through monitoring, centralized data review, site self-reporting, or audit
3. **Documentation**: Capture the deviation, root cause, impact assessment, and corrective action
4. **Reporting**: Important deviations reported to IRB per institutional policy and to sponsor per monitoring plan; include in the clinical study report (ICH E3 Section 10.2)
5. **Trending**: Analyze deviation patterns across sites and over time to identify systemic issues
6. **CAPA**: For recurring or high-impact deviations, implement formal corrective and preventive actions with effectiveness monitoring

---

## Checkpoint B — GCP Compliance Review

1. [ ] All 13 ICH-GCP principles are operationally addressed
2. [ ] Risk-based quality management plan is documented and active
3. [ ] TMF is complete per the DIA TMF Reference Model
4. [ ] All study personnel have current GCP training documented
5. [ ] Monitoring plan is implemented and monitoring reports are current
6. [ ] Protocol deviations are documented, classified, reported, and trended
7. [ ] Investigational product accountability is current at all sites
8. [ ] Delegation of Authority Logs are up to date at all sites
9. [ ] Financial disclosures are complete and current
10. [ ] CAPA plans for any open findings are active and tracked

---

## Quality Audit

- [ ] ICH-GCP E6(R2) version is cited (not the original E6 or E6(R1))
- [ ] RBQM implementation includes all four phases (identify, control, communicate, review)
- [ ] TMF completeness rate is measured and >95% for critical documents
- [ ] GCP training records include date, topic, trainer, and attendee signature
- [ ] Monitoring visit frequency matches the risk-based monitoring plan
- [ ] SDV rate is justified and documented (100% SDV is no longer the default expectation under RBQM)
- [ ] Protocol deviation trending identifies systemic vs. isolated issues
- [ ] Regulatory inspection readiness can be confirmed within 48 hours of notice
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. GCP is a minimum standard, not a ceiling — sponsors and sites may implement additional quality measures
2. RBQM does not mean less monitoring — it means smarter, data-driven monitoring focused on critical processes and data
3. The investigator is ultimately responsible for the conduct of the trial at the site, even when CROs perform delegated functions
4. FDA Form 1572 is a legally binding document — the investigator commits to GCP compliance, IRB review, and protocol adherence
5. Source documents are the first place a data point is recorded — electronic health records, lab printouts, and participant diaries qualify; CRFs are not source documents unless protocol-specified
6. Audit trails in electronic systems must comply with 21 CFR Part 11 (attributable, legible, contemporaneous, original, accurate — ALCOA)
7. Never backdate or alter trial records — corrections must maintain the original entry, reason for change, date of change, and identity of person making the change
8. GCP inspection preparation should be continuous, not a pre-inspection scramble — maintain inspection-ready TMF and documentation at all times
9. Mark any compliance gap that requires immediate remediation with [VERIFY] for quality-assurance escalation
10. This skill produces compliance management frameworks — GCP determinations and inspection responses require qualified regulatory and quality-assurance professionals
