# Primary Sources and Verification Register

Checked October 30, 2026. Full texts were read through the case.dev API (`/search/v1/contents`) unless the method says otherwise. The ICD-10 MS-DRG V44 Definitions Manual is published as HTML pages on cms.gov; the pages named below were read individually, not the whole manual. AHA Coding Clinic is paywalled and was not read. Re-check before relying on a rule for a submitted claim or an appeal.

## Contents

1. Sources checked
2. Confirmed statements
3. Corrections made to the earlier version of this skill
4. `[VERIFY]` list

## 1. Sources checked

| Source | URL read | Method; date | Supports |
|---|---|---|---|
| FY 2027 IPPS/LTCH PPS final rule, CMS-1849-F, 91 FR 49570 (Aug. 4, 2026), effective Oct. 1, 2026 | https://www.govinfo.gov/content/pkg/FR-2026-08-04/html/2026-15833.htm | Full text via case.dev (first 5,000,000 characters, covering the MS-DRG preamble); 2026-10-30 | V44; Z59 housing codes CC to NonCC (91 FR 49648); R53.2, E40-E43, P01.7, P03.0, O63.0, O63.9 maintained (49648-49652); Tables 6G-6J (49653); MS-DRG deletions (49595, 49620, 49635); 768 MS-DRGs (49919); sepsis definitions footnote (49891) |
| FY 2027 final rule correcting document, FR Doc. 2026-19946 (Sept. 29, 2026) | https://www.federalregister.gov/documents/2026/09/29/2026-19946/medicare-program-hospital-inpatient-prospective-payment-systems-for-acute-care-hospitals-ipps-and | Full text via case.dev; 2026-10-30 | Table 5 relative weights recalculated; no severity or CC exclusion correction found |
| MLN MM14592, IPPS and LTCH PPS FY 2027 changes | https://www.cms.gov/files/document/mm14592-inpatient-long-term-care-hospital-prospective-payment-systems-fy-2027-changes.pdf | Full text via case.dev; 2026-10-30 | MCE V44 for discharges on or after Oct. 1, 2026; 18 MS-DRGs deleted, 14 created, 768 total |
| ERRATA, ICD-10 MS-DRGs Version 44 | https://www.cms.gov/files/document/2027-errata-icd-10-ms-drgs-version-44.pdf | Full text via case.dev; 2026-10-30 | V44 grouper effective for discharges on or after Oct. 1, 2026; two added non-O.R. PCS codes |
| ICD-10 MS-DRG V44 Definitions Manual (final rule version), pages P0001, P0007, P0029, P0031, P0109, P0110, P0178, P0352, P0398-P0400, P1215-P1218, P1220, P1226, P1229, P1257, P1266, P1269 | https://www.cms.gov/icd10m/FY2027-fr-v44-fullcode-cms/fullcode_cms/P0001.html (and the named pages) | Full text via case.dev; 2026-10-30 | Table of contents (asterisk marks non-O.R. procedures; Appendix F, MS-DRGs 981-989); Appendix C structure; severity and PDX collections for the codes in the rules file; collections 0072 and 0113; DRG families 870-872, 193-195, 190-192, 377-379, 189; no Z59 code on the CC list |
| ICD-10-CM Official Guidelines for Coding and Reporting FY 2027 | https://www.cms.gov/files/document/fy-2027-icd-10-cm-coding-guidelines.pdf (CDC copy at ftp.cdc.gov, same title) | Full text via case.dev; 2026-10-30 | I.A.19; I.B.14; I.C.1.d; Section II A-K; Section III A-C; IV.H; Appendix I (POA) |
| ACDIS news, FY 2027 guideline changes (Oct. 1, 2026) | https://acdis.org/articles/news-cms-releases-fy-2027-icd-10-cm-coding-guidelines | Full text via case.dev; 2026-10-30 | Summary of FY 2027 changes (sepsis title, I.C.2.e, hypertension, Chapter 17, DES Z codes); names none in Sections II or III |
| UHDDS, 1984 revision, Health Information Policy Council notice, 50 FR 31038-40 (July 31, 1985) | https://www.govinfo.gov/content/pkg/FR-1985-07-31/pdf/FR-1985-07-31.pdf | Full text via case.dev (OCR of the scanned issue); 2026-10-30 | Item 11-a principal diagnosis and 11-b other diagnoses, verbatim |
| ACDIS/AHIMA Guidelines for Achieving a Compliant Query Practice, 2026 Update (August 2026) | https://bok.ahima.org/media/zc0bqdjt/2026_acdis-ahima_compliant-query-practice.pdf | Full text via case.dev; 2026-10-30 | Supersedes 2022; Sections V-VII rules in the query file |
| AHIMA Journal, "What's New in the 2026 Update" (Sept. 22, 2026); ACDIS webinar page (Sept. 30, 2026) | https://journal.ahima.org/page/guidelines-for-achieving-a-compliant-query-practice-whats-new-in-the-2026-update | Full text via case.dev; 2026-10-30 | Technology prompts are queries; clinical validation emphasis |
| 42 C.F.R. 412.3 (Admissions), eCFR current | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-412/subpart-A/section-412.3 | Full text via case.dev; 2026-10-30 | Inpatient order; 2-midnight expectation; inpatient-only; shorter-stay exception; last amended 90 FR 54082 (Nov. 25, 2025) |
| 42 C.F.R. 422.101 | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-422/subpart-C/section-422.101 | Full text via case.dev; 2026-10-30 | MA plans follow 412.3 admission criteria |
| 42 C.F.R. 412.4 | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-412/subpart-A/section-412.4 | Full text via case.dev; 2026-10-30 | Acute and post-acute transfer definitions; graduated per diem |
| ICD-10-PCS Official Guidelines for Coding and Reporting 2027 | https://www.cms.gov/files/document/2027-official-icd-10-pcs-coding-guidelines.pdf | Full text via case.dev; 2026-10-30 | B3.1a, B3.1b, B3.5; no guidance on counting ventilation hours |
| 42 C.F.R. 412.2 | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-412/subpart-A/section-412.2 | Full text via case.dev; 2026-10-30 | 412.2(c)(5) 3-day preadmission payment window |
| Medicare Claims Processing Manual, ch. 3, 20.2.1 (MCE edits) and 40.3 | https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/clm104c03.pdf | Full text via case.dev; 2026-10-30 | MCE edit 19 for 5A1955Z (more than four consecutive days); window services' diagnoses and procedures on the inpatient claim, CPT converted to ICD procedure codes, POA at the order |
| Medicare Program Integrity Manual, ch. 6, 6.5.2-6.5.3 | https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/pim83c06.pdf | Full text via case.dev; 2026-10-30 | DRG validation scope; symptom code not principal when cause known; deemed admission date |
| CMS Hospital-Acquired Conditions page; MLN901046 HAC-POA fact sheet | https://www.cms.gov/medicare/payment/hospital-acquired-conditions-hac; https://www.cms.gov/files/document/wpoafactsheetpdf | Full text via case.dev; 2026-10-30 | 14 HAC categories; DRA section 5001(c); Y and W paid, N and U not; HAC-POA distinct from HAC Reduction Program |

