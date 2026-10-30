# Tax and Accounting Rules for LBO Models

U.S. federal income tax and U.S. GAAP rules that change an LBO model's cash taxes, opening balance sheet or interest line. Each rule carries its citation and the date it was checked (see `primary-sources.md`). This file is for building a reasonable cash-tax projection inside a model; it is not tax advice. State and foreign taxes are out of scope and are [VERIFY] for the tax adviser. Figures that change by year carry their year.

## Contents

1. Corporate rate
2. Business interest limitation, IRC 163(j)
3. What counts as interest for 163(j)
4. OID and high-yield discount obligations
5. Net operating losses: IRC 172 and IRC 382
6. Bonus depreciation, IRC 168(k)
7. Deal costs: tax treatment
8. Deal costs and debt costs: GAAP treatment
9. Modeling checklist

## 1. Corporate rate

IRC 11(b): 21 percent of taxable income for a C corporation, for taxable years beginning after December 31, 2017. A pass-through target (partnership or S corporation) pays no entity-level federal income tax; model owner-level taxes or tax distributions only as the structure requires, and route the structure question to the M&A tax hand-off.

## 2. Business interest limitation, IRC 163(j)

- Deductible business interest expense for the year cannot exceed business interest income, plus 30 percent of adjusted taxable income (ATI), plus floor plan financing interest (IRC 163(j)(1)).
- Disallowed business interest carries forward indefinitely and is treated as business interest paid in the next taxable year (IRC 163(j)(2)). Model the carryforward balance and its use in later years.
- ATI definition by year (IRC 163(j)(8)(A)(v) as amended by Pub. L. 119-21, section 70303):
  - Taxable years beginning before January 1, 2022: depreciation, amortization and depletion are added back (EBITDA-like).
  - Taxable years beginning in 2022, 2023 and 2024: no add-back (EBIT-like).
  - Taxable years beginning after December 31, 2024: the add-back is restored permanently (EBITDA-like).
- For taxable years beginning after December 31, 2025, ATI is computed without regard to amounts included in income under IRC 951(a) (subpart F), 951A(a) (net CFC tested income, formerly GILTI) and 78, with related deduction adjustments (Pub. L. 119-21, section 70342). Relevant to targets with controlled foreign corporations; route to the tax adviser.
- Pub. L. 119-21 also addressed the interaction of the limitation with capitalized interest for taxable years beginning after December 31, 2025; the IRS FAQ states that business interest excludes interest capitalized under IRC 263(g) or 263A(f). Treat any capitalized-interest planning as [VERIFY] with the tax adviser.
- Small business exemption: a taxpayer (other than a tax shelter) meeting the IRC 448(c) gross receipts test is exempt (IRC 163(j)(3)). The inflation-adjusted threshold is $32,000,000 of average annual gross receipts for taxable years beginning in 2026 (Rev. Proc. 2025-32). Aggregation rules apply; a sponsor-backed target is usually well above the threshold. The 2027 amount is [VERIFY].
- ATI is a tax concept (taxable income with listed adjustments), not book EBITDA and not credit agreement EBITDA. Approximating ATI with tax EBITDA is acceptable in a model if labeled as an approximation and [VERIFY] by the tax adviser.

## 3. What counts as interest for 163(j)

Under the final regulations (Treas. Reg. 1.163(j)-1(b)(22), T.D. 9905, 2020), interest includes stated interest and original issue discount. The final regulations do not treat debt issuance costs as interest for 163(j) (they are deducted under the debt issuance cost rules, Treas. Reg. 1.446-5) [VERIFY current text], and the treatment of commitment fees was reserved for future guidance [VERIFY]. So book interest expense (which includes amortized debt issuance costs under GAAP) is not the same number as business interest expense. Build the 163(j) computation from tax interest, not from the income statement interest line.

## 4. OID and high-yield discount obligations

- OID is the excess of the stated redemption price at maturity over the issue price (IRC 1273(a)(1)). It is treated as zero when less than 0.25 percent of the stated redemption price times the number of complete years to maturity (IRC 1273(a)(3)). A term loan issued at 98.0 with a seven-year term (2.0 percent discount versus a 1.75 percent de minimis amount) has OID.
- OID accrues as interest over the life of the instrument on a constant-yield basis and enters the 163(j) computation.
- Applicable high yield discount obligations (IRC 163(i)): a corporate instrument with maturity more than five years from issue, yield to maturity at least the applicable federal rate plus five percentage points, and significant OID. A portion of the OID may be permanently disallowed and the rest deductible only when paid (IRC 163(e)(5)). PIK notes and deeply discounted instruments in a holdco structure are the usual candidates. Flag any PIK or high-discount tranche for the tax adviser; do not model the AHYDO outcome without that review [VERIFY].

