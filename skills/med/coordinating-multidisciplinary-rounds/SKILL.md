---
name: coordinating-multidisciplinary-rounds
description: Synthesizes input from nursing, pharmacy, PT/OT, social work, and case management into unified care plans. Use when conducting interdisciplinary rounds, coordinating care teams, or documenting team-based decisions.
tags:
  - coordination
  - hospital-medicine
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Coordination Plan
  skill_modes:
    - Coordination
---

# Coordinating Multidisciplinary Rounds

Synthesizes input from nursing, pharmacy, PT/OT, social work, and case management into unified care plans for hospitalized patients.

## Why This Skill Exists

Multidisciplinary rounds (MDR) are the primary mechanism for team-based care coordination in the inpatient setting. The Joint Commission standards for patient-centered care (PC.02.02.01) require interdisciplinary planning, and CMS expects documented evidence that care plans reflect input from multiple disciplines. Studies show that structured MDR reduce length of stay by 0.5-1.5 days, decrease 30-day readmission rates by 15-20%, and improve patient satisfaction scores.

Without a structured approach, MDR devolve into passive listening sessions where information is shared but not synthesized into actionable plans. Effective MDR require a hospitalist-led framework that assigns accountability, sets deadlines, and documents team consensus. The most common failure mode is lack of follow-through — decisions made during rounds that are never translated into orders, referrals, or discharge actions.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before conducting multidisciplinary rounds, confirm:

1. Which **team members** will participate — nursing, pharmacy, PT/OT, social work, case management, dietary, chaplaincy? *(Default: Core team = RN, pharmacist, CM, SW)*
2. What is the **patient census** and how many patients require MDR discussion? *(Default: All patients on service; prioritize those with LOS > geometric mean or discharge barriers)*
3. What is the **time allotment** per patient? *(Default: 2-4 minutes per patient)*
4. Are there **high-priority patients** requiring extended discussion — complex discharges, family conflicts, clinical deterioration? *(Default: Flag by case management or nursing pre-round)*
5. Is there a **standardized rounding template** in use at this facility? *(Default: Use the framework below)*
6. What **day of stay** is each patient on, relative to expected LOS? *(Default: Calculate from admission date vs. CMS geometric mean for MS-DRG)*

### Documents to Request

- Patient census list with admission dates, diagnoses, and attending assignment
- Case management tracking board (discharge disposition, barriers, target dates)
- Pharmacy medication reconciliation reports and therapeutic monitoring alerts
- PT/OT functional status assessments and mobility scores
- Social work psychosocial screening results
- Nursing care plan with active safety concerns (falls, skin, lines)
- Dietary/nutrition screening results (MUST or NRS-2002 scores)

---

## Step 1: Structure the Rounding Format

Use the following per-patient framework (target 3 minutes per patient):

| Time | Speaker | Content |
|------|---------|---------|
| 0:00-0:30 | **Physician** | One-liner, clinical trajectory (improving/stable/worsening), anticipated discharge date |
| 0:30-1:00 | **Nursing** | Overnight events, patient concerns, safety issues (falls, skin, pain control) |
| 1:00-1:30 | **Pharmacy** | Medication concerns: interactions, renal dosing, IV-to-PO conversion, antibiotic stewardship |
| 1:30-2:00 | **Case Management** | Insurance status, discharge disposition (home, SNF, LTACH, rehab), pending authorizations |
| 2:00-2:30 | **Social Work** | Psychosocial barriers, caregiver assessment, community resource needs |
| 2:30-3:00 | **PT/OT** | Functional status, mobility level, equipment needs, therapy recommendations |

---

## Step 2: Assign Accountability for Action Items

Every MDR discussion must produce documented action items with ownership:

**Action Item Template:**
```
Action: [Specific task]
Owner: [Name and discipline]
Deadline: [Date/time or "by discharge"]
Status: [Not started / In progress / Complete / Blocked — reason]
```

