# Form D skill hardening: change log (October 27, 2026)

Scope: `skills/legal/form-d-exempt-offering-notice`. Changes are in the working tree only. Nothing has been committed, merged or published; publication happens through the reviewed PR and the `legal-embed` workflow, and this log does not claim that any registry has been updated.

## Failure modes addressed

| # | Failure mode | Where the operative rule now lives | Cross-references |
|---|---|---|---|
| 1 | A document in the inventory is called "missing" because a search did not surface it | `references/source-reconciliation.md`, "Source-review completion gate" (inventory from the matter, open every file, four statuses, must-review categories, gate) | SKILL.md ground rule 11, Step 1, Step 3, QC gate, Troubleshooting; `output-template.md` header register |
| 2 | A field left blank or "MISSING" when the form offers a choice | `references/form-d-items.md`, "Evidence-to-field worksheet" (seven row elements; five statuses replacing MISSING: unknown fact, issuer election, not applicable, unverified external lookup, source conflict) | SKILL.md ground rule 12, Step 6, output section 3, QC gate; `output-template.md` section 3 columns; Items 1, 3, 5, 6, 7, 12, 16 reworded to use the statuses |
| 3 | Program totals carried across issuers | `references/fund-structures.md`, "Issuer-specific reconciliation before any program presentation" (per-issuer schedule, program schedule, arithmetic check, three conditions for a program total in an issuer field, worked example) | SKILL.md ground rule 13, Step 3, output section 3, QC gate; `form-d-items.md` Items 13, 14, 15; `source-reconciliation.md` reconciliation 1 and 8; `output-template.md` section 3 |
| 4 | A conflict noticed without a usable recommendation | `references/fund-structures.md`, "Required write-up for each conflict" (six ordered elements, counts under each outcome); `source-reconciliation.md` conflict write-up now requires the recommendation and the alternative | SKILL.md ground rule 14, Step 5; `output-template.md` section 2 column "Recommendation and alternatives" |
| 5 | A "Yes" on a bad actor questionnaire not reviewed | `references/source-reconciliation.md`, "Bad actor questionnaire review" (record fields; criteria walk-through under Rule 506(d)(1) and (d)(2); four characterizations; counsel decision and follow-up) | SKILL.md Step 5, Step 8, QC gate; `output-template.md` section 5 table; `primary-sources.md` rows for Rule 506(d)(1), (d)(2), (e) |
| 6 | Lookup failure treated as proof of non-existence, or a no-match softened | `references/edgar-access.md`, Step 1 rewritten (five outcomes with evidence and consequence; failed is never "not found"; no-match is never "unverified"; synthetic identifiers; prior notice unconfirmed under either outcome) | SKILL.md ground rule 2, Step 7, QC gate, Troubleshooting; `form-d-items.md` Items 1 and 12; `output-template.md` identifier lookup register |
| 7 | Issue list present but items or hand-offs incomplete | SKILL.md "Quality-Control Gate Before Responding" (thirteen confirmations); `references/output-template.md` section 5 (hand-off is complete only when the receiving workflow could start without re-reading the matter; required table columns for both hand-offs) and section 6 (open items with owner and next action) | SKILL.md Step 8, output sections 5 and 6 |

## Required changes A to H, mapped

- **A. Source-review completion gate**: `source-reconciliation.md` (gate section; must-review list; "missing" and "unavailable" are not statuses; unreadable rows carry a dependency list). Root skill Step 3 now runs the gate before reconciliation.
- **B. Evidence-to-field worksheet**: `form-d-items.md` (worksheet section). Output section 3 renamed and its columns expanded.
- **C. Issuer-specific calculations**: `fund-structures.md` (new section with schedules, arithmetic check, program-total conditions). Item 13 and Item 14 text in `form-d-items.md` now requires per-issuer computation first.
- **D. Item 11 decision framework**: `form-d-items.md` Item 11 rewritten (four questions, five readings, recommendation plus alternatives plus confirmation). `fund-structures.md` "Minimum investment waivers" reduced to a cross-reference. The earlier categorical sentence ("use the stated floor if the documents set one, and 0 if the GP's waiver discretion has no floor") is removed.
- **E. Eligibility conflicts**: `fund-structures.md` "Qualification conflicts and the required write-up". The ledger-flag rule ("never controls over an executed questionnaire") is stated there and in SKILL.md ground rule 4.
- **F. Bad actor "Yes" review**: `source-reconciliation.md` new section. Rule text for 506(d)(1)(iii), (d)(2) and (e) was re-read from the eCFR API on October 27, 2026 and the register updated. A fourth characterization, "outside the criteria on its face", was added to the three the assignment names so a reviewed benign event has a label; the assignment's three remain the flagged categories.
- **G. External lookup status**: `edgar-access.md` Step 1. The old four-bullet outcome list and the separate "failed lookup" paragraph are merged into one table.
- **H. Complete hand-off**: `output-template.md` section 5 (two tables, one per receiving skill; a sentence on what remains for the related workflow). SKILL.md Step 8 retitled "Hand off, completely".
- **Quality-control gate**: SKILL.md replaces "Quality Checks Before Responding" with the required thirteen-point gate, including the deadline-basis and settled-versus-provisional checks.

## Other changes

