# Primary Sources and Verification Register

Checked October 30, 2026. Full texts were read through the case.dev contents API (`/search/v1/contents`) unless the row says "search excerpt". Federal Register page pinpoints were located from the GPO page markers in the full text and are accurate to the page. Re-check any state statute and the Security Rule rulemaking status before relying on them for a live incident.

## Contents

1. Sources checked
2. Confirmed statements
3. Corrections made to the earlier skill text
4. `[VERIFY]` list

## 1. Sources checked

| Source | URL read | Method; date | Supports |
|---|---|---|---|
| 45 C.F.R. part 164 subpart D (164.400-414), eCFR | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D | Full text via case.dev; 2026-10-30 | Breach definition and exceptions; four factors; unsecured PHI; discovery and imputed knowledge; 60-day limits; content; substitute notice; media (more than 500); HHS (500 or more contemporaneous; fewer than 500 within 60 days after year end); BA notice; law enforcement delay; burden of proof |
| 45 C.F.R. 164.530, eCFR | https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.530 | Full text via case.dev; 2026-10-30 | Mitigation (f); documentation to meet the 164.414(b) burden (j)(1)(iv); six-year retention (j)(2) |
| HHS, Breach Notification Rule overview (last reviewed July 26, 2013) | https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html | Full text via case.dev; 2026-10-30 | Three exceptions in plain terms; option to notify without a risk assessment; delegation of individual notice to a BA; documentation of the burden |
| HHS, Guidance to Render Unsecured PHI Unusable, Unreadable, or Indecipherable (last reviewed July 26, 2013) | https://www.hhs.gov/hipaa/for-professionals/breach-notification/guidance/index.html | Full text via case.dev; 2026-10-30 | Encryption (164.304 definition, key not breached, keys stored separately; NIST SP 800-111, 800-52, 800-77, 800-113, FIPS 140-2) and destruction (NIST SP 800-88; redaction excluded) |
| HHS OCR, Fact Sheet: Ransomware and HIPAA (July 11, 2016) | https://www.hhs.gov/sites/default/files/RansomwareFactSheet.pdf | Full text via case.dev; 2026-10-30 | Ransomware encryption is an acquisition; breach presumed unless low probability shown; forensic factors; full-disk encryption decrypts transparently while the device is on |
| HHS, Submitting Notice of a Breach to the Secretary (last reviewed Feb. 13, 2026) | https://www.hhs.gov/hipaa/for-professionals/breach-notification/breach-reporting/index.html | Full text via case.dev; 2026-10-30 | Portal for HIPAA and Part 2 breaches; 500 or more: no later than 60 calendar days from discovery; fewer than 500: within 60 days after year end, may file earlier; estimates and addenda; a BA or QSO may submit on the entity's behalf |
| Breach Notification interim final rule, 74 FR 42740 (Aug. 24, 2009) | https://www.govinfo.gov/content/pkg/FR-2009-08-24/pdf/E9-20169.pdf | Full text via case.dev; 2026-10-30 | Clock starts when the incident is first known, not when the investigation ends; 60 days an outer limit (42750); billing-employee and receptionist examples (42747-48); media counting examples and "jurisdiction" (42753) |
| HIPAA Omnibus final rule, 78 FR 5566 (Jan. 25, 2013) | https://www.govinfo.gov/content/pkg/FR-2013-01-25/pdf/2013-01073.pdf | Full text via case.dev; 2026-10-30 | Agency test for BAs (5582); exceptions must be documented (5641); every factor addressed, good-faith assessment (5644); no delay waiting for a lost device (5647); media counting example (5654); BA agent discovery imputed (5656); law enforcement delay tolls the clocks (5658) |
| 42 C.F.R. 2.16 and 2.11, eCFR | https://www.ecfr.gov/current/title-42/chapter-I/subchapter-A/part-2/subpart-B/section-2.16 and .../section-2.11 | Full text via case.dev; 2026-10-30 | 2.16(b) applies part 160 and subpart D to Part 2 programs "in the same manner"; definitions of breach and unsecured record |
| Part 2 final rule, 89 FR 12472 (Feb. 16, 2024) | https://www.federalregister.gov/documents/2024/02/16/2024-02544/confidentiality-of-substance-use-disorder-sud-patient-records | Full text via case.dev; 2026-10-30 | Effective April 16, 2024; compliance February 16, 2026; no breach duty on QSOs (programs should contract for it; printed page 12520 and the alternatives discussion) |
| HHS press release, OCR civil enforcement program for Part 2 (Feb. 13, 2026) | https://www.hhs.gov/press-room/hhs-announce-civil-enforcement-program-sud-patient-records.html | Full text via case.dev; 2026-10-30 | OCR accepts Part 2 complaints and breach notifications from February 16, 2026 |
| HIPAA Security Rule NPRM, 90 FR 898 (Jan. 6, 2025) | https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information | Full text via case.dev; 2026-10-30 | Proposed 24-hour BA report of contingency plan activation, stated not to alter breach reporting; proposed 72-hour restoration |
| Unified Agenda entry, RIN 0945-AA22 | https://www.reginfo.gov/public/do/eAgendaViewRule?RIN=0945-AA22&operation=OPERATION_PRINT_RULE&pubId=202510 | Full text via case.dev; 2026-10-30 | Stage: Long-Term Actions; NPRM 01/06/2025; final action 07/00/2027 |
| Secondary reports on the Security Rule timetable (McDermott client alert, July 16, 2026; VertiComply, Oct. 12, 2026) | https://www.mcdermottlaw.com/insights/final-action-on-hipaa-security-rule-modifications-now-projected-for-july-2027/ ; https://verticomply.com/blog/hipaa-security-rule-update-2026-status | Full text via case.dev; 2026-10-30 | Cross-check only: no final rule published as of Oct. 12, 2026 |
| HHS OCR bulletin, Use of Online Tracking Technologies by HIPAA Covered Entities and Business Associates (with the court notice at the top) | https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html | Full text via case.dev; 2026-10-31 | Authenticated-page tracking generally has access to PHI; Am. Hosp. Ass'n v. Becerra, No. 4:23-cv-1110 (N.D. Tex. June 20, 2024) vacated the IP-address-plus-unauthenticated-page portion; HHS evaluating next steps; FTC HBNR may apply to non-HIPAA apps |
| 16 C.F.R. part 318, eCFR | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-318 | Full text via case.dev; 2026-10-30 | Scope; breach of security (includes unauthorized disclosure; access presumed acquisition); discovery; 60-day limits; FTC timing; media 500 or more; content; service provider notice |
| FTC HBNR amendments, 89 FR 47028 (May 30, 2024) | https://www.govinfo.gov/content/pkg/FR-2024-05-30/html/2024-10855.htm | Full text via case.dev; 2026-10-30 | Amendments effective July 29, 2024 |
| Cal. Civ. Code 1798.82 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.82 | Full text via case.dev; 2026-10-30 | 30 calendar days (SB 446, Stats. 2025, ch. 319, effective Jan. 1, 2026); AG sample copy within 15 days if more than 500 residents; (e) covered-entity content clause; encrypted data with compromised key |
| Cal. Health & Safety Code 1280.15 | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=HSC&sectionNum=1280.15 | Full text via case.dev; 2026-10-30 | 15 business days after detection to CDPH and patient; internal misdirection carve-out; law enforcement delay; penalties |
| N.Y. Gen. Bus. Law 899-aa | https://www.nysenate.gov/legislation/laws/GBS/899-AA | Full text via case.dev; 2026-10-30 | 30 days; medical and health insurance information; HIPAA-notice clause (2)(b); AG within 5 business days of HHS notice (9); inadvertent-disclosure determination (2)(a); (8)(a) recipients: AG, Department of State, State Police, and DFS only for 23 NYCRR 500.1 covered entities (re-read 2026-10-31) |
| Tex. Bus. & Com. Code 521.053 | https://statutes.capitol.texas.gov/Docs/BC/htm/BC.521.htm | Full text via case.dev; 2026-10-30, re-read 2026-10-31 | 60th day after determination, except law enforcement delay or as necessary to determine scope and restore integrity; AG by the 30th day after determination if at least 250 residents; health information is sensitive personal information |
| Wash. Rev. Code 19.255.005, .010, .030 | https://app.leg.wa.gov/RCW/default.aspx?cite=19.255.010 (and .005, .030) | Full text via case.dev; 2026-10-30, re-read 2026-10-31 | 30 days to residents, with delay for law enforcement or measures to determine scope and restore integrity; AG within 30 days if more than 500 residents; risk-of-harm exception; covered-entity deemed compliance with HITECH timing for AG notice |

