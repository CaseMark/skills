# Chronological Case Abstract -- Table Template

Use this template for the chronological case abstract (Step 2 of the
abstraction workflow). One row per encounter or discrete clinical event.
Maintain strict date order.

---

## Abstract Header

| Field | Value |
|---|---|
| **Patient** | [Name or De-identified ID] |
| **DOB / Age** | [DOB or age at time of abstraction] |
| **Sex** | [M / F / Other] |
| **Record Date Range** | [Start date] -- [End date] |
| **Purpose** | [Litigation / Audit / Quality / Coding Review / Research / Peer Review] |
| **Abstractor** | [Name or agent identifier] |
| **Date of Abstraction** | [Date] |
| **PHI Status** | [Full PHI / Limited Data Set / Safe Harbor De-identified] |

---

## Source Document Manifest

Complete this before beginning the chronological abstract.

| # | Document Type | Date | Author / Provider | Credentials | Page / File Ref | Status |
|---|---|---|---|---|---|---|
| 1 | H&P | YYYY-MM-DD | [Provider name] | [MD/DO/NP/PA] | pp. X--Y | Complete |
| 2 | Progress Note | YYYY-MM-DD | [Provider name] | [Credentials] | pp. X--Y | Complete |
| 3 | Operative Report | YYYY-MM-DD | [Provider name] | [Credentials] | pp. X--Y | Complete |
| 4 | Discharge Summary | YYYY-MM-DD | [Provider name] | [Credentials] | pp. X--Y | Partial -- missing page 2 |
| 5 | Lab Report | YYYY-MM-DD | [Lab / ordering provider] | -- | pp. X--Y | Complete |
| 6 | Imaging Report | YYYY-MM-DD | [Radiologist] | [Credentials] | pp. X--Y | Complete |
| ... | ... | ... | ... | ... | ... | ... |

**Status values:** Complete | Partial -- [reason] | Missing -- [reason] | Unsigned | Addended [date]

---

## Chronological Case Abstract

| # | Date | Setting | Provider (Credentials) | Document Type | Chief Complaint / Reason | Diagnoses | Procedures | Medications (Changes) | Key Findings (Lab / Imaging / Exam) | Referrals / Orders | Source Ref | Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | YYYY-MM-DD | Outpatient | Dr. A. Smith (MD, Cardiology) | Progress Note | Follow-up HTN | Essential hypertension (I10); Type 2 DM, uncontrolled (E11.65) | -- | Lisinopril 20mg daily (increased from 10mg) | BP 158/94; HbA1c 8.7% (H) | Referral to endocrinology | Manifest #2, p. 4 | -- |
| 2 | YYYY-MM-DD | ED | Dr. B. Jones (DO, Emergency Medicine) | H&P | Chest pain, acute onset | Acute STEMI, LAD (I21.01); Hyperlipidemia (E78.5) | EKG, troponin x3, CXR | Aspirin 325mg, Heparin drip, Atorvastatin 80mg | Troponin I 4.2 ng/mL (H); EKG: ST elevation V1-V4; CXR: clear | Emergent cardiology consult | Manifest #7, pp. 12--15 | -- |
| 3 | YYYY-MM-DD | Inpatient (OR) | Dr. C. Lee (MD, Interventional Cardiology) | Operative Report | STEMI intervention | Acute STEMI, LAD (I21.01); Single-vessel CAD | PCI with DES to LAD (92928) | Clopidogrel 600mg loading dose | 95% proximal LAD lesion; post-PCI TIMI 3 flow | Cardiac rehab referral | Manifest #8, pp. 16--19 | -- |
| 4 | YYYY-MM-DD | Inpatient | Dr. A. Smith (MD, Cardiology) | Discharge Summary | Post-STEMI discharge | Acute STEMI, LAD (I21.01); CAD, single vessel; Essential HTN (I10); Type 2 DM (E11.65); HLD (E78.5) | PCI with DES to LAD (92928) | Discharge meds: ASA 81mg, Clopidogrel 75mg, Atorvastatin 80mg, Lisinopril 20mg, Metformin 1000mg BID | EF 45% (mod reduced); no complications | Cardiology f/u 1 week; Endocrinology f/u 2 weeks | Manifest #10, pp. 22--25 | EF not documented in prior notes [INFERRED: new finding post-MI] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Column Guidance

