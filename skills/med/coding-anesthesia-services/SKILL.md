---
name: coding-anesthesia-services
language: en
description: Assigns anesthesia codes with time documentation, base/time unit calculation, and physical status modifiers. Use when coding anesthesia, calculating anesthesia units, or applying physical status modifiers.
tags:
  - coding
  - medical-coding-and-billing
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Coded Record
  skill_modes:
    - Coding
    - Classification
---

# Coding Anesthesia Services

Assigns anesthesia CPT codes (00100–01999) with time documentation, base unit plus time unit calculation, ASA physical status modifiers, qualifying circumstance add-on codes, and provider-specific billing (anesthesiologist vs. CRNA vs. medical direction). Covers general anesthesia, regional anesthesia, monitored anesthesia care (MAC), and post-operative pain management.

## Why This Skill Exists

Anesthesia coding uses a unique reimbursement formula unlike any other medical specialty: payment = (base units + time units + modifying units) × conversion factor. This formula requires accurate time documentation, correct base unit assignment from the ASA Relative Value Guide, appropriate physical status modifier selection, and proper reporting of the anesthesia provider model (personally performed, medically directed, medically supervised). Errors in any component directly affect reimbursement. The medical direction rules alone (QK, QX, QY, QZ, AA modifiers) are among the most complex in all of medical coding.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What surgical procedure was performed under anesthesia?
2. What type of anesthesia was administered? (general, regional, MAC, combined)
3. Who provided the anesthesia? (anesthesiologist alone, CRNA alone, anesthesiologist directing CRNAs, CRNA supervised)
4. What is the documented anesthesia start time, end time, and total time?
5. What is the patient's ASA physical status classification?
6. Were there qualifying circumstances? (extreme age, emergency, hypothermia, controlled hypotension)
7. What is the payer? (Medicare anesthesia rules differ from commercial payers)

### Documents Required

- Anesthesia record (pre-operative evaluation, intraoperative record, post-operative note)
- Time documentation (anesthesia start time, end time, continuous time log)
- ASA physical status assessment
- Operative report (to match anesthesia code to the surgical procedure)
- Provider assignment documentation (who directed, who administered)
- Pre-anesthesia evaluation note
- Post-anesthesia recovery note (PACU)

---

## Step 1 — Select the Anesthesia CPT Code

Match the anesthesia code to the surgical procedure, not the anesthesia technique.

- Anesthesia codes (00100–01999) are organized by anatomic region and surgical procedure type, not by anesthesia technique.
- **Selection rule**: Choose the anesthesia code that most specifically describes the surgical procedure performed. If multiple procedures are performed during a single anesthetic, report only the code with the highest base unit value.
- **Code structure examples**:
  - 00100: Anesthesia for procedures on salivary glands
  - 00400: Anesthesia for procedures on integumentary system of head, neck, and posterior trunk
  - 00740: Anesthesia for upper GI procedures
  - 01210: Anesthesia for open hip procedures
  - 01996: Daily hospital management of epidural/subarachnoid continuous drug administration (pain management — not linked to a surgical procedure)
- If no specific anesthesia code exists for the surgical procedure, use the code for the anatomic region.
- Some procedures have distinct anesthesia codes for open vs. endoscopic approaches (e.g., 00790 vs. 00797 for intra-abdominal procedures).
- **Do NOT use surgical CPT codes** for anesthesia billing — always use the 00100–01999 range.

## Step 2 — Calculate Base Units

Look up the base unit value from the ASA Relative Value Guide.

- Each anesthesia CPT code has an assigned base unit value reflecting the complexity and risk of providing anesthesia for that procedure.
- Base units range from 3 (low complexity, e.g., 00400 for integumentary procedures) to 30+ (high complexity, e.g., 00562 for procedures on the heart with cardiopulmonary bypass).
- **Medicare base units**: CMS publishes its own base unit values that may differ from ASA values. Always use CMS base units for Medicare claims and ASA base units for commercial claims (unless the commercial contract specifies otherwise).
- The base unit is assigned once per anesthetic — it does not change based on anesthesia duration.
- If multiple surgical procedures are performed under a single anesthetic, report only the anesthesia code with the highest base unit value.

