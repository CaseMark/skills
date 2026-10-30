# Primary Sources and Verification Register

Checked on October 30, 2026, in two passes the same day. The first pass used web search restricted to the issuing body's own site (irs.gov, congress.gov, govinfo.gov, storage.fasb.org, occ.gov, fdic.gov, support.microsoft.com, newyorkfed.org) and read the text each search returned. The second pass read full texts through the case.dev API (`/search/v1/contents`): statutes through law.cornell.edu (current U.S. Code text), regulations through ecfr.gov and law.cornell.edu, revenue procedures as irs.gov PDFs, ASU 2015-03 as the FASB PDF, and agency releases on their own sites. Each row gives the URL read, the method ("full text via case.dev" or "search excerpt") and the date. The FASB Codification itself (login required) was not opened; ASU text shows the paragraphs it amended. Re-check every item before relying on it in a client-facing deliverable; tax figures change annually and Pub. L. 119-21 guidance is still being issued.

## Contents

1. Authorities checked
2. Corrections made on full-text review
3. Unconfirmed, year-dependent or inference: treat as [VERIFY]

## 1. Authorities checked

| Authority | URL read | Method; date | What it supports in this skill |
|---|---|---|---|
| Corporate income tax rate, IRC 11(b) | govinfo.gov U.S. Code 2021 and 2023 editions; IRS Notice 2018-38; IRS Publication 542 | Search excerpt; 2026-10-30 | 21 percent flat rate for taxable years beginning after Dec. 31, 2017 |
| Business interest limitation, IRC 163(j)(1), (2), (3), (8) | https://www.law.cornell.edu/uscode/text/26/163 | Full text via case.dev; 2026-10-30 | 30 percent of ATI plus business interest income plus floor plan interest; indefinite carryforward; small business exemption by reference to IRC 448(c); current (8)(A) adds back depreciation, amortization and depletion and excludes 951(a), 951A(a) and 78 inclusions |
| ATI add-back restored | Pub. L. 119-21 (July 4, 2025), sec. 70303; Internal Revenue Bulletin 2026-15; IRS FAQ; Form 8990 instructions line 11 | Search excerpt; current statute text read in full (row above); 2026-10-30 | Add-back for taxable years beginning after Dec. 31, 2024; not added back for 2022-2024 |
| ATI excludes CFC inclusions | Pub. L. 119-21, sec. 70342; IRB 2026-15; CRS Report R48611 | Search excerpt; current statute text read in full; 2026-10-30 | Exclusion of 951(a), 951A(a) and 78 inclusions for taxable years beginning after Dec. 31, 2025 |
| Capitalized interest and 163(j) | IRS business interest FAQ (2026 update) and newsroom item; IRS Fact Sheet FS-2026-14 | Search excerpt; 2026-10-30 | For taxable years beginning after Dec. 31, 2025, business interest expense includes interest capitalized in the year, except under IRC 263(g) or 263A(f) |
| Gross receipts threshold | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf (Rev. Proc. 2025-32, section 3.30) | Full text via case.dev; 2026-10-30 | $32,000,000 average annual gross receipts for taxable years beginning in 2026 |
| 2027 inflation adjustments | https://www.irs.gov/newsroom/inflation-adjusted-tax-items-by-tax-year | Full text via case.dev; 2026-10-30 | Page lists 2026 items only; no 2027 revenue procedure posted as of the check date |
| Definition of interest for 163(j) | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR0b6a3ddd4d7a2c9/section-1.163(j)-1 (paragraph (b)(22)); T.D. 9905 preamble, 85 Fed. Reg. (Sept. 14, 2020) | Regulation: full text via case.dev; preamble: search excerpt; 2026-10-30 | OID, qualified stated interest and issuer de minimis OID listed as interest; debt issuance costs and commitment fees not listed |
| ATI add-back scope | T.D. 9905 preamble and the Jan. 19, 2021 Federal Register notice on Treas. Reg. 1.163(j)-1(b)(1)(i)(D)-(F); Instructions for Form 8990 (Rev. Dec. 2025) | Search excerpt; 2026-10-30 | Add-backs cover depreciation, amortization of intangibles and depletion; debt issuance cost deductions are not among them |
| Debt issuance costs (tax) | https://www.law.cornell.edu/cfr/text/26/1.446-5 | Full text via case.dev; 2026-10-30 | Treated as if they decreased issue price; deducted under the OID rules of 1.163-7, constant yield or the de minimis rules |
| OID definition and de minimis rule | https://www.law.cornell.edu/uscode/text/26/1273 | Full text via case.dev; 2026-10-30 | OID treated as zero below 1/4 of 1 percent of stated redemption price times complete years to maturity (1273(a)(3)) |
| AHYDO, IRC 163(e)(5), 163(i) | govinfo.gov U.S. Code 2024 edition; Rev. Proc. 2008-51; current statute text in the 163 row | Search excerpt; 2026-10-30 | Three-part definition; disqualified portion disallowed, remainder deductible when paid |
| NOL deduction, IRC 172(a), (b) | https://www.law.cornell.edu/uscode/text/26/172 | Full text via case.dev; 2026-10-30 | 80 percent limit for post-2017 NOLs in years beginning after 2020, after pre-2018 NOLs; indefinite carryforward for post-2017 NOLs; 20-year carryforward for pre-2018 NOLs |
| Ownership change limit, IRC 382(b)(1), (e), (f), (g) | https://www.law.cornell.edu/uscode/text/26/382; Treas. Reg. 1.382-5 and IRS Chief Counsel memorandum 0140049 (search excerpts) | Statute: full text via case.dev; others: search excerpt; 2026-10-30 | Value immediately before the change times the long-term tax-exempt rate; (e)(2) value after a redemption or corporate contraction in connection with the change; (f) highest adjusted federal long-term rate in the three-month period ending with the change month; (g) ownership change |
| Bonus depreciation | Pub. L. 119-21, sec. 70301; IRS Notice 2026-11; Rev. Proc. 2026-15 (search excerpts); https://www.law.cornell.edu/uscode/text/26/168 and https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR5a5b8d1d5b0d2f5/section-1.168(k)-2 | Statute and regulation: full text via case.dev; notice and revenue procedure: search excerpt; 2026-10-30 | Permanent 100 percent for property acquired after Jan. 19, 2025; used property qualifies only if not previously used by the taxpayer and acquired by purchase within 179(d)(2) and (3) |
| Facilitative transaction costs | Treas. Reg. 1.263(a)-5 (search excerpt); https://www.irs.gov/pub/irs-drop/rp-11-29.pdf | Revenue procedure: full text via case.dev; regulation: search excerpt; 2026-10-30 | Capitalization of facilitative costs; success-based fee presumption; elective 70 percent deductible / 30 percent capitalized safe harbor by statement on the original return |
| Acquisition-related costs (GAAP) | ASC 805-10-25-23 as quoted in Deloitte DART Business Combinations Roadmap sec. 5.4 | Search excerpt; 2026-10-30 (asc.fasb.org returned no text) | Expensed as incurred; costs to issue debt or equity follow other GAAP |
| Debt issuance cost presentation | https://storage.fasb.org/ASU%202015-03.pdf | Full text via case.dev; 2026-10-30 | ASU 2015-03 amended 835-30-45-1A (direct deduction from the face amount of the note, not a deferred charge) and 835-30-45-3 (amortization reported as interest expense) |
| Revolver issuance costs | ASU 2015-15 (SEC staff announcement); Deloitte DART Debt Roadmap sec. 5.4 | Search excerpt; 2026-10-30 | Line-of-credit costs may be deferred as an asset and amortized ratably over the term, drawn or not |
| Leveraged lending guidance withdrawn | https://www.occ.gov/news-issuances/news-releases/2025/nr-ia-2025-119.html; OCC Bulletin 2025-44 and FDIC press release (search excerpts) | Release: full text via case.dev; others: search excerpt; 2026-10-30 | OCC and FDIC rescinded the 2013 Interagency Guidance on Leveraged Lending and the 2014 FAQs on Dec. 5, 2025; general safe-and-sound lending principles apply; a 6.0x leverage figure is not a current OCC or FDIC supervisory threshold |
| Federal Reserve SR 13-3 | https://www.federalreserve.gov/supervisionreg/srletters/sr1303.htm | Full text via case.dev (cached copy); 2026-10-30 | Page as read shows no rescission notice; see the [VERIFY] list |
| Benchmark rate transition | ARRC materials at newyorkfed.org (Mar. 5, 2021 press release; Oct. 6, 2021 fallback summary); CME Group Term SOFR materials | Search excerpt; 2026-10-30 | USD LIBOR panel settings ceased after June 30, 2023; CME Term SOFR is the ARRC-recommended forward-looking term rate |
| XIRR | Microsoft Support, "XIRR function" | Search excerpt; 2026-10-30 | Dated cash flows discounted on a 365-day year from the first date; iterative solve |
| Iterative calculation | Microsoft Support, "Remove or allow a circular reference in Excel" and "Change formula recalculation, iteration, or precision in Excel" | Search excerpt; 2026-10-30 | Defaults of 100 iterations and 0.001 maximum change |

