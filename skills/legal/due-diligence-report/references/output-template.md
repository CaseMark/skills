# Output Template

## Contents

1. Header and source-review register
2. Part 1. Determination and executive summary
3. Part 2. Findings matrix
4. Part 3. Area analyses
5. Part 4. Consents, notices and closing deliverables
6. Part 5. Reconciliation table
7. Part 6. Open items and supplemental requests
8. Part 7. Hand-offs and `[VERIFY]` list

Produce the header and the seven parts in this order. Use plain sentences and put detail in tables. A red-flag report keeps Parts 1, 2, 4, 6 and 7 and shortens Part 3 to Critical and Significant items; a full-form report keeps every part.

## Header

- Transaction, structure (stock purchase, reverse triangular merger, forward merger, asset purchase, minority investment, financing), client and client's side, target entities in the perimeter, report type (red-flag or full-form), today's date, data room cut-off date, preparer note: "Draft for attorney review. Privileged and confidential; prepared at the direction of counsel."
- Materiality threshold applied, who set it, and the aggregation rule applied.
- Report version: general, or clean-team only.
- **Source-review register**, one row per data room folder or document reviewed:

| Index no. | File | Counterparty or subject | Executed? | Status | Pages read | Method or note |
|---|---|---|---|---|---|---|
| | name as indexed | | executed / draft / form / summary | Reviewed / Reviewed: summary only (not relied on) / Unreadable after attempt / Not located after index and Q&A check / Not relevant / Withheld: privilege or clean team | | OCR tried; Q&A reference; who supplies |

## Part 1. Determination and executive summary

One determination label, used exactly:

- **Complete for attorney review**: every in-scope document is Reviewed or classified, and no source-review gap remains on a Critical or Significant finding.
- **Issued subject to listed open items**: findings are drafted, and each open item that could change a rating is listed in Part 6.
- **Scope-limited: index or summary review only**: findings rest on an index, a seller summary or management statements rather than executed documents. Every finding carries that limit.
- **Declined: hard stop**: a hard stop in SKILL.md applies. Give the reason and the alternative offered; no report of the kind requested.

Then: Critical findings (issue, impact, required action); Significant findings (issue, impact, proposed protection); required consents and approvals (third-party, regulatory, HSR or other antitrust, CFIUS or industry regulators, with each marked for confirmation); top open items.

## Part 2. Findings matrix

| # | Area | Finding | Source (index no., document, section, page, date) | Rating | Gap class (if open) | Exposure or impact as the source states it | Recommendation | Proposed deal protection |
|---|---|---|---|---|---|---|---|---|

Ratings, used exactly: **Critical** (likely deal-breaker, closing condition or price issue; resolve before signing or closing); **Significant** (material value or operations impact; address with price, special indemnity, escrow, covenant or condition); **Moderate** (manageable; covenant or post-closing plan); **Minor** (awareness only). Gap classes: unknown fact, source conflict, unverified external lookup, policy election.

## Part 3. Area analyses

One subsection per area in scope: corporate and capitalization; material contracts; restrictive covenants; litigation and claims; regulatory and permits; IP and technology (including open source); employment, benefits and WARN; real estate; environmental; privacy and cybersecurity; insurance; indebtedness and liens; tax (summary only, with the hand-off). Each subsection states what was reviewed, what was not, the findings in rating order, and open items.

## Part 4. Consents, notices and closing deliverables

| Contract or permit | Counterparty | Clause and locator | Governing law | Structure assumed | Outcome label | If structure changes | Action and timing |
|---|---|---|---|---|---|---|---|

Outcome labels, used exactly: Consent required; Notice only; Termination or other right triggered; No consent on these facts; Judgment call: governing law unsettled; Outside the deal perimeter.

Closing deliverables list: payoff letters, UCC-3 terminations, lien releases, IP assignments and recordations, consents, novation requests, WARN notices (with the date each is due and who gives it).

## Part 5. Reconciliation table

Every figure and every characterization drawn from a summary is traced to the executed source. Where two sources disagree, show both and the one used.

| Item | Summary, schedule or index says | Executed source says (locator) | Conflict? | Value used and why |
|---|---|---|---|---|
| Change-of-control term in a key contract | | | | |
| Contract term and renewal | | | | |
| Debt and liens (debt schedule vs. UCC and judgment searches) | | | | |
| Headcount, full-time and part-time, by site | | | | |
| Litigation list vs. docket search and correspondence | | | | |
| IP owner of record vs. seller's IP schedule | | | | |
| Aggregated sub-threshold contracts with the same risk term | | | | |

## Part 6. Open items and supplemental requests

| # | Open item | Gap class | Affects finding # | Request to seller (index or Q&A reference) | Owner | Needed by |
|---|---|---|---|---|---|---|

## Part 7. Hand-offs and `[VERIFY]` list

A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| disclosure-schedules | Findings that become exceptions to representations (contracts, consents, litigation, liens, IP, employees) | Finding, source locator, rating, and the representation it qualifies |
| merger-agreement | Findings that call for a special indemnity, escrow, closing condition, covenant, definition change (Indebtedness, Permitted Liens, Affiliate) or a privilege carve-out | Finding, exposure as stated, proposed protection, structure assumed |
| hsr-filing | Competitively sensitive information exchanged outside a clean team, pre-closing coordination, or a filing threshold question | What was shared, with whom, when, and the protocol in place |
| analyzing-m-and-a-tax-implications | Tax findings, structure changes that alter tax treatment, worker classification payroll tax exposure | Returns reviewed, audits, structure assumed, open tax items |
| consent-letter | Each contract labeled Consent required or Notice only | Counterparty, clause, deal description permitted to be disclosed, deadline |
| due-diligence-checklist | Supplemental request list for gaps | Open items from Part 6 |

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

## Deal protection mapping

| Risk type | Drafting lever |
|---|---|
| Known liability (litigation, WARN, misclassification) | Special indemnity; escrow; price adjustment |
| Compliance gap | Pre-closing covenant; closing condition |
| Contract consent or termination right | Closing condition for key consents; covenant to seek others; bring-down |
| IP ownership gap | Pre-closing confirmatory assignments; specific representation; holdback |
| Undisclosed lien or indebtedness | Payoff letter and release as closing deliverables; Indebtedness definition |
| Restrictive covenant binding the buyer group | Pre-closing waiver or amendment from the counterparty; closing condition |

Close with: "Draft for attorney review. Findings rest on the documents listed in the source-review register as of the data room cut-off date."
