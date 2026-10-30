# Output Template

Produce the header and the six parts in this order. Plain sentences; detail in tables. Every date shows its weekday.

## Contents

1. Header and source-review register
2. Part 1. Readiness determination, burden matrix and clocks
3. Part 2. Blocking issues and judgment calls
4. Part 3. Reconciliation table (fact to record)
5. Part 4. Draft brief
6. Part 5. Statement of facts or responsive statement, objections, Rule 56(d) declaration
7. Part 6. Hand-offs, open items and `[VERIFY]` list

## Header

- Court and case number; judge; parties; which party moves; whether the paper is a motion, an opposition, a reply or a cross-motion; claims and defenses at issue; today's date; preparer note: "Draft for attorney review."
- Governing procedure: Rule 56 or the state rule; local rule; scheduling order; judge's individual practices; whether each was read in current text on today's date.
- **Source-review register**, one row per file in the matter:

| File | Type | Date | Status | Pages read | Note |
|---|---|---|---|---|---|
| name as received | transcript, declaration, exhibit, discovery response, pleading, scheduling order, local rule, prior brief | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Readiness determination

One of these labels, used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft is still included unless a hard stop in SKILL.md applies; it may not be filed until each Critical item is closed.
- **Declined: hard stop**: a hard stop applies to the requested paper. Give the reason, the memo or request the hard stop calls for, and the compliant alternative.

Then:

1. **Burden matrix**, one row per claim, defense and element:

| Claim or defense | Element | Who bears the trial burden (source) | Evidentiary standard | Movant's route (negate / point out / establish) | Key record cites | Genuine dispute? |
|---|---|---|---|---|---|---|

2. **Clocks**, each element from its own trigger:

| Timed element | Trigger event and date | Rule or order | Period | Deadline (date, weekday) | Status |
|---|---|---|---|---|---|

3. **Discovery status**: what is outstanding, when it is scheduled, and whether a Rule 56(d) or equivalent declaration is needed.

## Part 2. Blocking issues and judgment calls

| # | Severity | Issue | Why it matters to the ruling | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: Critical (deadline missed or infeasible without a court order; movant with the trial burden relying only on the other side's lack of evidence; a material fact with no record cite; a statement-of-facts response missing or unsupported; relief sought that the rule does not allow, such as California summary adjudication that disposes of less than a cause of action; local rule or individual practices not read; client authority to concede a fact missing); High (admissibility objection likely to exclude a key exhibit; source conflict on a material figure; discovery outstanding on a contested element); Medium (format, length, citation form); Low (clean-up). Every row ends in a recommendation and what changes under the alternative.

Judgment calls (which grounds to lead with; whether to seek partial relief or a Rule 56(g) order in the alternative; whether to concede a fact for purposes of the motion only; whether to file a cross-motion; whether to move to strike or object in the papers) state the options, the recommendation and the reason.

## Part 3. Reconciliation table

Every fact in the brief traces to a numbered statement paragraph and a pinpoint in the record.

| Fact as stated in brief | Statement ¶ | Record pinpoint | Admissible form (witness, foundation, exception) | Contrary evidence (pinpoint) | Conflict? | Treatment |
|---|---|---|---|---|---|---|

Figures (damages, balances, dates) appear once per source with both values when sources differ, and the value used and why.

## Part 4. Draft brief

```text
[Caption per local rule]
[MEMORANDUM OF LAW / POINTS AND AUTHORITIES] IN [SUPPORT OF / OPPOSITION TO] [PARTY]'S MOTION FOR
[SUMMARY JUDGMENT / PARTIAL SUMMARY JUDGMENT / SUMMARY ADJUDICATION]

PRELIMINARY STATEMENT
  Who moves, on which claims or defenses (each identified, Rule 56(a)), and the one-paragraph reason.

STATEMENT OF FACTS
  Each fact with the statement paragraph and the record pinpoint, e.g. (SUF ¶ 7; Lee Dep. 45:12-46:3).
  No argument; no fact absent from the statement.

LEGAL STANDARD
  Rule 56(a) or the state rule; burden allocation for this motion (from the burden matrix);
  the evidentiary standard if heightened; cited only from references/primary-sources.md.

ARGUMENT
  I. [Claim or defense] fails / is established because [element]
     A. Governing rule (substantive law, cited or [VERIFY])
     B. Record application, fact by fact, with statement paragraphs
     C. The opponent's best evidence, credited, and why the element still fails (movant),
        or why it creates a genuine dispute (nonmovant)
  II. [Next ground]
  [Opposition only] Rule 56(d): the facts unavailable, by reference to the declaration.
  [Alternative] Partial relief or a Rule 56(g) order identifying established facts.

CONCLUSION AND RELIEF
  Exact relief: which claims or defenses, against or for which parties; judgment or order sought.

[Signature block; certificate of compliance with word or page limits where required; certificate of service]
```

The brief does not ask the court to weigh credibility, does not cite a fact missing from the statement, and does not cite authority absent from `references/primary-sources.md` without `[VERIFY]`.

## Part 5. Statement of facts or responsive statement, objections, Rule 56(d) declaration

1. **Statement of undisputed material facts** (movant): numbered, one fact per paragraph, each with a pinpoint, in the forum's format (two-column in California).
2. **Responsive statement** (nonmovant): every movant paragraph reproduced where the rule requires, with a response from the vocabulary in `references/state-and-local-practice.md`, then additional material facts.
3. **Evidentiary objections**: paragraph, material, ground (hearsay, foundation, personal knowledge, authentication), the admissible form the proponent would need, and where the objection appears in the papers.
4. **Rule 56(d) declaration outline** (when needed): facts sought and how; how they would create a genuine dispute on which element; efforts made with dates; why unsuccessful; the order requested (defer, deny, or allow time).

## Part 6. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| summary-judgment-motion | A personal injury motion package is wanted rather than a commercial brief | Claims, elements, record cites, deadlines |
| motion-to-compel | The 56(d) discovery is being withheld | Requests, responses, deficiency dates, the element each request bears on |
| deposition-summary-page-line | Transcripts lack page:line summaries for pinpoints | Transcript files, issues and elements to index |
| deposition-errata-sheet | A witness's testimony needs correction within the Rule 30(e) window | Transcript, pages, proposed changes and reasons |
| court-document-formatting | Caption, limits and certificates must match the court | Court, judge, document type, word count |
| summary-judgment | A ruling has issued and must be summarized | The order, the motion, the ruling by claim |

**Open items**, each with owner and next action:

| # | Open item | Depends on | Owner | Next action | Blocks filing? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Not to be filed until counsel confirms the governing rules and deadlines, every record citation, and the client's authority for any concession."
