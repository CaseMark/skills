---
name: discovery-response-summary
description: >
  Produces a structured litigation discovery summary organizing interrogatory
  responses, requests for production, requests for admission, deposition
  transcripts, and privilege logs into a thematic, issue-based analytical
  memorandum. Use this skill when the user mentions discovery summary, discovery
  analysis, response review, discovery gap analysis, privilege log review,
  deposition summary, follow-up discovery planning, summary judgment preparation,
  or trial preparation from discovery. Also trigger when the user references
  thematic discovery organization, cross-referencing discovery responses, or
  asks for help synthesizing voluminous discovery materials. Even if the user
  just says "summarize these discovery responses" or "what did we learn from
  discovery," use this skill.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Discovery Response Summary

## Why This Skill Exists

Litigation teams drown in discovery responses organized by request number rather than by legal issue. When an attorney needs to know "what do we have on the notice element?" they must mentally cross-reference interrogatories, document productions, RFAs, and deposition testimony — a process that is slow, error-prone, and impossible to delegate effectively. Critical admissions get buried, evidentiary gaps go unnoticed until summary judgment, and follow-up discovery opportunities expire.

This skill synthesizes voluminous discovery materials into a thematic, issue-organized memorandum that maps what has been established, what is disputed, and what gaps remain — directly supporting motions to compel, summary judgment, settlement, and trial preparation.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Discovery requests** — interrogatories, RFPs, RFAs with request numbers and service dates
2. **Responses and objections** — all written responses, including supplemental responses
3. **Production logs** — Bates ranges, privilege logs, withholding notices
4. **Deposition transcripts** — if available, with page/line citations
5. **Operative pleadings** — complaint and answer to anchor thematic organization to claims/defenses
6. **Case posture** — what is the next milestone (summary judgment, mediation, trial, class cert)?

**If the user doesn't respond**, apply and clearly label these defaults: organize by claims and defenses from the complaint/answer; include all discovery types provided; federal court; neutral analytical tone.

> If operative pleadings are missing, organize by the discovery categories provided and flag that issue-mapping is provisional.

---

## Step 1: Produce Executive Summary

- Scope of discovery conducted (methods, parties, date range)
- Top 3–5 findings favorable to client
- Top 3–5 critical gaps or adverse admissions
- Recommended immediate next steps

---

## Step 2: Build Thematic Analysis

Group all discovery responses across all methods by legal issue — not by request number:

| Issue/Element | Interrogatory | RFP | RFA | Deposition | Assessment |
|---|---|---|---|---|---|
| Liability – [element] | No. X: [summary] | No. X: [summary] | No. X: Admitted/Denied | [Witness], [page:line] | Established / Disputed / Gap |
| Damages | ... | ... | ... | ... | ... |
| Affirmative defenses | ... | ... | ... | ... | ... |

This is the primary deliverable — it answers "what do we have on each issue?" in one table.

---

## Step 3: Organize Discovery by Type

### Interrogatories
For each response:
- **No. [X]**: [Verbatim or tight paraphrase of request]
  - *Objections*: [List]
  - *Substantive answer*: [Summary]
  - *Flag*: Admission / Evasive / Names new witness / References Bates [XXX]

### Requests for Production
- **No. [X]**: [Category requested]
  - *Produced*: [Bates range or description]
  - *Withheld*: [Privilege/ground asserted]
  - *Deficiency*: [Yes/No — describe]

### Requests for Admission
- **No. [X]**: [Statement]
  - *Response*: Admitted / Denied / Objected / Insufficient denial
  - *Strategic note*: [If admitted, usable at SJ/trial]

### Deposition Testimony
- **[Witness name]** ([date])
  - Key admissions: [topic] — [page:line]
  - Contradictions with written discovery: [describe]
  - Documents identified: [Bates or description]

---

## Step 4: Analyze Privilege Log

| Entry | Privilege Claimed | Basis Adequate? | Challenge Viable? |
|---|---|---|---|
| [Doc/date] | Attorney-client / Work product | Yes / No | Yes / No — reason |

Flag patterns: over-designation, missing privilege elements, subject-matter waiver arguments.

---

## Step 5: Build Deficiency Tracker

| Request | Deficiency | Basis for MTC | Priority |
|---|---|---|---|
| Rog No. X | Boilerplate objection, no substantive answer | FRCP 33(b)(3) [VERIFY] | High |
| RFP No. X | Produced subset only, no log for withheld | FRCP 34(b)(2)(C) [VERIFY] | Medium |

---

## Step 6: Produce Gap Analysis and Next Steps

**Additional interrogatories needed:**
- [ ] [Topic — reason gap exists]

**Additional RFPs needed:**
- [ ] [Category — what's missing and why it matters]

**Depositions to take:**
- [ ] [Witness — identified in discovery response No. X, not yet deposed]

**Follow-up / MTC candidates:**
- [ ] [Specific deficient response — proposed remedy]

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial summary, ask:

1. Does the thematic organization match your case theory — any issues to reorder or add?
2. Are the "established / disputed / gap" assessments calibrated correctly for your litigation posture?
3. Which follow-up actions should be prioritized first?
4. Should I generate a standalone deficiency tracker or motion-to-compel analysis from the flagged items?

If the user doesn't answer, recommend prioritizing the gap analysis and deficiency tracker for the nearest deadline and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Every finding cited to a specific request number, Bates number, or deposition page:line
- Thematic analysis covers all claims, defenses, and disputed elements
- No discovery type omitted from the cross-reference table
- Favorable and adverse findings separately labeled
- Privilege log entries summarized without revealing protected content
- Deficiency tracker includes rule basis and priority
- Gap analysis tied to specific missing evidence needed for claims/defenses
- Inconsistencies between interrogatory answers and deposition testimony flagged for impeachment
- All rule citations verified or marked `[VERIFY]`
- Neutral analytical tone maintained throughout

---

## Guidelines

- Cite every finding to a specific request number, Bates number, or deposition page:line
- Flag FRCP rule violations but mark jurisdiction-specific rules `[VERIFY]` if not U.S. federal
- Note any inconsistencies between verified interrogatory answers and deposition testimony — these are potential impeachment opportunities
- Maintain neutral analytical tone; separately label favorable vs. adverse findings
- Do not summarize privilege log entries in a way that reveals protected content
- For state court matters, confirm applicable discovery rules differ from FRCP before citing deadlines or limits
- **Anti-hallucination** — all case citations must be verified or left as explicit placeholders; no plausible-sounding but unverified citations
- **Attorney review required** — all output is practice-support work product; it must be reviewed by supervising counsel before use in motions, client communications, or filings
