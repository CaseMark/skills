# Output Template

Produce the header and the sections below, in this order. Put numbers in tables; keep prose short. Every figure carries a source locator (document, page or section, tab and cell) or [UNVERIFIED]. State the currency and units once in the header and do not mix units.

## Contents

1. Header and source-review register
2. Section 1. Covenant term sheet
3. Section 2. Consolidated EBITDA bridge
4. Section 3. Covenant calculations and status
5. Section 4. Clocks
6. Section 5. Breach path: cure, waiver, amendment
7. Section 6. Basket register
8. Section 7. Classification and disclosure inputs
9. Section 8. Draft compliance certificate
10. Section 9. Reconciliation checks
11. Section 10. Issues, declined items and judgment calls
12. Section 11. Hand-offs
13. Section 12. Open items and [VERIFY] list

## Header

- Borrower group (Borrower and Restricted Subsidiaries), facility, agent, Test Period end date, date prepared, basis (actual, preliminary or forecast), and "Draft for review by a qualified finance professional, counsel and the auditor."
- Source-review register, one row per file received:

| File | Type | Date | Rank | Status | Sections read | Note |
|---|---|---|---|---|---|---|
| as received | credit agreement, amendment, waiver, conformed copy, certificate exhibit, prior certificate, financial statements, add-back support, debt schedule, basket log, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

## 1. Covenant term sheet

| Item | Agreement text (quoted or paraphrased) | Section | Note |
|---|---|---|---|
| Covenant, ratio and level for this Test Period | | | Level set by Test Period end date |
| Accounting terms: GAAP-change mechanism, frozen lease or other accounting rules, rounding clause | | | |
| Cross-default threshold and conditions | | | |
| Next two levels and their dates | | | |
| Springing condition, measurement date | | | |
| Test Period definition | | | |
| Consolidated EBITDA caps, bases, effective dates | | | |
| Cash netting limit | | | |
| Cure right terms | | | |
| Grace periods by covenant type | | | |
| Required Lenders and class votes | | | |

## 2. Consolidated EBITDA bridge

| Row | Amount | Definition clause | Source locator | Cap or sublimit applied | Disallowed | Note |
|---|---|---|---|---|---|---|
| Consolidated Net Income | | | | | | |
| Add-back: ... | | | | | | |
| Capped items before cap | | | | | | |
| Cap: base, percentage, result | | | | | | |
| Pro forma acquired or disposed EBITDA | | | | | | |
| Consolidated EBITDA | | | | | | |
| Memo: reported GAAP EBITDA; earnings-release Adjusted EBITDA | | | | | | Reconciliation only |

## 3. Covenant calculations and status

| Covenant | Numerator | Denominator | Ratio (unrounded) | Rounding clause applied? | Level | Status | Basis | EBITDA cushion ($ and %) | Debt capacity | Next level at current figures |
|---|---|---|---|---|---|---|---|---|---|---|

Pass or fail is decided on the unrounded ratio unless the agreement has a rounding clause, which is then applied exactly. Status uses only: Compliant; Compliant - watch; Not tested; Default - grace period running; Breach - cure available; Breach - waived; Event of Default; Undetermined. For Not tested, show the springing computation beneath the table.

## 4. Clocks

| Element | Trigger event | Trigger date | Period and day count (calendar or Business Days) | Holidays inside the window | Due date and weekday | Business Day roll applied? | Open on the preparation date? | Source |
|---|---|---|---|---|---|---|---|---|

One row per element; each row names its own trigger.

## 5. Breach path: cure, waiver, amendment

- Cure: eligibility test (count, consecutive quarters, rolling-period limit, life limit), minimum amount with formula, window and deadline, where it counts and where it is disregarded, funding restrictions during the window.
- Grace period: whether one applies to this covenant.
- Waiver or amendment: the vote required for each requested change, exposure counted, Defaulting Lenders excluded, percentage achieved and date first met.
- Non-pro-rata proposals: sharing clause, exceptions, consent class, and the counsel hand-off.

