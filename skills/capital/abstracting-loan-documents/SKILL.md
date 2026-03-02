---
name: abstracting-loan-documents
description: Abstracts loan agreements into structured term sheets covering interest rates, covenants, amortization schedules, default provisions, and prepayment terms. Use when reviewing loan documentation, comparing lending terms, or preparing credit committee materials.
tags:
  - abstraction
  - lending
  - debt
metadata:
  author: casemark
  practice_areas:
    - Commercial Lending
    - Debt Capital Markets
  document_types:
    - Loan Agreement
    - Term Sheet
  skill_modes:
    - Abstraction
---

# Abstracting Loan Documents

Extracts structured terms from loan agreements.

## Workflow

1. **Identify** loan type and parties
2. **Extract** economic terms — principal, rate, maturity, fees
3. **Map** covenants — financial (with specific thresholds) and non-financial
4. **Document** default provisions — events of default, cure periods, remedies
5. **Note** prepayment terms — penalties, lockout periods, yield maintenance
6. **Flag** unusual or non-standard provisions

## Output Template

```markdown
## Loan Abstract

### Parties & Structure
| Field | Value |
|-------|-------|
| Borrower | |
| Lender(s) | |
| Agent | |
| Loan Type | [Term / Revolver / LOC / Construction] |
| Commitment | |
| Maturity Date | |

### Economic Terms
| Term | Detail |
|------|--------|
| Interest Rate | [Fixed/Floating, spread, benchmark] |
| Default Rate | |
| Origination Fee | |
| Unused Fee | |
| Amortization | [Schedule or interest-only period] |

### Financial Covenants
| Covenant | Threshold | Testing Frequency |
|----------|-----------|-------------------|

### Non-Financial Covenants
- [Reporting requirements, insurance, permitted indebtedness, etc.]

### Events of Default
| Event | Cure Period | Cross-Default? |
|-------|-----------|---------------|

### Prepayment
| Period | Penalty/Premium |
|--------|----------------|

### Security / Collateral
[Description of pledged assets]

### Notable / Non-Standard Provisions
- [Anything unusual]
```

## Key Rules

- Interest rate: specify benchmark (SOFR, Prime), spread, floor, and cap
- Covenants: capture exact thresholds and testing dates, not just "leverage ratio"
- Cross-default provisions: note triggers from other agreements
- Change of control provisions: often buried but critical
- Subordination: note where this debt sits in the capital structure
- Material adverse change (MAC) clauses: note the definition scope
