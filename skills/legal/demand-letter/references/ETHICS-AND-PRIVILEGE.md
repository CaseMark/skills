# Ethics, Privilege, and Required Disclosures

Read this file before Step 8 of `../SKILL.md` (tone calibration) and whenever any of the triggers below fires. A demand letter is simultaneously a settlement instrument, a future exhibit, and a regulated communication. Ethics violations and missed disclosures are not style issues — they are grounds for bar discipline, statutory damages against the sender, and dismissal of the underlying claim.

All rule references are to the ABA Model Rules of Professional Conduct. Every state has adopted its own variant; conform to the sending attorney's actual state rules. Citations here are defaults — `[VERIFY]` each one against the governing state. The Model Rule text quoted below was re-read on the ABA site on October 30, 2026 (see `primary-sources.md`).

## Contents

- Model Rule 3.1: meritorious claims
- Model Rule 4.1: truthfulness
- Model Rule 4.2: represented persons
- Model Rule 8.4 and threats of criminal, administrative or disciplinary charges
- Fee-recovery rule
- FRE 408 / state-evidence-rule reality check
- FDCPA and Regulation F: required disclosures
- Work-product and privilege: what not to disclose
- Defamation and privilege within the letter
- Pre-send checklist

---

## Model Rule 3.1 — Meritorious Claims and Contentions

> "A lawyer shall not bring or defend a proceeding, or assert or controvert an issue therein, unless there is a basis in law and fact for doing so that is not frivolous …"

**What this forbids in a demand letter.**
- Asserting a legal theory without a factual basis for each element.
- Threatening claims that the drafter knows have no legal support.
- Multiplying theories purely to inflate settlement pressure.

**Agent action.** Before asserting any cause of action in §3 of the draft, confirm §2 of the draft contains at least one source-cited fact for every element. If an element lacks factual support, drop that cause of action and tell the user.

## Model Rule 4.1 — Truthfulness in Statements to Others

> "In the course of representing a client a lawyer shall not knowingly: (a) make a false statement of material fact or law to a third person …"

**What this forbids.**
- Misstating the holding of a case.
- Overstating the amount of damages available under a statute.
- Inventing facts, witnesses, or documents.
- Asserting fee-recovery entitlements that no statute or contract supports.

**Agent action.**
- Every statutory cite → verify via `legal-research`.
- Every case cite → verify format and good-law status via `citation-bluebook`.
- Every factual assertion → traceable to an exhibit or source, or labeled `[UNVERIFIED — client-provided]`.
- Fee claim → identify contract section or statutory subsection that authorizes it; if neither, drop the fee claim.

**Anti-hallucination rule.** If `legal-research` or `citation-bluebook` has not been run and an authority is uncertain, mark it `[VERIFY]` inline. Do not publish an unverified citation.

## Model Rule 4.2 — Communication with Represented Persons

> "In representing a client, a lawyer shall not communicate about the subject of the representation with a person the lawyer knows to be represented by another lawyer in the matter, unless the lawyer has the consent of the other lawyer or is authorized to do so by law or a court order."

**What this forbids in demand-letter context.**
- Sending a demand letter directly to the party when the drafter knows the party has retained counsel in the matter. The rule requires actual knowledge, but knowledge may be inferred from the circumstances; a lawyer cannot close their eyes to the obvious (Comment [8]).
- Copying the party on a letter when counsel is known — the "cc" to the party triggers the same rule.
- For a represented organization, communicating with a constituent who supervises, directs or regularly consults with the organization's lawyer about the matter, who can obligate the organization in the matter, or whose act or omission may be imputed to it (Comment [7]). Former constituents are outside the rule.

**Represented-party workflow (Checkpoint A, new item 10 in SKILL.md).**
1. Ask the user: "Is the recipient party known or reasonably believed to be represented by counsel in this matter?"
2. If yes → the letter must be addressed and served to counsel. The recipient party may appear on the `cc:` line only if counsel consents.
3. If unknown but the counterparty is a corporation → reasonable inquiry required. Standard practice: if prior correspondence has come from a specific attorney or firm, address there.
4. If no → address the party directly.

