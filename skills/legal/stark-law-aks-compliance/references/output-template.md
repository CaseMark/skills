# Output Template

Produce the header and the eight parts in this order, one set of conclusions per arrangement and per period when terms changed. Keep sentences plain and put detail in tables. Every date shows its weekday. Quote agreement terms only from the executed documents, with section and page.

## Contents

1. Header and source-review register
2. Part 1. Opinion status and conclusion labels
3. Part 2. Arrangement matrix and threshold screen
4. Part 3. Stark analysis
5. Part 4. AKS analysis
6. Part 5. State law, reliance and exposure
7. Part 6. Blocking issues, judgment calls and reconciliation table
8. Part 7. Remediation, disclosure path and arrangement controls
9. Part 8. Hand-offs, open items and `[VERIFY]` list

## Header

- Addressee (the client), matter, arrangements reviewed, today's date, preparer note: "Draft for attorney review."
- Client and role (hospital, health system, physician group, physician, investor); requester's role; conflict check result.
- Question asked: prospective structuring review, review of an existing arrangement, look-back review of a past period, or disclosure decision.
- Forum facts: state of each party and of the services, federal circuit, payer mix.
- **Source-review register**, one row per file:

| File | Type | Date | Status | Pages read | Note |
|---|---|---|---|---|---|
| name as received | agreement, amendment, signature page, payment ledger, time logs, FMV report, org chart, referral data, emails, board minutes, prior opinion, advisory opinion | | Reviewed / Not relevant / Unreadable after attempt / Still needed | | method tried, or who supplies it |

## Part 1. Opinion status and conclusion labels

**Opinion status**, one label used exactly:

- **Ready for attorney review**: no open item above Low.
- **Ready subject to listed confirmations**: open items are High or lower.
- **Not ready: blocking issues**: at least one Critical item is open. The analysis is still included unless a hard stop applies.
- **Declined: hard stop**: give the reason, the request or routing the hard stop calls for, and what can be done instead.

**Stark label**, one per arrangement and period, used exactly:

- **Stark: not implicated**: no physician or immediate family member, no referral, no DHS payable by Medicare, or no financial relationship; say which.
- **Stark: exception met**: name the exception; every element Met with a source.
- **Stark: exception not met**: name each exception tested and each element not met. For a proposed arrangement, the label describes the arrangement as structured.
- **Stark: undetermined**: a blocking fact prevents a conclusion; say what decides it.

**AKS label**, one per arrangement and period, used exactly:

- **AKS: safe harbor met**: name the safe harbor; every element Met with a source.
- **AKS: no safe harbor; risk low**: no safe harbor, and the facts and intent evidence show low risk; say why.
- **AKS: no safe harbor; risk elevated**: no safe harbor, and a referral-related purpose, a volume-based term, or another risk factor is present.
- **AKS: undetermined**: a blocking fact prevents a conclusion.

**State law label**: **State law: no issue on verified statutes**, **State law: issue identified**, or **State law: not researched [VERIFY]**.

**Disclosure path label**: **Disclosure path: none indicated**, **Disclosure path: CMS SRDP**, **Disclosure path: OIG SDP**, **Disclosure path: contractor refund**, or **Disclosure path: counsel decision required**.

Then a one-paragraph summary per arrangement: the labels, the main reason, the main exposure if the conclusion is wrong, and the recommended action.

## Part 2. Arrangement matrix and threshold screen

| # | Parties (DHS entity; physician or other referral source) | Type | Term and dates | Compensation as written | Compensation as paid | Referral source a physician? | DHS payable by Medicare? | Direct, indirect, stand in the shoes |
|---|---|---|---|---|---|---|---|---|

## Part 3. Stark analysis

For each arrangement: the exception or exceptions tested, an element table (Element / Requirement and citation / Fact and source / Met, Not met, Unknown), then separate conclusions on fair market value, commercial reasonableness, and volume or value, each with its own evidence. Then set in advance and any modification, holdover status, and the clocks.

**Clock format**, one row per timed element:

| Element | Trigger event | Trigger date (weekday) and evidence | Period | Deadline or days elapsed | Status | Source |
|---|---|---|---|---|---|---|

