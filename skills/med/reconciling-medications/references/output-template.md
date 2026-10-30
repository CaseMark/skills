# Output Template

Produce the header and sections in this order. Every value carries a source locator (document, date and time, author role) or `[UNVERIFIED]`. Use the status, verification, type and priority labels from the reconciliation rules file verbatim. Nothing in the output is an order.

## Contents

1. Header
2. Section 1. Summary
3. Section 2. Source register
4. Section 3. BPMH worksheet
5. Section 4. Comparison worksheet
6. Section 5. Discrepancy list for the prescriber
7. Section 6. High-alert medication detail
8. Section 7. Allergy check
9. Section 8. Reconciliation table (source and document conflicts)
10. Section 9. Hand-off information check (discharge, transfer out, outpatient)
11. Section 10. Gaps and open items
12. Section 11. Hand-offs
13. Section 12. Declined part
14. Section 13. Reviewer sign-off
15. Usage notes

## Header

```
MEDICATION RECONCILIATION WORKSHEET (DRAFT)
Patient:            [de-identified ID; age; sex]
Transition:         [Admission | External transfer in | External transfer out | Discharge | Outpatient or ED encounter]
Comparison:         [BPMH vs admission orders | BPMH, sending MAR and transfer list vs receiving orders | active orders vs transfer-out list | BPMH and active orders vs discharge list | BPMH vs medications given or changed at the visit]
Identifier match:   [two identifiers checked on every source: all agree | source excluded: <source, identifier, reason>]
Date and time:      [YYYY-MM-DD HH:MM]
Sending / receiving:[facility, unit]
Accreditation cite: [NPG.14.05.01 (hospital, 2026) | NPSG.03.06.01 (program named) | not stated]
Prepared for:       [pharmacist or prescriber role]
Status:             Draft for pharmacist or prescriber review. Not an order.
```

## 1. Summary

| Count | Number |
|---|---|
| BPMH lines (Confirmed / Single source / Conflicting sources) | |
| Comparison rows (Match / Documented change / Unexplained discrepancy / Cannot determine) | |
| Discrepancy list items (Critical / High / Moderate / Low) | |
| High-alert lines with any item | |

One sentence on the most urgent item. Never a statement that the list is reconciled or final.

## 2. Source register

| Source | Type (interview, bottles, fill history, outside MAR, prior discharge list, transfer form, clinic note, PDMP, orders, inpatient MAR, discharge list, discharge summary) | Date or range | Status (Reviewed / Unreadable after attempt / Still needed) | Note |
|---|---|---|---|---|

State at the top whether the home list rests on one source type.

## 3. BPMH worksheet

| # | Generic (brand) | Strength and formulation | Dose | Route | Frequency (PRN reason) | Indication | Last dose | Sources and locators | Verification |
|---|---|---|---|---|---|---|---|---|---|
| 1 | metoprolol succinate (Toprol-XL) | 50 mg ER tab | 50 mg | PO | daily | HTN | 2026-10-29 08:00 per patient | interview; bottle label 2026-10-01 | Confirmed |

Include OTC, supplements, inhalers, patches, eye and ear drops, injectables on weekly or monthly schedules, samples and PRN products. For each "Conflicting sources" line, show each source's version on its own line.

## 4. Comparison worksheet

One row per medication across the baseline and every compared list.

| # | Medication | Baseline (BPMH or pre-transfer) | Admission or post-transfer orders | Inpatient MAR at transition | Discharge list | Discharge summary | Row status | Type | Reason and locator (if documented) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | warfarin | 5 mg PO daily | 5 mg PO daily | 7.5 mg 10-24 | 7.5 mg daily | "continue warfarin" | Documented change | Dose | INR note, hospitalist, 10-24 |
| 2 | omeprazole | 20 mg PO daily (OTC) | absent | absent | absent | not mentioned | Unexplained discrepancy | Omission | none found |

Drop columns that do not apply to the transition; never leave a supplied list out.

## 5. Discrepancy list for the prescriber

The core deliverable. Every row that is not Match or Documented change, every Conflicting sources or Single source high-alert BPMH line, every document conflict and every allergy check conflict.

| # | Priority | Medication | Type | What each source says (locators) | Why flagged | Question for the prescriber | Owner |
|---|---|---|---|---|---|---|---|
| 1 | Critical | apixaban | Held, not resumed | Note 10-22: resume 48 h after EGD; MAR: last dose 10-22 08:00; discharge list: absent | High-alert; resume condition stated; no resume or stop documented | "Apixaban was held for the 10-23 EGD with a plan to resume at 48 hours. Should it appear on the discharge list, and if not, what is the reason to document?" | Discharging prescriber |

Write each question so either answer is easy to give. Do not suggest the answer, a dose, a start or a stop.

## 6. High-alert medication detail

One block for each high-alert medication with a discrepancy list item:

```
Drug:            [generic (brand)]
ISMP class:      [anticoagulant | insulin | opioid | sulfonylurea | oral methotrexate (non-oncologic) | other]
Item number:     [#]
Baseline:        [dose / route / frequency / formulation, or NOT ON BPMH]
Each list:       [admission | post-transfer | MAR | discharge list | summary]
Discrepancy:     [one line]
Documented reason: [quote and locator, or "none found"]
Monitoring documented: [lab, level or assessment with value, time and locator, or "none found"; record only, no recommendation]
Name check:      [ISMP confused-name pair, if any]
Open question:   [the question in Section 5]
```

## 7. Allergy check

One row per documented allergy or intolerance, from every source that lists one. Record a conflict for any line on any list that names the allergen or, where the allergy record or a source states it, a related agent.

| Allergy or intolerance | Reaction | Source and locator | Conflicting line (list, drug, dose) | Question for the prescriber |
|---|---|---|---|---|
| penicillin | hives (2019) | BPMH interview; ED triage allergy list | discharge list: amoxicillin-clavulanate 875-125 mg BID | "The discharge list includes amoxicillin-clavulanate and the record lists a penicillin allergy with hives. Is this intended, and if so, what should be documented?" |
| sulfa | rash | SNF transfer form | none found | none |

Each conflict also goes on the discrepancy list as type "Allergy or contraindication conflict", priority Critical. Allergy lists that differ across sources go in the reconciliation table. Do not write "remove", "contraindicated" or any instruction.

## 8. Reconciliation table (source and document conflicts)

| # | Fact | Source A says | Source B says | Stronger evidence and why | Still needs prescriber confirmation? |
|---|---|---|---|---|---|

Typical rows: transfer form against outside MAR; fill history against interview; discharge list against discharge summary; checkbox reason against progress note.

## 9. Hand-off information check (discharge, transfer out, outpatient)

| Item (CMS A-0810 guidance; NPG.14.05.01 EP 4) | Present? | Locator | Note |
|---|---|---|---|
| Actual reconciled medication list going to the next provider (not a pointer to the EHR) | | | |
| Changes during hospitalization identified (new, changed, stopped, held) | | | |
| Prescription, OTC and herbal products included | | | |
| Allergies (drug and food) and drug interactions listed | | | |
| Written medication information for the patient or caregiver | | | |
| Discharge list, discharge summary and prescriptions agree | | | |
| Transfer out: medication list and last-dose times from the sending MAR go with the patient | | | |
| Outpatient or ED encounter: written information on new or changed medications (only the new drug if a short-term drug was the only change) | | | |

## 10. Gaps and open items

| # | Gap | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Affects item | Who can resolve | Next step |
|---|---|---|---|---|---|

Then every `[VERIFY]` relied on, with what would settle it.

## 11. Hand-offs

| To skill | Why | What is passed | What this worksheet did not do |
|---|---|---|---|
| managing-anticoagulation-therapy | Duplicate anticoagulant, switch-rule and periprocedural timing review | Anticoagulant lines, items and MAR times | Did not choose an agent or a restart time |
| managing-atrial-fibrillation | Choosing an anticoagulant for atrial fibrillation | The duplicate or interchange item | Did not select an agent |
| reconciling-inpatient-medications | In-stay order continuity (ICU to floor, service change, post-op resumption) | The BPMH and active orders | Did not reconcile unit-to-unit orders |
| coordinating-care-transitions | Post-discharge follow-up of the reconciled list | The list after prescriber decisions | Did not arrange follow-up |
| managing-renal-dose-adjustments | Dose questions tied to renal function | Drug, dose, creatinine values with dates | Did not judge renal dosing |
| assessing-drug-interactions | Interaction screen of the reviewed list | The list after prescriber decisions | Did not grade interactions |

## 12. Declined part

Use only when part of the request was declined. One row per declined request, with the label verbatim:

| Label | Request as made | Offered instead |
|---|---|---|
| Declined: order writing | | The discrepancy list for the prescriber to act on |
| Declined: drug or dose selection | | A neutral question and, where relevant, a hand-off |
| Declined: intent classification | | The item left as Unexplained discrepancy for the prescriber |
| Declined: finalizing the list | | Draft status with open items listed |
| Declined: compliance attestation | | The standard that applies and the items that bear on it, without a finding that it was met |

## 13. Reviewer sign-off

```
Prepared as a draft from the sources in Section 2. Discrepancy list items are open
until the prescriber documents a decision. This worksheet is not an order and does
not by itself show that any accreditation or CMS requirement was met.

Reviewed by (name, credentials): ____________________
Date and time:                   ____________________
Items resolved / open:           ____ / ____
```

## Usage notes

- More than 20 medications: keep the summary, the discrepancy list and the high-alert detail first; the full worksheets follow.
- Export for an EHR or a spreadsheet: pipe-delimited tables or JSON with the same column names.
- Shared drafts: de-identify; keep only the identifiers the reviewer needs.