**What this rule does NOT forbid.**
- Sending a statutorily-required pre-suit notice to an address specified by statute (e.g., registered agent). The "authorized by law" exception covers this. Best practice is still to serve known counsel concurrently.
- Sending a letter to a party when no counsel is known, even if counsel is later retained before receipt.

## Model Rule 8.4 — Misconduct

> "It is professional misconduct for a lawyer to: … (b) commit a criminal act that reflects adversely on the lawyer's honesty, trustworthiness, or fitness as a lawyer in other respects; … (d) engage in conduct that is prejudicial to the administration of justice …"

**In demand-letter context — the "criminal-threat leverage" rule.** The rules differ by state, and this skill applies the strictest version as its house rule.
- The ABA Model Rules contain no counterpart to DR 7-105(A) of the former Model Code of Professional Responsibility, which barred threatening criminal charges solely to gain an advantage in a civil matter. ABA Formal Opinion 92-363 (1992) reads the Model Rules to permit raising possible criminal charges only when the criminal matter is related to the civil claim, both are warranted by law and fact, and no improper influence over the criminal process is suggested; Rules 4.1, 8.4(b)-(d) and state extortion statutes still apply.
- Several states keep an express ban. California Rule of Professional Conduct 3.10 (effective November 1, 2018): a lawyer shall not threaten to present criminal, administrative, or disciplinary charges to obtain an advantage in a civil dispute. "Administrative charges" include a complaint to any body that can suspend a license or impose a fine. Identify the sending lawyer's state rule `[VERIFY]` before relying on the ABA position.

**Forbidden phrasings — never generate any of these.**
- "Unless the sum of $X is paid, we will refer this matter to the [District Attorney | United States Attorney | FBI] for criminal prosecution."
- "Failure to comply will result in criminal charges being filed against you."
- "This conduct constitutes [wire fraud | mail fraud | embezzlement]; pay now to avoid prosecution."
- "We will report this to the IRS as tax evasion if payment is not received."
- "If you do not settle, we will file a bar complaint against you."
- "We will contact your employer / licensing board / immigration authorities if you do not pay."

**Permissible phrasings — what you CAN say.**
- "This letter does not constitute a threat of criminal prosecution, and nothing herein should be construed as one." (Standard prophylactic — include in §7 of the template when any conduct described could have criminal overlap.)
- Factual descriptions of conduct that happens to be criminal, when the letter seeks only civil remedies, without a conditional threat linking non-payment to referral.
- Regulatory references as information ("We note that [agency] maintains jurisdiction over this conduct") — but not as leverage.

**Gray area (jurisdiction-specific `[VERIFY]`).** Statements that "we reserve all rights, including referral to regulatory authorities" are permissible in some jurisdictions, prohibited in others. When in doubt, omit.

---

## Fee-recovery rule

**Never claim attorney's fees without a verified basis.** This is both a Rule 4.1 issue (false statement of law) and a malpractice concern.

Acceptable bases:
- Contract fee-shifting clause, verbatim-quoted in the letter.
- Statutory fee-shifting provision, cited with pinpoint. See `DAMAGES-METHODOLOGY.md` Category 7 for a list.
- Bad-faith common-law exception in the governing jurisdiction, verified via `legal-research`.

Unacceptable:
- "You will be liable for our fees if this proceeds to litigation" — without identifying the statute or clause that would create that liability.
- "We will seek fees under [statute that does not provide for them]."
- Bluffing fee-shifting to inflate settlement pressure.

---

## FRE 408 / state-evidence-rule reality check

Federal Rule of Evidence 408 (and most state analogs) excludes offers to compromise and conduct / statements made during compromise negotiations from evidence **to prove or disprove the validity or amount of a disputed claim, or to impeach by prior inconsistent statement**. The rule has carve-outs that frequently swallow it:

- **Admissible for other purposes.** Statements in the letter can still be used to prove bias, negate a contention of undue delay, prove effort to obstruct a criminal investigation, etc.
- **Admissible in later disputes.** If the demand letter becomes evidence in a different dispute (e.g., a coverage dispute between insurer and insured), FRE 408 may not exclude it.
- **State variation.** State rules differ in scope. Georgia's current rule is O.C.G.A. § 24-4-408 (2013 evidence code, replacing former § 24-3-37); its subsection (b) excludes conduct or statements made in compromise negotiations without FRE 408's purpose limits, subject to the "another purpose" exceptions in subsection (c). California's analog is Evidence Code § 1152 `[VERIFY]`. Confirm the governing rule before relying on it.
- **Business torts.** Some jurisdictions admit demand-letter language to prove a bad-faith-refusal-to-settle claim against an insurer — the whole point of a Stowers/Holt letter is that the insurer's response is admissible in the subsequent coverage action.

