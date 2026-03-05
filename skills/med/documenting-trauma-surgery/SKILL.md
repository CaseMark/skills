---
name: documenting-trauma-surgery
description: Creates trauma surgery documentation with injury severity scoring and damage control principles. Use when documenting trauma operations, calculating ISS, or recording damage control sequences.
tags:
  - documentation
  - surgery
metadata:
  author: casemark
  practice_areas:
    - General Surgery
    - Surgical Subspecialties
  document_types:
    - Clinical Documentation
  skill_modes:
    - Documentation
---

# Documenting Trauma Surgery

Creates trauma surgery documentation with injury severity scoring and damage control principles.

## Why This Skill Exists

Trauma is the leading cause of death for Americans under age 45, and trauma surgery documentation faces unique challenges: operations are emergent with no preoperative planning, patients often cannot provide history, injuries are frequently multi-system, and the documentation must simultaneously support clinical care, injury severity scoring (ISS), trauma registry reporting, and medicolegal defense. The American College of Surgeons Committee on Trauma (ACS-COT) requires Level I and Level II trauma centers to maintain comprehensive trauma registries with standardized injury coding, and verification site reviews specifically examine documentation quality.

Damage control surgery — a staged approach where initial surgery controls hemorrhage and contamination, followed by ICU resuscitation and delayed definitive repair — requires meticulous documentation of each operative phase, the clinical rationale for staging, and the resuscitation endpoints between stages. Poor documentation leads to inaccurate ISS calculation (affecting trauma center verification, research, and benchmarking), coding errors, and medicolegal vulnerability in the high-litigation trauma environment.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What was the mechanism of injury (blunt, penetrating, blast, burn, other)? **Default: [VERIFY — obtain from trauma team leader]**
2. What were the prehospital vitals and GCS? **Default: [VERIFY — obtain from EMS report]**
3. What injuries were identified on primary and secondary survey? **Default: [VERIFY]**
4. Was the patient taken directly to the OR or was imaging obtained first? **Default: [VERIFY]**
5. Is this a damage control surgery (DCS) or definitive repair? **Default: [VERIFY]**
6. What is the patient's hemodynamic status and resuscitation status? **Default: [VERIFY]**
7. What blood products have been administered? **Default: [VERIFY — from massive transfusion protocol record]**
8. What is the trauma activation level (full, modified, consult)? **Default: [VERIFY]**

### Documents to Request

- EMS/prehospital report (mechanism, vitals, interventions)
- Trauma team leader assessment
- Primary and secondary survey documentation
- FAST exam results
- Imaging reports (chest X-ray, pelvic X-ray, CT pan-scan)
- Massive transfusion protocol records
- Anesthesia record
- Prior operative reports (if staged DCS)
- Trauma registry data collection form

---

## Step 1: Injury Documentation and AIS/ISS Scoring

### Abbreviated Injury Scale (AIS) and Injury Severity Score (ISS)

Document each injury with its AIS code and severity:

| AIS Severity | Description | Examples |
|---|---|---|
| 1 — Minor | Superficial injury | Skin abrasion, minor contusion |
| 2 — Moderate | Reversible injury, not life-threatening | Simple fracture, small pneumothorax |
| 3 — Serious | Not immediately life-threatening, potential long-term sequelae | Open fracture, major hemothorax, bowel perforation |
| 4 — Severe | Life-threatening, survival probable | Liver laceration Grade III-IV, flail chest with contusion |
| 5 — Critical | Life-threatening, survival uncertain | Aortic injury, massive hepatic disruption, severe TBI |
| 6 — Unsurvivable | Virtually unsurvivable | Decapitation, total body disruption |

### ISS Calculation

ISS uses the three most severely injured body regions (from six: head/neck, face, chest, abdomen/pelvic contents, extremities/pelvic girdle, external):

```
ISS = (highest AIS in region 1)² + (highest AIS in region 2)² + (highest AIS in region 3)²
```

**ISS ranges**: 1-75 (any single AIS 6 automatically = ISS 75)
**ISS ≥16 = major trauma** (associated with >10% mortality)
**ISS ≥25 = severe trauma** (associated with >25% mortality)

