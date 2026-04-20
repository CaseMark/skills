---
name: coding-laboratory-services
language: en
description: Assigns laboratory CPT codes with panel construction and specimen-specific modifiers. Use when coding lab tests, building lab panels, or applying laboratory modifiers.
tags:
  - coding
  - medical-coding-and-billing
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Coded Record
  skill_modes:
    - Coding
    - Classification
---

# Coding Laboratory Services

Assigns laboratory CPT codes (80047–89398) with correct panel construction, specimen-specific modifiers, CLIA waiver requirements, reference laboratory billing rules, and medical necessity validation against LCD/NCD policies. Covers organ/disease-oriented panels, drug assays, hematology, chemistry, urinalysis, microbiology, surgical pathology, cytopathology, and molecular diagnostics.

## Why This Skill Exists

Laboratory coding requires precise understanding of panel composition rules (when to code a panel vs. individual tests), specimen modifiers, reference laboratory billing, and medical necessity requirements. Labs represent one of the highest-volume claim categories and are heavily targeted by Medicare prepayment review. CMS NCDs and LCDs restrict coverage for many lab tests to specific diagnoses — billing without meeting coverage criteria results in denial and potential fraud exposure. The 2018 PAMA (Protecting Access to Medicare Act) market-based pricing system has reduced Medicare lab reimbursement, making accurate coding critical for financial sustainability.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What laboratory tests were ordered and performed?
2. Where was the test performed? (in-house laboratory, reference laboratory, hospital lab)
3. What is the ordering provider and their NPI?
4. What specimen type was collected? (blood, urine, tissue, swab, other)
5. Is this a screening or diagnostic test? (affects coverage and diagnosis coding)
6. What is the CLIA certification level of the performing laboratory?
7. What payer covers this test? (Medicare NCD/LCD requirements vary by MAC jurisdiction)

### Documents Required

- Laboratory order with clinical indication/diagnosis
- Test results/report
- Specimen collection documentation
- CLIA certificate (waived, moderate complexity, high complexity)
- Applicable NCD/LCD policies for the tests ordered
- ABN (Advance Beneficiary Notice) if test may not be covered
- Reference laboratory agreement (if tests are sent out)
- Fee schedule for the performing laboratory

---

## Step 1 — Determine Panel vs. Individual Test Coding

Apply CPT panel composition rules strictly.

**Panel coding rules:**
- A panel code may be reported ONLY when ALL component tests in the panel are performed. If any component is missing, the panel code cannot be used — code each test individually instead.
- If ALL panel components are performed PLUS additional individual tests, report the panel code + the additional individual test codes.
- Do NOT code a panel AND separately code the individual components of that same panel — this is unbundling.

**Common panels and their components:**
- **80048 — Basic Metabolic Panel (BMP)**: Calcium, carbon dioxide, chloride, creatinine, glucose, potassium, sodium, urea nitrogen (BUN). All 8 must be performed.
- **80050 — General Health Panel**: 80053 (CMP) + 85025 (CBC with diff) + 84443 (TSH). All components must be performed.
- **80053 — Comprehensive Metabolic Panel (CMP)**: All 8 BMP components + albumin, bilirubin total, alkaline phosphatase, protein total, ALT, AST. All 14 must be performed.
- **80061 — Lipid Panel**: Total cholesterol (82465), HDL (83718), triglycerides (84478). All 3 must be performed. Note: LDL is typically calculated, not directly measured — calculated LDL is NOT a component of the panel code.
- **80076 — Hepatic Function Panel**: Albumin, bilirubin total, bilirubin direct, alkaline phosphatase, protein total, ALT, AST. All 7 must be performed.

**Partial panel scenarios:**
- If 7 of 8 BMP components are performed, code the 7 individual tests — do NOT use 80048.
- If a panel is performed plus additional tests not in the panel, report the panel code + individual codes for the extra tests. Example: CMP (80053) + magnesium (83735) = 80053 + 83735.

