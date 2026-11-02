# AML Reporting Rules for Transaction Testing

## Contents

1. SAR threshold and filing clock by institution type
2. Clocks and windows table, one trigger per element
3. Determination, not the alert, starts the SAR clock
4. Continuing activity and no-SAR documentation are elections
5. CTRs, aggregation across branches and linked accounts, exemptions
6. Structuring
7. Section 314(a) matches
8. Confidentiality, tipping off and permitted channels

Citations are to 31 C.F.R. unless stated. Each rule was read in full on 2026-10-30 or 2026-10-31; URLs and methods are in `references/primary-sources.md`. Program and policy design under these rules belongs to aml-compliance-program; this file is used to test transactions, alerts, cases and filings against them.

## 1. SAR threshold and filing clock by institution type

| Institution type | SAR rule | Mandatory threshold | Extra 30 days if no suspect identified? |
|---|---|---|---|
| Bank, savings association, credit union | 1020.320(a)(2), (b)(3) | $5,000 | Yes, never more than 60 days from initial detection |
| Money services business: dealer in foreign exchange, issuer or seller of traveler's checks or money orders, provider or seller of prepaid access, money transmitter, U.S. Postal Service (1022.320(a)(1) lists 1010.100(ff)(1), (3)-(7)) | 1022.320(a)(2), (b)(3) | $2,000; $5,000 only where a money order or traveler's check issuer identifies the activity from clearance records (1022.320(a)(3)) | No. 30 calendar days from initial detection, with no extension |
| Check casher (1010.100(ff)(2)) | Not listed in 1022.320(a)(1) | No mandatory SAR rule; voluntary filing permitted (1022.320(a)(1)) | Not applicable |
| Broker-dealer | 1023.320 | $5,000 | Yes |
| Mutual fund, insurance company, FCM or IB, loan or finance company | 1024.320, 1025.320, 1026.320, 1029.320 (confirmed by sibling aml-compliance-program) | $5,000 | Yes |

Bank agency tiers. The banking agencies' own SAR rules add tiers that 1020.320 does not contain. For a national bank, 12 C.F.R. 21.11(c) requires a SAR for insider abuse in any amount, for $5,000 or more where a suspect can be identified, for $25,000 or more regardless of potential suspects, and for $5,000 or more involving potential money laundering or BSA violations. The FDIC rule is 12 C.F.R. part 353; the Federal Reserve's is 12 C.F.R. 208.62; the NCUA's is 12 C.F.R. 748.1. Cite the $25,000 tier to the agency rule, never to 1020.320, and never apply it to an MSB.

Voluntary SARs below any threshold are permitted under every rule above. A threshold limits the duty to file; it never makes suspicious activity below it "explained".

## 2. Clocks and windows table, one trigger per element

| Element | Trigger event | Period | Rule |
|---|---|---|---|
| SAR (bank, broker-dealer, mutual fund, insurer, FCM/IB, loan or finance company) | Initial detection of facts that may constitute a basis for filing: the date the institution, in its review or otherwise, knows or has reason to suspect the activity meets a SAR definition | 30 calendar days | 1020.320(b)(3) and analogs; FFIEC manual, SAR section |
| Same, no suspect identified on the detection date | Same detection date | Up to 30 more days to identify a suspect; never more than 60 days from detection | Same |
| SAR (MSB) | Initial detection of facts | 30 calendar days, no extension | 1022.320(b)(3) |
| Immediate telephone notice to law enforcement | A violation requiring immediate attention, such as an ongoing money laundering scheme | Immediately, in addition to a timely SAR | 1020.320(b)(3); 1022.320(b)(3) |
| Continuing-activity SAR (only if the institution elects the guidance cadence) | Filing date of the prior related SAR | 90-day review period starting the day after that filing; file by day 120 after the prior filing | Interagency SAR FAQs Q2-Q3 (Oct. 9, 2025) |
| Alert review | Alert generation | No regulatory period; a reasonable time set by the institution's procedure and measured | FFIEC manual, SAR section |
| CTR | Business day of the reportable transaction (night, weekend and holiday deposits count on the next business day) | File within 15 days following that day | 1010.306(a)(1); 1010.313(b) |
| CTR exemption designation (FinCEN Form 110, where required) | First reportable transaction to be exempted | By the close of the 30-calendar-day period beginning after that day | 1020.315(c)(1) |
| CTR exemption eligibility review | Prior review | At least once each year | 1020.315(d) |
| 314(a) match report | Posting of FinCEN's request | In the manner and time frame the request specifies (FFIEC manual: within 14 days of posting unless the request says otherwise) | 1010.520(b)(3)(ii) |
| Lookback report | The order, agreement or engagement letter that requires it | As that document states | The document itself (an unknown fact until supplied) |

Show every computed date with its weekday. No rule read moves a SAR due date that falls on a weekend or federal holiday; treat roll-forward as unsettled and recommend filing by the last business day before the date. A date that has passed is past due under either reading when the next business day has also passed.

## 3. Determination, not the alert, starts the SAR clock

- The FFIEC manual: "initial detection" is not the moment a transaction is highlighted for review; the period starts when the institution, during its review or because of other factors, knows or has reason to suspect the activity meets one or more SAR definitions.
- Test each filed SAR against the determination date shown in the case record (investigator conclusion, escalation memo, committee minute). A case-closure date, a QA sign-off date or a SAR-drafting date is not the trigger.
- An alert date is not the trigger either, so a SAR filed more than 30 days after the alert but within 30 days of determination is timely. Test the gap between alert and determination separately against the institution's review time standard; a long gap is a timeliness-of-review finding, not a late SAR.
- If no determination date is evidenced, the timeliness label is "Not determinable"; request the record rather than assuming the alert or closure date.

