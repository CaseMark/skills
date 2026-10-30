# Primary Sources and Verification Register

## Contents

1. How these sources were checked
2. Cases
3. Rules, regulations and Commission statements
4. Points deliberately not supported by authority
5. `[VERIFY]` list

## How these sources were checked

All checks were made on 2026-10-30. Opinions and rules were read through the case.dev API: `/search/v1/contents` for the full text of official court and agency pages, `/legal/v1/verify` for reporter citations, and `/search/v1/search` to locate sources. "Full text via case.dev" means the opinion or rule was read in full, not a snippet. Justia is an unofficial compilation of official opinions and is labeled as such. CourtListener pages were blocked for text retrieval; citations were still checked against CourtListener through `/legal/v1/verify`. Before advising on any point below, re-read the authority; the agreement in front of you controls over every default described here.

## Cases

| Authority | URL read | Method; date | What it supports | Status |
|---|---|---|---|---|
| CBS Inc. v. Ziff-Davis Publishing Co., 75 N.Y.2d 496 (1990) | https://law.justia.com/cases/new-york/court-of-appeals/1990/75-n-y-2d-496-0.html (Justia copy); citation via /legal/v1/verify | Full text via case.dev; 2026-10-30 | New York: the question is whether the buyer believed it was purchasing the seller's promise, not whether it believed the warranted facts; buyer who closed while disputing the financial statements, expressly preserving its position, could sue (503-504) | Confirmed |
| Galli v. Metz, 973 F.2d 145 (2d Cir. 1992) | https://law.justia.com/cases/federal/appellate-courts/F2/973/145/386424/ (Justia copy); citation via /legal/v1/verify | Full text via case.dev; 2026-10-30 | New York law as applied by the Second Circuit: buyer that closes with full knowledge and acceptance of facts disclosed by the seller that would breach the warranty has waived the breach unless it expressly preserves its rights (151); preservation by express statement (150, as cited in Rogath) | Confirmed; pin 151 confirmed from the quotation in Rogath |
| Rogath v. Siebenmann, 129 F.3d 261 (2d Cir. 1997) | https://law.justia.com/cases/federal/appellate-courts/F3/129/261/621183/ (Justia copy); citation via /legal/v1/verify | Full text via case.dev; 2026-10-30 | Source and extent of the buyer's knowledge decide waiver: seller-disclosed facts and closing without reservation waive; third-party or common knowledge may not | Confirmed; no pin cite used (Justia text has no page markers) |
| Eagle Force Holdings, LLC v. Campbell, 187 A.3d 1209 (Del. 2018) | https://courts.delaware.gov/Opinions/Download.aspx?id=273430 (official slip opinion) | Full text via case.dev; 2026-10-30 | Majority footnote 185 acknowledges the debate on recovery for warranties known to be untrue at signing and says the Court has not resolved it, noting most states follow Ziff-Davis; concurrence says Delaware law "casts doubt" on suing over what the buyer knew to be false | Confirmed (slip op. 47 n.185); reporter pin 1236 n.185 taken from the ABA Business Law Today article below |
| In re Dura Medic Holdings, Inc. Consolidated Litigation, C.A. No. 2019-0474-JTL (Del. Ch. Feb. 20, 2025) | https://courts.delaware.gov/Opinions/Download.aspx?id=375640 (official slip opinion) | Full text via case.dev; 2026-10-30 | Schedule 4.8 disclosed one government audit, not others; disclosure outside the agreement (a diligence call; materials in the data room) "has no bearing" on the contractual rep; integration clause bars extrinsic evidence to vary the rep; breach of a rep does not require justifiable reliance (quoting Cobalt); materiality qualifier excludes de minimis issues (quoting Akorn) | Confirmed; reporter citation `[VERIFY]` |
| Cobalt Operating, LLC v. James Crystal Enters., LLC, 2007 WL 2142926 (Del. Ch. July 20, 2007), aff'd, 945 A.2d 594 (Del. 2008) (table) | Quoted in Dura Medic | Search excerpt (quotation in a full-text opinion); 2026-10-30 | Reps allocate risk; seller cannot avoid them because buyer's diligence did not uncover their falsity | Quotation confirmed in Dura Medic; Cobalt itself not read |
| Akorn, Inc. v. Fresenius Kabi AG, 2018 WL 4719347 (Del. Ch. Oct. 1, 2018), aff'd, 198 A.3d 724 (Del. 2018) | Quoted in Dura Medic; affirmance citation via /legal/v1/verify | Search excerpt; 2026-10-30 | Materiality qualifier in a rep excludes "small, de minimis, and nitpicky issues"; pro-sandbagging reasoning | Quotations confirmed in Dura Medic; Akorn itself not read |
| The Williams Cos. v. Energy Transfer LP, C.A. No. 12168-VCG (Del. Ch. Dec. 29, 2021) (2021 WL 6136723, as cited in Dura Medic) | https://courts.delaware.gov/Opinions/Download.aspx?id=328050 (official slip opinion) | Full text via case.dev; 2026-10-30 | "Reasonably apparent on its face" clause excuses otherwise-breaching action only where facially necessary to permit the activity the exception provides, that is, where an inconsistency would otherwise result; rejected a "logically related" reading; exceptions moved into the disclosure letter applied to the covenants they came from | Confirmed |
| Sam I Aggregator LP v. Mars Holdco Corp., C.A. No. 2023-1217-KSJM (Del. Ch. Aug. 15, 2025) | https://courts.delaware.gov/Opinions/Download.aspx?id=383700 (official slip opinion) | Full text via case.dev; 2026-10-30 | Disclosure letter that defined a former officer's demand as the "allegations" and placed it under the accounting-controls rep expressly qualified that rep; buyer could not narrow it (pleading-stage dismissal of counterclaims) to an employment matter; the letter included a "reasonably apparent" clause | Confirmed |
| BBP Holdco, Inc. v. Brunswick Corp., C.A. No. N20C-10-135 PRW CCLD (Del. Super. July 14, 2025) | https://courts.delaware.gov/Opinions/Download.aspx?id=382310 (official slip opinion) | Full text via case.dev; 2026-10-30 | Article III preamble ("Except as otherwise set forth in the disclosure schedule ...") made each schedule an exception to the reps in that article; Schedule 3.16, naming the regulator, the directive article and the notice, adequately disclosed the written notice | Confirmed |
| Arwood v. AW Site Services, LLC, C.A. No. 2019-0904-JRS (Del. Ch. Mar. 9, 2022) | https://businesslawtoday.org/2025/04/chancery-court-clarifies-delawares-position-on-sandbagging-and-use-of-transaction-multiple-to-calculate-damages/ (ABA Business Law Today, April 10, 2025) | Search excerpt (secondary); 2026-10-30 | "Delaware is, or should be, a pro-sandbagging jurisdiction" (as quoted) | Quoted language from secondary source only; not relied on for any rule |