## Step 3 — Calculate Time Units

Convert documented anesthesia time to time units.

- **Anesthesia time begins**: When the anesthesiologist or CRNA begins preparing the patient for anesthesia (e.g., placing monitors, starting IV access in the OR) and ends when the anesthesiologist or CRNA is no longer in personal attendance (patient is safely placed under post-anesthesia supervision).
- **Time unit calculation**: Total anesthesia minutes ÷ 15 = time units (most payers, including Medicare).
  - Example: 90 minutes of anesthesia = 90 ÷ 15 = 6.0 time units.
  - Example: 47 minutes = 47 ÷ 15 = 3.13 time units (Medicare rounds to one decimal; some payers round differently).
- **Medicare time reporting**: Report actual minutes on the claim (field 24G on CMS-1500 or in anesthesia time fields). The MAC calculates time units.
- **Commercial payers**: Some require time units; others require actual minutes. Check payer-specific requirements.
- Anesthesia time must be continuous — do not include breaks or delays not attributable to anesthesia care.
- Pre-operative evaluation time and post-operative pain management time are NOT included in anesthesia time for the surgical procedure.

## Step 4 — Assign Physical Status Modifiers

Apply ASA Physical Status Classification to the patient.

| Modifier | ASA Class | Description | Additional Units (Medicare) |
|----------|-----------|-------------|---------------------------|
| P1 | ASA I | Normal healthy patient | 0 |
| P2 | ASA II | Patient with mild systemic disease | 0 |
| P3 | ASA III | Patient with severe systemic disease | 1 |
| P4 | ASA IV | Patient with severe systemic disease that is a constant threat to life | 2 |
| P5 | ASA V | Moribund patient not expected to survive without the operation | 3 |
| P6 | ASA VI | Brain-dead patient for organ donation | 0 |

- Physical status is assigned by the anesthesiologist/CRNA based on pre-operative evaluation.
- **Medicare** adds physical status units (P3 = +1, P4 = +2, P5 = +3) to the total unit calculation. P1, P2, and P6 add 0 units.
- **Commercial payers** vary — some do not recognize physical status additional units. Check the contract.
- The physical status modifier must match the documented ASA classification in the pre-anesthesia evaluation.

## Step 5 — Apply Qualifying Circumstance Codes

Report add-on codes for conditions that increase anesthesia complexity.

- **99100**: Anesthesia for patient of extreme age (under 1 year or over 70 years). Adds 1 unit.
- **99116**: Anesthesia complicated by utilization of total body hypothermia. Adds 5 units.
- **99135**: Anesthesia complicated by utilization of controlled hypotension. Adds 5 units.
- **99140**: Anesthesia complicated by emergency conditions. Adds 2 units.
- Qualifying circumstance codes are add-on codes — they are reported in addition to the primary anesthesia code.
- Multiple qualifying circumstances may apply to the same case (e.g., 99100 + 99140 for emergency surgery on an elderly patient).
- **Medicare does NOT recognize qualifying circumstance codes** — they are not separately payable. However, some commercial payers do recognize them. Check the contract.

## Step 6 — Apply Provider-Type Modifiers (Medical Direction Rules)

Select the correct modifier based on the anesthesia care model.

