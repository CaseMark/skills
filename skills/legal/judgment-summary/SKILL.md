---
name: judgment-summary
description: Produces structured U.S. litigation judgment summaries from court opinions or final orders, covering caption, procedural history, facts, issues, standards of review, holdings, precedent treatment, concurrences/dissents, disposition, and practical implications with pinpoint citations. Use for judgment summary, opinion summary, final decision summary, post-trial review, appeal analysis, or case outcome briefs.
tags:
  - litigation
  - summarization
  - summary
---

# Judgment Summary

Delivers a citation-ready summary of a final judgment or opinion with holdings, standards of review, and practical impact.

## Prerequisites

1. Full opinion or judgment text with page or paragraph numbering.
2. Case citation details: court, docket number, decision date, judge or panel.
3. Procedural posture and relevant lower court rulings.
4. Record of key filings or orders referenced by the court.

## Output Structure / Process

1. Extract case metadata and confirm jurisdiction.
2. Identify issues, standards of review, and holdings with pinpoint cites.
3. Separate background, material, and disputed facts.
4. Track precedent treatment and any split implications.
5. Capture disposition details, remand instructions, and deadlines.
6. Translate holdings into practical implications without advocacy.

Use the following template and fill every section. If a field is missing, write `Not stated`.

```
CASE CAPTION
- Case name:
- Court:
- Docket no.:
- Decision date:
- Judge/Panel:
- Jurisdiction:
- Prior history:

SYNOPSIS (<=150 words)
- Core holding:
- Practical significance:

PROCEDURAL HISTORY
- Lower court decisions:
- Basis for appeal/review:
- Standard(s) of review:
- Scope of review:

FACTS
- Background facts:
- Material facts:
- Disputed facts:

ISSUES AND HOLDINGS
| Issue | Legal Standard | Rule/Reasoning | Holding | Pin Cite |
| --- | --- | --- | --- | --- |

PRECEDENT TREATMENT
| Case | Treatment (Followed/Distinguished/Overruled/Questioned) | Point of Use | Pin Cite |
| --- | --- | --- | --- |
- Circuit split or split resolution: Yes/No + brief note

CONCURRENCE / DISSENT
- Author(s):
- Key departures:
- Implications:

DISPOSITION
- Result (affirmed/reversed/vacated/remanded):
- Remand instructions:
- Costs/fees:
- Deadlines or conditions:

PRACTICAL IMPLICATIONS
- Litigation impact:
- Transactional/compliance impact:
- Evidence/procedure impact:
- Risk posture or strategy notes:

KEY CITATIONS
- Holdings:
- Critical facts:
- Notable reasoning:
```

Target length: 1,500 to 3,000 words unless the decision is unusually short.

## Guidelines

- Neutral tone; no advocacy or editorial framing.
- Distinguish holdings from dicta explicitly.
- Preserve the court’s terminology for standards and tests.
- If a legal citation is uncertain, mark it `[VERIFY]`.
- Do not infer facts or procedural steps not stated in the opinion.
- If non-U.S. or specialized court, note deviations from U.S. practice in the Synopsis.
- Use pinpoint cites for every holding and for any fact the court labels material.
