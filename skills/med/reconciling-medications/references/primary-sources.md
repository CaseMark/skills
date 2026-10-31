# Primary Sources and Verification Register

Checked October 30, 2026. Full texts were read through the case.dev API (`/search/v1/contents`) unless the method column says otherwise. Re-check before relying on a requirement for a survey response, a policy or a legal filing.

## Contents

1. Sources checked
2. Confirmed statements
3. Corrections to the earlier version of this skill
4. Disposition of the deleted RECONCILIATION-TEMPLATE.md
5. `[VERIFY]` list

## 1. Sources checked

| Source | URL read | Method; date | Supports |
|---|---|---|---|
| Joint Commission, National Performance Goals effective January 2026, Hospital Program | https://digitalassets.jointcommission.org/api/public/content/9ca80055182b4274842a5780a94f2c82 | Full text via case.dev; 2026-10-30 | NPG.14.05.01 EPs 1-5 and notes; NPG.14.04.01 (anticoagulants); NPG.06.01.01 EP 6 (PDMP access) |
| Joint Commission, National Patient Safety Goals page | https://www.jointcommission.org/en-us/standards/national-patient-safety-goals | Full text via case.dev; 2026-10-30 | NPGs effective January 1, 2026 replace NPSGs for the Hospital and Critical Access Hospital programs; other programs keep 2026 NPSG chapters |
| Joint Commission, NPG #14 Effectively Managing Medications page | https://www.jointcommission.org/en-us/standards/national-performance-goals/effectively-managing-medications | Full text via case.dev; 2026-10-30 | Goal 14 scope; "maintains and communicates accurate patient medication information"; 6.5 medication errors per 100 admissions |
| Joint Commission, 2026 Critical Access Hospital NPGs (goal list) | https://digitalassets.jointcommission.org/api/public/content/0f9c90310d214329829754d996216b9a | Full text via case.dev; 2026-10-30 | CAH Goal 14, medication management; EPs not in this document |
| Joint Commission, NPSGs effective January 2026, Nursing Care Center Program | https://digitalassets.jointcommission.org/api/public/content/94389f1cc45940fd90d7954147cac4c4?v= | Full text via case.dev; 2026-10-30 | NPSG.03.06.01 rationale and EPs for that program |
| Joint Commission, NPSGs effective January 2026, Home Care Program | https://digitalassets.jointcommission.org/api/public/content/844857809e384b85b6275c4dcc75900b?v=030315f0 | Full text via case.dev; 2026-10-30 | NPSG.03.06.01 present in the 2026 home care chapter |
| Joint Commission FAQ 000001214, non-24-hour settings (Feb. 17, 2026) | https://www.jointcommission.org/en-us/knowledge-library/support-center/standards-interpretation/standards-faqs/000001214 | Full text via case.dev; 2026-10-30 | Applicability where medication is given or the regimen changes; short-term additions; no list expected when nothing changed |
| Joint Commission FAQ 000001207, limited scope of service (Oct. 2, 2025) | https://www.jointcommission.org/en-us/knowledge-library/support-center/standards-interpretation/standards-faqs/000001207 | Full text via case.dev; 2026-10-30 | Limited-scope home care must still reconcile; elements for drugs the organization supplies |
| Joint Commission Glossary, "Medication" | https://www.jointcommission.org/en-us/knowledge-library/support-center/general/glossary | Full text via case.dev; 2026-10-30 | Definition of medication, inclusions and exclusions |
| WHO High 5s SOP, Assuring Medication Accuracy at Transitions in Care: Medication Reconciliation, Version 3, September 2014 | https://cdn.who.int/media/docs/default-source/patient-safety/high5s/h5s-sop.pdf; WHO listing page https://www.who.int/publications/m/item/high5s-standard-operating-protocol-medication-reconciliation (dated February 23, 2021) | Full text via case.dev; 2026-10-30 | BPMH content and sources; proactive and retroactive models; 24-hour goal; undocumented intentional and unintentional; BPMDP; transfer and discharge not evaluated; Phase 1 population |
| AHRQ MATCH Toolkit for Medication Reconciliation, Pub. No. 11(12)-0059, revised August 2012 | https://www.ahrq.gov/sites/default/files/publications/files/match.pdf; index page https://www.ahrq.gov/patient-safety/settings/hospital/match/index.html (content last reviewed April 2023) | Full text via case.dev; 2026-10-30 | Figure 9 interview prompts; sources list and label caution; Table 3 categories; unintended discrepancy types; external transfer three-source rule |
| 42 C.F.R. 482.43 (hospital discharge planning) | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-482/subpart-C/section-482.43 | Full text via case.dev (eCFR); 2026-10-30 | Paragraph (b) transmission of necessary medical information at discharge |
| CMS State Operations Manual, Appendix A (Rev. 248, issued September 18, 2026), tag A-0810 (Rev. 238, issued March 20, 2026) | https://www.cms.gov/Regulations-and-guidance/Guidance/Manuals/downloads/som107ap_a_hospitals.pdf | Full text via case.dev; 2026-10-30 | Interpretive guidance for 482.43(b): reconciled medication list including OTC and herbal; actual list, not an EHR pointer; allergies and interactions; transfer content |
| 42 C.F.R. 482.23(c)(6) (nursing services; self-administration), with SOM Appendix A tags A-0412 and A-0413 | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-482/subpart-C/section-482.23; SOM PDF above | Full text via case.dev (eCFR and SOM); 2026-10-30 | (c)(6)(ii): self-administration of the patient's own medications only under a practitioner's order and hospital policy, with identification, integrity check, security and documentation of reported doses |
| 42 C.F.R. 485.642 (CAH discharge planning) | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-485/subpart-F/section-485.642 | Full text via case.dev (eCFR); 2026-10-30 | Paragraph (b), same transmission duty for CAHs |
| 42 C.F.R. 483.21 (long-term care comprehensive care plans and discharge) | https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-483/subpart-B/section-483.21 | Full text via case.dev (eCFR); 2026-10-30 | (c)(2)(iii) reconciliation of pre-discharge and post-discharge medications, prescribed and OTC |
| ISMP List of High-Alert Medications in Acute Care Settings (2024) | https://online.ecri.org/hubfs/ISMP/Resources/ISMP_HighAlert_AcuteCare_List.pdf (ECRI-hosted copy of the ISMP list) | Full text via case.dev; 2026-10-30 | Classes and specific drugs in the rules file |
| ISMP List of Confused Drug Names (2024) | https://online.ecri.org/hubfs/ISMP/Resources/ISMP_ConfusedDrugNames.pdf (ECRI-hosted copy) | Full text via case.dev; 2026-10-30 | Pairs named in the rules file and evals |
| FDA Pregnancy and Lactation Labeling (Drugs) Final Rule page | https://www.fda.gov/drugs/labeling-information-drug-products/pregnancy-and-lactation-labeling-drugs-final-rule | Full text via case.dev; 2026-10-30 | Letter categories removed; effective June 30, 2015, phased conversion |

