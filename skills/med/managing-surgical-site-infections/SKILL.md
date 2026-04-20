---
name: managing-surgical-site-infections
language: en
description: Classifies SSIs using CDC criteria with treatment protocols and reporting requirements. Use when identifying surgical infections, classifying SSI depth, or implementing SSI treatment.
tags:
  - management
  - surgery
  - surgical
  - treatment
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

# Managing Surgical Site Infections

Classifies SSIs using CDC criteria with treatment protocols and reporting requirements.

## Why This Skill Exists

Surgical site infections (SSIs) are the most common healthcare-associated infection in surgical patients, occurring in 2-5% of all inpatient surgeries and up to 20% of emergency abdominal procedures. The CDC National Healthcare Safety Network (NHSN) provides the standardized surveillance definitions used for mandatory reporting in most US states. SSIs increase length of stay by 7-10 days, double the risk of ICU admission, increase 30-day readmission rates, and add $10,000-$25,000 per infection in direct costs.

CMS includes SSI rates in its Hospital-Acquired Condition Reduction Program, directly linking SSI performance to reimbursement penalties. ACS NSQIP tracks SSIs as a primary quality outcome, and the Standardized Infection Ratio (SIR) is publicly reported on CMS Hospital Compare. This skill provides the complete framework for SSI identification using CDC/NHSN criteria, classification by depth, evidence-based treatment, and mandatory reporting compliance.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What was the index surgical procedure and date? **Default: [VERIFY — obtain from operative report]**
2. When did signs of infection first appear (POD number)? **Default: [VERIFY]**
3. What are the clinical signs (erythema, drainage, dehiscence, fever, leukocytosis)? **Default: [VERIFY]**
4. Was there a prosthetic implant placed during the surgery? **Default: no**
5. What was the CDC wound classification at the time of surgery (I-IV)? **Default: [VERIFY from operative report]**
6. What organisms, if any, have been cultured? **Default: cultures pending or not yet obtained**
7. What treatment has been initiated? **Default: none yet**
8. Is the patient within the NHSN surveillance window? **Default: [VERIFY]**

### Documents to Request

- Operative report with wound classification
- Preoperative and postoperative vital signs and WBC trends
- Wound assessment nursing notes
- Culture and sensitivity results
- Imaging studies (CT, ultrasound) if deep infection suspected
- Antibiotic administration record (prophylactic and therapeutic)
- ACS NSQIP data collection form
- Institutional infection control reporting requirements

---

## Step 1: CDC/NHSN SSI Classification

### Surveillance Window

SSIs must occur within the CDC/NHSN-defined surveillance period:
- **No implant**: Within 30 days of the operative procedure
- **With implant** (prosthetic valve, mesh, joint prosthesis, vascular graft): Within 90 days of the operative procedure

### SSI Classification by Depth

| Classification | Criteria (must meet ALL listed) | Tissue Involved |
|---|---|---|
| **Superficial Incisional SSI** | Infection within 30 days of surgery AND involves only skin and subcutaneous tissue AND at least one of: (1) purulent drainage from the incision, (2) organisms identified from aseptically obtained wound culture, (3) incision deliberately opened by surgeon due to signs of infection AND patient has at least one sign (pain/tenderness, swelling, erythema, warmth), (4) diagnosis of superficial SSI by surgeon or attending | Skin, subcutaneous tissue |
| **Deep Incisional SSI** | Infection within 30 days (or 90 if implant) AND involves deep soft tissues AND at least one of: (1) purulent drainage from the deep incision, (2) deep incision spontaneously dehisces or is deliberately opened by surgeon when patient has fever >38°C or localized pain/tenderness, (3) abscess found on direct exam, reoperation, or imaging | Fascia, muscle |
| **Organ/Space SSI** | Infection within 30 days (or 90 if implant) AND involves any part of the body deeper than the fascia/muscle that was opened or manipulated during surgery AND at least one of: (1) purulent drainage from a drain placed in the organ/space, (2) organisms identified from aseptically obtained culture of organ/space fluid or tissue, (3) abscess found on direct exam, reoperation, or imaging | Any anatomic site opened during surgery (e.g., peritoneal cavity, mediastinum) |

