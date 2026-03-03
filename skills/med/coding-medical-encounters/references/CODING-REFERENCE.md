# Coding Medical Encounters — Reference

Detailed reference tables for ICD-10-CM, CPT E/M coding, modifiers, and common pitfalls. Load this file when you need specifics beyond the main skill workflow.

---

## ICD-10-CM Code Structure

ICD-10-CM codes are 3–7 characters in length, alphanumeric, with the following structure:

```
X  XX  .  X  X  X  X
│  │      │  │  │  └─ 7th character: extension (episode of care, fetus ID)
│  │      │  │  └──── 6th character: additional specificity
│  │      │  └─────── 5th character: additional specificity
│  │      └────────── 4th character: additional specificity (after decimal)
│  └───────────────── 2nd–3rd characters: category detail
└──────────────────── 1st character: chapter/body system (alpha, A-Z except U)
```

### Chapter Overview

| Range | Body System / Category |
|-------|----------------------|
| A00-B99 | Infectious and parasitic diseases |
| C00-D49 | Neoplasms |
| D50-D89 | Blood and immune mechanism diseases |
| E00-E89 | Endocrine, nutritional, and metabolic diseases |
| F01-F99 | Mental, behavioral, and neurodevelopmental disorders |
| G00-G99 | Nervous system diseases |
| H00-H59 | Eye and adnexa diseases |
| H60-H95 | Ear and mastoid process diseases |
| I00-I99 | Circulatory system diseases |
| J00-J99 | Respiratory system diseases |
| K00-K95 | Digestive system diseases |
| M00-M99 | Musculoskeletal and connective tissue diseases |
| N00-N99 | Genitourinary system diseases |
| O00-O9A | Pregnancy, childbirth, and puerperium |
| R00-R99 | Symptoms, signs, abnormal findings |
| S00-T88 | Injury, poisoning, external causes |
| V00-Y99 | External causes of morbidity |
| Z00-Z99 | Factors influencing health status and contact with services |

### 7th Character Extensions (Injury Codes S00-T88)

| Character | Meaning |
|-----------|---------|
| A | Initial encounter |
| D | Subsequent encounter |
| S | Sequela |
| G | Subsequent encounter for fracture with delayed healing |
| K | Subsequent encounter for fracture with nonunion |
| P | Subsequent encounter for fracture with malunion |

**Rule:** If a code requires a 7th character but has fewer than 6 characters, fill with placeholder `X` (e.g., `S52.001A` for a specific fracture, but `T36.0X5A` when the 5th/6th are placeholders).

---

## E/M Medical Decision Making (MDM) Grid — 2021 Guidelines

Level is determined by the **highest 2 of 3 elements**. One element can be below threshold.

### Number and Complexity of Problems Addressed

| Level | Criteria | Examples |
|-------|----------|----------|
| **Straightforward** | 1 self-limited or minor problem | Insect bite, cold sore, medication refill for stable condition |
| **Low** | 2+ self-limited/minor; OR 1 stable chronic illness; OR 1 acute uncomplicated illness/injury | URI + allergic rhinitis; controlled HTN check; ankle sprain |
| **Moderate** | 1+ chronic illness with mild exacerbation, progression, or side effects of treatment; OR 2+ stable chronic illnesses; OR 1 undiagnosed new problem with uncertain prognosis; OR 1 acute illness with systemic symptoms; OR 1 acute complicated injury | COPD exacerbation; DM2 + HTN + hyperlipidemia; new breast lump; pyelonephritis; complex laceration |
| **High** | 1+ chronic illness with severe exacerbation, progression, or side effects of treatment; OR 1 acute or chronic illness or injury that poses a threat to life or bodily function | Acute MI; stroke; DKA; acute respiratory failure; suspected malignancy staging |

### Amount and/or Complexity of Data Reviewed and Analyzed

| Level | Criteria |
|-------|----------|
| **Straightforward** | Minimal or none |
| **Low** | Must meet **1 of 2** categories: _(Category 1)_ Order and review of tests; OR _(Category 2)_ Review of prior external notes or data; or order tests from external source; or discuss with external physician/QHP |
| **Moderate** | Must meet **1 of 3** categories: _(Category 1)_ Order and review tests + independent interpretation of test; OR _(Category 2)_ Review prior external notes + independent interpretation; OR _(Category 3)_ Discussion of management with external physician/QHP |
| **High** | Must meet **2 of 3** categories: _(Category 1)_ Order and review tests + independent interpretation; _(Category 2)_ Review prior external notes + independent interpretation; _(Category 3)_ Discussion of management with external physician/QHP |

### Risk of Complications and/or Morbidity or Mortality

| Level | Criteria | Examples |
|-------|----------|----------|
| **Straightforward** | Minimal risk of morbidity from additional diagnostic testing or treatment | OTC drugs, rest, elastic bandages |
| **Low** | Low risk | OTC drugs; minor surgery without risk factors; physical/occupational therapy |
| **Moderate** | Moderate risk | Prescription drug management; minor surgery with identified risk factors; elective major surgery without risk factors; diagnostic procedures with identified risk factors; treatment significantly limited by social determinants of health |
| **High** | High risk | Drug therapy requiring intensive monitoring for toxicity; decision regarding emergency major surgery; decision regarding hospitalization; decision regarding DNR or de-escalation of care due to poor prognosis; parenteral controlled substances |

### E/M Code Quick-Select (Outpatient)

| Level | New Patient | Established Patient | MDM Level Required |
|-------|-------------|--------------------|--------------------|
| 1 | — | 99211 | May not require physician presence |
| 2 | 99202 | 99212 | Straightforward |
| 3 | 99203 | 99213 | Low |
| 4 | 99204 | 99214 | Moderate |
| 5 | 99205 | 99215 | High |

