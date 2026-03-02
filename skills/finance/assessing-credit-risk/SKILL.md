---
name: assessing-credit-risk
description: Evaluates borrower creditworthiness using quantitative and qualitative frameworks including financial analysis, industry assessment, and management evaluation. Use when underwriting loans, preparing credit committee presentations, or monitoring existing credit exposures.
tags:
  - assessment
  - credit
  - underwriting
metadata:
  author: casemark
  practice_areas:
    - Credit Analysis
    - Commercial Lending
  document_types:
    - Credit Assessment
  skill_modes:
    - Assessment
---

# Assessing Credit Risk

Produces structured credit assessments for lending decisions.

## Workflow

1. **Profile** borrower — entity type, industry, size, history
2. **Analyze** financials — ratios, trends, cash flow adequacy
3. **Assess** industry risk — cyclicality, competitive dynamics, regulatory environment
4. **Evaluate** management — track record, strategy, governance
5. **Structure** assessment — risk rating with supporting factors
6. **Recommend** — approve/decline with conditions

## The Five C's Framework

| C | Assessment Area | Key Questions |
|---|----------------|--------------|
| Character | Management quality, track record | Payment history, legal issues, reputation |
| Capacity | Ability to repay | Cash flow analysis, debt service coverage |
| Capital | Financial cushion | Net worth, equity contribution, reserves |
| Collateral | Security for the loan | Asset quality, LTV, liquidation value |
| Conditions | External factors | Industry trends, economic cycle, regulatory |

## Output Template

```markdown
## Credit Assessment: [Borrower Name]

### Borrower Profile
| Field | Detail |
|-------|--------|
| Entity Type | |
| Industry | [NAICS code and description] |
| Years in Business | |
| Annual Revenue | |
| Requested Facility | [Type, amount, purpose] |

### Financial Summary
| Metric | Year -2 | Year -1 | Current | Trend |
|--------|---------|---------|---------|-------|
| Revenue | | | | |
| EBITDA | | | | |
| Net Income | | | | |
| Debt/EBITDA | | | | |
| DSCR | | | | |
| Current Ratio | | | | |

### Five C's Assessment
| Factor | Rating | Key Observations |
|--------|--------|-----------------|
| Character | [1-5] | |
| Capacity | [1-5] | |
| Capital | [1-5] | |
| Collateral | [1-5] | |
| Conditions | [1-5] | |

### Risk Rating: [1-10 scale with definition]

### Strengths
- [Key positive factor]

### Weaknesses / Mitigants
| Weakness | Mitigant |
|----------|---------|

### Recommendation
[Approve / Approve with conditions / Decline]
**Conditions**: [If applicable]
```

## Key Rules

- DSCR (Debt Service Coverage Ratio) is the single most important ratio — must be >1.25x minimum
- Cash flow analysis matters more than profitability for credit
- Adjusted EBITDA: add back owner compensation, one-time items, but document adjustments
- Global cash flow: include all entities under common ownership
- Concentration risk: revenue, customer, supplier, geographic
- Guarantor analysis: personal financial statements if guarantees are involved

For credit scoring methodology, see [references/CREDIT-SCORING.md](references/CREDIT-SCORING.md).