**Critical distinction**: A wound culture growing skin flora (e.g., coagulase-negative Staphylococcus from a superficial swab) without clinical signs of infection does NOT meet SSI criteria. Culture alone is insufficient — clinical criteria must be met.

---

## Step 2: Diagnostic Workup

### Clinical Assessment

| Finding | Implication | Next Step |
|---|---|---|
| Incisional erythema >2 cm from wound edge | Possible SSI; distinguish from normal postoperative erythema | Measure and document daily; obtain culture if worsening |
| Purulent drainage | Meets SSI criterion | Culture the drainage; assess depth |
| Wound dehiscence | May indicate deep SSI | Probe the wound to assess fascial integrity; CT if deep |
| Fever + leukocytosis + wound tenderness | Systemic response to SSI | Blood cultures, CT abdomen if deep/organ-space suspected |
| Fluctuance at wound site | Subcutaneous abscess | Bedside I&D vs. CT-guided drainage |

### Laboratory Studies

- CBC with differential (WBC trend)
- Blood cultures x2 (if systemic signs)
- Wound culture — tissue biopsy or deep swab technique (NOT superficial wound swab)
- Procalcitonin (to differentiate bacterial from other inflammatory causes)
- CRP (trending marker for treatment response)

### Imaging

- **CT with IV contrast**: Standard for suspected deep incisional or organ/space SSI; identifies abscess, fluid collection, gas
- **Ultrasound**: Useful for superficial fluid collections, seroma vs. abscess differentiation
- **MRI**: When CT is insufficient (e.g., spinal SSI, soft tissue extent)

---

## Step 3: Treatment by SSI Classification

### Superficial Incisional SSI

1. **Open the wound**: Remove sutures/staples over the affected area
2. **Express and culture the purulence**: Send for gram stain, aerobic/anaerobic culture
3. **Irrigate**: Saline irrigation of the wound cavity
4. **Pack open**: Moist gauze packing, wound care with dressing changes Q12-24h
5. **Antibiotics**: NOT routinely required for superficial SSI managed with adequate I&D. Add oral antibiotics only if:
   - Cellulitis extends >2 cm from wound edge
   - Systemic signs (fever, leukocytosis)
   - Immunocompromised patient
   - Prosthetic implant present
6. **Healing**: By secondary intention or delayed primary closure

### Deep Incisional SSI

1. **Open the wound to the depth of infection**: Explore to fascia
2. **Assess fascial integrity**: If fascia is intact, manage as deep wound infection. If fascia is disrupted (fascial dehiscence), urgent surgical consultation for re-closure
3. **Culture deep tissue**: Not surface swab
4. **IV antibiotics**: Empiric coverage targeting expected organisms per wound classification:
   - Clean wound SSI: Vancomycin (MRSA coverage) + cefazolin
   - GI surgery SSI: Piperacillin-tazobactam or carbapenem
5. **Drain any collection**: Bedside or CT-guided depending on depth and location
6. **NPWT**: Consider negative pressure wound therapy for large deep wounds

### Organ/Space SSI (Intra-Abdominal Abscess, Empyema, etc.)

1. **Source control**: The priority — either percutaneous CT-guided drainage or operative washout
2. **IV antibiotics**: Broad-spectrum empiric coverage, then narrow based on culture
3. **Repeat imaging**: 48-72h after drainage to confirm adequacy
4. **Interventional radiology consultation**: For percutaneous drainage of accessible collections
5. **Operative management**: Required when percutaneous drainage is insufficient, when there is diffuse peritonitis, or when the source requires operative repair (e.g., anastomotic leak)

---

## Step 4: Antibiotic Selection and Duration

### Empiric Antibiotic Selection

| SSI Type | Likely Organisms | Empiric Regimen |
|---|---|---|
| Clean wound | S. aureus (including MRSA), coag-neg Staph, Strep | Vancomycin ± cefazolin |
| Clean-contaminated (GI) | Gram-negatives, anaerobes, Enterococcus | Piperacillin-tazobactam |
| Contaminated/Dirty | Polymicrobial (gram-neg, anaerobes, Enterococcus) | Meropenem or piperacillin-tazobactam + vancomycin |
| Prosthetic implant | S. aureus, S. epidermidis, Propionibacterium | Vancomycin + rifampin (if retaining implant) |

### Duration Guidelines