## 2. Confirmed statements

| Statement | Where |
|---|---|
| Hospital and CAH programs moved from NPSGs to NPGs on January 1, 2026 | NPSG page |
| Hospital medication information requirement is NPG.14.05.01 with EPs 1-5 as summarized in the transition file | Hospital NPG document |
| Discrepancies include omissions, duplications, contraindications, unclear information and changes; a qualified individual identified by the hospital compares | NPG.14.05.01 EP 3 |
| Good-faith effort from the patient and/or other sources meets EP 1 intent; documentation required | NPG.14.05.01 EP 1, Note 2 |
| Non-hospital programs keep NPSG.03.06.01 in 2026 (nursing care center, home care read) | 2026 program NPSG documents |
| BPMH verified with more than one source; other sources never substitute for an interview where possible | WHO SOP Step 1-2; MATCH Chapter 5 |
| BPMH reflects actual use, which may differ from what was prescribed | WHO SOP Step 2 |
| Reconciliation goal within 24 hours of admission | WHO SOP Step 3 |
| Formulary substitution and procedure holds are intended-discrepancy examples; undocumented differences need physician follow-up | MATCH Table 3 |
| Discharge information may include a reconciled list with OTC and herbal products; an actual list is required, not an EHR pointer | SOM Appendix A, A-0810 |
| Opioids (all routes), insulin, anticoagulants and oral sulfonylureas are ISMP high-alert classes | ISMP 2024 list |

