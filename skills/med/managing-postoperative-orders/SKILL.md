---
name: managing-postoperative-orders
language: en
description: Generates postoperative order sets with pain management, DVT prophylaxis, diet advancement, and activity progression. Use when writing post-op orders, managing surgical recovery, or creating post-procedure protocols.
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

# Managing Postoperative Orders

Generates postoperative order sets with pain management, DVT prophylaxis, diet advancement, and activity progression.

## Why This Skill Exists

Postoperative orders are the primary communication tool between the surgeon and the nursing/pharmacy team in the critical hours following surgery. Omission errors in post-op orders are the most common source of preventable postoperative morbidity — a missed VTE prophylaxis order can lead to fatal pulmonary embolism; an inappropriate diet order can cause aspiration or anastomotic leak. CMS Surgical Care Improvement Project (SCIP) measures and Joint Commission National Patient Safety Goals both require documented postoperative plans addressing pain, VTE prophylaxis, antibiotic stewardship, and glucose management.

Structured, protocol-driven postoperative order sets reduce variability, prevent omissions, and improve ERAS compliance. This skill produces comprehensive order sets aligned with ACS NSQIP best practices and institutional safety standards.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What procedure was performed? **Default: [VERIFY — obtain from operative report]**
2. What is the patient's ASA class and significant comorbidities? **Default: ASA II, no significant comorbidities**
3. Was an ERAS protocol initiated preoperatively? **Default: no**
4. What is the patient's Caprini VTE risk score? **Default: [VERIFY — calculate from chart]**
5. Does the patient have allergies to NSAIDs, opioids, or anticoagulants? **Default: NKDA**
6. What drains, catheters, or tubes are in place? **Default: none**
7. Were there any intraoperative complications affecting recovery? **Default: none**
8. What is the patient's baseline renal function (Cr/GFR)? **Default: normal**

### Documents to Request

- Operative report (for procedure details, EBL, drain placement)
- Anesthesia record (for intraoperative medications, fluid balance, airway details)
- Preoperative medication reconciliation
- Allergy list
- Baseline laboratory values
- ERAS protocol order set (if applicable)
- Institutional VTE prophylaxis guidelines

---

## Step 1: Admission and Monitoring Orders

Structure the initial order block using the ADC-VAN-DISML mnemonic:

| Category | Order Element | Example |
|---|---|---|
| **A**dmit | Service, attending, level of care | Admit to General Surgery, Dr. Smith, surgical floor |
| **D**iagnosis | Post-op diagnosis | s/p laparoscopic cholecystectomy |
| **C**ondition | Status | Stable |
| **V**itals | Frequency | Q4h x24h, then Q8h; notify MD for HR >120, SBP <90, T >38.5°C, UOP <0.5 mL/kg/h |
| **A**llergies | Confirmed list | Penicillin (anaphylaxis) |
| **N**ursing | Special instructions | I&O Q shift, daily weights, HOB elevated 30°, sequential compression devices at all times |
| **D**iet | Progression plan | NPO → clear liquids → regular diet as tolerated |
| **I**V fluids | Type, rate | LR at 125 mL/h, reassess with AM labs |
| **S**pecial | Drains, tubes, lines | JP drain to bulb suction, record output Q8h; Foley to gravity, remove POD1 |
| **M**edications | See Steps 2-4 | — |
| **L**abs | Timing | CBC, BMP in AM; repeat Hgb if EBL >500 mL |

---

## Step 2: Pain Management Orders

Apply multimodal analgesia principles per ERAS Society and ACS guidelines:

**Tier 1 — Non-opioid foundation (order for all patients unless contraindicated):**
- Acetaminophen 1000 mg PO/IV Q6h scheduled (max 3g/day if liver disease; 4g/day otherwise)
- Ketorolac 15-30 mg IV Q6h x 48h (hold if CrCl <30, GI bleed history, or EBL >500 mL), then transition to ibuprofen 400 mg PO Q6h

**Tier 2 — Adjuncts:**
- Gabapentin 300 mg PO Q8h (reduce for renal impairment; caution in elderly for sedation)
- Lidocaine patch 5% to incision area Q12h (on 12h, off 12h)
- Local anesthetic infiltration or TAP block per anesthesia

**Tier 3 — Opioids (rescue only, with stewardship documentation):**
- Oxycodone 5 mg PO Q4h PRN moderate pain (NRS 4-6)
- Hydromorphone 0.2 mg IV Q3h PRN severe pain (NRS 7-10)
- PCA order if indicated (document settings: demand dose, lockout interval, 4-hour limit, no basal rate)

Document opioid stewardship: calculate oral morphine equivalents (OME) daily, target de-escalation to oral-only by POD 2.

---

## Step 3: VTE Prophylaxis Orders

Select based on Caprini score and bleeding risk:

