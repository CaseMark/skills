---
name: coding-behavioral-health-services
language: en
description: Assigns behavioral health procedure codes with time-based requirements and modifier application. Use when coding therapy sessions, applying psychiatric codes, or documenting behavioral health services.
tags:
  - coding
  - medical-coding-and-billing
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Coded Record
  skill_modes:
    - Coding
    - Classification
---

# Coding Behavioral Health Services

Assigns behavioral health procedure codes for psychiatric evaluations, psychotherapy, psychological testing, substance use disorder treatment, and crisis intervention services. Covers time-based code selection, add-on psychotherapy with E/M, provider credential-based modifier application, and payer-specific behavioral health coverage rules.

## Why This Skill Exists

Behavioral health coding has unique complexities: most services are time-based (requiring precise time documentation), multiple service types can occur in a single encounter (E/M + psychotherapy), provider credential requirements vary by payer and state, and the Mental Health Parity Act creates coverage obligations that differ from medical/surgical benefits. Common errors include incorrect time-range selection, failure to use add-on psychotherapy codes when E/M is also billed, missing crisis code documentation, and applying incorrect provider modifiers. Behavioral health claim denial rates are 15–20% higher than medical claims.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What type of behavioral health service was provided? (evaluation, psychotherapy, testing, crisis intervention, medication management)
2. What is the provider's credential? (MD/DO psychiatrist, PhD psychologist, LCSW, LPC, LMFT, NP)
3. What is the face-to-face time documented for the session?
4. Was an E/M service performed in addition to psychotherapy?
5. Is the patient new or established?
6. What is the service setting? (office, hospital outpatient, inpatient, partial hospitalization, telehealth)
7. What payer covers the service and are there specific behavioral health carve-out rules?

### Documents Required

- Complete encounter/session note with presenting problem, interventions, patient response, and plan
- Time documentation (start time, end time, total face-to-face time)
- Treatment plan with goals, objectives, and interventions
- Diagnostic assessment or psychiatric evaluation (for initial visits)
- Psychological testing raw data and interpretation report (for testing services)
- Provider credentials and licensure documentation
- Prior authorization documentation (if applicable)

---

## Step 1 — Code Psychiatric Diagnostic Evaluations

Select the appropriate evaluation code for initial assessments.

- **90791 — Psychiatric diagnostic evaluation**: Comprehensive assessment including history, mental status exam, and treatment recommendations. No medical services. Typically 45–60 minutes but not time-based — report regardless of time spent.
- **90792 — Psychiatric diagnostic evaluation with medical services**: Same as 90791 but includes medical assessment, medication review, and physical exam components. Reported by physicians (MD/DO) or qualified NPPs who can prescribe.
- These codes are used for initial evaluations — not for follow-up visits or ongoing treatment.
- Multiple sessions for a comprehensive evaluation are permitted (report 90791/90792 for each session with documentation justifying the need for multiple evaluation sessions).
- Do NOT bill 90791/90792 with same-day psychotherapy or E/M codes — the evaluation includes the therapeutic interaction on that date.

## Step 2 — Code Psychotherapy Services (Time-Based)

Select psychotherapy codes based on face-to-face time with the patient.

**Standalone psychotherapy (when no E/M is billed):**
- **90832**: 16–37 minutes of psychotherapy
- **90834**: 38–52 minutes of psychotherapy
- **90837**: 53+ minutes of psychotherapy

**Add-on psychotherapy with E/M (when E/M is also billed):**
- **+90833**: 16–37 minutes of psychotherapy, reported with E/M code
- **+90836**: 38–52 minutes of psychotherapy, reported with E/M code
- **+90838**: 53+ minutes of psychotherapy, reported with E/M code

**Key rules:**
- Time refers to face-to-face psychotherapy time with the patient (and/or family member), not total encounter time.
- Time spent on E/M activities (medication review, physical exam) is NOT counted toward psychotherapy time.
- Document start time, end time, and activities for both E/M and psychotherapy components when billing both.
- The add-on codes (+90833, +90836, +90838) can ONLY be reported with an E/M code — they cannot stand alone.
- If total psychotherapy time is less than 16 minutes, it is not separately reportable — it is included in the E/M service.

## Step 3 — Code Medication Management and E/M

Apply E/M coding rules when medication management is the primary service.

- There is no standalone "medication management" CPT code — medication management is coded as an E/M service (99202–99215 for office, 99221–99233 for inpatient).
- Apply 2021+ E/M guidelines: MDM or time determines code level.
- For psychiatric medication management, MDM typically involves: prescription drug management requiring monitoring for toxicity (moderate risk), number of medications managed, complexity of medication interactions.
- When psychotherapy is also provided in the same encounter: bill the E/M code + add-on psychotherapy code (+90833/+90836/+90838).
- Time for E/M activities (reviewing records, discussing medications, coordinating care) is separate from psychotherapy time.

## Step 4 — Code Psychological and Neuropsychological Testing

Apply testing code structure for assessment services.

