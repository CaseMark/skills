# Output Template

Produce the header and the six parts in this order. Keep sentences plain; put detail in tables. Every date shows its weekday; every deadline shows a time and time zone.

## Contents

1. Header and source-review register
2. Part 1. Demand readiness determination
3. Part 2. Blocking issues and judgment calls
4. Part 3. Reconciliation table
5. Part 4. Draft demand letter
6. Part 5. Exhibit index and delivery log
7. Part 6. Hand-offs, open items and `[VERIFY]` list

## Header

- Matter, claimant(s), insured(s), insurer(s), claim number, date of loss, today's date, preparer note: "Draft for attorney review."
- Classification: third-party failure-to-settle or first-party, with one sentence of reasons.
- Governing law: the state, the statute or common-law rule applied, and whether the statute's current text was re-read on today's date.
- **Source-review register**, one row per file in the matter:

| File | Type | Date | Status | Pages read | Note |
|---|---|---|---|---|---|
| name as received | declarations page, disclosure, crash report, records, bills, lien notice, plan document, prior correspondence, authority letter | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Demand readiness determination

One of these labels, used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The draft letter is still included unless a hard stop in SKILL.md applies; it may not be sent until each Critical item is closed.
- **Declined: hard stop**: a hard stop applies. No letter of the kind requested; give the reason, the request or memo the hard stop calls for, and the compliant alternative.

Then:

1. **Statutory checklist** for the governing statute, one row per required term: term, where it appears in the draft (paragraph), status (met / missing / not applicable), source. If no statute applies, say so and list the common-law elements instead (for Texas, the three Garcia elements).
2. **Deadline computation** in the fixed format of `references/governing-law-and-statutes.md`, section 6.
3. **Insured-and-limits matrix**, **lien matrix** and **claimant matrix** from `references/liens-and-multiple-claimants.md`.

## Part 2. Blocking issues and judgment calls

| # | Severity | Issue | Why it matters to the bad faith record | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: Critical (no documented authority for release scope, lien approach or payee, which blocks sending; limits unconfirmed; demand below a statutory floor or missing a statutory term; per-occurrence demand for one claimant; competing claims that exceed the occurrence limit; asserted liens that approach or exceed the offer; first-party matter framed as failure-to-settle; condition the insurer cannot perform; narrower release without documented release-scope authority); High (source conflict on a figure the offer depends on; competing claimants not quantified; lien amount unknown); Medium (exhibit gaps that do not affect a statutory term); Low (clean-up). Every row ends in a recommendation and what changes under the alternative.

Judgment calls (a narrower release than all insureds, which needs documented release-scope authority given after the memo explains the exposure, multi-claimant approach, window length beyond the floor, lien payee lines) each state the options, the recommended choice and the reason.

## Part 3. Reconciliation table

Every figure and identifier in the letter traces to a source. Where two sources disagree, show both and the one used.

| Item | Value in letter | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Per-person limit | | declarations page | adjuster letter | | |
| Claim number | | | | | |
| Date and location of loss | | | | | |
| Medical specials (billed / paid) | | bills, Ex. | ledger, Ex. | | |
| Each lien amount | | | | | |
| Names of all insureds released | | | | | |
| Insurer's designated demand address | | | | | |

## Part 4. Draft demand letter

```text
[Date]

Via [method required by the governing statute, return receipt requested where required]
[Adjuster or designated address], [Insurer]
Re: [Claimant] / [Insured(s)]   Claim No. [ ]   Policy No. [ ]   Date of loss [ ]   Location [ ]

[Statutory label or reference, for example "Time-Limited Demand under [statute]"]

1. Offer. [Claimant] offers to settle all claims against [every insured released] arising from the
   [date] [occurrence] for [amount], which is within the [per-person] limit of [ ].
2. Release. [Full / limited] release of [named insureds] for [claims]. Reserved: [claims or parties, if any].
3. Liens. [Claimant] will satisfy all valid liens from the settlement proceeds, including [list].
   At [Insurer]'s option, [Insurer] may pay [lien amount] directly to [lienholder] or into
   [escrow], to be paid before the release is delivered; using this option is not a counteroffer.
4. Acceptance. Written acceptance of these terms in their entirety, delivered to [address] or
   [email or fax], no later than [date] ([weekday]) at [time] [time zone].
5. Payment. [Amount] payable to [payee] by [method] no later than [date, consistent with any statutory payment floor].
6. Liability. [Four to eight evidence-cited sentences with exhibit references.]
7. Injuries and damages. [Known injuries; specials with totals; future care; exhibit references.]
8. Records enclosed. [Records, provider list and authorizations required by the statute.]
9. Request to the insurer. Please provide a copy of this demand to your insured(s) [and any excess carrier].
10. Expiration. If not accepted as stated by the deadline, this offer is withdrawn.

Exhibit index: [see Part 5]
```

The letter states facts and terms. It does not threaten, does not predict a bad faith verdict, and does not contact a represented insured directly.

## Part 5. Exhibit index and delivery log

| Exhibit | Description | Pages | Supports paragraph |
|---|---|---|---|

| Recipient | Address used (source) | Method | Sent | Received (evidence) | Deadline recomputed from actual receipt? |
|---|---|---|---|---|---|

## Part 6. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| demand-letter | No insurer policy-limits demand is appropriate (uninsured defendant, non-insurance claim, general pre-suit demand) | Parties, claims, damages, exhibits, deadline rationale |
| coverage-opinion | A liability coverage question (duty to defend or indemnify, coverage defense, reservation of rights) drives the outcome | Policy, endorsements, the insurer's stated position, the claim facts |
| legal-research | A first-party coverage question (property, UM/UIM) drives the outcome; no dedicated skill exists | Policy, endorsements, the insurer's stated position, the claim facts, the governing state |
| lien-resolution-summary | After acceptance, or when lien amounts are unknown | Lien matrix, payer contacts, dates of conditional payment letters |
| release-of-claims | The insurer accepts and asks for the release document | Release scope, insureds, reserved claims, lien clause |
| settlement-distribution | Funds are received | Gross amount, liens, fees and costs per engagement |

**Open items**, each with owner and next action:

| # | Open item | Depends on | Owner | Next action | Blocks sending? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Not to be sent until counsel confirms the governing statute's current text, the limits, and the client's authority."
