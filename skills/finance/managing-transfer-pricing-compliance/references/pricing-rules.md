# Pricing Rules: Methods, Comparability, Range and Transaction Types

U.S. rules are Treas. Reg. 1.482-1 through 1.482-9 under IRC 482, read in full on October 30, 2026. OECD paragraph numbers are from the OECD Transfer Pricing Guidelines (January 2022 edition, with the Amount B annex to Chapter IV added February 19, 2024). Foreign local rules are never assumed to match either; mark them [VERIFY] by jurisdiction.

## Contents

1. Arm's length standard and best method rule
2. Comparability and the functional analysis
3. Tested party and profit level indicator
4. Arm's length range, interquartile range and the adjustment point
5. Data years and loss-making comparables
6. Taxpayer-initiated adjustments, secondary adjustments and blocked income
7. Services
8. Intangibles, DEMPE, IRC 367(d) and cost sharing
9. Intercompany loans and guarantees
10. OECD points that differ from the U.S. regulations

## 1. Arm's length standard and best method rule

- IRC 482 lets the IRS allocate income among commonly controlled businesses to prevent evasion or clearly reflect income. For a transfer or license of intangible property (as defined in IRC 367(d)(4)), the income must be commensurate with the income attributable to the intangible; the IRS may value on an aggregate basis or on realistic alternatives.
- Best method rule, 1.482-1(c): the method that gives the most reliable measure of an arm's length result under the facts; no strict priority; a method may be used without proving others inapplicable, but a more reliable method shown later must be used. The two primary factors are the degree of comparability and the quality of the data and assumptions.
- Specified methods: tangible goods, 1.482-3 (CUP, resale price, cost plus, CPM, profit split); intangibles, 1.482-4 (CUT, CPM, profit split, unspecified); services, 1.482-9 (services cost method, CUSP, gross services margin, cost of services plus, CPM, profit split); loans, 1.482-2(a); cost sharing, 1.482-7.
- Penalty link: only a specified method, reasonably selected and applied, can exclude an adjustment from the net adjustment penalty under 1.6662-6(d)(2); an unspecified method has its own test at 1.6662-6(d)(3).

## 2. Comparability and the functional analysis

- Factors, 1.482-1(d)(1): functions, contractual terms, risks, economic conditions, property or services. Material differences must be adjusted for when their effect can be measured; otherwise reliability falls. Unadjusted industry averages cannot establish an arm's length result (1.482-1(d)(2)).
- Contractual terms, 1.482-1(d)(3)(ii)(B): written terms agreed before the transactions are respected only if consistent with economic substance; greatest weight goes to the parties' actual conduct, and inconsistent terms may be disregarded and replaced with imputed terms. With no written agreement, terms are imputed from conduct.
- OECD Chapter I risk framework (para. 1.60): identify economically significant risks; read the contract; find who performs control and risk-mitigation functions and has financial capacity; test whether conduct follows the contract; allocate the risk to the party that controls it and has capacity; price the delineated transaction.
- Record the FAR (functions, assets, risks) for both parties before choosing a method; entity labels (limited-risk distributor, contract manufacturer, entrepreneur) follow the FAR, never the reverse.

## 3. Tested party and profit level indicator

