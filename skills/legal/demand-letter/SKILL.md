---
name: demand-letter
description: >
  Drafts litigation-ready U.S. pre-suit demand letters that function as settlement
  instruments and defensible future exhibits. Enforces element-driven narratives,
  verified authority, damages methodology, and ethics guardrails. Use this skill
  when the user mentions demand letter, pre-suit demand, breach and cure notice,
  settlement demand, notice of intent to file, cease and desist demand for payment,
  or pre-litigation correspondence. Also trigger when the user asks about FRE 408
  framing, contractual notice compliance, statutory pre-suit prerequisites, evidence
  preservation notices, or quantifying damages for a demand package.
tags:
  - drafting
  - letter
  - litigation
---

# Pre-Suit Demand Letter

A demand letter is simultaneously a settlement instrument and a future exhibit. A defective letter can contain admissions, unsupported claims, or ethics violations — and where statutory pre-suit notice is required (TX DTPA 60-day, MA Ch. 93A 30-day, FL med-mal), defects can waive claims entirely. This skill produces letters where every assertion is sourced, every theory verified or flagged, damages are quantified with methodology, and tone is calibrated for judicial review.

---

## Related skills

- `legal-research` — verify the statutory regime for the letter's state/claim type and cite-check any case law
- `citations` — Bluebook format + good-law status on cases referenced
- `generating-documents`, `docx`, `pdf` — produce the final letter in the format the attorney actually sends

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Governing contract(s)** — notice clauses, cure provisions, forum-selection, arbitration clauses
2. **Correspondence** — emails, letters, texts in chronological order
3. **Financial records** — invoices, payments, chargebacks, proof of tender
4. **Supporting evidence** — incident reports, photos, expert reports, third-party communications
5. **Prior demands** — settlement communications or notices already sent
6. **Statute of limitations** — accrual date, tolling facts, contractual limitations periods
7. **Forum facts** — entity citizenship, principal place of business, forum-selection clauses
8. **Client objectives** — preferred outcome, acceptable range, timing, relationship preservation
9. **Recipient entity** — verify corporate name, registered agent, contractual notice address

**Defaults** (if user doesn't respond): general demand for payment; commercial dispute; FRE 408 header; 30-day response deadline; formal professional tone. Label all defaults explicitly.

---

## Step 1: Diagnose Legal Function

- Analyze contractual notice requirements — methods, deemed-received provisions, cure periods
- Classify letter type: demand for payment, breach + intent to terminate, anchored settlement invitation, preservation trigger, or statutory prerequisite
- Check statutory prerequisites — TX DTPA 60-day, MA Ch. 93A 30-day, FL med-mal, construction defect, lemon law
- Align with dispute resolution mechanism — do not threaten filing in an improper forum

---

## Step 2: Build Element-Driven Fact Narrative

- Chronological structure tied to claim elements
- Source every fact ("On April 18, your project manager wrote…")
- Quote contract terms and correspondence exactly — selective quotation is an attack surface
- No conclusory labels ("fraudulent," "criminal") without supporting facts
- Adversarial awareness: opposing counsel will mine for admissions

---

## Step 3: Articulate Legal Theories

- State primary claims tied to requested remedy — do not over-plead
- Include secondary claims only when they add leverage (fee-shifting, punitive, treble damages)
- Cite specific statutory sections for UDAP and fee-shifting hooks
- Mark unverified citations: `[VERIFY: cite applicable statute]`
- Never assert fee recovery without verified contractual or statutory basis

---

## Step 4: Quantify Damages

| Category | Requirements |
|---|---|
| Direct/expectation | Evidentiary basis for each line item |
| Consequential | Foreseeability and causation chain |
| Statutory multipliers | Specific statute and qualifying conduct |
| Prejudgment interest | Rate, accrual date, governing authority |
| Fees and costs | Contractual or statutory basis only |

Address mitigation, offsets, and credits. Provide enough detail for credibility without revealing walkaway number.

---

## Step 5: Include Preservation Notice

Include formal litigation-hold language requiring preservation of all documents and ESI (emails, texts, database records, metadata) and immediate suspension of routine destruction policies.

---

## Step 6: Frame Demands and Proposed Resolution

- Monetary: specify amount, payee, timing, method
- Non-monetary: specify deliverables, acceptance criteria, deadlines
- If settlement is plausible, include term-sheet concepts: release scope, confidentiality, non-disparagement

---

## Step 7: Set Deadline and Consequences

- Use specific calendar dates, not relative periods ("within 10 days")
- Align with contractual cure periods
- State intent to file — specify forum
- Never threaten criminal prosecution as civil leverage (Model Rule 8.4)

---

## Step 8: Calibrate Tone and Privilege Posture

- Write as if a judge will read it
- Consider marking "Settlement Communication — Subject to FRE 408 / State Equivalent"
- FRE 408 labeling is a signal, not a shield — state rules vary
- Exclude defamatory statements, attorney-client communications, and unnecessary personal information

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the draft, ask:

1. Does this correctly identify the recipient entity and contractual notice address?
2. Is the damages methodology and total demand within the authorized range?
3. Are there statutory pre-suit requirements to verify before sending?
4. Should this be sent as a settlement communication (FRE 408) or an unconditional demand?

If no answer, recommend verifying recipient entity and notice method (most common failure point) and proceed if authorized.

---

## Quality Audit

- [ ] Correct recipient entity name and notice address
- [ ] Contractual notice method satisfied (certified mail, courier, etc.)
- [ ] Cure period aligned with contract terms
- [ ] Every factual assertion sourced or labeled "client-provided, unverified"
- [ ] Legal citations verified or marked `[VERIFY]`
- [ ] Damages internally consistent (dates, interest, mitigation)
- [ ] No threats of criminal/regulatory action as civil leverage
- [ ] FRE 408 / settlement posture addressed
- [ ] Preservation notice included
- [ ] FDCPA disclosures included if applicable
- [ ] Specific calendar deadline
- [ ] Attorney review required before sending

---

## Guidelines

**Jurisdiction flags:**
- **California**: CCP § 998 cost-shifting distinct from demand letters `[VERIFY]`
- **Texas**: DTPA 60-day pre-suit notice (Tex. Bus. & Com. Code § 17.505) `[VERIFY]`
- **Massachusetts**: Ch. 93A 30-day demand identifying the unfair/deceptive act `[VERIFY]`
- **Florida**: Med-mal and insurance claims have specific pre-suit prerequisites `[VERIFY]`
- Many states require retraction demands in defamation cases before filing

**Anti-hallucination:**
- Do not invent statutory citations, case names, or verdict data
- Mark all unverified legal claims with `[VERIFY]`
- Do not assert fee recovery without verified basis
- No defamatory statements or conclusory labels without factual support

**Ethics:** Model Rule 3.1 (meritorious claims), 4.1 (truthfulness), 8.4 (no criminal threats as leverage). FDCPA compliance when applicable.

**ATTORNEY REVIEW REQUIRED** — No demand letter produced by this skill may be sent without attorney review and approval.
