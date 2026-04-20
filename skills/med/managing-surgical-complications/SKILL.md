---
name: managing-surgical-complications
language: en
description: Classifies and documents surgical complications using Clavien-Dindo grading with management protocols. Use when managing post-surgical complications, grading adverse events, or documenting complication management.
tags:
  - management
  - surgery
  - surgical
metadata:
  author: casemark
  practice_areas:
    - General Surgery
    - Surgical Subspecialties
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Surgical Complications

Classifies and documents surgical complications using Clavien-Dindo grading with management protocols.

## Why This Skill Exists

Surgical complications occur in 3-17% of all surgical cases depending on procedure complexity and patient factors. Standardized classification and documentation of complications is required for ACS NSQIP quality reporting, institutional quality dashboards, morbidity and mortality conferences, and medicolegal defense. The Clavien-Dindo classification system is the internationally accepted standard for grading postoperative complications, and its consistent application enables meaningful benchmarking across surgeons, institutions, and time periods.

Failure to recognize, classify, and escalate complications in a timely manner is a leading cause of failure-to-rescue events — the ACS defines failure to rescue as death after a treatable complication. Institutions with lower failure-to-rescue rates do not necessarily have fewer complications; they recognize and respond to them faster. This skill provides the framework for systematic complication identification, grading, management, and documentation.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What was the index operation, date, and surgeon? **Default: [VERIFY — obtain from operative report]**
2. When did the complication present (POD number and clinical context)? **Default: [VERIFY]**
3. What are the clinical signs and symptoms of the complication? **Default: [VERIFY]**
4. What diagnostic workup has been performed (labs, imaging)? **Default: [VERIFY]**
5. What management has been initiated so far? **Default: none yet**
6. Has the complication required return to the operating room? **Default: no**
7. What is the patient's baseline risk profile (ASA class, NSQIP predicted morbidity)? **Default: ASA II**
8. Has the attending surgeon been notified? **Default: yes**

### Documents to Request

- Original operative report
- Postoperative progress notes from the day the complication was identified
- Laboratory results (trending values: WBC, lactate, Cr, Hgb)
- Imaging reports related to the complication
- Nursing assessments and vital sign trends
- Medication administration record (antibiotics, vasopressors, anticoagulants)
- Any re-operative reports if return to OR occurred

---

## Step 1: Complication Identification and Classification

Apply the Clavien-Dindo classification system:

| Grade | Definition | Examples |
|---|---|---|
| **I** | Any deviation from normal postoperative course without the need for pharmacological treatment or surgical/endoscopic/radiological intervention. Allowed: antiemetics, antipyretics, analgesics, diuretics, electrolytes, physiotherapy. Includes wound infections opened at the bedside. | Atelectasis requiring incentive spirometry, ileus resolving with conservative management |
| **II** | Requiring pharmacological treatment with drugs OTHER than those allowed for Grade I. Includes blood transfusions and TPN. | UTI requiring antibiotics, DVT requiring anticoagulation, transfusion for anemia |
| **IIIa** | Requiring surgical, endoscopic, or radiological intervention NOT under general anesthesia | CT-guided abscess drainage, percutaneous cholecystostomy, endoscopic stenting |
| **IIIb** | Requiring surgical, endoscopic, or radiological intervention UNDER general anesthesia | Re-exploration for hemorrhage, anastomotic leak requiring reoperation |
| **IVa** | Life-threatening complication requiring ICU management — single organ dysfunction | Respiratory failure requiring ventilation, dialysis for AKI |
| **IVb** | Life-threatening complication requiring ICU management — multi-organ dysfunction | Septic shock with ARDS and AKI |
| **V** | Death of the patient | — |

**Suffix "d"**: Append if the patient is still suffering from the complication at follow-up (e.g., Grade IIId = patient with a persistent enterocutaneous fistula requiring ongoing management).

---

## Step 2: Initial Assessment and Workup

When a complication is suspected, perform a structured assessment:

1. **Clinical assessment**: Focused history (new symptoms, timeline), physical exam of the surgical site and relevant systems, vital signs with trends.
2. **Laboratory workup**:
   - CBC with differential (WBC trend, Hgb drop)
   - BMP (Cr trend for AKI, electrolyte derangements)
   - Lactate (tissue hypoperfusion)
   - Procalcitonin (bacterial infection differentiation)
   - Coagulation studies (if hemorrhage or DIC concern)
   - Blood cultures x2 (if fever >38.3°C or clinical sepsis)
3. **Imaging**:
   - CT abdomen/pelvis with IV contrast: anastomotic leak, abscess, hemorrhage
   - CT angiography: active arterial bleeding
   - Chest X-ray: effusion, pneumothorax, pneumonia
   - Duplex ultrasound: DVT
   - CT pulmonary angiography: pulmonary embolism