| Caprini Score | Risk Level | Prophylaxis |
|---|---|---|
| 0-2 | Low | Early ambulation + SCDs |
| 3-4 | Moderate | Enoxaparin 40 mg SQ daily OR heparin 5000 units SQ Q8h + SCDs |
| ≥5 | High | Enoxaparin 40 mg SQ daily + SCDs; consider extended prophylaxis (28 days) for cancer surgery |

**Special populations:**
- CrCl <30: Use unfractionated heparin 5000 units SQ Q8h instead of enoxaparin
- BMI >40: Enoxaparin 40 mg SQ Q12h (weight-based dosing)
- Active bleeding or high hemorrhage risk: SCDs only; reassess Q12h for transition to pharmacologic prophylaxis
- Epidural in situ: Coordinate with anesthesia; hold LMWH 12h before and 4h after catheter manipulation

Document first dose timing: initiate 6-12 hours postoperatively per institutional protocol.

---

## Step 4: Antibiotic Stewardship

- **Prophylactic antibiotics**: Discontinue within 24 hours of surgical end time per SCIP/CMS measures (exception: cardiac surgery, 48 hours)
- **Therapeutic antibiotics**: If contamination found intraoperatively, convert to therapeutic course — document indication, planned duration, and culture-directed adjustment plan
- **Surgical site surveillance**: Order wound checks per nursing protocol

Standard prophylaxis continuation (do NOT extend beyond 24h without documentation):

| Procedure Type | Antibiotic | Duration |
|---|---|---|
| Clean (Class I) | Cefazolin | Single dose + 1 re-dose if >4h case |
| Clean-contaminated (Class II) | Cefazolin + metronidazole (colorectal) | ≤24 hours |
| Contaminated (Class III) | Therapeutic course | Based on cultures |

---

## Step 5: Diet, Activity, and Disposition Planning

**Diet advancement** (per ERAS unless bowel-specific contraindication):
- POD 0: Ice chips or clear liquids
- POD 1: Regular diet as tolerated (ERAS evidence supports early feeding even after colorectal surgery)
- Document: hold advancement if nausea/vomiting, abdominal distension, or absent bowel function beyond POD 3

**Activity progression:**
- POD 0: Dangle at bedside, 2 assisted walks (minimum)
- POD 1: Ambulate 4x daily with PT/nursing; remove Foley catheter
- POD 2+: Progressive ambulation; incentive spirometry 10 breaths Q1h while awake

**Discharge criteria** (document as checklist):
- Tolerating regular diet
- Pain controlled on oral medications (NRS ≤4)
- Ambulating independently
- No signs of surgical complication (fever, tachycardia, wound issues)
- Bowel function returned (for GI procedures)

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is VTE prophylaxis ordered with the correct agent and dose for the patient's risk score and renal function?
2. Are prophylactic antibiotics set to discontinue within 24 hours?
3. Is the pain management plan multimodal with opioids reserved for breakthrough only?
4. Are all drains, tubes, and catheters accounted for with output monitoring orders?
5. Does the diet advancement plan align with ERAS or procedure-specific guidelines?

---

## Quality Audit

- [ ] Admission diagnosis matches operative report post-op diagnosis
- [ ] Vital sign parameters with specific notification thresholds documented
- [ ] I&O monitoring ordered for appropriate duration
- [ ] Multimodal pain regimen ordered with non-opioid foundation
- [ ] Opioid orders include stewardship limits and de-escalation plan
- [ ] VTE prophylaxis ordered within 6-12 hours post-op
- [ ] Caprini score documented as basis for VTE prophylaxis selection
- [ ] Prophylactic antibiotics ordered to discontinue within 24 hours
- [ ] Diet progression plan documented
- [ ] Activity orders include specific ambulation targets
- [ ] Drain/tube management orders include output documentation frequency
- [ ] Foley removal timing ordered (target POD 1 per ERAS)
- [ ] Morning labs ordered
- [ ] Discharge criteria documented

---

## Guidelines

1. Always use the ADC-VAN-DISML framework to prevent omission of critical order categories.
2. Never omit VTE prophylaxis — document the reason if pharmacologic prophylaxis is held (active bleeding, epidural) and set a reassessment trigger.
3. ERAS compliance requires early oral intake and early ambulation; override only with documented clinical justification.
4. Do not extend prophylactic antibiotics beyond 24 hours without converting to a therapeutic order with documented indication and planned duration.
5. Adjust all renally-cleared medications for the patient's current GFR, not the pre-admission baseline.
6. Document oral morphine equivalents (OME) daily for opioid stewardship reporting.
7. Set clear nursing notification parameters — vague orders like "notify MD PRN" are insufficient; specify vital sign thresholds.
8. Review and reconcile home medications by POD 1; restart chronic medications (statins, beta-blockers, antihypertensives) as soon as the patient tolerates oral intake.
