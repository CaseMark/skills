---
name: distilling-regulatory-filings
description: Distills SEC and FINRA regulatory filings into structured summaries highlighting material disclosures, risk factors, insider transactions, and related-party dealings. Use when reviewing proxy statements, 8-Ks, Schedule 13Ds, or other regulatory filings for material information.
tags:
  - summarization
  - sec-filings
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - Compliance
    - Equity Research
  document_types:
    - 8-K
    - Proxy Statement
    - 13-D
  skill_modes:
    - Summarization
    - Analysis
---

# Distilling Regulatory Filings

Extracts material information from regulatory filings.

## Workflow

1. **Identify** filing type and triggering event
2. **Extract** material disclosures — what is being reported and why
3. **Assess** materiality — impact on company value, operations, governance
4. **Cross-reference** — does this contradict or update prior filings?
5. **Flag** — insider transactions, related-party dealings, governance changes

## Filing Types and Focus Areas

| Filing | Focus |
|--------|-------|
| 8-K | Material events (M&A, leadership, earnings, legal) |
| Proxy (DEF 14A) | Executive comp, board nominees, shareholder proposals |
| 13-D/13-G | Activist/institutional ownership changes |
| S-1/S-3 | Offerings — use of proceeds, dilution, risk factors |
| Form 4 | Insider trading activity |
| 13-F | Institutional holdings quarterly |

## Output Template

```markdown
## Filing Summary: [Company] — [Filing Type] — [Date]

### Filing Purpose
[Why this was filed — triggering event]

### Material Disclosures
| # | Disclosure | Impact Assessment |
|---|-----------|-------------------|

### Key Details
[Filing-type-specific structured extraction]

### Red Flags / Notable Items
- [Unusual provisions, related-party transactions, timing concerns]

### Implications
[What this means for investors/stakeholders]
```

## Key Rules

- 8-K item numbers indicate the type of event — always note them
- Proxy: executive compensation tables have required SEC format — extract total comp
- 13-D filings signal activist intent — note stated purpose
- Form 4: distinguish open-market purchases from option exercises and 10b5-1 plans
- Related-party transactions: always flag regardless of materiality threshold
- Filing timing relative to earnings or other events can be significant