## 2. Confirmed statements

| Statement | Where |
|---|---|
| Media notice requires more than 500 residents of a State or jurisdiction; HHS contemporaneous notice requires 500 or more in total | 164.406(a), 164.408(b) |
| A breach is discovered on the first day known, or that would have been known with reasonable diligence, to any workforce member or agent other than the wrongdoer | 164.404(a)(2) |
| The clock does not wait for the investigation to end | 74 FR 42750; Omnibus preamble |
| Each of the four factors must be addressed | 78 FR 5644 |
| Encryption is a safe harbor only if the key or process has not been breached | HHS guidance |
| Ransomware encryption of ePHI is an acquisition; breach presumed unless low probability shown | HHS ransomware fact sheet |
| Part 2 programs must give breach notice under subpart D from February 16, 2026 | 42 C.F.R. 2.16(b); 89 FR 12472; HHS press release |
| Security Rule NPRM is not final; final action projected July 2027 | Unified Agenda RIN 0945-AA22 |
| FTC rule: media at 500 or more; access presumed acquisition; no low-probability test | 16 C.F.R. 318.2, 318.3, 318.5 |

## 3. Corrections made to the earlier skill text

| Item | Before | After |
|---|---|---|
| HHS notice for 500 or more | "Contemporaneously with individual notice" only | Contemporaneous with individual notice under 164.408(b); HHS page also states no later than 60 days from discovery |
| State timelines | "30 days in some states"; Texas cited to Health & Safety Code 181.202 | Specific verified rows (CA, NY, TX, WA) with their own triggers; Texas breach notice is Bus. & Com. Code 521.053 |
| Encryption | Encryption equals safe harbor | Safe harbor only with compliant encryption and an uncompromised key; device state matters |
| Part 2 | Listed only as a sensitive data category | Separate regime under 42 C.F.R. 2.16(b) |