**Common action categories:**
- **Physician actions**: Order changes, consult requests, goals-of-care discussions, procedure scheduling
- **Nursing actions**: Patient education, safety interventions, care coordination with family
- **Pharmacy actions**: Medication optimization, discharge medication reconciliation, prior authorization for specialty drugs
- **Case management actions**: Insurance authorization, facility placement, DME ordering, home health referral
- **Social work actions**: Psychosocial assessment completion, community resource connection, guardianship or capacity evaluation
- **PT/OT actions**: Functional assessments, equipment recommendations, home safety evaluation

---

## Step 3: Address Discharge Barriers Systematically

For each patient with LOS approaching or exceeding the geometric mean, identify and categorize barriers:

| Barrier Category | Examples | Responsible Discipline |
|-----------------|----------|----------------------|
| **Clinical** | Pending procedure, IV antibiotics, unstable vitals | Physician |
| **Functional** | Not meeting therapy goals, unsafe mobility | PT/OT |
| **Social** | No caregiver, homeless, unsafe home environment | Social work |
| **Insurance/Authorization** | Pending SNF authorization, denied rehab | Case management |
| **Patient/Family** | Refusing discharge, unrealistic expectations, family conflict | Team (physician-led) |
| **Medication** | Prior authorization needed, patient cannot afford discharge meds | Pharmacy |
| **Equipment** | Home O2, hospital bed, wheelchair not yet arranged | Case management |

---

## Step 4: Document Team Consensus

After each patient discussion, document the following in the EMR:

1. **Interdisciplinary care plan update**: Summary of team input and agreed-upon plan
2. **Discharge readiness assessment**: Ready / Not ready — with specific unmet criteria
3. **Estimated discharge date**: Confirmed or revised based on MDR discussion
4. **Escalation needs**: Any issue requiring attending-to-attending communication, ethics consultation, or administrative intervention
5. **Patient/family communication plan**: Who will discuss what, and when

---

## Step 5: Track Metrics and Process Quality

Monitor the following MDR effectiveness metrics:

- **Attendance rate**: % of core team members present (target >= 90%)
- **Action item completion rate**: % of assigned actions completed by deadline (target >= 85%)
- **LOS vs. geometric mean**: Track daily for each patient; flag outliers
- **Discharge before noon rate**: Percentage of discharges completed by 12:00 PM (target >= 30%)
- **Readmission rate**: 30-day all-cause readmission for patients who went through MDR

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After completing multidisciplinary rounds:

1. Does every patient have a documented **estimated discharge date**?
2. Are all **action items** assigned to a specific owner with a deadline?
3. Have **discharge barriers** been categorized and assigned for resolution?
4. Were any patients identified as needing **escalation** to attending, ethics, or administration?
5. Is the MDR documentation in the EMR and accessible to all team members?

---

## Quality Audit

- [ ] All core disciplines participated or sent a representative
- [ ] Each patient was discussed using the structured format
- [ ] Estimated discharge date is documented for every patient
- [ ] Active discharge barriers are identified and assigned
- [ ] Medication reconciliation status is addressed for patients within 24h of discharge
- [ ] Functional status and therapy goals are documented
- [ ] Insurance and authorization status is current
- [ ] Patient/family communication needs are identified
- [ ] Action items have named owners and deadlines
- [ ] High-priority patients received extended discussion time
- [ ] Documentation is completed within 2 hours of rounds
- [ ] LOS outliers are escalated with barrier analysis

---

## Guidelines

- Hospitalist leads and time-keeps — do not allow single-discipline monologues exceeding their allotted time
- Start with patients closest to discharge to capture early-morning discharge opportunities
- Flag any patient on hospital day 3+ without a clear discharge plan for focused barrier analysis
- Pharmacy should address antibiotic stewardship at every MDR — review indication, duration, and IV-to-PO conversion eligibility
- Case management should present insurance status proactively, not reactively when discharge is imminent
- Document MDR decisions as team consensus, not individual opinions — this is legally significant
- When team members disagree on discharge readiness, document the disagreement and the resolution
- Use a visual tracking board (whiteboard or EMR dashboard) that is updated in real-time during rounds
