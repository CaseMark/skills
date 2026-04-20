---
name: managing-privacy-breach-response
language: en
description: Guides HIPAA breach investigation with risk assessment, notification requirements, and remediation documentation. Use when managing data breaches, assessing breach risk, or documenting breach response.
tags:
  - management
  - healthcare-compliance
  - risk
metadata:
  author: casemark
  practice_areas:
    - Healthcare Compliance
    - HIPAA
    - Healthcare Regulation
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Privacy Breach Response

A structured framework for investigating, assessing, notifying, and remediating breaches of unsecured protected health information under the HIPAA Breach Notification Rule (45 CFR §§ 164.400–414) and HITECH Act § 13402.

## Why This Skill Exists

Since the 2013 Omnibus Rule shifted the breach standard from a "harm" threshold to a presumption-of-breach model, covered entities and business associates face strict notification timelines and escalating penalties for delayed or incomplete responses. OCR enforcement data shows breach notification failures—late notifications, inadequate risk assessments, missing substitute notices—as a top category in resolution agreements. A disciplined breach response process reduces regulatory exposure, limits reputational damage, satisfies state AG notification requirements that often run parallel to HIPAA, and preserves evidence needed for litigation defense against class actions that routinely follow large breaches.

---

## Checkpoint A — Incident Intake and Triage

### Intake Questions

1. When was the incident discovered, and by whom? The 60-day notification clock starts from the date the first workforce member knew or should have known of the breach per § 164.404(a)(2).
2. What type of incident occurred—unauthorized access, improper disclosure, loss/theft of device, cyberattack, misdirected communication, improper disposal?
3. How many individuals are potentially affected? This determines whether the 500-individual threshold for contemporaneous HHS/media notification applies.
4. What categories of PHI were involved—demographic, clinical, financial, SSN, substance abuse (42 CFR Part 2), psychotherapy notes, genetic information?
5. Was the PHI "unsecured" per HHS guidance—i.e., was it not encrypted per NIST SP 800-111 or not destroyed per NIST SP 800-88?
6. Is the entity a covered entity or business associate, and has the other party been notified?
7. Has law enforcement requested a notification delay under § 164.412?
8. Are there state breach notification laws that impose shorter timelines or broader notification requirements?
9. Has the entity engaged forensic investigators, and is investigation under attorney-client privilege?
10. Is there evidence of ongoing unauthorized access requiring immediate containment?

### Required Documents

- Incident report with timeline of discovery and initial response actions
- IT forensic analysis or preliminary findings
- List of affected systems, devices, and data repositories
- Business associate agreement (if BA-related incident)
- PHI data mapping for affected systems
- Current breach notification policies and procedures
- Prior breach log entries for pattern analysis
- Insurance policy (cyber liability) declarations page
- State-by-state notification requirement matrix for affected individuals' residences
- Communication templates (individual notice, media notice, HHS submission)

---

## Step 1 — Containment and Evidence Preservation

- Immediately isolate affected systems to prevent ongoing unauthorized access without destroying forensic evidence.
- Engage forensic investigators under attorney-client privilege through legal counsel where litigation is anticipated.
- Preserve all relevant logs—access logs, audit trails, system logs, email server logs, VPN logs—before automatic rotation destroys evidence.
- Document the chain of custody for all devices and media involved in the incident.
- If the breach involves a business associate, activate the BA notification and cooperation provisions of the BAA.
- Implement temporary compensating controls (password resets, access revocations, network segmentation) while root cause analysis proceeds.
- Record all containment actions with timestamps, responsible parties, and outcomes.

---

## Step 2 — Four-Factor Breach Risk Assessment

Apply the four-factor risk assessment required by § 164.402(2) to determine whether the incident constitutes a reportable breach:

**Factor 1 — Nature and Extent of PHI Involved**:
- Identify the specific data elements exposed (names, SSNs, diagnoses, treatment records, financial information).
- Assess whether the PHI includes sensitive categories that increase harm risk—HIV/AIDS, substance abuse, mental health, reproductive health, genetic data.
- Determine the volume of records and whether data is structured (database) or unstructured (scanned documents, free text).

**Factor 2 — Unauthorized Person Who Used or Received the PHI**:
- Identify the unauthorized recipient and their relationship to the entity (employee in wrong department, external vendor, unknown threat actor, unintended recipient of fax/email).
- Assess whether the recipient has independent obligations to protect PHI (e.g., another covered entity, a BA).
- Evaluate the recipient's ability and motivation to use the PHI for harmful purposes.

**Factor 3 — Whether PHI Was Actually Acquired or Viewed**:
- Distinguish between access opportunity and confirmed access—a lost encrypted laptop where encryption was active presents lower risk than a confirmed database exfiltration.
- Review forensic evidence for indicators of data access, exfiltration, or copying.
- Consider whether the PHI was returned or destroyed before it could be used.

**Factor 4 — Extent to Which Risk Has Been Mitigated**:
- Document all mitigation steps: retrieval of disclosed PHI, recipient attestations of deletion, credit monitoring offered, system patches applied, access revoked.
- Assess residual risk after mitigation efforts.
- Determine whether mitigation reduces the probability of compromise to a level where notification may not be required.

**Conclusion**: Document whether, based on the totality of the four factors, there is a low probability that PHI has been compromised. If the assessment does not demonstrate low probability, the incident is a reportable breach and notification must proceed.

