---
name: deposition-impeachment-builder
description: Drafts deposition-ready impeachment sequences using the Commit–Credit–Confront (CCC) method. Diagnoses whether a contradiction is material, generates controlled commitment and confrontation questions, and tailors the Credit foundation to the prior statement type (sworn testimony, interrogatory response, email, corporate record, declaration, etc.). Embeds FRE 613, FRE 801(d)(1)(A)/(d)(2), and FRCP 30 guardrails, anti-hallucination constraints, and privilege-awareness. Use when building impeachment sequences for depositions, preparing cross-examination on prior inconsistent statements, or creating usable transcript clips for summary judgment or trial.
tags:
  - analysis
  - checklist
  - drafting
  - litigation
  - summary
---

# Deposition Impeachment Builder

Drafts a Commit–Credit–Confront impeachment sequence for deposition, producing a controlled script, deployment memo, and checklist of missing information.

## Prerequisites

1. **Current testimony** — verbatim transcript excerpt (Q&A with page/line) or exact anticipated answer; paraphrases require attorney confirmation of precise phrasing
2. **Prior statement** — full text (not snippet), statement type, date, author/speaker, recipients, and pin-cite (page:line for transcripts; paragraph/section for documents)
3. **Witness's connection** — how the witness authored, signed, verified, sent, or adopted the prior statement
4. **Case context** — forum (federal/state), posture (fact discovery/MSJ/pretrial), claims/defenses, witness role (party, 30(b)(6) designee, percipient, expert)
5. **Strategic intent** — impeachment only vs. substantive use; video deposition; protective order applicability

**If any required input is missing, pause and ask targeted follow-up questions. Never fabricate quotes, dates, page numbers, or document attributes.**

---

## Output Structure

Generate three deliverables:

### 1. Commit–Credit–Confront Script

#### Phase 1 — COMMIT: Lock the Current Testimony

**Goal:** Eliminate every escape hatch before the witness knows a contradiction is coming.

Rules:
- Use the witness's own vocabulary
- Single factual proposition per question
- No compound questions
- Define ambiguous terms neutrally before committing
- Confirm certainty; fork hedged answers into a second committed proposition

**Template pattern:**
```
"Just so I understand: you [core proposition], correct?"
"You're not saying [narrowing qualifier]—you're saying [absolute proposition], right?"
"You're certain about that? No doubt in your mind?"
"And [close remaining escape route], correct?"
```

#### Phase 2 — CREDIT: Establish Reliability and Adoption

Tailor foundation to prior statement type:

| Statement Type | Credit Focus | Key Questions |
|---|---|---|
| **Prior deposition/hearing testimony** | Oath, counsel present, opportunity to correct errata | "You were under oath?" / "Your lawyer was present?" / "You reviewed and didn't change this testimony?" |
| **Signed declaration / verified response** | Signature, review, penalty of perjury | "You read this before signing?" / "You swore the contents were true?" |
| **Email / text authored by witness** | Account ownership, routine practice, contemporaneity, recipients, intent to rely | "That's your email address?" / "You sent this in the ordinary course?" / "You intended [recipient] to rely on it as accurate?" |
| **Email / doc drafted by others, adopted by witness** | Review, approval, transmission authority | "You reviewed this before it was sent?" / "You authorized it to go out?" |
| **Interrogatory response** | Witness's role in preparation, verification, steps taken to ensure accuracy | "Did you review the draft?" / "You signed the verification?" |
| **Corporate record / third-party doc** | Receipt, reliance, notice — **flag:** may not constitute witness's "statement"; different evidentiary posture | "You were copied?" / "You relied on it?" |

**Credit containment:** If witness tries to devalue the prior statement mid-Credit ("I was confused"), address immediately:
> "You wouldn't give false testimony just because you were [tired/confused], right?"

#### Phase 3 — CONFRONT: Present the Inconsistency

Disciplined rhythm — do not deviate:

1. **Re-commit** — immediately restate current testimony
2. **Mark and orient** — mark exhibit or identify by Bates; confirm witness is on correct page/line
3. **Read verbatim** — quote exact language; include `[PAGE:LINE]` placeholder if pin-cite unavailable
4. **Obtain admission** — two variants:

