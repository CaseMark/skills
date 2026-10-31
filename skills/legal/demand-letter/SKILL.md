---
name: demand-letter
language: en
description: >
  Drafts U.S. pre-suit demand letters that work as settlement instruments and as
  defensible future exhibits: notices of breach and demands for cure, payment
  demands, cease and desist demands, statutory pre-suit notices (Massachusetts Chapter
  93A, Texas DTPA 60-day notice, California CLRA 1782, Florida Chapter 558 and
  medical-malpractice notice of intent, defamation retraction demands, Magnuson-Moss
  opportunity to cure) and FDCPA collection demands. Builds an element-driven fact
  narrative with a source for every assertion, verifies or flags each authority,
  quantifies damages with methodology (multipliers, interest, mitigation, fees),
  computes each deadline from its own trigger, and applies ethics guardrails
  (represented parties, no criminal-threat leverage, FRE 408). Use for demand letter,
  pre-suit demand, settlement demand, 93A letter, DTPA notice, notice of intent, or
  pre-litigation correspondence. Routes any offer to settle within policy limits to
  bad-faith-demand and coverage questions to coverage-opinion.
tags:
  - drafting
  - letter
  - litigation
---

# Pre-Suit Demand Letter

Produces a draft pre-suit demand letter, with drafting notes (source map, reconciliation table, gap register, clock table, hand-offs and `[VERIFY]` list), in which every assertion is sourced, every theory is verified or flagged, damages carry their methodology, and the deadline is computed from the right trigger. Everything it produces is a draft for review, signature and service by a licensed attorney; this skill drafts, it does not sign, and it does not send. This file is the controller; operational detail lives in `references/`, opened when a step says so.

## Why This Skill Exists

A demand letter is simultaneously a settlement instrument and a future exhibit. A defective letter can contain admissions, unsupported claims or ethics violations, and where a statute makes pre-suit notice a prerequisite (Chapter 93A, DTPA, CLRA, Florida medical malpractice, construction defect, FDCPA, retraction statutes), a defect can abate, cap or bar the claim. The errors are predictable and are listed below. Most trace to drafting from a client summary instead of the contract, the statute and the records.

## Where Mistakes Hide

| Input / Document | What It Is Used For | Where the Error Hides |
|---|---|---|
| Client intake note on who the parties are | Which statute applies and who must receive the letter | A business claimant drafted under the consumer section (93A § 11 has no § 9(3) demand and no bad-faith-refusal multiplier); a trade name instead of the Secretary of State entity; a letter addressed to a party whose counsel has already written in the matter (Rule 4.2) |
| Client damages spreadsheet or lump-sum figure | §4 damages and the demand total | A multiplier applied to the wrong base (DTPA "knowing" trebles economic damages only; mental anguish is trebled only on an intentional finding); fees claimed with no contract or statute; a total presented as computed when it was supplied; a demand above the authorized ceiling |
| Statutory pre-suit regime | Contents, service method and the waiting period | One 30-day default used for every regime, though each clock has its own length and trigger (mailing, delivery, receipt, filing); required contents missing (DTPA amounts stated separately; Florida expert affidavit; Chapter 558 reference to the chapter) |
| Contract notice and cure clause | Notice method, address, cure period, forum | A deadline shorter than the contractual cure period; email used where the clause requires courier; a forum named in breach of a forum-selection or arbitration clause |
| Consumer-debt facts (law firm regularly collects for the client) | Whether the FDCPA and Regulation F apply | Missing validation information or mini-Miranda; a 10-day pay-or-sue deadline inside the validation period (overshadowing, § 1692g(b)) |
| Facts with criminal or regulatory overlap (embezzlement, bad checks, licensed recipient) | Tone and leverage in §7 | A conditional threat to go to the prosecutor, licensing board or bar; "reserve the right to refer" phrasing that reads as the same threat (California Rule 3.10 bars threatening criminal, administrative or disciplinary charges) |
| A request for a "policy-limits letter" to a liability insurer, or any pre-answer offer on a Georgia motor-vehicle injury claim | Choice of workflow and template branch | An offer drafted here instead of in `bad-faith-demand`, whether or not it is called time-limited, missing statutory material terms and minimum periods (O.C.G.A. § 9-11-67.1(b) covers every attorney-prepared pre-answer offer on such a claim: acceptance at least 30 days from receipt) |
| Client wish to "go public" or tell customers, the press or a regulator unless paid | Leverage in §7 and the cover email | A demand for money coupled with a threat of exposure or accusation, which can be criminal extortion even in a lawyer's letter (*Flatley v. Mauro*, 39 Cal. 4th 299 (2006)); copying customers or the press, which also strips litigation privilege |
| Client facts that sound like elements | §2 narrative and §3 theories | A cause of action pleaded without one sourced fact per element; conclusory labels ("fraudulent", "willful") with no supporting facts |

