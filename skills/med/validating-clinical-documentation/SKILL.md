---
name: validating-clinical-documentation
description: Reviews clinical documentation for completeness, specificity, and compliance with CDI standards, generating queries for missing or unclear elements. Use when performing clinical documentation improvement reviews, auditing chart quality, or identifying documentation gaps.
tags:
  - analysis
  - cdi
  - documentation-improvement
metadata:
  author: casemark
  practice_areas:
    - Clinical Documentation Improvement
    - Revenue Cycle
  document_types:
    - CDI Query
  skill_modes:
    - Analysis
---

# Validating Clinical Documentation

Performs CDI review with query generation for documentation gaps.

## Workflow

1. **Review** note against documentation standards for the encounter type
2. **Check** specificity — are diagnoses coded to highest specificity?
3. **Identify** gaps — missing severity, laterality, acuity, causal relationships
4. **Generate** physician queries — specific, non-leading, compliant
5. **Assess** medical necessity — does documentation support the services billed?

## Output Template

```markdown
## CDI Review

### Document Reviewed
[Note type, date, provider, encounter type]

### Documentation Quality
| Element | Status | Notes |
|---------|--------|-------|
| Chief complaint | [Complete/Incomplete] | |
| HPI elements | [X/8 elements] | |
| Exam documentation | [Adequate/Inadequate] | |
| Assessment specificity | [Specific/Non-specific] | |
| Plan documentation | [Complete/Incomplete] | |

### CDI Queries

#### Query 1: [Topic]
- **Type**: [Clarification / Specificity / Completeness]
- **Clinical Indicator**: [What in the chart suggests more specificity is needed]
- **Query**: "[Non-leading question for the provider]"
- **Possible Responses**: [Clinically valid options]

### Impact Assessment
- **Current coding**: [What codes documentation supports now]
- **Potential coding**: [What codes could be supported with clarification]
```

## Key Rules

- Queries must be non-leading — present clinical indicators and ask for clarification
- Never suggest a specific diagnosis in a query
- Acceptable: "Can you clarify the type of heart failure?" with options
- Unacceptable: "Does the patient have systolic heart failure?"
- CDI is about accuracy, not upcoding
- Queries must be based on clinical indicators in the record
