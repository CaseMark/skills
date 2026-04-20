---
name: coordinating-surgical-scheduling
language: en
description: Manages surgical scheduling with block time utilization, equipment needs, and team coordination. Use when scheduling surgeries, managing OR block time, or coordinating surgical resources.
tags:
  - coordination
  - surgery
  - surgical
metadata:
  author: casemark
  practice_areas:
    - General Surgery
    - Surgical Subspecialties
  document_types:
    - Coordination Plan
  skill_modes:
    - Coordination
---

# Coordinating Surgical Scheduling

Manages surgical scheduling with block time utilization, equipment needs, and team coordination.

## Why This Skill Exists

Operating room time is the most expensive resource in a hospital, costing $30-100 per minute depending on the institution and service. Efficient surgical scheduling directly impacts institutional revenue, patient access to care, surgeon satisfaction, and staff workload. ACS and AORN guidelines emphasize that OR utilization rates between 75-85% represent optimal efficiency — below 75% indicates wasted capacity, while above 85% leads to overtime, staff burnout, and case cancellations.

Same-day surgical cancellations cost institutions $1,500-$5,000 per cancelled case and delay patient care. Common preventable causes include incomplete preoperative workup, missing clearances, equipment unavailability, and scheduling conflicts. This skill standardizes the surgical scheduling workflow from case request through OR assignment, ensuring all prerequisites are verified, resources are allocated, and the OR schedule maximizes utilization while maintaining safety margins.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What procedure(s) need to be scheduled and by which surgeon? **Default: [VERIFY]**
2. What is the urgency classification (elective, urgent, emergent)? **Default: elective**
3. What is the estimated case duration (surgeon time + anesthesia setup/recovery)? **Default: [VERIFY — obtain from surgeon or historical data]**
4. Does the case require specialized equipment (robot, C-arm, microscope, cell saver, neuromonitoring)? **Default: standard equipment**
5. Does the patient have specific anesthesia requirements (general, regional, MAC)? **Default: general**
6. Is the patient's preoperative workup complete (H&P, labs, clearances, consent)? **Default: [VERIFY]**
7. Are there case-sequencing requirements (e.g., patient must be first case due to latex allergy, infection isolation)? **Default: no**
8. What is the insurance authorization status? **Default: [VERIFY]**

### Documents to Request

- Surgeon's case request form with procedure, CPT codes, and estimated duration
- Patient demographics and insurance information
- Prior authorization or pre-certification documentation
- Preoperative checklist status (H&P, labs, consent, clearances)
- Equipment and implant request list
- Anesthesia pre-assessment or pre-screening documentation
- Historical case duration data for the procedure and surgeon

---

## Step 1: Case Urgency Classification and Prioritization

Classify surgical urgency using the NCEPOD framework adapted for scheduling:

| Classification | Definition | Scheduling Timeline | Example |
|---|---|---|---|
| **Immediate (Emergency)** | Life, limb, or organ threatening; resuscitation simultaneous with surgery | Within minutes | Ruptured AAA, acute hemorrhage, peritonitis |
| **Urgent** | Rapid deterioration expected; time-sensitive condition | Within 24 hours | Acute appendicitis, incarcerated hernia, fracture |
| **Expedited** | Condition requires early surgery but not immediately life-threatening | Within days to 2 weeks | Cancer resection after staging, symptomatic gallstones |
| **Elective** | Planned procedure at a time to suit patient and institution | Scheduled at mutual convenience | Hernia repair, joint replacement, bariatric surgery |

**Scheduling priority rules:**
- Emergent cases pre-empt elective cases and are assigned to the next available OR
- Urgent cases are added to the next day's schedule; elective cases may be displaced
- Patients with time-sensitive conditions (e.g., cancer within NCCN-recommended surgical windows) receive expedited scheduling

---

## Step 2: Preoperative Readiness Verification

Before a case receives an OR time slot, verify all prerequisites using a structured checklist:

| Prerequisite | Status Required | Responsible Party |
|---|---|---|
| H&P completed (within 30 days, updated within 24h) | Complete | Surgeon or designee |
| Surgical consent signed | Signed with correct procedure + laterality | Surgeon |
| Insurance authorization | Approved or peer-to-peer completed | Scheduling coordinator |
| Labs obtained and reviewed | Within acceptable ranges | Surgeon / Pre-Admit Testing |
| Type and screen / crossmatch | Ordered per blood bank policy | Pre-Admit Testing |
| Cardiac clearance (if indicated) | Documented | Cardiologist / PCP |
| Anesthesia pre-assessment | Complete | Anesthesia team |
| Anticoagulation management plan | Documented with hold dates | Surgeon |
| Bowel prep (if colorectal) | Instructions given to patient | Surgeon office |
| NPO instructions | Provided with clear liquid cutoff time | Pre-Admit Clinic |

If ANY prerequisite is not verified ≥48 hours before the scheduled case, flag the case as "at risk for cancellation" and escalate to the surgeon's office.

---

## Step 3: OR Assignment and Resource Allocation

### Block Time Management

Most institutions use a block scheduling model. Allocate cases within the block considering:

