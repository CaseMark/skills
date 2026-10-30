# Output Template

Produce the header and the sections below, in this order. Put numbers in tables; keep prose short. Every figure carries a source locator, an assumption register ID, or [UNVERIFIED]. State currency and units (for example USD millions, shares in millions) once in the header and do not mix them.

## Contents

1. Header
2. Section 1. Value summary and football field
3. Section 2. Assumption register
4. Section 3. Forecast and unlevered free cash flow
5. Section 4. Discount rate
6. Section 5. DCF and terminal value
7. Section 6. Trading comparables
8. Section 7. Precedent transactions
9. Section 8. Enterprise value to equity value bridge
10. Section 9. Fully diluted shares and per-share value
11. Section 10. Sensitivities
12. Section 11. Reconciliation checks
13. Section 12. Issues, conflicts and judgment calls
14. Section 13. Hand-offs
15. Section 14. Open items and [VERIFY] list

## Header

- Subject company (legal entity), subject interest (class, shares or percentage, control or minority, marketable or not), date prepared, "Draft for review by a qualified valuation professional."
- Standard of value (fair value under ASC 820, fair market value, investment value, statutory fair value, or IVS market value), premise of value, valuation date, purpose and intended users.
- Engagement label: "Draft analysis; not a conclusion of value or calculated value under VS Section 100, not an IVS-compliant valuation report, and not a fairness opinion."
- Build basis: spreadsheet delivered, table model in the response, or review of a supplied model. Discounting convention (end-period or mid-period; stub length).
- Source-review register: one row per file received.

| File | Type | Date | Rank | Status | Pages, tabs or sections read | Note |
|---|---|---|---|---|---|---|
| name as received | audited FS, 10-K/10-Q, indenture, equity plan, cap table, management forecast, broker or data-provider pull, supplied model, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

Partial decline. When a hard stop blocks one part of the request (for example per-share value with no share data), produce the rest and put the blocked part in Section 1 as: "Not produced (hard stop): [what was asked], because [trigger]. Needed to proceed: [items]." Never fill the blocked figure with an estimate.

## 1. Value summary and football field

| Method | Low | Base | High | Driving inputs | Weight and reason |
|---|---|---|---|---|---|
| DCF (Gordon growth) | | | | WACC, g | |
| DCF (exit multiple) | | | | WACC, multiple | |
| Trading comparables | | | | multiple range, LTM or NTM | |
| Precedent transactions | | | | multiple range, control adjustment | |

Then the concluded range at the level of value stated in the header, enterprise value and equity value, and per-share value if produced.

## 2. Assumption register

| ID | Assumption | Value | Units | Source locator or [UNVERIFIED] | Gap class (if open) | Sensitivity tested? |
|---|---|---|---|---|---|---|

Gap classes: unknown fact, source conflict, unverified external lookup, policy election.

## 3. Forecast and unlevered free cash flow

Annual table, historical and forecast: revenue, growth, EBITDA, margin, D&A, EBIT, operating taxes, capex, change in NWC, SBC (and whether added back), UFCF. Name the forecast's author and date and whether it is a most-likely or probability-weighted case.

## 4. Discount rate

| Input | Value | Source and date |
|---|---|---|
| Risk-free rate | | |
| Equity risk premium | | |
| Peer levered betas, D/E, tax rates | | |
| Median unlevered beta | | |
| Subject D/E and relevered beta | | |
| Cost of equity | | |
| Pre-tax and after-tax cost of debt | | |
| Weights (D/V, E/V) | | |
| WACC | | |

## 5. DCF and terminal value

Discount factor table by period showing the time t used. Terminal value by both methods with: implied exit multiple of the Gordon value, implied growth of the exit multiple value, the long-run nominal growth benchmark and its source, PV of terminal value as a share of EV.

## 6. Trading comparables

| Peer | Why included | Growth | Margin | EV (same bridge as subject) | EV/LTM EBITDA | EV/NTM EBITDA | P/E | Fiscal year end and calendarization |
|---|---|---|---|---|---|---|---|---|

Statistics (median, interquartile range), the selected range and why, and the subject metric for the same period.

