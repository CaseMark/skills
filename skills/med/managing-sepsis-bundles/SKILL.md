---
name: managing-sepsis-bundles
description: Tracks sepsis bundle compliance with lactate timing, fluid resuscitation, and antibiotic administration. Use when managing sepsis protocols, tracking bundle elements, or documenting sepsis care.
tags:
  - management
  - emergency-medicine
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Sepsis Bundles

Tracks Sepsis-3 identification, SEP-1 bundle compliance, and documents lactate clearance, antibiotic timing, fluid resuscitation, and vasopressor initiation per Surviving Sepsis Campaign guidelines.

## Why This Skill Exists

Sepsis kills 270,000 Americans annually and is the leading cause of death in US hospitals. CMS SEP-1 is a publicly reported quality measure that tracks six-hour bundle compliance—hospitals with low compliance face financial penalties, reputational damage, and increased mortality. Each hour of delay in appropriate antibiotic administration increases sepsis mortality by 7.6%. Despite this, national SEP-1 compliance hovers around 50%, primarily due to documentation failures rather than clinical care gaps.

The 2021 Surviving Sepsis Campaign guidelines and Sepsis-3 definitions shifted the diagnostic framework from SIRS criteria to qSOFA and SOFA scoring. Understanding these definitions is essential because documentation that conflates SIRS-based sepsis with Sepsis-3 organ dysfunction criteria creates coding and compliance errors.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. When was the patient first identified as meeting sepsis screening criteria (time zero)?
2. Does the patient meet Sepsis-3 criteria: suspected infection PLUS acute organ dysfunction (SOFA ≥2 from baseline)?
3. What is the suspected source of infection (pneumonia, UTI, intra-abdominal, skin/soft tissue, bloodstream, unknown)?
4. What were the initial vital signs, lactate level, and mental status at time zero?
5. Were blood cultures obtained before antibiotic administration?
6. What empiric antibiotic regimen was chosen, and was it administered within 1 hour of sepsis recognition?
7. Has 30 mL/kg crystalloid been initiated for hypotension (MAP <65) or lactate ≥4 mmol/L?
8. If hypotension persists after fluid challenge, have vasopressors been initiated?

### Documents to Request

- Sepsis screening tool timestamp (nursing or EMR alert)
- Initial and repeat lactate values with timestamps
- Blood culture collection time (before antibiotics)
- Antibiotic order time AND administration time (these differ and both matter)
- Fluid resuscitation volume and administration times
- Vasopressor initiation time (if applicable)
- Physician reassessment documentation after fluid bolus
- Source control assessment (imaging, surgical consultation)
- Procalcitonin and other biomarkers if obtained

---

## Step 1: Sepsis-3 Definition Application

### Sepsis Identification

**Sepsis** = Suspected or documented infection + acute organ dysfunction (SOFA score increase ≥2 points from baseline)

### qSOFA (Quick SOFA) — Bedside Screening Tool

| Criterion | Threshold | Points |
|---|---|---|
| Altered mental status | GCS <15 | 1 |
| Respiratory rate | ≥22 breaths/min | 1 |
| Systolic blood pressure | ≤100 mmHg | 1 |

qSOFA ≥2 suggests possible sepsis and should trigger further workup. Note: qSOFA is a **screening tool**, not a diagnostic criterion—it has high specificity but low sensitivity.

### SOFA Score Components (for organ dysfunction quantification)

| System | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Respiration (PaO2/FiO2) | ≥400 | <400 | <300 | <200 with support | <100 with support |
| Coagulation (Platelets x10³) | ≥150 | <150 | <100 | <50 | <20 |
| Liver (Bilirubin mg/dL) | <1.2 | 1.2-1.9 | 2.0-5.9 | 6.0-11.9 | >12 |
| Cardiovascular (MAP/vasopressors) | MAP ≥70 | MAP <70 | Dopa ≤5 or dobutamine | Dopa >5 or epi ≤0.1 or norepi ≤0.1 | Dopa >15 or epi >0.1 or norepi >0.1 |
| CNS (GCS) | 15 | 13-14 | 10-12 | 6-9 | <6 |
| Renal (Creatinine/UOP) | <1.2 | 1.2-1.9 | 2.0-3.4 | 3.5-4.9 or UOP <500 | >5 or UOP <200 |

