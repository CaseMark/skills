---
name: conducting-antimicrobial-stewardship
language: en
description: Reviews antibiotic appropriateness with spectrum optimization, de-escalation, and duration recommendations. Use when reviewing antibiotic use, recommending de-escalation, or conducting antibiotic time-outs.
tags:
  - process
  - pharmacy
metadata:
  author: casemark
  practice_areas:
    - Clinical Pharmacy
    - Pharmacy
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---

# Conducting Antimicrobial Stewardship

Reviews antibiotic appropriateness with spectrum optimization, de-escalation, and duration recommendations.

## Why This Skill Exists

Antimicrobial resistance is recognized by the WHO as one of the top ten global public health threats. In the United States, antibiotic-resistant infections cause over 35,000 deaths annually (CDC AR Threats Report). The Joint Commission requires antimicrobial stewardship programs (ASPs) for all accredited hospitals (MM.09.01.01), and CMS Conditions of Participation mandate hospital ASPs as of 2020.

Inappropriate antibiotic use—wrong spectrum, excessive duration, unnecessary empiric broad-spectrum therapy—drives Clostridioides difficile infections (CDI), multi-drug resistant organism (MDRO) emergence, and unnecessary adverse drug events. Pharmacist-led stewardship interventions including prospective audit with feedback, formulary restriction, and IV-to-PO conversion programs have demonstrated 10-30% reductions in antibiotic use, decreased CDI rates, and significant cost savings. Core metrics tracked by the National Healthcare Safety Network (NHSN) Antibiotic Use module include standardized antimicrobial administration ratio (SAAR) by agent category.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the suspected or confirmed infection site? (Default: request clinical assessment)
2. What cultures and sensitivities are available or pending? (Default: review microbiology results)
3. What empiric antibiotic(s) were started, with dose, route, and start date? (Default: pull from MAR)
4. What is the patient's allergy profile, specifically beta-lactam allergy history and severity? (Default: clarify allergy type—anaphylaxis vs. rash vs. intolerance)
5. What is the patient's renal and hepatic function? (Default: request recent labs)
6. What is the institutional antibiogram for the suspected pathogen? (Default: use current-year antibiogram)
7. Is this a de-escalation review, an antibiotic time-out (48-72h), or a new regimen evaluation? (Default: 48-72h time-out)
8. Are there MDRO risk factors (recent hospitalization, prior antibiotics, nursing home, travel)? (Default: screen from history)

### Documents to Request

- Culture and sensitivity reports (blood, urine, sputum, wound, CSF)
- Current antibiogram for the institution
- Medication administration record with antibiotic start dates
- Allergy history with reaction type documentation
- Labs: CBC with differential, procalcitonin, CRP, SCr/BUN, LFTs, lactate
- Imaging reports supporting infection diagnosis (CXR, CT)
- Prior antibiotic exposure in last 90 days

---

## Step 1: Assess Antibiotic Indication and Empiric Appropriateness

Verify that antibiotics are indicated. Rule out non-infectious causes:
- Asymptomatic bacteriuria (do NOT treat except in pregnancy or pre-urologic procedure)
- Colonization vs. infection (e.g., MRSA nares colonization, tracheostomy colonization)
- Viral syndromes not requiring antibiotics

If antibiotics are indicated, evaluate empiric selection against:
- Institutional antibiogram susceptibility rates (>80% threshold for empiric coverage)
- IDSA/ATS guidelines for the specific infection type
- Spectrum appropriateness: Is the regimen too broad for the likely pathogen?

**Common empiric regimen matching:**

| Infection | Guideline-Preferred Empiric | Avoid Unless Specific Indication |
|---|---|---|
| Community-acquired pneumonia (non-ICU) | Ceftriaxone + azithromycin OR respiratory fluoroquinolone | Vancomycin, piperacillin-tazobactam |
| Hospital-acquired pneumonia | Piperacillin-tazobactam OR cefepime ± vancomycin (if MRSA risk) | Carbapenems (unless ESBL risk) |
| Uncomplicated UTI | Nitrofurantoin, TMP-SMX | Fluoroquinolones (reserve) |
| Intra-abdominal | Ceftriaxone + metronidazole OR piperacillin-tazobactam | Carbapenems (first-line) |
| Skin/soft tissue (purulent) | TMP-SMX, doxycycline (outpatient); vancomycin (inpatient MRSA) | Broad-spectrum for simple cellulitis |

---

## Step 2: 48-72 Hour Antibiotic Time-Out

At 48-72 hours, reassess every antibiotic order:

1. **Culture results available?** De-escalate to narrowest effective spectrum based on susceptibilities
2. **Clinical improvement?** Assess temperature trend, WBC, procalcitonin trajectory, hemodynamic stability
3. **Can IV convert to PO?** Patient must be afebrile ≥24h, tolerating oral intake, GI tract functional, hemodynamically stable
4. **Duration appropriate?** Apply evidence-based duration recommendations:

