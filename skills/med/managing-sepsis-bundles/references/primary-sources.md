# Primary Sources and Verification Register

Checked October 30, 2026, in two passes the same day. The first pass used web-search extracts because direct retrieval of qualitynet.cms.gov, cms.gov, sccm.org and pmc.ncbi.nlm.nih.gov was blocked. The second pass read full texts through the case.dev API (`/search/v1/contents`). The v5.18a manual itself sits on qualitynet.cms.gov, which serves pages through JavaScript and could not be read; its Alphabetical Data Dictionary was read in full from a mirror posted by KHA Quality (Kentucky Hospital Association), whose header reads "Hospital IQR Manual Version 5.18a" and whose footer reads "Specifications Manual for National Hospital Inpatient Quality Measures Discharges 01-01-26 (1Q26) through 12-31-26 (4Q26)". The v5.18a measure information form, algorithm, Appendix C and release notes were not found in readable form. Each row gives the URL read, the method ("full text via case.dev" or "search excerpt") and the date. Re-check before relying on a rule for a submitted abstraction.

## Contents

1. Sources checked
2. Confirmed statements
3. Corrections made on full-text review
4. `[VERIFY]` list

## 1. Sources checked

| Source | URL read | Method; date | Supports |
|---|---|---|---|
| CMS Specifications Manual v5.18a, Alphabetical Data Dictionary (mirror) | https://www.khaquality.com/wp-content/uploads/2026/03/1b-AlphaDD.pdf (KHA Quality mirror of the CMS manual) | Full text via case.dev; 2026-10-30 | Every "DD, <element>" rule in the SEP-1 rules file: severe sepsis criteria, pregnancy criteria, presentation times, septic shock, lactate, cultures, antibiotic, crystalloid, hypotension, vasopressor, reassessment, exclusion elements |
| CMS Specifications Manual v5.18a, measure information form, algorithm, Appendix C, release notes | https://qualitynet.cms.gov/inpatient/specifications-manuals (JavaScript; not readable) | Not read | Length-of-stay and discharge-within-6-hours exclusions, antibiotic tables, algorithm outcomes: see the `[VERIFY]` list |
| v5.18 posting notice, listserve 2025-66-IP (June 24, 2025) | https://www.qualityreportingcenter.com/globalassets/listserves/2025/iqr/2025-66-ip%5Flistserve%5Fiqr%5Fv5.18-specs-manual-posting%5Fvdraft-508.pdf | Full text via case.dev; 2026-10-30 | v5.18 for 01/01/2026-12/31/2026 discharges; SEP-1 updates; COVID-19 exclusion removed from the Initial Patient Population |
| v5.18a addendum notice, listserve 2025-96-IP (Sept. 19, 2025) | https://www.qualityreportingcenter.com/globalassets/listserves/2025/iqr/2025-96-ip%5Flistserve%5Fiqr%5Fv5.18a-specs-manual-posting%5Fvfinal-508.pdf | Full text via case.dev; 2026-10-30 | Addendum for 2026 discharges; Appendix A.1 Table 4.01 (SEP) updated for FY 2026 codes |
| v5.18a webinar notice, listserve 2026-41-IP (May 15, 2026) | https://www.qualityreportingcenter.com/globalassets/listserves/2026/iqr/2026-41-ip%5Fsep-1-2026-webinar-listserv%5Ffinal%5F508.pdf | Full text via case.dev; 2026-10-30 | CMS SEP-1 v5.18a review webinar, May 19, 2026; slides on QualityNet (not readable) |
| v5.19 posting notice, listserve 2026-57-IP (July 1, 2026); eCQI Resource Center notice | https://www.qualityreportingcenter.com/globalassets/listserves/2026/iqr/2026-57-ip_listserve_iqr_v5.19-specs-manual-posting_508.pdf; https://ecqi.healthit.gov/national-hospital-inpatient-quality-measures-updated-specifications-manual | Full text via case.dev; 2026-10-30 | v5.19 for 01/01/2027-12/31/2027 discharges, with updated SEP-1 abstraction guidance |
| SEP-1 composite measure training, April 2025 (v5.17a) | https://www.qualityreportingcenter.com/globalassets/iqr2025-events/iqr040125/april-2025_sep1_npc_vfinal_508.pdf | Full text via case.dev; 2026-10-30 | v5.17a governs 2025 discharges |
| SEP-1 Q&A transcripts and training, 2016-2024 | QualityReportingCenter archived IQR events (August 2024 v5.16 training, 2019 v5.7 Q&A, 2022 algorithm overview, 2016-2017 webinars) | Search excerpt; 2026-10-30 | Version history only (v5.3a initial-hypotension gap; earlier antibiotic tables); superseded where the v5.18a data dictionary speaks |
| KHA Quality SEP-1 abstraction tool template, April 2026 | https://www.khaquality.com/wp-content/uploads/2026/05/Sepsis-Abstraction-Tool-Template-April-2026.pdf | Full text via case.dev; 2026-10-30 | Secondary cross-check of the data dictionary (reassessment window from crystalloid administration time; three reassessment routes) |
| FY 2024 IPPS/LTCH PPS final rule | Federal Register, Aug. 28, 2023 | Search excerpt (secondary reports); 2026-10-30 | SEP-1 in Hospital VBP Safety domain from FY 2026 |
| FY 2027 IPPS/LTCH PPS final rule | Federal Register, Aug. 4, 2026 (2026-15833) | Search excerpt (summaries); 2026-10-30 | No SEP-1 change found; sepsis readmission measure finalized for HRRP |
| Sepsis-3 | Singer M, et al. JAMA 2016;315(8):801-810 | Search excerpt; 2026-10-30 | Sepsis and septic shock definitions; SOFA 2 or more; qSOFA |
| SOFA table | Sepsis-3 Table 1 as reproduced in peer-reviewed tables and the MSD Manual | Search excerpt; 2026-10-30 | Organ thresholds in the clinical criteria file |
| SOFA-2 | JAMA 2025;334(23):2090-2103, doi 10.1001/jama.2025.20516 | Search excerpt; 2026-10-30 | Revised score; six systems; correction Jan. 29, 2026 |
| SSC Bundle 2018 update | Levy MM, Evans LE, Rhodes A. Crit Care Med 2018;46(6):997-1000 | Search excerpt (secondary tables); 2026-10-30 | Hour-1 bundle elements; time zero at triage or earliest chart annotation |
| SSC adult guidelines 2026 | https://link.springer.com/article/10.1007/s00134-026-08361-1 (Intensive Care Med 2026;52:863-936, published Mar. 23, 2026; Crit Care Med companion doi 10.1097/CCM.0000000000007075) | Full text via case.dev; 2026-10-30 | Statements 4, 10, 13, 14, 16-18, 43, 44, 51, 52, 54-56, 79; 129 statements; no SOFA-2 |
| CDC sepsis burden | CDC, Sepsis Data and Burden page | Search excerpt; 2026-10-30 | About 1.7 million adults with sepsis yearly; at least 350,000 die in hospital or are discharged to hospice |
| ICD-10-CM Official Guidelines I.C.1.d | CDC/CMS ICD-10-CM guidelines | Search excerpt (secondary); 2026-10-30 | R65.20, R65.21; underlying systemic infection coded first |

