---
name: interpreting-coagulation-studies
language: en
description: Structures coagulation test interpretation with mixing studies and inhibitor identification. Use when interpreting coag panels, evaluating bleeding disorders, or analyzing mixing study results.
tags:
  - analysis
  - pathology
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Coagulation Studies

Structures coagulation test interpretation with mixing studies and inhibitor identification.

## Why This Skill Exists

Coagulation testing underpins the diagnosis and management of bleeding disorders, thrombophilia, anticoagulant therapy monitoring, and perioperative hemostasis assessment. Misinterpretation of a prolonged PTT — failing to distinguish a factor deficiency from a lupus anticoagulant or a specific factor inhibitor — can lead to inappropriate therapy: unnecessary factor replacement, missed anticoagulant monitoring, or failure to diagnose acquired hemophilia, which carries a mortality rate of 8-22%. The ISTH (International Society on Thrombosis and Haemostasis), CLSI guidelines (H47-A2, H21-A5), and CAP Coagulation (COA) checklist establish the standards for test performance, mixing study interpretation, and factor assay methodology.

Laboratories must maintain reagent-specific reference ranges, validate mixing study interpretation criteria, and participate in CAP proficiency testing for coagulation. CLIA requires documented procedures for all testing phases and competency assessment for technologists performing coagulation assays. This skill provides a systematic framework for interpreting coagulation results accurately and consistently.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Clinical indication** — Bleeding evaluation, thrombophilia workup, anticoagulant monitoring (warfarin, heparin, DOAC), pre-procedural screen, or unexplained prolonged PT/PTT? Default: unexplained prolonged PTT.
2. **Current anticoagulant therapy** — Is the patient on warfarin, heparin (UFH/LMWH), DOACs (rivaroxaban, apixaban, dabigatran), or none? Default: none; flag [VERIFY].
3. **Bleeding history** — Personal and family bleeding history, surgical history? Default: not provided.
4. **Specimen integrity** — Citrate tube fill level adequate (90-100% fill), time to centrifugation < 1 hour, lipemic or icteric? Default: adequate.
5. **Baseline results** — PT, INR, PTT, thrombin time, fibrinogen results available? Default: PT and PTT only.
6. **Prior coagulation workup** — Previous mixing studies, factor levels, lupus anticoagulant testing? Default: none on file.
7. **Platelet count** — Current platelet count (low platelets can affect some clot-based assays)? Default: within normal limits.

### Documents to Request

- Complete coagulation panel results (PT, INR, PTT, TT, fibrinogen)
- CBC with platelet count
- Medication list with anticoagulant details and timing of last dose
- Mixing study results (if performed)
- Individual factor assay levels
- Lupus anticoagulant panel results (dRVVT, PTT-LA, hexagonal phase)
- Clinical notes on bleeding episodes, surgical history, and family history
- Specimen collection and processing documentation

---

## Step 1: Initial Screening Test Interpretation

Evaluate the basic coagulation screening panel systematically:

| Test | Measures | Prolonged By |
|---|---|---|
| PT/INR | Extrinsic + common pathway (VII, X, V, II, fibrinogen) | Warfarin, vitamin K deficiency, liver disease, DIC, factor VII deficiency |
| PTT (aPTT) | Intrinsic + common pathway (XII, XI, IX, VIII, X, V, II, fibrinogen) | Heparin, factor deficiency (VIII, IX, XI, XII), lupus anticoagulant, specific inhibitor |
| Thrombin time (TT) | Fibrinogen to fibrin conversion | Heparin, dabigatran, dysfibrinogenemia, low fibrinogen, FDPs |
| Fibrinogen (Clauss) | Functional fibrinogen | DIC, liver disease, dysfibrinogenemia, L-asparaginase |

**Pattern recognition:**

| PT | PTT | TT | Fibrinogen | Likely Interpretation |
|---|---|---|---|---|
| Prolonged | Normal | Normal | Normal | Factor VII deficiency, early warfarin, mild vitamin K deficiency |
| Normal | Prolonged | Normal | Normal | Factor VIII, IX, XI, XII deficiency, lupus anticoagulant, specific inhibitor |
| Prolonged | Prolonged | Normal | Normal | Common pathway (X, V, II) deficiency, warfarin, liver disease |
| Prolonged | Prolonged | Prolonged | Low | DIC, severe liver disease, massive transfusion |
| Normal | Prolonged | Prolonged | Normal | Heparin contamination, dabigatran |

---

## Step 2: Mixing Study Performance and Interpretation

When PTT (or PT) is prolonged and the cause is unknown, perform a mixing study:

**Procedure**: Mix patient plasma 1:1 with normal pooled plasma (NPP). Test immediately and after 37°C incubation for 1-2 hours.

**Interpretation framework:**

| Immediate Mix | Incubated Mix | Interpretation |
|---|---|---|
| Corrects to normal | Remains corrected | Factor deficiency — proceed to individual factor assays |
| Corrects to normal | Prolongs again (time-dependent) | Factor VIII inhibitor (Bethesda assay indicated) |
| Does not correct | Does not correct | Lupus anticoagulant or non-specific inhibitor |
| Partial correction | Variable | Multiple factor deficiencies, weak inhibitor, or DOAC interference |

**Correction criteria**: Use the Rosner index (ICA) or institutional cutoff. Rosner index = [(Mix PTT - NPP PTT) / Patient PTT] x 100. Values > 11-15% (institution-specific) indicate failure to correct.

**Critical**: Some weak lupus anticoagulants may partially correct. If clinical suspicion for LA is high, proceed to dedicated LA testing regardless of mixing study result.