- 1.482-5(b)(2)(i): the tested party is the participant whose operating profit can be verified with the most reliable data and fewest, most reliable adjustments, and for which reliable comparables exist; in most cases the least complex party that does not own valuable intangibles or unique assets. OECD para. 3.18: the tested party should be consistent with the functional analysis and will most often be the one with the less complex functional analysis.
- A foreign affiliate can be the tested party if its accounts can be verified and adjusted to the same standards.
- PLIs, 1.482-5(b)(4): rate of return on capital employed; financial ratios (operating profit to sales; gross profit to operating expenses, often called the Berry ratio); other PLIs, such as operating profit to total costs (net cost plus) for a contract manufacturer, if they reliably measure arm's length income ((b)(4)(iii)). One PLI per range. Multi-year data is the CPM default: 1.482-5(b)(4) says PLIs should be derived from enough years to measure returns reliably and that the period generally should encompass at least the taxable year under review and the two preceding taxable years; 1.482-1(f)(2)(iii)(A) ordinarily requires the tested party's results for the same years. A single-year test is a policy election that needs a stated reason (for example, the tested party's first year of operation).

## 4. Arm's length range, interquartile range and the adjustment point

- 1.482-1(e)(1): a taxpayer whose result falls within the arm's length range is not adjusted.
- 1.482-1(e)(2)(iii)(A): the full range of all comparables is used only when information is complete enough that all material differences are identified and adjusted for. Otherwise (the usual case for CPM with database comparables), 1.482-1(e)(2)(iii)(B) applies and the range is narrowed by a valid statistical method; the interquartile range ordinarily serves.
- Interquartile range, 1.482-1(e)(2)(iii)(C), computed this way and no other:
  1. Sort the n results in ascending order.
  2. The 25th percentile is the lowest result such that at least 25 percent of results are at or below it.
  3. If exactly 25 percent of results are at or below a result (n divisible by 4), the 25th percentile is the average of that result and the next higher one.
  4. The 75th percentile is found the same way; the median (50th percentile) the same way under 1.482-1(e)(3).
  Spreadsheet QUARTILE, QUARTILE.INC, PERCENTILE and QUARTILE.EXC interpolate and can give different figures; show the regulation figure and note any difference. Worked check: for 12 results, the 25th percentile is the average of the 3rd and 4th, the median the average of the 6th and 7th, the 75th percentile the average of the 9th and 10th. For 10 results: 3rd, average of 5th and 6th, 8th. For 7 results: 2nd, 4th, 6th.
- 1.482-1(e)(3): if the result falls outside the range, the IRS may adjust to any point in the range; where the interquartile range is used, ordinarily to the median; otherwise ordinarily to the arithmetic mean. Quantify both the move to the nearest quartile and the move to the median; the gap between them is the exposure a taxpayer accepts by stopping at the quartile.
- 1.6662-6(d)(2)(ii)(A)(5): arbitrarily choosing an extreme point of the range weighs against reasonableness for penalty protection.
- A result inside the full range but outside the interquartile range is outside the arm's length range when (e)(2)(iii)(B) applies.

## 5. Data years and loss-making comparables

- 1.482-1(f)(2)(iii)(A) starts from the taxable year under review, but (f)(2)(iii)(B) says multi-year data must ordinarily be considered for CPM (1.482-5) and is ordinarily not used for CUP or CUSP. For CPM the three-year period in section 3 is therefore the default, with the tested party's data for the same years. Check every comparable's fiscal year end; mismatched or stale years (a prior year's search rolled forward without an update) are a defect, not a convenience.
- 1.6662-6(d)(2)(ii)(A)(2): use the most current reliable data available before the end of the taxable year; data obtained after year-end but before filing is kept as principal document (9).
- 1.482-1(f)(2)(iii)(C): persistent losses among controlled taxpayers may indicate non-arm's length pricing.
- OECD paras. 3.64 and 3.65: no overriding rule includes or excludes loss-makers; a loss should trigger investigation; exclude where losses do not reflect normal business conditions or reflect risks not comparable to the tested party's; do not reject a comparable on the sole basis of a loss. Para. 3.66: investigate abnormally high profits the same way. Record a reason for every accept or reject; show the range with and without disputed comparables when the decision changes the answer.

## 6. Taxpayer-initiated adjustments, secondary adjustments and blocked income

- 1.482-1(a)(3): a taxpayer may report on a timely filed return (including extensions) results based on prices different from those charged, to reflect an arm's length result. No untimely or amended return may decrease taxable income based on such adjustments.
- OECD paras. 3.69 to 3.71 and 4.38: price-setting and outcome-testing approaches both exist; compensating adjustments are not accepted everywhere, so a true-up can produce double taxation. Confirm the counterparty jurisdiction's rule [VERIFY].
- Secondary adjustments: after a primary 482 adjustment, the cash that the books did not move would otherwise be a secondary adjustment (for example, a deemed dividend or capital contribution). Under Rev. Proc. 99-32 (issued under 1.482-1(g)(3)) a U.S. taxpayer may instead set up an interest-bearing account receivable or payable equal to the primary adjustment and repatriate it free of those secondary consequences. For a taxpayer-initiated adjustment under 1.482-1(a)(3), elect by a statement filed with the return and pay the account within 90 days of filing; for an IRS-initiated adjustment, through a closing agreement with payment within 90 days of its execution. Offsets for bona fide debts, distributions and capital contributions are allowed only within the stated years.
- Blocked income, 1.482-1(h)(2): a foreign legal restriction counts only if publicly promulgated and generally applicable, remedies for a waiver were exhausted, it expressly prevented payment in any form, and the parties did not circumvent it; otherwise the deferred income method may be elected on a timely return (or an amended return filed before the IRS first contacts the group about the year). In 3M Co. v. Commissioner, 154 F.4th 574 (8th Cir. Oct. 1, 2025), the court held the IRS could not allocate to 3M royalties Brazilian law barred it from receiving, reversing the Tax Court's reliance on the regulation after Loper Bright. Rehearing was denied, and the Supreme Court extended the government's certiorari deadline to June 19, 2026 (No. 25A1233). Whether the rule binds outside the Eighth Circuit, and the case's later history, are [VERIFY]; analyze both the regulation's reading and the 3M reading.
- A true-up changes the price of goods already imported and services already invoiced: customs value, VAT or GST, withholding tax and the books of both entities. IRC 1059A caps the basis or inventory cost of property imported from a related person at the costs taken into account for customs value. Route the customs and VAT work to managing-indirect-tax-analysis.

## 7. Services

- Services cost method (1.482-9(b)): cost with no markup is the best method only if (i) the service is a specified covered service (by revenue procedure) or a low margin covered service (median comparable markup at or below 7 percent), (ii) it is not an excluded activity (manufacturing, production, natural resources, construction, distribution or agency, R&D, engineering or scientific, financial transactions including guarantees, insurance), (iii) the taxpayer reasonably concludes in its business judgment that it does not contribute significantly to key competitive advantages, core capabilities or fundamental risks of success or failure, and (iv) books and records include a statement of intent to apply the method.
- Benefit test, 1.482-9(l)(3): no charge for activities with indirect or remote benefit, duplicative activities, shareholder activities, or passive association.
- BEAT link, IRC 59A(d)(5): an amount paid for services is excepted from base erosion payments if the services meet the services cost method eligibility requirements (ignoring the business judgment rule) and the amount constitutes the total services cost with no markup component. How a marked-up fee is split between cost and markup is in Treas. Reg. 1.59A-3 [VERIFY]; the markup itself is never excepted. BEAT rate 10.5 percent for taxable years beginning after Dec. 31, 2025 (IRC 59A(b)(1)(A)). Route BEAT computation to analyzing-international-tax-planning.
- The OECD Chapter VII revision is a consultation draft (June 1, 2026), not adopted guidance.

## 8. Intangibles, DEMPE, IRC 367(d) and cost sharing

- 1.482-4(f)(3): the legal owner is treated as sole owner unless ownership is inconsistent with economic substance. 1.482-4(f)(2): consideration may be adjusted periodically to stay commensurate with income, even if the year of transfer is closed, subject to the exceptions in (f)(2)(ii).
- OECD paras. 6.32, 6.42, 6.56 and 6.71: legal ownership alone confers no right to retain intangible returns; members performing and controlling development, enhancement, maintenance, protection and exploitation (DEMPE) functions, providing assets and assuming risks must be paid for them. Build a DEMPE table: function, entity performing it, entity controlling it, people and location, funding.
- IRC 367(d): a U.S. person's transfer of intangible property to a foreign corporation in a section 351 or 361 exchange is treated as a sale for contingent payments over the useful life, with annual ordinary income inclusions commensurate with income. IRC 367(d)(4) includes goodwill, going concern value, workforce in place, customer lists and contracts. A contribution of intangibles to a foreign subsidiary is therefore never "no transfer pricing event". Computation and structure route to analyzing-international-tax-planning.
- Cost sharing (1.482-7): a CSA needs a contemporaneous written contract (k)(1), documentation (k)(2), accounting (k)(3) and a CSA Statement filed by each participant (k)(4); platform contributions require a platform contribution transaction payment.

## 9. Intercompany loans and guarantees

- 1.482-2(a)(1)(ii)(B): the interest rules apply only to bona fide debt; an alleged loan that is in substance equity is not repriced, it is recharacterized.
- Safe haven, 1.482-2(a)(2)(iii)(B): a stated rate from 100 percent to 130 percent of the applicable federal rate (AFR) is treated as arm's length. Below 100 percent (or no interest), (B)(2) sets the rate at 100 percent of the AFR compounded semiannually. Above 130 percent, (B)(3) sets it at 130 percent compounded semiannually unless the taxpayer establishes a more appropriate compound rate under (a)(2)(i); that phrase belongs to the upper limit only. The escape for both directions is the separate "However" sentence in (B)(3): a compound rate charged above the upper limit but below the (a)(2)(i) rate, or below the lower limit but above the (a)(2)(i) rate, is deemed arm's length.
- AFR term, (a)(2)(iii)(C): short-term for 3 years or less; mid-term over 3 and up to 9 years; long-term over 9 years; in effect on the date the loan is made. Demand loans use the short-term rate for each day outstanding.
- The safe haven does not apply when: the lender is regularly in the business of lending to unrelated parties ((a)(2)(iii)(D)); principal or interest is in a currency other than U.S. dollars ((a)(2)(iii)(E)); the loan proceeds were borrowed by the lender at the borrower's situs ((a)(2)(ii)); or the term loan predates May 9, 1986. In those cases price under (a)(2)(i): amount, duration, security, credit standing of the borrower, and the prevailing rate for comparable loans between unrelated parties.
- Guarantees: a financial guarantee is an excluded activity for the services cost method (1.482-9(b)(4)(viii)), so it cannot be charged at cost under that method. Under OECD Chapter X Section D (paras. 10.154 onward), first separate the benefit of implicit support from group membership (passive association, para. 10.156; compare 1.482-9(l)(3)(v)) from the explicit, legally binding guarantee (para. 10.163); a letter of comfort assumes no explicit risk. The yield approach (paras. 10.174 and 10.175) prices the interest spread the explicit guarantee adds, net of implicit support. No guarantee fee is due where the borrower gets no benefit beyond passive association; a fee is expected where an explicit guarantee lowers its rate or raises its borrowing capacity. U.S. treatment of guarantee fees beyond these points is [VERIFY].
- The safe haven settles only the U.S. rate. The borrower's country applies its own rules and the OECD Chapter X guidance (accurate delineation, borrower credit rating, para. 10.88 onward) [VERIFY by jurisdiction].

## 10. OECD points that differ from the U.S. regulations

- Point in range: OECD para. 3.62 permits any point where comparables are equally reliable and suggests central tendency where defects remain; U.S. 1.482-1(e)(3) adjusts ordinarily to the median of the interquartile range.
- Ownership: U.S. starts from legal ownership tested against economic substance; OECD starts from DEMPE contributions. Present both readings where they diverge.
- Amount B (Annex to Chapter IV): simplified pricing for qualifying baseline distribution. Notice 2025-04 lets U.S. taxpayers rely on it for taxable years beginning on or after Jan. 1, 2025, before proposed regulations (agenda RIN 1545-BR72, NPRM projected November 2026 [VERIFY]). Whether the counterparty jurisdiction applies Amount B is [VERIFY].
- Pillar Two: GloBE Model Rules (Dec. 2021) Article 3.2.3 requires cross-border transactions between constituent entities to be recorded in the same amount in both entities' accounts and consistent with the arm's length principle; late true-ups can therefore change GloBE income. The January 5, 2026 side-by-side package changed safe harbours for groups with eligible parents. Route all GloBE computations to analyzing-international-tax-planning.