Document each injury, its AIS code, the body region, and the calculated ISS. This feeds directly into the trauma registry.

---

## Step 2: Trauma Operative Report — Special Elements

In addition to standard operative report elements, trauma operative reports must include:

### Indication Section
- Mechanism and time of injury
- Prehospital and ED vitals (include lowest SBP and GCS)
- FAST exam results (positive/negative, which quadrant)
- Imaging findings that prompted surgery (or documentation that patient was too unstable for imaging)
- Hemodynamic status at decision to operate (e.g., "Pt remained hypotensive with SBP 70s despite 2 units pRBC; decision made for emergent exploratory laparotomy")

### Findings Section (systematic exploration)

For exploratory laparotomy, document a complete systematic survey:

| Structure | Finding | AIS Grade |
|---|---|---|
| Diaphragm (bilateral) | Intact / laceration with location | — |
| Liver | Intact / laceration grade (AAST grading) | — |
| Spleen | Intact / laceration grade (AAST grading) | — |
| Stomach | Intact / perforation location | — |
| Duodenum (Kocher maneuver) | Intact / injury | — |
| Small bowel (run entire length) | Intact / perforation / mesenteric injury | — |
| Colon (entire length) | Intact / perforation / devascularization | — |
| Rectum | Intact / injury | — |
| Kidneys (bilateral) | Intact / contusion / laceration | — |
| Bladder | Intact / rupture (intra vs. extraperitoneal) | — |
| Major vessels (aorta, IVC, iliac, mesenteric) | Intact / injury with type | — |
| Pelvis / retroperitoneum | Hematoma (zone I, II, or III) / expanding vs. stable | — |

Document negative findings explicitly ("spleen was inspected and found intact") to confirm the survey was complete.

### AAST Organ Injury Scale

Document organ injuries using the American Association for the Surgery of Trauma (AAST) grading:

| Organ | Grade I | Grade II | Grade III | Grade IV | Grade V |
|---|---|---|---|---|---|
| Liver | Subcapsular hematoma <10% SA, laceration <1cm depth | Hematoma 10-50% SA, laceration 1-3 cm depth | Hematoma >50% SA, laceration >3 cm depth | Parenchymal disruption 25-75% of lobe | Parenchymal disruption >75% of lobe, juxtahepatic venous injury |
| Spleen | Subcapsular hematoma <10% SA, laceration <1 cm depth | Hematoma 10-50% SA, laceration 1-3 cm depth | Hematoma >50% SA, laceration >3 cm depth | Laceration involving segmental/hilar vessels, devascularization >25% | Shattered spleen, hilar vascular injury devascularizing spleen |

---

## Step 3: Damage Control Surgery Documentation

When a damage control approach is used, document each phase:

### Phase 1: Damage Control Laparotomy (DCL)

Document the lethal triad status at the time of DCL decision:
- **Hypothermia**: Core temperature <35°C
- **Acidosis**: pH <7.2, base deficit >6, lactate >4 mmol/L
- **Coagulopathy**: INR >1.5, PTT >60s, fibrinogen <100, clinical non-surgical bleeding

Document the DCL objectives achieved:
- [ ] Hemorrhage controlled (method: packing, ligation, shunt, clamp)
- [ ] Contamination controlled (method: stapled resection, suture repair, drainage)
- [ ] Temporary abdominal closure (TAC) method (negative pressure dressing, Bogota bag, vacuum-pack)
- [ ] Time in OR
- [ ] Blood products administered intraoperatively (pRBC, FFP, platelets, cryo, TXA)
- [ ] EBL
- [ ] Packs placed (number, location)
- [ ] Plan for return to OR (expected timing: 24-72 hours)

### Phase 2: ICU Resuscitation

Document resuscitation targets between DCS stages:
- Temperature >36°C
- pH >7.25, lactate trending down
- INR <1.5, fibrinogen >150
- Base deficit improving
- Hemodynamic stability (off or weaning vasopressors)
- Urine output >0.5 mL/kg/h

### Phase 3: Definitive Surgery (Planned Re-Exploration)

