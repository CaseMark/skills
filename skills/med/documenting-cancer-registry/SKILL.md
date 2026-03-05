---
name: documenting-cancer-registry
description: Abstracts cancer cases for registry submission with required data elements and coding standards. Use when abstracting cancer cases, coding registry data, or documenting cancer reporting.
tags:
  - documentation
  - oncology
metadata:
  author: casemark
  practice_areas:
    - Medical Oncology
    - Hematology-Oncology
    - Radiation Oncology
  document_types:
    - Clinical Documentation
  skill_modes:
    - Documentation
---

# Documenting Cancer Registry

Abstracts cancer cases for registry submission with required data elements and coding standards.

## Why This Skill Exists

Cancer registries are mandated by law in all 50 US states and are the backbone of cancer surveillance, epidemiology, and outcomes research. The National Program of Cancer Registries (NPCR) and Surveillance, Epidemiology, and End Results (SEER) program collect standardized data on every cancer case diagnosed in the United States. Commission on Cancer (CoC) accreditation requires that cancer programs maintain a cancer registry with complete, accurate, and timely case abstraction.

Registry data elements follow strict coding standards: ICD-O-3 for topography and morphology, AJCC staging, NAACCR data dictionary, and STORE manual abstracting rules. Coding errors corrupt national surveillance data, affect facility quality metrics, and trigger CoC compliance deficiencies. CTR (Certified Tumor Registrar) professionals perform abstraction, but clinicians and AI-assisted systems increasingly support data extraction accuracy. The stakes are real: registry data informs NCI-funded research, ACS cancer statistics publications, and federal healthcare policy.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the cancer diagnosis being abstracted (primary site, histology)? (Default: [VERIFY])
2. What is the date of diagnosis per STORE manual rules? (Default: determine from first pathologic confirmation or clinical diagnosis)
3. Is this case reportable per state registry rules? (Default: verify reportability)
4. What class of case is this (analytic vs. non-analytic)? (Default: determine per CoC definitions)
5. Is this a single primary or are there multiple primaries requiring separate abstracts? (Default: apply SEER multiple primary rules)
6. What staging system applies (AJCC TNM, Ann Arbor, other disease-specific)? (Default: AJCC 8th edition for solid tumors)
7. Has first course treatment been completed or is it ongoing? (Default: document all treatments in first course)
8. What is the patient's current vital status? (Default: alive at last contact)

### Documents to Request

- Pathology reports (all biopsies, surgical specimens, cytology)
- Operative reports for all cancer surgeries
- Radiology imaging reports (CT, MRI, PET/CT, bone scan)
- Chemotherapy administration records (agents, dates, doses)
- Radiation therapy summary (fields, dose, fractionation, dates)
- Death certificate if applicable
- Consultation notes from all treating physicians
- Molecular/biomarker testing results
- Clinical trial enrollment documentation if applicable
- Discharge summaries for cancer-related hospitalizations

---

## Step 1: Determine Reportability and Case Eligibility

**Reportable conditions per NAACCR/STORE standards:**
- All invasive cancers (behavior code /3 in ICD-O-3)
- In situ cancers (behavior code /2) except in situ cervix (CIN III is not reportable as cancer)
- Benign and borderline CNS tumors (behavior codes /0 and /1 for brain and CNS)
- Pilocytic astrocytoma and other specific borderline neoplasms per site-specific rules

**Non-reportable:** Basal cell carcinoma of skin, squamous cell carcinoma of skin (except genital sites and select other sites per state rules), most benign tumors outside CNS.

**Class of case determination:**
- Class 00: Diagnosed at this facility, no treatment here or elsewhere
- Class 10: Diagnosed at this facility, all treatment here
- Class 11–14: Diagnosed at this facility, treatment partially or fully elsewhere
- Class 20–22: Diagnosed elsewhere, treatment partially or fully at this facility
- Analytic cases (classes 00–22) count toward CoC metrics; non-analytic cases (classes 30+) are abstracted but do not count toward quality measures.

---

## Step 2: Code Primary Site and Histology

**ICD-O-3 Topography (site) coding:**
- Use the most specific subsite code available (e.g., C50.4 for upper-outer quadrant of breast, not C50.9 NOS)
- When the subsite is not documented, use the NOS (.9) code for the site
- For overlapping lesions, use the .8 (overlapping) code when applicable

**ICD-O-3 Morphology (histology) coding:**
- Four-digit histology code + one-digit behavior code (e.g., 8140/3 = adenocarcinoma, malignant)
- Use the most specific histology term from the pathology report
- When multiple biopsies show different histologies at the same site, code the highest-grade or most specific histology
- Grade: 1 = well differentiated, 2 = moderately differentiated, 3 = poorly differentiated, 4 = undifferentiated, 9 = not determined

**Multiple primary rules (SEER/CoC):**
- Apply site-specific multiple primary and histology coding rules published by SEER
- Generally: different histologic groups at the same site = separate primaries; same histology at different sites = separate primaries
- Same histology at paired organs (bilateral breast) within specific time rules may be single or multiple primaries per site-specific guidelines