**Note:** 99201 was deleted in 2021. New patient encounters start at 99202.

### E/M Code Quick-Select (Inpatient/Observation)

| Level | Initial | Subsequent | Discharge |
|-------|---------|------------|-----------|
| Low | 99221 | 99231 | 99238 (≤30 min) |
| Moderate | 99222 | 99232 | 99239 (>30 min) |
| High | 99223 | 99233 | — |

---

## Common Modifiers Reference

| Modifier | Name | Use Case | Key Rules |
|----------|------|----------|-----------|
| -25 | Significant, Separately Identifiable E/M | E/M on same day as minor procedure (0- or 10-day global) | Documentation must show the E/M was above and beyond the decision/work of the procedure |
| -57 | Decision for Surgery | E/M where decision for major surgery (90-day global) was made | Only for major procedures; use -25 for minor |
| -59 | Distinct Procedural Service | Bypass NCCI bundling edit when services are truly distinct | Last resort — use X{EPSU} modifiers first; must document different session, site, organ, or incision |
| -XE | Separate Encounter | Distinct NCCI service performed at a different encounter on same day | Subset of -59 |
| -XS | Separate Structure | Distinct NCCI service on a different organ/structure | Subset of -59 |
| -XP | Separate Practitioner | Distinct NCCI service by a different practitioner | Subset of -59 |
| -XU | Unusual Non-Overlapping Service | Service not ordinarily reported together but appropriate in the circumstance | Subset of -59 |
| -76 | Repeat Procedure, Same Physician | Same procedure repeated on same day by same provider | Must document medical necessity for repeat |
| -77 | Repeat Procedure, Different Physician | Same procedure repeated on same day by different provider | |
| -26 | Professional Component | Physician interpretation only (facility bills -TC) | Required when global service is split |
| -TC | Technical Component | Facility/equipment cost only | Pair with -26 on professional claim |
| -LT | Left Side | Identifies laterality | Must match documentation and diagnosis laterality |
| -RT | Right Side | Identifies laterality | |
| -50 | Bilateral Procedure | Same procedure on both sides | Some payers want -50 on one line; others want -LT/-RT on two lines — check payer rules |
| -51 | Multiple Procedures | 2+ procedures in same session | May trigger payment reduction; some codes are -51 exempt |
| -52 | Reduced Services | Procedure partially completed | Document why full service was not rendered |
| -22 | Increased Procedural Services | Substantially greater effort than typical | Requires operative note documentation of what made it more complex; send report with claim |

---

## Top Coding Pitfalls

### 1. Upcoding

**What:** Assigning a higher-level code than documentation supports.
**Example:** Billing 99215 when MDM only supports moderate complexity (99214).
**Prevention:** Complete the MDM grid — 2 of 3 elements must meet the billed level.

### 2. Unbundling

**What:** Billing component codes separately when a comprehensive code exists.
**Example:** Billing CBC components individually instead of 85025 (CBC with differential).
**Prevention:** Check NCCI edit pairs before finalizing. Use CMS NCCI lookup tool.

### 3. Missing Specificity

**What:** Using an unspecified code when the documentation contains specific information.
**Example:** Coding `M54.5` (low back pain, unspecified) when the note says "right-sided lumbosacral radiculopathy" → `M54.41`.
**Prevention:** Read the full note. Check for laterality, acuity, type, and anatomic site.

### 4. Incorrect Sequencing

**What:** Listing a secondary diagnosis as the principal.
**Example:** Coding hypertension as principal when the patient presented for a diabetic foot ulcer.
**Prevention:** Ask "what was the reason for the encounter?" — that condition is principal.

### 5. Missing 7th Character

**What:** Omitting required 7th character on injury, fracture, and obstetric codes.
**Example:** Submitting `S72.001` instead of `S72.001A` for initial femur fracture encounter.
**Prevention:** Any S/T code requires episode of care extension. Use `X` placeholder when needed.

### 6. Modifier -25 Abuse

**What:** Appending -25 to E/M without a separately identifiable service documented.
**Example:** Billing 99213-25 with a wart destruction when the E/M note only discusses the wart.
**Prevention:** The E/M must address a condition above and beyond the procedure — separate HPI, exam, and assessment for the distinct problem.

### 7. Ignoring HCC Capture (Medicare Advantage)

**What:** Failing to code chronic conditions that are HCC-relevant when they are addressed.
**Example:** Patient with documented CKD Stage 3, COPD, and major depression — only coding the acute visit reason.
**Prevention:** For MA payers, code all chronic conditions that are monitored, evaluated, assessed, or treated during the encounter.

### 8. Copy-Forward Documentation

**What:** Coding from cloned/templated notes that don't reflect the actual encounter.
**Example:** Note says "lungs clear" via copy-forward but patient presented with pneumonia.
**Prevention:** Verify documentation is encounter-specific. Flag cloned language patterns and query the provider.

---

## NCCI Edit Quick-Reference

The National Correct Coding Initiative (NCCI) maintains two types of edit tables:

| Edit Type | Meaning | Action |
|-----------|---------|--------|
| **Column 1 / Column 2** | Column 2 code is a component of Column 1 — cannot bill separately | Check modifier indicator: 0 = never separate; 1 = modifier may override |
| **Mutually Exclusive** | Codes cannot reasonably be performed together in the same session | Generally cannot override even with modifier |

**Modifier indicator values:**
- `0` — No modifier allowed; codes are always bundled
- `1` — Modifier allowed to indicate distinct service (use -59 or X{EPSU})
- `9` — Not applicable (edit deleted)

**Lookup:** CMS NCCI edit files are updated quarterly. Always verify against the current effective date.
