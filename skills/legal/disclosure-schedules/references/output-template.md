# Output Template

Produce the header and the six parts in this order. Keep sentences plain; put detail in tables. Every schedule reference uses the numbering of the newest agreement draft, with the draft identified in the header.

## Contents

1. Header and source-review register
2. Part 1. Schedule readiness determination
3. Part 2. Blocking issues and judgment calls
4. Part 3. Rep-to-schedule map
5. Part 4. Draft disclosure schedules (or review markup)
6. Part 5. Reconciliation table
7. Part 6. Hand-offs, open items and `[VERIFY]` list

## Header

- Deal, structure (merger, stock purchase, asset purchase), parties, side represented (seller drafting or buyer review), governing law, agreement draft number and date, today's date, preparer note: "Draft for attorney review."
- **Source-review register**, one row per file:

| File | Type | Date | Status | Pages read | Note |
|---|---|---|---|---|---|
| name as received | agreement draft, prior schedule draft, contract, litigation file, cap table, data room index, diligence report, client email | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Schedule readiness determination

One of these labels, used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft schedules are still included unless a hard stop in SKILL.md applies.
- **Declined: hard stop**: a hard stop applies. Give the reason, what the hard stop calls for, and the alternative offered.

Then one paragraph: what the schedules cover, what they do not, and the top three risks.

## Part 2. Blocking issues and judgment calls

| # | Severity | Issue | Rep and schedule affected | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity:

- **Critical**: schedule numbering that does not match the newest draft; a rep the seller needs to qualify that has no lead-in (agreement change needed); a list or exception rep whose population has not been reviewed against source documents; a known exception not disclosed or described without its substance; general data room incorporation; an admission of liability or privileged content in a disclosure; a supplement treated as curing a breach without agreement text; a buyer closing over a seller-disclosed breach without a reservation of rights or amendment where the governing law makes that a waiver.
- **High**: cross-reference relied on without express reference; knowledge or materiality qualifier added in the schedule; inconsistency with the cap table, data room index or diligence report; public-company carve-out window or exclusions misapplied.
- **Medium**: description complete but imprecise (date, parties or amendment missing); confidentiality restriction on a contract not addressed.
- **Low**: formatting, defined-term clean-up.

Every row ends in a recommendation and what changes under the alternative. Judgment calls (scheduling below-threshold items, accepting a narrower cross-reference clause, closing over a supplement) state the options, the recommendation and the reason.

## Part 3. Rep-to-schedule map

| Agreement section (draft [n]) | Rep subject | Rep type (list / exception / both) | Lead-in present? (section / article / none) | Qualifiers (knowledge, materiality, threshold, lookback) | Entity scope | Schedule number | Prior schedule number (if renumbered) | Cross-references |
|---|---|---|---|---|---|---|---|---|

Below the map, show each threshold computation: item, stated amount and period, annualized amount, threshold, in or out.

## Part 4. Draft disclosure schedules (or review markup)

```text
DISCLOSURE SCHEDULES
to the [Agreement] dated [ ] among [ ]

General terms
1. Section references are to the Agreement. Each disclosure qualifies the correspondingly numbered
   Section and any other Section to which it is expressly cross-referenced [and, to the extent the
   Agreement so provides, any other Section to which its relevance is reasonably apparent on its face].
2. Inclusion of an item is not an admission of liability, of breach, or that the item is material or
   outside the ordinary course of business.
3. These schedules do not expand any representation, warranty or covenant.
4. Descriptions of documents are qualified by the documents, each of which has been made available
   to Buyer as identified below.
5. Headings are for convenience only.

Schedule [3.10] - Litigation
1. [Caption], [court], [docket no.], filed [date]. [Plaintiff] alleges [claims as pleaded]. Relief
   sought: [as pleaded]. Status: [ ]. See also Schedule [3.17(a)].

Schedule [3.13(a)] - Material Contracts
1. [Title] dated [ ] between [Company entity] and [counterparty], as amended by [ ]. [Annual amount and
   basis.] [Exception, if any: consent right / termination right / default, with section reference.]
```

For buyer review, give the seller's text, the proposed change, and the reason, item by item.

## Part 5. Reconciliation table

| Item | Value in schedule | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Agreement draft and section number | | latest draft | prior schedule draft | | |
| Contract date, parties, amount | | executed contract | data room index | | |
| Litigation caption and status | | pleading or charge | litigation log | | |
| Share and option counts | | stock ledger | cap table | | |
| Diligence report finding | | report | schedule entry | | |

## Part 6. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| merger-agreement | A rep needs a lead-in, a qualifier change, a materiality scrape, a sandbagging or anti-sandbagging clause drafted, a supplement-cure rule or a special indemnity (supplement classification and buyer knowledge at closing stay in this skill) | Section numbers, current text, proposed text, reason |
| due-diligence-report | A diligence finding has no matching disclosure, or a disclosure has no diligence support | Finding, schedule entry, source documents |
| hsr-filing | Item 3(b) transaction documents for an HSR filing may include the agreement and its schedules | Schedule list, governmental consents and approvals schedule, confidentiality notes |
| analyzing-m-and-a-tax-implications | Tax representations, tax indemnity, and tax audits and elections disclosed in schedules | Tax schedule entries and source returns |
| ma-closing-checklist | Supplements, consents and reservation letters must be tracked to closing | Item, trigger date, owner, deadline |

**Open items**, each with owner and next action:

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Blocks delivery? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Not to be delivered until counsel confirms the agreement draft, the cross-reference clause and each disclosure against its source document."
