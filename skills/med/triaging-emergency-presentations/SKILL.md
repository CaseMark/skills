---
name: triaging-emergency-presentations
description: Applies ESI triage methodology to assign acuity levels based on presenting complaints, vital signs, and resource needs. Use when triaging ED patients, assigning acuity scores, or prioritizing emergency cases.
tags:
  - emergency-medicine
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
  document_types:
    - Report
  skill_modes:
    - Analysis
---

# Triaging Emergency Presentations

Applies the Emergency Severity Index (ESI) triage methodology to assign acuity levels based on presenting complaints, vital signs, and anticipated resource needs.

## Why This Skill Exists

Triage errors in the emergency department are a leading contributor to adverse patient outcomes. Studies show that undertriage occurs in 5-10% of ED visits and is associated with a 2-4x increase in mortality for patients who should have been assigned a higher acuity level. The Emergency Severity Index (ESI), now in version 4, is the most widely adopted triage algorithm in the United States and is endorsed by the American College of Emergency Physicians (ACEP) and the Emergency Nurses Association (ENA).

Accurate triage determines not only patient placement and timing of physician evaluation but also drives resource allocation, staffing decisions, and CMS quality metrics. The Joint Commission requires documented triage assessments, and incorrect acuity assignment can trigger compliance findings. This skill ensures consistent, defensible triage documentation that aligns with ESI v4 methodology and supports both clinical decision-making and regulatory requirements.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the patient's chief complaint in their own words? (Default: document verbatim)
2. What are the initial vital signs including HR, BP, RR, SpO2, and temperature? (Default: all values required)
3. Is the patient arriving by EMS with prehospital report available? (Default: yes if EMS transport)
4. What is the patient's age? (Default: document exact age; flag if pediatric <14 or geriatric >65)
5. Are there any known allergies or current medications? (Default: query and document)
6. What is the pain score using age-appropriate scale (NRS, Wong-Baker, FLACC)? (Default: NRS 0-10 for adults)
7. Is the patient a trauma activation based on field criteria? (Default: apply local trauma activation criteria)
8. What is the patient's mental status using AVPU or GCS? (Default: AVPU for triage, GCS if altered)

### Documents to Request

- EMS prehospital care report (PCR) or run sheet
- Transfer paperwork if arriving from another facility
- Previous ED visit records within 72 hours (bounce-back screening)
- Current medication list or pharmacy printout
- Advance directives or POLST if applicable
- Insurance and demographic information for registration

---

## Step 1: Immediate Life-Threat Screening (ESI Level 1)

Before applying the full ESI algorithm, screen for immediate life threats requiring resuscitative intervention.

**ESI Level 1 criteria (any one present):**

| Criterion | Examples |
|-----------|----------|
| Unresponsive | GCS ≤8, no purposeful movements |
| Pulseless / apneic | Cardiac arrest, respiratory arrest |
| Intubated / active resuscitation | Arrived on BVM, active CPR |
| Severe hemodynamic instability | SBP <80 with AMS, active massive hemorrhage |
| Acute overdose with obtundation | GCS <12, respiratory depression |

If any Level 1 criterion is met, assign ESI-1 immediately and activate the resuscitation team. Do not proceed further in the algorithm.

---

## Step 2: High-Risk Situation Screening (ESI Level 2)

If the patient is not ESI-1, evaluate for high-risk situations that require rapid physician evaluation.

**ESI Level 2 criteria — answer these three decision points:**

1. **Should this patient not wait?** Conditions where delay causes irreversible harm:
   - Acute chest pain concerning for ACS (use HEART score screening)
   - Stroke symptoms within 24 hours (activate stroke alert)
   - Acute respiratory distress (SpO2 <90%, tripoding, accessory muscle use)
   - Severe sepsis signs (fever + tachycardia + hypotension or AMS)
   - Active suicidal ideation with plan or means

2. **Is there new-onset confusion, lethargy, or disorientation?** Any acute change in mental status = ESI-2.

3. **Is the patient in severe distress?** Clinical judgment of severe pain (NRS ≥8) or severe emotional distress requiring immediate intervention.

**Vital sign danger zone flags (auto-trigger ESI-2):**

| Vital Sign | Adult Danger Zone |
|------------|-------------------|
| HR | <50 or >130 |
| SBP | <90 or >200 |
| RR | <10 or >30 |
| SpO2 | <92% on room air |
| Temp | >104°F (40°C) or <95°F (35°C) |

---

## Step 3: Resource Prediction (ESI Levels 3-5)

For patients who are not ESI-1 or ESI-2, predict the number of ED resources needed.

**Resource counting rules (per ESI v4 Handbook):**

Resources that COUNT (each = 1 resource):
- Labs (all blood draws = 1 resource regardless of number of tests)
- ECG
- Imaging (each modality = 1: X-ray = 1, CT = 1, ultrasound = 1)
- IV fluids (bolus or continuous)
- IV/IM medications (each separate administration)
- Specialty consultation
- Simple procedure (laceration repair, splinting, I&D)
- Complex procedure (conscious sedation, LP)

