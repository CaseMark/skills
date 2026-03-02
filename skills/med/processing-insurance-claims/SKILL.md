---
name: processing-insurance-claims
description: Assembles insurance claim packages from encounter data with proper code assignment, modifier application, and supporting documentation. Use when preparing claims for submission, auditing claims for accuracy, or resolving claim denials.
tags:
  - operations
  - billing
  - claims
metadata:
  author: casemark
  practice_areas:
    - Revenue Cycle
    - Practice Management
  document_types:
    - Insurance Claim
  skill_modes:
    - Processing
---

# Processing Insurance Claims

Builds complete claim packages from encounter data.

## Workflow

1. **Verify** patient eligibility and benefit verification
2. **Assign** codes — ICD-10 (diagnosis) and CPT/HCPCS (procedure)
3. **Apply** modifiers — bilateral, multiple procedures, distinct services
4. **Check** medical necessity — diagnosis supports procedure
5. **Validate** — bundling rules, frequency limits, authorization requirements
6. **Package** — all supporting documentation attached

## Output Template

```markdown
## Claim Preparation

### Patient/Insurance
- **Patient**: [Name, DOB]
- **Payer**: [Insurance, ID, Group]
- **Authorization**: [Auth number if required]

### Claim Lines
| Line | CPT/HCPCS | Modifier | ICD-10 (Dx Pointer) | Units | Charges |
|------|-----------|----------|---------------------|-------|---------|

### Validation Checks
| Check | Status | Notes |
|-------|--------|-------|
| Medical necessity (dx supports px) | [Pass/Fail] | |
| Bundling/CCI edits | [Pass/Fail] | |
| Frequency limits | [Pass/Fail] | |
| Authorization | [Obtained/N/A] | |
| Timely filing | [Within limit] | |

### Supporting Documentation
- [Required attachments listed]
```

## Key Rules

- Medical necessity: every procedure code must link to a supporting diagnosis
- CCI (Correct Coding Initiative) edits: check for bundled procedures
- Modifier usage must be supported by documentation
- Timely filing deadlines vary by payer — typically 90-365 days
- Coordination of benefits: primary payer must be billed first
- Always check for prior authorization requirements before submission
