---
name: managing-clinical-documentation-improvement
language: en
description: Designs CDI programs with NLP-assisted query generation and documentation quality metrics. Use when implementing CDI programs, designing documentation queries, or measuring documentation quality.
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

# Managing Clinical Documentation Improvement

Designs and operates Clinical Documentation Improvement (CDI) programs with NLP-assisted query generation, documentation quality metrics, and DRG impact analysis. This skill covers CDI program structure, query design, technology-assisted review, and outcomes measurement for both inpatient and outpatient settings.

## Why This Skill Exists

Clinical documentation drives diagnosis coding, which determines DRG assignment (inpatient reimbursement), HCC risk scores (Medicare Advantage and ACO risk adjustment), quality measure performance, severity-of-illness and risk-of-mortality indicators, and public reporting outcomes. Incomplete or imprecise documentation understates patient acuity, resulting in: underpayment (average CDI program recovers $1,500-3,000 per inpatient case), inaccurate severity metrics (affecting hospital rankings), and misrepresented case mix (affecting resource allocation and benchmarking). CDI bridges the gap between clinical knowledge and coded data by identifying documentation opportunities and facilitating physician queries.


CDI programs have evolved beyond inpatient DRG optimization. Outpatient CDI targeting HCC risk adjustment, quality measure documentation, and SDOH capture is increasingly critical for organizations participating in value-based care arrangements. The shift to ICD-10-CM's expanded specificity requirements (over 72,000 codes vs. ICD-9-CM's 14,000) amplified the documentation-coding gap, making CDI programs essential for accurate clinical data representation.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Program scope** --- Inpatient CDI, outpatient/ambulatory CDI (HCC-focused), or both?
2. **Current CDI staffing** --- Number of CDI specialists, credentials (CCDS, CDIP, RN, coding certification), and current caseload per specialist
3. **Technology platform** --- What CDI technology is in use? (3M 360 Encompass, Optum CDI, Nuance CDI, Iodine, EHR-native CDI module, manual review)
4. **Documentation platform** --- How do physicians document? (EHR templates, dictation/transcription, voice-to-text, hybrid)
5. **Query methodology** --- How are physician queries delivered? (EHR-based electronic query, paper query, verbal communication)
6. **Baseline metrics** --- Current query rate, query response rate, query agreement rate, case mix index (CMI), CC/MCC capture rate, and top DRG-shift opportunities
7. **Coding partnership** --- What is the relationship between CDI and Health Information Management (HIM) coding? Concurrent vs. retrospective workflow? Reconciliation process for CDI-coder disagreements?

### Required Documents

- CDI program policies and procedures manual
- Current query templates and query response options
- CDI productivity and outcome reports (last 12 months)
- Case mix index trend data by service line
- Top 25 DRGs by volume and revenue
- CC/MCC capture rate benchmarks (ACDIS benchmarks, internal targets)
- NLP/technology platform configuration documentation

8. **Outpatient CDI scope** --- Is outpatient/ambulatory CDI in scope for HCC risk adjustment, quality measure documentation, or SDOH capture?
9. **Physician engagement** --- What is the current level of physician engagement with CDI? What education programs have been conducted?

### CDI Benchmark Reference

| Metric | ACDIS National Benchmark | Target |
|---|---|---|
| Query rate (queries per admission) | 40-60% | Organization-specific |
| Query response rate | 80-90% | >= 85% |
| Query agreement rate | 65-75% | >= 70% |
| CDI review coverage | 70-100% | >= 80% of target admissions |
| Average queries per CDI specialist per day | 4-8 | 5-7 |
| CC/MCC capture rate improvement | 2-5% over baseline | Organization-specific |
---

## Step 1 --- Design the CDI Review Process

Structure the concurrent documentation review workflow:

