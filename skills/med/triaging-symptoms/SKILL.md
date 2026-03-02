---
name: triaging-symptoms
description: Generates ranked differential diagnoses from symptom presentations with red-flag identification and urgency classification. Use when evaluating symptom complaints, building differential lists, or determining care urgency.
tags:
  - assessment
  - triage
  - differential-diagnosis
metadata:
  author: casemark
  practice_areas:
    - Emergency Medicine
    - Primary Care
  document_types:
    - Triage Assessment
  skill_modes:
    - Analysis
    - Assessment
---

# Triaging Symptoms

Produces structured differentials from symptom presentations.

## Workflow

1. **Gather** — symptom onset, duration, severity, modifying factors, associated symptoms
2. **Screen** red flags — symptoms requiring emergent evaluation
3. **Generate** differential — ranked by probability given the presentation
4. **Categorize** urgency — emergent, urgent, routine
5. **Recommend** — initial workup to narrow the differential

## Output Template

```markdown
## Symptom Triage Assessment

### Presentation
- **Chief Complaint**: [CC]
- **Onset/Duration**: [Timeline]
- **Severity**: [Scale if available]
- **Associated Symptoms**: [List]
- **Modifying Factors**: [Better/worse with]

### Red Flags
- [Any alarm symptoms identified — or "None identified"]

### Urgency: [Emergent / Urgent / Routine]

### Differential Diagnosis
| # | Diagnosis | Likelihood | Key Supporting Features |
|---|----------|-----------|----------------------|
| 1 | [Most likely] | High | [Why] |

### Recommended Workup
- [Test/evaluation to narrow differential]
```

## Key Rules

- Red flag screening ALWAYS comes before differential generation
- Rank differentials by probability, not by severity
- Include "can't miss" diagnoses even if low probability (e.g., PE in chest pain)
- Never provide a single diagnosis — always a differential list
- Explicitly state when presentation warrants emergency evaluation
- This is a decision-support tool — not a diagnosis