| Factor | Optimization Rule |
|---|---|
| Case duration | Schedule based on historical average duration for that surgeon and procedure, not the surgeon's estimate (surgeon estimates trend 15-20% short) |
| First case starts | Assign patients requiring fasting glucose management or pediatric patients as first case |
| Equipment setup | Robotic cases require 30-45 min setup time; schedule consecutively to minimize turnover |
| Contamination sequencing | Clean cases before contaminated/dirty cases; MRSA/VRE cases last |
| Implant coordination | Confirm vendor and implants on-site 24h before the case |
| Anesthesia complexity | High-acuity patients (ASA IV, anticipated difficult airway) should be first or second case to ensure optimal anesthesia staffing |

### Turnover Time Optimization
- Target turnover: 25-35 minutes for standard cases, 45-60 minutes for robotic
- Pre-position equipment and trays before the prior case ends
- Use a parallel processing model: clean-up team enters as the patient exits; setup team begins simultaneously
- Track and report actual turnover times weekly for quality improvement

---

## Step 4: Communication and Confirmation Protocol

### 72-Hour Pre-Operative Confirmation
Contact the patient to confirm:
- Surgery date, arrival time, and location
- NPO instructions reiterated
- Medication hold/take instructions (especially anticoagulants, diabetic medications, ACE inhibitors)
- Ride home arranged (for outpatient procedures)
- COVID/respiratory illness screening per institutional protocol

### Day-Before Verification
- Confirm OR assignment, start time, and room number with the OR charge nurse
- Verify equipment availability (contact vendor for implants, confirm robot availability)
- Confirm blood product availability (for cases with crossmatch orders)
- Verify anesthesia assignment (especially for cases requiring specialized anesthesia skills)
- Confirm bed availability for postoperative admission (ICU, step-down, floor)

### Day-Of Huddle
Participate in the pre-operative briefing (typically 0630-0700):
- Review the board: case sequence, surgeon assignments, room assignments
- Flag high-risk cases, equipment concerns, or staffing issues
- Identify potential schedule disruptions (emergency add-ons, delayed starts)

---

## Step 5: Schedule Performance Tracking

Track and report key metrics monthly:

| Metric | Target | Calculation |
|---|---|---|
| OR utilization rate | 75-85% | (Total case time + turnover) / Available block time |
| First case on-time start | ≥90% | Incision within 5 min of scheduled start time |
| Same-day cancellation rate | <2% | Cancellations / Total scheduled cases |
| Average turnover time | ≤30 min | Wheels-out to wheels-in |
| Case duration accuracy | Within 15% of estimate | Actual duration vs. scheduled duration |
| Block utilization by surgeon | ≥70% per block | Used time / Allocated block time |
| Add-on case volume | Track | Unscheduled cases added to the schedule |

**Block time reallocation rules:**
- If a surgeon's block utilization falls below 70% for 3 consecutive months, release unused block time to the open scheduling pool
- Surgeons with >85% utilization may request additional block time
- Open time is available first-come-first-served starting 7 days before the date

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is every scheduled case verified for preoperative readiness (H&P, consent, labs, clearances)?
2. Does the OR assignment account for equipment needs, case sequencing, and turnover time?
3. Has the patient been contacted with pre-operative instructions (NPO, medications, arrival time)?
4. Is post-operative bed availability confirmed for admission cases?
5. Are scheduling performance metrics being tracked and reported monthly?

---

## Quality Audit

- [ ] Urgency classification assigned to every case
- [ ] Preoperative readiness checklist verified ≥48 hours before case date
- [ ] Insurance authorization confirmed prior to scheduling
- [ ] OR room assigned with appropriate equipment and staffing
- [ ] Case duration estimated using historical data (not surgeon estimate alone)
- [ ] Case sequencing considers contamination class and equipment needs
- [ ] Implant/vendor availability confirmed 24h before case
- [ ] Patient contacted 72h preop with instructions confirmed
- [ ] Day-before verification completed (equipment, blood, bed, anesthesia)
- [ ] Day-of huddle attended and schedule reviewed
- [ ] First case start time documented for on-time metric
- [ ] Same-day cancellations documented with root cause
- [ ] Turnover times documented for each transition
- [ ] Monthly OR utilization report generated and reviewed

---

## Guidelines

1. Use historical case duration data (average of last 10 cases for that surgeon-procedure combination) for scheduling — surgeon time estimates are consistently 15-20% shorter than actual case time.
2. Build a 10-15% buffer into each OR day's schedule to accommodate case extensions and emergent add-ons without triggering overtime.
3. Same-day cancellations must have a root cause documented — track cancellation reasons monthly and address systemic issues (e.g., incomplete preop workup → improve pre-admit testing process).
4. Never schedule a case without a completed insurance authorization for elective procedures — denial after the procedure creates unrecoverable revenue loss.
5. For robot cases, schedule consecutively in the same room to minimize docking/undocking time and avoid conflicts with other teams needing the system.
6. Confirm post-operative bed assignments before the patient enters the OR for inpatient cases — sending a patient to PACU without a floor bed creates boarding delays that cascade through the schedule.
7. Communicate schedule changes immediately to all affected parties: surgeon, anesthesia, nursing, patient, and equipment vendors.