- **Superficial SSI with adequate I&D, no cellulitis**: No antibiotics or 5-7 days oral
- **Deep incisional SSI with adequate source control**: 7-10 days IV, then oral step-down
- **Organ/space SSI with adequate source control**: 4-7 days after source control (per STOP-IT trial for intra-abdominal infections)
- **Prosthetic implant infection**: 6 weeks IV if retaining implant; consult infectious disease

Narrow antibiotics based on culture and sensitivity results. Document de-escalation rationale.

---

## Step 5: Reporting and Prevention

### Mandatory Reporting

1. **NHSN surveillance**: Report all SSIs meeting CDC criteria through the NHSN system. Include:
   - Procedure code (NHSN operative procedure category)
   - SSI classification (superficial, deep, organ/space)
   - Date of event
   - Organism(s) identified
   - Whether the event was detected during readmission
2. **ACS NSQIP**: Report as a 30-day surgical outcome
3. **Institutional reporting**: Report to infection control per institutional protocol
4. **State reporting**: Many states mandate SSI reporting for specific procedure categories (e.g., colon surgery, CABG, hip/knee arthroplasty)

### SSI Prevention Bundle (for future cases)

| Element | Evidence |
|---|---|
| Appropriate antibiotic prophylaxis (correct agent, dose, timing, redosing) | SCIP/CMS core measure |
| Preoperative chlorhexidine bathing | Reduces skin colonization |
| Surgical site hair removal by clipping (not shaving) | Shaving increases SSI risk |
| Normothermia maintenance (≥36°C) | Hypothermia impairs neutrophil function |
| Perioperative glucose control (<180 mg/dL) | Hyperglycemia impairs immune function |
| Supplemental oxygen | Controversial; institutional discretion |
| Wound protector for GI surgery | Reduces superficial SSI in contaminated cases |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Does the SSI classification (superficial, deep, organ/space) meet CDC/NHSN criteria with all required elements documented?
2. Has the wound been cultured appropriately (tissue/deep technique, not superficial swab)?
3. Is the antibiotic regimen appropriate for the SSI type and being de-escalated based on culture data?
4. Has source control been achieved (drainage, debridement, or reoperation)?
5. Has the SSI been reported through all required systems (NHSN, NSQIP, institutional, state)?

---

## Quality Audit

- [ ] SSI identified within the NHSN surveillance window (30 or 90 days)
- [ ] CDC/NHSN classification criteria met and documented
- [ ] SSI depth classified (superficial, deep, organ/space) with supporting evidence
- [ ] Wound culture obtained using appropriate technique (tissue biopsy or Levine)
- [ ] Imaging obtained for suspected deep or organ/space SSI
- [ ] Source control achieved (wound opened, abscess drained, or reoperation)
- [ ] Empiric antibiotics appropriate for wound class and likely organisms
- [ ] Antibiotics de-escalated based on culture and sensitivity data
- [ ] Antibiotic duration documented with rationale
- [ ] SSI reported to NHSN per surveillance protocol
- [ ] SSI reported to ACS NSQIP as 30-day outcome
- [ ] Institutional infection control notified
- [ ] SSI prevention bundle compliance reviewed for the index case
- [ ] Case flagged for M&M review if preventable factors identified

---

## Guidelines

1. Use CDC/NHSN definitions strictly for classification and reporting — institutional definitions that differ from NHSN create data inconsistencies and audit risk.
2. A positive wound culture alone does NOT constitute an SSI. Clinical criteria (purulence, dehiscence with clinical signs, or abscess) must be met.
3. Source control is the cornerstone of SSI treatment. Antibiotics without adequate source control (drainage, debridement) will fail.
4. Duration of antibiotics after adequate source control should follow the STOP-IT trial principle: 4 days after source control for intra-abdominal infections is as effective as longer courses.
5. De-escalate antibiotics based on culture data within 48-72 hours. Prolonged broad-spectrum therapy drives resistance and C. difficile infection.
6. For prosthetic implant infections, involve infectious disease early — implant retention vs. removal decisions require specialized assessment.
7. Review the SSI prevention bundle compliance for every SSI case. If the prophylactic antibiotic was late, the wrong agent, or was extended beyond 24 hours, document the compliance failure for quality improvement.
