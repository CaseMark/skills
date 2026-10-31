# Primary Sources and Verification Register

## Contents

1. How these sources were checked
2. Statutes and FinCEN regulations
3. Bank agency rules and state rule
4. Guidance, FAQs and the FFIEC manual
5. Model risk guidance status
6. Rule status notes
7. Corrections to the prior version of this skill
8. Disposition of the former AML-RED-FLAGS.md
9. `[VERIFY]` list

## 1. How these sources were checked

Checked on 2026-10-30 and 2026-10-31 through the case.dev research API: `/search/v1/contents` to read a page or PDF in full ("full text via case.dev") and `/search/v1/search` to locate documents. eCFR pages are the current point-in-time view (not the official edition); Cornell LII pages are unofficial compilations and are labeled as mirrors where used. Items marked "sibling-confirmed" were read in full by the reviewed legal skill aml-compliance-program on 2026-10-30 and are relied on without re-reading. Re-read the current eCFR text of any rule before a report goes to a regulator.

## 2. Statutes and FinCEN regulations

| Authority | URL read | Method; date | What it supports |
|---|---|---|---|
| 31 U.S.C. 5318(g)(2)(A) | law.cornell.edu/uscode/text/31/5318 (mirror) | Full text via case.dev; 2026-10-30 | No notification to any person involved that a transaction was reported, by current or former personnel or contractors |
| 31 U.S.C. 5324(a) | law.cornell.edu/uscode/text/31/5324 | Sibling-confirmed | Structuring and assisting in structuring prohibited |
| 31 C.F.R. 1010.100(ff), (xx) | ecfr.gov/current/title-31/subtitle-B/chapter-X/part-1010/subpart-A/section-1010.100 | Full text via case.dev; 2026-10-30 | MSB categories (ff)(1)-(7), check casher at (ff)(2); structuring in any amount, at one or more institutions, on one or more days; need not exceed $10,000 at one institution on one day |
| 1010.306(a) | ecfr.gov ... part-1010/subpart-C/.../section-1010.306 | Full text via case.dev; 2026-10-30 | CTR within 15 days following the transaction day; copies kept five years from the report |
| 1010.311 | ecfr.gov ... section-1010.311 | Full text via case.dev; 2026-10-30 | CTR for currency transactions of more than $10,000 |
| 1010.313 | ecfr.gov ... section-1010.313 | Full text via case.dev; 2026-10-30 | All domestic branches; multiple transactions by or on behalf of any person over $10,000 cash in or cash out in one business day; night, weekend and holiday deposits on the next business day |
| 1010.314 | ecfr.gov ... section-1010.314 | Full text via case.dev; 2026-10-30 | No structuring, assisting, or causing failure to file or a false CTR |
| 1010.410(e) | ecfr.gov ... section-1010.410 | Sibling-confirmed | Nonbank transmittal-of-funds records at $3,000 or more |
| 1010.520(b)(3) | ecfr.gov ... part-1010/subpart-E/section-1010.520 | Full text via case.dev; 2026-10-30 | 314(a) search scope (current accounts, prior 12 months, transactions in prior 6 months unless the request says otherwise); report in the manner and time frame the request specifies; one contact; use and nondisclosure limits |
| 1020.315 | ecfr.gov ... part-1020/subpart-C/section-1020.315 | Full text via case.dev; 2026-10-30 | Exempt persons; Form 110 within 30 days; annual review; ineligible businesses; agent limitation; SAR duty and monitoring system for exempt accounts (h) |
| 1020.320 | ecfr.gov ... part-1020/subpart-C/section-1020.320 | Full text via case.dev; 2026-10-30 | $5,000; three SAR definitions; 30 days from initial detection, 30 more if no suspect, never more than 60; immediate telephone notice; five-year retention; confidentiality |
| 1022.320 | ecfr.gov ... part-1022/subpart-C/section-1022.320 | Full text via case.dev; 2026-10-30 | (a)(1) MSB categories required to file (not check cashers); (a)(2) $2,000 and four definitions including structuring "or other means"; (a)(3) $5,000 for clearance-record review; (b)(3) 30 days, no extension; (c) retention; (d) confidentiality |
| 1023.320 | ecfr.gov ... part-1023/subpart-C/section-1023.320 | Full text via case.dev; 2026-10-30 | Broker-dealer $5,000; 30 days, 60 if no suspect |
| 1024.320, 1025.320, 1026.320, 1029.320 | ecfr.gov sections named | Sibling-confirmed | $5,000; 30 days, 60 if no suspect |

## 3. Bank agency rules and state rule

