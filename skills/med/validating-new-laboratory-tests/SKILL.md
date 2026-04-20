---
name: validating-new-laboratory-tests
language: en
description: Structures test validation with precision, accuracy, linearity, and reference range establishment. Use when validating new assays, documenting method comparisons, or establishing reference ranges.
tags:
  - validation
  - pathology
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Validation Report
  skill_modes:
    - Validation
---

# Validating New Laboratory Tests

Structures test validation with precision, accuracy, linearity, and reference range establishment.

## Why This Skill Exists

Every new laboratory test, instrument, or method must be validated before patient results are reported. CLIA 42 CFR 493.1253 requires that laboratories verify or establish performance specifications for accuracy, precision, analytical measurement range (AMR), and reportable range before introducing any test. For laboratory-developed tests (LDTs) and modified FDA-cleared tests, the laboratory must perform a full analytical validation establishing these parameters from scratch. CAP accreditation checklist GEN.20371 and method-specific checklists (CHM, HEM, etc.) mandate documented validation protocols, acceptance criteria, and laboratory director approval before go-live.

The consequences of inadequate validation are severe: inaccurate results affecting patient care, CAP citations leading to corrective action requirements, CLIA sanctions up to suspension of testing, and medicolegal liability. The CLSI EP series (EP05, EP06, EP09, EP15, EP28) provides the consensus methodology for each validation study. This skill ensures that every validation study follows CLSI methodology and meets regulatory requirements.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Test/method** — What analyte and platform are being validated? Default: not specified; flag [VERIFY].
2. **Validation type** — New test (full validation), new instrument for existing test (verification), or modified method? Default: verification of FDA-cleared method.
3. **Regulatory classification** — FDA-cleared/approved, laboratory-developed test (LDT), or modified FDA-cleared? Default: FDA-cleared.
4. **Specimen types** — What specimen types will be tested (serum, plasma, whole blood, urine, CSF, other)? Default: serum.
5. **Comparator method** — What is the reference or predicate method for comparison? Default: current laboratory method.
6. **Clinical purpose** — Screening, diagnosis, monitoring, or pharmacogenomics? Default: diagnosis.
7. **Target go-live date** — When must validation be complete? Default: 60 days.

### Documents to Request

- Manufacturer's package insert with claimed performance specifications
- CLSI EP guidelines relevant to each validation study (EP05, EP06, EP09, EP15, EP28)
- Comparator method performance data (current precision, bias, AMR)
- Clinical Laboratory Improvement Advisory Committee (CLIAC) guidance for the analyte
- CAP checklist requirements for the specific test discipline
- Institutional validation protocol template
- Prior validation studies for the same analyte (if replacing an existing method)
- Proficiency testing survey results for the comparator method

---

## Step 1: Precision Study (CLSI EP05-A3)

Evaluate the repeatability and within-laboratory precision of the new method:

**Protocol:**
- Minimum 2 levels of QC material or patient pools (normal and abnormal range)
- Run each level in duplicate, 2 runs per day, for a minimum of 20 days (CLSI EP05-A3 standard protocol)
- This yields at minimum 80 data points per level

**Analysis:**

| Precision Component | Calculation | Acceptance Criteria |
|---|---|---|
| Repeatability (within-run) | SD and CV from replicates within each run | CV <= manufacturer claim |
| Within-laboratory (total) | SD and CV from all data across 20 days | CV <= manufacturer claim or clinical requirement |
| Between-day | SD component from ANOVA | Assess for systematic day-to-day variation |
| Between-run | SD component from ANOVA | Assess for systematic run-to-run variation |

**Acceptance**: Total imprecision (CV%) must be <= the manufacturer's stated precision or <= 1/4 of the total allowable error (TEa) for the analyte (per Westgard sigma-metric guidance).

---

## Step 2: Accuracy / Method Comparison Study (CLSI EP09-A3)

Compare the new method to the reference or comparator method:

**Protocol:**
- Minimum 40 patient specimens spanning the clinically relevant concentration range
- Each specimen tested by both new and comparator method within 2 hours
- Include specimens at low, normal, and high concentrations
- Test each specimen once on each method (or in duplicate if precision is a concern)

**Analysis:**
- **Deming or Passing-Bablok regression**: Slope (target 0.9-1.1), intercept (target near 0), and correlation coefficient (r >= 0.975).
- **Bland-Altman difference plot**: Mean bias and 95% limits of agreement.
- **Medical decision point bias**: Calculate bias at each clinical decision point and compare to TEa.

| Metric | Acceptable | Marginal | Unacceptable |
|---|---|---|---|
| Slope | 0.95-1.05 | 0.90-0.95 or 1.05-1.10 | < 0.90 or > 1.10 |
| Correlation (r) | >= 0.975 | 0.95-0.975 | < 0.95 |
| Bias at decision point | < 1/2 TEa | 1/2 to 1x TEa | > TEa |

---

## Step 3: Analytical Measurement Range (AMR) and Linearity (CLSI EP06-A)

Verify the analytical measurement range (reportable without dilution):

**Protocol:**
- Prepare at minimum 5 concentration levels spanning the manufacturer's claimed AMR
- Use certified reference material, calibrator dilutions, or spiked patient pools
- Each level tested in triplicate (minimum) or quadruplicate
- Include concentrations at and beyond the claimed AMR boundaries

