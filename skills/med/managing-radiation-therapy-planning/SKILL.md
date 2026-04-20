---
name: managing-radiation-therapy-planning
language: en
description: Structures radiation treatment planning documentation with dose constraints and target volumes. Use when documenting radiation plans, reviewing dose constraints, or coordinating radiation therapy.
tags:
  - management
  - oncology
  - treatment
metadata:
  author: casemark
  practice_areas:
    - Medical Oncology
    - Hematology-Oncology
    - Radiation Oncology
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Radiation Therapy Planning

Structures radiation treatment planning documentation with dose constraints and target volumes.

## Why This Skill Exists

Radiation therapy is used in approximately 50% of all cancer patients at some point during their treatment. Treatment planning requires precise documentation of target volumes, dose prescriptions, fractionation schemes, and organ-at-risk (OAR) dose constraints. Errors in radiation planning can result in catastrophic outcomes — underdosing the tumor leads to treatment failure, while overdosing normal structures causes severe or fatal toxicity.

ASTRO, AAPM, and ACR publish practice parameters and technical standards for radiation treatment planning. NRC regulations (10 CFR Part 35) govern medical use of radioactive material. Joint Commission sentinel event reporting includes radiation therapy errors. The QUANTEC (Quantitative Analysis of Normal Tissue Effects in the Clinic) publication provides the evidence base for OAR dose constraints used in treatment planning. Systematic documentation per ICRU standards ensures reproducible, auditable treatment plans.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the cancer diagnosis, stage, and treatment intent (curative, adjuvant, palliative)? (Default: [VERIFY])
2. What is the anatomic treatment site? (Default: specify primary site and involved regions)
3. What radiation modality is planned (external beam, brachytherapy, protons, SBRT/SRS)? (Default: external beam photon)
4. Is radiation being delivered concurrently with systemic therapy? If yes, specify agents. (Default: specify)
5. Has simulation been completed? Are imaging datasets available? (Default: pending)
6. Are there prior radiation treatment records? (Default: no — if yes, obtain prior dose records)
7. What is the patient's ECOG performance status? (Default: assess)
8. Are there anatomic considerations affecting planning (prosthetics, pacemakers, body habitus)? (Default: assess)

### Documents to Request

- Diagnostic imaging (CT, MRI, PET/CT) for target delineation
- Simulation CT dataset with immobilization documentation
- Pathology report with disease extent and margin status (for adjuvant RT)
- Surgical/operative report if post-operative radiation
- Prior radiation treatment records with dose summaries (critical for re-irradiation)
- NCCN guideline recommendations for RT dose and fractionation
- Relevant clinical trial protocol RT specifications if applicable
- Medical physics quality assurance documentation

---

## Step 1: Define Target Volumes per ICRU Standards

**ICRU 83 (IMRT) / ICRU 50/62 (conventional) volume definitions:**

| Volume | Definition | Determined By |
|--------|-----------|--------------|
| GTV (Gross Tumor Volume) | Demonstrable tumor on imaging and clinical exam | Imaging + clinical findings |
| CTV (Clinical Target Volume) | GTV + subclinical microscopic disease margin | Disease biology and anatomy |
| ITV (Internal Target Volume) | CTV + internal motion margin (breathing, organ filling) | 4D CT or fluoroscopy |
| PTV (Planning Target Volume) | CTV/ITV + setup uncertainty margin | Institutional setup data, typically 3–5mm for IGRT |

**Site-specific target volume guidance:**

- **Breast (whole breast):** CTV = entire ipsilateral breast tissue. PTV = CTV + 5–7mm. Boost CTV = surgical cavity + 10–15mm.
- **Lung (definitive):** GTV = primary tumor + involved nodes. CTV = GTV + 6–8mm. ITV from 4D CT. PTV = ITV + 5mm.
- **Head & neck:** GTV = primary tumor + positive nodes. CTV includes at-risk nodal levels per tumor site. PTV = CTV + 3–5mm (3mm with daily IGRT).
- **Prostate (definitive):** CTV = prostate ± seminal vesicles. PTV = CTV + 5–7mm (3–5mm posterior at rectal interface).
- **CNS (whole brain):** CTV = entire brain parenchyma to cribriform plate inferiorly.

Document each volume with the contouring reference (atlas, protocol, or institutional standard).

---

## Step 2: Prescribe Dose and Fractionation

**Common evidence-based fractionation schemes:**

| Site/Indication | Dose/Fractionation | Evidence Basis |
|----------------|-------------------|----------------|
| Breast (whole breast, conventional) | 50 Gy / 25 fractions | Standard |
| Breast (hypofractionated) | 40–42.56 Gy / 15–16 fractions | START-B, FAST-Forward trials |
| NSCLC (definitive, concurrent chemo) | 60 Gy / 30 fractions | RTOG 7301, RTOG 0617 |
| NSCLC (SBRT, peripheral T1-2) | 54 Gy / 3 fractions or 50 Gy / 5 fractions | RTOG 0236/0618 |
| Head & neck (definitive) | 70 Gy / 35 fractions (2 Gy/fx) | Standard with concurrent cisplatin |
| Prostate (conventional) | 78–81 Gy / 39–45 fractions | Dose escalation trials |
| Prostate (moderate hypofractionation) | 60 Gy / 20 fractions | HYPO-RT-PC, CHHiP trials |
| Whole brain RT | 30 Gy / 10 fractions | Standard palliative |
| Bone metastasis (palliative) | 8 Gy / 1 fraction or 30 Gy / 10 fractions | ASTRO guideline |
| Spinal cord compression | 30 Gy / 10 fractions or 20 Gy / 5 fractions | Rades et al. data |

