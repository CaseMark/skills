---
name: deposition-transcript-analyzer
description: >-
  Analyzes completed deposition transcripts to extract maximum litigation
  value. Generates executive summaries, testimony indexes, admission
  compilations, impeachment opportunities, credibility assessments,
  motion/trial designations, and follow-up action checklists. Use when
  reviewing a deposition transcript for case strategy, summary judgment
  preparation, trial preparation, or post-deposition work product. Trigger
  keywords: deposition analysis, transcript review, testimony index,
  admissions, impeachment, deposition summary, trial designations.
tags:
  - analysis
  - litigation
  - memo
  - summarization
  - summary
---

# Deposition Transcript Analyzer

Systematically extracts and organizes deposition testimony for motions, trial preparation, and case strategy.

## Prerequisites

1. Completed deposition transcript (full text or upload)
2. Party/witness identification (role in case, represented party)
3. Claims and defenses at issue (to prioritize relevant testimony)
4. Known prior statements or documents for impeachment comparison (optional)

## Output Structure / Process

### Phase 1 — Executive Summary

```
DEPOSITION SUMMARY
==================
Witness: [Name] | Role: [Plaintiff/Defendant/Third-party]
Date: [Date] | Pages: [#] | Examining Counsel: [Names/Parties]

WITNESS PROFILE
---------------
Demeanor:          [Cooperative / Hostile / Evasive / Credible]
Preparation level: [Well-prepared / Poorly prepared / Over-coached]

KEY TAKEAWAYS
-------------
1. [Most significant testimony]
2. [Second most significant]
3. [Third most significant]

HELPFUL TESTIMONY                          HARMFUL TESTIMONY
-----------------                          -----------------
• [Favorable point] (p. XX)                • [Unfavorable point] (p. XX)
• [Favorable point] (p. XX)                • [Unfavorable point] (p. XX)

CREDIBILITY: [Assessment + likely jury appeal]

FOLLOW-UP NEEDED
----------------
• Documents to obtain:
• Witnesses to depose:
• Discovery requests:
• Legal research:
```

---

### Phase 2 — Testimony Index

| Page:Line | Topic | Summary | Importance | Use |
|-----------|-------|---------|------------|-----|
| 45:3–46:12 | Meeting on 3/15 | W. attended; describes termination discussion | High | Liability |
| 52:8–53:4 | Knowledge of complaint | W. denies awareness before decision | High | Impeachment |
| 78:15–79:22 | Emotional impact | W. describes ongoing distress | Medium | Damages |

**Index categories:** Chronology · Key events · Witness knowledge · Documents discussed · Admissions · Denials · Credibility issues · Damages · Expert-related

---

### Phase 3 — Admission Compilation

**Admission types:**
| Type | Description |
|------|-------------|
| Direct | Witness explicitly concedes a fact |
| Implied | Testimony logically supports your position |
| Adoptive | Witness adopts document content or another's statement |
| Party binding | If party-witness, binds the party under FRE 801(d)(2) |

```
ADMISSIONS — [WITNESS NAME]
============================

LIABILITY ADMISSIONS
--------------------
1. ADMISSION: [Factual proposition established]
   Citation:   p. XX, ll. X–X
   Quote:      "[Exact transcript language]"
   Significance: [Why this matters to a claim element]

DAMAGES ADMISSIONS
------------------
[Same format]

CREDIBILITY ADMISSIONS
----------------------
[Same format]
```

---

### Phase 4 — Impeachment Index

| Issue | Depo Testimony | Contradicting Source | Citation | Use At |
|-------|---------------|---------------------|----------|--------|
| Knowledge timing | "Learned in April" (p. 45) | Email dated March 3 | Ex. 5 | SJ/Trial |
| Meeting attendance | "Wasn't there" (p. 52) | Attendance log | Ex. 8 | Trial |

**Impeachment categories:**
- **Internal inconsistencies** — Witness contradicted within same deposition (note both page refs)
- **Prior inconsistent statements** — Conflicts with prior depo, interrogatory answers, declarations
- **Document contradictions** — Testimony vs. exhibit content
- **Implausibility** — Memory gaps on events witness organized/owned
- **Bias/interest** — Financial stake, relationship, animosity

---

### Phase 5 — Motion & Trial Designations

**Summary Judgment Designations** (FRCP 56):

| Motion Topic | Page:Line | Summary | Support/Oppose SJ |
|--------------|-----------|---------|-------------------|
| [Claim element] | 45:3–12 | [Description] | Support |

**Trial Designations** (FRCP 32):

| Purpose | Page:Line | Content Summary | Est. Time |
|---------|-----------|-----------------|-----------|
| Liability | 45:3–48:22 | Decision-making process | 5 min |
| Damages | 78:15–82:4 | Impact on plaintiff | 4 min |

**Counter-Designations:** For each expected opposing designation, identify context pages that qualify or contradict.

---

### Phase 6 — Credibility Assessment

| Factor | Rating | Examples from Transcript |
|--------|--------|--------------------------|
| Consistency | High / Medium / Low | [p. refs] |
| Responsiveness | Direct / Evasive / Argumentative | [p. refs] |
| Memory | Good / Selective / Poor | [p. refs] |
| Bias indicators | None / Some / Significant | [p. refs] |
| Document support | Strong / Weak / Contradicted | [p. refs] |

**Jury appeal:** Note likeability, believability, witness strengths/weaknesses for trial team memo.

---

### Phase 7 — Follow-Up Checklist

| Action | Basis in Transcript | Priority |
|--------|---------------------|----------|
| Subpoena [document] | Referenced at p. 45 | High |
| Depose [person] | Identified as witness at p. 52 | Medium |
| RFA on [topic] | Lock in admission | High |
| Research [legal issue] | Raised by testimony | Medium |

---

### Quick Analysis Template (Time-Limited)

```
QUICK DEPOSITION ANALYSIS
=========================
Witness: _______________  Date: _______________

TOP 5 TAKEAWAYS:
1.    2.    3.    4.    5.

BEST ADMISSIONS (p. ref):
1.    2.    3.

BIGGEST PROBLEMS (p. ref):
1.    2.

KEY IMPEACHMENT OPPORTUNITY:

IMMEDIATE FOLLOW-UP:

CREDIBILITY (1–10): ___
```

## Guidelines

- Cite every extract with page:line — no paraphrasing without citation
- Distinguish party-witness admissions (FRE 801(d)(2) non-hearsay) from third-party witness testimony
- Flag errata-sheet changes if transcript has been corrected — original testimony may still be usable for impeachment
- For video depositions, note demeanor observations bracketed as `[OBSERVATION]` to distinguish from transcript text
- Counter-designations must provide context without distorting meaning (FRE 106 completeness rule)
- FRCP 32 governs admissibility at trial; confirm witness unavailability or adverse-party status before designating
- Verify local rules for designation/counter-designation exchange deadlines in the applicable district

**Key authorities:**
- FRCP 32 — Using depositions in court proceedings
- FRCP 56 — Summary judgment (deposition use)
- FRE 801(d)(2) — Party-opponent admissions (non-hearsay)
- FRE 613 — Prior inconsistent statements (impeachment)