**Analysis:**
- Plot measured vs. expected values
- Calculate polynomial regression; compare first-order (linear) to higher-order models
- Non-linearity: If the difference between the linear and polynomial fit exceeds the TEa at any point, the AMR is narrowed to the linear range

**Reportable Range**: If the clinical range extends beyond the AMR, validate dilution protocols. Document dilution factor and recovery at each validated dilution step.

---

## Step 4: Reference Range Verification (CLSI EP28-A3c)

Verify that the manufacturer's stated reference range is applicable to the laboratory's patient population:

**Protocol — Verification (FDA-cleared tests):**
- Test a minimum of 20 healthy individuals representative of the patient population (per CLSI EP28)
- If no more than 2 of 20 fall outside the manufacturer's claimed range, the reference range is verified
- If more than 2 of 20 fall outside, a full reference range study is required (120+ subjects per partition)

**Protocol — Establishment (LDTs or when verification fails):**
- Minimum 120 reference individuals per partition (e.g., male/female, pediatric/adult)
- Calculate 2.5th and 97.5th percentiles as reference limits using nonparametric methods
- Partition by age, sex, and other demographic variables as clinically appropriate

---

## Step 5: Additional Validation Studies

Perform additional studies as applicable:

- **Carryover study**: Test high-low-low sequence to detect analyte carryover between specimens. Carryover < 1% of the high-concentration value is generally acceptable.
- **Interference study (CLSI EP07)**: Test known interferents (hemolysis, lipemia, icterus, bilirubin, common drugs). Document interference thresholds.
- **Limit of detection (LoD) / Limit of quantitation (LoQ)**: For assays where clinical decisions depend on low-level detection (troponin, tumor markers, drugs of abuse).
- **Stability study**: Specimen stability at room temperature, refrigerated, and frozen conditions.
- **Specimen type comparison**: If multiple specimen types are claimed (serum vs. plasma), perform a comparison study between them.

---

## Step 6: Validation Report and Go-Live Approval

Assemble the complete validation report:

1. **Study summary**: Test name, platform, validation type, dates performed.
2. **Precision results**: CV% for each level with acceptance determination.
3. **Accuracy results**: Regression statistics, Bland-Altman analysis, decision-point bias.
4. **AMR/linearity**: Verified range with any limitations documented.
5. **Reference range**: Verified or established, with population description.
6. **Additional studies**: Carryover, interference, LoD/LoQ, stability.
7. **Limitations**: Any identified limitations affecting clinical use.
8. **Conclusion**: Statement of acceptance or rejection with rationale.
9. **Laboratory director signature**: Required for go-live approval per CLIA.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Does the precision study meet the minimum 20-day/2-run/2-level protocol per CLSI EP05?
2. Does the method comparison include at least 40 specimens spanning the clinically relevant range?
3. Is the AMR verified at a minimum of 5 concentration levels including boundary values?
4. Is the reference range verified using 20 subjects (or established using 120+ subjects for LDTs)?
5. Has the laboratory director reviewed and signed the validation report?

---

## Quality Audit

- [ ] Validation type correctly classified (verification vs. full validation vs. modification)
- [ ] Precision study follows CLSI EP05-A3 protocol (20 days, 2 runs, 2 levels)
- [ ] Total CV% meets acceptance criteria (manufacturer claim or clinical requirement)
- [ ] Method comparison includes >= 40 specimens across the concentration range
- [ ] Regression statistics and Bland-Altman analysis documented
- [ ] Bias at medical decision points compared to TEa
- [ ] AMR verified at >= 5 concentration levels per CLSI EP06
- [ ] Dilution protocol validated if reportable range exceeds AMR
- [ ] Reference range verified (20 subjects) or established (120+ subjects)
- [ ] Interference studies performed for hemolysis, lipemia, icterus
- [ ] LoD/LoQ established for analytically sensitive assays
- [ ] Validation report signed by laboratory director before go-live
- [ ] CAP checklist requirements met for the specific test discipline

---

## Guidelines

- Distinguish verification (FDA-cleared, confirming manufacturer claims) from validation (LDT or modified method, establishing specifications from scratch); the regulatory burden differs significantly
- Follow CLSI EP05-A3 exactly for precision studies: 20 days minimum, 2 runs per day, 2 replicates per run — shortcuts undermine statistical power and invite CAP citations
- Include specimens at clinical decision points in the method comparison (e.g., glucose at 126 mg/dL, HbA1c at 6.5%); demonstrating acceptable performance at decision points is more clinically meaningful than overall correlation
- When the manufacturer's reference range cannot be verified, perform a full establishment study with 120+ subjects per partition rather than adopting reference ranges from literature
- Document all deviations from the planned validation protocol and justify why the deviation does not invalidate results
- Do not go live until the laboratory director has reviewed all data and signed the validation report — this is a CLIA regulatory requirement
- Retain all raw validation data, worksheets, and statistical analyses for the life of the test system or as required by institutional policy (minimum 2 years per CLIA)
- Plan for ongoing performance monitoring after go-live: compare the first month of patient results to the comparator method if running in parallel