## 2. Confirmed statements

| Statement | Where (full text unless noted) |
|---|---|
| v5.18a governs 01/01/2026-12/31/2026 inpatient discharges; v5.19 governs 2027 | Notices 2025-66-IP, 2025-96-IP, 2026-57-IP; data dictionary footer |
| SEP-1 ICD-10-CM codes are in Appendix A, Table 4.01, updated in v5.18a | Notice 2025-96-IP |
| COVID-19 exclusion removed from the Initial Patient Population in v5.18; no COVID-19 instruction in the v5.18a data dictionary | Notice 2025-66-IP; data dictionary searched in full |
| Severe sepsis: all three criteria within six hours; SIRS and organ dysfunction inequalities as listed in the rules file; pregnancy thresholds when the pregnancy element is Yes | DD, Severe Sepsis Present; Pregnant 20 Weeks Through Day 3 Post-delivery |
| Values attributed by a provider, before or within 24 hours after presentation and in the same documentation, to a chronic condition, medication, normal-for-patient state or non-infectious acute cause are not used | DD, Severe Sepsis Present |
| Provider documentation terms, qualifiers ("rule out" is positive), six-hour negation, bacteremia and septicemia excluded | DD, Severe Sepsis Present; Septic Shock Present |
| Presentation time: earliest of last criterion and provider documentation; lab result time for lab criteria; arrival-time rules; no triage rule | DD, Severe Sepsis Presentation Time; Severe Sepsis Present |
| Septic shock: persistent hypotension, initial lactate 4 or more, or provider documentation; not present if more than six hours after severe sepsis; lactate route timed by lab result | DD, Septic Shock Present; Septic Shock Presentation Time |
| Windows for initial lactate, blood cultures, antibiotic, repeat lactate, crystalloid, vasopressor, reassessment | DD element for each, as cited in the rules file |
| Crystalloid: 10 percent rule applies to the ordered volume and the target must be completely infused; lesser-volume criteria; IBW rule; order content; fluids that count; 125 mL/hour rule | DD, Crystalloid Fluid Administration |
| Initial hypotension: two readings within three hours, 6 hours before to 6 hours after presentation, before the target volume is complete; time of the second reading | DD, Initial Hypotension; Initial Hypotension Time |
| Persistent hypotension: last two consecutive readings in the hour after the target volume; vasopressor rules for a single or normal-then-low reading | DD, Persistent Hypotension |
| Exclusion elements: comfort care (DNR is not comfort care), transfer, clinical trial, administrative contraindication | DD elements named in the rules file |
| Vasopressors from Appendix C Table 5.2; anticoagulants in Table 5.3 | DD, Vasopressor Administration; Severe Sepsis Present |
| Reassessment: three routes; window from crystalloid start to 6 hours after septic shock | DD, Repeat Volume Status and Tissue Perfusion Assessment Performed (updated v5.18) |
| Sepsis-3 definitions, SOFA 2 or more, qSOFA thresholds, septic shock criteria | Singer 2016 (search excerpt) |
| Hour-1 bundle elements and time zero | Levy 2018 (search excerpt) |
| SSC 2026 statements and strengths in the clinical criteria file, including MAP 60-65 for 65 or older (14) and IV corticosteroids without a specified regimen (79); no SOFA-2 | SSC 2026, Intensive Care Med full text |