| Infection | Recommended Duration | Evidence |
|---|---|---|
| Community-acquired pneumonia | 5 days (minimum, if clinically stable) | ATS/IDSA 2019 |
| Uncomplicated UTI (cystitis) | 3-5 days (nitrofurantoin 5d, TMP-SMX 3d) | IDSA 2011 |
| Complicated UTI/pyelonephritis | 5-7 days (fluoroquinolone 5d, beta-lactam 7d) | NEJM (Yahav 2018) |
| Intra-abdominal (source controlled) | 4 days | STOP-IT trial |
| Uncomplicated skin/soft tissue | 5-6 days | IDSA 2014 |
| Bacteremia (uncomplicated GNR) | 7 days | PIRATE trial |

---

## Step 3: Spectrum Optimization and De-Escalation

Apply de-escalation logic systematically:

- **Broad → narrow:** Piperacillin-tazobactam → ampicillin-sulbactam or ceftriaxone if susceptible
- **Combination → monotherapy:** Vancomycin + cefepime → cefazolin alone if MSSA identified
- **IV → PO conversion:** Bioequivalent oral options: fluoroquinolones (~100%), linezolid (~100%), metronidazole (~100%), fluconazole (~90%), TMP-SMX (~95%), doxycycline (~93%)
- **Dose optimization:** Extended-infusion beta-lactams (piperacillin-tazobactam 4h infusion, meropenem 3h infusion) for enhanced PK/PD target attainment
- **Therapeutic drug monitoring:** Vancomycin AUC/MIC-guided dosing (target AUC 400-600 mg·h/L), aminoglycoside peaks/troughs

---

## Step 4: Restricted Antibiotic Review

Evaluate use of restricted agents against institutional criteria:

**Commonly restricted agents and required justifications:**
- **Carbapenems (meropenem, ertapenem):** ESBL-producing organism, failed narrower therapy, polymicrobial with resistant profile
- **Daptomycin:** VRE bloodstream infection, MRSA with vancomycin MIC ≥2
- **Linezolid:** VRE infection, MRSA pneumonia (where vancomycin penetrates poorly)
- **Ceftazidime-avibactam:** KPC-producing CRE, documented susceptibility
- **Antifungals (micafungin, voriconazole, amphotericin B):** Documented or high-risk invasive fungal infection

---

## Step 5: Document Stewardship Intervention

Record in the medical record:
1. Intervention type: de-escalation, duration recommendation, IV-to-PO, discontinuation, dose optimization
2. Clinical rationale with culture/sensitivity reference
3. Prescriber communication method and response (accepted, modified, declined with reason)
4. Follow-up plan and reassessment date

Track metrics: antibiotic days of therapy (DOT) per 1,000 patient-days, de-escalation rate, IV-to-PO conversion rate, CDI incidence.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Were all active antibiotics reviewed against available culture and sensitivity data?
2. Is the spectrum the narrowest effective option for the identified or suspected pathogen?
3. Has antibiotic duration been set to the evidence-based minimum?
4. Were IV-to-PO conversion candidates identified and transitioned?
5. Are restricted antibiotic uses justified against institutional criteria?

---

## Quality Audit

- [ ] Antibiotic indication is documented and infection diagnosis is supported
- [ ] Empiric selection aligns with institutional antibiogram and guideline recommendations
- [ ] Culture data was reviewed and de-escalation performed when susceptibilities allowed
- [ ] Antibiotic duration follows evidence-based recommendations (not default 7-14 days)
- [ ] IV-to-PO conversion assessed using bioavailability and clinical criteria
- [ ] Beta-lactam allergy was clarified (true anaphylaxis vs. non-severe reaction)
- [ ] Dose adjusted for renal function and optimized for PK/PD targets
- [ ] Restricted antibiotic use is justified against institutional criteria
- [ ] Procalcitonin or clinical response used to support discontinuation decisions
- [ ] CDI risk assessed for patients on broad-spectrum or prolonged courses
- [ ] Intervention documented in medical record with prescriber communication
- [ ] Outcome metrics tracked (DOT, de-escalation rate, conversion rate)
- [ ] Duplicate antibiotic coverage identified and resolved (e.g., double anaerobic coverage)

---

## Guidelines

- Apply the IDSA/SHEA principle: "the right drug, right dose, right duration, right route"
- De-escalation is NOT the same as discontinuation—always narrow before stopping
- Extended-infusion beta-lactams improve outcomes in critically ill patients; recommend as default for ICU
- Procalcitonin trends are more useful than single values for guiding antibiotic discontinuation
- Clarify beta-lactam allergies aggressively—over 90% of reported penicillin allergies are not true IgE-mediated
- Do not treat positive cultures without clinical evidence of infection (colonization ≠ infection)
- Track and report ASP metrics to the Pharmacy and Therapeutics Committee quarterly
- Coordinate with infection prevention for MDRO surveillance and outbreak management
