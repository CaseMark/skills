# Reserving Methods and Diagnostics

Mechanics and selection rules for property and casualty unpaid claim estimates. Citations are to `references/primary-sources.md`. Figures in this file illustrate formulas; they are not benchmarks.

## Contents

1. Data checks and the three dates
2. Age-to-age factor selection
3. Tail factor
4. Development (chain ladder) method
5. Expected claims and Bornhuetter-Ferguson
6. Cape Cod
7. Case reserve and settlement changes (Berquist-Sherman)
8. Reconciling paid and incurred indications
9. Loss trend, including social inflation
10. Loss adjustment expense: DCC and AO
11. Salvage, subrogation and deductibles
12. Reinsurance: gross, ceded, net and collectibility
13. Selected estimate and range of reasonable estimates
14. Assumption labels

## 1. Data checks and the three dates

- Record the accounting date (separates paid from unpaid), the valuation date (data cut-off) and the review date (information cut-off), as ASOP No. 43 section 4.1(d) requires them in the communication.
- Basis of every triangle: paid or reported (case incurred); cumulative or incremental; gross, ceded or net; with or without DCC; net or gross of salvage and subrogation received; accident, policy, report or underwriting year; units.
- Tie the latest diagonal to Schedule P Part 1 by line (and to Parts 2 and 3 for the history), or to the general ledger for a GAAP-only entity. The Actuarial Report must show the data used was neither created nor destroyed (2026 ASI, Actuarial Opinion paragraph 7.C).
- Identify large losses, catastrophe events, commutations, pooling changes, retroactive reinsurance (excluded from Schedule P) and line remapping before computing any factor.

## 2. Age-to-age factor selection

- Compute link ratios for every interval; show all-year and recent-year simple and volume-weighted averages and the medial average (excluding high and low).
- Immature or volatile years: a factor resting on one or two accident years, a factor driven by one large claim, or the latest diagonal after a known operational change is not a basis for selection by itself. Name the years excluded and why, or adjust the data (Section 7).
- Read the diagonal, not only the columns. A step change down one calendar-year diagonal across several ages is a calendar-year effect (case strengthening, a new claims system, a settlement initiative, a law change), not a change in the development pattern.
- Development assumes consistent claim processing, a stable mix of claims, stable policy limits and stable reinsurance retentions (Friedland, Chapter 7, key assumptions). State which assumption the data violates.
- Every selected factor carries an assumption label (Section 14).

## 3. Tail factor

- A tail is needed whenever development continues past the last age in the triangle: the last observed factors exceed 1.000, claims remain open at the last age, or the line is long-tailed (workers compensation, medical professional liability, general and auto liability). A tail of 1.000 is an assumption that must be supported like any other.
- The tail multiplies every accident year's cumulative factor, so it is leveraged across the whole reserve (Friedland, Chapter 7, citing Thorne's review of Berquist and Sherman).
- Support, in order of preference: the entity's own older data (a longer triangle, Schedule P prior row, claim-level open counts), a curve fitted to the observed factors, then a cited industry benchmark marked as an unverified external lookup until its source is in the file.
- Exponential decay fit: let d_k = factor_k - 1 for the last n observed intervals and r = (d_last / d_first)^(1/(n-1)). Tail = product over k = 1, 2, ... of (1 + d_last x r^k). Show r, the tail and the dollar effect; test one higher and one lower tail.
- Lines with heavy subrogation can develop below 1.000 late (factors approach 1.000 from below); do not force a tail above 1.000 there.

## 4. Development (chain ladder) method

- Cumulative development factor at age j: CDF_j = product of selected age-to-age factors from j to the last age, times the tail.
- Ultimate = latest cumulative value x CDF at its age. Indicated IBNR (reported basis) = ultimate - reported; indicated unpaid (paid basis) = ultimate - paid. Unpaid = case + IBNR, where this skill's IBNR includes development on known claims ("bulk") unless the stated basis separates them.
- Percent unreported or unpaid at age j = 1 - 1/CDF_j.
- Weakness: highly leveraged for immature years, so a small change in early reported losses moves the ultimate a lot (Friedland, Chapter 9).

## 5. Expected claims and Bornhuetter-Ferguson

- Expected claims = a priori expected loss ratio (ELR) x on-level earned premium (or a pure premium x exposure).
- Bornhuetter-Ferguson IBNR = expected claims x (1 - 1/CDF); B-F ultimate = actual reported (or paid) + that amount. Bornhuetter and Ferguson (PCAS 1972) define the IBNR factor as 1.000 - 1.000/loss development factor. The key assumption is that unreported claims develop on expected claims, not on reported claims to date (Friedland, Chapter 9).
- The ELR must be independent of the result being tested. Acceptable sources, each documented: on-level, trended ultimate loss ratios of mature accident years from the development method; a pricing indication with its own derivation; a cited industry benchmark for a new line. A business plan, budget, board target or management expectation is not an independent source: it assumes the answer, and an expected claims method "implicitly relies on the accuracy of policy pricing and underwriting" (Friedland, Chapter 8). A plan ELR may appear only as a labeled sensitivity.
- Use the same expected claims for the paid and reported B-F (Friedland, Chapter 9).

## 6. Cape Cod