## 2. Corrections made on full-text review

| Item | Before | After | Source |
|---|---|---|---|
| ASC 835-30-45-1A | "Added by ASU 2015-03" | Amended by ASU 2015-03; amortization as interest expense is 835-30-45-3, also amended | ASU 2015-03, amendment paragraph 3 and the 835-30-00-1 table |
| Pre-2018 NOL carryforward | [VERIFY] | 20 taxable years following the loss year (IRC 172(b)(1)(A)(ii)(I)) | IRC 172 |
| 80 percent limit base | "Taxable income computed before the NOL deduction" | Taxable income computed without the 172, 199A and 250 deductions, less pre-2018 NOLs (IRC 172(a)(2)) | IRC 172 |
| Bonus depreciation on used property | [VERIFY] in full | Statutory and regulatory used-property test stated; only its application to asset and deemed asset purchases remains [VERIFY] | IRC 168(k)(2)(E); Treas. Reg. 1.168(k)-2(b)(3)(iii) |
| Commitment fees for 163(j) | "Reserved for future guidance" | Not listed as interest in Treas. Reg. 1.163(j)-1(b)(22); later guidance still [VERIFY] | eCFR 1.163(j)-1 |

No eval expectation changed: eval 2 cites ASC 835-30 (ASU 2015-03) without the paragraph verb, and eval 5's NOLs (2019-2023) are all post-2017, so the 80 percent cap of $33.52m (80 percent of $41.9m) and the $14.0m Section 382 limit are unchanged.

