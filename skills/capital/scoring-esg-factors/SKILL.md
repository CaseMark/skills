---
name: scoring-esg-factors
description: Evaluates companies against Environmental, Social, and Governance criteria using structured scoring frameworks with methodology transparency and materiality weighting. Use when assessing ESG risk, screening investments for sustainability criteria, or preparing ESG disclosure analysis.
tags:
  - assessment
  - esg
  - sustainability
metadata:
  author: casemark
  practice_areas:
    - ESG Investing
    - Compliance
  document_types:
    - ESG Assessment
  skill_modes:
    - Assessment
    - Scoring
---

# Scoring ESG Factors

Produces structured ESG assessments with transparent methodology.

## Workflow

1. **Identify** material ESG factors for the industry (SASB materiality map)
2. **Collect** data — company disclosures, third-party ratings, news
3. **Score** each pillar — Environmental, Social, Governance
4. **Weight** by materiality — industry-specific factor importance
5. **Compare** to peers and sector benchmarks
6. **Flag** controversies and momentum (improving/deteriorating)

## Output Template

```markdown
## ESG Assessment: [Company]

### Overall Score: [X/100]
| Pillar | Score | Weight | Weighted Score | Peer Rank |
|--------|-------|--------|---------------|-----------|
| Environmental | | | | |
| Social | | | | |
| Governance | | | | |

### Environmental
| Factor | Score | Evidence | Materiality |
|--------|-------|----------|-------------|
| Carbon Emissions | | | [High/Med/Low] |
| Energy Management | | | |
| Water/Waste | | | |
| Supply Chain | | | |

### Social
| Factor | Score | Evidence | Materiality |
|--------|-------|----------|-------------|
| Labor Practices | | | |
| D&I | | | |
| Community Impact | | | |
| Data Privacy | | | |

### Governance
| Factor | Score | Evidence | Materiality |
|--------|-------|----------|-------------|
| Board Independence | | | |
| Executive Comp | | | |
| Audit/Accounting | | | |
| Shareholder Rights | | | |

### Controversies
| Controversy | Severity | Date | Status |
|------------|----------|------|--------|

### ESG Momentum: [Improving / Stable / Deteriorating]
```

## Key Rules

- Materiality varies by industry — carbon matters more for energy than software
- Use SASB materiality map as the starting framework
- Score based on disclosed data; note when scoring on absence of disclosure
- Distinguish between policies (what they say) and performance (what they do)
- Third-party rating disagreement is common — note it, don't hide it
- Greenwashing check: compare marketing claims to actual metrics