**Septic shock** = Sepsis + vasopressor requirement to maintain MAP ≥65 + lactate >2 mmol/L despite adequate volume resuscitation.

---

## Step 2: SEP-1 Bundle Elements and Timing

### Hour-1 Bundle (Surviving Sepsis Campaign 2021)

All elements should be initiated within 1 hour of sepsis recognition:

| Element | Target | SEP-1 Metric Window |
|---|---|---|
| Measure lactate | Initial level within 6 hours | Must be drawn within 6 hours of time zero |
| Obtain blood cultures before antibiotics | 2 sets (4 bottles) from 2 sites | Must be drawn before first antibiotic dose |
| Administer broad-spectrum antibiotics | Appropriate empiric coverage for suspected source | Within 3 hours (present on admission) or 1 hour (severe sepsis/shock) |
| Administer 30 mL/kg crystalloid | For hypotension (MAP <65) or lactate ≥4 | Start within 3 hours; complete within 6 hours |
| Apply vasopressors | If hypotension persists after fluid resuscitation | Document reassessment and vasopressor initiation |
| Remeasure lactate | If initial lactate >2 mmol/L | Within 6 hours of initial measurement |

### Antibiotic Selection by Suspected Source

| Source | Empiric Regimen | Key Considerations |
|---|---|---|
| Pneumonia (community) | Ceftriaxone + azithromycin OR respiratory fluoroquinolone | Consider MRSA coverage if risk factors |
| Pneumonia (hospital/ventilator) | Piperacillin-tazobactam or meropenem + vancomycin ± inhaled aminoglycoside | Anti-pseudomonal coverage required |
| Urinary tract | Ceftriaxone or fluoroquinolone | Piperacillin-tazobactam if complicated or resistant organisms |
| Intra-abdominal | Piperacillin-tazobactam or meropenem | Must cover anaerobes and gram-negatives |
| Skin/soft tissue | Vancomycin + piperacillin-tazobactam | Clindamycin for toxin suppression in necrotizing fasciitis |
| Unknown source | Vancomycin + piperacillin-tazobactam or meropenem | Broadest coverage; narrow when cultures return |
| Meningitis | Vancomycin + ceftriaxone + ampicillin (if >50 or immunocompromised) + dexamethasone | Dexamethasone before or with first antibiotic dose |

---

## Step 3: Fluid Resuscitation and Hemodynamic Management

### Initial Fluid Resuscitation