## Ground Rules

1. **Draft only.** Never state or imply that a letter is ready to send. Attorney review, signature and service are required; if the user says "send it," stop and say so.
2. **Source-review gate.** Before calling any document or fact missing, check what was provided and try to open, extract or OCR it. Classify every remaining gap as an unknown fact, a source conflict, an unverified external lookup (Secretary of State, registered agent, statute currency), or a policy election (client choices such as forum, FRE 408 posture, the demand number).
3. **Hierarchy of authority.** Executed contract and amendments, then statute and regulation text, then the underlying records (invoices, bank records, medical records), then correspondence, then client summaries, spreadsheets and emails. When sources conflict, name both in the reconciliation table, say which controls and why, and use the controlling value. Never resolve a conflict silently.
4. **Citation discipline.** Every factual assertion and damages line carries a source locator (exhibit, document, page) or `[UNVERIFIED — client-provided]`. Every statute and case is verified through `legal-research` and `citation-bluebook` or marked `[VERIFY]`. Never invent a citation, registered agent, address or verdict.
5. **Elements before theories.** Plead a cause of action only when §2 has at least one sourced fact for each element (Model Rule 3.1). If an element is unsupported, drop the theory and tell the user.
6. **The statute overrides the template.** Where a pre-suit regime applies, its contents, service method and waiting period control over every default in this file.
7. **No threats of criminal, administrative or disciplinary charges, or of public exposure,** to gain advantage in the civil matter, in any form, including "reserve the right to refer" phrasing (house rule; California Rule 3.10 and its Comment [1] bar stating or implying that such charges will be pursued unless the matter settles; a threat of exposure tied to payment can be extortion).
8. **No unsupported money.** No multiplier, fee, interest or consequential-damages claim without its verified basis and shown arithmetic. Never disclose the client's ceiling or walkaway number.
9. **Stay in lane.** Any offer to a liability insurer to settle within limits, and any pre-answer attorney offer on a Georgia motor-vehicle injury claim, goes to `bad-faith-demand`; a coverage position goes to `coverage-opinion`. Hand off with the facts, not just the skill name.

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Governing contract(s)** — notice clauses, cure provisions, forum-selection, arbitration clauses.
2. **Correspondence** — emails, letters, texts in chronological order, including any letter from opposing counsel.
3. **Financial records** — invoices, payments, chargebacks, proof of tender, bank records.
4. **Supporting evidence** — incident reports, photos, expert reports, third-party communications.
5. **Prior demands** — settlement communications or notices already sent.
6. **Statute of limitations** — accrual date, tolling facts, contractual limitations periods. If tolling facts exist, the accrual date is unclear, or the claim is near limitations, run `legal-research` before drafting.
7. **Forum facts** — entity citizenship, principal place of business, forum-selection clauses.
8. **Client objectives** — preferred outcome, authorized settlement ceiling, timing, relationship preservation. This ceiling is the "authorized range" in Checkpoint B.
9. **Recipient entity and claimant status** — legal name as filed with the Secretary of State, registered agent, contractual notice address; whether claimant and recipient are consumers or businesses. Verify through the state's business-entity search; if the state is unknown, ask.
10. **Represented-party check** — is the recipient known to be represented by counsel in this matter? If yes, the letter goes to counsel (`references/ETHICS-AND-PRIVILEGE.md`).