- **Case selection criteria** --- Define which admissions receive CDI review. Common criteria: all inpatient admissions (100% review for large programs), targeted high-opportunity DRGs (sepsis, respiratory failure, malnutrition, heart failure), cases with high severity-of-illness potential, surgical cases with complication/comorbidity opportunities
- **Review timing** --- Define the review schedule: initial review within 24-48 hours of admission (working DRG assignment), follow-up review every 48-72 hours for cases with pending queries, and pre-coding final review before discharge
- **Clinical indicator identification** --- CDI specialists review: lab results (lactate > 2 for sepsis, albumin < 3.0 for malnutrition, BNP > 400 for heart failure), vital signs (fever, tachycardia, hypotension), medication orders (vasopressors suggesting shock, antibiotics suggesting infection), and clinical notes (treatment intensity, monitoring frequency, clinical language suggesting undocumented diagnoses)
- **DRG impact analysis** --- For each documentation opportunity, estimate the DRG impact: current working DRG vs. potential DRG with complete documentation, difference in relative weight, CC vs. MCC distinction, and whether the documentation gap represents a genuine clinical condition that is supported by clinical indicators

- **Outpatient CDI focus areas** --- For ambulatory CDI, target: HCC condition recapture at annual visits, chronic condition specificity (diabetes with complications vs. without), SDOH documentation (Z55-Z65 codes), and disease severity documentation for risk-adjusted quality measures
---

## Step 2 --- Design Physician Queries

Craft effective queries that improve documentation:

- **Query types** --- Use structured query categories: (a) Diagnosis clarification (clinical indicators suggest a condition not documented), (b) Specificity queries (documented diagnosis lacks required specificity --- e.g., "acute kidney injury" without stage), (c) Cause-and-effect (linking diagnoses --- e.g., "is the acute kidney injury related to the sepsis?"), (d) Present on admission (POA) status clarification
- **Query construction rules** --- Follow ACDIS/AHIMA compliant query guidelines: present clinical indicators supporting the query, do not lead the physician to a specific diagnosis, offer clinically appropriate response options (including "unable to determine" and "clinically undetermined"), reference the specific documentation location (note date, lab result) that triggered the query
- **Non-leading format** --- Compliant queries present findings and ask open questions. Non-compliant: "Can you document sepsis?" Compliant: "Lab results show lactate of 4.2, WBC of 18,000, and the patient is receiving IV antibiotics and vasopressors. Based on your clinical judgment, is there a diagnosis that further clarifies the clinical picture? Please document in the medical record."
- **Electronic query delivery** --- Configure electronic query delivery in the EHR to maximize response rates: appear in the physician's task list or inbox, link directly to the relevant note for documentation, allow one-click response, and automatically route responses to the CDI specialist
- **Query escalation** --- Define escalation for non-responsive physicians: initial query (Day 0), reminder (Day 2), escalation to department chair (Day 5), final pre-coding query (Day 7 or discharge, whichever is first)

- **Query tracking and analytics** --- Maintain a query database tracking: query type, clinical condition, queried physician, response time, response outcome, DRG impact, and whether the query led to a documentation change. Analyze patterns quarterly to identify high-yield query types and low-responding physicians for targeted education
---

## Step 3 --- Implement NLP-Assisted CDI

Leverage technology to augment CDI specialist productivity:

- **NLP case prioritization** --- Configure NLP to score admissions based on documentation opportunity potential: cases with clinical indicators suggesting high-acuity conditions not yet documented, cases where current documentation supports a higher-severity DRG than currently assigned, and cases with known high-opportunity conditions (sepsis, malnutrition, respiratory failure, encephalopathy)
- **Automated clinical indicator detection** --- Train or configure NLP to identify: sepsis criteria (SIRS + suspected infection source from antibiotics and cultures), malnutrition indicators (BMI < 18.5, albumin < 3.0, prealbumin < 15, documented weight loss), acute respiratory failure indicators (supplemental O2 > 4L, ABG abnormalities, mechanical ventilation), and acute kidney injury staging (creatinine trends per KDIGO criteria)
- **NLP-generated query drafts** --- Use NLP to pre-populate query templates with patient-specific clinical indicators: pull relevant lab values, medication orders, and vital signs directly into the query body, reducing CDI specialist documentation time from 15 minutes to 5 minutes per query
- **False positive management** --- NLP systems generate false positives. Track the rate of NLP-suggested opportunities that CDI specialists dismiss after clinical review. Tune NLP sensitivity to maintain a positive predictive value > 50% (fewer than half of suggestions dismissed)
- **Retrospective NLP analysis** --- Run NLP against coded/discharged cases to identify missed opportunities: cases where clinical indicators supported a CC/MCC that was not coded, and cases where documentation was present but coding missed the capture. Feed findings back to coder education