| Authority | URL read | Method; date | What it supports |
|---|---|---|---|
| 12 C.F.R. 21.11(c) (OCC) | ecfr.gov/current/title-12/chapter-I/part-21/subpart-B/section-21.11 | Full text via case.dev; 2026-10-30 | Insider abuse any amount; $5,000 with a suspect; $25,000 regardless of suspects; $5,000 for money laundering or BSA violations |
| 12 C.F.R. 353.3 (FDIC) | ecfr.gov/current/title-12/chapter-III/subchapter-B/part-353/section-353.3 | Full text via case.dev; 2026-10-30 | Same tiers including $25,000 regardless of suspects; 30 calendar days from initial detection |
| 3 NYCRR 504.3 (New York DFS) | law.cornell.edu/regulations/new-york/3-NYCRR-504.3 (mirror) | Full text via case.dev; 2026-10-30 | Transaction monitoring program attributes for DFS-regulated institutions: detection scenarios with thresholds, end-to-end pre- and post-implementation testing, documentation of parameters and thresholds, ongoing analysis of relevance. State-variable; applies only to DFS-regulated institutions |

## 4. Guidance, FAQs and the FFIEC manual

| Document | URL read | Method; date | What it supports |
|---|---|---|---|
| Interagency SAR FAQs (FinCEN, Federal Reserve, FDIC, NCUA, OCC), Oct. 9, 2025 | federalreserve.gov/supervisionreg/srletters/SR2504a1.pdf | Full text via case.dev; 2026-10-30 | Q1 near-threshold activity alone is not a SAR basis, structuring definition, monitoring commensurate with risk; Q2 no separate continuing-activity review required; Q3 elective cadence, continuing SAR 120 days after the prior filing (day 150), no-suspect variant (day 180); Q4 no requirement or expectation to document a no-file decision |
| FFIEC BSA/AML Examination Manual, Suspicious Activity Reporting | bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04 | Full text via case.dev; 2026-10-30 | Banner: section to be updated for the 2021 and 2025 FAQs; five monitoring components; filtering criteria and thresholds documented, periodically tested, programming independently validated; change control; managing alerts; initial detection is not the moment a transaction is flagged; clock starts on knowing or reason to suspect; review in a reasonable period; law enforcement inquiry prompts review; still says to document no-file decisions |
| FFIEC manual, Currency Transaction Reporting | .../AssessingComplianceWithBSARegulatoryRequirements/05 | Full text via case.dev; 2026-10-30 | Branch aggregation; ATM and other transaction types; FIN-2012-G001 common-ownership presumption and when to aggregate; 15 calendar days |
| FFIEC manual, Transactions of Exempt Persons | .../AssessingComplianceWithBSARegulatoryRequirements/06 | Full text via case.dev; 2026-10-30 | Exemption administration consistent with 1020.315 |
| FFIEC manual, Special Information Sharing Procedures | .../AssessingComplianceWithBSARegulatoryRequirements/07 | Full text via case.dev; 2026-10-30 | 314(a) lists every two weeks; report matches within 14 days of posting or as the request specifies; no SAR solely because of a match; not the sole basis for account decisions; nondisclosure |
| FFIEC manual, BSA/AML Independent Testing | bsaaml.ffiec.gov/manual/AssessingTheBSAAMLComplianceProgram/03 | Full text via case.dev; 2026-10-30 | Who may test; outside parties not involved in other BSA functions; report to board or outside-director committee; no regulatory frequency; document transaction testing |

## 5. Model risk guidance status

| Document | URL read | Method; date | What it supports |
|---|---|---|---|
| SR 26-2 and Revised Guidance on Model Risk Management (Apr. 17, 2026) | federalreserve.gov/supervisionreg/srletters/SR2602.pdf | Full text via case.dev; 2026-10-30 | Supersedes SR 11-7 (Apr. 4, 2011) and SR 21-8 (Apr. 9, 2021, BSA/AML systems); not enforceable standards; most relevant above $30 billion; "model" excludes deterministic rule-based processes; validation, outcomes analysis, ongoing monitoring, vendor products |
| OCC News Release 2026-29 (Apr. 17, 2026) | occ.gov/news-issuances/news-releases/2026/nr-occ-2026-29.html | Full text via case.dev; 2026-10-30 | Rescinds OCC Bulletins 2011-12 and 2021-19, Bulletin 1997-24 and the Model Risk Management booklet; RFI on AI planned |
| FDIC press release (Apr. 17, 2026) | fdic.gov/news/press-releases/2026/agencies-issue-revised-model-risk-guidance | Full text via case.dev; 2026-10-30 | Rescinds FIL-22-2017 and FIL-27-2021 |
| OCC Bulletin 2025-26 (Oct. 6, 2025) | occ.gov/news-issuances/bulletins/2025/bulletin-2025-26.html | Full text via case.dev; 2026-10-30 | Community banks not required to validate models annually |

