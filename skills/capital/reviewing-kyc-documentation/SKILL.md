---
name: reviewing-kyc-documentation
description: Evaluates Know Your Customer documentation packages for completeness, verifies identity documentation requirements, and assigns customer risk classifications per BSA/AML requirements. Use when onboarding new clients, conducting periodic KYC reviews, or assessing customer due diligence adequacy.
tags:
  - compliance
  - kyc
  - onboarding
metadata:
  author: casemark
  practice_areas:
    - AML Compliance
    - Client Onboarding
  document_types:
    - KYC Package
  skill_modes:
    - Checklist
    - Assessment
---

# Reviewing KYC Documentation

Assesses KYC package completeness and risk classification.

## Workflow

1. **Determine** customer type — individual, entity, trust, etc.
2. **Check** required documentation — identity, address, ownership, purpose
3. **Verify** beneficial ownership — 25% threshold (FinCEN CDD Rule)
4. **Screen** against sanctions lists (OFAC, UN, EU) and PEP databases
5. **Classify** risk — low, medium, high based on risk factors
6. **Document** deficiencies and required remediation

## Output Template

```markdown
## KYC Review

### Customer Information
| Field | Provided | Verified | Notes |
|-------|----------|----------|-------|
| Legal Name | | | |
| Date of Formation/Birth | | | |
| Address | | | |
| Tax ID (EIN/SSN) | | | |
| Business Type / Occupation | | | |
| Purpose of Account | | | |

### Beneficial Ownership (Entities)
| Owner | % Ownership | ID Verified? | Control Person? |
|-------|-----------|-------------|----------------|

### Screening Results
| List | Result | Date Screened |
|------|--------|--------------|
| OFAC SDN | [Clear/Hit] | |
| OFAC Non-SDN | [Clear/Hit] | |
| PEP Database | [Clear/Hit] | |
| Adverse Media | [Clear/Hit] | |

### Risk Classification
| Risk Factor | Assessment | Weight |
|-------------|-----------|--------|
| Customer Type | | |
| Geography | | |
| Product/Service | | |
| Transaction Patterns | | |
| **Overall Risk**: | **[Low/Medium/High]** | |

### Documentation Deficiencies
| # | Missing/Incomplete Item | Required By | Priority |
|---|------------------------|------------|---------|

### Determination
[Approve / Approve pending items / Reject / Escalate]
```

## Key Rules

- Beneficial ownership: must identify all individuals with 25%+ ownership AND one control person
- OFAC screening is mandatory — no exceptions, no grace period
- PEP (Politically Exposed Person) status requires Enhanced Due Diligence
- Risk rating drives ongoing monitoring intensity
- Re-review frequency: high-risk annually, medium every 2-3 years, low every 5 years
- Documentation must be current — expired IDs require renewal