## Rules, regulations and Commission statements

| Authority | URL read | Method; date | What it supports | Status |
|---|---|---|---|---|
| 17 C.F.R. 229.601(a)(5), (a)(6) and (b)(2)(ii) (Regulation S-K Item 601) | https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.600/section-229.601 | Full text via case.dev; 2026-10-30 | (a)(5): schedules to filed exhibits need not be filed if not material and not otherwise disclosed; list of omitted schedules; copy to the Commission on request. (a)(6): redaction of personal information. (b)(2)(ii): redaction of immaterial, customarily confidential terms of an acquisition agreement, with marking and supplemental-copy requirements | Confirmed (current eCFR text) |
| SEC Report of Investigation under Section 21(a), Release No. 34-51283 (Mar. 1, 2005) (Titan) | https://www.sec.gov/litigation/investreport/34-51283.htm | Full text via case.dev; 2026-10-30 | Reps in an agreement included in a public disclosure document are disclosure to investors; the issuer must consider whether additional material facts are needed so they are not misleading | Confirmed |
| Fed. R. Evid. 801(d)(2) | https://www.law.cornell.edu/rules/fre/rule_801 | Full text via case.dev; 2026-10-30 | A party's own statement, or one it adopted or authorized, offered against it is not hearsay | Confirmed; state evidence rules not checked |

## Points deliberately not supported by authority

These are drafting practice, stated as such in the skill: the standard general-terms provisions and each side's usual position; the description checklist; the RWI exclusions for known and interim breaches (policy-specific); the severity scale; the indemnity arithmetic format. Fed. R. Evid. 502 was read and not used: it governs disclosures in federal proceedings or to federal agencies, not a voluntary disclosure to a deal counterparty.

## `[VERIFY]` list

| Statement | Why unconfirmed | What settles it |
|---|---|---|
| Whether disclosing privileged advice to a buyer in a schedule waives the privilege, and whether a common-interest doctrine protects deal-related sharing | Varies by jurisdiction; not researched | Controlling law of the forum and governing law |
| Buyer-knowledge (sandbagging) default in states other than New York and Delaware | Not researched | Governing state's appellate decisions |
| Delaware Supreme Court resolution of the sandbagging question | Reserved in Eagle Force n.185; Chancery decisions since then are pro-sandbagging | A later Delaware Supreme Court decision |
| Reporter citation for Dura Medic (333 A.3d 227 appears in a case database) | `/legal/v1/verify` returned not found | Atlantic Reporter or Westlaw check |
| Reporter pin 1236 n.185 for Eagle Force | Footnote text read in the slip opinion; page from a secondary source | Atlantic Reporter check |