## 3. Corrections made on full-text review

| Item | Before | After | Source |
|---|---|---|---|
| Reassessment window | After crystalloid completion; a note before completion does not count | From the crystalloid infusion start (Crystalloid Fluid Administration Time) to 6 hours after septic shock presentation | DD, Repeat Volume Status and Tissue Perfusion Assessment Performed |
| Reassessment routes | Attestation, focused exam, or CVP, ScvO2, ultrasound, passive leg raise, fluid challenge | Attestation of exam or systems review; review of five of eight listed parameters; or CVP/RAP, ScvO2, echocardiogram, fluid challenge or passive leg raise, or carotid flow time | Same element |
| ED triage-time rule | Triage time when all criteria met at triage `[VERIFY]` | No triage rule; earliest ED arrival time for pre-hospital or present-on-arrival documentation; floor arrival for direct admits | DD, Severe Sepsis Presentation Time |
| Blood culture look-back | 48 hours | 24 hours before presentation, or 24 hours before an antibiotic started in the 24 hours before presentation; acceptable-delay exceptions | DD, Blood Culture Collection; Acceptable Delay |
| Lab timestamps | Collection time, result time "where the manual says so" | Result time for criteria (including the septic shock lactate); draw time for the lactate elements, with supporting times if no draw time | DD, Severe Sepsis Present; Septic Shock Presentation Time; Initial Lactate Level Collection |
| Fluids that count | Crystalloids only; albumin excluded | Crystalloids or balanced crystalloids at more than 125 mL/hour; colloids only through a documented lesser-volume reason; order must state type, volume and rate or duration | DD, Crystalloid Fluid Administration |
| Antibiotic tables | Monotherapy and combination tables required | v5.18a antibiotic element names no table; table use for 2026 is `[VERIFY]` | DD, Broad Spectrum or Other Antibiotic Administration |
| Pregnancy | Not covered | Separate SIRS, hypotension and creatinine thresholds from v5.18 | DD, Pregnant 20 Weeks Through Day 3 Post-delivery |
| Septic shock timing | Not stated | Septic shock more than six hours after severe sepsis presentation is not present | DD, Septic Shock Present |
| Evals 1, 4, 5 | Table membership Must; fluid order without a rate; reassessment "after 23:10" | Table question stated as `[VERIFY]` dependency; order given a 90-minute duration; reassessment window from crystalloid start | evals/evals.json |

## 4. `[VERIFY]` list

1. The exact wording of the v5.18 release notes on the COVID-19 change (release notes are on QualityNet and were not readable; the v5.18a data dictionary has no COVID-19 instruction).
2. Exclusions defined outside the data dictionary: length of stay over 120 days and discharge within 6 hours of presentation (measure information form and algorithm not read).
3. How the algorithm scores an antibiotic first started more than 24 hours before presentation (the data dictionary sets only the 72-hour look-back for abstracting the dose).
4. Whether v5.18a applies Appendix C antibiotic tables to the antibiotic element, and their numbers and contents (the v5.18a data dictionary element names no table and has no selection element; Appendix C and the algorithm were not read).
5. How the algorithm scores Crystalloid Fluid Administration value 4 (VAD, refusal, documented lack of fluid responsiveness).
6. Hospital VBP weighting, baseline and any change after FY 2027 (program rules not read in full).
7. Whether any revised consensus definition of sepsis adopts SOFA-2 (SSC 2026 does not).
8. Sepsis-3, SOFA and Levy 2018 rows rest on search excerpts; read the papers before quoting them.
