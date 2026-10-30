# Primary Sources and Verification Register

## Contents

1. How these sources were checked
2. Rules, statutes and regulations
3. Cases
4. Court guidance and dockets
5. `[VERIFY]` list

## How these sources were checked

All checks were made on 2026-10-30 through the case.dev API: `/search/v1/contents` for rule, statute, regulation, court-guidance and opinion pages, `/legal/v1/full-text` for opinions hosted on Justia and FindLaw, and `/legal/v1/verify` for reporter citations. "Full text via case.dev" means the whole rule, section or opinion was retrieved and the cited passage was read, not a snippet. Cornell LII, Justia, FindLaw and leginfo are publishers of the official text; Justia and FindLaw are unofficial reproductions of the opinions. Where a reporter citation could not be matched by `/legal/v1/verify`, the row says so and gives the source that confirmed it. Re-read the current Rule 23 text, the controlling circuit's law and the local rules before any filing.

## Rules, statutes and regulations

| Authority | URL read | Method; date | What it supports | Status |
|---|---|---|---|---|
| Fed. R. Civ. P. 23, with Committee Notes through the 2018 Amendment | https://www.law.cornell.edu/rules/frcp/rule_23 | Full text via case.dev; 2026-10-30 | (c)(2)(B) best notice practicable, contents (i)-(vii), notice by mail, electronic or other means; (c)(5) subclasses; (e) applies to classes proposed for settlement; (e)(1)(B) "will likely be able to" approve and certify; (e)(2)(A)-(D) factors; (e)(3) agreements statement; (e)(4) new opt-out; (e)(5)(A) objection content; (e)(5)(B) court approval after hearing for payments to forgo or withdraw objections or appeals; (e)(5)(C) Rule 62.1; (h)(1)-(4) fee motion, notice to class, objections, findings; 2018 Committee Note on claims rate, unclaimed funds, other litigation, fee deferral, "relief actually delivered" | Confirmed. The LII history line ends at 2009; the 2018 Committee Note is present |
| Fed. R. Civ. P. 6(a) | https://www.law.cornell.edu/rules/frcp/rule_6 | Full text via case.dev; 2026-10-30 | Applies to rules, orders and statutes without their own method; (1)(C) weekend and holiday rollover; (5) next day forward or backward; (6) legal holidays | Confirmed |
| Fed. R. Civ. P. 54(d)(2)(B)-(C) | https://www.law.cornell.edu/rules/frcp/rule_54 | Full text via case.dev; 2026-10-30 | Fee motion within 14 days after judgment unless a statute or court order provides otherwise; proceedings subject to Rule 23(h) | Confirmed |
| 28 U.S.C. 1711 | https://www.law.cornell.edu/uscode/text/28/1711 | Full text via case.dev; 2026-10-30 | Definitions: "class action" (federal filing or removal), "proposed settlement"; applies to actions commenced on or after Feb. 18, 2005 | Confirmed |
| 28 U.S.C. 1712 | https://www.law.cornell.edu/uscode/text/28/1712 | Full text via case.dev; 2026-10-30 | (a) coupon-attributable fee based on value of coupons redeemed; (b) lodestar, multiplier permitted; (c) mixed relief; (d) valuation expert; (e) hearing and written finding; unclaimed coupon value to charities not counted for fees | Confirmed |
| 28 U.S.C. 1713 | https://www.law.cornell.edu/uscode/text/28/1713 | Full text via case.dev; 2026-10-30 | Net-loss settlements need a written finding | Confirmed |
| 28 U.S.C. 1714 | https://www.law.cornell.edu/uscode/text/28/1714 | Full text via case.dev; 2026-10-30 | No geographic favoritism | Confirmed |
| 28 U.S.C. 1715 | https://www.law.cornell.edu/uscode/text/28/1715 | Full text via case.dev; 2026-10-30 | (a) appropriate federal and state officials; (b) each participating defendant serves within 10 days after the proposed settlement is filed, items (1)-(8); (c) depository institutions; (d) no final approval order earlier than 90 days after the later service; (e) class member may refuse to be bound, with limitation; (f) no expansion of officials' authority | Confirmed |
| Treas. Reg. 1.468B-1(c) | https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR6e8b0a5e3b0e0e4/section-1.468B-1 | Full text via case.dev; 2026-10-30 | Qualified settlement fund: court order and continuing jurisdiction, claims from tort, contract or violation of law, segregated or a trust | Confirmed |
| Cal. Civ. Code 1542 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1542 | Full text via case.dev; 2026-10-30 | General release does not extend to unknown or unsuspected claims; amended by Stats. 2018, ch. 157, effective Jan. 1, 2019 | Confirmed |

