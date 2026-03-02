---
name: auditing-hipaa-compliance
description: Evaluates systems, processes, or documentation against HIPAA technical and administrative safeguard requirements with gap identification and remediation recommendations. Use when assessing healthcare IT systems, reviewing data handling processes, or preparing for HIPAA audits.
tags:
  - compliance
  - hipaa
  - audit
metadata:
  author: casemark
  practice_areas:
    - Health IT
    - Compliance
  document_types:
    - Compliance Audit
  skill_modes:
    - Checklist
    - Assessment
---

# Auditing HIPAA Compliance

Structured HIPAA compliance assessment against 45 CFR 164 requirements.

## Workflow

1. **Scope** — identify what is being audited (system, process, department)
2. **Assess** Technical Safeguards (164.312) — access control, audit logs, integrity, auth, transmission
3. **Assess** Administrative Safeguards (164.308) — risk analysis, workforce training, incident response
4. **Assess** Physical Safeguards (164.310) — facility access, workstation security, device controls
5. **Classify** findings — by severity and required vs. addressable
6. **Recommend** remediation with priority

## Output Template

```markdown
## HIPAA Compliance Audit

### Scope
[What was assessed, date, assessor]

### Summary
- **Compliant**: [X] / [Total] requirements
- **Gaps Found**: [Count by severity]

### Findings

#### Critical (Immediate Action Required)
| # | Requirement | CFR Reference | Finding | Remediation |
|---|-----------|--------------|---------|-------------|

#### High (Fix Before Next Audit)
| # | Requirement | CFR Reference | Finding | Remediation |
|---|-----------|--------------|---------|-------------|

#### Medium / Low
[Same format]

### Remediation Priority
1. [Highest priority action]
2. [Next priority]
```

## Key Rules

- Reference specific CFR sections (e.g., "164.312(a)(1) — Access Control")
- Distinguish Required vs. Addressable specifications
- Addressable does not mean optional — it means "implement or document equivalent"
- Audit logs must cover 6-year retention minimum
- Risk assessment must be documented and current (updated annually minimum)
- This is an assessment tool — not legal compliance certification
