# ICD-10-CM Coding Conventions

## General Coding Principles

1. **Code to highest specificity** — use the most specific code supported by documentation
2. **Primary diagnosis** = reason for the encounter (not necessarily the most severe condition)
3. **Sequence matters** — primary diagnosis first, then secondary conditions that affect care
4. **Code only confirmed diagnoses** in outpatient settings; "probable/suspected" coded as symptoms
5. **Inpatient exception**: Conditions described as "probable," "suspected," "likely," "questionable," "possible," or "still to be ruled out" may be coded as if confirmed

## Code Structure

```
A00.0
│││ │
│││ └─ Extension (4th-7th characters): laterality, episode, specificity
│││
││└── Subcategory (4th character)
│└─── Category (3 characters)
└──── Chapter letter
```

## Common Coding Errors

| Error | Example | Correct Approach |
|-------|---------|-----------------|
| Coding to unspecified when specificity exists | M54.5 (low back pain, unspecified) when note says "lumbar radiculopathy" | M54.16 or M54.17 (radiculopathy, lumbar/lumbosacral) |
| Coding suspected conditions in outpatient | Coding "rule out PE" as I26.99 | Code the symptoms: R06.00 (dyspnea), R07.9 (chest pain) |
| Missing laterality | M17.1 (primary osteoarthritis, unspecified knee) when note says "right knee" | M17.11 (right knee) |
| Missing 7th character | S52.001 (fracture) without episode | S52.001A (initial), S52.001D (subsequent), S52.001S (sequela) |
| Using manifestation as primary | H36 (retinal disorder in disease elsewhere) as primary | Code the underlying disease first, manifestation second |

## Combination Codes

Some conditions have combination codes that include both the condition and a common manifestation:

| Instead of Two Codes | Use Single Code |
|---------------------|----------------|
| E11 (T2DM) + separate eye code | E11.3x (T2DM with ophthalmic complications) |
| I25 (chronic IHD) + I50 (heart failure) | I25.5 (ischemic cardiomyopathy) if documented |
| J44 (COPD) + J96 (respiratory failure) | J44.1 (COPD with acute exacerbation) + J96.xx if both documented |

## Excludes Notes

| Type | Meaning | Action |
|------|---------|--------|
| **Excludes1** | "NOT CODED HERE" — mutually exclusive | Never use both codes together |
| **Excludes2** | "NOT INCLUDED HERE" — not part of this code | May use both codes together if both conditions exist |

## Z-Codes (Factors Influencing Health Status)

Use as primary diagnosis when the encounter is for something other than a disease:

| Category | Examples |
|----------|---------|
| Z00-Z13 | Screening, examinations |
| Z20-Z29 | Exposure, immunization, prophylactic measures |
| Z30-Z39 | Reproductive management |
| Z40-Z53 | Encounters for procedures and aftercare |
| Z55-Z65 | Social determinants of health |
| Z66-Z99 | Personal/family history, status codes |