- **Modifier AA — Anesthesiologist personally performed**: The anesthesiologist was personally present and performed the entire anesthetic without a CRNA. Pays 100% of the anesthesia fee.
- **Modifier QK — Medical direction of 2–4 CRNAs**: The anesthesiologist medically directs 2–4 concurrent cases with CRNAs. The anesthesiologist bills with QK (pays 50%); each CRNA bills with QX (pays 50%).
- **Modifier QX — CRNA under medical direction**: The CRNA provides anesthesia under the medical direction of an anesthesiologist. Pays 50%.
- **Modifier QY — Medical direction of one CRNA**: The anesthesiologist medically directs a single CRNA. Anesthesiologist bills with QY (pays 50%); CRNA bills with QX (pays 50%).
- **Modifier QZ — CRNA without medical direction**: The CRNA provides anesthesia independently without any physician direction. Pays 100% of the CRNA fee schedule.
- **Modifier AD — More than 4 concurrent procedures**: The anesthesiologist is supervising (not directing) more than 4 concurrent cases. Medical supervision pays a flat rate per case (3 base units, no time).

**Medical direction requirements (7 conditions):**
The anesthesiologist must fulfill ALL seven for medical direction (QK/QY):
1. Perform a pre-anesthesia exam and evaluation
2. Prescribe the anesthesia plan
3. Personally participate in the most demanding aspects of the anesthesia plan (induction and emergence)
4. Ensure that all procedures in the anesthesia plan are performed by a qualified individual
5. Monitor the course of anesthesia at frequent intervals
6. Remain physically available for immediate diagnosis and treatment of emergencies
7. Provide post-anesthesia care

## Step 7 — Calculate Total Reimbursement

Apply the anesthesia payment formula.

**Formula**: Payment = (Base Units + Time Units + Modifying Units) × Conversion Factor

- **Example**: Hip replacement, 120 minutes, ASA III patient, anesthesiologist personally performed.
  - Base units (01210): 8
  - Time units: 120 ÷ 15 = 8.0
  - Physical status (P3): +1
  - Qualifying circumstances: 0
  - Total units: 8 + 8 + 1 = 17
  - Payment: 17 × conversion factor (e.g., $22.27 Medicare 2024) = $378.59
- The conversion factor varies by payer, geographic locality, and contract terms.
- Medicare publishes an anesthesia conversion factor annually in the Physician Fee Schedule Final Rule.

---

## Checkpoint B — Review

- [ ] Anesthesia CPT code matches the surgical procedure documented in the operative report
- [ ] Base units match the ASA Relative Value Guide (commercial) or CMS base units (Medicare)
- [ ] Anesthesia start/end times are documented and time units are calculated correctly
- [ ] ASA physical status modifier matches the pre-anesthesia evaluation
- [ ] Qualifying circumstance codes are applied only when documented and recognized by the payer
- [ ] Provider-type modifier (AA, QK, QX, QY, QZ, AD) matches the actual anesthesia care model
- [ ] Medical direction requirements (7 conditions) are documented when QK/QY is used
- [ ] Total unit calculation is arithmetically correct

---

## Quality Audit

- [ ] Time documentation on the anesthesia record includes continuous start-to-end times without gaps
- [ ] Concurrent case documentation supports the medical direction claim (anesthesiologist present at induction/emergence for each case)
- [ ] Physical status assignment is clinically appropriate and consistent with the patient's medical history
- [ ] Multiple procedures under a single anesthetic report only the highest base-unit code
- [ ] MAC (monitored anesthesia care) cases meet medical necessity criteria when billed separately from the procedure
- [ ] Post-operative pain management (62320–62327, 01996) is coded separately when applicable and not double-counted in surgical anesthesia time

---

## Guidelines

- Follow ASA Relative Value Guide for base unit assignments and coding conventions
- Apply CMS Medicare Claims Processing Manual Chapter 12 §50 for Medicare anesthesia billing rules
- Reference CMS anesthesia base unit file for Medicare-specific base unit values
- Follow ASA Physical Status Classification System definitions for modifier assignment
- Apply CMS medical direction rules (7 conditions) for modifier QK/QY billing
- Never bill anesthesia time for periods where the provider was not in continuous attendance
- Mark with [VERIFY] any case where the anesthesia code-to-surgical procedure mapping is ambiguous
- Include disclaimer that anesthesia reimbursement is highly payer-specific and conversion factors vary by contract