## 4. `[VERIFY]` list

1. State breach statutes other than California, New York, Texas and Washington: deadlines, attorney general thresholds, whether paper records are covered, and HIPAA deemed-compliance clauses.
2. Whether Cal. Civ. Code 1798.82(a)(2)'s 30-day timing applies to a HIPAA covered entity (the text of (e) exempts only the (d) content rules; no Attorney General guidance was read).
3. State holiday calendars for business-day clocks (New York 5 business days; California 15 business days).
4. How days are counted after a 164.412 law enforcement delay ends (the preamble says the delay tolls the clock; the counting method is not stated).
5. Whether, for a covered entity that is also a Part 2 program, impermissibility of a use or disclosure of Part 2 records is measured against Part 2's rules (2.16(b) applies subpart D "in the same manner"; the preamble on this point was not read in full).
6. The Texas "date on which the person determines that the breach occurred" and the Washington risk-of-harm standard: no agency rule or guidance defining them was read.
7. Security Rule rulemaking: content and dates of any final rule (projected July 2027).
8. HHS portal form fields and addendum procedure beyond the breach reporting page.
9. Whether a state deadline falling on a weekend or holiday rolls forward under that state's general construction law (federal subpart D and 16 C.F.R. Part 318 do not roll).
10. How far the Texas, Washington and California "determine the scope and restore integrity" delay reaches past the stated day.
11. Whether a HIPAA notice sent after day 30 satisfies New York's 30-day resident rule through 899-aa(2)(b).
12. HHS's next steps on the tracking technologies bulletin after the June 2024 vacatur.