## Cases

| Case | URL read | Method; date | What it supports | Status |
|---|---|---|---|---|
| Amchem Products, Inc. v. Windsor, 521 U.S. 591 (1997) | https://supreme.justia.com/cases/federal/us/521/591/ | Full text via case.dev; citation via /legal/v1/verify; 2026-10-30 | Settlement class must meet Rule 23(a) and (b) except trial manageability; "undiluted, even heightened, attention" to class definitions; present-injury and exposure-only claimants under one representative | Confirmed |
| Wal-Mart Stores, Inc. v. Dukes, 564 U.S. 338 (2011) | https://supreme.justia.com/cases/federal/us/564/338/ | Full text via case.dev (syllabus passage); 2026-10-30 | Individualized monetary claims belong in (b)(3), not (b)(2) | Confirmed |
| Boeing Co. v. Van Gemert, 444 U.S. 472 (1980) | https://supreme.justia.com/cases/federal/us/444/472/ | Full text via case.dev; 2026-10-30 | Fees from the whole common fund, including unclaimed shares, where each member's share is ascertainable | Confirmed |
| Matsushita Elec. Indus. Co. v. Epstein, 516 U.S. 367 (1996) | https://supreme.justia.com/cases/federal/us/516/367/ | Full text via case.dev; citation via /legal/v1/verify; 2026-10-30 | Under the Full Faith and Credit Act, a state-court class settlement judgment that released exclusively federal claims precluded them in federal court, because state (Delaware) law gave the release that effect | Confirmed |
| Devlin v. Scardelletti, 536 U.S. 1 (2002) | https://supreme.justia.com/cases/federal/us/536/1/ | Full text via case.dev; 2026-10-30 | Timely objecting non-named class members may appeal without intervening | Confirmed |
| Frank v. Gaos, 139 S. Ct. 1041 (2019) (per curiam) | https://www.supremecourt.gov/opinions/18pdf/17-961_j42k.pdf | Full text via case.dev; 2026-10-30 | Cert granted on cy pres-only settlement; vacated and remanded on standing; merits not reached | Confirmed |
| Johnson v. NPAS Solutions, LLC, 975 F.3d 1244 (11th Cir. 2020) | https://media.ca11.uscourts.gov/opinions/pub/files/201812344.pdf | Full text via case.dev; citation via /legal/v1/verify; 2026-10-30 | Objection deadline before fee petition violates Rule 23(h) (harmless on its facts); Greenough and Pettus prohibit incentive awards compensating time or rewarding suit; findings required | Confirmed |
| Johnson v. NPAS Solutions, LLC, 43 F.4th 1138 (11th Cir. 2022) | Citation via /legal/v1/verify (CourtListener: Dickenson v. NPAS Solutions) | Search excerpt; 2026-10-30 | Rehearing en banc denied | Citation confirmed |
| Trustees v. Greenough, 105 U.S. 527 (1882) | Citation via /legal/v1/verify; quoted in NPAS | Search excerpt; 2026-10-30 | Reasonable litigation costs and fees allowed; salary and private expenses of the suing creditor not allowed | Citation confirmed; holding as quoted in NPAS |
| Murray v. Grocery Delivery E-Services USA Inc., 55 F.4th 340 (1st Cir. 2022) | https://law.justia.com/cases/federal/appellate-courts/ca1/21-1931/21-1931-2022-12-16.html | Full text via case.dev; 2026-10-30 | Approval vacated: without separate counsel for distinct groups, equitable allocation could not be assessed; incentive awards not prohibited within Rule 23(e) | Confirmed; reporter citation from vLex search result (not matched by /legal/v1/verify) |
| Melito v. Experian Mktg. Sols., Inc., 923 F.3d 85 (2d Cir. 2019) | Citation via /legal/v1/verify; quoted in Moses and Murray | Search excerpt; 2026-10-30 | Incentive awards not per se unlawful | Citation confirmed |
| Hyland v. Navient Corp., 48 F.4th 110 (2d Cir. 2022) | https://law.justia.com/cases/federal/appellate-courts/ca2/20-3765/20-3765-2022-09-07.html | Full text via case.dev; 2026-10-30 | Rejects Greenough and Pettus argument against service awards | Confirmed; reporter citation from search results |
| Moses v. New York Times Co., 79 F.4th 235 (2d Cir. 2023) | https://law.justia.com/cases/federal/appellate-courts/ca2/21-2556/21-2556-2023-08-17.html | Full text via case.dev; 2026-10-30 | No presumption of fairness; 23(e)(2) factors weighed holistically including fees and awards; access codes are coupons under 1712; incentive awards not per se unlawful | Confirmed; reporter citation from search results |
| Scott v. Dart, 99 F.4th 1076 (7th Cir. 2024) | Citation via /legal/v1/verify; Impact Fund summary | Search excerpt; 2026-10-30 | Seventh Circuit permits service awards | Citation confirmed; holding from summary |
| In re Apple Inc. Device Performance Litig., 50 F.4th 769 (9th Cir. 2022) | https://caselaw.findlaw.com/court/us-9th-circuit/1913652.html | Full text via case.dev; 2026-10-30 | Ninth Circuit rejects Greenough argument; incentive awards permitted | Confirmed; reporter citation from vLex search result |
| Wal-Mart Stores, Inc. v. Visa U.S.A. Inc., 396 F.3d 96 (2d Cir. 2005) | https://law.justia.com/cases/federal/appellate-courts/F3/396/96/592521/ | Full text via case.dev; 2026-10-30 | Release limited by identical factual predicate and adequacy of representation | Confirmed |
| Hesse v. Sprint Corp., 598 F.3d 581 (9th Cir. 2010) | https://law.justia.com/cases/federal/appellate-courts/ca9/08-35235/08-35235-2011-02-25.html | Full text via case.dev; 2026-10-30 | Prior settlement did not release claims lacking the identical factual predicate or adequate representation | Confirmed |
| Pearson v. NBTY, Inc., 772 F.3d 778 (7th Cir. 2014) | https://law.justia.com/cases/federal/appellate-courts/ca7/14-1389/14-1389-2014-11-19.html | Full text via case.dev; 2026-10-30 | Clear-sailing and kicker clauses; notice and fees are costs not benefits; settlement value measured by what the class receives | Confirmed |
| Redman v. RadioShack Corp., 768 F.3d 622 (7th Cir. 2014) | https://law.justia.com/cases/federal/appellate-courts/ca7/14-1471/14-1471-2014-09-19.html | Full text via case.dev; 2026-10-30 | Administrative costs excluded from class benefit; clear sailing gets intense scrutiny; fee motion after objection deadline violated Rule 23(h) | Confirmed; /legal/v1/verify matched a different case name, reporter citation confirmed by NPAS and Pearson |
| Briseño v. Henderson, 998 F.3d 1014 (9th Cir. 2021) | https://law.justia.com/cases/federal/appellate-courts/ca9/19-56297/19-56297-2021-06-01.html | Full text via case.dev; 2026-10-30 | Bluetooth scrutiny (disproportionate fees, clear sailing, kicker) applies to post-certification settlements under amended 23(e)(2)(C) | Confirmed |
| In re Bluetooth Headset Prods. Liab. Litig., 654 F.3d 935 (9th Cir. 2011) | Citation via /legal/v1/verify (multiple matches, including this case); quoted in Briseño | Search excerpt; 2026-10-30 | Three warning signs of collusion: disproportionate distribution, clear sailing, reverter | Citation confirmed; holding as quoted in Briseño |
| In re Mercury Interactive Corp. Sec. Litig., 618 F.3d 988 (9th Cir. 2010) | https://cdn.ca9.uscourts.gov/datastore/opinions/2010/08/18/08-17372.pdf | Full text via case.dev; 2026-10-30 | Objection deadline must follow the fee motion; earlier deadline misapplies Rule 23(h) | Confirmed |
| In re HP Inkjet Printer Litig., 716 F.3d 1173 (9th Cir. 2013) | https://law.justia.com/cases/federal/appellate-courts/ca9/11-16097/11-16097-2013-05-15.html | Full text via case.dev; 2026-10-30 | Fee attributable to coupons must use redemption value | Confirmed |
| Klier v. Elf Atochem N. Am., Inc., 658 F.3d 468 (5th Cir. 2011) | https://caselaw.findlaw.com/court/us-5th-circuit/1581180.html | Full text via case.dev; 2026-10-30 | Cy pres only when direct distribution is not possible; court may not override bargained-for terms | Confirmed |
| In re Baby Prods. Antitrust Litig., 708 F.3d 163 (3d Cir. 2013) | https://law.justia.com/cases/federal/appellate-courts/ca3/12-1165/12-1165-2013-02-19.html | Full text via case.dev; 2026-10-30 | Cy pres permissible but inferior to direct distribution; direct benefit relevant to fees | Confirmed |
| Keil v. Lopez, 862 F.3d 685 (8th Cir. 2017) | Citation via /legal/v1/verify; discussed in NPAS | Search excerpt; 2026-10-30 | Rule 23(h) timing error held harmless | Citation confirmed; holding as described in NPAS |