## 7. Precedent transactions

| Date | Target | Acquirer | Stake acquired | EV | EV/LTM EBITDA | Premium to unaffected price | Consideration | Relevance |
|---|---|---|---|---|---|---|---|---|

State whether the indication is on a control basis and the adjustment applied to reach the subject interest's level of value.

## 8. Enterprise value to equity value bridge

| Item | Amount | Basis (fair value, carrying, liquidation preference, after-tax) | Valuation date match | Source |
|---|---|---|---|---|

List every item in `references/valuation-mechanics.md` Section 6, including items assessed and set to zero with the reason (for example operating lease liabilities on a post-rent basis).

## 9. Fully diluted shares and per-share value

| Security | Count | Strike or conversion price | Method (basic, TSM, full count, conversion test) | Incremental shares at converged value |
|---|---|---|---|---|

Then the iteration result: per-share value, diluted count and the change at the last iteration.

## 10. Sensitivities

Two-way tables of per-share or equity value: WACC versus g; WACC versus exit multiple; comps multiple versus metric. Centre cell equals the base case.

## 11. Reconciliation checks

Every row is computed, not asserted. A Fail or Not built row goes to Section 12.

| # | Check | Test | Result (Pass / Fail / Not built) | Difference | Note |
|---|---|---|---|---|---|
| V1 | UFCF build ties | EBIT x (1 - t) + D&A - capex - change in NWC = UFCF each year; base-year EBIT ties to the statements | | | |
| V2 | Rate matches cash flow | UFCF at WACC, FCFE at cost of equity | | | |
| V3 | WACC arithmetic | Weights sum to 100 percent; relevering D/E equals weighting D/E | | | |
| V4 | Discount timing | Each period's t matches the valuation date, stub and convention | | | |
| V5 | Terminal value cross-check | Implied multiple and implied growth computed; base g at or below the long-run nominal growth benchmark or justified | | | |
| V6 | Terminal value share | PV(TV) / EV stated; explanation if above about 75 to 80 percent | | | |
| V7 | Bridge completeness | Every Section 6 item assessed at the valuation date; no claim twice, no asset whose income is in UFCF | | | |
| V8 | Lease consistency | Lease liability treatment matches the EBITDA and UFCF basis and the comps' EV basis | | | |
| V9 | Share count | Diluted count recomputed; TSM and conversion test at the converged value | | | |
| V10 | SBC consistency | SBC is either expensed, or added back with future dilution modeled; not added back with no dilution | | | |
| V11 | Multiple basis | EV multiples on EV metrics, equity multiples on equity metrics; LTM to LTM, NTM to NTM | | | |
| V12 | Level of value | Premiums and discounts match the subject interest and the standard of value | | | |
| V13 | Sensitivity anchor | Centre cell of each table equals the base case | | | |

## 12. Issues, conflicts and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on value | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (value or per-share wrong by a material amount; a reconciliation check fails); High (value changes materially under the alternative); Medium (presentation, or a conflict with a clear controlling source); Low (clean-up). Judgment calls (SBC treatment, pension tax treatment, terminal timing, weights) list the options, the choice and what changes under each.

## 13. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (figures, dates, locators) | Open questions | What this model did not do |
|---|---|---|---|---|
| building-lbo-models | LBO model and sponsor returns (IRR, MOIC) using the DCF and comparables that support the exit multiple | | | |
| conducting-cost-of-capital-analysis | Stand-alone WACC study (equity risk premium, beta estimation, debt cost) | | | |
| managing-fair-value-measurement | ASC 820 hierarchy classification and valuation technique documentation | | | |
| writing-investment-committee-memos | Drafting or reviewing the IC memo; this model supplies the valuation model outputs behind it (range, methods, sensitivities, risks) | | | |

Add or remove rows to match the matter.

## 14. Open items and [VERIFY] list

| # | Open item | Gap class | Depends on | Owner | Next action | Changes which output |
|---|---|---|---|---|---|---|

Then each [VERIFY] statement and what would settle it.

Close with: "Draft for review by a qualified valuation professional. Not a conclusion of value, fairness opinion, or investment, tax, accounting or legal advice."