- SKILL.md description updated to name the gate, the worksheet, issuer-by-issuer reconciliation and precise lookup outcomes (736 characters; limit 1,024). Body is 159 lines (limit 500).
- A Troubleshooting section was added to SKILL.md (the spec checklist requires one; the skill had none).
- Contents sections added to `source-reconciliation.md`, `form-d-items.md`, `fund-structures.md` and `output-template.md`, which now exceed 100 lines.
- `amendments-and-deadlines.md` is unchanged; the deadline-basis rule already lived there and is now enforced by the QC gate.
- Judgment calls preserved: one filing versus several, Item 13 cap presentation, Regulation S treatment, Item 5 for a new fund, Item 16 presentation, Item 11 readings, entity type for non-U.S. vehicles. Each now requires a recommendation, the alternatives and what changes under each, rather than a single hard-coded answer.
- No operative rule is stated in full in more than one file; `evals/check-package.py` fails if the Item 11 framework or the lookup-outcome table is duplicated.

## Tests added

`skills/legal/form-d-exempt-offering-notice/evals/`: `evals.json` (repository eval format), `README.md`, `check-package.py` (structural check), `fixtures/` (a shared synthetic base matter and nine case files) and `expected/` (common expectations plus one Must / Must not file per test). The nine cases: overlooked questionnaire; subscription versus ledger; common program cap; waived minimum (documented floor and policy floor); investor qualification conflict; bad actor "Yes" (one with the order in the file, one without); unreadable document; affirmative EDGAR no-match; failed lookup. All identifiers are fictional; CIK 0009876543 and the issuer name were confirmed as affirmative no-matches on EDGAR on October 27, 2026 before the fixtures were written.

Test results are in `test-results-2026-10-27.md` in this directory.

## Files changed

See `git status` for the working tree: SKILL.md and six of seven references modified (`amendments-and-deadlines.md` untouched); `evals/` added; this directory added.

---

# Addendum, October 28, 2026: external run feedback folded in, with a trim pass

Source: feedback from an agent that ran the pre-revision skill on a different synthetic matter (Cascade Fund III) and missed a $12m-versus-$15m commitment mismatch that cascaded into Items 13 and 15, an agent state-registration gap, and a feeder Regulation S double count. Four of its eight suggestions were already covered by the October 27 revision (gate with artifact; Item 13 computed; Item 15 from reconciled amounts; bad actor characterization after applying the criteria). The remaining four, and two small additions, are now in the working tree.

| Suggestion | Where it landed |
|---|---|
| 1. Per-investor reconciliation artifact with ledger and delta columns | `fund-structures.md`, "Investor reconciliation table" (every investor; executed amount, ledger amount, delta, introduced by, Regulation D or S, resolution) ahead of the per-issuer schedule; `output-template.md` Section 3 opens with it; QC gate bullet "an empty or partial table means the draft is incomplete"; gate status Reviewed now says "signature page, acceptance block and questionnaire, not a sample" |
| 2. Item 13 computed, never copied | `form-d-items.md` Item 13: "never a single figure copied from a ledger, closing memo or client email"; a differing ledger total is a Section 2 conflict |
| 3. Client instruction to use a lower-ranked source is a red flag | `source-reconciliation.md`, new section "Client instructions that point at a lower-ranked source" with a worked example; SKILL.md ground rule 4 and Step 3; QC gate bullet; `output-template.md` severity High for such an instruction |
| 4. Mechanical blue-sky matrix, agent-introduced versus direct | `output-template.md` Section 5: "placement agent cross-check matrix", one row per investor, Gap only where introduced by an agent and the state is outside the exhibit; "A Direct-introduced investor creates no agent registration gap"; `source-reconciliation.md` reconciliation 4 and `form-d-items.md` Item 12 cross-reference it; QC gate bullet; Troubleshooting row |
| 5. Regulation S in both variants | `fund-structures.md` offshore feeders and per-issuer schedule: 13(b) and 14 shown as "Regulation D only" and "All sales" on adjacent rows with the recommended one marked; `form-d-items.md` Items 13 and 14; SKILL.md Step 6; QC gate |
| 6. Item 15 from reconciled amounts | `form-d-items.md` Item 15: rate times the table's executed amounts for agent-introduced investors; a ledger fee figure is a cross-check only |
| 7. Bad actor severity | `output-template.md` Section 2: Critical only for "potentially disqualifying" on the primary document; unresolved, disclosure-only and outside-the-criteria are High and routed, not concluded. The characterization step itself is kept (assignment requirement F); the feedback's "don't decide, flag" is applied to severity, not to the review |
| 8. Trap map | SKILL.md, "Where mistakes hide" table (document, what it is used for, where the error hides), replacing most of the prose in "Why This Skill Exists" |

**Trim pass.** To hold the package near its October 27 size: SKILL.md Step 4 first-sale bullets reduced to pointers at `amendments-and-deadlines.md` (which already held them); "Why This Skill Exists" cut to three sentences; ground rule 5 shortened; `source-reconciliation.md` "Unreadable documents" section merged into the gate and the hierarchy bullets tightened; `form-d-items.md` Items 1, 3 and 11 readings tightened without removing any reading; `fund-structures.md` co-issuer consequences, worked-example tail, Rule 506(b) and Investment Company Act paragraphs, and the Item 11 cross-reference tightened; `output-template.md` Section 4 list tightened. No operative rule was removed.

| Measure | Committed (d7209e1) | October 27 revision | Now |
|---|---|---|---|
| Words, SKILL.md plus references | 11,389 | 17,852 | 18,207 |
| SKILL.md body lines | 126 | 160 | 164 |

**Tests.** Test 10 `offshore-feeder-reg-s` added: a Cayman feeder with two Regulation S investors and one U.S. tax-exempt investor introduced by Brightwater (California, on Exhibit C), a register Program sheet that double counts the feeder ($131m / 9 investors), and a client email instructing that the Program sheet totals be used on both filings. `check-package.py` now also requires the trap map, the client-instruction section, the reconciliation table columns, both Regulation S variants, the matrix header (in output-template only) and the severity rule, and expects ten tests. Results are in `test-results-2026-10-27.md`, addendum.