Document findings in a complication assessment note that includes the Clavien-Dindo grade assignment.

---

## Step 3: Management Protocols by Complication Type

### Hemorrhage (postoperative bleeding)
- **Resuscitation**: Large-bore IV access, crystalloid bolus, activate massive transfusion protocol if hemodynamically unstable
- **Transfusion targets**: Hgb >7 g/dL (general), >8 g/dL (cardiac disease); platelets >50K if actively bleeding
- **Decision to return to OR**: Based on hemodynamic instability despite resuscitation, >2 units pRBC in 4h, expanding hematoma, CT evidence of active extravasation
- **Interventional alternative**: Angioembolization for select arterial bleeding sources

### Anastomotic Leak
- **Contained leak (small, drained)**: NPO, IV antibiotics, CT-guided drain placement, close drain output monitoring
- **Free leak with peritonitis**: Emergent return to OR for washout, diversion vs. revision, drain placement
- **Document**: POD of leak, WBC/lactate at detection, imaging findings, management pathway

### Surgical Site Infection — See dedicated SSI skill for full CDC classification and management

### Venous Thromboembolism
- **DVT**: Initiate therapeutic anticoagulation (assess bleeding risk timing post-op); if <48h post-major surgery, consider IVC filter
- **PE**: CTA for diagnosis; anticoagulation or thrombolysis per hemodynamic severity; massive PE → consider catheter-directed therapy or surgical embolectomy

---

## Step 4: Escalation and Communication

Document the escalation pathway for each complication:

- **Time of recognition**: When the complication was first identified
- **Notification chain**: Resident → attending → consulting services (IR, critical care, pulmonology)
- **Patient/family communication**: Document the conversation including who was present, what was disclosed, questions asked, and patient understanding
- **Rapid response / Code Blue**: If patient meets institutional criteria, document activation and team response

For Clavien-Dindo Grade ≥ IIIb:
- Notify department quality officer within 24 hours
- Enter event into institutional safety reporting system
- Flag for M&M conference review

---

## Step 5: Documentation and Reporting

Structure the complication progress note:

1. **Event identification**: Date, POD, complication type
2. **Clavien-Dindo grade**: With rationale for grade assignment
3. **Clinical status**: Vitals, exam findings, lab/imaging results
4. **Management plan**: Interventions performed and planned
5. **Prognosis**: Expected trajectory and recovery timeline
6. **NSQIP reportable event?**: Yes/no with 30-day occurrence flag
7. **Quality reporting**: Entered into institutional system (date, report ID)

Report the complication in all relevant quality systems:
- ACS NSQIP (if within 30 days of index operation and meets variable definitions)
- Institutional surgical quality dashboard
- State reporting system (if mandatory for the complication type)

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the Clavien-Dindo grade correctly assigned and supported by the documented intervention?
2. Has the complication been reported to the attending surgeon and quality officer (if Grade ≥ IIIb)?
3. Is the management plan documented with specific interventions, monitoring parameters, and escalation criteria?
4. Has the patient/family been informed and is the disclosure conversation documented?
5. Has the event been entered into applicable quality reporting systems?

---

## Quality Audit

- [ ] Complication identified with specific POD and clinical presentation
- [ ] Clavien-Dindo grade assigned with written rationale
- [ ] Laboratory and imaging workup documented with results
- [ ] Management plan documented with specific interventions
- [ ] Escalation chain documented (who was notified, when)
- [ ] Patient/family communication documented
- [ ] Re-operative report available if return to OR required
- [ ] NSQIP reportable event determination made
- [ ] Institutional quality report filed (if Grade ≥ IIIb)
- [ ] Complication note entered as a distinct progress note (not buried in routine daily note)
- [ ] Follow-up plan documented with expected resolution timeline
- [ ] M&M conference flagged if Grade ≥ IIIb or if system failure contributed
- [ ] Discharge summary includes complication, grade, and management summary

---

## Guidelines

1. Assign the Clavien-Dindo grade based on the HIGHEST level of intervention required to treat the complication, not the severity of symptoms.
2. A complication managed with bedside wound opening is Grade I; the same wound infection requiring IV antibiotics is Grade II; the same infection requiring OR washout under general anesthesia is Grade IIIb.
3. Never retroactively downgrade a complication based on ultimate outcome — grade at the time of peak intervention.
4. Blood transfusion for postoperative anemia is always at least Grade II, even if the patient was "expected" to need it.
5. Document complications separately from routine progress notes to ensure they are captured in quality reporting.
6. The suffix "d" is applied at the time of discharge or last follow-up, not during the acute management phase.
7. For medicolegal protection, document the timeline of recognition, notification, and response — failure-to-rescue claims focus on delays in escalation, not on the occurrence of the complication itself.
