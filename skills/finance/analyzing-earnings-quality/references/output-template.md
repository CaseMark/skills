# Output Template

Produce the header and the sections below, in this order. Put numbers in tables; keep prose short. Every figure carries a source locator (document, page or tab, line or cell) or [UNVERIFIED]. State currency and units once in the header and do not mix them. Sections that do not apply (for example Section 8 for a private company) stay in place with "Not applicable" and the reason.

## Contents

1. Header and source-review register
2. Section 1. Scope and conclusions summary
3. Section 2. Adjustment register and EBITDA bridge
4. Section 3. Pro forma column
5. Section 4. Accruals and cash conversion
6. Section 5. Working capital days, reserves and capitalized costs
7. Section 6. Beneish M-score
8. Section 7. Revenue-side and classification red flags
9. Section 8. Non-GAAP disclosure review (registrants)
10. Section 9. Reconciliation checks
11. Section 10. Issues, conflicts and judgment calls
12. Section 11. Declined parts
13. Section 12. Hand-offs
14. Section 13. Open items and [VERIFY] list

## Header

- Company and legal entity analyzed (consolidated group, carve-out or subsidiary), registrant status (registrant under 17 CFR 244.101(c) or not), purpose (buy-side diligence, lender review, equity research screen, issuer disclosure review), date prepared, "Draft for review by a qualified accounting and finance professional."
- Periods analyzed (fiscal years, LTM date and how LTM was built), currency and units.
- Source-review register, one row per file received:

| File | Type | Period | Rank | Status | Pages, tabs or sections read | Note |
|---|---|---|---|---|---|---|
| name as received | audited FS, reviewed interims, QoE report, management adjustments schedule, trial balance, aging, reserve rollforward, earnings release, 10-K/10-Q, CIM, email | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

Rank 1: audited statements and executed agreements. Rank 2: reviewed interims, trial balances, subledgers. Rank 3: QoE report and management schedules. Rank 4: CIM, presentations, emails.

## 1. Scope and conclusions summary

Five to ten lines: reported EBITDA, management-adjusted or QoE-adjusted EBITDA, diligence-adjusted EBITDA (this analysis), the difference and its three largest drivers, cash conversion, the highest-severity red flags, and what remains open. No statement that the company committed fraud or manipulated earnings.

## 2. Adjustment register and EBITDA bridge

| # | Adjustment | Amount | Source locator | Prior-two-year history | Label | In diligence-adjusted? | Note |
|---|---|---|---|---|---|---|---|
| | Reported EBITDA (net income + interest + taxes + D&A) | | | | | | |
| A1 | ... | | | | Supported / Recurring / Pro forma only / Tailored / Unsupported | Yes / No | |
| | Management or QoE adjusted EBITDA | | | | | | |
| | Diligence-adjusted EBITDA | | | | | | |

State the difference between management or QoE adjusted EBITDA and diligence-adjusted EBITDA in dollars and percent, and, when a price or leverage figure is given, the multiple or leverage on each.

## 3. Pro forma column

| Item | Amount | Evidence of realization | Dis-synergies or offsets | Cap at historical cost? | Timing |
|---|---|---|---|---|---|

Show diligence-adjusted EBITDA plus pro forma items as a separate total, labeled "Pro forma; not historical earnings".

## 4. Accruals and cash conversion

| Year | Net income | CFO | Accruals (Sloan) | Accruals (NI - CFO) | Average total assets | Accrual ratio | EBITDA | CFO / EBITDA | (CFO - capex) / EBITDA |
|---|---|---|---|---|---|---|---|---|---|

Explain every period below 100 percent CFO to EBITDA by named drivers with amounts.

## 5. Working capital days, reserves and capitalized costs

| Year | Revenue growth | Receivables growth | DSO | Inventory growth | DIO | DPO | Over-90-day receivables % | Allowance coverage % |
|---|---|---|---|---|---|---|---|---|

Reserve rollforward per reserve (beginning, provision, utilization, other, ending) and the EBITDA effect of any release. Capitalization rate by period for software and contract costs and EBITDA at the prior-period rate.

## 6. Beneish M-score

| Variable | Year t inputs | Year t-1 inputs | Value | Coefficient | Contribution |
|---|---|---|---|---|---|

Then: M to two decimals, probability (standard normal CDF of M), the read-out label ("Above -1.78 (screen flag)" or "At or below -1.78 (no screen flag)"), the variables driving the result, and the model's limits for this company. If two consecutive fiscal years are not available, use the Section 11 label "Declined - Insufficient periods" and name the missing input.