Document the prescribed dose in Gy, number of fractions, dose per fraction, treatment technique (3D-CRT, IMRT, VMAT, SBRT/SRS), and energy (6MV, 10MV, etc.).

---

## Step 3: Apply Organ-at-Risk Dose Constraints

**Key QUANTEC-based OAR constraints:**

| Organ at Risk | Constraint | Clinical Endpoint |
|--------------|-----------|-------------------|
| Spinal cord | Dmax <45–50 Gy (conventional fractionation) | Myelopathy |
| Brainstem | Dmax <54 Gy | Necrosis |
| Optic nerves/chiasm | Dmax <54–55 Gy | Blindness |
| Parotid glands | Mean <26 Gy (at least one gland) | Xerostomia |
| Lung (bilateral) | V20 <30–35%, Mean <20 Gy | Pneumonitis |
| Heart | Mean <26 Gy, V25 <10% | Cardiac toxicity |
| Esophagus | Mean <34 Gy | Esophagitis |
| Liver | Mean <30–32 Gy, V30 <40% | RILD |
| Kidneys | Mean <18 Gy (each), V20 <32% | Nephropathy |
| Rectum | V70 <20%, V50 <50% | Proctitis |
| Bladder | V70 <35%, V65 <50% | Cystitis |
| Femoral heads | V50 <5% | Fracture/necrosis |
| Brachial plexus | Dmax <66 Gy | Plexopathy |
| Cochlea | Mean <45 Gy | Hearing loss |

For SBRT, use BED-corrected constraints (consult AAPM TG-101 or institutional SBRT constraints).

---

## Step 4: Document the Treatment Plan

The complete radiation treatment plan document includes:

1. **Clinical indication** — diagnosis, stage, treatment intent, concurrent systemic therapy
2. **Simulation details** — date, position, immobilization device, imaging (CT, MRI fusion)
3. **Target volumes** — GTV, CTV, PTV with dimensions and contouring references
4. **Prescription** — dose, fractionation, treatment technique, energy
5. **OAR constraints** — each relevant organ with dose constraint and achieved dose
6. **Plan quality metrics** — PTV D95, D2, homogeneity index, conformity index
7. **Image guidance** — IGRT frequency and method (CBCT, kV, surface guidance)
8. **Physics QA** — patient-specific QA results (IMRT/VMAT plan verification)
9. **Physician approval** — attending radiation oncologist signature and date

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are target volumes defined per ICRU standards with documented contouring references?
2. Does the prescribed dose and fractionation match evidence-based guidelines for this indication?
3. Are all relevant OAR constraints documented with achieved dose values?
4. Is prior radiation history accounted for in cumulative dose calculations?
5. Is the treatment plan signed by the attending radiation oncologist?

---

## Quality Audit

- [ ] Target volumes (GTV, CTV, PTV) defined per ICRU standards
- [ ] Contouring reference documented (atlas, protocol, or institutional standard)
- [ ] Dose prescription matches NCCN/ASTRO guideline for the indication
- [ ] Fractionation scheme supported by evidence with trial reference
- [ ] All relevant OAR constraints documented per QUANTEC
- [ ] OAR achieved doses recorded alongside constraint values
- [ ] Prior radiation dose documented and accounted for in composite plan
- [ ] Treatment technique and energy specified
- [ ] Image guidance method and frequency documented
- [ ] Patient-specific QA performed for IMRT/VMAT plans
- [ ] Concurrent systemic therapy documented with RT plan
- [ ] Simulation and immobilization details recorded
- [ ] Plan reviewed and signed by attending radiation oncologist
- [ ] Treatment summary generated for referring providers

---

## Guidelines

- Never initiate radiation treatment without documented physics QA verification of the plan
- Prior radiation dose records are essential for any re-irradiation case — cumulative dose to critical structures must be calculated
- For concurrent chemoradiation, document the specific systemic agent and dose — some agents act as radiosensitizers requiring dose modification awareness
- SBRT constraints differ substantially from conventional fractionation constraints — do not apply QUANTEC conventional constraints to SBRT plans without BED conversion
- Document any deviation from standard dose constraints with clinical justification and physician acknowledgment
- For clinical trial protocols with specific RT quality assurance requirements, complete all protocol-mandated RT documentation before treatment initiation
- Treatment interruptions >5 days should be documented with reason and compensatory plan (gap correction)
- Maintain a minimum 6-week interval between completion of prior radiation and re-irradiation to the same or adjacent field unless protocol-directed