## 3. Corrections to the earlier version of this skill

| Item | Before | After |
|---|---|---|
| Accreditation citation | NPSG.03.06.01 for all settings | NPG.14.05.01 for hospitals from January 1, 2026; NPSG.03.06.01 for programs that still have NPSGs |
| Pregnancy flag | "Category X drug" | Letter categories removed under the PLLR; describe the labeling concern |
| Burden statistics | 1.3 million injuries, 7,000 deaths, 30-70 percent discrepancy rate (unsourced) | Removed; replaced with figures from documents read |
| Allergy and renal tables | "Remove immediately", "consider dose decrease", recommended renal doses | Removed as orders; questions routed to the prescriber or a hand-off skill |
| Attestation | Claimed compliance with NPSG.03.06.01 | Reviewer sign-off with no compliance claim |
| Allergy check | Old section 5a dropped in the first rewrite | Restored as an allergy check table with a neutral question column and the "Allergy or contraindication conflict" type; no instruction wording |
| Transitions covered | Admission, internal transfer, external transfer in, discharge | Admission, external transfer in and out, discharge, outpatient or ED encounter (NPG.14.05.01 EPs 1, 2, 4, 5); in-stay transfers routed to reconciling-inpatient-medications |
| Anticoagulant hand-off | "Anticoagulant choice" to managing-anticoagulation-therapy | Duplicate, switch-rule and periprocedural timing review there; agent choice for atrial fibrillation to managing-atrial-fibrillation, whose description claims anticoagulation selection |
| Concentrated electrolytes | "KCl over 40 mEq", "NaCl 23.4 percent" | ISMP wording: potassium chloride for injection concentrate; sodium chloride for injection over 0.9 percent |

## 4. Disposition of the deleted RECONCILIATION-TEMPLATE.md

The earlier reference file was merged into the output template on October 30, 2026.

| Old section | Disposition | Where now or why |
|---|---|---|
| 1. Report header | Moved | Output template, Header, with the identifier-match and standard fields added |
| 2. Summary dashboard | Moved | Output template, Section 1, using the new status and priority vocabulary |
| 3. Reconciliation matrix | Moved | Output template, Sections 3 and 4 (BPMH and comparison worksheets) |
| 4. High-alert medication detail | Kept | Output template, Section 6; "Monitoring" kept as "Monitoring documented" with locator; "Action Needed" replaced by the open question |
| 5a. Allergy cross-check | Kept | Output template, Section 7; the "remove immediately" and "contraindicated" actions dropped as orders |
| 5b. Drug-drug interactions, "Action" column | Dropped as order | Interaction grading handed to assessing-drug-interactions; "monitor INR, consider dose decrease" was an order |
| 6. Renal and hepatic dose flags, "Recommended Adj." column | Dropped as order | Renal dose changes are traced as discrepancies (rules file, Section 11); dosing judgment handed to managing-renal-dose-adjustments |
| 7. Unresolved items | Moved | Output template, Section 10, with gap classes |
| 8. Pharmacist attestation | Dropped | It asserted compliance with NPSG.03.06.01; replaced by the reviewer sign-off in Section 13 with no compliance claim |
| Usage notes | Kept | Output template, Usage notes |

## 5. `[VERIFY]` list

1. CAH NPG standard and EP numbering for medication information (only the CAH goal list was read).
2. No Joint Commission crosswalk from NPSG.03.06.01 to NPG.14.05.01 was read; the correspondence rests on comparing the texts.
3. 2026 NPSG.03.06.01 text for ambulatory, behavioral health, office-based surgery, telehealth, rural health clinic and other programs not read.
4. State PDMP query mandates and interstate data sharing (state-variable).
5. Who may collect a BPMH (pharmacy technicians, nurses) under state practice rules and facility policy.
6. Later editions of the ISMP high-alert and confused-name lists, and the ISMP community and ambulatory high-alert list (not read).
7. Whether legacy discharge tags still printed in the SOM Appendix A PDF (for example A-0837, Rev. 87) carry any force beside A-0810.
