---
name: risk-analysis
description: Generates structured risk analysis summaries for legal matters, synthesizing case documents to identify, categorize, and evaluate risks by severity and likelihood with quantified exposures and mitigation strategies. Covers litigation exposure, regulatory compliance, contractual liability, reputational risk, and operational vulnerabilities. Use when preparing risk assessments, exposure analyses, liability summaries, or pre-filing risk evaluations for corporate governance matters.
tags:
  - analysis
  - corporate
  - summarization
  - summary
---

# Risk Analysis Summary

Produces a prioritized risk analysis from matter documents, quantifying exposures and recommending mitigation strategies for attorneys, clients, and stakeholders.

## Prerequisites

1. **Matter documents** — contracts, pleadings, correspondence, regulatory filings, insurance policies
2. **Matter context** — jurisdiction, industry, phase (pre-filing, active litigation, settlement), key parties
3. **Client risk tolerance** — if known, any thresholds for acceptable exposure or strategic constraints

## Output Structure

### 1. Executive Overview

| Element | Content |
|---|---|
| Matter snapshot | One-paragraph factual summary |
| Top 3-5 risks | Ranked by severity × likelihood, one sentence each with estimated exposure |
| Immediate action items | Time-sensitive deadlines, SOL dates, regulatory windows |

### 2. Risk Register

For each identified risk, complete this table row:

| Field | Description |
|---|---|
| **Risk ID** | Sequential (R-01, R-02, ...) |
| **Category** | Contractual / Regulatory / Litigation / Financial / Reputational / Operational |
| **Description** | Specific risk statement grounded in document evidence |
| **Factual basis** | Cite specific contract provisions, regulatory sections, correspondence, or facts |
| **Legal authority** | Applicable statutes, regulations, case law — mark `[VERIFY]` if uncertain |
| **Likelihood** | High / Medium / Low — with reasoning |
| **Severity** | Critical / Major / Moderate / Minor |
| **Financial exposure** | Range: best-case / most-likely / worst-case |
| **Non-monetary impact** | Reputational, regulatory sanctions, operational disruption if applicable |
| **Mitigating factors** | Available defenses, insurance coverage, factual counterarguments |
| **Interdependencies** | Other risk IDs that compound or conflict with this risk |

### 3. Risk Matrix

Plot risks on a 3×3 severity/likelihood grid:

```
              │ Low Likelihood │ Medium         │ High
─────────────┼────────────────┼────────────────┼──────────────
Critical     │                │                │
Major        │                │                │
Moderate     │                │                │
```

Place risk IDs in appropriate cells.

### 4. Mitigation Strategies

For each risk rated Major/High or above:

- **Recommended action** — specific, practical step
- **Type** — Legal defense / Procedural / Settlement / Insurance / Operational change
- **Feasibility** — High / Medium / Low
- **Estimated effectiveness** — degree of exposure reduction
- **Resource requirements** — cost, time, personnel
- **Trade-offs** — does this mitigation exacerbate another risk?

### 5. Timeline and Prioritization

| Priority | Risk ID | Action | Deadline/Trigger | Owner |
|---|---|---|---|---|
| Urgent | | | | |
| Near-term (30-90 days) | | | | |
| Strategic (90+ days) | | | | |

Flag all hard deadlines: statutes of limitations, contractual cure periods, regulatory filing dates.

### 6. Information Gaps

List areas where additional investigation, discovery, or expert consultation is needed to refine the risk assessment.

## Guidelines

- **Ground every risk in evidence** — cite specific documents, provisions, or facts; never assert risk in the abstract
- **Quantify wherever possible** — dollar ranges with stated assumptions; flag estimates as conservative/aggressive
- **Separate fact from inference** — clearly distinguish established facts, reasonable inferences, and speculative scenarios
- **Balanced tone** — neither minimize genuine risks nor catastrophize manageable exposures
- **Audience awareness** — use clear language accessible to business stakeholders; define legal terms on first use
- **Acknowledge uncertainty** — state confidence level and identify what additional information would change the assessment
- **Check interdependencies** — flag where addressing one risk may worsen another
- **Jurisdiction-specific** — note where risk analysis depends on forum, governing law, or regulatory body