## Court guidance and dockets

| Source | URL read | Method; date | What it supports | Status |
|---|---|---|---|---|
| N.D. Cal., Procedural Guidance for Class Action Settlements (published Nov. 1, 2018; modified Dec. 5, 2018, Aug. 4, 2022, Sept. 5, 2024) | https://cand.uscourts.gov/rules-forms-fees/northern-district-guidelines/procedural-guidance-class-action-settlements | Full text via case.dev; 2026-10-30 | Explain class and release differences; claim-rate estimate from named comparables; reversions; administrator bids; at least 35 days to opt out or object to the settlement and fee motion; CAFA and 1712 compliance; overlapping cases served within one day; cy pres relationships; post-distribution accounting within 21 days after checks go stale | Confirmed; binding only as the presiding judge applies it |
| Isaacson v. Moses, No. 25-1411 (U.S.) | https://www.supremecourt.gov/search.aspx?filename=/docket/docketfiles/html/public/25-1411.html | Full docket via case.dev; 2026-10-30 | Petition on service awards; response requested; briefs in opposition Sept. 18, 2026; distributed for the Nov. 6, 2026 conference | Confirmed as of 2026-10-30 |
| Brief in opposition, The New York Times Co., No. 25-1411 | https://www.supremecourt.gov/DocketPDF/25/25-1411/424932/20260918171702284_Moses%20-%20Response%20to%20Cert%20Petition.pdf | Full text via case.dev; 2026-10-30 | Remand history: new $2,375,000 non-reversionary fund; final approval Oct. 10, 2024; Second Circuit affirmed Feb. 10, 2026 | Confirmed |
| Inside Class Actions, "Federal Circuit Agrees with Majority View" (Apr. 6, 2026) | https://www.insideclassactions.com/2026/04/06/federal-circuit-agrees-with-majority-view-on-class-representative-incentive-awards/ | Full text via case.dev; 2026-10-30 | Reports Nat'l Veterans Legal Servs. Program v. United States (Fed. Cir. Mar. 20, 2026) permitting incentive awards | Secondary source; opinion not read |

