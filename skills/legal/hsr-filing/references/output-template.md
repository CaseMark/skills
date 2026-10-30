# Output Template

Produce the header and six parts in this order. Plain sentences; detail in tables. Every date shows its weekday; every deadline shows a time and "ET". Every annually adjusted figure shows the notice it came from and its effective date.

## Contents

1. Header and source-review register
2. Part 1. Reportability determination
3. Part 2. Blocking issues and judgment calls
4. Part 3. Reconciliation table
5. Part 4. Filing preparation workplan
6. Part 5. Waiting period, closing timeline and pre-closing conduct
7. Part 6. Hand-offs, open items and `[VERIFY]` list

## Header

- Matter, acquiring person (UPE), acquired person (UPE), transaction type (merger, stock purchase, asset purchase, non-corporate interest, joint venture formation, open-market or tender offer), signing date, expected closing date, today's date, preparer note: "Draft for attorney review."
- Thresholds used: "2026 thresholds, 91 Fed. Reg. 2133 (Jan. 16, 2026), effective February 17, 2026; re-checked on [date]". If closing may fall after the next annual adjustment, say so here.
- Form version: pre-February 10, 2025 Form or 2025 Form (client election), with the status date from `references/waiting-period-and-conduct.md`, section 1.
- **Source-review register**, one row per file:

| File | Type | Date | Status | Pages read | Note |
|---|---|---|---|---|---|
| name as received | purchase agreement, disclosure schedule, cap table, org chart, LLC or LP agreement, financial statements, board deck, banker book, CIM, integration plan, email | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Reportability determination

One label per acquisition, used exactly:

- **Filing required**: every element of the test is met and no exemption applies on the facts.
- **No filing required**: an element fails or an exemption's conditions are all confirmed; state which.
- **Undetermined: open items**: the outcome turns on a fact not yet established; name the fact, both outcomes, and who supplies it.
- **Declined: hard stop**: a hard stop in SKILL.md applies to what was requested; give the reason and the compliant alternative.

Then, in this fixed format for each acquisition:

```
Acquisition:               <what> from <acquired UPE> by <acquiring UPE>
Value held as a result:    $<amount>  = <component> + <component> + ...  (801.10 / 801.13 basis)
Size of transaction:       <in excess of / not in excess of> $133.9M (2026); <above / at or below> $535.5M (2026)
Size of person:            <not required | acquiring $<x> (source, date); acquired $<y> (source, date); met / not met>
Exemptions screened:       <rule>: <conditions met / failed and why>
Notification threshold:    <threshold> (801.1(h))   [voting securities only]
Filing fee:                $<fee> (2026 tier), payable by the acquiring person
Determination:             <label>
```

Then the **valuation worksheet** (every component with source locator, included or excluded, and the rule), the **party table** (each entity in the chain, percentage held, control test applied, UPE conclusion), and the **exemption screen** (each exemption considered, every condition, the fact that meets or fails it).

## Part 2. Blocking issues and judgment calls

| # | Severity | Issue | Why it matters | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: **Critical** (an element of reportability unresolved; a valuation component missing; UPE unknown; an exemption relied on with an unconfirmed condition; a conduct provision that transfers operational control before expiry; a filing or closing date computed from the wrong trigger); **High** (source conflict on a figure the threshold or fee depends on; Item 4(c) collection incomplete; fair market value determination missing or older than 60 days); **Medium** (form-version election open; parallel state notice not assessed); **Low** (clean-up). Each row ends with a recommendation, what changes under the alternative, and an owner.

Judgment calls (for example: which closing date governs the threshold year, election of form version, treatment of a contingent payment that cannot be reasonably estimated) each state the options, the recommended choice and the reason.

## Part 3. Reconciliation table

| Item | Value used | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Cash at closing | | purchase agreement section | funds-flow memo | | |
| Liabilities assumed | | agreement, assumed-liabilities schedule | closing balance sheet | | |
| Deferred, escrowed or contingent consideration | | | | | |
| Non-compete or other separate payments | | | | | |
| Shares or interests already held | | cap table or register | broker statement | | |
| Acquiring UPE total assets / net sales | | audited statements (date) | management accounts | | |
| Acquired UPE total assets / net sales | | | | | |
| Filing and receipt dates | | Kiteworks confirmation | email | | |

## Part 4. Filing preparation workplan

1. Filer(s), certifying individual and authority basis (803.6); affidavit type (803.5).
2. Item 3(b) transaction documents: the executed agreement or letter of intent, non-competes and other agreements between the parties (drafts only where the Instructions permit).
3. Item checklist for the form version used, each item with owner, source and status.
4. **Item 4(c)/4(d) index**:

| Doc # | Title | Date | Author | Prepared by or for (officer or director) | Item | Produced / withheld (log ref) |
|---|---|---|---|---|---|---|

5. Custodian list searched (the filing person's own officers and directors; collected by this skill), date ranges, and any custodian not yet searched.
6. Item 8 prior acquisitions (pre-February 10, 2025 form): five years, overlapping 6-digit NAICS codes, with the Instructions' size limits.
7. Fee payment: amount, payer, wire reference placeholder `[[ ]]`.
8. Parallel notices (Washington State copy; Department of War copy if applicable) as open items.

## Part 5. Waiting period, closing timeline and pre-closing conduct

1. The waiting-period computation in the fixed format of `references/waiting-period-and-conduct.md`, section 4, once per filing scenario.
2. Timeline table, each element with its own trigger event:

| Element | Trigger event | Date and time (ET) | Rule |
|---|---|---|---|
| Fair market value determination window | Filing date (or closing if no filing) | | 801.10(c)(3) |
| Acquired person's filing (801.30 deals) | Receipt of acquiring person's filing | | 801.30(b)(2) |
| Waiting period expiry | Receipt of last required filing (or acquiring filing for 801.30) | | 803.10(b) |
| Threshold year | Closing date | | FTC annual notice |
| Notification expiry | Waiting period expiry | | 803.7(a) |
| Contract outside date | Signing | | purchase agreement section |

3. **Pre-closing conduct review**: each interim covenant and integration step, its section, the treatment from `references/waiting-period-and-conduct.md`, section 6, and the redraft.

## Part 6. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| merger-agreement | HSR covenant, efforts standard, outside date, fee allocation, interim operating covenants need drafting or revision | Determination, expected timeline, covenant redlines from Part 5 |
| disclosure-schedules | Governmental consents and approvals schedules must list the HSR filing, or the HSR facts change a representation | The filing obligation, acquired person identity, Part 5 timeline |
| due-diligence-report | Target overlaps, or gun-jumping or information-exchange issues, surface in diligence | Overlap NAICS codes, the Part 5 conduct review, clean-team protocol |
| analyzing-m-and-a-tax-implications | Structure and purchase price allocation, or tax treatment of deferred, contingent and rollover consideration | Valuation worksheet and consideration terms |

**Open items**, each with owner and next action:

| # | Open item | Depends on | Owner | Next action | Blocks filing or closing? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Thresholds, fees and form requirements change; re-confirm against the FTC's current notice and the PNO before filing and before closing."
