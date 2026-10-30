# Output Template

Produce the header and the six parts in this order. Plain sentences, detail in tables. Every figure carries its unit (dollars, thousands, millions), its period and its source locator.

## Contents

1. Header and source-review register
2. Part 1. Report readiness determination
3. Part 2. Blocking issues and judgment calls
4. Part 3. Reconciliation table, tie-outs and overlap matrix
5. Part 4. Draft expert report
6. Part 5. Schedules, exhibits and materials considered
7. Part 6. Hand-offs, open items and `[VERIFY]` list

## Header

- Matter, court and case number, retaining party, testifying expert (name, or "not yet identified"), plaintiff entity whose losses are measured, claims and measures counsel has identified, today's date, report due date (and its source: scheduling order, stipulation or Rule 26(a)(2)(D) default), preparer note: "Draft for review by the testifying expert and counsel."
- Governing rules: forum (federal or state), disclosure rule applied, admissibility standard applied, and whether each was confirmed for this forum on today's date.
- **Source-review register**, one row per file:

| File | Type | Date | Status | Pages or tabs read | Note |
|---|---|---|---|---|---|
| name as received | pleading, contract, financial statements, general ledger, tax return, projection, budget, interview notes, deposition, opposing report, data extract | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Report readiness determination

One of these labels, used exactly:

- **Ready for expert review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft is still included unless a hard stop in SKILL.md applies; it may not be signed or served until each Critical item is closed.
- **Declined: hard stop**: a hard stop applies. No draft of the kind requested; give the reason, the request list or compliant alternative the hard stop calls for, and what can proceed.

Then:

1. **Rule 26(a)(2)(B) checklist**: one row per element (i) to (vi), with the report section, status (complete / incomplete / not applicable), and the gap.
2. **Admissibility checklist**: one row per FRE 702 element (a) to (d) for each opinion, with where the report shows it and the weakest point.
3. **Measure summary**: claim, measure, period, valuation date, and the instruction or authority for each.

## Part 2. Blocking issues and judgment calls

| # | Severity | Issue | Why it matters (disclosure, admissibility or amount) | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: Critical (a projection relied on without tests; overlapping categories added together; but-for and actual periods or entities that do not match; Rule 26(a)(2)(B) element missing, including the testimony list, publications or compensation; a counsel-provided assumption not identified as such; facts or data considered not listed; prejudgment interest or a legal entitlement stated as an expert opinion; interest on future losses; contingent compensation; causation not isolated from obvious other causes; valuation date or choice between overlapping frameworks not yet instructed by counsel where the total depends on it); High (unsupported discount rate or risk counted twice; avoided costs not analyzed; mitigation evidence not quantified; data not validated); Medium (presentation gaps that do not affect an opinion); Low (clean-up). Every row ends in a recommendation and what changes under the alternative.

Judgment calls (valuation date, lost-volume treatment of replacement business, choice between alternative measures, discount rate within a supported range, treatment of contested facts) each state the options, the figure under each, the recommended choice and the reason, and whether the choice belongs to the expert or to counsel.

## Part 3. Reconciliation table, tie-outs and overlap matrix

Every figure in the report traces to a source. Where two sources disagree, show both and the one used.

| Item | Value used | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Historical revenue by period | | audited statements | general ledger or tax return | | |
| Incremental margin and each avoided cost | | | | | |
| But-for revenue by period | | method and inputs | | | |
| Actual revenue by period | | | | | |
| Mitigation revenue and margin | | | | | |
| Discount rate and components | | | | | |
| Valuation date | | counsel instruction | | | |

**Tie-outs** (each must hold, or the difference is explained): historical revenue ties to audited or filed statements; but-for minus actual equals lost revenue in every period; each category total ties to its schedule; the report total equals the sum of the non-overlapping categories; the totals reconcile to the Rule 26(a)(1)(A)(iii) computation or the change is explained.

