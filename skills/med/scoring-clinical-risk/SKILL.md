---
name: scoring-clinical-risk
description: Calculates standardized clinical risk scores from patient data including HEART, Wells, CHA2DS2-VASc, MELD, CURB-65, and other validated instruments. Use when assessing patient risk stratification, calculating prognostic scores, or documenting risk-based clinical decisions.
tags:
  - assessment
  - risk-scoring
  - clinical-decision-support
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
    - Cardiology
    - Internal Medicine
  document_types:
    - Risk Assessment
  skill_modes:
    - Calculation
    - Assessment
---

# Scoring Clinical Risk

Computes validated clinical risk scores with interpretation.

## Workflow

1. **Identify** appropriate risk score for the clinical question
2. **Collect** required data elements — flag any missing inputs
3. **Calculate** score using validated criteria
4. **Interpret** result — risk category and associated recommendations
5. **Document** score with all inputs shown for auditability

## Supported Scores

| Score | Use Case | Reference |
|-------|----------|-----------|
| HEART | Chest pain risk stratification | See references |
| Wells (PE) | Pulmonary embolism probability | See references |
| Wells (DVT) | Deep vein thrombosis probability | See references |
| CHA₂DS₂-VASc | Atrial fibrillation stroke risk | See references |
| HAS-BLED | Bleeding risk in anticoagulation | See references |
| MELD/MELD-Na | Liver disease severity/transplant priority | See references |
| CURB-65 | Pneumonia severity | See references |
| APACHE II | ICU mortality prediction | See references |
| Glasgow Coma Scale | Consciousness level | See references |
| SOFA | Organ dysfunction/sepsis | See references |

## Output Template

```markdown
## Risk Score: [Score Name]

### Inputs
| Criterion | Value | Points |
|-----------|-------|--------|
| [Criterion 1] | [Patient value] | [Points assigned] |
| **Total** | | **[Total]** |

### Missing Data
- [Any required fields not available]

### Result
- **Score**: [Number]
- **Risk Category**: [Low/Moderate/High]
- **Interpretation**: [What this score means clinically]
- **Recommended Action**: [Guideline-based next step for this risk level]
```

## Key Rules

- Show all inputs and point assignments — scores must be auditable
- If a required input is missing, state the assumption made OR report range
- Use the most current validated version of each score
- Note score limitations and populations where it's not validated
- Never use a risk score as a sole decision-making tool — it supports clinical judgment

For detailed scoring criteria, see [references/RISK-SCORE-CRITERIA.md](references/RISK-SCORE-CRITERIA.md).
