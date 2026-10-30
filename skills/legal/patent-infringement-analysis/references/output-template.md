# Output Template

Produce the header and nine parts in this order. Put detail in tables; keep sentences plain. Every date shows its weekday. Quote claim language only from the text in force (original patent or the latest certificate), with column and line or certificate page.

## Contents

1. Header and source-review register
2. Part 1. Analysis status and claim positions
3. Part 2. Patent status and claim version
4. Part 3. Claim construction
5. Part 4. Accused product evidence register
6. Part 5. Claim charts
7. Part 6. Infringement theories: actor, place and knowledge
8. Part 7. Remedy windows and willfulness facts
9. Part 8. Blocking issues and reconciliation table
10. Part 9. Hand-offs, open items and `[VERIFY]` list

## Header

- Matter, client, the client's side (patent owner, exclusive licensee, accused party, supplier, customer), requester and role, purpose (pre-suit assessment, response to notice letter, litigation, design-around review), today's date.
- Line: "Draft infringement analysis prepared at the direction of counsel for attorney review. Not an opinion of counsel."
- Patent(s) and asserted claims; accused products, versions and dates.
- **Source-review register**, one row per file:

| File | Type | Date or version | Status | Pages or files read | Note |
|---|---|---|---|---|---|
| name as received | patent, file history paper, certificate, IPR paper, assignment, license, source code, schematic, teardown, data sheet, marketing, letter | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Analysis status and claim positions

**Analysis status**, one label used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open; the analysis is still included unless a hard stop applies.
- **Declined: hard stop**: give the reason, the request or routing the hard stop calls for, and what can be done instead.

**Claim position**, one label per asserted claim and accused version, used exactly:

- **Infringement position supported**: every limitation "Met literally" or "Met under DOE only," with a direct infringer identified.
- **Non-infringement position supported**: at least one limitation "Not met" under the construction most favorable to the patent owner, or no attributable direct infringer.
- **Contested: both positions arguable**: the result turns on a disputed construction or disputed evidence; state which.
- **Not determinable on current evidence**: a limitation rests only on evidence below rank 2, or evidence is missing; list what decides it.

Then a one-paragraph summary: the position per claim, the main reason, the main risk if the position is wrong, and the next step. State results adverse to the client plainly.

## Part 2. Patent status and claim version

| Claim | Depends on | Original text locator | Certificates (type, number, date) | Text in force | Status label |
|---|---|---|---|---|---|

Status labels, used exactly: **In force: original text**; **In force: text amended by certificate**; **Canceled**; **Expired**; **Unenforceable period flagged**; **Status unconfirmed**.

Term computation, with its own trigger for each element:

| Element | Trigger event | Trigger date (weekday) and evidence | Period | Result date (weekday) | Source |
|---|---|---|---|---|---|
| Statutory term | earliest U.S. application referenced under 120/121/365(c)/386(c) | | 20 years | | 154(a)(2) |
| Term adjustment or extension | face of patent; USPTO record | | days | | 154(b) |
| Terminal disclaimer | end of the reference patent's full statutory term as the disclaimer defines it (early lapse of the reference patent does not count unless the disclaimer says so) | | | | 253(b); 1.321; MPEP 1490 |
| Common ownership for a double-patenting disclaimer | any date common ownership ended | | | | 1.321(c)(3) |
| Maintenance fees | grant date | | 3.5/7.5/11.5 years + 6 months | | 41(b) |

**IPR register**, one row per IPR or reexamination:

| Proceeding | Petitioner and real parties in interest | Claims challenged | Grounds | Final decision and date | Certificate and date | Patent owner statements bearing on construction (paper, page) | 315(e) estoppel reach |
|---|---|---|---|---|---|---|---|

## Part 3. Claim construction

| Term | Claim(s) | Proposed construction | Intrinsic support (col:line; file history paper and page; IPR paper and page) | Opposing construction | Lexicography or disavowal? | Outcome changes? |
|---|---|---|---|---|---|---|

For each 112(f) or nonce term: claimed function; corresponding structure or algorithm with locator; whether the specification discloses it.

## Part 4. Accused product evidence register

