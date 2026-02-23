---
name: appeal-document-summary
description: >-
  Produces structured U.S. appellate document summaries that map procedural
  posture, issues on appeal, standards of review, record support, and
  competing arguments into a memo-ready format. Use for appeal review,
  appellate brief intake, notice of appeal analysis, record on appeal
  synthesis, and oral argument prep. Trigger keywords: appeal, appellate,
  notice of appeal, brief, record on appeal, standard of review, oral
  argument, cross-appeal, appellate summary.
tags:
  - litigation
  - summarization
  - summary
---

# Appeal Document Summary

Generate a memo-ready appellate summary that is record-grounded, issue-driven, and standard-of-review aware.

## Prerequisites

1. **Record set** — lower court orders/judgment, briefs, transcripts, docket, exhibits.
2. **Party posture** — appellant/appellee (and any cross-appeals or consolidated matters).
3. **Procedural timeline** — key dates for judgment, notice of appeal, briefing schedule.
4. **Jurisdictional context** — appellate court, originating court, applicable rules.

## Output Structure / Process

Use the following memo structure and fill every section with record citations or explicitly mark gaps.

**Memo Outline**

1. Case Caption and Courts
2. Procedural Posture and Jurisdiction
3. Issues on Appeal and Standards of Review
4. Factual Background (Record-Bound)
5. Arguments and Authorities
6. Dispositive Issues and Risk Assessment
7. Related Proceedings and Collateral Effects
8. Pending Motions and Deadlines
9. Next Steps and Research Gaps

**Required Tables**

Table 1 — Issues and Standards  
| Issue | Appellant Claim of Error | Appellee Response | Standard of Review | Record Support | Dispositive? |
| --- | --- | --- | --- | --- | --- |

Table 2 — Key Orders and Rulings  
| Date | Court | Order/Ruling | Impact on Appeal | Record Cite |

Table 3 — Authorities Map  
| Issue | Primary Authorities | Opposing Authorities | Conflicts/Novelty |

Table 4 — Record Gaps  
| Topic | Missing/Weak Record Support | Risk | Suggested Remedy |

**Narrative Rules**

- Facts must be tied to record cites. If a fact is disputed or unsupported, label it.
- Separate factual background from legal arguments.
- For each issue: identify error type (legal, factual, procedural) and relief sought.
- Identify jurisdictional and preservation issues early.

**Template**

```markdown
## Case Caption and Courts
- Appellant:
- Appellee:
- Originating Court:
- Appellate Court:
- Appeal Type: (as of right / discretionary / interlocutory)

## Procedural Posture and Jurisdiction
- Judgment/Order on Appeal:
- Notice of Appeal Filed:
- Timeliness:
- Jurisdictional Basis:
- Preservation Status:

## Issues on Appeal and Standards of Review
(Insert Table 1)

## Factual Background (Record-Bound)
- Chronology:
- Key Record Citations:
- Disputed Facts:

## Arguments and Authorities
- Appellant:
- Appellee:
- Conflicts / Issues of First Impression:

## Dispositive Issues and Risk Assessment
- Strongest Points:
- Weakest Points:
- Standard-of-Review Sensitivity:

## Related Proceedings and Collateral Effects
- Prior Appeals / Parallel Cases:
- Preclusion Risks:
- Amicus / Public Interest:

## Pending Motions and Deadlines
- Motions:
- Briefing Schedule:
- Oral Argument:

## Next Steps and Research Gaps
- Research Tasks:
- Record Supplement Needs:
```

## Guidelines

- Use neutral, analytic tone; assess both sides.
- Flag preservation defects, waiver risks, and jurisdictional defects.
- Identify standards of review per issue and explain impact in one sentence.
- Note any requests for relief that exceed the record or standard of review.
- Do not infer facts not in the record; mark gaps explicitly.
