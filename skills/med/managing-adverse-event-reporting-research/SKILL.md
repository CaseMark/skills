---
name: managing-adverse-event-reporting-research
description: Documents research adverse events with causality assessment and regulatory reporting timelines. Use when reporting research AEs, assessing causality, or managing safety reporting.
tags:
  - management
  - clinical-research
  - regulatory
  - research
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

# Managing Adverse Event Reporting in Research

## Why This Skill Exists

Adverse event (AE) reporting is a non-negotiable regulatory obligation in clinical research. Failure to report serious and unexpected adverse events within mandated timelines violates 21 CFR 312.32 (IND Safety Reporting), ICH-GCP E6(R2) Section 4.11, and can trigger FDA clinical holds, site termination, or participant harm. This skill provides the complete AE identification, documentation, causality assessment, and reporting workflow so that every safety event is captured accurately and reported within regulatory deadlines.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. Is this an IND study (FDA-regulated) or non-IND research?
2. What is the sponsor type (industry, investigator-initiated, cooperative group)?
3. What is the current MedDRA version for coding (e.g., MedDRA v26.1)?
4. What severity-grading scale is specified in the protocol (CTCAE v5.0, WHO, or investigator judgment of mild/moderate/severe)?
5. What is the protocol-defined AE collection period (from first dose through follow-up window)?
6. Are there solicited AEs (protocol-specified events collected at defined intervals)?
7. Does the protocol define any events of special interest (AESI)?
8. Who is the sponsor safety-reporting contact and what is the reporting mechanism (safety database, fax, email)?
9. Is there a DSMB or safety monitoring committee reviewing AEs?
10. What are the IRB reporting requirements for unanticipated problems (institutional SOP)?

### Required Source Documents
- Protocol (safety reporting section and AE definitions)
- Investigator's Brochure (reference safety information / expected AE list)
- SAE reporting forms (sponsor-specific or CIOMS-I form)
- MedDRA coding dictionary (current version)
- CTCAE grading tables (if applicable)
- Site SOPs for AE documentation and reporting
- DSMB charter (if applicable)
- Delegation of Authority Log (who can assess AEs)

---

## Step 1 — Identify and Capture Adverse Events

Define the AE identification process:

### Definitions (per ICH-GCP E6(R2) 1.2)
- **Adverse Event (AE)**: Any untoward medical occurrence in a participant, whether or not considered related to the investigational product
- **Serious Adverse Event (SAE)**: Any AE that results in death, is life-threatening, requires hospitalization or prolongation of existing hospitalization, results in persistent or significant disability/incapacity, is a congenital anomaly/birth defect, or is an important medical event that may jeopardize the participant and require intervention
- **Adverse Drug Reaction (ADR)**: An AE with at least a reasonable possibility of causal relationship to the investigational product
- **Suspected Unexpected Serious Adverse Reaction (SUSAR)**: An ADR that is both serious and not consistent with the applicable product information (IB for investigational products)

### Collection Methods
1. **Spontaneous reporting**: Ask open-ended questions at each visit ("How have you been feeling since your last visit?") — never ask leading questions about specific symptoms unless they are solicited per protocol
2. **Solicited events**: Protocol-specified AEs (e.g., injection-site reactions) collected via diaries, ePRO, or structured assessments at defined timepoints
3. **Laboratory/diagnostic AE detection**: Clinically significant abnormal lab values, ECG findings, or imaging results that the investigator determines are AEs
4. **Inter-visit reporting**: Define how participants report events between visits (24-hour call line, electronic diary, email to coordinator)

---

## Step 2 — Document Adverse Events Completely

For each AE, capture all required data elements per ICH-GCP and 21 CFR 312.32:

1. **Event term**: Verbatim description as reported by investigator (coded to MedDRA Preferred Term and mapped to System Organ Class)
2. **Onset date**: Date and time (if available) of first occurrence
3. **Resolution date**: Date resolved or "ongoing" at last assessment
4. **Severity/grade**: CTCAE grade (1–5) or mild/moderate/severe/life-threatening/fatal per protocol
5. **Seriousness criteria**: Check all that apply (death, life-threatening, hospitalization, disability, congenital anomaly, important medical event)
6. **Causality assessment**: Investigator's assessment of relationship to study drug (see Step 3)
7. **Action taken with study drug**: None, dose reduced, drug interrupted, drug discontinued, not applicable
8. **Outcome**: Recovered/resolved, recovering/resolving, not recovered/not resolved, recovered with sequelae, fatal, unknown
9. **Treatment given**: Yes/No; if yes, describe concomitant medications or procedures
10. **Expectedness**: Expected (listed in IB) or unexpected per reference safety information

---

## Step 3 — Assess Causality

Apply the protocol-specified causality assessment method:

### WHO-UMC System
- **Certain**: Plausible time relationship, cannot be explained by disease or other drugs, response to withdrawal clinically plausible, rechallenge positive
- **Probable/Likely**: Reasonable time relationship, unlikely disease or other drugs, clinically reasonable response to withdrawal
- **Possible**: Reasonable time relationship, could also be explained by disease or other drugs
- **Unlikely**: Improbable time relationship, disease or other drugs provide plausible explanation
- **Conditional/Unclassified**: Event reported but more data needed for assessment
- **Unassessable/Unclassifiable**: Insufficient or contradictory information