Document as a separate operative report:
- Pack removal (number and condition — any retained packs is a never event)
- Definitive organ repair or resection
- Anastomosis creation (or diversion decision with rationale)
- Definitive abdominal wall closure (or reason for leaving open with closure plan)

---

## Step 4: Massive Transfusion Protocol Documentation

Document MTP activation and products administered:

| Time | pRBC | FFP | Platelets | Cryo | Calcium | TXA |
|---|---|---|---|---|---|---|
| 0-15 min | 4 units | 4 units | 1 apheresis | 10 units | 1g CaCl | 1g bolus |
| 15-30 min | 4 units | 4 units | — | — | 1g CaCl | — |
| 30-60 min | 2 units | 2 units | 1 apheresis | — | — | 1g infusion |
| **Total** | **10** | **10** | **2** | **10** | **2g** | **2g** |

Document:
- Time MTP was activated and by whom
- Ratio of pRBC:FFP:Platelets (target 1:1:1 per PROPPR trial)
- TXA administration (must be given within 3 hours of injury per CRASH-2 trial)
- Serial point-of-care labs (TEG/ROTEM if available, or CBC/INR/fibrinogen Q30min)
- MTP termination time and reason

---

## Step 5: Trauma Registry and Quality Reporting

Ensure documentation supports:

1. **Trauma registry data elements**: Mechanism, prehospital data, ED vitals, injury AIS codes, ISS, procedures, complications, LOS, disposition, mortality
2. **ACS-COT Performance Improvement (PI) filters**: Cases that trigger mandatory PI review:
   - Trauma death
   - ICU stay >3 days
   - Unplanned return to OR
   - Missed injury identified after initial evaluation
   - Transfer to higher level of care
3. **TQIP (Trauma Quality Improvement Program)**: National benchmarking data — accurate ISS and outcome coding is essential
4. **State trauma registry reporting**: Required in most states, with specific data fields and submission timelines

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are all injuries documented with AAST grading and AIS codes for ISS calculation?
2. Does the operative report include systematic survey documentation (all structures evaluated)?
3. For DCS cases, are all phases documented separately with resuscitation targets and endpoints?
4. Is the MTP documented with products, ratios, and timing?
5. Are trauma registry data elements complete and PI filters identified?

---

## Quality Audit

- [ ] Mechanism of injury documented with time of injury
- [ ] Prehospital vitals and GCS documented from EMS report
- [ ] FAST exam results documented
- [ ] All injuries listed with AAST grading (organ injuries) and AIS codes
- [ ] ISS calculated and documented
- [ ] Systematic surgical exploration documented with negative findings
- [ ] AAST organ injury grades match operative findings
- [ ] DCS decision rationale documented (lethal triad indicators)
- [ ] Each DCS phase has a separate operative report
- [ ] Pack count documented at each phase (placed and removed)
- [ ] MTP documented with product totals and ratios
- [ ] TXA administration documented (timing relative to injury)
- [ ] Resuscitation endpoints documented between DCS phases
- [ ] Trauma registry data elements completed
- [ ] ACS-COT PI filters screened and flagged cases identified

---

## Guidelines

1. Document the decision to operate and the hemodynamic rationale — "taken to OR because of instability despite resuscitation" is legally stronger than "taken to OR for exploratory laparotomy."
2. Always document a complete systematic exploration, including negative findings. Failure to document examination of a structure may be interpreted as failure to examine it at all.
3. Use AAST organ injury grading for all solid and hollow viscus injuries — this is the standardized language for trauma registry coding and inter-institutional comparison.
4. For DCS, document the lethal triad parameters (temperature, pH/lactate, coagulation) at the time of the DCL decision and at each subsequent phase transition. This demonstrates the clinical rationale for staged surgery.
5. Count all packs placed during DCL and count all packs removed during re-exploration. Document these counts explicitly — a retained pack is a never event.
6. TXA must be administered within 3 hours of injury per CRASH-2 evidence. After 3 hours, TXA may increase mortality. Document the time of injury and the time of TXA administration.
7. Maintain a 1:1:1 ratio (pRBC:FFP:platelets) during massive transfusion per PROPPR trial evidence. Document the actual ratio achieved and any deviations with rationale.