**Overlap matrix**: categories on both axes; each cell "no overlap", "overlap: amount and period", or "alternative measures". No total includes two categories that measure the same dollars for the same period.

**Period alignment table**: for each category, but-for start and end, actual start and end, entity, accounting basis.

## Part 4. Draft expert report

```text
EXPERT REPORT OF [NAME], [CREDENTIALS]
[Case caption]   Prepared for: [retaining party / counsel]   Date: [ ]   DRAFT

1. Assignment and summary of opinions
   Questions counsel asked me to address; each opinion in one sentence with its figure or range.
2. Qualifications                                  [Rule 26(a)(2)(B)(iv); CV at Appendix A]
   Publications in the previous 10 years: Appendix A.
3. Prior testimony                                 [Rule 26(a)(2)(B)(v); Appendix B]
   Every case in the previous 4 years with trial or deposition testimony.
4. Compensation                                    [Rule 26(a)(2)(B)(vi)]
   Hourly rates for the expert and staff; compensation is not contingent on the opinions or outcome.
5. Facts or data considered                        [Rule 26(a)(2)(B)(ii); Appendix C]
   Including interviews, materials reviewed and not used, and data or assumptions provided by counsel.
6. Background
   Parties, the plaintiff entity, business, relationship, the alleged act, dates.
7. Assumptions
   Each assumption, its source (counsel-provided, management-provided, or the expert's own),
   its basis, and the effect if it is wrong.
8. Damages framework
   Measure for each claim as instructed by counsel; but-for and actual worlds; periods;
   valuation date; why each method fits; standards followed.
9. Analysis and calculations                       [Rule 26(a)(2)(B)(i), (iii); Schedules 1-n]
   By category: method, inputs with sources, steps, result. Projection tests. Avoided costs.
   Causation and other causes. Mitigation. Discounting. Overlap removal.
10. Sensitivity and alternative scenarios
   Inputs varied, supported ranges, results; contested facts shown under each version.
11. Opinions
   Each opinion, its basis and reasons, stated no more broadly than the analysis supports.
   Damages before interest. Interest, if counsel instructs, in a separate labeled schedule.
12. Limitations and right to supplement
   Data not yet produced; how the opinion would change; supplementation under Rule 26(e).
Signature: [prepared and signed by the witness after review]
```

## Part 5. Schedules, exhibits and materials considered

| Schedule | Content | Inputs (sources) | Ties to |
|---|---|---|---|

| Materials considered | Type | Bates or locator | Relied on? | If not relied on, why |
|---|---|---|---|---|

## Part 6. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| expert-witness-designation | Serving the Rule 26(a)(2) disclosure | Expert identity, subject matter, opinions summary, report date, compensation |
| expert-witness-report-analysis | Critiquing the opposing damages report or preparing rebuttal points | Opposing report, its schedules, the overlap and period tables from this draft |
| expert-deposition | Preparing the expert to testify or to depose the opposing expert | Opinions, assumptions by source, sensitivity table, weakest points |
| motion-in-limine | Moving to exclude or defending a Rule 702 challenge | Admissibility checklist, authorities from the primary sources register |
| economic-loss-report | Personal injury wage-loss and earning-capacity reports | Earnings history, worklife inputs, discount rate basis |
| expert-report-class-damages | Class-wide damages or a Rule 23 damages model | Liability theory, class definition, data available |
| patent-infringement-analysis | Patent liability, claim scope or noninfringing alternatives drive the royalty | Accused products, licenses, design-around evidence |
| forensic-accounting-report | Tracing, fraud or accounting irregularities underlie the claim | Ledger issues found, transactions to trace |

**Open items**, each with owner and next action:

| # | Open item | Depends on | Owner | Next action | Blocks signing or service? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for review by the testifying expert and counsel. The opinions become the expert's only after the expert has performed or directed the analysis, reviewed every figure, and adopted the report. Not to be signed or served until the Critical items are closed."