## 3. Unconfirmed, year-dependent or inference: treat as [VERIFY]

| Statement | Status |
|---|---|
| IRC 448(c) threshold for taxable years beginning in 2027 | The IRS inflation-adjusted items page listed no 2027 revenue procedure on 2026-10-30 |
| ASC 805-10-25-23 wording | Read as quoted by Deloitte DART; asc.fasb.org returned no text |
| Commitment fee treatment for 163(j) | Not listed as interest in the final regulation; no later guidance located |
| Ordering of capitalized interest against carryforwards under Pub. L. 119-21 for taxable years after 2025 | Scope rule confirmed in IRS excerpts; ordering mechanics not located |
| Whether a given LBO financing step is a redemption or corporate contraction under IRC 382(e)(2) | Statute read in full; application is fact-specific |
| AHYDO outcome for any specific instrument | Requires the AFR for the issue month and a yield computation by the tax adviser |
| Long-term tax-exempt rate for a given closing month | Published monthly by revenue ruling; not looked up |
| Bonus depreciation for the target's existing assets in an asset purchase or deemed asset purchase election | Used-property test confirmed; its application to these structures not reviewed |
| Federal Reserve status of the 2013 leveraged lending guidance | OCC and FDIC withdrawal confirmed; the copy of SR 13-3 read shows no rescission, and no Federal Reserve rescission was located |
| Pushdown accounting or IFRS differences for the opening balance sheet | Not reviewed |
| State, local and foreign income tax effects | Out of scope |
| Market terms (Term SOFR forward curve, credit spreads, OID levels, sweep percentages, leverage multiples) | Change daily; take from the user's materials or mark [VERIFY] with the date |