## Part 4. AKS analysis

For each arrangement: remuneration and who gives and receives it; federal program business involved; safe harbor element table; intent evidence for and against, with sources; the governing circuit's intent standard or both readings; FCA causation standard in the circuit or `[VERIFY]`; the AKS label.

## Part 5. State law, reliance and exposure

1. State and other all-payor laws screened (statute, reach, conclusion or `[VERIFY]`).
2. Advisory opinions and prior opinions: who may rely, what they address, each material factual difference.
3. Exposure: Stark payment denial and refund (period, DHS claims, amount if supplied), CMPs, AKS criminal and civil exposure, FCA hand-off.

## Part 6. Blocking issues, judgment calls and reconciliation table

| # | Severity | Issue | Why it matters | Source | Recommendation and alternatives | Owner |
|---|---|---|---|---|---|---|

Severity: Critical (no executed agreement located; no fair market value support for compensation relied on; compensation paid differs from compensation written; set-in-advance failure; referral-related intent evidence; stand-in-the-shoes status unknown; a cure window about to close; an advisory opinion relied on by a non-requestor); High (FMV report stale or silent on part of the scope; time records missing; payer mix unknown; state law unresearched where commercial business is material); Medium; Low.

Judgment calls (restructure, terminate, refund, disclose, seek an advisory opinion) each state the options, the recommended choice and the reason.

**Reconciliation table**:

| Item | Source 1 (locator) | Source 2 (locator) | Conflict? | Value used and why |
|---|---|---|---|---|
| Effective, expiration and signature dates | agreement | signature page or e-signature log | | |
| Compensation rate and formula | agreement or amendment | payment ledger | | |
| Services furnished | agreement | time logs or deliverables | | |
| Ownership of each party | org chart | operating agreement or cap table | | |
| Referral and DHS volume | referral report | claims data | | |
| FMV range and date | valuation report | term sheet | | |

## Part 7. Remediation, disclosure path and arrangement controls

1. Prospective fixes: amend in writing before the services the change covers, restructure, or terminate; never backdate.
2. Look-back: noncompliant period, affected DHS claims, quantification method, the 60-day clock and suspension status, and the disclosure path label with reasons.
3. Arrangement controls tied to the findings: central master list of physician contracts, expiration tracking with renewal lead time, payment-to-contract reconciliation before each payment, time-record requirement for hourly or stipend arrangements, FMV refresh cadence, and an approval step for any rate change.

## Part 8. Hand-offs, open items and `[VERIFY]` list

**Hand-offs.** A hand-off carries the facts the receiving workflow needs; a skill name alone is not a hand-off.

| To | When | What to pass |
|---|---|---|
| conducting-stark-law-analysis | The compliance department needs a provider-side operational review or documentation workflow for arrangements across the portfolio | Arrangement matrix, exception chosen per arrangement, element gaps |
| conducting-false-claims-analysis | FCA exposure, qui tam risk, overpayment quantification or settlement modeling is needed | Noncompliant periods, affected claims, AKS and Stark conclusions, disclosure path |
| conducting-anti-kickback-analysis | Provider-side safe harbor documentation for many payment arrangements | Safe harbor element tables and gaps |
| physician-employment-agreement or healthcare-services-agreement | The structure is settled and the agreement must be drafted | Compensation formula, term, duties, exception and safe harbor elements to build in |
| managing-compliance-programs | The client needs a program-wide compliance plan (training, hotline, auditing) rather than an arrangement opinion | Findings and the arrangement controls in Part 7 |
| legal-research | A state self-referral, anti-kickback, fee-splitting or patient brokering law is not verified in `references/primary-sources.md` (no dedicated skill exists) | State, payer mix, arrangement terms, the question |

**Open items**:

| # | Open item | Gap class | Owner | Next action | Blocks the opinion? |
|---|---|---|---|---|---|

**`[VERIFY]` list:** each statement, why it is unconfirmed, and what would settle it.

Close with: "Draft for attorney review. Not to be relied on or shared until counsel confirms the executed documents, the payment history, the governing circuit and state law, and every clock in Part 3."
