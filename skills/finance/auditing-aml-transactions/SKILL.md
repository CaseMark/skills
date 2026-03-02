---
name: auditing-aml-transactions
description: Screens transaction data for anti-money laundering red flags, generates suspicious activity analysis, and structures SAR narrative elements using FATF and FinCEN frameworks. Use when reviewing transaction patterns, preparing suspicious activity reports, or conducting AML compliance reviews.
tags:
  - compliance
  - aml
  - financial-crime
metadata:
  author: casemark
  practice_areas:
    - AML Compliance
    - Financial Crime
  document_types:
    - SAR
    - Transaction Review
  skill_modes:
    - Audit
    - Assessment
---

# Auditing AML Transactions

Identifies suspicious patterns and structures AML analysis.

## Workflow

1. **Screen** transactions against red flag typologies
2. **Analyze** patterns — velocity, structuring, layering, geographic risk
3. **Profile** customer activity against expected behavior
4. **Assess** risk level — low, medium, high
5. **Document** findings for SAR filing decision
6. **Draft** SAR narrative elements if filing threshold met

## Red Flag Categories

| Category | Indicators |
|----------|-----------|
| Structuring | Transactions just below reporting thresholds ($10K), split deposits |
| Velocity | Unusual spike in transaction volume or value |
| Geographic | Transactions involving high-risk jurisdictions (FATF list) |
| Layering | Rapid movement through multiple accounts with no business purpose |
| Round amounts | Large round-dollar transactions inconsistent with business type |
| Cash intensive | Cash activity inconsistent with stated business |
| Third party | Unexplained third-party involvement in transactions |

## Output Template

```markdown
## AML Transaction Review

### Subject
| Field | Detail |
|-------|--------|
| Customer | [Name / ID] |
| Account Type | |
| Customer Since | |
| Risk Rating | [Current] |
| Review Period | |

### Transaction Summary
| Metric | Value | Expected Range | Flag |
|--------|-------|---------------|------|
| Total Volume | | | |
| Transaction Count | | | |
| Cash Activity | | | |
| Wire Activity | | | |
| High-Risk Jurisdiction Activity | | | |

### Red Flags Identified
| # | Red Flag | Transactions | Description | Severity |
|---|----------|-------------|-------------|----------|

### Pattern Analysis
[Narrative description of suspicious patterns observed]

### Risk Assessment: [Low / Medium / High]

### Recommendation
- [ ] No further action
- [ ] Enhanced monitoring
- [ ] SAR filing recommended
- [ ] Account closure recommended

### SAR Narrative Elements (if filing)
[Who, what, when, where, why — structured for SAR filing]
```

## Key Rules

- SAR filing is mandatory within 30 days of detection for transactions >$5,000
- Do NOT tip off the customer that a SAR has been or may be filed
- Document the decision process even when deciding NOT to file
- Structuring analysis: look at patterns, not just individual transactions
- High-risk jurisdictions: reference current FATF list
- Beneficial ownership: identify who ultimately controls the funds

For AML red flag typologies, see [references/AML-RED-FLAGS.md](references/AML-RED-FLAGS.md).