**Drafter's rule.** Draft every sentence of every demand letter as if it is admissible. The FRE 408 label is a signal to the recipient and a modest hedge at trial — not a shield against a well-drafted admissibility argument. Factual admissions, conclusory accusations, and defamatory statements belong nowhere in a demand letter, labeled or not.

**When to keep the FRE 408 header (from TEMPLATE.md §Optional FRE 408 header):**
- Letter explicitly invites settlement.
- Letter includes a specific number that may be withdrawn or modified.
- Letter includes release or term-sheet language.

**When to omit:**
- Pure statutory-notice letter satisfying a pre-suit prerequisite (Ch. 93A, DTPA, CLRA, FDCPA § 1692g). The statutes contemplate the letter itself being admissible.
- Pure cease-and-desist with no monetary compromise offered.
- Policy-limits demand where the drafter affirmatively wants the letter admissible in a subsequent bad-faith/Stowers/Holt action against the insurer. (Tactical choice; `[VERIFY]` with governing jurisdiction's bad-faith framework.)

---

## FDCPA — required verbatim disclosures

Triggers: sender is a "debt collector" under 15 U.S.C. § 1692a(6) **AND** communication concerns a "debt" under § 1692a(5) (consumer obligation for personal, family, or household purposes). Attorneys who regularly collect consumer debts, including through litigation, are debt collectors (*Heintz v. Jenkins*, 514 U.S. 291 (1995)). Regulation F (12 C.F.R. Part 1006) implements the Act and now controls the content of both disclosures below. See `JURISDICTION-PRESUIT.md` for a fuller FDCPA row.

### § 1692e(11) — "mini-Miranda" disclosure

The FDCPA requires disclosure that the communication is from a debt collector (§ 1692e(11); 12 C.F.R. § 1006.18(e)). The required content differs between initial and subsequent communications, and the disclosure is not required in a formal pleading.

**Initial written communication with the consumer.** Include a statement (verbatim or substantive equivalent):

> "This is an attempt to collect a debt. Any information obtained will be used for that purpose. This communication is from a debt collector."

**Subsequent written communications with the consumer** (after the initial). Include at minimum:

> "This communication is from a debt collector."

**Placement.** Conspicuous. Common practice is immediately above the salutation or immediately below the Re: line. Do not bury it in a footer or the signature block.

### § 1692g — validation notice

Required in the initial written communication with the consumer or within 5 days after the initial communication. Under Regulation F, the notice must carry the validation information in 12 C.F.R. § 1006.34(c), which goes beyond the five statutory items below: the collector's name and dispute address, the consumer's name and address, the itemization date, the amount on that date, an itemization of interest, fees, payments and credits since then, the current amount, the date the collector will treat as the end of the validation period, and the consumer-response prompts. Model Form B-1 (Appendix B to Part 1006) is a safe harbor. The statutory core is:

1. The amount of the debt.
2. The name of the creditor to whom the debt is owed.
3. A statement that unless the consumer, within 30 days after receipt of the notice, disputes the validity of the debt or any portion thereof, the debt will be assumed to be valid by the debt collector.
4. A statement that if the consumer notifies the debt collector in writing within the 30-day period that the debt, or any portion thereof, is disputed, the debt collector will obtain verification of the debt or a copy of a judgment against the consumer and a copy of such verification or judgment will be mailed to the consumer by the debt collector.
5. A statement that, upon the consumer's written request within the 30-day period, the debt collector will provide the consumer with the name and address of the original creditor, if different from the current creditor.

**Overshadowing rule.** Collection activities and communications during the 30-day period may not overshadow or be inconsistent with the disclosure of the consumer's right to dispute the debt or request original-creditor information (§ 1692g(b)). A demand to pay, or a threat to sue, by a date inside the validation period is the classic overshadowing pattern; this skill never sets a payment or suit deadline earlier than the validation period end date. Compute that date under § 1006.34(b)(5): 30 days after the consumer receives the notice, where receipt may be assumed on any date at least five days (excluding legal public holidays, Saturdays and Sundays) after the collector provides it.

### State-law analogs

Many states have parallel regimes with additional disclosures: California Rosenthal Fair Debt Collection Practices Act, New York General Business Law § 600 et seq. + DFS Regulation Part 1, Texas Finance Code Ch. 392, and others. **If the consumer is outside the federal-only rule, check the state analog via `legal-research`.**

### Consequence of omission

- Additional damages up to $1,000 in an individual action; in a class action, up to the lesser of $500,000 or 1 percent of the collector's net worth for the unnamed members (§ 1692k(a)(2)).
- Actual damages.
- Costs and attorney's fees to the consumer-plaintiff (§ 1692k(a)(3)).
- Reputational cost (FDCPA violations are enforced by the CFPB and FTC and are class-action-prone).

Omission of § 1692e(11) or § 1692g is among the most common and most easily proven FDCPA violations.

---

## Work-product and privilege — what NOT to disclose in a demand letter

A demand letter is a communication with an adversary. It is **not** privileged, it is **not** work product, and it will be produced in discovery if the matter proceeds. Draft accordingly.

**Never disclose in a demand letter:**
- The client's walkaway number, settlement ceiling, or authorized range.
- Witness-credibility assessments (positive or negative).
- The identity of retained experts or the substance of their preliminary opinions, unless attaching the final expert report as an exhibit.
- Internal legal-theory evaluations ("we considered claim X but rejected it because of weakness Y").
- Prior settlement discussions with other parties not mentioned in the narrative.
- Client's financial position or insurance coverage (unless strategically disclosed as a Stowers/Holt lever, with specific reason).
- Privileged attorney-client communications (even summaries).
- Internal investigation memoranda.
- Prior draft versions of the letter.
- The client's risk tolerance or litigation appetite.

**What you CAN disclose without waiver concerns:**
- The factual narrative (§2 of the letter) — already assumed to be admissible.
- The legal theories being asserted (§3) — required to put the adversary on notice.
- The damages methodology and amounts (§4) — required for the demand to be meaningful.
- Exhibits attached as evidence — they are documents, not privileged.
- The name of the sending attorney — obvious.

**When in doubt.** Omit. A short, focused letter preserves leverage better than a long one that leaks strategy.

---

## Defamation and privilege within the letter

Statements in a demand letter are generally protected by a **qualified litigation privilege** in most jurisdictions — a pre-suit privilege for statements made in anticipation of litigation, provided the statements are made in good faith and have some reasonable relation to the contemplated litigation. The privilege is not absolute in all jurisdictions, and it does not protect:

- Statements made to persons with no legitimate interest in the matter (e.g., cc'ing the recipient's employer, customers, or the press without a stake in the dispute).
- Statements demonstrably made without a good-faith basis.
- Statements beyond the scope of the contemplated claims (e.g., gratuitous attacks on the recipient's character unrelated to the dispute).

**Rule.** Draft every statement in the letter as if it will be tested against an abuse-of-privilege standard. Do not include facts or conclusions that serve no purpose except to damage the recipient's reputation. Do not cc anyone without a legitimate interest. Do not publish the letter — including to the press or on a client website — without a separate analysis of republication liability.

---

## Pre-send checklist (tied to `../SKILL.md` Quality Audit)

- [ ] Rule 3.1: every pleaded claim has source-cited factual support for every element.
- [ ] Rule 4.1: every citation verified via `legal-research` / `citation-bluebook` or marked `[VERIFY]`.
- [ ] Rule 4.2: if recipient is represented, letter addressed and served to counsel.
- [ ] Rule 8.4: no criminal-threat leverage; prophylactic disclaimer included where conduct has criminal overlap.
- [ ] Fee claims backed by verified contract or statute.
- [ ] FRE 408 label kept or omitted per the decision rule; choice is defensible.
- [ ] FDCPA: if applicable, § 1692e(11) and § 1692g disclosures present and not overshadowed.
- [ ] No work-product or privileged material disclosed.
- [ ] No defamatory or gratuitous statements; cc list limited to legitimate interest.
- [ ] Bar number on signature block.