- **Date:** Use YYYY-MM-DD. If only month/year is known, use YYYY-MM-00 and flag.
- **Setting:** Inpatient, Outpatient, ED, ASC, Telehealth, SNF, Home Health, Rehab.
- **Diagnoses:** Use ICD-10-CM-level natural language. Include laterality, acuity, specificity. Separate multiple diagnoses with semicolons.
- **Procedures:** Use CPT/HCPCS-level natural language with code in parentheses where identifiable.
- **Medications (Changes):** Only document changes (new, discontinued, dose adjusted) at each encounter. Note indication if documented.
- **Key Findings:** Clinically significant lab values (with H/L/abnormal flag), imaging impressions, and physical exam findings.
- **Source Ref:** Tie back to the Source Document Manifest entry number and page range.
- **Flags:** Use for: `[INFERRED]`, `[PER: provider]`, `[VERIFY]`, `[UNSIGNED]`, `[ADDENDED: date]`, `[ILLEGIBLE]`, `[GAP: description]`.

---

## Problem List Summary

Consolidate all diagnoses from the chronological abstract into a single list.

| # | Diagnosis (ICD-10-CM Language) | Onset Date | Status | Resolved Date | Notes |
|---|---|---|---|---|---|
| 1 | Essential hypertension | YYYY-MM-DD | Active | -- | Uncontrolled per last encounter |
| 2 | Type 2 diabetes mellitus, uncontrolled | YYYY-MM-DD | Active | -- | HbA1c 8.7%; endocrinology referral pending |
| 3 | Acute STEMI, LAD | YYYY-MM-DD | Resolved | YYYY-MM-DD | PCI with DES; EF 45% post |
| 4 | Coronary artery disease, single vessel | YYYY-MM-DD | Active | -- | On DAPT |
| 5 | Hyperlipidemia | YYYY-MM-DD | Active | -- | Atorvastatin 80mg |
| ... | ... | ... | ... | ... | ... |

**Status values:** Active | Chronic-stable | Resolved | Rule-out | Historical

---

## Medication Summary

Current medications as of the most recent encounter in the abstract.

| # | Medication (Generic) | Brand | Dose | Route | Frequency | Start Date | Indication (if documented) | Source Ref |
|---|---|---|---|---|---|---|---|---|
| 1 | Aspirin | -- | 81 mg | PO | Daily | YYYY-MM-DD | STEMI / CAD | Manifest #10 |
| 2 | Clopidogrel | Plavix | 75 mg | PO | Daily | YYYY-MM-DD | Post-PCI DAPT | Manifest #10 |
| 3 | Atorvastatin | Lipitor | 80 mg | PO | Daily | YYYY-MM-DD | Hyperlipidemia / ACS | Manifest #10 |
| 4 | Lisinopril | Zestril | 20 mg | PO | Daily | YYYY-MM-DD | Hypertension / post-MI | Manifest #10 |
| 5 | Metformin | Glucophage | 1000 mg | PO | BID | YYYY-MM-DD | Type 2 DM | Manifest #10 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## CDI Queries

List any CDI queries generated during abstraction. If none, state "No CDI
queries identified."

```
CDI QUERY #1
Record:    [Document type, date, provider]
Issue:     [What is ambiguous or missing]
Clinical Indicators: [Supporting lab/imaging/exam data]
Suggested Clarification: [Specific question for the provider]
Impact:    [Coding / quality measure / legal relevance affected]
```

---

## Abstraction Notes

Document all gaps, limitations, assumptions, and flags here.

- **Missing records:** [List any records referenced but not available]
- **Illegible sections:** [List any sections that could not be abstracted]
- **Unsigned notes:** [List any unsigned documents and their status]
- **Scope limitations:** [Any records excluded and why]
- **Assumptions:** [Any assumptions made, with rationale]

---

## Attestation

> This clinical abstract reflects only facts documented in the source medical
> records identified in the Source Document Manifest. All inferred data elements
> are marked with `[INFERRED]`. All secondary references are marked with
> `[PER: source]`. Gaps in documentation are explicitly identified. This
> abstract is a summary tool and does not constitute a substitute for review of
> the complete medical record.
>
> Abstractor: _______________  Date: _______________
