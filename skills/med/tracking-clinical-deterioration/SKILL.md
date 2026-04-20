---
name: tracking-clinical-deterioration
language: en
description: Implements early warning score monitoring (NEWS, MEWS) with escalation criteria. Use when monitoring clinical deterioration, calculating early warning scores, or triggering rapid response criteria.
tags:
  - monitoring
  - hospital-medicine
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Tracking Report
  skill_modes:
    - Monitoring
---

# Tracking Clinical Deterioration

Implements early warning score monitoring (NEWS, MEWS) with escalation criteria for early identification of patients at risk for clinical decompensation.

## Why This Skill Exists

Failure to rescue — the inability to recognize and respond to clinical deterioration before a cardiac arrest or ICU transfer — is a leading cause of preventable inpatient death. Studies show that 60-80% of cardiac arrests on general medical floors are preceded by detectable physiologic deterioration 6-8 hours beforehand. The National Early Warning Score (NEWS2), endorsed by the Royal College of Physicians and adopted widely in US hospitals, provides a standardized aggregate scoring system that outperforms single-parameter triggers for predicting ICU transfer, cardiac arrest, and death within 24 hours.

The Joint Commission requires hospitals to have a mechanism for patients, families, and staff to escalate care concerns (Condition H / Rapid Response). CMS Conditions of Participation mandate ongoing patient assessment with documented escalation protocols. Hospitals that implement structured early warning systems reduce unexpected ICU transfers by 20-30% and in-hospital cardiac arrest rates by 15-25%.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before initiating deterioration tracking, confirm:

1. Which **early warning scoring system** does the institution use — NEWS2, MEWS, or a proprietary system? *(Default: NEWS2)*
2. What is the **vital sign monitoring frequency** — Q4h, Q2h, Q1h, continuous? *(Default: Per acuity level and current orders)*
3. What are the institution's **escalation thresholds** and corresponding actions? *(Default: See NEWS2 escalation protocol below)*
4. Does the patient have **baseline abnormalities** that affect scoring — chronic hypoxia (COPD on home O2), baseline tachycardia (autonomic dysfunction), chronic hypotension? *(Default: Document baselines to prevent alarm fatigue)*
5. Is there a **rapid response team (RRT)** or **medical emergency team (MET)** available? *(Default: 24/7 coverage required)*
6. What is the patient's **code status** — does it affect the escalation pathway? *(Default: Full code escalation; modified for DNR/CMO)*
7. Has the patient had any **sentinel events** in the past 24 hours — falls, medication errors, procedures, new symptom onset? *(Default: Review event log)*

### Documents to Request

- Vital sign flowsheet with 24-48 hour trends
- Current NEWS2 or MEWS scores (if auto-calculated by EMR)
- Medication administration record (sedatives, antihypertensives, opioids that affect vitals)
- Recent lab results (lactate, WBC, creatinine, troponin)
- Active problem list with baseline physiologic parameters
- Code status documentation
- Prior rapid response or code blue records (if applicable)

---

## Step 1: Calculate the NEWS2 Score

The National Early Warning Score 2 uses seven physiologic parameters:

| Parameter | 3 | 2 | 1 | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|---|---|---|
| **RR** (breaths/min) | ≤8 | — | 9-11 | 12-20 | — | 21-24 | ≥25 |
| **SpO2 Scale 1** (%) | ≤91 | 92-93 | 94-95 | ≥96 | — | — | — |
| **SpO2 Scale 2** (%) | ≤83 | 84-85 | 86-87 | 88-92 (on air) or ≥93 (on O2) | 93-94 (on O2) | 95-96 (on O2) | ≥97 (on O2) |
| **Supplemental O2** | — | — | Yes | No | — | — | — |
| **SBP** (mmHg) | ≤90 | 91-100 | 101-110 | 111-219 | — | — | ≥220 |
| **HR** (bpm) | ≤40 | — | 41-50 | 51-90 | 91-110 | 111-130 | ≥131 |
| **Consciousness** | — | — | — | Alert | — | — | V, P, or U |
| **Temperature** (°C) | ≤35.0 | — | 35.1-36.0 | 36.1-38.0 | 38.1-39.0 | ≥39.1 | — |

**SpO2 Scale 2** is used for patients with hypercapnic respiratory failure (e.g., COPD with target SpO2 88-92%).

**Total score range: 0-20**

---

## Step 2: Apply Escalation Protocols Based on Score

| NEWS2 Score | Risk Level | Clinical Response |
|-------------|------------|-------------------|
| **0-4** | Low | Continue routine monitoring Q4-6h |
| **3 in any single parameter** | Low-Medium | Urgent bedside assessment by RN; notify physician within 1 hour |
| **5-6** | Medium | Increase monitoring to Q1h; physician assessment within 1 hour; consider ICU outreach |
| **≥7** | High | Emergency response — physician at bedside immediately; consider RRT activation; continuous monitoring; ICU assessment |