- Used-up premium for each year = on-level earned premium / CDF (premium matching the claims expected to be reported by the valuation date).
- Cape Cod ELR = sum of reported claims / sum of used-up premium, over the years included (Friedland, Chapter 10; Stanard, PCAS 1985, method 3, "adjustment to total known losses").
- Cape Cod IBNR for each year = Cape Cod ELR x on-level earned premium x (1 - 1/CDF). Trend and on-level adjustments, when used, are applied before the sum.
- Cape Cod derives the ELR from the entity's own data, so it is the natural independent cross-check on a B-F ELR.

## 7. Case reserve and settlement changes (Berquist-Sherman)

- Reported development assumes no significant change in case reserve adequacy; paid development assumes no significant change in the speed of closure and payment (Friedland, Chapter 7). Berquist and Sherman (PCAS 1977) treat both by data adjustment once the change is detected.
- Diagnostics: ratio of paid to reported by age; average case reserve per open claim by age, compared across diagonals after trend; closed-with-payment to reported counts (disposal rates); claims department memos on reserving philosophy, systems or staffing.
- Case strengthening on one diagonal raises that diagonal's reported values and its age-to-age factors. Averaging those factors and applying them to the strengthened diagonal counts the strengthening twice. Strengthening by itself moves amounts from IBNR into case; it does not raise the ultimate.
- Adjustments: restate the latest diagonal's case reserves to the historical adequacy level (or restate history to the current level by trended average case reserves) and recompute factors; rely more on paid methods if settlement rates are stable; disclose the adjustment as a change in method.
- A settlement speed-up distorts paid factors the same way; restate paid by disposal rates or rely on reported methods if case adequacy is stable.

## 8. Reconciling paid and incurred indications

- Show paid and reported indications side by side by accident year with the difference in dollars and percent.
- Explain each material difference by a named cause (case adequacy change, settlement change, large loss, reopened claims, data error) before weighting. An unexplained difference is an open item, not a reason to average.
- State the weight given to each method by year and why (maturity, data change, leverage). ASOP No. 43 section 3.6.1 asks for multiple methods or a disclosed reason for one.

## 9. Loss trend, including social inflation

- Statutory liabilities are based on the estimated ultimate cost "including the effects of inflation and other societal and economic factors" (SSAP No. 55); ASOP No. 43 sections 3.6.6 and 3.6.7 require the actuary to consider external and changing conditions.
- Trend an older year's ultimate loss ratio to a target year's cost level: ELR_target = ULR_year x (1 + t)^(target year - year), with premium already on-level. State t, its source (a claims trend study, closed-claim severities) and whether it includes social inflation (verdict severity, litigation rates, attorney representation).
- Where severity has shifted recently, factors and tails selected from older years may understate late development; run a sensitivity and report the dollar effect.

## 10. Loss adjustment expense: DCC and AO

- DCC (defense, litigation and medical cost containment, internal or external) is reported with losses in Schedule P Parts 2 to 4 and usually projected with losses or on its own triangle.
- AO (adjusters, settling agents, coverage-determination attorney fees including litigation with the policyholder, and extra-contractual and bad-faith lawsuit costs) is estimated separately, for example by a paid-AO-to-paid-loss ratio applied to a share of case reserves and all of IBNR (Friedland, Chapter 17).
- Misclassification moves amounts between the DCC triangle and AO and distorts both projections. Test classification against the SSAP No. 55 lists in `references/statutory-and-gaap-rules.md` Section 5.

## 11. Salvage, subrogation and deductibles

- Record whether paid data are net of salvage and subrogation received. A projection of paid data net of recoveries produces an ultimate net of all recoveries, received and future; deducting anticipated salvage and subrogation again counts it twice.
- Anticipated salvage and subrogation deducted from carried reserves is reported in Schedule P Part 1 and Exhibit B item 8 of the SAO; impaired recoverables may not reduce reserves (SSAP No. 55).
- High-deductible business: reserves are net of the deductible, with no credit for amounts due from the insured that are uncollectible (SSAP No. 65).

## 12. Reinsurance: gross, ceded, net and collectibility

- Keep gross, ceded and net consistent; net estimates derived by applying net-to-gross ratios must respect treaty terms (quota share, excess of loss, aggregate stop loss) by year (Friedland, Chapter 14).
- Collectibility: if the estimate is net of material recoverables, consider collectibility (ASOP No. 36 section 3.6; ASOP No. 43 section 3.3(c)). Gather management's knowledge of disputes, reinsurer ratings, Schedule F items such as paid recoverables over 90 days past due, and regulatory actions against reinsurers (2026 ASI, relevant comment D). Show the net estimate with and without doubtful recoverables.
- The statutory provision for reinsurance on Schedule F and the netting of ceded reserves are different mechanisms; name which one the user is asking about.

## 13. Selected estimate and range of reasonable estimates

- The selected (point) estimate is a judgment across methods by year, not an average by default. State its intended measure (for example an actuarial central estimate) per ASOP No. 43 section 3.3(a).
- A range of reasonable estimates is a range of estimates each reasonable on its own; disclose the basis of the range (ASOP No. 43 section 4.2(a)). It is not a confidence interval unless built as one.
- The carried reserve is compared with both the range and the point; the labels and their tests are in `references/output-template.md` Section 7. A carried amount below the point but inside the range is not deficient.

## 14. Assumption labels

Each factor, tail, ELR, trend and weight in the assumption register takes one label:
- **Supported**: derived from the entity's data or a cited source by a stated method, and consistent with the diagnostics.
- **Judgmental**: chosen by stated judgment inside the span of the data-derived indications, with the reason written down.
- **Unsupported**: no derivation; outside the indications without a reason; resting on immature or distorted data without adjustment; or taken from a business plan, budget or target.