- **96130**: Psychological testing evaluation by psychologist, first hour (includes interpretation and report).
- **+96131**: Each additional hour of psychological testing evaluation.
- **96136**: Psychological testing administration by psychologist, first 30 minutes.
- **+96137**: Each additional 30 minutes of administration by psychologist.
- **96138**: Psychological testing administration by technician, first 30 minutes.
- **+96139**: Each additional 30 minutes by technician.
- **96132/+96133**: Neuropsychological testing evaluation, first hour and additional hours.
- **96146**: Computer-based psychological testing, automated interpretation.

**Key rules:**
- Evaluation codes (96130–96133) cover the psychologist's time reviewing results, integrating data, interpreting findings, and writing the report.
- Administration codes (96136–96139) cover the time spent administering tests face-to-face.
- Document each test administered, time per test, and administering provider.
- The report must document specific tests used, raw scores, standard scores, interpretation, and clinical recommendations.

## Step 5 — Code Crisis Intervention and Intensive Services

Apply codes for acute behavioral health emergencies.

- **90839**: Psychotherapy for crisis, first 60 minutes. The crisis must involve a life-threatening or highly complex psychiatric emergency.
- **+90840**: Each additional 30 minutes of crisis psychotherapy beyond the first 60 minutes.
- **Crisis documentation requirements**: Document the nature of the crisis, imminent danger assessment (suicidal ideation, homicidal ideation, psychotic decompensation), interventions performed, and disposition/safety plan.
- Crisis codes are not routine therapy sessions — they require documentation of an acute psychiatric emergency.
- **H0034–H0037 (HCPCS)**: Community-based behavioral health services, including medication training, mental health assessment, and community psychiatric support. Used primarily by Medicaid-funded programs.
- **Intensive Outpatient Program (IOP)**: Typically billed with revenue codes and HCPCS codes (S9480 for IOP per diem). Requirements vary by payer.
- **Partial Hospitalization Program (PHP)**: Revenue code 0912/0913 with appropriate procedure codes. Must meet CMS criteria for partial hospitalization.

## Step 6 — Apply Provider and Service Modifiers

Select modifiers based on provider credentials and service circumstances.

- **Modifier HO**: Services provided by a master's-level clinician (LCSW, LPC, LMFT). Required by some Medicaid programs.
- **Modifier HN**: Services provided by a bachelor's-level clinician. Some payers require this for behavioral health technicians.
- **Modifier 95**: Synchronous telehealth service via real-time audio/video. Apply when behavioral health services are delivered via telehealth platform.
- **Modifier GT**: Telehealth via interactive audio/video (some payers use GT instead of 95).
- **Modifier 52**: Reduced services — when a therapy session ends early (e.g., patient unable to tolerate full session but minimum time threshold is met).
- **Modifier 25**: Significant, separately identifiable E/M on same day as a procedure (e.g., E/M + psychotherapy on same day when billed with standalone psychotherapy code instead of add-on).
- **Place of Service (POS)**: 11 (office), 02 (telehealth in patient's home), 10 (telehealth in healthcare facility), 22 (hospital outpatient), 52 (psychiatric facility), 53 (community mental health center).

---

## Checkpoint B — Review

- [ ] Psychotherapy code matches documented face-to-face time (not total encounter time)
- [ ] Add-on psychotherapy codes are paired with an E/M code — never reported standalone
- [ ] E/M time and psychotherapy time are documented separately and do not overlap
- [ ] Provider credential matches the code billed and payer requirements for that credential
- [ ] Crisis codes are supported by documentation of an acute psychiatric emergency
- [ ] Testing codes distinguish between evaluation (interpretation) and administration time
- [ ] Place of service is correct for the encounter setting
- [ ] ICD-10-CM behavioral health diagnoses are coded to maximum specificity (e.g., F33.1 major depressive disorder recurrent moderate, not F32.9 unspecified)

---

## Quality Audit

- [ ] Time documentation is internally consistent (start/end times match reported time ranges)
- [ ] Add-on psychotherapy frequency is proportionate to E/M visit volume (not every E/M has add-on therapy)
- [ ] Crisis code usage is reserved for genuine emergencies — not routine therapy sessions
- [ ] Provider credentialing is verified for each billing provider — state licensure + payer credentialing
- [ ] Treatment plan updates support ongoing medical necessity for continued therapy sessions
- [ ] Session notes document specific interventions used (CBT, DBT, motivational interviewing) — not just "supportive therapy"
- [ ] Prior authorization requirements are met for services that require them (testing, intensive programs)

---

## Guidelines

- Follow AMA CPT guidelines for Psychiatry section (90785–90899) and E/M section for medication management
- Apply CMS Medicare Claims Processing Manual Chapter 12 §180 for psychiatric services billing
- Reference APA Practice Guidelines for evidence-based treatment standards
- Follow state-specific scope of practice rules for non-physician behavioral health providers
- Apply Mental Health Parity and Addiction Equity Act (MHPAEA) requirements for coverage parity
- Never bill psychotherapy time that exceeds the documented face-to-face time with the patient
- Mark with [VERIFY] any session where time documentation is missing or ambiguous
- Include disclaimer that behavioral health coding rules vary significantly by payer and state licensing requirements