## 2. Confirmed statements

| Statement | Where |
|---|---|
| V44 applies to discharges on or after Oct. 1, 2026 | MM14592; V44 errata |
| Z59.00-Z59.02, Z59.10-Z59.12, Z59.19, Z59.811, Z59.812, Z59.819 are NonCC for FY 2027 | 91 FR 49648; V44 Appendix C Part 1 page 47 (no Z59 code) |
| R65.20 is an MCC excluded when the principal diagnosis is A41.9, A41.51 or another code in collection 0072 | V44 Appendix C Part 1 page 19; collection 0072 |
| J18.9 is an MCC; collection 0113 does not contain A41.9, A41.51 or K26.4 | V44 Appendix C Part 1; collection 0113 (129 codes) |
| 870-872 split on MV more than 96 hours, then MCC only | V44 MDC 18 page |
| 193-195, 190-192 and 377-379 split MCC / CC / neither; K92.1 and K26.4 both group to 377-379 | V44 MDC 04 and MDC 06 pages |
| Code assignment rests on the provider's statement, not clinical criteria | Guidelines I.A.19 |
| SDOH may be coded from other clinicians' documentation; malnutrition is not on the exception list | Guidelines I.B.14 |
| Yes/no queries cannot introduce a new diagnosis; a dietitian's malnutrition note alone does not support a yes/no query | 2026 brief, Definitions and yes/no format |
| POA is judged at the inpatient order; ED conditions are POA | Guidelines Appendix I |

## 3. Corrections made to the earlier version of this skill

| Item | Before | After | Source |
|---|---|---|---|
| Sepsis DRG titles | 870 base "no CC", 871 "with CC", 872 "with MCC" | 870 MV more than 96 hours; 871 with MCC; 872 without MCC | V44 MDC 18 |
| Joint replacement row | 468-470 three-way split | Removed; 466-468 deleted for FY 2027 | 91 FR 49620 |
| PACT scope | "Over 280 MS-DRGs" | Count not stated; `[VERIFY]` against FY 2027 tables | 42 CFR 412.4 |
| HAC | HAC Reduction Program described as the POA payment rule | HAC-POA provision (DRA 5001(c)) distinguished from ACA 3008 program | MLN901046 |
| Query standard | "AHIMA and ACDIS practice briefs" | 2026 update named, with its format rules | 2026 brief |
| Revenue estimates | "$10,000-$30,000 per case", "15-20% undercaptured" | Removed as unsourced | none found |

## 4. `[VERIFY]` list

1. AHA Coding Clinic answers that bear on a case (paywalled; not read).
2. Severity, PDX collection or Part 3 exclusion of any code not listed in `references/drg-coding-rules.md`, Section 4 (Tables 6I, 6J, 6G and 6H were not read as files).
3. FY 2027 relative weights and GMLOS from corrected Table 5 (not read).
4. FY 2027 post-acute care transfer qualifying MS-DRG list and its count.
5. Each payer's contract: payment basis (MS-DRG, APR-DRG, per diem) and any clinical definition it applies, such as Sepsis-3.
6. NUBC patient discharge status code values (not read).
7. FY 2027 ICD-10 HAC code list (categories confirmed; code list page not read).
8. Ventilation-hour counting conventions for 5A1955Z (start and stop points; Coding Clinic, not read). The ICD-10-PCS 2027 guidelines were read and do not address them.
9. Sepsis-2 and Sepsis-3 definitions rest on the final rule footnote, not the source papers.
10. HAC payment by POA indicator (Y and W paid; N and U not) rests on the MLN901046 FY 2015 chart; confirm no later change.