**Defaults** (if the user says "use defaults" or does not respond): general demand for payment; commercial dispute; FRE 408 header; formal professional tone; 30-day response deadline, which any applicable statute or contract overrides (DTPA 60 days' notice before filing; Florida medical malpractice 90 days after delivery; Chapter 558 60 or 120 days; FDCPA validation period; a longer contractual cure period). Label every default in the draft.

**Hard stops.** Do not produce a letter, or the named part of it, when:

- The limitations period would run before the statutory waiting period ends. Escalate to the attorney with the dates; the statute may excuse notice (for example DTPA § 17.505(b)).
- A statutory prerequisite cannot be met on the materials given (for example a Florida notice of intent with no verified expert opinion). Do not call the notice compliant; list what is missing.
- The demand total exceeds the authorized ceiling, or no ceiling was given, unless the letter demands a liquidated balance in full and offers no compromise. Use a `{{DEMAND AMOUNT — attorney to set}}` placeholder.
- The user asks for a threat of criminal, administrative or disciplinary charges, or of exposure to the media, customers or the public unless paid. Decline that content and draft the civil demand.
- The sender is a debt collector on a consumer debt and the user wants a payment or suit deadline before the validation period ends. Set no such deadline.
- The request is any offer to a liability insurer to settle within limits, or any pre-answer attorney offer on a Georgia motor-vehicle injury claim, however labeled. Route to `bad-faith-demand`.

## Step 1: Diagnose Legal Function

- Analyze contractual notice requirements: methods, deemed-received provisions, cure periods.
- Classify the letter: demand for payment, breach plus intent to terminate, anchored settlement invitation, preservation trigger, or statutory prerequisite.
- Align with the dispute-resolution mechanism; do not threaten filing in an improper forum (arbitration clauses govern).

**Statutory pre-suit branch.** If any of these apply, read `references/JURISDICTION-PRESUIT.md` and follow its row before Step 2: MA Ch. 93A § 9 (and the § 11 carve-out); TX DTPA § 17.505; CA CLRA § 1782(a); FL Ch. 766; construction defect (CA SB 800, TX Ch. 27, FL Ch. 558); FDCPA § 1692g and Regulation F; MMWA opportunity to cure; Stowers background; defamation retraction. If the claim or state is not listed, run `legal-research` with the query template at the bottom of that file.

**Exemplar lookup.** Find the nearest archetype in `references/ARCHETYPE-INDEX.md` and read its text exemplar in `assets/examples/` before drafting, for tone, length and cite density. If none matches, say so.

**Template branch.** Read `references/TEMPLATE.md` and pick one branch: `statutory-notice`, `insurer-claim` (a claim presentation to an insurer that makes no offer and sets no lapse date), or `commercial`.

## Step 2: Build Element-Driven Fact Narrative

- Chronological structure tied to claim elements; source every fact inline ("On April 18, your project manager wrote…", Exhibit B).
- Quote contract terms and correspondence exactly; selective quotation is an attack surface.
- No conclusory labels ("fraudulent," "criminal," "willful") without facts for each element of the label.
- Opposing counsel will mine this section for admissions.

**Decision rule.** One source-cited fact per claim element, minimum. If an element has no support, do not plead that cause of action in Step 3; tell the user what is missing.

## Step 3: Articulate Legal Theories

- State primary claims tied to the requested remedy; do not over-plead.
- Cite specific statutory sections for UDAP and fee-shifting hooks; mark unverified citations `[VERIFY]`.
- Never assert fee recovery without a verified contractual or statutory basis (`references/ETHICS-AND-PRIVILEGE.md`, fee-recovery rule).

**Primary-vs-secondary rule.** The primary claim is the one whose elements are best supported by §2 facts and whose remedy matches the client objective (Checkpoint A item 8). Add a secondary claim only if it independently unlocks a remedy (fees, punitive, treble) or survives a foreseeable defense to the primary.

**Verification trigger.** Every statutory citation goes to `legal-research`; every case citation to `citation-bluebook`. Unverified stays `[VERIFY]` inline.

## Step 4: Quantify Damages

Read `references/DAMAGES-METHODOLOGY.md`. Categories: direct, consequential, statutory multipliers, prejudgment interest, liquidated, mitigation offsets, fees and costs. Follow its cross-cutting rules, including what to do with a client total that has no line-item backup. Recompute every figure from its sources; for a multiplier, name the conduct finding it requires and the base it multiplies. Address mitigation, offsets and credits affirmatively. Never reveal the walkaway number.

## Step 5: Include Preservation Notice

Include litigation-hold language covering documents and ESI and suspension of routine destruction (`references/TEMPLATE.md` §5). That paragraph is a trigger and catch-all. For high-risk evidence (short-retention surveillance video, vehicle EDR data, product exemplars, custodian-controlled ESI, medical devices), invoke `spoliation-letter` for an itemized preservation demand.

## Step 6: Frame Demands and Proposed Resolution

- Monetary: amount, payee, timing, method. Non-monetary: deliverables, acceptance criteria, deadlines.
- **Term-sheet rule.** Include release scope, confidentiality and non-disparagement only when the letter explicitly invites settlement. Omit them from pure statutory notices (93A, DTPA, CLRA, FDCPA § 1692g, Florida medical malpractice). Boilerplate is in `references/TEMPLATE.md` §6.

## Step 7: Set Deadline and Consequences

- Use calendar dates, not relative periods ("by [date]", not "within 10 days"); align with contractual cure periods.
- State intent to file and name the forum. Never threaten criminal, administrative or disciplinary action (`references/ETHICS-AND-PRIVILEGE.md`, forbidden phrasings).

**Clock table.** Compute each timed element from its own trigger and show it in the drafting notes:

| Element | Length | Trigger |
|---|---|---|
| MA 93A § 9(3) demand before suit; tender window | 30 days; 30 days | Mailing or delivery of the demand |
| TX DTPA § 17.505 notice before suit | 60 days | Notice given; recipient's offer window runs 60 days from its receipt |
| CA CLRA § 1782 correction window | 30 days | Recipient's receipt of the notice |
| FL § 766.106 presuit period | 90 days | Delivery of the notice of intent |
| FL § 558.004 notice before suit | 60 days (120 for an association of more than 20 parcels) | Service of the notice of claim |
| FDCPA / Regulation F validation period | 30 days | Consumer's receipt; may be assumed 5 days after sending, excluding weekends and legal public holidays |
| Contractual cure period | Per clause | The clause's deemed-receipt rule |

Default deadline 30 calendar days, overridden as above. Sub-14-day deadlines only for imminent harm (ongoing infringement, spoliation risk, a foreclosure sale date), justified in the letter.

**Forum rule.** A forum-selection clause controls. Otherwise name a forum with personal jurisdiction over the recipient and proper venue (28 U.S.C. § 1391 or the state equivalent), matching the client's preference; if undecided, flag and ask.

## Step 8: Calibrate Tone and Privilege Posture

- Write as if a judge will read it.
- Decide the "Settlement Communication — Subject to FRE 408 / State Equivalent" header using `references/TEMPLATE.md` (optional FRE 408 header) and the reality check in `references/ETHICS-AND-PRIVILEGE.md`.
- Exclude defamatory statements, attorney-client communications, and unnecessary personal information. Copy no one without a legitimate interest.

## Checkpoint B: Post-Draft Alignment

After delivering the draft, ask:

1. Is the recipient entity, notice address and addressee (party or counsel) correct?
2. Is the demand total within the authorized range (Checkpoint A item 8)? If it exceeds the ceiling, stop and escalate to the attorney. Never send an unauthorized demand number.
3. Are statutory pre-suit requirements verified before sending (`references/JURISDICTION-PRESUIT.md`)?
4. Should this go as a settlement communication (FRE 408) or an unconditional demand?

If the user does not answer, recommend verifying the recipient entity and notice method (the most common failure point) and proceed only if Checkpoint A item 8 authorized the demand total.

## Quality Audit

Confirm each item before responding. If one fails, fix the draft.

1. Recipient entity and notice address match the Secretary of State record and the contract, with the source recorded; a represented recipient is addressed through counsel and the party is not copied.
2. Claimant and recipient status (consumer or business) was decided before the statute was chosen, and the statute's section matches it.
3. The contractual notice method is used and stated; the deadline is not shorter than any cure period.
4. Every factual assertion and damages line has a source locator or `[UNVERIFIED — client-provided]`, and the source map in the drafting notes covers all of them.
5. Every pleaded claim has one sourced fact per element; no conclusory labels without supporting facts.
6. Every citation is verified through `legal-research` or `citation-bluebook`, or marked `[VERIFY]`.
7. Damages reconcile: line items sum to the total; each multiplier names its conduct finding and base; interest shows rate, accrual date and source; fees cite a verified clause or subsection; mitigation and credits addressed.
8. Each deadline is a calendar date computed from its own trigger in the clock table; statutory periods override the 30-day default.
9. No threat of criminal, administrative or disciplinary charges, or of public exposure, tied to payment; the prophylactic sentence is included where conduct has criminal overlap.
10. FDCPA and Regulation F content (mini-Miranda, validation information, validation period end date, no overshadowing deadline) is present whenever the sender is a debt collector on a consumer debt.
11. FRE 408 posture decided under the `references/ETHICS-AND-PRIVILEGE.md` rule; preservation paragraph present, with `spoliation-letter` invoked for high-risk evidence.
12. Exemplar consulted (name the `assets/examples/` file) or no-match stated; one template branch only; signature block carries the bar number.
13. Drafting notes include the reconciliation table, gap register, hand-offs and `[VERIFY]` list, and the response says attorney review is required before sending.

## Guidelines

- **Using this file.** An agent runs Checkpoint A, Steps 1-8, Checkpoint B and the Quality Audit in order and states when a step does not apply. An attorney can use the steps as a checklist and the Quality Audit as the pre-send gate; the decision rules mark where the default posture yields to attorney judgment, which should be overridden consciously, not by omission.
- **Output format.** Return the letter and drafting notes inline. Invoke `anthropic-skills:docx` or `anthropic-skills:pdf` only when the user asks for a file and only after the Quality Audit passes.
- **Jurisdiction.** `references/JURISDICTION-PRESUIT.md` covers 93A, DTPA, Stowers, CLRA, construction defect, Florida medical malpractice, FDCPA and Regulation F, MMWA and retraction statutes; anything else goes to `legal-research`.
- **Ethics.** `references/ETHICS-AND-PRIVILEGE.md` covers Model Rules 3.1, 4.1, 4.2 and 8.4, state threat rules, FRE 408, FDCPA disclosures, privilege and forbidden phrasings.
- **Exemplars.** `references/ARCHETYPE-INDEX.md` maps the 14 text exemplars in `assets/examples/` with use-when and do-not-copy notes.
- **Anti-hallucination.** Do not invent statutory citations, case names, verdicts, registered agents or addresses. If a fact or source is uncertain, flag it rather than publish it.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| A contract or invoice the client mentioned "is not in the file" | Scanned PDF, image attachment or unrelated file name | Open every file, OCR scans, then classify the gap; never call it missing on a text search alone |
| Two documents give different amounts or dates | Amendment, partial payment, or a client spreadsheet built from memory | Reconciliation table; the higher-ranked source controls; tell the user |
| Entity search returns no match or several | Trade name, merger, or a lookup that failed | Record the outcome as an unverified external lookup; use a placeholder, never a guessed entity |
| A record is illegible or redacted | Poor scan, privilege redaction | State what could not be read and which assertions depend on it; mark them `[UNVERIFIED — client-provided]` |
| Client insists on a deadline shorter than the statute or contract allows | Leverage instinct | Use the statutory or contractual date; explain the consequence in the drafting notes |
| Client total is higher than the computed damages | Multiplier on the wrong base, fees without basis, or an intentional-conduct assumption | Show both figures and the finding each requires; Checkpoint B ceiling check |
| Opposing counsel appears mid-matter | New representation | Re-address to counsel; drop the party from the cc line |

## Related Skills

- legal-research: verify the pre-suit regime, limitations and tolling, and any statute the letter cites.
- citation-bluebook: format and good-law status for every case cited.
- spoliation-letter: dedicated, itemized preservation demand when Step 5 finds high-risk evidence.
- bad-faith-demand: any offer to a liability insurer to settle within policy limits (Stowers or a similar regime) and any pre-answer attorney offer on a Georgia motor-vehicle injury claim (O.C.G.A. § 9-11-67.1); hand over the insured, limits, injuries, liens and deadline facts.
- coverage-opinion: whether a policy covers the claim, duty to defend or indemnify, or a reservation-of-rights position.
- pi-demand-summary: builds the personal-injury damages narrative that feeds §4.
- demand-package and demand-package-compilation: assemble the letter and exhibits into a transmittable package.
- settlement-agreement: drafts the release once the recipient accepts.
- anthropic-skills:docx and anthropic-skills:pdf: produce the final file after the Quality Audit passes.

## Reference Files

| File | Read it when |
|---|---|
| `references/TEMPLATE.md` | Choosing a branch, drafting §1-§8, and assembling the drafting notes (output template) |
| `references/JURISDICTION-PRESUIT.md` | Any statutory pre-suit regime, its contents, service method and clock |
| `references/DAMAGES-METHODOLOGY.md` | Step 4: every damages category, multiplier base, interest and fees |
| `references/ETHICS-AND-PRIVILEGE.md` | Steps 3, 7 and 8; represented parties, threats, FRE 408, FDCPA disclosures |
| `references/ARCHETYPE-INDEX.md` | Step 1 exemplar lookup in `assets/examples/` |
| `references/primary-sources.md` | Citing a statute or rule; what was checked, when, and the `[VERIFY]` list |