---

## Step 3: Abstract Required Data Elements

**NAACCR required data elements (core set):**

| Category | Key Data Elements |
|----------|-----------------|
| Patient demographics | Name, DOB, sex, race, ethnicity, SSN, address at diagnosis |
| Tumor identification | Primary site (ICD-O-3), histology, behavior, grade, laterality |
| Staging | AJCC clinical and pathologic TNM, stage group, staging basis |
| First course treatment | Surgery (site-specific surgery codes), chemotherapy (yes/no/specific agents), radiation (beam type, dose, target), hormonal therapy, immunotherapy, other |
| Treatment dates | Date of first treatment, date of each modality initiation |
| Diagnostic confirmation | Method of diagnostic confirmation (histology of primary, cytology, clinical only, etc.) |
| Biomarkers | ER, PR, HER2 (breast); PSA, Gleason (prostate); site-specific biomarkers as defined by NAACCR |
| Follow-up | Date of last contact, vital status, cancer status (NED, alive with disease, dead of disease, dead of other cause) |

**Collaborative staging / AJCC staging data items:**
- For each staging data item, record the value from the medical record using the NAACCR-defined coding scheme
- Clinical T, N, M values and pathologic T, N, M values are recorded separately
- Document the staging basis and any site-specific factors required by AJCC (e.g., PSA, Gleason for prostate; ER/PR/HER2 for breast)

---

## Step 4: Code First Course Treatment

First course of treatment includes all cancer-directed therapy administered before disease progression or recurrence:

**Surgery coding:**
- Use site-specific surgery codes (NAACCR Item #1290)
- Document surgical approach, extent of resection, margin status
- Code "no surgery" when only biopsy performed (biopsy is not treatment)

**Systemic therapy coding:**
- Chemotherapy: code as single-agent or multi-agent; record specific agents when possible
- Hormonal therapy: code separately from chemotherapy (e.g., tamoxifen, aromatase inhibitors)
- Immunotherapy: code checkpoint inhibitors, vaccines, and other immune-based treatments
- Targeted therapy: code per current NAACCR definitions (may be classified under chemotherapy or other treatment)

**Radiation therapy coding:**
- Record treatment modality (external beam, brachytherapy, radioisotopes)
- Document total dose, number of fractions, treatment dates
- Regional vs. distant radiation (palliative to metastatic site)

---

## Step 5: Complete Follow-Up Documentation

- **Date of last contact:** Most recent documented patient encounter
- **Vital status:** Alive, dead (document source: death certificate, medical record, obituary)
- **Cancer status at last contact:** No evidence of disease, alive with disease, dead of this cancer, dead of other cause
- **Recurrence information:** Document date, type (local, regional, distant), and site of first recurrence
- **Follow-up schedule:** Annual follow-up required per CoC standards; 90% follow-up rate required for accreditation

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Is the case reportable per NAACCR/state registry rules?
2. Are ICD-O-3 topography and morphology codes accurate and specific?
3. Have SEER multiple primary rules been applied correctly?
4. Is staging documented per AJCC 8th edition with all required site-specific factors?
5. Does the first course treatment coding capture all modalities administered before progression?

---

## Quality Audit

- [ ] Case reportability confirmed per NAACCR/state rules
- [ ] Class of case correctly assigned (analytic vs. non-analytic)
- [ ] ICD-O-3 topography code at most specific subsite level
- [ ] ICD-O-3 morphology code matches pathology report histology
- [ ] Behavior code correct (/2 for in situ, /3 for invasive)
- [ ] SEER multiple primary rules applied for patients with multiple cancers
- [ ] AJCC 8th edition staging complete with clinical and pathologic T, N, M
- [ ] Site-specific staging factors coded (ER/PR/HER2, PSA, Gleason, etc.)
- [ ] Date of diagnosis assigned per STORE manual rules
- [ ] First course treatment coded completely for all modalities
- [ ] Treatment dates documented for each modality
- [ ] Follow-up data current (date of last contact, vital status)
- [ ] Abstract completeness rate meets CoC standard (≥90% within 6 months of diagnosis)
- [ ] Data quality review performed before submission

---

## Guidelines

- Date of diagnosis is defined by STORE manual rules — it is NOT always the pathology report date. It may be the date of first clinical diagnosis if pathologic confirmation comes later.
- Always use the most specific ICD-O-3 code available — NOS codes should be used only when the medical record lacks specificity
- Multiple primaries are determined by published SEER rules, not clinical judgment — follow the algorithm exactly
- First course treatment ends at disease progression or recurrence, not at an arbitrary time cutoff
- Abstracts for analytic cases should be completed within 6 months of diagnosis per CoC standards
- Annual follow-up must achieve ≥90% completeness rate for CoC accreditation
- Registry data is used for national cancer statistics — coding accuracy affects public health policy and research
- When medical record documentation is ambiguous, consult with the treating physician before coding — do not infer treatment intent from incomplete records