## Step 2 — Code Drug Testing and Therapeutic Drug Monitoring

Apply the drug testing code structure correctly.

**Presumptive drug testing (screening):**
- **80305**: Without instrument — immunoassay cup/dipstick, read by direct optical observation. Not instrument-assisted.
- **80306**: With instrument — immunoassay read by instrument-assisted direct optical observation (e.g., handheld reader).
- **80307**: Instrument chemistry analyzers (e.g., immunoassay, chromatography). One code per date of service regardless of the number of drug classes tested.
- Presumptive testing identifies the PRESENCE of a drug class — does NOT identify specific drugs or quantify levels.

**Definitive drug testing (confirmatory):**
- **80320–80377**: Specific drug/drug class codes reported per drug class confirmed.
- Each code represents a specific drug class (e.g., 80346 for benzodiazepines, 80353 for opiates).
- Report one code per drug class identified/confirmed. Multiple drug classes = multiple codes.
- Definitive testing uses mass spectrometry (GC-MS, LC-MS/MS) or similar high-specificity methods.

**Therapeutic drug monitoring (TDM):**
- **80150–80299**: Quantitative measurement of specific drug levels to manage therapy.
- Each TDM code is drug-specific (e.g., 80185 for phenytoin, 80202 for vancomycin).
- Report each drug level separately — these are not panels.

## Step 3 — Code Surgical Pathology and Cytopathology

Apply specimen-based coding for pathology services.

**Surgical pathology levels (88302–88309):**
- Level is determined by the SPECIMEN TYPE, not the provider's effort.
- **88302 (Level II)**: Gross and microscopic exam — appendix (incidental), fallopian tube (sterilization), foreskin (newborn).
- **88304 (Level III)**: Gross and microscopic — gallbladder, hernia sac, hydrocele sac, skin (excision benign lesion).
- **88305 (Level IV)**: Gross and microscopic — most biopsy specimens, bone marrow biopsy, breast biopsy, colon biopsy, liver biopsy, lung biopsy.
- **88307 (Level V)**: Gross and microscopic — breast resection, colon resection, larynx (partial/total), lung resection, kidney (nephrectomy).
- **88309 (Level VI)**: Gross and microscopic — bone resection, colon total resection, exenteration (pelvic, radical).
- Each separately identifiable specimen receives its own pathology code. Two biopsies from different sites = 2 × 88305.

**Cytopathology:**
- **88104–88108**: Cytopathology of fluids, washings, brushings.
- **88112**: Selective cellular enhancement technique (e.g., Thin Prep).
- **88141–88175**: Cervical/vaginal cytology (Pap smear) — screening vs. manual review vs. automated.
- Pap smear screening is coded with Z12.4 (screening for cervical neoplasm) as the primary diagnosis for screening tests.

## Step 4 — Apply Laboratory Modifiers

Select specimen, service, and location-specific modifiers.

- **Modifier 26 — Professional component**: The pathologist's interpretation only (for pathology codes that have professional/technical splits).
- **Modifier TC — Technical component**: The laboratory's processing, staining, and slide preparation (without interpretation).
- **Modifier 91 — Repeat clinical diagnostic lab test**: The same test repeated on the same day for clinical necessity (e.g., repeat glucose to monitor treatment). Do NOT use for reruns due to equipment malfunction, specimen problems, or quality control.
- **Modifier 59 / XS — Distinct specimen**: When the same test is performed on specimens from different anatomic sites or different specimen types on the same date.
- **Modifier QW — CLIA waived test**: Appended to codes for tests performed under a CLIA Certificate of Waiver. Required by Medicare for waived-test reimbursement.
- **Modifier 90 — Reference (outside) laboratory**: The billing entity did not perform the test but is reporting it to the payer on behalf of the performing reference laboratory.
- **Modifier 92 — Alternative laboratory platform testing**: Used for tests performed using alternative methods approved under CLIA.

## Step 5 — Validate Medical Necessity (NCD/LCD Coverage)