## 4. Continuing activity and no-SAR documentation are elections

- No separate post-SAR review of a customer or account is required; risk-based monitoring may be relied on (SAR FAQs Q2, Oct. 9, 2025).
- If the institution elects the guidance cadence: day 0 detection, day 30 initial SAR, day 120 end of the 90-day period, day 150 continuing SAR; with no suspect, days 60, 150 and 180 (FAQ Q3). Anchor to the prior SAR's filing date, never to detection.
- No requirement or expectation exists to document a decision not to file (FAQ Q4). The FFIEC manual's SAR section still says banks should document no-file decisions, and carries a banner telling examiners to refer to the 2021 and 2025 FAQs. Name the conflict; the FAQ is the later interagency statement. Where the institution's own procedure requires a no-file rationale, test compliance with that procedure and label it a policy election.
- Near-threshold cash activity alone is not a SAR basis without knowledge, suspicion or reason to suspect evasion (FAQ Q1). It remains a reason to review, and the review's conclusion is what is tested.

## 5. CTRs, aggregation across branches and linked accounts, exemptions

- A CTR is required for each deposit, withdrawal, exchange or other payment or transfer in currency of more than $10,000 (1010.311). Exactly $10,000 is not reportable on its own.
- A financial institution includes all its domestic branches (1010.313(a)). Multiple currency transactions are one transaction when the institution knows they are by or on behalf of any person and total more than $10,000 cash in, or cash out, in one business day (1010.313(b)). Cash in and cash out are not netted.
- Aggregation follows the person, not the account or branch: deposits a customer makes at two branches into two of the customer's accounts, including ATM deposits, aggregate. A system that aggregates per account or per branch misses these.
- Businesses with a common owner: separately incorporated businesses are presumed independent and are not aggregated merely because one person owns them; where they are not operated independently (same staff and address, one pays the other's or the owner's expenses), aggregation is appropriate going forward (FinCEN FIN-2012-G001 as summarized in the FFIEC manual, CTR section).
- Exemptions (banks only, 1020.315): exempt person categories in (b); Form 110 designation within 30 days; annual eligibility review; ineligible businesses in (e)(8); no exemption where the exempt person acts as agent for another beneficial owner (f). Exemption does not relieve SAR duties; a sharp increase in an exempt customer's cash can trigger a SAR, and the bank must keep a monitoring system for non-listed business and payroll customer accounts (1020.315(h)). Test exempt customers' cash in the monitoring population.
- Retention: CTR copies five years from the report (1010.306(a)(2)).

## 6. Structuring

- Structuring is conducting or attempting one or more currency transactions, in any amount, at one or more institutions, on one or more days, in any manner, to evade CTR reporting; the transactions need not exceed $10,000 at any single institution on any single day (1010.100(xx)). Structuring and assisting in structuring are prohibited (1010.314; 31 U.S.C. 5324(a)).
- A single-transaction rule (cash over $10,000) or a per-account daily aggregate cannot detect it. Test with multi-day, multi-branch, multi-account and multi-conductor views of the same person.
- A SAR is required where the institution knows, suspects or has reason to suspect the transactions are designed to evade (1020.320(a)(2)(ii); 1022.320(a)(2)(ii), which says "whether through structuring or other means"). Evidence beyond amounts (a question about the reporting threshold, splitting across tellers or branches, refusing ID) is what supplies the reason to suspect.
- For MSBs, splitting funds transfers to stay under the $3,000 recordkeeping amount in 1010.410(e) is an attempt to evade a requirement of Chapter X.

## 7. Section 314(a) matches

- On a FinCEN request, search, unless the request says otherwise, current accounts of a named suspect, accounts maintained in the preceding 12 months, and recorded transactions and funds transmittals in the preceding 6 months (1010.520(b)(3)(i)); report matches in the manner and time frame the request specifies (1010.520(b)(3)(ii)).
- A match is not by itself a basis for a SAR, and the request should not be the sole basis to close or keep an account (FFIEC manual, Information Sharing, citing FinCEN's 314(a) FAQs). A match is a reason to review the subject's activity under the SAR procedure; a match confirmed to FinCEN and never referred for review is a finding.
- Use the request only to report to FinCEN, to decide on accounts or transactions, or to comply with Chapter X; never disclose that FinCEN requested or obtained information, except to FinCEN, the requesting agency or the named contact (1010.520(b)(3)(iv)).

## 8. Confidentiality, tipping off and permitted channels

- A SAR, and any information that would reveal one, is confidential (1020.320(e); 1022.320(d)). No current or former director, officer, employee, agent or contractor may notify any person involved in the transaction that it was reported (31 U.S.C. 5318(g)(2)(A)).
- Permitted: disclosure to FinCEN, law enforcement and BSA examining regulators; sharing underlying facts and documents (not the SAR) with another institution for a joint SAR; sharing within the corporate structure as regulation or guidance permits.
- Test work papers, QA comments, customer letters and relationship-manager notes for SAR references. A closure or exit letter states a business reason or none.
- Retention: SAR copies and supporting documentation five years from filing (1020.320(d); 1022.320(c)).