| Variant | Language | Use When |
|---|---|---|
| Conservative | "So your testimony today is different from what you said under oath on [DATE], correct?" | Preserving the record; avoiding overreach |
| Aggressive | "Which is accurate — your [email/deposition] from [DATE], or your testimony today?" | Witness is a party; full contradiction is binary |

5. **Stop.** Do not ask "why," "how," or "could it be." No open-ended questions after confrontation.

**Containment follow-ups** (if witness evades):
- "What part is inaccurate?"
- "When did you first realize it was wrong?"
- "Who told you that?" / "What document did you review?"
- "Where is that reflected in writing?"

---

### 2. Deployment Memo (1 page)

Include:
- **What this impeachment accomplishes** (element/credibility theme it addresses)
- **Timing recommendation** — impeach now vs. bank for trial
- **Opposing responses to anticipate** and containment strategy
- **Substantive vs. impeachment-only use** — flag for attorney analysis under FRE 801(d)(1)(A) / 801(d)(2)

**Timing decision table:**

| Objective | Timing | Rationale |
|---|---|---|
| Discovery roadmap | Early | Forces witness to explain, surfaces documents/witnesses |
| Trial-quality clip | Bank | Starker after multiple aligned denials; avoids educating witness |
| Settlement signal | Mid-deposition | Demonstrates narrative instability without full rehearsal |
| Rapid-fire credibility destruction | Series at end | Effective for witnesses with multiple contradictions |

---

### 3. Missing Information Checklist

List all `[PLACEHOLDERS]` requiring attorney completion before use:
- `[PAGE:LINE]` — pin-cite for prior statement
- `[EXHIBIT NO.]` — exhibit identifier
- `[DATE]` — any unconfirmed date
- Any quotation labeled as a paraphrase requiring verbatim verification

---

## Guidelines

**Evidentiary rules — federal defaults (flag state variations):**
- **FRE 613(a):** No obligation to show prior statement to witness before examining on it, but must disclose to adverse party's counsel on request
- **FRE 613(b):** Extrinsic evidence of prior inconsistent statement requires opportunity to explain or deny
- **FRE 801(d)(1)(A):** Prior inconsistent statement given under penalty of perjury at a proceeding or deposition is non-hearsay and usable substantively
- **FRE 801(d)(2):** Opposing party statements are non-hearsay
- **FRE 106 (Completeness):** Opposing counsel may require introduction of other portions; review full context before use

**Procedural:**
- **FRCP 30(c)(2):** Objections during deposition limited to relevance and privilege; instructions not to answer narrowly limited
- **FRCP 30(b)(6):** Corporate designee testimony may bind the organization — flag for attorney verification; do not assert binding effect without confirmation

**State-specific flags (request forum before finalizing):**

| Jurisdiction | Key Rule |
|---|---|
| California | EC §770 — judge may exclude extrinsic evidence unless witness given opportunity to explain; EC §780 — credibility factors |
| New York | CPLR 4514 — stricter limits on unsworn/unwritten prior statements |
| Common law (Browne v. Dunn) | Must "put the case" to the witness — confront explicitly before relying in closing |
| Arbitration | AAA/JAMS rules and scheduling order govern; treat as separate regime |

**Professional responsibility:**
- ABA Model Rule 3.3 — candor when excerpts used in court filings
- ABA Model Rule 3.4 — do not impeach with a document that does not actually contain the contradiction
- ABA Model Rule 4.2 — all questioning through formal proceeding with counsel present
- If witness cites counsel discussions to explain changed testimony, pivot to nonprivileged facts: timing, documents reviewed, non-lawyer communications

**Anti-hallucination (non-negotiable):**
- Never invent page/line numbers, quotation marks around fabricated text, dates, or document attributes
- Every proposed quotation without a verbatim source must be labeled `[PLACEHOLDER — VERIFY BEFORE USE]`
- Every case law or statutory citation must be verified or labeled `[VERIFY]`

**Materiality test before drafting:** Tie the contradiction to a claim element, defense element, damages component, or credibility theme in one sentence. If you cannot, flag the impeachment as a candidate for trial cross-examination rather than deposition use.

**Attorney review required before use in any proceeding. This skill is attorney work product, not legal advice.**