## 7. Revenue-side and classification red flags

| # | Flag | Metric and value | Comparison | Severity | Evidence needed to clear or confirm | Route to |
|---|---|---|---|---|---|---|

Severity: High (changes adjusted earnings or cash conversion materially, or a recognition question on a material amount); Medium (a trend without a quantified earnings effect yet); Low (presentation or documentation).

## 8. Non-GAAP disclosure review (registrants)

| # | Measure and document (release, 10-Q, 10-K, proxy) | Issue | Rule or CFI | Label (Noncompliant / Staff-view risk / Acceptable with disclosure) | Effect on the measure | Suggested fix |
|---|---|---|---|---|---|---|

## 9. Reconciliation checks

Every row is computed, not asserted. A Fail row goes to Section 10.

| # | Check | Test | Result (Pass / Fail / Not run) | Difference | Note |
|---|---|---|---|---|---|
| E1 | Reported EBITDA | Net income + interest + income taxes + D&A = reported EBITDA, each from the statements | | | |
| E2 | Bridge foots | Reported EBITDA + each adjustment = adjusted EBITDA, for the management or QoE bridge and for the diligence bridge | | | |
| E3 | Adjustment support | Each adjustment ties to a source locator or carries Unsupported | | | |
| E4 | LTM build | Fiscal year + current year-to-date - prior year-to-date = LTM, per line | | | |
| E5 | Cash flow ties | CFO and capex equal the cash flow statement for the same period | | | |
| E6 | Accrual inputs | Balance sheet changes used in Sloan accruals equal the two balance sheets | | | |
| E7 | Accrual methods | Sloan accruals versus NI - CFO: difference explained (acquisitions, non-cash items) | | | |
| E8 | Working capital days | Receivables, inventory, payables, revenue and COGS tie to the statements; same basis each year | | | |
| E9 | Reserve rollforward | Beginning + provision - utilization +/- other = ending, per reserve and year | | | |
| E10 | M-score recomputation | Each variable recomputed from the inputs; M equals the weighted sum; coefficients and -1.78 cutoff as in Beneish (1999) | | | |
| E11 | Non-GAAP reconciliation | Starts from the GAAP measure and foots to the non-GAAP measure (registrants) | | | |
| E12 | Units and periods | One currency and unit; numerator and denominator on the same period basis | | | |

## 10. Issues, conflicts and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Effect on adjusted EBITDA, cash conversion or a ratio | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Judgment calls (two-year window applied to a private company, materiality threshold, stock-based compensation policy, scaling base) list the options, the choice and what changes under each.

## 11. Declined parts

When a hard stop declines part of a request, open that part with this fixed label, using the hard stop's name exactly as Checkpoint A gives it:

"Declined - [hard stop name]: [the part requested]. Needed to proceed: [what would allow it, or 'nothing; this part will not be produced']."

Hard stop names: No anchor statement; Insufficient periods; Target-driven adjustments; Conduct conclusion or assurance; Audited figures set aside. For example, "Declined - Target-driven adjustments: identifying addbacks to reach $47.5m of adjusted EBITDA." Complete the rest of the deliverable. A declined part is never replaced by a figure produced another way.

## 12. Hand-offs

A hand-off names the specific facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (figures, dates, locators) | Open questions | What this analysis did not do |
|---|---|---|---|---|
| managing-revenue-recognition | ASC 606 five-step contract analysis for bill-and-hold, principal or agent, variable consideration and contract modification flags | | | |
| building-lbo-models | Diligence-adjusted EBITDA for the model's bridge to credit agreement Consolidated EBITDA, debt sizing and returns | | | |
| writing-investment-committee-memos | EBITDA addbacks and QoE adjustments the IC memo relies on; the memo drafts the recommendation | | | |
| conducting-working-capital-due-diligence | Working capital normalization and the peg | | | |
| managing-earnings-releases | A registrant's earnings release and GAAP to non-GAAP reconciliation | | | |
| legal-research | Securities law exposure or enforcement questions (no dedicated finance skill) | | | |

Add or remove rows to match the matter.

## 13. Open items and [VERIFY] list

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Depends on | Owner | Next action | Changes which output |
|---|---|---|---|---|---|---|

Then each [VERIFY] statement and what would settle it.

Close with: "Draft for review by a qualified accounting and finance professional. Not an audit, review, examination or agreed-upon procedures report, not a fairness opinion, not legal advice, and not a finding that any person committed fraud or manipulated earnings."