| Accused product and version | Evidence item | Evidence rank (1-5) | Date or version covered | Locator | Limitations it bears on |
|---|---|---|---|---|---|

## Part 5. Claim charts

One chart per claim per accused version:

| # | Limitation (text in force) | Construction applied | Accused feature and evidence (locator, rank) | Why it meets or does not meet | Limitation label |
|---|---|---|---|---|---|

Limitation labels, used exactly: **Met literally**; **Met under DOE only**; **Not met**; **Not determinable on current evidence**.

For each "Met under DOE only," add the bars check:

| Limitation | Vitiation | Amendment or argument in record (paper, page) | Festo presumption and rebuttal | Disclosed but unclaimed? | Result |
|---|---|---|---|---|---|

For each method claim, and each system claim with components held by different parties:

| Step or component | Who performs or controls it | Where | Evidence | Attributable to accused party? Basis (agency, contract, conditions benefit and sets manner or timing, joint enterprise) |
|---|---|---|---|---|

## Part 6. Infringement theories: actor, place and knowledge

| Theory | Accused party | Direct infringer relied on | Place of acts | Knowledge of patent: date and evidence | Knowledge of infringement: date and evidence | Assessment |
|---|---|---|---|---|---|---|
| 271(a) direct | | n/a | | n/a | n/a | |
| 271(b) inducement | | | | | | |
| 271(c) contributory | | | | | | |
| 271(f)(1) or (2) | | | | | | |
| 271(g) | | | | | | |

## Part 7. Remedy windows and willfulness facts

- Damages window: earliest date (latest of issue date, 286 lookback date from the planned or actual filing date, notice date if 287 limits) and latest date (expiration or present), each with trigger and evidence.
- Marking: patented articles sold by patentee or licensees, marking method and dates, notice letters and whether each identifies a specific product.
- Willfulness facts: knowledge date, copying evidence, design-around efforts, good-faith positions. Facts only; no damages amount.

## Part 8. Blocking issues and reconciliation table

| # | Severity | Issue | Why it matters to the claim positions | Source | Recommendation | Owner |
|---|---|---|---|---|---|---|

Severity: Critical (claim text in force unconfirmed; asserted claim canceled or patent expired for the period analyzed; limitation charted only from marketing; construction dispute that flips a claim; no attributable direct infringer for an indirect theory); High (version of accused product unconfirmed; knowledge date unproven; file history incomplete); Medium; Low.

| Item | Value used | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Earliest U.S. filing date referenced | | patent face | file history | | |
| Claim text in force | | patent | certificate | | |
| Accused feature for each disputed limitation | | technical document | marketing or admission | | |
| Date of knowledge | | letter | testimony | | |
| Date of first accused sale or use in the U.S. | | | | | |

## Part 9. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| expert-report-on-damages | Any damages amount, royalty rate or lost profits question | Claims with infringement position supported, accused versions, damages window and triggers, marking and notice findings, knowledge date, place of acts, licenses in the record |
| claim-construction-chart | Counsel needs a joint claim construction chart for a Markman submission | Construction table, intrinsic citations, opposing constructions |
| answer-with-invalidity-contentions | The client is a defendant needing invalidity contentions or validity defenses in its answer | Construction table, IPR register and estoppel notes, prior art in the record |
| notice-of-prior-art | Prior art should be disclosed or an IPR petition prepared | Asserted claims, constructions, references found, 315(b) bar date |
| patent-infringement-complaint | The patent owner decides to sue | Claims with infringement position supported, charts, knowledge and marking facts |
| preservation-letter | Evidence of the accused product or of knowledge must be preserved | Custodians, products, versions, date ranges |
| ip-infringement-analysis | The question involves trademark, copyright or trade secret claims | Facts and documents for the non-patent claim |
| legal-research | Design, plant or foreign patents, or a forum rule not in the register; no dedicated skill exists | Question, forum, documents |

**Open items**, each with owner and next action:

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Blocks a claim position? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft infringement analysis for attorney review. Not an opinion of counsel. Not to be relied on or sent outside the privileged group until counsel confirms the claim text in force, the constructions and the accused-product evidence."
