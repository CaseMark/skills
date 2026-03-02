---
name: coordinating-transitions-of-care
description: Produces transition-of-care packages with medication reconciliation, follow-up coordination, and patient education for care setting changes. Use when discharging patients, transferring between facilities, or transitioning from inpatient to outpatient care.
tags:
  - operations
  - care-coordination
  - patient-safety
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Care Management
  document_types:
    - Transition of Care Package
  skill_modes:
    - Checklist
    - Coordination
---

# Coordinating Transitions of Care

Manages information flow during care setting transitions.

## Workflow

1. **Reconcile** medications — compare admission, inpatient, and discharge lists
2. **Coordinate** follow-up — appointments, pending tests, outstanding referrals
3. **Communicate** to receiving provider — structured handoff
4. **Educate** patient — condition, medications, warning signs, contacts
5. **Verify** — patient/caregiver teach-back of key points

## Output Template

```markdown
## Transition of Care Package

### Transition Type
[Inpatient → Home / Inpatient → SNF / ED → Home / etc.]

### Medication Reconciliation
| Medication | Pre-Admission | During Stay | At Discharge | Change |
|-----------|--------------|-------------|-------------|--------|

### Pending Items
| Item | Expected Date | Responsible Provider | Action Required |
|------|--------------|---------------------|-----------------|

### Follow-Up Appointments
| Provider | Date/Timeframe | Purpose | Scheduled? |
|----------|---------------|---------|------------|

### Receiving Provider Summary
[Structured handoff: reason for care, course, current status, pending items, anticipated needs]

### Patient Education Checklist
- [ ] Medication changes reviewed
- [ ] Warning signs discussed
- [ ] Follow-up appointments confirmed
- [ ] Emergency contact provided
- [ ] Teach-back completed
```

## Key Rules

- Medication reconciliation is the highest-risk element — compare all three lists
- "Pending results" must have clear ownership — who follows up
- Patient must know who to call and when to seek emergency care
- SNF/rehab transfers need functional status and therapy recommendations
- 48-hour post-discharge callback reduces readmissions — include in plan
