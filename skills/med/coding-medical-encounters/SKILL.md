---
name: coding-medical-encounters
description: Suggests ICD-10-CM diagnosis codes and CPT/HCPCS procedure codes from clinical documentation with supporting documentation references and coding rationale. Use when coding clinical encounters, auditing coding accuracy, or preparing claims documentation.
tags:
  - coding
  - icd-10
  - cpt
  - billing
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
  document_types:
    - Coding Summary
  skill_modes:
    - Analysis
    - Coding
---

# Coding Medical Encounters

Maps clinical documentation to billing codes.

## Workflow

1. **Review** clinical documentation — identify all diagnoses and procedures
2. **Select** primary diagnosis — the condition chiefly responsible for the encounter
3. **Code** ICD-10-CM — most specific code supported by documentation
4. **Code** CPT/HCPCS — procedures and services rendered
5. **Validate** — documentation supports code specificity
6. **Check** — modifier requirements, bundling rules, medical necessity

## Output Template

```markdown
## Coding Summary

### Diagnosis Codes (ICD-10-CM)
| Order | Code | Description | Documentation Support |
|-------|------|-------------|---------------------|
| Primary | [Code] | [Description] | [Where in note] |
| Secondary | [Code] | [Description] | [Where in note] |

### Procedure Codes (CPT/HCPCS)
| Code | Description | Modifier | Documentation Support |
|------|-------------|----------|---------------------|

### E/M Level Assessment
- **Visit Type**: [New/Established, Outpatient/Inpatient]
- **MDM Complexity**: [Straightforward/Low/Moderate/High]
- **Suggested E/M**: [99213, etc.]
- **Supporting Elements**: [Number of problems, data reviewed, risk]

### Coding Notes
- [Specificity opportunities — where documentation could support a more specific code]
- [Query opportunities — where documentation is ambiguous]
```

## Key Rules

- Code only what is documented — never assume
- Use the most specific code the documentation supports
- Primary diagnosis = reason for the encounter, not the most severe condition
- Unconfirmed diagnoses in outpatient: code symptoms, not the suspected condition
- Inpatient: can code conditions described as "probable" or "suspected"
- Flag documentation gaps as CDI queries, don't fill them with assumptions
- Stay current — ICD-10 updates annually (October 1)

For ICD-10 coding conventions and guidelines, see [references/ICD10-GUIDELINES.md](references/ICD10-GUIDELINES.md).
For E/M level determination guide, see [references/EM-LEVELS.md](references/EM-LEVELS.md).