Confirm diagnosis codes meet coverage requirements for each test.

- CMS National Coverage Determinations (NCDs) establish nationwide coverage rules. Example: NCD 190.21 for Pap smear screening defines frequency limits (every 2 years for average risk, annually for high risk).
- Local Coverage Determinations (LCDs) vary by MAC jurisdiction and define covered diagnoses for specific lab tests.
- Each lab test must be linked to a diagnosis code that establishes medical necessity under the applicable NCD/LCD.
- Screening tests have specific Z-code diagnoses and frequency limits:
  - Screening lipid panel: Z13.220, covered annually for Medicare patients.
  - Screening PSA: Z12.5, covered annually for men age 50+.
  - Screening HbA1c: Z13.1, covered for at-risk patients.
- If a test does not meet NCD/LCD criteria, an ABN (Advance Beneficiary Notice) must be provided to the patient BEFORE the test is performed to hold the patient financially responsible.
- ABN must include: the test, the reason it may not be covered, the estimated cost, and the patient's signature and option selection.

## Step 6 — Handle Reference Laboratory Billing

Apply correct billing for tests sent to outside laboratories.

- **Direct billing by reference lab**: The reference laboratory bills the payer directly. Most common for Medicare patients (Medicare requires the performing lab to bill unless specific exceptions apply).
- **Billing by ordering provider (modifier 90)**: The ordering provider's office bills the payer and reimburses the reference lab. The ordering provider appends modifier 90 to the lab code. This model is common for commercial payers but has restrictions under Medicare.
- **Specimen collection only**: If the ordering provider only collects the specimen and sends it to a reference lab, the provider can bill:
  - 36415 — Routine venipuncture
  - 36416 — Capillary blood collection
  - P9612 — Catheterized urine specimen
  - 99000 — Handling/conveyance of specimen to reference lab (some payers)
- The reference lab performing the test bills the procedure codes.
- Under PAMA (2018+), Medicare lab reimbursement is based on market-based rates from private payer data — this affects both reference lab and in-house lab payment.

---

## Checkpoint B — Review

- [ ] Panel codes are used only when ALL component tests are performed
- [ ] No panel component is double-reported (panel + individual component for the same test)
- [ ] Drug testing codes match the testing methodology (presumptive vs. definitive)
- [ ] Surgical pathology levels match the specimen type per CPT definitions
- [ ] Modifier QW is appended to CLIA-waived tests
- [ ] Modifier 91 is used only for clinically indicated repeat tests (not reruns or QC)
- [ ] NCD/LCD medical necessity requirements are met for each test-diagnosis pair
- [ ] ABN is documented when coverage is uncertain or not met

---

## Quality Audit

- [ ] Panel construction is audited for completeness — panels are not reported with missing components
- [ ] Reference laboratory billing arrangements comply with Medicare reassignment rules
- [ ] Modifier 90 usage is tracked and verified against reference lab agreements
- [ ] Repeat test modifier (91) usage is reviewed for clinical justification
- [ ] NCD/LCD compliance rates are tracked by test category
- [ ] ABN completion rates are monitored for tests with known coverage limitations
- [ ] CLIA certificate is current and covers the complexity level of tests performed in-house

---

## Guidelines

- Follow AMA CPT Pathology and Laboratory section guidelines for code assignment
- Apply CMS Medicare Claims Processing Manual Chapter 16 for laboratory billing rules
- Reference CMS NCD and LCD databases for test-specific coverage requirements
- Follow CLIA regulations for laboratory certification and testing complexity classification
- Apply PAMA market-based pricing rules for Medicare lab fee schedule
- Never bill for tests not actually performed or resulted
- Never use a panel code when not all panel components are performed
- Mark with [VERIFY] any test-diagnosis pairing where NCD/LCD coverage is uncertain
- Include disclaimer that laboratory billing rules are payer-specific and NCD/LCD coverage varies by jurisdiction