## 6. Basket register

| Covenant | Basket and clause | Type | Capacity formula | Capacity at test date | Used (date, transaction) | Remaining | Reclassification allowed? | Source |
|---|---|---|---|---|---|---|---|---|

Builder basket roll: opening, each addition, each use, closing; reconcile to the last certificate.

## 7. Classification and disclosure inputs

For the accountant, not a conclusion: framework (US GAAP or IFRS); violation at the balance sheet date or after it; grace period and probability of cure; waiver date, scope, binding and irrevocable, period; issuance or available-to-be-issued date; covenants at measurement dates within 12 months and probability of failure; refinancing evidence; carrying amount including unamortized costs; S-X 4-08(c) or 470-10-50-2 disclosure facts; the paragraph each fact goes to.

## 8. Draft compliance certificate

Follow the agreement's exhibit. Fill the calculations from Sections 2 and 3, the Default or Event of Default representation (disclosing any that exist), basket and Available Amount usage where required, and leave the officer signature block blank and marked "Draft - not executed".

## 9. Reconciliation checks

| # | Check | Test | Result (Pass / Fail / Not built) | Difference | Note |
|---|---|---|---|---|---|
| C1 | EBITDA bridge ties | Consolidated Net Income plus each row equals Consolidated EBITDA | | | |
| C2 | Statements tie | Each bridge input ties to the financial statements or a support schedule | | | |
| C3 | LTM build | Four quarters sum to the Test Period figure; quarters match prior certificates or the change is explained | | | |
| C4 | Caps applied | Each capped total is at or below its cap with the stated base | | | |
| C5 | Debt ties | Covenant debt ties to the balance sheet and debt schedule at the test date | | | |
| C6 | Cash netting | Netted cash is unrestricted, within any cap, and excludes cure proceeds | | | |
| C7 | Level and date | Level matches the grid for the Test Period end date | | | |
| C8 | Springing trigger | Trigger computed at the measurement date with the stated exclusions | | | |
| C9 | Prior certificate continuity | Methodology matches the last certificate or the change is disclosed | | | |
| C10 | Basket roll | Opening plus additions minus uses equals closing for each builder basket | | | |
| C11 | Vote count | Waiver or amendment percentage recomputed excluding Defaulting Lenders | | | |

## 10. Issues, declined items and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on ratio or status | Recommendation | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (status changes, or a certificate would be inaccurate); High (cushion changes materially or a deadline is at risk); Medium (presentation or a conflict with a clear controlling source); Low (clean-up).

Declined items, one line each, in this form: "Declined (part): [what was asked] - [Ground Rule or hard stop] - [what the package shows instead]". The rest of the package is still produced.

## 11. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (figures, dates, locators) | Open questions | What this package did not do |
|---|---|---|---|---|
| building-lbo-models | Inbound: ongoing covenant calculations and compliance certificates after close come here; send back re-sizing or a revised projection case | | | |
| analyzing-covenant-compliance | Stressed-case headroom, cure capacity and default triggers | | | |
| analyzing-earnings-quality | Add-backs or accruals the statements do not support | | | |
| managing-credit-facility-administration | Borrowing base, availability and ABL reporting | | | |
| managing-sec-reporting | 10-Q or 10-K debt footnote and default disclosure | | | |
| legal-research | Interpretation of sharing exceptions, "open market purchase" and other non-pro-rata proposals; no dedicated skill claims this | | | |
| loan-forbearance | Lender-side forbearance agreement after an Event of Default | | | |

Add or remove rows to match the matter.

## 12. Open items and [VERIFY] list

| # | Open item | Gap class (unknown fact, source conflict, unverified external lookup, policy election) | Owner | Next action | Changes which output |
|---|---|---|---|---|---|

Close with: "Draft for review by a qualified finance professional, counsel and the auditor. Not legal, accounting or investment advice; not an executed compliance certificate."
