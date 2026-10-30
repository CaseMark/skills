# Output Template

Produce the header and the seven parts in this order. Plain sentences; detail in tables. Every date shows its weekday where a clock runs from it.

## Contents

1. Header and source-review register
2. Part 1. Determination
3. Part 2. Blocking issues and judgment calls
4. Part 3. Term sheet reconciliation and defined-term map
5. Part 4. Price waterfall tie-out
6. Part 5. Draft agreement or markup
7. Part 6. Clocks and closing deliverables
8. Part 7. Hand-offs, open items and `[VERIFY]` list

## Header

- Matter; parties; side represented (buyer, target, seller stockholders, other); public or private target; structure (forward, reverse triangular, 251(h) two-step); state of incorporation of each constituent; governing law of the agreement; today's date; deliverable mode (new draft, or review of a counterparty draft); preparer note: "Draft for attorney review."
- **Source-review register**, one row per file:

| File | Type | Date | Status | Sections read | Note |
|---|---|---|---|---|---|
| name as received | term sheet or LOI, counterparty draft, charter, bylaws, cap table or stock ledger, QoE report, diligence memo, disclosure schedule draft, RWI binder, commitment letters, client email | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Determination

One label, used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft or markup is still included unless a hard stop applies.
- **Declined: hard stop**: a hard stop in SKILL.md applies to the request or to a requested provision. Give the reason, what is produced instead (issues list, term sheet questions, compliant alternative provision) and what would lift the stop.

Then one paragraph: what the agreement does for the represented side, the three provisions that most affect closing certainty and value, and what must happen before signing.

## Part 2. Blocking issues and judgment calls

| # | Severity | Provision (section) | Issue | Effect on the represented side | Source | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Severity:
- **Critical**: a walk right, MAE, bring-down or termination term that shifts closing risk against the client without the client's documented decision; a price waterfall that does not tie or counts an item twice; an interim covenant that transfers operational control or competitively sensitive information before regulatory clearance; a provision void or unenforceable under the statute as drafted (for example, uncapped and indefinite indemnity of non-signing stockholders); a known diligence finding with no recovery path; a stockholder approval or appraisal step that misstates the statute.
- **High**: a source conflict on a figure or defined term the price or a condition depends on; a definition whose use in another section changes its effect; a policy election with no client instruction.
- **Medium**: drafting that is unclear but not outcome-changing; cross-reference errors.
- **Low**: clean-up.

Every row ends in a recommendation and what changes under the alternative. Judgment calls (bring-down standard, sandbagging position, basket type, emergency exception, appraisal condition, regulatory efforts ceiling) each give the options, the recommended choice for the represented side and the reason.

## Part 3. Term sheet reconciliation and defined-term map

**Reconciliation.** Every economic and risk term in the draft traces to its source; conflicts are shown, not resolved silently.

| Term | Draft (section) | Term sheet or LOI (locator) | Other source (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Base price and form of consideration | | | | | |
| Working capital target and basis | | | QoE page | | |
| Indebtedness items | | | | | |
| Escrow and holdback amounts | | | | | |
| Cap, basket, survival | | | | | |
| Termination and reverse termination fees | | | | | |
| Outside date and extensions | | | | | |

**Defined-term map.** One row per high-risk term (MAE, Knowledge, Indebtedness, Transaction Expenses, Closing Working Capital, Fundamental Representations, Willful Breach, Fraud):

| Term | Definition (section) | Used in (sections) | Effect at each use | Problem found |
|---|---|---|---|---|

## Part 4. Price waterfall tie-out

Show the computation with each figure sourced, then the check that every balance sheet item appears in exactly one line.

```
Base Purchase Price                         [amount]   [source]
- Closing Indebtedness                      [amount]   [items listed]
+ Closing Cash (if applicable)              [amount]
+/- (Closing Working Capital - Target)      [amount]   [basis of each]
- Unpaid Transaction Expenses               [amount]
= Closing Merger Consideration              [amount]
Per-share or per-unit allocation           [waterfall by class, from the cap table]
```

| Balance sheet item | In Indebtedness? | In working capital (peg)? | In working capital (closing)? | In Transaction Expenses? | Counted once? |
|---|---|---|---|---|---|

## Part 5. Draft agreement or markup

Article skeleton for a new draft: Definitions; The Merger (effective time, charter and bylaws, directors and officers); Conversion of Securities and Payment (exchange agent, equity awards, appraisal shares, withholding, adjustment); Representations of the Company; Representations of Parent and Merger Sub; Covenants (conduct of business, access, no-shop or go-shop, stockholder approval, regulatory efforts, financing, employee matters, D&O indemnification); Conditions; Termination and Fees; Indemnification (private only) or No Survival (public); Miscellaneous (specific performance, governing law and forum, non-recourse, third-party beneficiaries, schedules). Bracket every term not settled by the client and mark its gap class.

For a review: a section-by-section markup table.

| Section | Counterparty text (quoted) | Proposed change | Reason | Priority |
|---|---|---|---|---|

## Part 6. Clocks and closing deliverables

| Element | Period | Trigger event | Date (weekday) | Source |
|---|---|---|---|---|

Each element takes its own trigger (meeting date, taking of the vote, action by consent, giving of notice, effective date, receipt of the HSR filing by both agencies, signing). Closing deliverables: officer's certificate (bring-down), secretary's certificate, good standing, certificate of merger, payoff letters, invoices for Transaction Expenses, resignations, FIRPTA or W-9 forms as tax counsel directs, escrow agreement, paying agent agreement.

## Part 7. Hand-offs, open items and `[VERIFY]` list

A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| hsr-filing | Any filing may be required, or interim covenants, access or integration planning touch the target's operations before closing | Parties, values, structure, interim covenant text, access and clean-team terms, outside date |
| disclosure-schedules | Representations are final enough to schedule against, or a schedule exception drives a representation change | Representation list with section numbers, qualifiers, cross-application standard, known exceptions from diligence |
| due-diligence-report | A representation, special indemnity or condition depends on a diligence fact not yet confirmed | The provision, the fact needed, the data room locator if any |
| analyzing-m-and-a-tax-implications | Structure choice, intended tax treatment, tax representations, tax indemnity, allocation, withholding | Structure, consideration mix, entity classifications, intended treatment as instructed |
| escrow-agreement; voting-agreement; proxy-statement; ma-closing-checklist | Ancillary documents or closing logistics | Escrow amounts and release mechanics; support agreement terms; meeting timetable; deliverables list |

**Open items**, each with owner and next action:

| # | Open item | Gap class | Depends on | Owner | Next action | Blocks signing? |
|---|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Not for signature until counsel confirms the open items, the current statutory text, and the client's decisions on each judgment call."
