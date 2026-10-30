# Output Template

Produce the header and the sections below, in this order. Put numbers in tables; keep prose short. Every figure carries a source locator, a register ID from the assumption register, or [UNVERIFIED]. State the currency and units (for example USD millions) once in the header and do not mix units.

## Contents

1. Header
2. Section 1. Transaction summary and sources and uses
3. Section 2. EBITDA bridge
4. Section 3. Assumption register
5. Section 4. Operating projections and free cash flow
6. Section 5. Debt schedule
7. Section 6. Tax schedule
8. Section 7. Exit and returns
9. Section 8. Sensitivities and scenarios
10. Section 9. Credit statistics
11. Section 10. Reconciliation checks
12. Section 11. Issues, conflicts and judgment calls
13. Section 12. Hand-offs
14. Section 13. Open items and [VERIFY] list

## Header

- Deal or target name, sponsor, date prepared, "Draft for review by a qualified finance professional."
- Assumed closing date, fiscal year end, projection period, assumed exit date or dates.
- Model build basis: spreadsheet delivered, table model in the response, or review of a supplied model.
- Circularity treatment elected (iterative with circuit breaker, beginning-balance interest, or closed form).
- Source-review register: one row per file received.

| File | Type | Date | Rank | Status | Pages, tabs or sections read | Note |
|---|---|---|---|---|---|---|
| name as received | audited FS, QoE, CIM, credit agreement, commitment letter, fee letter, purchase agreement, funds flow, sponsor model, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

## 1. Transaction summary and sources and uses

Entry multiple, the EBITDA definition it applies to, enterprise value, equity purchase price bridge, leverage at close on credit agreement EBITDA.

| Sources | Amount | % | Multiple of [named] EBITDA | Source | Uses | Amount | % | Source |
|---|---|---|---|---|---|---|---|---|

Totals on one line each, then the line "Sources minus uses = 0.00". Show OID either as a use (debt at face in sources) or netted in sources, and say which.

## 2. EBITDA bridge

| Line | Amount | Source locator | In management-adjusted? | In credit agreement EBITDA? (definition clause) | Cap applied | Note |
|---|---|---|---|---|---|---|
| Reported EBITDA | | | | | | |
| Addback: ... | | | | | | |
| Management-adjusted EBITDA | | | | | | |
| Credit agreement EBITDA | | | | | | |

State which figure drives entry valuation, which drives debt sizing and covenants, and the difference in dollars and turns of leverage.

## 3. Assumption register

| ID | Assumption | Value | Units | Source locator or [UNVERIFIED] | Gap class (if open) | Sensitivity tested? |
|---|---|---|---|---|---|---|

Gap classes: unknown fact, source conflict, unverified external lookup, policy election.

## 4. Operating projections and free cash flow

Annual table for each historical year and projection year: revenue, growth, EBITDA, margin, D&A, EBIT, capex (maintenance and growth), change in working capital, cash taxes, unlevered free cash flow, cash interest, levered free cash flow.

## 5. Debt schedule

One block per tranche per period: beginning balance, draws or PIK, mandatory amortization, sweep, optional prepayment, ending balance, rate (benchmark, floor, margin, all-in), balance basis for interest, cash interest, non-cash interest. Then: cash available for debt service, minimum cash, excess cash flow per the agreement's definition, sweep percentage and step-down test, revolver availability.

## 6. Tax schedule

By taxable year: taxable income build, tax depreciation, ATI (with the rule that applies to that year), 163(j) limit, business interest expense (stated interest plus OID accrual), disallowed amount and carryforward roll, NOL usage (80 percent limit and any IRC 382 limit), cash taxes. Each line marked as an approximation for tax adviser review.

## 7. Exit and returns

| Exit date | Exit EBITDA (LTM or NTM) | Exit multiple (rationale) | Exit EV | Net debt at exit | Exit costs | Management equity | Sponsor equity value |
|---|---|---|---|---|---|---|---|

Sponsor cash flow schedule:

| Date | Event | Contribution (negative) | Distribution (positive) | Source |
|---|---|---|---|---|

Then IRR (dated, XIRR basis) and MOIC, gross of fund fees and carry unless stated otherwise, with the holding period in years.

## 8. Sensitivities and scenarios

Two-way tables (IRR and MOIC): entry versus exit multiple; exit year versus exit multiple; leverage versus EBITDA growth. A scenario table for base, management, lender and downside cases with returns, minimum liquidity and covenant headroom.

## 9. Credit statistics

By year: total and senior leverage (gross and net, on credit agreement EBITDA), interest coverage, fixed charge coverage, free cash flow to debt, cumulative paydown percent, covenant level and headroom.

## 10. Reconciliation checks

Every row is computed, not asserted. A Fail or Not built row goes to Section 11.

| # | Check | Test | Periods | Result (Pass / Fail / Not built) | Difference | Note |
|---|---|---|---|---|---|---|
| R1 | Sources equal uses | Total sources minus total uses = 0 | Close | | | |
| R2 | Equity plug | Sponsor equity = total uses minus debt sources minus rollover and co-invest | Close | | | |
| R3 | Debt schedule rolls forward | Per tranche: beginning + draws + PIK - amortization - sweep - optional = ending; ending equals next beginning | All | | | |
| R4 | Balance sheet balances | Total assets minus total liabilities and equity = 0, including the opening balance sheet at close | All | | | |
| R5 | Cash ties | Cash flow statement ending cash = balance sheet cash = cash line in the debt schedule | All | | | |
| R6 | Liquidity floor | Cash at or above minimum cash; revolver drawn at or below commitment | All | | | |
| R7 | Interest recomputed | Rate times stated balance basis, recomputed by hand for one period per tranche | One per tranche | | | |
| R8 | Circularity | Successive iterations differ by less than the tolerance, or beginning-balance election disclosed | All | | | |
| R9 | Retained earnings roll | Beginning + net income - dividends = ending | All | | | |
| R10 | Net debt at exit | Exit bridge net debt equals the debt schedule and cash at the exit date | Exit | | | |
| R11 | Returns arithmetic | MOIC = distributions / contributions; IRR dates match the sponsor cash flow schedule | Exit | | | |
| R12 | Leverage at close | Debt at close / credit agreement EBITDA matches the commitment papers' sizing | Close | | | |
| R13 | 163(j) carryforward | Beginning + disallowed - used = ending | All | | | |

## 11. Issues, conflicts and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on equity check, IRR or leverage | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (equity check, debt sizing or covenant compliance wrong by a material amount; a reconciliation check fails); High (a returns or tax figure changes materially under the alternative); Medium (presentation or a conflict with a clear controlling source); Low (clean-up). Judgment calls (exit multiple, circularity treatment, scenario weights, ECF timing) list the options, the choice and what changes under each.

## 12. Hand-offs

A hand-off names the specific facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (figures, dates, document locators) | Open questions | What this model did not do |
|---|---|---|---|---|
| analyzing-m-and-a-tax-implications | Structure, step-up, 163(j), 382, AHYDO, deal-cost deductibility | | | |
| analyzing-earnings-quality | Addbacks not supported by the QoE or the statements | | | |
| managing-debt-covenant-compliance | Covenant definitions and headroom tests | | | |
| writing-investment-committee-memos | Returns, risks, sensitivities for the IC | | | |

Add or remove rows to match the matter.

## 13. Open items and [VERIFY] list

| # | Open item | Gap class | Depends on | Owner | Next action | Changes which output |
|---|---|---|---|---|---|---|

Then each [VERIFY] statement and what would settle it.

Close with: "Draft for review by a qualified finance professional. Not investment, tax, accounting or legal advice, and not a lender commitment."
