# Metrics and Formulas

Every metric states its formula, its inputs with source locators, the periods used and the scaling base. A metric computed on a different definition than the one below is labeled with the definition actually used. Ratios are screens that point to where to look; none of them proves an error or misstatement.

## Contents

1. Accruals (Sloan 1996 balance-sheet measure, cash-flow measure)
2. Cash conversion
3. Working capital days (DSO, DIO, DPO)
4. Beneish (1999) M-score: variables, coefficients, cutoff
5. Reserve and allowance rollforward tests
6. Capitalized cost tests (internal-use software, contract costs)
7. Revenue-side red flag tests (channel stuffing, bill-and-hold, related parties)
8. One-time gains and classification tests
9. Common computation errors

## 1. Accruals

**Sloan (1996) operating accruals, balance-sheet method.** Accruals = (change in current assets - change in cash and cash equivalents) - (change in current liabilities - change in debt included in current liabilities - change in income taxes payable) - depreciation and amortization expense. Sloan scales accruals, earnings and cash flows by average total assets (beginning plus end of year, divided by two). In Sloan's tests, earnings is operating income after depreciation; the cash flow component is earnings minus accruals.

What Sloan found (The Accounting Review 71(3), 1996, sample of 40,679 NYSE and AMEX firm-years, 1962-1991): the accrual component of earnings is less persistent than the cash component, and stock prices act as if investors "fixate" on earnings. A hedge portfolio long the lowest-accrual decile and short the highest earned a 10.4 percent size-adjusted return in the first year after formation (4.8 percent in the second). Use it for persistence: earnings carried by high accruals are expected to revert faster. It is not a fraud test.

**Cash-flow method (for periods after cash flow statements exist).** Total accruals = income from continuing operations - cash flow from operations (CFO). Scale by average total assets. The two methods differ (acquisitions, divestitures, non-cash items and reclassifications break the balance-sheet method), so state which one was used and do not compare one company's balance-sheet accruals with another's cash-flow accruals.

**Read-out.** Show accruals and the accrual ratio by year for at least two years, the direction of change, and the main driver (receivables, inventory, payables, other). There is no regulatory threshold; any cutoff (for example a peer median band) is a policy election stated in the assumption register.

## 2. Cash conversion

| Measure | Formula | Note |
|---|---|---|
| CFO to EBITDA | CFO / EBITDA | Primary measure; state whether EBITDA is reported or adjusted |
| CFO to net income | CFO / net income | Unstable when net income is near zero |
| Free cash flow conversion | (CFO - capital expenditures) / EBITDA | Include capitalized software and capitalized contract costs in capital expenditures when they are paid in investing activities |
| Adjusted EBITDA cash gap | Adjusted EBITDA - (CFO + cash interest + cash taxes) | Shows how much of the adjusted figure never arrives as cash |

Rules: compute on the same period basis (fiscal year or LTM) for numerator and denominator; show at least two periods; explain any period below 100 percent of EBITDA by naming the drivers (working capital build, cash interest and taxes, payments for items added back, capitalized costs). CFO raised by receivables factoring, supplier finance programs, payables stretched past terms or the timing of tax payments is labeled as such. "Free cash flow" has no uniform definition; give the formula wherever the term is used (SEC staff CFI 102.07).

## 3. Working capital days

| Measure | Default formula | Alternatives (state if used) |
|---|---|---|
| DSO | Ending gross trade receivables / revenue x 365 | Average receivables; credit sales only; quarterly x 91.25 |
| DIO | Ending inventory / cost of goods sold x 365 | Average inventory |
| DPO | Ending trade payables / cost of goods sold x 365 | Purchases as the denominator |

Compare growth in receivables and inventory with growth in revenue and cost of goods sold. Receivables or inventory growing materially faster than sales is the pattern Beneish's DSRI captures and the most common sign of pulled-forward or channel-loaded sales; it can also come from a credit-terms change, a large customer or an acquisition. Obtain the aging (current, 31-60, 61-90, over 90 days) and the allowance at each date, the subsequent-period cash receipts, credit memos and returns, and any change in customer payment terms.

## 4. Beneish (1999) M-score

Source: M. D. Beneish, "The Detection of Earnings Manipulation," Financial Analysts Journal 55(5), 1999, pp. 24-36 (Table 2 definitions; Table 3 unweighted probit estimates). Year t is the year under test; t-1 the prior year. All eight variables need two consecutive fiscal years.

| Variable | Definition | Coefficient |
|---|---|---|
| Constant | | -4.840 |
| DSRI | (Receivables t / Sales t) / (Receivables t-1 / Sales t-1) | +0.920 |
| GMI | Gross margin t-1 / Gross margin t, where gross margin = (Sales - COGS) / Sales | +0.528 |
| AQI | [1 - (Current assets t + net PP&E t) / Total assets t] / [same for t-1] | +0.404 |
| SGI | Sales t / Sales t-1 | +0.892 |
| DEPI | Depreciation rate t-1 / Depreciation rate t, where rate = Depreciation / (Depreciation + net PP&E) | +0.115 |
| SGAI | (SG&A t / Sales t) / (SG&A t-1 / Sales t-1) | -0.172 |
| TATA | [(change in current assets - change in cash) - (change in current liabilities - change in current maturities of long-term debt - change in income tax payable) - depreciation and amortization] / Total assets t | +4.679 |
| LVGI | [(Long-term debt t + Current liabilities t) / Total assets t] / [same for t-1] | -0.327 |

