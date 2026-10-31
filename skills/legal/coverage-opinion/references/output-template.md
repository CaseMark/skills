# Output Template

Produce the header and the seven parts in this order. Keep sentences plain; put detail in tables. Every date shows its weekday. Quote policy language only from the issued policy, with form number, edition, section and page.

## Contents

1. Header and source-review register
2. Part 1. Opinion status and coverage positions
3. Part 2. Policy and forms reconciliation
4. Part 3. Analysis
5. Part 4. Blocking issues and judgment calls
6. Part 5. Reconciliation table
7. Part 6. Recommended next steps and letter outline
8. Part 7. Hand-offs, open items and `[VERIFY]` list

## Header

- Addressee (the client), matter, insured(s), claimant(s), insurer(s), policy numbers and periods, underlying suit caption and court, today's date, preparer note: "Draft for attorney review."
- Client and role: insurer, named insured, additional insured, excess carrier; the requester's role (coverage counsel, in-house claims, defense counsel) and the conflict check result.
- Governing law: the state chosen, the reason, the contacts considered, and whether the choice is contested.
- **Source-review register**, one row per file in the matter:

| File | Type | Date or edition | Status | Pages read | Note |
|---|---|---|---|---|---|
| name as received | declarations, forms schedule, coverage form, endorsement, complaint, tender letter, reservation letter, claim notes, other policy | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Opinion status and coverage positions

**Opinion status**, one label used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The analysis is still included unless a hard stop in SKILL.md applies; no position may be communicated to the other side until each Critical item is closed.
- **Declined: hard stop**: a hard stop applies. Give the reason, the document request or routing the hard stop calls for, and what can be done instead.

**Duty to defend**, one label per policy and period, used exactly:

- **Duty to defend: owed**: potential coverage and no ground that warrants a reservation.
- **Duty to defend: owed, subject to reservation**: potential coverage, with identified grounds that may defeat indemnity.
- **Duty to defend: not owed**: no claim in the suit is potentially covered under the governing materials rule, every scheduled form has been read, and the reason is stated.
- **Duty to defend: undetermined**: a blocking item prevents any position; say what decides it.

**Duty to indemnify**, one label per policy and period, used exactly:

- **Duty to indemnify: not yet determinable**
- **Duty to indemnify: owed on established facts**
- **Duty to indemnify: not owed on established facts**

Then a one-paragraph summary: the position, the main reason, the main risk to the client if the position is wrong, and the recommended action.

## Part 2. Policy and forms reconciliation

| Period | Carrier and layer | Policy no. | Scheduled form (number and edition) | In file? | Edition matches? | Note |
|---|---|---|---|---|---|---|

Policy matrix for multiple policies: carrier, layer, period, limits, other-insurance clause (quoted), tender date, response.

## Part 3. Analysis

1. **Choice of law.** Contacts, conflict rule, result, and the alternative if contested.
2. **Materials rule.** Which documents decide the duty to defend in the governing state, and which extrinsic facts were considered or excluded and why.
3. **Insuring agreement.** Insured status, "suit", "damages", injury type, "occurrence", territory, policy period and trigger, known injury; burden.
4. **Exclusions and exceptions.** Each exclusion considered, quoted, with exceptions; burden and construction standard; result; exclusions considered and rejected.
5. **Conditions.** Notice, cooperation, voluntary payments, consent; clocks in the fixed format below; prejudice analysis where required.
6. **Reservation, disclaimer and waiver.** What has been sent, when, to whom; timeliness; content gaps; waiver or estoppel risk.
7. **Conflicts.** Whether a reservation creates a conflict, independent counsel rights, and who represents whom.
8. **Other insurance and allocation.** Policy matrix, other-insurance clauses, trigger across periods, allocation reading, tenders.
9. **Duty to indemnify.** Facts that will decide it; evidence and owner.

**Clock format**, one row per timed element:

| Element | Trigger event | Trigger date (weekday) and evidence | Period | Deadline or days elapsed | Status | Source |
|---|---|---|---|---|---|---|

## Part 4. Blocking issues and judgment calls

| # | Severity | Issue | Why it matters to the coverage position | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: Critical (scheduled form or endorsement missing; edition conflict on a provision relied on; governing state undetermined where the materials rule differs; a disclaimer or reservation clock missed or about to run; conflict of interest unresolved; denial recommended where the governing rule is unconfirmed); High (source conflict on a date or limit; other carriers not tendered; prejudice evidence not gathered); Medium (missing claim notes that do not change the position); Low (clean-up).

Judgment calls (filing a declaratory action, withdrawing a defense, offering independent counsel, seeking reimbursement, tendering to other carriers) each state the options, the recommended choice and the reason.

## Part 5. Reconciliation table

| Item | Value used | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|---|
| Policy period | | declarations | claim notes | | |
| Form and edition of each provision quoted | | forms schedule | form in file | | |
| Date of injury or damage | | complaint para. | claim notes | | |
| Date insured learned of occurrence | | | | | |
| Date of notice and tender | | | | | |
| Date insurer had facts to disclaim | | | | | |
| Date of each reservation or disclaimer letter | | | | | |

## Part 6. Recommended next steps and letter outline

Numbered steps with owner and date. If a reservation or disclaimer letter is recommended, give its outline:

```text
[Date]
Via [method required by statute, if any]
To: [named insured; any additional insured; claimant where the statute requires]
Re: [Suit caption] / Policy No. [ ] / Period [ ]

1. The suit and the tender, with dates.
2. The position: defending under reservation / disclaiming / declining, with the label from Part 1.
3. Each provision relied on, quoted with form number and edition.
4. The allegations or facts that raise each ground.
5. Rights reserved (including any reimbursement right the governing law allows).
6. The insured's rights (independent counsel where a conflict exists; right to submit information).
7. Other insurance: request for other policies and tenders made.
8. Contact for questions.
```

## Part 7. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| bad-faith-demand | A claimant (or the insured's counsel for an excess exposure) needs a time-limited policy-limits demand once coverage is accepted or reserved | Policy, limits, every insured, the coverage position and reservation grounds |
| demand-letter | The client needs a general pre-suit demand for payment from a party that is not acting as an insurer on a policy, with no coverage position to take | Parties, claim, damages, exhibits, deadline rationale |
| tender-of-defense | The insured should tender to a contractual indemnitor (subcontractor, vendor, landlord) as well as to its insurers | Contract indemnity and insurance clauses, suit papers, tender dates |
| legal-research | The dispute is first-party coverage (property, UM/UIM, PIP), which is outside this skill's liability-only scope | Policy, claim, insurer's position, governing state |
| insurance-policy-summary | The policy has not yet been summarized | Declarations, forms schedule, endorsements |

**Open items**, each with owner and next action:

| # | Open item | Gap class | Owner | Next action | Blocks communicating the position? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Not to be sent until counsel confirms the governing law, the issued policy forms, and every clock in Part 3."