### Naranjo Algorithm (alternative)
- 10-question standardized assessment yielding a score: definite (≥9), probable (5-8), possible (1-4), doubtful (≤0)

The investigator must make the causality determination — sponsors may query but cannot downgrade the investigator's assessment.

---

## Step 4 — Apply Regulatory Reporting Timelines

Report within the mandated deadlines based on event classification:

### IND Safety Reports to FDA (21 CFR 312.32)
| Event Type | Timeline | Form |
|------------|----------|------|
| Fatal or life-threatening SUSAR | 7 calendar days (initial) + 8 days (follow-up) | IND Safety Report / MedWatch 3500A |
| All other SUSARs | 15 calendar days | IND Safety Report / MedWatch 3500A |
| Aggregate safety findings (increased rate of expected SAEs) | 15 calendar days | IND Safety Report |

### Sponsor to Investigator Notification
- SUSARs must be communicated to all investigators and IRBs promptly per ICH-GCP 5.17

### Investigator to IRB Reporting
- Unanticipated problems involving risk to participants or others: per institutional policy (typically within 5–10 business days)
- Deaths and life-threatening events: often within 24–48 hours per local SOP
- Annual/continuing review: aggregate safety summary

### EMA Requirements (if applicable)
- Fatal/life-threatening SUSARs: 7 days + 8 days follow-up via EudraVigilance
- All other SUSARs: 15 days via EudraVigilance
- Annual Safety Report (DSUR) per ICH E2F

---

## Step 5 — Process SAE Narratives

Write clinical narratives for all SAEs using the CIOMS format:

1. **Opening sentence**: Age, sex, relevant medical history, study arm (blinded or unblinded as appropriate), event term
2. **Clinical course**: Chronological description — date of onset, presenting symptoms, diagnostic workup, treatments administered, hospitalization details (admission/discharge dates)
3. **Outcome**: Resolution, sequelae, or death with cause
4. **Investigator's causality assessment**: Stated with rationale
5. **Dechallenge/Rechallenge**: Document response to stopping and (if applicable) restarting study drug
6. **Concomitant medications**: List all with start/stop dates
7. **Assessment of expectedness**: Reference specific section of IB

Narratives should be factual, concise (typically 200-500 words), and avoid speculative language.

---

## Step 6 — Maintain the Safety Database

Ensure ongoing data integrity in the safety database:

1. **Coding**: All AEs coded to MedDRA (PT and SOC) by qualified medical coders; coding changes require documentation
2. **Duplicate detection**: Implement algorithms to identify duplicate reports (same participant, same event, reported by different sources)
3. **Follow-up**: Track all open SAEs; request follow-up information from sites at defined intervals; document all attempts to obtain missing information
4. **Reconciliation**: Reconcile AE database with clinical database entries at least quarterly and before database lock
5. **Line listings**: Maintain current SAE line listings for DSMB review and regulatory queries

---

## Checkpoint B — AE Reporting Review

1. [ ] All SAEs have been reported within mandated timelines (7/15 days)
2. [ ] Causality assessments are documented for every AE
3. [ ] MedDRA coding is consistent and uses the correct dictionary version
4. [ ] SAE narratives are complete, factual, and include all CIOMS elements
5. [ ] Expectedness determination references the current IB version
6. [ ] IRB notifications have been filed for all unanticipated problems
7. [ ] DSMB has received updated safety data per charter schedule
8. [ ] Safety database is reconciled with clinical database
9. [ ] All follow-up reports for unresolved SAEs are current
10. [ ] Sponsor safety contact has confirmed receipt of all IND Safety Reports

---

## Quality Audit

- [ ] No SAE report exceeded the 7-day or 15-day reporting deadline
- [ ] All AEs have onset date, severity, causality, outcome, and seriousness documented
- [ ] MedDRA version is consistent across all coded events
- [ ] CTCAE grading is applied correctly (grade 3 = severe, grade 4 = life-threatening, grade 5 = death)
- [ ] No SAE narratives contain speculative causality language
- [ ] Dechallenge/rechallenge information is documented where applicable
- [ ] AE collection period aligns with protocol-defined windows
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. Never delay SAE reporting to gather additional information — submit the initial report within the timeline with available data and follow up
2. The investigator's causality assessment is the final determination — sponsors may disagree but cannot override it
3. Do not code multiple verbatim terms to the same MedDRA PT without clinical justification for combining
4. Severity (CTCAE grade) and seriousness (SAE criteria) are distinct concepts — a grade 3 AE is not automatically an SAE
5. All AEs occurring during the protocol-defined collection period must be captured, including those considered unrelated
6. Pre-existing conditions should be captured as AEs only if they worsen during the study
7. Pregnancy is not an AE but must be reported; pregnancy outcomes (spontaneous abortion, congenital anomaly) are reportable events
8. For blinded studies, expedited unblinding may be required for SUSAR reporting — follow protocol and sponsor procedures
9. Mark any causality assessment that is ambiguous or contested with [VERIFY] for medical-monitor review
10. This skill produces AE documentation — clinical assessment of individual cases requires a qualified physician investigator