1. Calculate 30 mL/kg based on actual body weight (NOT ideal body weight)
2. Use balanced crystalloid (lactated Ringer's or Plasmalyte) preferred over 0.9% NaCl to reduce hyperchloremic acidosis
3. Administer as rapidly as tolerated—most should complete within 1-3 hours
4. Document fluid responsiveness: improvement in MAP, heart rate, urine output, lactate

### Vasopressor Initiation

If MAP remains <65 mmHg after 30 mL/kg crystalloid (or clinician reassessment determines further fluid is unlikely to benefit):

| Agent | Starting Dose | Max Dose | Notes |
|---|---|---|---|
| Norepinephrine (first-line) | 0.1 mcg/kg/min | 1-2 mcg/kg/min | Alpha-1 >> beta-1; preferred vasoactive |
| Vasopressin (second-line adjunct) | 0.03-0.04 units/min | 0.04 units/min (fixed) | Add when norepinephrine 0.25-0.5 mcg/kg/min |
| Epinephrine (third-line) | 0.1 mcg/kg/min | Titrate to effect | For catecholamine-refractory shock with cardiac dysfunction |
| Phenylephrine | 0.5-2 mcg/kg/min | 5 mcg/kg/min | Pure alpha—limited role; consider if tachyarrhythmia limits others |

---

## Step 4: Lactate Clearance Monitoring

| Initial Lactate | Action | Repeat Timing |
|---|---|---|
| <2 mmol/L | Sepsis (not shock); standard monitoring | Not mandatory for SEP-1 but clinically prudent |
| 2-4 mmol/L | Indicates tissue hypoperfusion; guide resuscitation | Repeat within 2-4 hours |
| ≥4 mmol/L | Septic shock criterion; aggressive resuscitation | Repeat within 6 hours (SEP-1 requirement) |

**Target**: ≥10% lactate clearance per 2 hours OR normalization (<2 mmol/L). Failure to clear lactate despite adequate resuscitation suggests ongoing tissue hypoxia, need for source control, or mitochondrial dysfunction.

---

## Step 5: Source Control and Reassessment

1. Identify the source: obtain appropriate imaging (CT abdomen, chest X-ray, ultrasound)
2. Determine if source requires intervention: abscess drainage, surgical debridement, device removal, decompression
3. Source control should be achieved within 6-12 hours of identification when possible
4. Reassess at 6 hours: repeat vital signs, lactate, clinical exam
5. De-escalate antibiotics within 48-72 hours based on culture sensitivities
6. Consider stopping antibiotics at 7-10 days for most infections; use procalcitonin-guided discontinuation when available

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the time zero (sepsis recognition time) clearly documented and defensible?
2. Were blood cultures obtained BEFORE the first antibiotic dose (timestamp comparison)?
3. Is the antibiotic regimen appropriate for the suspected source with adequate spectrum?
4. Is fluid resuscitation calculated at 30 mL/kg with actual body weight documented?
5. Is the 6-hour physician reassessment documented with exam findings and plan?

---

## Quality Audit

| # | Criterion | Pass/Fail |
|---|---|---|
| 1 | Time zero clearly identified and documented | |
| 2 | Sepsis-3 criteria met (infection + SOFA ≥2) and documented | |
| 3 | Initial lactate drawn within 6 hours of time zero | |
| 4 | Blood cultures drawn before antibiotic administration | |
| 5 | Antibiotics administered within 1 hour of sepsis recognition | |
| 6 | Antibiotic spectrum appropriate for suspected source | |
| 7 | 30 mL/kg crystalloid initiated within 3 hours for eligible patients | |
| 8 | Repeat lactate obtained within 6 hours if initial >2 mmol/L | |
| 9 | Vasopressor initiated for persistent hypotension post-fluids | |
| 10 | 6-hour physician reassessment documented | |
| 11 | Source control assessment documented with timeline | |
| 12 | Antibiotic de-escalation plan documented | |
| 13 | Weight used for fluid calculation documented | |
| 14 | All SEP-1 bundle element timestamps recorded | |
| 15 | Heart failure patients assessed for modified fluid approach | |

---

## Guidelines

1. **Time zero determination** is the most contested element in SEP-1—it should be the earliest time that infection AND organ dysfunction criteria are simultaneously present; retrospective backdating is a compliance and legal risk
2. **Blood cultures before antibiotics** is critical but should never delay antibiotic administration more than 45 minutes—if access is difficult, give antibiotics and document the reason cultures were deferred
3. **30 mL/kg is not mandatory for every sepsis patient**—it applies only to sepsis-induced hypotension or lactate ≥4; for normotensive sepsis without elevated lactate, fluid decisions are clinician judgment
4. **Heart failure and ESRD patients** may not tolerate 30 mL/kg—document clinical assessment, consider smaller boluses with reassessment, and document the rationale for modified fluid volumes
5. **Norepinephrine is first-line vasopressor**—dopamine is associated with higher arrhythmia rates and mortality in septic shock; it should not be used as a first-line agent
6. **Lactate is not a specific marker**—elevated lactate can reflect aerobic glycolysis (beta-agonists, epinephrine), liver failure, or seizure rather than tissue hypoxia; interpret in clinical context
7. **Procalcitonin** is most useful for guiding antibiotic duration (discontinue when PCT <0.25 or >80% decline from peak) rather than for initial diagnosis
8. **Corticosteroids** (hydrocortisone 200 mg/day IV) are recommended for septic shock refractory to vasopressors, not for routine sepsis management