- **NLP vendor evaluation criteria** --- When selecting or evaluating NLP-assisted CDI technology, assess: condition detection sensitivity (>= 80% for target conditions), positive predictive value (>= 50% to avoid alert fatigue), EHR integration capability, workflow integration with CDI specialist review queue, and vendor transparency on algorithm methodology
---

## Step 4 --- Measure CDI Program Outcomes

Track metrics that demonstrate program value:

- **Query metrics** --- Query rate (queries per admission), query response rate (target > 85%), query agreement rate (target > 70%), average query turnaround time (target < 48 hours), and query type distribution
- **Financial impact** --- DRG change rate (percentage of reviewed cases with DRG shift), average relative weight increase per DRG shift, total estimated revenue impact (DRG shifts x relative weight change x blended rate), and CC/MCC capture rate trend
- **Documentation quality indicators** --- SOI/ROM distributions compared to expected benchmarks (Vizient, Premier), specificity rates for key diagnoses (e.g., percentage of heart failure cases documented as systolic vs. diastolic vs. unspecified), present on admission (POA) accuracy rate
- **Coder-CDI reconciliation** --- Track the rate and reasons for coder disagreement with CDI-recommended codes. Common disagreement areas: differing interpretation of clinical criteria, missing documentation despite query response, coding guideline application differences
- **Benchmark comparison** --- Compare program metrics against ACDIS benchmarks: national CDI query rate, agreement rate, review coverage, and CMI impact

- **Service line analysis** --- Break down CDI metrics by service line (cardiology, pulmonology, general surgery, orthopedics, oncology) to identify service lines with the greatest documentation improvement opportunity and tailor CDI specialist assignments accordingly
---

## Step 5 --- Operate the CDI-Coding Reconciliation Process

Align CDI and coding for final code assignment:

- **Concurrent reconciliation** --- Where CDI and coding overlap on active cases, define the reconciliation workflow: CDI documents the working DRG and recommended codes, coder reviews CDI recommendations alongside the documentation, disagreements are flagged for joint review before final code submission
- **Retrospective reconciliation** --- For cases where CDI and coding produce different code assignments, conduct weekly reconciliation meetings: review disagreement cases, determine which code assignment is correct per ICD-10-CM Official Guidelines and AHA Coding Clinic guidance, and document the resolution
- **Escalation to physician** --- When CDI-coding disagreement centers on clinical interpretation (not coding guidelines), escalate to the attending physician for clarification. Do not code a diagnosis that the physician has not documented, even if clinical indicators are present
- **Education feedback loop** --- Use reconciliation findings to drive education: if CDI specialists consistently miss coding guidelines, update CDI training; if coders consistently miss documentation nuances, update coder training; if physicians consistently fail to document specific conditions, design targeted physician education


### CDI Impact Tracking Table

| Impact Category | Metric | Measurement Method |
|---|---|---|
| Financial | DRG shift revenue impact | (DRG weight change) x (blended rate) per case |
| Financial | CC/MCC capture rate change | Monthly trending vs. baseline |
| Quality | SOI/ROM distribution shift | Vizient or Premier benchmark comparison |
| Quality | Mortality index improvement | Risk-adjusted per service line |
| Compliance | Query compliance rate | ACDIS/AHIMA audit of query samples |
| Operational | CDI specialist productivity | Reviews per FTE per day |
---