---

## Step 3 — Notification Execution

**Individual Notification (§ 164.404)**:
- Send written notice to affected individuals within 60 calendar days of discovery via first-class mail or email (if individual previously agreed to electronic notice).
- Include all required content: description of breach and date, types of PHI involved, steps individuals should take to protect themselves, what the entity is doing to investigate and mitigate, and contact information for questions.
- For individuals with outdated contact information, provide substitute notice—web posting for 90 days plus toll-free number for 10+ individuals, or media notice for areas with outdated addresses.
- For urgent situations involving possible misuse, consider supplemental telephone notice.

**HHS Notification (§ 164.408)**:
- For breaches affecting 500+ individuals: submit to HHS contemporaneously with individual notice using the HHS breach reporting portal. These are posted to the public "Wall of Shame."
- For breaches affecting fewer than 500 individuals: log and submit to HHS within 60 days of the end of the calendar year in which the breach was discovered.

**Media Notification (§ 164.406)**:
- Required when a breach affects 500+ residents of a single state or jurisdiction.
- Issue a press release or equivalent notice to prominent media outlets serving the affected area.
- Time concurrently with individual notification.

**State Notification**:
- Map affected individuals to state of residence and apply each state's breach notification statute (e.g., California Civil Code § 1798.82, New York General Business Law § 899-aa, Texas Health & Safety Code § 181.202).
- Many states impose shorter timelines than HIPAA (e.g., 30 days in some states) and require notification to the state AG.

---

## Step 4 — Root Cause Analysis and Remediation

- Complete a formal root cause analysis identifying technical, administrative, and human factors that enabled the breach.
- Map root causes to specific HIPAA Security Rule or Privacy Rule requirements that were deficient.
- Develop a corrective action plan with: specific remediation steps, responsible parties, target completion dates, and verification methods.
- Implement workforce re-training targeted to the specific failure mode (not generic HIPAA refresher).
- Update policies and procedures to address identified gaps.
- If the breach reveals systemic risk analysis deficiencies, conduct a focused Security Risk Analysis update per § 164.308(a)(1)(ii)(A).
- Document all remediation for potential OCR investigation response.

---

## Step 5 — Post-Incident Documentation and Reporting

- Compile a complete breach response file including: incident report, forensic findings, four-factor risk assessment, notification copies, delivery confirmations, remediation plan, and board/leadership briefings.
- Update the breach log per § 164.530(j) with all required information.
- Prepare a board-level summary of the incident, response actions, costs, and risk posture changes.
- Retain all breach documentation for a minimum of six years per § 164.530(j).
- If OCR opens an investigation, coordinate response through legal counsel and provide documentation in accordance with OCR's data request format.

---

## Checkpoint B — Response Completeness Review

1. Confirm the 60-day notification deadline is met from the date of discovery (not the date the investigation concluded).
2. Verify the four-factor risk assessment is documented in writing with analysis of each factor and a clear conclusion.
3. Confirm individual notifications contain all five required content elements per § 164.404(c).
4. Verify HHS portal submission is complete and matches the details in individual notifications.
5. Confirm state notification requirements are met for all affected individuals' states of residence.
6. Validate that the business associate (if involved) provided timely notification to the covered entity per BAA and § 164.410.
7. Review corrective action plan for specificity—generic commitments to "improve security" are insufficient.
8. Confirm breach log is updated with this incident.
9. Verify all documentation is preserved for the six-year retention period.

---

## Quality Audit

- [ ] Discovery date correctly identified and 60-day clock calculated accurately
- [ ] Four-factor risk assessment addresses each factor with specific evidence
- [ ] PHI categorization includes sensitive data types (substance abuse, HIV, mental health, genetic)
- [ ] Individual notification letters contain all five required elements
- [ ] Substitute notice procedures followed for individuals with outdated addresses
- [ ] HHS notification submitted via portal within required timeframe
- [ ] Media notification issued if 500+ state/jurisdiction threshold met
- [ ] State breach notification requirements mapped and satisfied
- [ ] Root cause analysis identifies specific technical and administrative failures
- [ ] Corrective action plan has named owners, deadlines, and verification criteria
- [ ] Breach log updated with complete incident details
- [ ] Documentation retained for minimum six-year period

---

## Guidelines

- The 60-day notification period is a maximum, not a target—OCR has stated that entities should notify "without unreasonable delay" and will scrutinize entities that consistently use the full 60 days.
- Never skip the four-factor risk assessment, even when a breach appears obvious—the documented assessment is essential evidence in OCR investigations and protects against allegations of failure to properly evaluate incidents.
- Encryption is the primary safe harbor: if PHI was encrypted per NIST standards and the encryption key was not compromised, the data is "secured" and breach notification is not required per HHS guidance.
- Business associates must report breaches to covered entities without unreasonable delay and no later than 60 days; BAAs may contractually shorten this period.
- Coordinate with law enforcement early—§ 164.412 permits notification delay if law enforcement provides a written statement that notice would impede a criminal investigation.
- When multiple state breach notification laws apply, use the strictest requirement as the baseline rather than managing different timelines per state.
- Breach response files should be assembled with the assumption that OCR will request them—clear, organized documentation demonstrates good faith compliance.
- This skill produces compliance documentation, not legal advice. Coordinate all breach notification decisions with qualified healthcare privacy counsel.