## `[VERIFY]` list

| Statement | Why unconfirmed | What settles it |
|---|---|---|
| Disposition of Isaacson v. Moses, No. 25-1411, after the Nov. 6, 2026 conference | Pending on the check date | Supreme Court docket |
| Federal Circuit service-award holding and reporter citation (Nat'l Veterans Legal Servs. Program) | Known only from a law-firm summary | The opinion |
| Service-award law in the Third, Fourth, Fifth, Sixth, Eighth, Tenth and D.C. Circuits | Not researched for this skill | Controlling circuit opinions |
| Whether a material change after notice requires re-notice and new CAFA notice | Circuit- and fact-dependent | Controlling circuit law and the judge's order |
| Appeal period used to define the Effective Date | Depends on whether a United States party is involved (Fed. R. App. P. 4(a)) | Fed. R. App. P. 4(a) text |
| Local rules, standing orders and judge-specific procedures (for example, opt-out window floors, sealing of blow provisions, fee-motion lead time) | Vary by district and judge | The district's rules and the judge's procedures page |
| Practice of supplementing CAFA notice with later-created materials | Not stated in 1715 | Controlling circuit or district practice |
| State-court class settlements: the state class rule, notice requirements and any state official notice | Outside federal Rule 23 and 1715 | The state's rule and statutes |