---

## Step 3: Factor Assay Interpretation

When mixing study suggests factor deficiency, order specific factor assays:

| Factor | Normal Range | Associated Condition |
|---|---|---|
| Factor VIII | 50-150% | Hemophilia A (< 1% severe, 1-5% moderate, 5-40% mild), acquired hemophilia A, von Willebrand disease type 3 |
| Factor IX | 50-150% | Hemophilia B |
| Factor XI | 60-150% | Factor XI deficiency (common in Ashkenazi Jewish population) |
| Factor XII | 50-150% | Prolonged PTT but NO clinical bleeding |
| Factor VII | 50-150% | Isolated PT prolongation |
| Factor V | 50-150% | Rare; combined with factor VIII deficiency in MCFD2/LMAN1 mutations |
| Factor II (prothrombin) | 50-150% | Rare; lupus anticoagulant-associated hypoprothrombinemia |
| vWF antigen + activity | 50-150% | von Willebrand disease (type 1, 2, 3) |

**Bethesda assay** for inhibitor quantification: Report in Bethesda Units (BU). > 5 BU = high-titer inhibitor requiring bypassing agents. < 5 BU = low-titer, may respond to high-dose factor.

---

## Step 4: Lupus Anticoagulant Evaluation

If mixing study fails to correct, evaluate for lupus anticoagulant per ISTH guidelines:

1. **Screening tests** (phospholipid-dependent, prolonged): dRVVT screen, PTT-LA (silica-based aPTT with low phospholipid).
2. **Mixing studies**: Demonstrate inhibitory activity is not corrected by NPP.
3. **Confirmatory tests** (phospholipid excess corrects the prolongation): dRVVT confirm (with added phospholipid), hexagonal phase phospholipid neutralization.
4. **Criteria for positive LA** (ISTH 2009 update): Prolonged phospholipid-dependent screening test + evidence of inhibitor (mixing study) + correction with excess phospholipid + exclusion of other coagulopathies.

**Interference alerts**: Heparin, DOACs, and elevated CRP can cause false-positive LA results. Document anticoagulant status and consider DOAC neutralization (DOAC Stop or activated charcoal adsorption) before testing.

---

## Step 5: Report Construction and Clinical Correlation

Assemble the interpretive report:

1. **Test results summary**: All coagulation values with reference ranges.
2. **Pattern analysis**: Classify the abnormality pattern (isolated PT, isolated PTT, combined, etc.).
3. **Mixing study interpretation**: Correction vs. non-correction with Rosner index calculation.
4. **Specific factor levels**: With clinical correlation to bleeding severity.
5. **Inhibitor quantification**: Bethesda titer if applicable.
6. **LA evaluation**: Positive, negative, or indeterminate per ISTH criteria.
7. **Clinical correlation statement**: Link laboratory findings to clinical presentation.
8. **Recommendations**: Further testing, hematology consultation, or monitoring plan.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Was the effect of anticoagulant therapy excluded or accounted for before attributing prolongation to factor deficiency or inhibitor?
2. Is the mixing study interpreted using a validated correction criterion (Rosner index or institutional cutoff)?
3. Are factor levels reported with correlation to clinical bleeding severity (severe, moderate, mild)?
4. Does the lupus anticoagulant assessment meet all ISTH criteria (screen, mix, confirm, exclude)?
5. Were specimen integrity issues (hemolysis, underfill, heparin contamination) addressed?

---

## Quality Audit

- [ ] Specimen adequacy verified (citrate fill volume 90-100%, processed within 1 hour)
- [ ] PT, PTT, TT, and fibrinogen performed and results documented
- [ ] Anticoagulant therapy status confirmed before interpretation
- [ ] Mixing study performed at immediate and incubated time points
- [ ] Rosner index or equivalent correction criterion calculated and documented
- [ ] Factor assays ordered based on mixing study results and clinical pattern
- [ ] Bethesda assay performed when factor inhibitor is suspected
- [ ] Lupus anticoagulant evaluated per ISTH 2009/2020 guidelines when appropriate
- [ ] DOAC interference considered and addressed with neutralization if needed
- [ ] Clinical correlation provided linking lab findings to bleeding or thrombotic history
- [ ] Hematology consultation recommended when inhibitor titer > 5 BU or rare factor deficiency identified
- [ ] All results reported with reagent-specific reference ranges
- [ ] CAP COA checklist compliance verified

---

## Guidelines

- Always confirm specimen adequacy (citrate tube fill, no clots, no hemolysis) before interpreting coagulation results; reject underfilled tubes per CLSI H21-A5
- Rule out anticoagulant effect (heparin, warfarin, DOACs) as the first step in any unexplained PT/PTT prolongation
- Perform mixing studies at both immediate and incubated (37°C, 1-2 hours) time points; a time-dependent inhibitor pattern (corrects then prolongs) is the hallmark of factor VIII inhibitors
- Use the Rosner index or an equivalent validated criterion for mixing study interpretation; visual inspection of "correction" is insufficient
- For lupus anticoagulant testing, always use at least two phospholipid-dependent screening tests from different principles (dRVVT + PTT-LA) per ISTH
- Factor XII deficiency prolongs the PTT but does NOT cause clinical bleeding; never delay surgery based solely on an isolated PTT prolongation attributable to factor XII
- Report Bethesda titer quantitatively and classify as high-titer (> 5 BU) or low-titer (< 5 BU) to guide treatment selection
- Maintain reagent lot-specific reference ranges and re-validate with each reagent or instrument change
