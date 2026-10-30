# Output Template

Produce the header and the sections below, in this order. Put figures in tables; keep prose short. Every fact carries a source locator (document, page, section, tab or cell) or [UNVERIFIED]; every rule carries its citation and tax year from `primary-sources.md` or [VERIFY]. State the currency, units and tax year once in the header.

## Contents

1. Header and source-review register
2. Section 1. Question, scope and recommendation range
3. Section 2. Structure snapshot
4. Section 3. Status and eligibility tests
5. Section 4. Clock table
6. Section 5. Two-layer comparison
7. Section 6. Sensitivities
8. Section 7. Reconciliation checks
9. Section 8. Issues, conflicts and judgment calls
10. Section 9. Hand-offs
11. Section 10. Open items and [VERIFY] list

## Header

- Client or matter name, date prepared, tax years covered, "Draft for review by a qualified tax adviser."
- Deliverable type: entity-choice memo, structure review, election checklist, or review of a supplied model.
- Source-review register, one row per file received:

| File | Type | Date | Rank | Status | Pages, tabs or sections read | Note |
|---|---|---|---|---|---|---|
| name as received | charter, bylaws, operating agreement, shareholders' agreement, stock ledger, Form 2553 or IRS acceptance letter, Form 8832, returns, financial statements, valuation, model, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

Rank 1: executed governing documents, filed elections and IRS letters, filed returns. Rank 2: audited financial statements, valuation reports, stock ledger with transfer records. Rank 3: management accounts, models, cap table spreadsheets. Rank 4: emails, memos, summaries and secondary commentary.

## 1. Question, scope and recommendation range

The decision asked, the alternatives compared, the tax years, the owners covered, what is out of scope and where it is routed. State results as a range or as conditional on named policy elections; no single recommendation without the conditions it depends on.

## 2. Structure snapshot

| Entity | Jurisdiction | Federal classification and source | Owners (vote %, value %) | Elections and effective dates | Consolidated group member? | Notes |
|---|---|---|---|---|---|---|

Add an owner table: owner, type (individual, trust, partnership, corporation, exempt, foreign), residence, material participation, marginal rate band for the year.

## 3. Status and eligibility tests

| Test | Entity or block | Rule and citation (tax year) | Facts relied on (locator) | Result: Met / Not met / Not determinable | What would change it |
|---|---|---|---|---|---|
| S eligibility: shareholders | | IRC 1361(b)(1)(A)-(C) | | | |
| S eligibility: one class of stock | | IRC 1361(b)(1)(D); Treas. Reg. 1.1361-1(l) | | | |
| QSBS per block: regime, gross assets, active business, holding | | IRC 1202 | | | |
| Affiliated group membership (vote and value) | | IRC 1504(a) | | | |
| CAMT applicable corporation (aggregated) | | IRC 59(k)(1) | | | |
| AET exposure; PHC tests | | IRC 531-537; 541-542 | | | |
| PTE election eligibility by state | | State statute [VERIFY] | | | |

## 4. Clock table

One row per timed element, each with its own trigger event, computed date, and the source for the trigger date.

| Element | Trigger event | Trigger date (locator) | Length or test | Computed date | Citation |
|---|---|---|---|---|---|

## 5. Two-layer comparison

Per alternative and per tax year, for a stated distribution policy (payout share of after-tax earnings):

| Line | Alternative A | Alternative B | Citation and year |
|---|---|---|---|
| Pre-tax income | | | |
| Entity-level federal tax | | | |
| Entity-level state tax and PTE tax | | | |
| Owner-level income included (wages, K-1 share, dividends) | | | |
| 199A deduction (with the binding limit named) | | | |
| Owner-level federal income tax | | | |
| NIIT | | | |
| Owner-level state tax and credits | | | |
| Payroll taxes (or "not modeled") | | | |
| Total tax | | | |
| Effective rate on pre-tax income | | | |

Then the exit table (stock sale, asset sale) with IRC 1202 exclusion by block, and the break-even payout share.

## 6. Sensitivities

At least: payout share (0, break-even, 100 percent); exit year against the IRC 1202 tiers and the IRC 1374 recognition period; owner marginal rate band; state of residence; year-dependent figures through 2030 where the SALT cap changes.

## 7. Reconciliation checks

Every row is computed, not asserted. A Fail goes to Section 8.

| # | Check | Test | Result (Pass / Fail / Not applicable) | Difference | Note |
|---|---|---|---|---|---|
| R1 | Ownership adds up | Vote and value each total 100 percent per entity | | | |
| R2 | Classification sourced | Every entity has a classification with an election, letter or default rule cited | | | |
| R3 | Two layers | Entity tax plus owner tax equals total tax for each alternative and year | | | |
| R4 | Distribution policy | Distributions equal after-tax earnings times the stated payout share | | | |
| R5 | 199A limits | Deduction does not exceed 20 percent of QBI, the wage or UBIA limit where it applies, or 20 percent of taxable income less net capital gain | | | |
| R6 | QSBS by block | Each block's regime matches its acquisition and issue dates; exclusion does not exceed the per-issuer limit | | | |
| R7 | Group membership | Each consolidated member meets 80 percent vote and 80 percent value every day of the year | | | |
| R8 | CAMT aggregation | Status test sums AFSI of every IRC 52(a) or (b) group member | | | |
| R9 | PTE tie-out | PTE tax paid per owner ties to owner credits and, for an S corporation, to equalizing distributions | | | |
| R10 | Dated authority | Every rate and threshold shows its tax year and citation | | | |

## 8. Issues, conflicts and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on status or tax | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (an election, QSBS status or group membership fails, or total tax changes materially); High (a figure changes materially under an alternative reading); Medium (a conflict with a clear controlling source); Low (clean-up). Judgment calls list the options, the choice and what changes under each.

## 9. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Trigger | Facts passed (figures, dates, locators) | Open questions | What this analysis did not do |
|---|---|---|---|---|
| analyzing-international-tax-planning | A foreign owner, foreign subsidiary, CFC, treaty, inbound or outbound structure, or a foreign-parented group CAMT test | | | |
| managing-transfer-pricing-compliance | Pricing of transactions with related parties outside the consolidated group, or any cross-border intercompany charge | | | |
| analyzing-m-and-a-tax-implications | Buying or selling a business or entity, pre-sale reorganizations, step-up elections, acquired losses | | | |
| analyzing-partnership-tax-structures | Partnership allocations, basis, waterfalls and carried interest inside an LLC alternative | | | |
| analyzing-state-income-tax | Nexus, apportionment and combined reporting beyond the PTE election decision | | | |

Add or remove rows to match the matter.

## 10. Open items and [VERIFY] list

| # | Open item | Gap class (unknown fact, source conflict, unverified external lookup, policy election) | Depends on | Owner | Next action | Changes which result |
|---|---|---|---|---|---|---|

Then each [VERIFY] statement and what would settle it.

Close with: "Draft for review by a qualified tax adviser. Not tax, legal or accounting advice, and not a tax opinion."
