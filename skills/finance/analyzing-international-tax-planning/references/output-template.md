# Output Template

Produce the header and the sections below, in this order, omitting a section only by writing "Not in scope" and the reason. Every figure carries a source locator, a computation reference, or [UNVERIFIED]. Every rate carries the taxable year it applies to and its citation. State currency and units once in the header.

## Contents

1. Header and source-review register
2. Section 1. Structure, ownership and taxable years
3. Section 2. Rule set by taxable year
4. Section 3. Outbound: subpart F, NCTI and foreign tax credit
5. Section 4. FDDEI
6. Section 5. Repatriation and distributions
7. Section 6. Inbound: withholding, treaty and LOB, BEAT, FIRPTA
8. Section 7. Pillar Two exposure
9. Section 8. Elections register
10. Section 9. Reconciliation checks
11. Section 10. Issues, conflicts and judgment calls
12. Section 11. Hand-offs
13. Section 12. Open items and [VERIFY] list

## Header and source-review register

- Matter, client group, date prepared, "Draft for review by a qualified tax adviser."
- Question presented in one sentence; direction (outbound, inbound or both); years covered.
- Source-review register:

| File | Type | Date | Rank | Status | Pages, tabs or sections read | Note |
|---|---|---|---|---|---|---|
| name as received | entity chart, organizational documents, Form 8832, tax returns and Forms 5471 / 8992 / 8993 / 1118, financial statements, GloBE workpapers, treaty text, W-8 forms, agreements, emails | | 1-4 | Reviewed / Not relevant / Unreadable after attempt / Still needed | | |

Rank 1: executed legal documents and filed elections. Rank 2: filed returns and audited financial statements. Rank 3: workpapers, models and management schedules. Rank 4: emails, summaries and slide decks.

## 1. Structure, ownership and taxable years

| Entity | Jurisdiction | U.S. classification (per se, default or elected, with Form 8832 date) | Direct owner and % (vote and value) | CFC / U.S. shareholder status | Taxable year (begin and end dates) | Source |
|---|---|---|---|---|---|---|

Name the entity whose tax each later section computes (U.S. shareholder, CFC, withholding agent, constituent entity).

## 2. Rule set by taxable year

| Taxpayer | Taxable year begins | Ends | Rule set (2018-2025 regime or Pub. L. 119-21 regime) | Items affected (250 rates, QBAI, 960(d) %, 904(b)(5), BEAT rate, pro rata share) | Citation |
|---|---|---|---|---|---|

## 3. Outbound: subpart F, NCTI and foreign tax credit

Per CFC:

| CFC | Subpart F income (after 954(c)(6) and any high-tax election) | Tested income or (loss) | Tested foreign income taxes | QBAI (pre-2026 shareholder years only) | Source |
|---|---|---|---|---|---|

Per U.S. shareholder: NCTI (or GILTI for years beginning before 2026), inclusion percentage, 960(d) deemed-paid taxes (rate and year), section 78 gross-up, section 250 deduction (rate, year, 250(a)(2) limit test), taxable inclusion, pre-credit tax.

FTC limitation by basket:

| Basket | Foreign-source gross income | Allocated deductions (by type; interest and R&E shown as zero for NCTI basket years beginning after 2025) | Foreign-source taxable income | Limitation | Creditable taxes | Credit | Excess (carryover allowed? 951A basket: no) |
|---|---|---|---|---|---|---|---|

Then residual U.S. tax and an effective-rate bridge: foreign tax, U.S. residual, total, as a percentage of pre-tax foreign income.

## 4. FDDEI

DEI build (gross income less exclusions, including dispositions after June 16, 2025 of intangibles and depreciable property), allocable deductions (interest and R&E excluded for years beginning after 2025), foreign-use and foreign-person evidence by revenue stream, FDDEI, deduction at the rate for the year, effective rate.

## 5. Repatriation and distributions

| Distribution | Date and ex-dividend date | Payer | PTEP portion (959) | 245A portion | Holding period test (days held in the 731-day window; date it is or will be met) | Hybrid deduction account | Foreign withholding | Credit, deduction or disallowance (245A(d), 960(d)(4)) | U.S. tax |
|---|---|---|---|---|---|---|---|---|---|

Compare repatriation pathways (dividend, PTEP distribution, loan repayment, return of capital, liquidation) by total tax cost, each with its year.

## 6. Inbound: withholding, treaty and LOB, BEAT, FIRPTA

| Payment | Payer (withholding agent) | Payee and beneficial owner | Gross | Statutory rate and cite | Treaty and article | LOB test relied on and evidence | Rate applied | Tax | Source |
|---|---|---|---|---|---|---|---|---|---|