Resources that DO NOT count:
- History and physical examination
- Point-of-care glucose
- Saline lock placement
- Tetanus immunization
- Prescription refills
- Simple wound care (bandaging only)
- Oral medications

**Assignment table:**

| Predicted Resources | ESI Level | Typical Examples |
|--------------------:|-----------|-----------------|
| ≥2 | ESI-3 | Abdominal pain needing labs + CT; chest pain needing ECG + troponin + CXR |
| 1 | ESI-4 | Simple laceration repair; single X-ray for ankle injury |
| 0 | ESI-5 | Prescription refill; suture removal; medication recheck |

**Vital sign check for ESI-3:** After assigning ESI-3, re-check vital signs against danger zone criteria. If vital signs fall in danger zone, uptriage to ESI-2.

---

## Step 4: Special Population Modifications

### Pediatric Triage Adjustments
- Use age-adjusted vital sign norms (pediatric vital sign reference table)
- Fever in neonates <28 days = automatic ESI-2 regardless of appearance
- Pediatric Assessment Triangle (PAT): Appearance, Work of Breathing, Circulation to Skin
- Non-verbal children: use FLACC pain scale rather than NRS

### Geriatric Triage Adjustments
- Elderly patients often present with blunted vital sign responses; maintain lower threshold for ESI-2
- Falls in patients on anticoagulants = ESI-2 if head strike or any neurologic complaint
- Sepsis in elderly may present as confusion alone without fever or tachycardia

### Obstetric Triage Adjustments
- Pregnant patients >20 weeks with abdominal pain or vaginal bleeding = ESI-2
- Apply obstetric triage acuity scale (OTAS) in conjunction with ESI when available
- Vital sign norms differ in pregnancy (physiologic tachycardia, lower BP in 2nd trimester)

---

## Step 5: Documentation and Reassessment

### Required Triage Documentation Elements
- Date and time of triage (must be within minutes of arrival)
- Triage nurse name and credentials
- Chief complaint in patient's words
- Mechanism of injury (if trauma)
- Complete vital signs set
- Pain assessment with score
- AVPU or GCS mental status
- ESI acuity level assigned with brief rationale
- Allergies, medications, and pertinent medical history
- Isolation or infection control precautions triggered
- Reassessment intervals initiated

### Reassessment Intervals by ESI Level

| ESI Level | Reassessment Interval | Scope |
|-----------|----------------------|-------|
| ESI-1 | Continuous | Full vital signs + neuro checks |
| ESI-2 | Every 15-30 min | Vital signs + chief complaint status |
| ESI-3 | Every 60 min | Vital signs + pain reassessment |
| ESI-4 | Every 120 min | Brief check-in, vital signs PRN |
| ESI-5 | Every 120 min | Brief check-in |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Does the assigned ESI level match the clinical presentation when cross-referenced with the ESI v4 algorithm decision tree?
2. Were vital sign danger zones evaluated and documented, including pediatric age-adjusted norms if applicable?
3. Is the resource prediction count accurate and consistent with the documented workup plan?
4. Were special population modifiers (pediatric, geriatric, obstetric, psychiatric) applied where relevant?
5. Is the reassessment interval assigned and documented per facility protocol?

---

## Quality Audit

- [ ] Chief complaint documented in patient's own words
- [ ] Complete vital signs recorded (HR, BP, RR, SpO2, Temp) at triage time
- [ ] ESI level (1-5) explicitly assigned with rationale
- [ ] Mental status assessed and documented (AVPU or GCS)
- [ ] Pain score assessed using age-appropriate scale
- [ ] Life-threat screening (ESI-1 criteria) documented as evaluated
- [ ] High-risk screening (ESI-2 criteria) documented as evaluated
- [ ] Resource prediction documented for ESI-3/4/5 assignments
- [ ] Vital sign danger zone check performed for ESI-3 patients
- [ ] Allergies and current medications queried and documented
- [ ] Special population modifiers applied if applicable
- [ ] Reassessment interval assigned per ESI level
- [ ] Isolation or infection control screening completed
- [ ] Triage time stamp is within departmental standards (typically <5 min from arrival)

---

## Guidelines

1. Never assign ESI-5 to a patient who has not had vital signs assessed — vital sign omission is the most common triage documentation deficiency cited in Joint Commission surveys.
2. When in doubt between two acuity levels, always assign the higher acuity (lower number) — uptriage is clinically safer and more defensible than undertriage.
3. Document the specific clinical reasoning for ESI-2 assignments using the three decision-point framework: "should not wait," "acute AMS," or "severe distress."
4. Reassessment must be documented even for patients who are seen quickly — the interval begins at triage, not at physician evaluation.
5. Psychiatric patients with suicidal ideation and a plan or access to means are always ESI-2; do not downgrade based on stable vital signs.
6. Track and report undertriage rates as a quality metric — ACEP recommends undertriage rates below 5% as a departmental benchmark.
7. ESI is a snapshot at time of triage; patients may require re-triage if clinical status changes significantly while waiting.
8. Maintain inter-rater reliability by conducting quarterly triage calibration exercises using standardized case scenarios from the ESI v4 Implementation Handbook.
