---
name: condensing-credit-reports
description: Condenses full credit reports into risk-focused summaries with score drivers, derogatory items, utilization analysis, and trend indicators. Use when reviewing borrower creditworthiness, preparing loan applications, or assessing consumer credit profiles.
tags:
  - summarization
  - credit
  - risk-assessment
metadata:
  author: casemark
  practice_areas:
    - Consumer Lending
    - Credit Analysis
  document_types:
    - Credit Report
  skill_modes:
    - Summarization
---

# Condensing Credit Reports

Produces risk-focused credit summaries from detailed reports.

## Workflow

1. **Extract** scores — FICO, VantageScore across bureaus
2. **Identify** score drivers — positive and negative factors
3. **Summarize** tradelines — total accounts, types, balances, limits
4. **Flag** derogatory items — collections, charge-offs, bankruptcies, liens
5. **Calculate** utilization — overall and per-card
6. **Assess** trajectory — improving, stable, or deteriorating

## Output Template

```markdown
## Credit Report Summary

### Scores
| Bureau | Score | Model | Date |
|--------|-------|-------|------|

### Score Factors
**Positive**: [Top factors helping score]
**Negative**: [Top factors hurting score]

### Account Summary
| Category | Count | Total Balance | Total Limit | Utilization |
|----------|-------|--------------|------------|-------------|
| Revolving | | | | |
| Installment | | | | |
| Mortgage | | | | |

### Derogatory Items
| Item | Creditor | Amount | Date | Status |
|------|----------|--------|------|--------|

### Payment History
- **On-time rate**: [%]
- **Late payments (30/60/90+)**: [Counts]

### Risk Assessment
- **Profile**: [Excellent / Good / Fair / Poor / Very Poor]
- **Trend**: [Improving / Stable / Deteriorating]
- **Key Concerns**: [If any]
```

## Key Rules

- Report scores from all available bureaus — they can differ significantly
- Utilization >30% is a yellow flag, >50% is red
- Age of accounts matters — note average and oldest
- Hard inquiries in last 12 months indicate active credit seeking
- Distinguish between closed/paid collections and active ones
- Medical collections are treated differently under newer scoring models