**Rapid Response Team (RRT) activation criteria** (in addition to NEWS2 ≥ 7):
- Acute change in mental status (new confusion, lethargy, agitation)
- Respiratory distress not responsive to current oxygen delivery
- New-onset chest pain with hemodynamic changes
- Systolic BP < 80 mmHg despite fluid resuscitation
- Urine output < 0.5 mL/kg/hr for > 4 hours
- Staff or family "worried" about patient (gut instinct criterion)

---

## Step 3: Document Deterioration Events

When clinical deterioration is identified, document the following:

```
CLINICAL DETERIORATION NOTE

Date/Time of recognition: [Timestamp]
NEWS2 Score: [Score] (prior score [X] at [time] — change of [+/-Y])
Triggering parameters: [List specific abnormal vitals]

Assessment:
- Clinical presentation: [Describe current status]
- Likely etiology: [Differential for deterioration — sepsis, PE, ACS, 
  hemorrhage, respiratory failure, medication effect]
- Interventions initiated: [Specific actions taken]

Escalation:
- RRT activated: Yes/No — if no, document rationale
- ICU consulted: Yes/No
- Attending notified: Yes/No — time and method
- Family notified: Yes/No (per patient preference)

Orders placed:
- [List new orders — labs, imaging, medications, monitoring changes]

Plan:
- Continue monitoring at [frequency]
- Reassess in [timeframe]
- Escalation threshold for next action: [Specific parameter]
```

---

## Step 4: Prevent Failure to Rescue

Implement these proactive monitoring strategies:

**High-risk populations requiring enhanced monitoring:**
- Post-procedure patients (first 24 hours)
- Patients on opioid PCA or IV opioids (respiratory depression risk)
- Patients with new or escalating oxygen requirements
- Patients transferred from ICU within 48 hours ("ICU bounce-back" risk)
- Patients receiving blood products (transfusion reactions)
- Patients with sepsis or suspected infection on antibiotics < 48 hours
- Patients with active GI bleeding

**Afferent limb optimization** (detection):
- Ensure vital signs are taken at ordered frequency — audit compliance
- Use continuous pulse oximetry for high-risk patients
- Implement capnography monitoring for patients on opioid infusions
- Encourage nursing to escalate "gut feeling" concerns without objective threshold

**Efferent limb optimization** (response):
- RRT must arrive at bedside within 5 minutes of activation
- Pre-built order sets for common deterioration scenarios (sepsis bundle, STEMI protocol, stroke code)
- ICU bed availability confirmed within 30 minutes of transfer decision

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After any deterioration event or monitoring review:

1. Is the **NEWS2 score** accurately calculated and documented?
2. Was the **escalation protocol** followed for the score level?
3. Are **new orders** and **monitoring frequency changes** in place?
4. Has the **attending** been notified of all Medium and High risk scores?
5. Is there a **reassessment plan** with specific timeline and parameters?

---

## Quality Audit

- [ ] NEWS2 score is calculated at every vital sign assessment
- [ ] Baseline abnormalities are documented to contextualize scoring
- [ ] Escalation protocol matches the score level
- [ ] RRT activation criteria are posted and accessible to nursing staff
- [ ] Deterioration events are documented with the structured note template
- [ ] Time from recognition to physician assessment is within protocol limits
- [ ] ICU transfer decision time is documented
- [ ] Code status is confirmed before escalation actions
- [ ] Medication effects on vitals are considered (beta-blockers, opioids, sedatives)
- [ ] Post-deterioration debrief is conducted for RRT activations
- [ ] Score trending is documented (not just current score, but trajectory)
- [ ] Family/patient notification occurs per preference documentation
- [ ] High-risk populations have enhanced monitoring orders in place

---

## Guidelines

- Trending is more important than absolute values — a NEWS2 score of 4 that was 1 yesterday is more concerning than a stable 4
- Never dismiss single-parameter scores of 3 — these are clinically significant even if the total score is low
- Baseline documentation prevents alarm fatigue — a COPD patient with chronic SpO2 of 90% should not trigger the same response as a previously healthy patient
- Respiratory rate is the most sensitive early indicator of deterioration and the most commonly inaccurately measured vital sign — encourage actual counting for 60 seconds
- Family and nursing concern ("something is wrong") should be treated as a valid escalation trigger per The Joint Commission Condition H standards
- Document the clinical reasoning for NOT escalating when a score would otherwise trigger action (e.g., "NEWS2 = 5 due to chronic baseline tachycardia; patient at clinical baseline per nursing assessment")
- After every RRT activation, conduct a brief debrief: Was escalation timely? Were there earlier signs that were missed?
- Patients transferred from ICU should have enhanced monitoring (Q2h vitals minimum) for the first 24-48 hours on the floor
