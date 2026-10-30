# U.S. International Tax Rules by Taxable Year

U.S. federal income tax rules for outbound and inbound structures, with each rate and threshold tied to the taxable year it governs. Statutory text was read as current on October 30, 2026 (see `primary-sources.md` for URLs and methods). Pub. L. 119-21 (July 4, 2025) rewrote much of this area for taxable years beginning after December 31, 2025; proposed regulations issued in August and September 2026 are not final. This file supports a draft analysis; it is not tax advice. Anything a row marks [VERIFY] stays open until a tax adviser confirms it.

## Contents

1. Choosing the rule set: whose taxable year controls
2. Rate and threshold table by taxable year
3. Net CFC tested income (section 951A)
4. Subpart F, section 954(c)(6), high-tax elections and ownership rules
5. Foreign tax credit: baskets, deemed-paid credit, expense allocation
6. FDDEI (section 250(b))
7. Section 245A dividends, holding period and hybrid dividends
8. Entity classification and hybrid rules
9. Outbound transfers: section 367 and cost sharing structure
10. Inbound: BEAT, withholding, portfolio interest, FIRPTA, partnerships, corporate AMT, intercompany loans
11. Computation order for an NCTI year

## 1. Choosing the rule set: whose taxable year controls

| Change | Effective for | Whose year | Source |
|---|---|---|---|
| Section 250 rates 40% (NCTI) and 33.34% (FDDEI) | Taxable years beginning after Dec. 31, 2025 | The domestic corporation claiming the deduction | Pub. L. 119-21 sec. 70321(b) |
| NCTI replaces GILTI; QBAI and net deemed tangible income return removed; FDDEI replaces FDII; DTIR removed | Taxable years beginning after Dec. 31, 2025 | The U.S. shareholder (Treasury's reading in proposed Treas. Reg. 1.951A-7(c), REG-115646-25, 91 Fed. Reg. 55037, Aug. 26, 2026) | Sec. 70323(c) |
| Section 960(d) deemed-paid 90% and section 78 gross-up change | Taxable years beginning after Dec. 31, 2025 | Taxpayer claiming the credit | Sec. 70312(c)(1) |
| 10% FTC disallowance on PTEP from 951A inclusions (960(d)(4)) | Foreign taxes on 959(a) amounts attributable to 951A inclusions after June 28, 2025 (proposed rule: inclusion in a U.S. shareholder year ending after June 28, 2025) | U.S. shareholder | Sec. 70312(c)(2); Notice 2025-77; REG-115145-25 |
| Expense allocation to the NCTI basket (904(b)(5)); inventory sourcing for foreign branches (904(b)(6)) | Taxable years beginning after Dec. 31, 2025 | Taxpayer | Secs. 70311(c), 70313(b) |
| DEI excludes income and gain from dispositions of intangibles and depreciable, amortizable or depletable property (250(b)(3)(A)(i)(VII)) | Sales or other dispositions after June 16, 2025, including in years beginning before 2026 | Domestic corporation | Sec. 70322(a)(3); Notice 2025-78 |
| DEI expense allocation excludes interest and R&E (250(b)(3)(A)(ii)) | Taxable years beginning after Dec. 31, 2025 | Domestic corporation | Sec. 70322(b)(2) |
| BEAT 10.5% | Taxable years beginning after Dec. 31, 2025 | Applicable taxpayer | Sec. 70331(d) |
| 954(c)(6) look-through made permanent | Taxable years of foreign corporations beginning after Dec. 31, 2025 (the prior extension ran through years beginning before Jan. 1, 2026, so no gap) | Foreign corporation | Sec. 70351(b) |
| One-month deferral election (898(c)(2)) repealed | Taxable years of specified foreign corporations beginning after Nov. 30, 2025, with a transition short year | Foreign corporation | Sec. 70352(b), (c) |
| 958(b)(4) restored (no downward attribution from foreign persons); new section 951B | Taxable years of foreign corporations beginning after Dec. 31, 2025 | Foreign corporation | Sec. 70353 |
| Pro rata share by period of ownership (951(a)(2), 951A(c)) | Taxable years of foreign corporations beginning after Dec. 31, 2025; dividend transition rule for years including June 28, 2025 | Foreign corporation | Sec. 70354(c); Notice 2025-75; REG-115646-25 |

Rule: a year is classified by the date it **begins**, never by the year it ends or the year the return is filed. A U.S. shareholder whose taxable year begins July 1, 2025 applies former section 951A (GILTI with QBAI) and the 50% / 37.5% section 250 rates for that whole year, even for a CFC year that begins after December 31, 2025 (proposed Treas. Reg. 1.951A-7(c)); its pro rata shares of that CFC's tested items follow amended section 951(a)(2).

## 2. Rate and threshold table by taxable year

| Item | Taxable years beginning in 2018-2025 | Taxable years beginning after Dec. 31, 2025 |
|---|---|---|
| Corporate rate (IRC 11(b)) | 21% | 21% |
| Section 250 deduction on GILTI / NCTI plus related 78 gross-up | 50% | 40% |
| U.S. rate on GILTI / NCTI before credits | 10.5% | 12.6% |
| Section 250 deduction on FDII / FDDEI | 37.5% | 33.34% |
| U.S. rate on FDII / FDDEI | 13.125% | 13.99986% (about 14.0%) |
| QBAI return deducted from tested income | 10% of QBAI less specified interest expense | None |
| Section 960(d) deemed-paid share of tested foreign income taxes | 80% | 90% |
| Section 78 gross-up of 960(d) taxes | 100% (inclusion percentage times tested foreign income taxes) | 100% (computed "without regard to the phrase 90 percent of") |
| Foreign tax rate at which the NCTI or GILTI residual is zero, before expense allocation | 13.125% | 14.0% |
| BEAT rate (59A(b)(1)(A)); banks and registered securities dealers add 1 point | 10% (5% for 2018) | 10.5% (11.5% for banks and dealers) |
| BEAT applicable taxpayer | $500 million average gross receipts (3 prior years) and base erosion percentage of 3% (2% banks and dealers) | Same |
| Subpart F and NCTI high-tax threshold (90% of the section 11 rate) | 18.9% | 18.9% |

Never apply the step-down that Pub. L. 115-97 had scheduled for 2026 (GILTI deduction 37.5%, FDII deduction 21.875%, BEAT 12.5% with all credits reducing regular tax). Pub. L. 119-21 struck all three before they took effect. For a domestic corporation, the section 250 deduction is limited by taxable income (250(a)(2)); test it before using the rates above.

## 3. Net CFC tested income (section 951A)

- Tested income: CFC gross income excluding ECI (952(b)), subpart F income, income excluded by a 954(b)(4) high-tax election, related-person dividends and foreign oil and gas extraction income, less properly allocable deductions including taxes (951A(b)(2)). Tested loss is the reverse.
- NCTI: the U.S. shareholder's pro rata share of tested income of all its CFCs less its pro rata share of tested losses. For U.S. shareholder years beginning after Dec. 31, 2025 there is no QBAI or net deemed tangible income return; a model that still subtracts 10% of QBAI understates the inclusion.
- Inclusion percentage = NCTI divided by aggregate pro rata tested income (960(d)(2)); it drives the deemed-paid credit and the gross-up.
- Individuals: no section 250 deduction or deemed-paid credit unless a section 962 election is made; route individual owners' elections to the tax adviser.
- Coordination: 163(j) adjusted taxable income excludes 951(a), 951A(a) and 78 inclusions for taxable years beginning after Dec. 31, 2025 (confirmed by the sibling skill building-lbo-models, `tax-and-accounting-rules.md`).

## 4. Subpart F, section 954(c)(6), high-tax elections and ownership rules

- Subpart F income (952, 954): foreign personal holding company income, foreign base company sales and services income; included under 951(a)(1)(A) with the pro rata share by period of ownership for CFC years beginning after 2025.
- 954(c)(6): dividends, interest, rents and royalties from a related CFC are not FPHCI to the extent attributable to the payor's income that is neither subpart F income nor ECI. Permanent for foreign corporation years beginning after Dec. 31, 2025. The exception does not apply to payments that create or increase a deficit that reduces subpart F income (954(c)(6)(B)).
- Subpart F high-tax exception (954(b)(4); Treas. Reg. 1.954-1(d)): elective; the net item must bear an effective foreign rate above 90% of the section 11 rate (18.9%).
- NCTI high-tax exclusion (Treas. Reg. 1.951A-2(c)(7)): elective, made by the controlling domestic shareholders for all members of a CFC group, tested by tested unit, same 18.9% threshold. The regulation cites former 951A(c)(2)(A)(i)(III); its continued application to NCTI under renumbered 951A(b)(2)(A)(i)(III) is [VERIFY]. Excluded income takes its taxes out of the 960(d) pool, so model the election both ways.
- Ownership: 958(b)(4) restored for foreign corporation years beginning after 2025, so stock owned by a foreign parent is no longer attributed down to its U.S. subsidiaries for CFC status; section 951B (foreign-controlled U.S. shareholders) applies instead. Re-test CFC status for every foreign-parented group.

## 5. Foreign tax credit: baskets, deemed-paid credit, expense allocation

- Four separate limitations (904(d)(1)): section 951A category (NCTI), foreign branch, passive and general. Never pool credits across baskets.
- No carryback or carryforward of excess credits in the 951A category (904(c), last sentence). Excess NCTI-basket credits are lost in the year.
- Deemed-paid credit (960(d)(1)): 90% times inclusion percentage times tested foreign income taxes (years beginning after 2025; 80% before).
- Expense allocation for the NCTI basket (904(b)(5), years beginning after 2025): allocate only the section 250(a)(1)(B) deduction, deductions for taxes on that income, and deductions directly allocable to it. Interest expense and R&E expenditures are never allocated to it; deductions that would have been are allocated to U.S.-source income. Proposed Treas. Reg. 1.904(b)-4 (REG-117273-25, 91 Fed. Reg., Sept. 11, 2026) treats stewardship and legal expenses as not directly allocable and NOLs and section 986(c) loss as directly allocable; taxpayers may rely on it in its entirety.
- 960(d)(4): 10% of foreign taxes paid or deemed paid on distributions of PTEP from 951A inclusions after June 28, 2025 is not creditable.
- Section 245A(d): no credit and no deduction for foreign taxes on a dividend for which a 245A deduction is allowed, including withholding tax.

## 6. FDDEI (section 250(b))

- Deduction eligible income (DEI): gross income excluding subpart F and NCTI inclusions, financial services income, CFC dividends, domestic oil and gas extraction income, foreign branch income and (dispositions after June 16, 2025) income and gain from dispositions of intangible property (as defined in 367(d)(4)) and of depreciable, amortizable or depletable property, including 367(d) deemed sales; less allocable deductions other than interest and R&E (years beginning after 2025).
- FDDEI: DEI from property sold to a non-U.S. person for foreign use, or services provided to a person (or with respect to property) outside the United States, with the related-party and domestic-intermediary rules of 250(b)(2). There is no deemed tangible income return after 2025, so FDDEI is not reduced by a QBAI return.
- Proposed Treas. Reg. 1.250(b)-1(h) (REG-117130-25, 91 Fed. Reg., Aug. 20, 2026) defines the dispositions the exclusion reaches and applies to dispositions after June 16, 2025; taxpayers may rely on it if they and their related parties follow it in its entirety.

## 7. Section 245A dividends, holding period and hybrid dividends

- Deduction for the foreign-source portion of dividends from a specified 10-percent owned foreign corporation received by a domestic corporation that is a U.S. shareholder (245A(a)). PFICs that are not CFCs are excluded.
- Holding period (246(c)(1)(A) as modified by 246(c)(5)): the stock must be held more than 365 days during the 731-day period beginning 365 days before the ex-dividend date, and during that time the foreign corporation must remain a specified 10-percent owned foreign corporation and the taxpayer a U.S. shareholder. The day of acquisition is excluded and the day of disposition included (246(c)(3)). Periods under a contract to sell or other risk-diminishing positions reduce the count (246(c)(4)). The period can be completed after the dividend; a sale before it is completed denies the deduction.
- Hybrid dividends (245A(e); Treas. Reg. 1.245A(e)-1): no 245A deduction, and no credit or deduction for related foreign taxes, to the extent of the U.S. shareholder's hybrid deduction accounts, which track deductions or other tax benefits the CFC received abroad for instruments that are stock for U.S. purposes. Accounts are adjusted at the close of the CFC's year and follow transferred shares.
- Distributions are sourced first from PTEP (959); PTEP is excluded from income rather than deducted, and its withholding taxes are creditable subject to 960(d)(4) and the basket rules.
- Treas. Reg. 1.245A-5 (extraordinary dispositions and reductions) also limits the deduction; proposed rules would turn off 1.245A-5(e) and (f) for foreign corporation years beginning after 2025 (REG-115646-25).

## 8. Entity classification and hybrid rules

- Per se corporations listed in Treas. Reg. 301.7701-2(b)(8) cannot elect. A foreign eligible entity defaults to association if all members have limited liability, partnership if two or more members and one lacks limited liability, disregarded if single-owner without limited liability (301.7701-3(b)(2)).
- Form 8832 effective date: no more than 75 days before and no more than 12 months after filing; an earlier date is moved to 75 days before filing (301.7701-3(c)(1)(iii)). After a change by election, no further election for 60 months unless the Commissioner permits (301.7701-3(c)(1)(iv)). A change in classification is a deemed liquidation or contribution with its own tax consequences, including section 367.
- Section 267A: no U.S. deduction for related-party interest or royalties paid under a hybrid transaction or to or by a hybrid entity where the payee does not include the amount or gets a deduction.
- Disregarded payments can create foreign deductions without U.S. income; check foreign anti-hybrid rules and Pillar Two treatment at the same time.

## 9. Outbound transfers: section 367 and cost sharing structure

- 367(a)(1): a U.S. person's transfer of property to a foreign corporation in a 332, 351, 354, 356 or 361 exchange is generally taxable because the foreign corporation is not treated as a corporation for gain recognition.
- 367(d): transfers of intangible property to a foreign corporation are treated as sales for annual contingent payments commensurate with income over the property's useful life; the deemed payments are ordinary income and, for dispositions after June 16, 2025, excluded from DEI.
- 367(b) governs inbound and foreign-to-foreign reorganizations and liquidations.
- Outbound restructurings: map each step (contribution, conversion by entity classification election, liquidation, sale) to 367(a) gain, 367(d) inclusions, and the change in where future intangible income is taxed (NCTI, subpart F, FDDEI exclusion for 367(d) amounts).
- Cost sharing arrangement structure (Treas. Reg. 1.482-7): identify the controlled participants, the intangible development area, the platform contribution transactions and how they are paid, and whether intangibles were transferred outside the arrangement (367(d)). This skill sets out the structure and its NCTI, subpart F, FDDEI and Pillar Two consequences; the pricing of buy-ins, platform contributions and 367(d) royalties, and their documentation and benchmarking, route to managing-transfer-pricing-compliance.

## 10. Inbound: BEAT, withholding, portfolio interest, FIRPTA, partnerships, corporate AMT, intercompany loans

- FDAP income of a foreign corporation from U.S. sources (interest, dividends, rents, royalties): 30% tax (881(a)) collected by withholding (1442, applying 1441 rules) unless a treaty or statutory exemption applies. The withholding agent is liable for tax it fails to withhold (1461).
- Portfolio interest exemption is unavailable to a 10-percent shareholder of the payor (881(c)(3)(B), by reference to 871(h)(3)(B)), to banks on ordinary-course loans and to CFCs receiving interest from related persons.
- BEAT: applicable taxpayer tests above; modified taxable income adds back base erosion tax benefits; payments subject to full 30% withholding are disregarded (59A(c)(2)(B)).
- FIRPTA: gain on U.S. real property interests is ECI (897); a domestic corporation is a USRPHC if USRPIs are at least 50% of the sum of USRPIs, foreign real property and trade or business assets (897(c)(2)), with a lookback of the shorter of the holding period or five years. Transferee withholding is 15% of the amount realized (1445(a)), with affidavit and other exemptions in 1445(b).
- Partnerships: withholding on ECI allocable to foreign partners at the highest rate in section 1 (37% for 2026 under 1(j)) for non-corporate partners and 21% for corporate partners (1446(a), (b)); a transferee of a partnership interest withholds 10% of the amount realized where 864(c)(8) treats gain as ECI (1446(f)).
- Operational withholding (Forms W-8, QI and QDD status, Forms 1042 and 1042-S, FATCA under 1471) routes to managing-international-withholding-tax.
- Corporate AMT for foreign-parented groups: a corporation is an applicable corporation if its 3-year average adjusted financial statement income exceeds $1 billion, and for a member of a foreign-parented multinational group (domestic and foreign entities in the same applicable financial statement with a foreign common parent) that test is run on the whole group's income while the corporation's own average must also be $100 million or more (59(k)(1)(B)(ii), (k)(2)); a foreign corporation's U.S. trade or business counts as a separate domestic corporation (59(k)(2)(C)). Tentative minimum tax is 15% of adjusted financial statement income less the corporate AMT foreign tax credit (55(b)(2)(A)). The domestic test outside this rule routes to analyzing-corporate-tax-structures.
- Intercompany loans across borders: on the U.S. side test 163(j) (with the ATI exclusion for 951(a), 951A and 78 inclusions for years beginning after 2025), 267A, 267(a)(3) timing, BEAT and portfolio interest; on the foreign side the lender's and borrower's interest-limitation, thin capitalization and anti-hybrid rules are local law and [VERIFY] per jurisdiction; treaty interest articles and their LOB tests govern withholding. The arm's-length interest rate and the AFR safe haven route to managing-transfer-pricing-compliance.

## 11. Computation order for an NCTI year

1. Fix each U.S. shareholder's and each CFC's taxable year and classify each by its beginning date (Section 1).
2. Confirm CFC and U.S. shareholder status with 958(b)(4) as restored and ownership by period.
3. For each CFC: subpart F income (after 954(c)(6) and any high-tax election), then tested income or loss, then tested foreign income taxes.
4. Aggregate to NCTI; compute the inclusion percentage, the 960(d) deemed-paid credit and the 78 gross-up.
5. Section 250 deduction at the rate for the domestic corporation's year, after the taxable income limit.
6. FTC limitation by basket with the expense allocation rules for the year; record lost NCTI-basket excess credits.
7. Residual U.S. tax and the effective rate; then BEAT, 163(j) and state hand-offs.
