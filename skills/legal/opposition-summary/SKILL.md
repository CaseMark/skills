---
name: opposition-summary
description: Generates structured analytical summaries of trademark opposition proceedings before the TTAB, covering opposition grounds, party arguments, evidence, procedural history, and outcomes. Produces balanced assessments for evaluating dispute strength, settlement options, and prosecution strategy. Use when summarizing trademark oppositions, TTAB proceedings, IP dispute analysis, or trademark conflict assessments.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Trademark Opposition Summary

Produces a structured analytical summary of a trademark opposition proceeding that serves as a standalone reference for case evaluation and strategic decision-making.

## Prerequisites

1. **Opposition file documents** — notice of opposition, answer, discovery materials, briefs, evidentiary submissions, TTAB decisions/orders
2. **Application details** — serial number, mark, goods/services, filing/priority dates
3. **Party identification** — opposer and applicant names, counsel, marks at issue

## Information Extraction

Locate and extract from uploaded documents:

| Data Point | Source |
|---|---|
| Application serial number, mark, goods/services, class(es) | Notice of Opposition, application records |
| Filing date, priority date, publication date | Application records, Official Gazette |
| Opposer's mark(s), registration number(s), goods/services | Notice of Opposition, registration certificates |
| Opposition grounds (each statutory basis) | Notice of Opposition |
| Applicant's defenses | Answer to Notice of Opposition |
| Key evidence (declarations, surveys, sales figures) | Trial briefs, exhibits |
| Procedural dates (filing, answer, discovery close, trial) | Board orders, scheduling notices |
| Outcome or current posture | Final decision or latest board order |

## Output Structure

### 1. Executive Overview
- Parties, marks in conflict, application number
- One-paragraph statement of primary issues in dispute
- Current status (ongoing/resolved) and outcome if concluded

### 2. Opposition Grounds

For each ground asserted, document in this format:

**Ground: [e.g., Likelihood of Confusion — §2(d)]**
- **Factual basis**: [specific allegations]
- **Legal theory**: [statutory/precedential framework]
- **Key evidence**: [exhibits, declarations, survey data]

Common grounds checklist:
- [ ] Likelihood of confusion (Lanham Act §2(d)) [VERIFY]
- [ ] Dilution of famous mark (§43(c)) [VERIFY]
- [ ] Descriptiveness/genericness (§2(e)(1)) [VERIFY]
- [ ] Prior common law rights
- [ ] False suggestion of connection (§2(a)) [VERIFY]
- [ ] Geographic descriptiveness (§2(e)(2)) [VERIFY]

### 3. Likelihood of Confusion Analysis (if applicable)

Analyze under the *DuPont* factors [VERIFY]:

| Factor | Opposer's Position | Applicant's Position | Assessment |
|---|---|---|---|
| Similarity of marks (appearance, sound, meaning, commercial impression) | | | |
| Relatedness of goods/services | | | |
| Similarity of trade channels | | | |
| Conditions of purchase / buyer sophistication | | | |
| Strength/fame of opposer's mark | | | |
| Evidence of actual confusion | | | |
| Number and nature of similar marks in use | | | |
| Concurrent use without confusion | | | |

### 4. Applicant's Defenses

Document each defense:
- Challenge to standing
- Mark dissimilarity arguments
- Goods/services distinction
- Trade channel differences
- Weakness of opposer's mark / crowded field
- Coexistence evidence
- Laches, acquiescence, or estoppel

### 5. Procedural History

Chronological table:

| Date | Event |
|---|---|
| | Application filed |
| | Published for opposition |
| | Notice of opposition filed |
| | Answer filed |
| | Discovery opens/closes |
| | Motions (summary judgment, etc.) |
| | Trial periods |
| | Decision issued |

Note any extensions, suspensions, or consolidated proceedings.

### 6. Outcome / Current Posture

If resolved:
- Opposition sustained or dismissed
- Tribunal's reasoning (key holdings)
- Conditions on registration, if any
- Appeal status

If ongoing:
- Current procedural posture
- Upcoming deadlines
- Pending motions

### 7. Strategic Assessment

- Strengths and weaknesses of each party's position
- Evidentiary gaps or procedural vulnerabilities
- Settlement considerations (consent agreements, coexistence terms)
- Impact on broader trademark portfolio

## Guidelines

- Present both parties' positions with equal rigor — flag strengths and weaknesses for each side
- Cite to specific exhibits, declarations, and filings by name and date
- Use exact quotations with attribution for key arguments or findings
- Mark any unverified legal citations with `[VERIFY]`
- Keep accessible to business stakeholders while maintaining legal precision
- Do not opine on ultimate outcome — present the analytical framework for the reader's judgment
- Note any settlement discussions or consent proposals in the record
- For dilution claims, separately address fame of the senior mark and likelihood of blurring/tarnishment
- The summary must be self-contained — a reader should not need to review the underlying file
