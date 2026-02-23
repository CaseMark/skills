---
name: newsletter-summary
description: >-
  Produces concise, actionable U.S. legal newsletter summaries of recent
  developments (case law, regulatory changes, guidance, enforcement,
  legislation) organized by practice area or theme. Delivers headlines, what
  happened, why it matters, and action items with citations and effective
  dates. Use for legal news digests, weekly/monthly client updates, or
  internal awareness. Trigger keywords: newsletter summary, legal update, case
  law update, regulatory update, weekly digest, compliance news.
tags:
  - corporate
  - research
  - summarization
  - summary
---

# Legal Newsletter Summary

Deliver a scannable, practice-relevant digest of recent legal developments with concrete implications and actions.

## Prerequisites

1. **Scope** — practice areas, jurisdictions, industries, and audience (internal, clients, executives)
2. **Time window** — default last 7–14 days unless user specifies
3. **Source access** — approved sources list or permission to research authoritative sources
4. **Format preference** — sectioning by practice area, jurisdiction, or theme; word count target if any

## Output Structure / Process

### 1) Intake & Scoping

Checklist:
- Confirm audience and tone (internal ops vs client-facing)
- Confirm practice areas and jurisdictions
- Confirm time window and publication cadence
- Define exclusions (e.g., no minor procedural updates)

### 2) Research & Source Capture

Source hierarchy (use highest available):
| Tier | Source Type | Examples | Use Notes |
| --- | --- | --- | --- |
| 1 | Primary law | Court opinions, statutes, regs, agency orders | Prefer for holdings and requirements |
| 2 | Official guidance | Agency guidance, FAQs, enforcement releases | Use for compliance signals |
| 3 | Bar/industry | Bar updates, reputable legal publications | Use for context and trends |

Capture fields per item:
- Source title, date, jurisdiction, authority
- Direct citation (case name, reporter, statute/reg number, docket)
- Link/locator if provided by user

### 3) Triage & Ranking

Rank each candidate item:
- **Impact**: High / Medium / Low
- **Urgency**: Immediate / Near-term / Watch
- **Scope**: Broad / Sector-specific / Narrow
- **Novelty**: New rule, major shift, split, clarification

Prioritize:
- New compliance obligations
- Binding appellate decisions
- Significant enforcement trends
- Deadlines or effective dates

### 4) Item Template (75–200 words each)

Use this exact structure:
| Field | Required Content |
| --- | --- |
| Headline | 8–14 words, action-oriented |
| What Happened | 1–3 sentences, factual |
| Why It Matters | 1–3 sentences, impact on practice/clients |
| Action Items | Bullets, concrete steps |
| Details | Court/agency, jurisdiction, effective date, citations |
| Confidence | High/Medium/Low if source quality is mixed |

### 5) Section Layout

Order within each section:
1. Urgent/time-sensitive
2. High impact precedential/regulatory
3. Emerging trends

Section header format:
- **Practice Area / Theme** — optional subheading for jurisdiction

### 6) Final Assembly Template

```markdown
# Legal Newsletter Summary
**Coverage Window:** {start_date}–{end_date}
**Jurisdictions:** {list}
**Practice Areas:** {list}

## {Practice Area / Theme}
### {Headline}
**What Happened:** ...
**Why It Matters:** ...
**Action Items:**
- ...
**Details:** Court/Agency, Jurisdiction, Effective Date, Citation(s)

## Watchlist / Upcoming
- {Pending appeals, comment periods, scheduled arguments}
```

### 7) Citation Rules

- Use Bluebook-style citations for cases and statutes where appropriate
- Include court and year for cases
- Include code section and latest amendment date for statutes/regs
- Mark uncertain citations as `[VERIFY]`

## Guidelines

- No editorializing; stick to verifiable facts and implications
- Never copy article text; summarize the underlying legal development
- Flag effective dates and compliance deadlines explicitly
- Note circuit splits or conflicting authority when present
- If no material updates, state “No material updates in the covered period”
- US-focused unless user specifies otherwise
- Use `[VERIFY]` for any citation not confirmed in a primary source
