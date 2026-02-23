---
name: financial-analysis-summary
description: Generates structured summaries of financial analyses for commercial litigation, translating forensic accounting reports, economic damage calculations, and business valuations into clear formats for attorneys, judges, and juries while maintaining technical rigor. Use when summarizing expert financial reports, economic damages analyses, lost profits calculations, business valuations, or financial dispute evidence for litigation support.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Financial Analysis Summary for Litigation

Distills complex financial analyses, forensic accounting reports, and expert findings into structured summaries suitable for legal proceedings.

## Prerequisites

1. **Source financial analysis** — expert reports, forensic accounting workpapers, or economic damage studies
2. **Supporting financial records** — statements, tax returns, transaction ledgers relied upon by the expert
3. **Case context** — nature of dispute, relevant time period, applicable jurisdiction, and intended use (settlement, trial, appellate review)

## Output Structure

### 1. Executive Overview

| Element | Content |
|---|---|
| Nature of dispute | Type of financial claim or valuation question |
| Time period | Examination window with specific dates |
| Principal conclusions | Top-line damages figure or valuation range |
| Expert(s) | Name, credentials, engagement scope |

### 2. Methodology

For each analytical approach used, document:

- [ ] Method name (DCF, comparable company, lost profits, market approach, etc.)
- [ ] Plain-language explanation of the technique
- [ ] Why this method was selected for this case
- [ ] Applicable professional standards (GAAP, AICPA, ASA, NACVA)
- [ ] Key assumptions and inputs

Common methodologies table:

| Claim Type | Typical Methods |
|---|---|
| Lost profits | Before-and-after, yardstick, sales projection |
| Business valuation | DCF, market multiples, asset-based |
| Economic damages | But-for analysis, mitigation offset |
| Fraud/disgorgement | Tracing, net equity analysis |

### 3. Key Financial Findings

Present in causal sequence:

1. **Alleged wrongful act** → financial impact chain
2. **Quantification** — calculations with stated assumptions
3. **Supporting evidence** — source documents, corroborating data
4. **Damage period** — start date, end date, rationale for each
5. **Total damages / valuation** — with breakdown by component

Use tables for numerical presentations:

```
| Damage Component       | Amount        | Method         | Period        |
|------------------------|---------------|----------------|---------------|
| Lost revenue           | $X,XXX,XXX   | Before-and-after| MM/YY–MM/YY |
| Increased costs        | $XXX,XXX     | Actual costs    | MM/YY–MM/YY |
| Prejudgment interest   | $XXX,XXX     | Statutory rate  | MM/YY–present|
| Total                  | $X,XXX,XXX   |                |               |
```

### 4. Data Sources & Limitations

- [ ] List each data source with reliability assessment
- [ ] Identify gaps in the financial record
- [ ] State how gaps were addressed (interpolation, proxy data, conservative assumptions)
- [ ] Note any documents requested but not produced

### 5. Sensitivity & Alternative Scenarios

| Scenario | Key Variable Changed | Resulting Range |
|---|---|---|
| Base case | — | $X |
| Conservative | [variable] reduced by X% | $Y |
| Aggressive | [variable] increased by X% | $Z |
| Opposing expert position | [describe difference] | $W |

### 6. Visual Exhibits

Include where they clarify the analysis:
- Trend charts (revenue/profit over damage period vs. but-for projection)
- Comparison tables (actual vs. projected performance)
- Waterfall charts (damage component buildup)
- Timeline diagrams (key events mapped to financial impact)

Number all exhibits sequentially; cross-reference in text.

### 7. Summary of Opinions

Restate each principal conclusion in clear, quotable language:

```
Opinion 1: [Definitive statement with dollar amount and basis]
Opinion 2: [...]
```

## Guidelines

- **Daubert/Frye readiness** — ensure the summary demonstrates that methods are generally accepted and reliably applied to case facts; flag the applicable admissibility standard for the jurisdiction
- **Audience calibration** — settlement summaries emphasize leverage points and ranges; trial summaries emphasize clarity for lay jurors; appellate summaries emphasize methodological soundness
- **Objectivity** — present analysis persuasively but within the bounds of the evidence; do not overstate certainty
- **Precision** — state all dollar amounts with appropriate precision; always include time periods and qualifications
- **Citations** — reference source documents, expert report page numbers, and financial records supporting each conclusion
- **Competing experts** — acknowledge opposing methodologies and explain points of divergence
- **Jurisdiction note** — U.S.-focused; for non-U.S. matters, adapt admissibility standards and professional frameworks accordingly
