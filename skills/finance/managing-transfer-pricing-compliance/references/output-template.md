# Output Template

Produce the header and the sections below, in this order, omitting a section only when the deliverable type in Checkpoint A excludes it (say so in one line). Put figures in tables. Every figure carries a source locator (document, page or tab, cell) or [UNVERIFIED]; every rule carries a citation from the primary sources file or [VERIFY]. State currency and units once.

## Contents

1. Header and source-review register
2. Declined parts
3. Section 1. Scope and controlled transaction inventory
4. Section 2. Functional analysis and characterization
5. Section 3. Method selection
6. Section 4. Benchmarking and accept/reject matrix
7. Section 5. Range, result and adjustment
8. Section 6. Intercompany agreements against conduct
9. Section 7. Year-end adjustment and collateral effects
10. Section 8. Documentation and penalty-protection status
11. Section 9. Reconciliation checks
12. Section 10. Issues, conflicts and judgment calls
13. Section 11. Hand-offs
14. Section 12. Open items and [VERIFY] list

## Header

- Group, entities in scope, taxable years, jurisdictions whose rules are applied, date prepared, "Draft for review by a qualified tax professional."
- Deliverable type: documentation report (local file or 6662(e) study), benchmarking or range test, year-end true-up computation, agreement review, penalty exposure review, loan, guarantee or services pricing review, or the pricing analysis behind an APA proposal or MAP position.
- Return filing date for each year in scope (or "not yet filed") and the source of that date.

| File | Type | Date (as stated on its face) | Rank | Status | Pages, tabs or sections read | Note |
|---|---|---|---|---|---|---|
| name as received | agreement, ledger, statutory accounts, prior study, database export, IDR, APA, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

Rank: 1 executed agreements, filed returns, audited or statutory accounts, APAs and IRS correspondence; 2 general ledger and trial balance; 3 prior studies, database exports, management schedules; 4 emails, summaries and user statements.

## Declined parts

List every part of the request a hard stop or ground rule blocks, one line each, in this exact form, before Section 1:

`Declined: [part] - [hard stop] - [what would allow it]`

Example: `Declined: dating the study before the return filing date - backdating hard stop - nothing; produce it under its actual completion date`. If nothing was declined, write "Declined parts: none." The rest of the deliverable proceeds on the parts not declined.

## 1. Scope and controlled transaction inventory

| # | Transaction | Payer | Recipient | Jurisdictions | Amount and currency | Agreement (locator) | Method | Tested party | Whose return is affected |
|---|---|---|---|---|---|---|---|---|---|

Then: CbC filer and the $850,000,000 preceding-period revenue test; entities excluded and why.

## 2. Functional analysis and characterization

| Function, asset or risk | Entity A | Entity B | Evidence (people, location, documents) | Control and financial capacity (for risks) |
|---|---|---|---|---|

For intangibles add a DEMPE table: function (development, enhancement, maintenance, protection, exploitation), entity performing, entity controlling, funding, legal owner. End with the characterization of each entity and the rows that support it.

## 3. Method selection

| Method | Data available | Reliability and comparability notes | Selected or rejected, and why | Specified method (Y/N) |
|---|---|---|---|---|

State the tested party and PLI and why each is the most reliable under the best method rule.

## 4. Benchmarking and accept/reject matrix

Search strategy (databases, codes, geography, years, screens), then:

| Comparable | Fiscal year end | Years used | Functions and risks | PLI value per year | Weighted PLI | Loss years | Accept or reject | Reason |
|---|---|---|---|---|---|---|---|---|

## 5. Range, result and adjustment

| Item | Value | Basis |
|---|---|---|
| Number of accepted comparables (n) | | |
| Years tested (CPM default: year under review and the two preceding years, 1.482-5(b)(4); a single year is a policy election with its reason) | | |
| Range applied (full range under 1.482-1(e)(2)(iii)(A), or interquartile range under (e)(2)(iii)(B)) and why | | |
| 25th percentile (position rule shown) | | 1.482-1(e)(2)(iii)(C) |
| Median (position rule shown) | | 1.482-1(e)(3) |
| 75th percentile (position rule shown) | | |
| Spreadsheet quartile figures, if supplied, and difference | | |
| Tested party PLI (numerator, denominator, source) | | |
| Within range? | | |
| Adjustment to nearest quartile (amount and direction) | | |
| Adjustment to median (amount and direction) | | |

