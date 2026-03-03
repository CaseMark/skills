---
name: coding-medical-encounters
description: Assigns ICD-10-CM diagnosis codes and CPT/HCPCS procedure codes with supporting documentation validation. Use when coding medical visits, selecting diagnosis codes, or assigning procedure codes.
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

# Coding Medical Encounters

Assigns ICD-10-CM diagnosis codes and CPT/HCPCS procedure codes to clinical encounters. Validates documentation sufficiency and ensures sequencing compliance.

## Related Skills

| Skill | Use When |
|-------|----------|
| `auditing-coding-accuracy` | Post-coding accuracy review or compliance audit |
| `managing-evaluation-management-coding` | Deep E/M level selection questions |
| `managing-modifier-applications` | Complex modifier stacking scenarios |
| `managing-bundling-rules` | NCCI edit resolution or unbundling questions |
| `managing-cdi-programs` | Documentation gaps require provider queries |

## Why This Skill Exists

Every code assigned to a medical encounter has downstream impact:

- **Revenue** — incorrect codes cause denials, underpayment, or overpayment
- **Compliance** — upcoding and unbundling trigger OIG audits and False Claims Act liability
- **Data quality** — HCC risk adjustment, quality measures, and population health analytics depend on accurate coding
- **Legal defensibility** — "if it's not documented, it didn't happen" is the foundational coding principle

This skill enforces a structured, documentation-driven coding workflow that reduces error rates and produces auditable output.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before assigning any code, confirm all inputs. Present this table and fill with user-supplied or document-derived answers:

| Input | Value | Source |
|-------|-------|--------|
| Encounter type | _(E/M, procedure, consult, telehealth, observation, etc.)_ | |
| Setting | _(outpatient, inpatient, ED, ASC, etc.)_ | |
| Provider specialty | | |
| Payer | _(Medicare, Medicaid, commercial, MA plan)_ | |
| Documentation available | _(progress note, op report, H&P, discharge summary)_ | |
| Date of service | | |
| Patient age / sex | _(affects code specificity)_ | |
| Prior coding exists? | _(yes/no — if yes, this is a review)_ | |

**Stop conditions** — Do NOT proceed if:
- Clinical documentation is incomplete or unsigned
- Encounter type is ambiguous and cannot be inferred
- No provider attestation exists for the services rendered

Flag missing items with `[QUERY PROVIDER]` and escalate to the CDI workflow (`managing-cdi-programs`).

---

## Step 1: Assign Diagnosis Codes (ICD-10-CM)

### Sequencing Rules

1. **Principal/primary diagnosis** — the condition established after study to be chiefly responsible for the encounter
2. **Secondary diagnoses** — conditions that affect treatment, require monitoring, or increase complexity
3. **Chronic conditions** — code only if addressed, treated, or affecting management during this encounter
4. **External cause codes** (V00-Y99) — required for injuries; never principal
5. **Z-codes** — for encounters driven by factors other than disease (screening, history, status)

### Specificity Requirements

Always code to the **highest level of specificity** the documentation supports:

- Laterality (right, left, bilateral) when the code set requires it
- Episode of care (initial, subsequent, sequela) for injury codes
- Trimester for obstetric codes
- Type 1 vs Type 2 for diabetes with manifestations

**Common specificity failures:**
- Using unspecified site when laterality is documented
- Defaulting to `.9` (unspecified) when a more specific code exists
- Missing 7th character extensions on injury/fracture codes

### Output: Diagnosis Code Table

| Seq | ICD-10-CM | Description | Specificity | Documentation Reference |
|-----|-----------|-------------|-------------|------------------------|
| 1 (Dx) | | | Full / Partial / `[QUERY]` | Page/section of note |
| 2 | | | | |
| 3 | | | | |

Mark any code where documentation is insufficient as `[QUERY PROVIDER]` with the specific deficiency noted.

---

## Step 2: Assign Procedure/Service Codes (CPT / HCPCS)

### E/M Code Selection (2021+ Guidelines)

For evaluation and management services, determine the level using **Medical Decision Making (MDM)**:

| MDM Element | Straightforward (99212/99202) | Low (99213/99203) | Moderate (99214/99204) | High (99215/99205) |
|-------------|-------------------------------|-------------------|------------------------|---------------------|
| **Problems** | 1 self-limited or minor | 2+ self-limited; or 1 stable chronic | 1+ chronic with exacerbation; or 2+ stable chronic; or 1 undiagnosed new problem | 1+ chronic illness with severe exacerbation; or 1 acute/chronic illness posing threat to life |
| **Data** | Minimal or none | Limited (order/review tests, review external notes) | Moderate (order/review tests + independent interpretation; or discussion with external physician) | Extensive (independent interpretation + discussion with external physician; or discussion of management with external physician) |
| **Risk** | Minimal risk of morbidity | Low risk; OTC drug management | Moderate risk; prescription drug management; minor surgery with risk factors | High risk; drug therapy requiring intensive monitoring; decisions about hospitalization; decisions about emergency surgery |

**Level requires 2 of 3 elements to meet or exceed the threshold.**

For the full MDM grid with examples, load `references/CODING-REFERENCE.md`.

### Non-E/M Procedure Codes

For procedures, surgeries, and ancillary services:

1. Identify the procedure performed from the operative/procedure note
2. Match to the most specific CPT or HCPCS Level II code
3. Check NCCI edits for bundling conflicts with other codes on the same DOS
4. Apply modifiers as needed (see Modifier section below)
5. Verify units if applicable (e.g., infusion time, lesion count)

### Modifier Application

Apply modifiers only when documentation supports them:

| Modifier | Use When | Common Error |
|----------|----------|--------------|
| -25 | Significant, separately identifiable E/M on same day as procedure | Appending without documented separate E/M |
| -59 / XE/XS/XP/XU | Distinct procedural service to bypass NCCI edit | Using -59 as a blanket unbundling tool |
| -76 | Repeat procedure by same physician, same day | Confusing with -77 (different physician) |
| -57 | Decision for major surgery during E/M | Using for minor procedures (use -25 instead) |
| -26 | Professional component only | Omitting when facility bills technical component |
| -LT / -RT | Left / right side | Missing laterality on bilateral procedures |

### Output: Procedure Code Table

| CPT/HCPCS | Description | Modifier(s) | Units | NCCI Check | Documentation Reference |
|-----------|-------------|-------------|-------|------------|------------------------|
| | | | | Pass / Conflict / N/A | Page/section |

---

## Step 3: Validate Code-to-Documentation Linkage

Every code must trace back to a specific documentation element. Complete this validation:

```
- [ ] Each diagnosis code supported by documented clinical finding, test result, or provider assessment
- [ ] Each procedure code supported by procedure note, operative report, or provider documentation
- [ ] E/M level supported by at least 2 of 3 MDM elements at or above the billed level
- [ ] Modifiers supported by documentation of distinct service, laterality, or separate encounter
- [ ] Sequencing follows principal diagnosis rules for the encounter type
- [ ] No unspecified codes when specific information is available in the documentation
- [ ] HCC-relevant diagnoses captured if payer is Medicare Advantage
```

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Present the complete coded encounter to the user before finalizing:

### Coded Encounter Summary

**Encounter:** [type] | **DOS:** [date] | **Provider:** [name] | **Payer:** [payer]

**Diagnosis Codes:**
_(Diagnosis Code Table from Step 1)_

**Procedure Codes:**
_(Procedure Code Table from Step 2)_

**Flags:**
- Queries pending: [count] — list each `[QUERY PROVIDER]` item
- NCCI conflicts: [count] — list each with resolution
- Specificity gaps: [count] — list codes that could be more specific

Ask: _"Does this coded encounter accurately reflect the services documented? Should any codes be added, removed, or changed?"_

Do NOT finalize until the user confirms.

---

## Quality Audit

Run these checks on every coded encounter before delivery:

| Check | Pass Criteria | Result |
|-------|---------------|--------|
| Specificity | No `.9` (unspecified) codes when documentation supports specificity | |
| Sequencing | Principal diagnosis is the condition chiefly responsible after study | |
| NCCI compliance | No unbundled code pairs without valid modifier and documentation | |
| Laterality | All applicable codes include laterality when documented | |
| 7th character | Injury/fracture codes include episode of care extension | |
| E/M level | MDM grid completed; 2 of 3 elements support billed level | |
| Modifier validity | Each modifier has documented clinical justification | |
| HCC capture | All HCC-eligible chronic conditions coded if MA payer | |
| Documentation linkage | Every code maps to a specific note section | |
| Upcoding risk | No codes assigned beyond what documentation supports | |

**If any check fails:** flag the specific code, cite the deficiency, and recommend corrective action before finalizing.

---

## Reference Files

| File | Contents |
|------|----------|
| `references/CODING-REFERENCE.md` | E/M MDM level grid with examples, modifier table, ICD-10-CM structure, top coding pitfalls |
