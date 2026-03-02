---
name: analyzing-epidemiological-data
description: Analyzes population health data to identify disease trends, risk factors, and statistical patterns with appropriate epidemiological measures. Use when reviewing public health data, calculating disease burden metrics, or interpreting population-level health statistics.
tags:
  - analysis
  - epidemiology
  - public-health
metadata:
  author: casemark
  practice_areas:
    - Public Health
    - Epidemiology
  document_types:
    - Epidemiological Analysis
  skill_modes:
    - Analysis
---

# Analyzing Epidemiological Data

Produces structured epidemiological analyses from population health data.

## Workflow

1. **Define** population and time period
2. **Calculate** key measures — incidence, prevalence, mortality rates
3. **Analyze** trends — temporal patterns, geographic variation
4. **Identify** risk factors — odds ratios, relative risk, attributable risk
5. **Assess** statistical significance and clinical significance
6. **Contextualize** — compare to benchmarks, prior periods, other populations

## Output Template

```markdown
## Epidemiological Analysis: [Condition/Outcome]

### Population
[Defined population, time period, data source]

### Key Measures
| Measure | Value | 95% CI | Comparison |
|---------|-------|--------|------------|
| Incidence rate | | | |
| Prevalence | | | |
| Mortality rate | | | |
| CFR | | | |

### Trend Analysis
[Direction, magnitude, statistical significance of trends]

### Risk Factor Analysis
| Risk Factor | Measure | Value | 95% CI | p-value |
|------------|---------|-------|--------|---------|

### Key Findings
1. [Major finding with statistical support]

### Limitations
- [Data quality, confounders, ecological fallacy risks]
```

## Key Rules

- Always report confidence intervals, not just point estimates
- Distinguish incidence from prevalence — they answer different questions
- Ecological fallacy warning: population-level associations may not apply to individuals
- Confounders must be acknowledged even if not adjustable
- Crude vs. adjusted rates — always specify
- Data source and quality assessment should accompany any analysis