M = -4.840 + 0.920 DSRI + 0.528 GMI + 0.404 AQI + 0.892 SGI + 0.115 DEPI - 0.172 SGAI + 4.679 TATA - 0.327 LVGI.

**Cutoff.** The score is a probit index; the probability of manipulation is the standard normal CDF of M. Beneish reports that at relative error costs of 20:1 or 30:1 the model classifies a firm as a manipulator when the estimated probability exceeds 0.0376, "a score greater than -1.78" (at 10:1, 0.0685 and -1.49). In his estimation sample this cutoff misclassified 26 percent of manipulators and 13.8 percent of non-manipulators; in the holdout sample, 50 percent and 7.2 percent. Use -1.78 with these eight coefficients. A figure of -2.22 circulates in secondary sources, usually tied to a five-variable version; it does not appear in the 1999 paper and must not be applied to the eight-variable score.

**Read-out labels.** "Above -1.78 (screen flag)" or "At or below -1.78 (no screen flag)". Report M to two decimals, the probability, each variable's value and its weighted contribution, and which variables drive the result. A flag means "investigate the drivers"; no flag does not clear the company. The model was built from 74 manipulators and industry-matched controls over 1982-1992 (estimation 1982-1988, holdout 1989-1992), with financial institutions excluded; say so when the target is a bank, insurer or other financial company, a start-up, or a company with a large acquisition in year t (AQI, SGI and DSRI distort).

## 5. Reserve and allowance rollforward tests

For each reserve (allowance for credit losses, sales returns, warranty, inventory obsolescence, rebates, self-insurance, restructuring): beginning balance + provision - utilizations or write-offs +/- other = ending balance, by year. Flags: provision falls or turns into a credit while the underlying risk rises (aging over 90 days up, warranty claims up, slow-moving inventory up); coverage ratio (reserve / gross base) falls; a release lands in the quarter a target was missed; releases are not disclosed as changes in estimate. Quantify the margin effect: EBITDA with the release removed, and EBITDA at the prior year's coverage ratio. A release can be correct; the deliverable states what evidence would support it.

## 6. Capitalized cost tests

- **Internal-use software (ASC 350-40).** Capitalization rate = costs capitalized / total development spend (expensed plus capitalized), by period. A rising rate raises EBITDA one for one because amortization sits below EBITDA. Compute EBITDA at the prior period's rate as a sensitivity and request the capitalization policy and project documentation. ASU 2025-06 removes the project-stage model; capitalization begins when management has authorized and committed to funding and completion is probable. It is effective for annual periods beginning after December 15, 2027 (early adoption permitted), so a change in rate around adoption may be a policy change rather than a change in activity; say which period applies which rule.
- **Costs to obtain a contract (ASC 340-40-25-1 to 25-4).** Incremental costs such as commissions are capitalized if expected to be recovered; the practical expedient allows expensing when the amortization period would be one year or less. A switch from the expedient to capitalization, or longer amortization periods, lifts EBITDA.
- **Costs to fulfill a contract (ASC 340-40-25-5).** Capitalized only if all three criteria are met; costs within another Topic (inventory, internal-use software, PP&E) follow that Topic.
- In cash conversion, deduct capitalized amounts paid in investing activities.

## 7. Revenue-side red flag tests

- **Channel stuffing and pull-forwards.** Quarter-end shipment spikes, distributor inventory weeks rising, extended payment terms or extra discounts at quarter end, high returns or credit memos in the next period, DSO and DIO rising faster than sales.
- **Bill-and-hold.** Revenue on goods still in the seller's possession requires all four criteria of ASC 606-10-55-83: substantive reason (for example, the customer requested it), product identified separately as the customer's, ready for physical transfer, and the seller cannot use it or direct it to another customer. The earnings quality review lists the evidence for each criterion and quantifies the revenue and gross profit at stake; the recognition conclusion goes to the revenue recognition workflow.
- **Related-party revenue and intersegment pricing.** ASC 850-10-50-5: related party transactions cannot be presumed to be at arm's length. For SEC registrants, Regulation S-X 4-08(k) requires related party amounts on the face of the statements. Quantify revenue and margin with related parties, compare pricing and terms with third-party sales, and remove or flag above-market margin in normalized earnings.

## 8. One-time gains and classification tests

List every gain inside operating income (sale of assets or businesses, insurance recoveries above book value, litigation awards, remeasurement gains, contingent consideration reversals, bargain purchase gains) and every charge added back. Adjusted earnings that add back charges but keep gains of the same kind are one-sided (SEC staff CFI 100.03). Test whether items moved between operating and non-operating lines between periods.

## 9. Common computation errors

| Error | Effect |
|---|---|
| Beneish GMI or DEPI inverted (t over t-1) | Sign of the signal reversed for that variable |
| SGAI or LVGI given positive coefficients | Score overstated when SG&A or leverage rises |
| TATA scaled by average assets or replaced by (net income - CFO) without saying so | Not the 1999 definition; label it |
| -2.22 cutoff applied to the eight-variable score | Flags firms the 1999 cutoff would not |
| DSO on net receivables in one year and gross in another | Trend distorted by allowance changes |
| Cash conversion on adjusted EBITDA in one period and reported in another | Trend not comparable |
| Sloan accruals scaled by ending assets | Not Sloan's definition; label it |