## 5. Net operating losses: IRC 172 and IRC 382

- NOLs arising in taxable years beginning after December 31, 2017 carry forward indefinitely, and for taxable years beginning after December 31, 2020 the deduction for those losses is limited to 80 percent of taxable income (computed before the NOL deduction, as the statute specifies); pre-2018 NOLs are deducted first and are not subject to the 80 percent limit (IRC 172(a), (b)); their remaining carryforward period is [VERIFY].
- An LBO is usually an ownership change of the target (more than 50 percentage point increase by 5-percent shareholders within a three-year testing period, IRC 382(g)). After the change, the annual limit on pre-change losses is the value of the old loss corporation immediately before the change times the long-term tax-exempt rate (IRC 382(b)(1), (e), (f)). The long-term tax-exempt rate is the highest adjusted federal long-term rate in effect for any month in the three-calendar-month period ending with the month of the change (IRC 382(f)); the IRS publishes it monthly in a revenue ruling. Use the published figure for the closing month and mark the value [VERIFY] until confirmed. Built-in gain and loss rules (IRC 382(h)) and the continuity of business enterprise requirement (IRC 382(c)) can change the answer; route to the tax adviser.
- Never assume target NOLs shelter the buyer's income in full after closing.

## 6. Bonus depreciation, IRC 168(k)

Pub. L. 119-21, section 70301, made 100 percent additional first-year depreciation permanent for qualified property acquired after January 19, 2025; property acquired before January 20, 2025 stays under the prior phase-down (Notice 2026-11; Rev. Proc. 2026-15). An election to use a lower percentage exists for the first taxable year that includes January 19, 2025. In a stock purchase without a basis step-up, only new capex qualifies; whether acquired tangible property qualifies in an asset purchase or a deemed asset purchase election depends on the used-property rules [VERIFY]. The step-up question goes to the M&A tax hand-off.

## 7. Deal costs: tax treatment

- Costs that facilitate an acquisition are capitalized (Treas. Reg. 1.263(a)-5). Success-based fees are presumed facilitative unless documented otherwise (Treas. Reg. 1.263(a)-5(f)).
- Safe harbor: for a covered transaction, a taxpayer may elect to treat 70 percent of a success-based fee as not facilitating the transaction (deductible) and capitalize 30 percent, by statement attached to the original return for the year paid (Rev. Proc. 2011-29). The election is irrevocable and transaction-specific.
- Financing fees are debt issuance costs, deducted over the term of the debt (Treas. Reg. 1.446-5) [VERIFY].
- Model the tax deduction of deal costs only after the tax adviser confirms the allocation; until then show deal costs as non-deductible in the base case and the safe-harbor result as a sensitivity.

## 8. Deal costs and debt costs: GAAP treatment

- Acquisition-related costs (advisory, legal, accounting, valuation and other professional fees) are expensed by the acquirer in the period incurred, except costs to issue debt or equity, which follow other GAAP (ASC 805-10-25-23). They do not go into goodwill.
- Debt issuance costs for a recognized term debt liability are presented as a direct deduction from the carrying amount of the debt, like a discount, and amortized to interest expense (ASC 835-30-45-1A, added by ASU 2015-03). OID is presented the same way.
- Costs of a line-of-credit (revolver) arrangement may be deferred as an asset and amortized ratably over the term of the arrangement whether or not it is drawn (SEC staff announcement codified by ASU 2015-15).
- Equity issuance costs reduce the proceeds recorded in equity.
- Where the target's statements are prepared under IFRS or the opening balance sheet uses pushdown accounting, flag the difference for the accountant [VERIFY].

## 9. Modeling checklist

1. Tax status of the target and each holding entity stated.
2. 163(j) computed by taxable year, with the ATI rule that applies to that year, the carryforward rolled, and tax interest (stated interest plus OID accrual) separated from book interest.
3. NOL usage capped at 80 percent where applicable and at the IRC 382 annual limit.
4. Depreciation for tax separate from book; bonus depreciation only on qualifying property by acquisition date.
5. Deal-cost deductions shown as a sensitivity until confirmed.
6. Every year-dependent figure dated; every tax conclusion marked as an approximation for tax adviser review.
