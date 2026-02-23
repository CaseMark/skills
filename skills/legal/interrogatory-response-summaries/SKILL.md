---
name: interrogatory-response-summaries
description: Generates structured summaries of interrogatory responses from discovery documents in commercial litigation. Extracts key facts, objections, evasions, patterns, and inconsistencies per interrogatory to support deposition prep, follow-up discovery, and motion practice — without requiring re-review of full response sets. Use when analyzing opposing party interrogatory answers, spotting discovery gaps, or preparing for depositions.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Interrogatory Response Summaries

Produces a structured analytical summary of interrogatory responses to support discovery strategy, deposition preparation, and motion practice.

## Prerequisites

1. **Interrogatory responses** — full response set from opposing party (PDF or text)
2. **Original interrogatories** — the propounded questions, if available separately
3. **Supplemental context** (optional) — prior discovery materials, prior statements, or court orders relevant to the responses

## Output Structure

### Part 1: Per-Interrogatory Summary Table

For each interrogatory, produce a row in this format:

| # | Question (condensed) | Response Type | Key Facts Disclosed | Objections | Gaps / Evasions | Follow-Up Needed |
|---|----------------------|---------------|--------------------|-----------:|-----------------|-----------------|
| 1 | … | Substantive / Objection only / Mixed / Referral to docs / No knowledge | Names, dates, amounts, locations | Privilege / Relevance / Overbroad / etc. | Deflections, non-answers | Yes/No + note |

**Response type definitions:**
- **Substantive** — direct factual answer
- **Mixed** — objection followed by partial answer
- **Referral** — answer directed to document production (note Bates range if available)
- **No knowledge** — responding party claims lack of knowledge or information
- **Objection only** — no substantive answer provided

### Part 2: Pattern Analysis

Identify recurring patterns across all responses:

- **Repeated objections** — same basis asserted across multiple interrogatories (e.g., privilege log issues, overbreadth boilerplate)
- **Blanket no-knowledge claims** — topics where responding party systematically disclaimed knowledge
- **Referral clusters** — interrogatories redirected to document production without further answer
- **Detailed responses** — areas where responding party was unexpectedly forthcoming (may signal strategic framing)
- **Discovery strategy signals** — inferred posture (e.g., stonewalling on damages, cooperative on liability)

### Part 3: Inconsistency & Risk Flags

| Interrogatory # | Issue | Conflicting Source | Significance |
|-----------------|-------|--------------------|--------------|
| … | Response conflicts with… | Prior deposition / produced doc / public record | High / Medium / Low |

Flag:
- Internal inconsistencies between responses
- Conflicts with produced documents or prior sworn statements
- Responses that may violate discovery rules or court orders → note as **motion practice candidate**

### Part 4: Follow-Up Discovery Checklist

- [ ] Interrogatories warranting meet-and-confer (identify by number)
- [ ] Deposition topics surfaced by responses
- [ ] Requests for production to pursue based on referrals or gaps
- [ ] Supplemental interrogatories to propound
- [ ] Privilege log review triggers

## Guidelines

- Preserve all source citations (document title, page/line) for each fact extracted — attorneys must be able to verify for motions and briefs
- Do not characterize objections as waived unless the record clearly supports it; flag for attorney review instead
- When a response combines objection + partial answer, summarize both independently — do not merge
- Flag any response to a contention interrogatory separately; these carry heightened strategic weight
- Note if the response set lacks a verification/signature page — potential waiver issue [VERIFY jurisdiction rule]
- US federal default: 25 interrogatory limit per FRCP 33(a)(1); flag if propounded set exceeds limit without court order [VERIFY local rules]