LOB worksheet: each test in the treaty's LOB article, Met / Not met / Not tested, with the facts relied on. BEAT: gross receipts test, base erosion percentage, modified taxable income, rate for the year. FIRPTA and 1446: USRPHC test, amount realized, withholding rate.

## 7. Pillar Two exposure

| Jurisdiction | Fiscal year | GloBE income | Adjusted covered taxes | ETR | SBIE | Excess profit | Top-up % | Top-up | Charging rule (QDMTT / IIR / UTPR) | Safe harbour tested and result | Local law status |
|---|---|---|---|---|---|---|---|---|---|---|---|

State whether the SbS election is made for each fiscal year commencing on or after January 1, 2026, where Section 1 of the GIR is filed, and that QDMTT exposure is computed regardless.

## 8. Elections register

| Election | Entity | Year | Made? (evidence) | Deadline and consistency rules | Effect if made / not made |
|---|---|---|---|---|---|

Include entity classification, subpart F and NCTI high-tax elections, section 962, section 78 and credit-versus-deduction choice, and the SbS Safe Harbour.

## 9. Reconciliation checks

Every row is computed, not asserted. A Fail row goes to Section 10.

| # | Check | Test | Result (Pass / Fail / Not run) | Difference | Note |
|---|---|---|---|---|---|
| X1 | Ownership | Direct ownership per entity sums to 100% and matches the chart and the 5471s | | | |
| X2 | Year classification | Every taxable year is labeled by its beginning date with the rule set applied | | | |
| X3 | NCTI | Sum of pro rata tested income minus sum of tested loss equals NCTI | | | |
| X4 | Credit and gross-up | Gross-up = inclusion % x tested foreign income taxes; deemed paid = 90% (or 80% for pre-2026 years) x gross-up | | | |
| X5 | Section 250 | Deduction = rate for the year x (inclusion + gross-up), after the 250(a)(2) limit | | | |
| X6 | FTC limitation | Credit in each basket does not exceed that basket's limitation; NCTI-basket excess shown as lost | | | |
| X7 | Expense allocation | Interest and R&E allocated to the NCTI basket are zero for years beginning after 2025 | | | |
| X8 | Distributions | Each distribution is sourced from PTEP before other E&P, and 245A is claimed only on the non-PTEP portion | | | |
| X9 | Withholding | Rate x gross payment equals tax withheld for each payment; treaty basis recorded | | | |
| X10 | Pillar Two | ETR = covered taxes / GloBE income; top-up = (15% - ETR) x (GloBE income - SBIE) | | | |
| X11 | Rate bridge | Foreign tax + U.S. residual = total tax in the effective-rate bridge | | | |

## 10. Issues, conflicts and judgment calls

| # | Severity | Issue | Sources in conflict (locators) | Controlling source and why | Tax effect and year | Recommendation and alternative | Owner |
|---|---|---|---|---|---|---|---|

Severity: Critical (a liability, credit or withholding amount is wrong by a material amount, or a reconciliation check fails); High (an election, LOB position or year classification is unsupported); Medium (a conflict with a clear controlling source); Low (clean-up).

## 11. Hand-offs

A hand-off names the facts the receiving workflow needs; a bare skill name is not a hand-off.

| To | Why | Facts passed (amounts, years, entities, locators) | Open questions | What this analysis did not do |
|---|---|---|---|---|
| managing-transfer-pricing-compliance | Intercompany pricing, documentation and benchmarking, including buy-in, platform contribution and 367(d) royalty pricing | | | |
| analyzing-corporate-tax-structures | Domestic entity choice, S corporation, QSBS, consolidated-group and PTE questions | | | |
| managing-international-withholding-tax | W-8 forms, QI, Forms 1042 and 1042-S, FATCA | | | |
| analyzing-state-income-tax | State treatment of NCTI, subpart F, 78, 250 and 245A | | | |
| managing-income-tax-provisions | ASC 740 for NCTI, Pillar Two and uncertain positions | | | |

Add or remove rows to match the matter.

Hand-ins this skill accepts from sibling skills (answer them in the sections above):

| From | Trigger |
|---|---|
| managing-transfer-pricing-compliance | 367(d) inclusions and outbound restructurings or transfers of intangibles; cost sharing arrangement structure; Pillar Two / GloBE effects of transfer pricing adjustments; NCTI, FDDEI and BEAT computations; treaty and foreign interest-limitation questions on intercompany loans |
| analyzing-corporate-tax-structures | Foreign owners or foreign subsidiaries of a domestic structure; CFCs, treaties, and inbound and outbound structures; the corporate AMT applicable-corporation test for foreign-parented groups (section 59(k)(2)) |

## 12. Open items and [VERIFY] list

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Depends on | Owner | Next action | Changes which output |
|---|---|---|---|---|---|---|

Close with: "Draft for review by a qualified tax adviser. Not a tax opinion, return position or legal advice."