## 6. Rule status notes

| Item | Source | Method; date | Status |
|---|---|---|---|
| FinCEN AML/CFT program rule, 91 FR 18704 (Apr. 10, 2026), FR Doc. 2026-07033 | federalregister.gov/index/2026/financial-crimes-enforcement-network | Full text via case.dev; 2026-10-31 (page "as of October 30, 2026") | Listed only as a proposed rule; not in effect. As proposed, a final rule would take effect 12 months after issuance (sibling-confirmed). Program design under it belongs to aml-compliance-program |
| OFAC Syrian Sanctions Regulations, 31 C.F.R. part 542 | govinfo.gov/content/pkg/FR-2025-08-26/html/2025-16324.htm | Full text via case.dev; 2026-10-30 | Removed effective Aug. 26, 2025; the former reference's country list named Syria as comprehensively sanctioned |

## 7. Corrections to the prior version of this skill

| Prior text | Correction | Source |
|---|---|---|
| "No dollar minimum for MSBs" | $2,000 (1022.320(a)(2)); $5,000 for issuer clearance-record review; check cashers have no mandatory SAR rule | 1022.320 |
| "$25,000+ with no identified suspect (banks)" stated as the SAR rule | That tier is in the banking agencies' rules (12 C.F.R. 21.11(c)(3), 353.3), not 1020.320 | 21.11; 353.3; 1020.320 |
| 60-day extension for an unidentified suspect, stated for all | Not available to MSBs | 1022.320(b)(3) |
| "Continuation SAR is due on the 90-day cycle"; "Continuing SARs every 90 days" | Continuing review elective; if elected, continuing SAR 120 days after the prior filing | SAR FAQs Q2-Q3 |
| "Document rationale for every disposition" | No requirement to document a no-file decision; an institution may elect to | SAR FAQs Q4 |
| "30 calendar days from initial detection" with detection undefined | Detection is the determination, not the alert or case closure | FFIEC manual, SAR section |
| OFAC-sanctioned countries listed including Syria | Country lists dropped; check current OFAC programs on the review date | 2025-16324 |

## 8. Disposition of the former AML-RED-FLAGS.md

The former reference was merged into `references/testing-methods-and-typologies.md`, sections 8 and 9, and deleted.

| Former content | Disposition | Where now |
|---|---|---|
| Ten typology categories and their indicators | Kept (condensed to one row per category) | Methods file, section 8 |
| Severity classification guide and the cluster note | Kept | Methods file, section 9 |
| "Usage" note tying the file to Step 2 | Moved | SKILL.md Step 4 |
| Named comprehensively sanctioned countries (North Korea, Iran, Cuba, Syria, Crimea) | Dropped as wrong (Syria regulations removed 2025) and as stale-prone | Instruction to check current OFAC and FATF lists |
| FinCEN advisory number for human trafficking | Dropped as unverified; typology kept | Methods file, section 8 |
| "Within 24-48 hours" rapid movement window | Kept as an indicator, not a rule | Methods file, section 8 |

## 9. `[VERIFY]` list

| Statement | Why unconfirmed | What settles it |
|---|---|---|
| Whether a SAR due date on a weekend or federal holiday moves to the next business day | No rule read addresses it (also open in aml-compliance-program) | FinCEN SAR filing instructions or FAQ |
| Text of FinCEN's 314(a) FAQs and FIN-2012-G001 | Read only as summarized in the FFIEC manual | FinCEN documents |
| SAR narrative content standards beyond the FFIEC manual's SAR quality passage | FFIEC Appendix L and FinCEN narrative guidance not read | Those documents |
| SAR rules for casinos, card clubs and housing GSEs (1021.320, 1030.320) | Not read | eCFR |
| Federal Reserve 12 C.F.R. 208.62 and NCUA 748.1 tiers | Not read; OCC and FDIC tiers read | eCFR |
| NYDFS Part 504 provisions beyond 504.3 (annual certification) | Not read | 3 NYCRR 504.4 |
| Current OFAC program list and FATF high-risk lists on a review date | Change frequently | OFAC and FATF websites on the date |
| Any later FFIEC manual revision of the SAR section to reflect the 2025 FAQs | Banner says an update is pending | bsaaml.ffiec.gov |
| The agencies' planned request for information on model risk and AI | Announced, not located | Federal Register |