Where a judgment (disputed comparable, multi-year versus single year) changes the answer, show the table both ways.

## 6. Intercompany agreements against conduct

| Agreement and clause | Contract term | Actual conduct or invoicing (locator) | Consistent? | Consequence (1.482-1(d)(3)(ii)(B)) | Recommendation |
|---|---|---|---|---|---|

## 7. Year-end adjustment and collateral effects

| Effect | Entity | Amount and direction | Timing (timely filed return?) | Customs or VAT treatment | Withholding | Books of both entities | Owner |
|---|---|---|---|---|---|---|---|

Then: how the cash moves (Rev. Proc. 99-32 account elected on the return, or the secondary adjustment that results), and any foreign payment restriction tested under 1.482-1(h)(2).

## 8. Documentation and penalty-protection status

| Principal document (1.6662-6(d)(2)(iii)(B)) | Exists? | Date finalized and evidence | Before return filed? | Note |
|---|---|---|---|---|
| 1 Business overview to 10 Index (one row each) | | | | |

Then: specified method reasonableness factors; IDR date and the 30-day due date, each with its weekday and whether IRC 7503 rolls it; penalty threshold arithmetic for any proposed or estimated adjustment; CbC, master file and local file status by jurisdiction.

## 9. Reconciliation checks

Every row is computed, not asserted. A Fail goes to Section 10.

| # | Check | Test | Result (Pass / Fail / Not run) | Difference | Note |
|---|---|---|---|---|---|
| R1 | Inventory ties to ledger | Each transaction equals both entities' intercompany accounts in amount and currency | | | |
| R2 | Tested party financials | Segmented P&L reconciles to the entity's trial balance or statutory accounts | | | |
| R3 | Comparable PLIs | Each PLI recomputed from the comparable's financials for the stated years | | | |
| R4 | Range arithmetic | Quartiles and median recomputed by the 1.482-1(e)(2)(iii)(C) rule; n stated | | | |
| R5 | Adjustment arithmetic | (Target PLI minus actual PLI) times the PLI base equals the adjustment | | | |
| R6 | True-up booked both sides | Same amount and currency in both entities; customs and VAT treatment recorded | | | |
| R7 | Agreement against invoices | Contract markup, royalty or rate equals what was charged | | | |
| R8 | Documentation dates | Each principal document's finalization date against the return filing date | | | |
| R9 | CbC and files consistent | Revenue and profit by jurisdiction agree across CbC report, master file and local files, or the difference is explained | | | |
| R10 | Loan interest | Interest recomputed from principal, rate, compounding and days; safe haven bounds tested where available | | | |

## 10. Issues, conflicts and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect (amount, year, entity) | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (result outside the range, penalty threshold met without protection, documentation not contemporaneous, safe haven misapplied, intangible transfer unanalyzed); High (comparable set or tested party defect that could move the result outside the range); Medium (agreement drafting gap with conduct consistent); Low (presentation).

## 11. Hand-offs

A hand-off names the facts the receiving work needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (amounts, dates, locators) | Open questions | What this draft did not do |
|---|---|---|---|---|
| analyzing-international-tax-planning | IRC 367(d), cost sharing structure, Pillar Two GloBE, NCTI, FDDEI, BEAT, treaty and foreign interest limits | | | |
| analyzing-corporate-tax-structures | Domestic entity, consolidation or state structure questions raised by the pricing | | | |
| managing-indirect-tax-analysis | Customs value and VAT effects of true-ups and price changes | | | |
| managing-tax-controversy | IRS examination, IDR strategy, protest, appeals, competent authority and APA procedure | | | |
| managing-tax-provision-preparation | ASC 740 provision and uncertain tax position effects | | | |

Add or remove rows to match the matter.

## 12. Open items and [VERIFY] list

| # | Open item | Gap class (unknown fact, source conflict, unverified external lookup, policy election) | Depends on | Owner | Next action | Changes which output |
|---|---|---|---|---|---|---|

Close with: "Draft for review by a qualified tax professional. Not tax or legal advice, not a transfer pricing opinion, and not an assurance of penalty protection."
