---
name: benchmarking-portfolio-performance
description: Analyzes portfolio returns against benchmarks with attribution analysis, risk-adjusted metrics, and factor exposure breakdown. Use when evaluating investment performance, preparing quarterly client reviews, or assessing manager skill.
tags:
  - analysis
  - portfolio
  - performance
metadata:
  author: casemark
  practice_areas:
    - Investment Management
    - Wealth Management
  document_types:
    - Performance Report
  skill_modes:
    - Analysis
    - Calculation
---

# Benchmarking Portfolio Performance

Produces structured performance attribution and risk analysis.

## Workflow

1. **Calculate** returns — total return, time-weighted, money-weighted
2. **Compare** to benchmark — absolute and relative performance
3. **Attribute** — what drove returns (allocation, selection, interaction)
4. **Risk-adjust** — Sharpe, Sortino, Information Ratio, Treynor
5. **Analyze** factor exposures — style, size, sector, geography
6. **Assess** consistency — rolling returns, drawdowns, up/down capture

## Output Template

```markdown
## Portfolio Performance Review: [Portfolio Name] — [Period]

### Return Summary
| Period | Portfolio | Benchmark | Excess | Ranking |
|--------|-----------|-----------|--------|---------|
| QTD | | | | |
| YTD | | | | |
| 1-Year | | | | |
| 3-Year Ann. | | | | |
| Since Inception | | | | |

### Risk Metrics
| Metric | Portfolio | Benchmark |
|--------|-----------|-----------|
| Volatility (Ann.) | | |
| Sharpe Ratio | | |
| Sortino Ratio | | |
| Max Drawdown | | |
| Beta | | |
| Alpha | | |
| Information Ratio | | |
| Tracking Error | | |
| Up Capture | | |
| Down Capture | | |

### Attribution Analysis
| Sector/Factor | Allocation Effect | Selection Effect | Total Effect |
|--------------|-------------------|-----------------|-------------|

### Top/Bottom Contributors
| Holding | Weight | Return | Contribution |
|---------|--------|--------|-------------|

### Assessment
[Performance narrative — skill vs. luck vs. factor exposure]
```

## Key Rules

- Time-weighted returns for manager evaluation; money-weighted for investor experience
- Risk-adjusted returns matter more than raw returns — always include Sharpe minimum
- Attribution must sum to the excess return (allocation + selection + interaction = alpha)
- Benchmark appropriateness: flag if benchmark doesn't match investment mandate
- Survivorship bias: note if comparing to indices that don't include failed companies
- Short periods (<3 years) have limited statistical significance for skill assessment