## Checkpoint B --- CDI Program Review

Review the program status quarterly:

- [ ] CDI review coverage meets organizational target (percentage of admissions reviewed)
- [ ] Query response rate exceeds 85%
- [ ] Query agreement rate exceeds 70%
- [ ] All queries comply with ACDIS/AHIMA compliant query guidelines
- [ ] NLP-assisted prioritization is functioning with acceptable positive predictive value
- [ ] CDI-coding reconciliation process is operational with documented disagreement resolution
- [ ] CMI trend reflects program impact adjusted for patient population changes
- [ ] Physician education is delivered based on documentation opportunity patterns

- [ ] Service line-specific CDI impact analysis is completed quarterly
- [ ] Outpatient CDI (if in scope) tracks HCC recapture rates and specificity improvements
- [ ] CDI specialist caseload does not exceed recommended benchmarks per ACDIS
---

## Quality Audit

- [ ] Query templates are reviewed annually for ACDIS/AHIMA compliance
- [ ] No queries lead the physician to a specific diagnosis (non-leading principle)
- [ ] Financial impact calculations use documented methodology with verifiable data
- [ ] CDI does not drive documentation of conditions not supported by clinical indicators (upcoding risk)
- [ ] NLP configuration is validated against clinical criteria for each target condition
- [ ] SOI/ROM distributions are compared against risk-adjusted benchmarks (not raw comparisons)
- [ ] CDI-coding disagreement rate is tracked and trending downward
- [ ] CDI specialist competency is assessed annually (ACDIS certification, case studies)
- [ ] Program metrics are reported to clinical and financial leadership quarterly

- [ ] CDI program has a documented compliance plan reviewed by the compliance department annually
- [ ] NLP-assisted CDI technology is validated against clinical criteria with documented sensitivity and PPV
- [ ] CDI impact on quality measures (not just financial metrics) is tracked and reported
- [ ] CDI education materials are updated annually to reflect current ICD-10-CM coding guidelines and AHA Coding Clinic guidance
---

## Guidelines

- CDI captures clinically supported documentation, not manufactured documentation. A CDI program that pressures physicians to document conditions not supported by clinical indicators is an upcoding scheme, not a quality program
- Query compliance is non-negotiable. Leading queries (e.g., "Please document sepsis") violate ACDIS/AHIMA guidelines and create compliance liability. Every query must present clinical indicators and ask for the physician's clinical judgment
- CDI for outpatient HCC capture is increasingly important for risk-bearing organizations. Outpatient CDI focuses on chronic condition specificity, condition recapture (documenting known conditions at annual visits), and SDOH documentation for HCC-relevant categories
- NLP is an augmentation tool, not a replacement for clinical CDI judgment. CDI specialists must validate every NLP-suggested opportunity against the complete clinical picture before issuing a query
- Track CDI's impact on quality metrics alongside financial metrics. Accurate diagnosis documentation improves SOI/ROM indicators, which affect hospital rankings, peer comparisons, and public reporting
- Malnutrition, sepsis, acute respiratory failure, and encephalopathy are the highest-impact CDI focus areas across most organizations. Prioritize NLP configuration and CDI specialist training for these conditions
- CDI and compliance must collaborate. Regular compliance audits of CDI query patterns and documentation changes protect the organization from False Claims Act risk
- Physician education is the long-term CDI strategy. Reducing the need for queries by improving initial documentation quality is more sustainable than expanding CDI specialist headcount

- Measure CDI ROI holistically: include financial impact (DRG shifts), quality impact (SOI/ROM, mortality index), compliance impact (reduced audit risk), and operational impact (coding accuracy improvement). A CDI program justified solely on revenue recovery misses the quality dimension
- CDI and coding must maintain independent review capability. CDI recommends; coding assigns. The final code must be supported by documentation and coding guidelines, not by CDI pressure