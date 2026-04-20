---
name: managing-critical-laboratory-values
language: en
description: Tracks critical value notification with documentation requirements and clinical correlation. Use when reporting critical lab values, verifying notification, or documenting critical result acknowledgment.
tags:
  - management
  - pathology
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Critical Laboratory Values

Tracks critical value notification with documentation requirements and clinical correlation.

## Why This Skill Exists

Critical laboratory values — results that represent life-threatening conditions requiring immediate clinical action — are among the most time-sensitive communications in healthcare. Failure to promptly notify a clinician of a potassium of 6.8 mEq/L, a platelet count of 10,000/uL, or a positive blood culture can result in patient death. Studies have documented adverse events and mortality directly attributable to delayed critical value reporting, making this one of the highest-risk failure points in laboratory operations.

CLIA 42 CFR 493.1291 requires laboratories to immediately alert the individual or entity requesting the test when results indicate a life-threatening condition. CAP accreditation (GEN.41329) requires a documented critical value policy with defined thresholds, notification process, documentation requirements, and quality monitoring. The Joint Commission's National Patient Safety Goals (NPSG.02.03.01) mandate timely reporting of critical results including critical values, critical test results, and significant changes. This skill ensures compliant, rapid, and documented critical value notification.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Analyte and result** — What is the critical value being reported? Default: not specified; flag [VERIFY].
2. **Patient location** — Inpatient (floor, ICU, ED, OR), outpatient clinic, or external provider? Default: inpatient.
3. **Specimen integrity** — Has the specimen been verified for hemolysis, clotting, or mislabeling before reporting as critical? Default: specimen verified.
4. **Repeat confirmation** — Has the critical value been repeated/verified per institutional policy before notification? Default: yes, per policy.
5. **Responsible provider** — Who is the ordering provider or covering clinician? Default: per LIS provider assignment.
6. **Prior critical values** — Has this patient had prior critical results for the same analyte? Default: no.
7. **Time of result** — When was the result generated? Default: current.

### Documents to Request

- Laboratory result with critical value flag
- Institutional critical value list with defined thresholds
- Notification policy (who to call, escalation path, time limits)
- Specimen integrity assessment (hemolysis, clotting, collection site)
- Prior critical values for the same patient (trending)
- Documentation template for critical value notification
- Quality metrics dashboard for critical value reporting

---

## Step 1: Critical Value Identification

Verify the result against the institutional critical value list. Common critical values per CAP/ASCP consensus:

### Chemistry Critical Values

| Analyte | Low Critical | High Critical |
|---|---|---|
| Glucose | < 40 mg/dL | > 450 mg/dL |
| Potassium | < 2.8 mEq/L | > 6.2 mEq/L |
| Sodium | < 120 mEq/L | > 160 mEq/L |
| Calcium (total) | < 6.0 mg/dL | > 13.0 mg/dL |
| Calcium (ionized) | < 0.78 mmol/L | > 1.58 mmol/L |
| Magnesium | < 1.0 mg/dL | > 4.7 mg/dL |
| Phosphorus | < 1.0 mg/dL | > 8.9 mg/dL |
| Creatinine | — | > 10.0 mg/dL (new, not dialysis) |
| Lactate | — | > 4.0 mmol/L |
| Troponin | — | Institutional threshold for new elevation |
| pH (blood gas) | < 7.20 | > 7.60 |
| pCO2 | < 20 mmHg | > 70 mmHg |
| pO2 | < 40 mmHg | — |

### Hematology Critical Values

| Analyte | Low Critical | High Critical |
|---|---|---|
| Hemoglobin | < 7.0 g/dL | > 20.0 g/dL |
| WBC | < 2.0 x 10^9/L | > 30.0 x 10^9/L (or any blasts) |
| Platelet count | < 20 x 10^9/L | > 1000 x 10^9/L |
| INR | — | > 5.0 |
| PTT | — | > 100 seconds (non-heparin) |
| Fibrinogen | < 100 mg/dL | — |

### Microbiology / Blood Bank Critical Values

| Finding | Always Critical |
|---|---|
| Positive blood culture | Yes — STAT Gram stain with notification |
| Positive CSF culture/Gram stain | Yes — immediate notification |
| Acid-fast bacilli smear positive | Yes — infection control notification |
| Transfusion reaction workup positive | Yes — immediate notification to blood bank medical director |

---

## Step 2: Pre-Notification Verification

Before calling a critical value, verify:

1. **Repeat testing**: Per institutional policy, repeat the test on the same specimen (or from a fresh aliquot) to confirm the result. Exception: do not delay reporting of immediately life-threatening values (e.g., K > 7.0 mEq/L) for repeat — call immediately and repeat concurrently.
2. **Specimen integrity**: Check for hemolysis (falsely elevated K, LDH), clotting (falsely low platelets), lipemia (interference), underfill (coagulation), or IV contamination.
3. **Patient identity**: Verify the specimen label matches the patient record. A critical value on a mislabeled specimen is doubly dangerous.
4. **Delta check**: Compare to the patient's previous result. A sudden change (e.g., K from 4.0 to 7.2) may indicate specimen error rather than clinical change. Investigate before reporting if the delta is physiologically implausible.
5. **Known status**: Check if the patient is on dialysis (creatinine/potassium), anticoagulation therapy (INR/PTT), or chemotherapy (WBC/platelets) — the value may still be critical but the clinical team may already be aware.

---

## Step 3: Notification Process

Execute the notification within the institutional time limit (typically 15-30 minutes from result verification):

**Notification steps:**
1. Call the ordering provider or covering clinician directly (not a unit clerk, not voicemail).
2. If the ordering provider is unreachable within 10 minutes, escalate per the notification chain: covering resident → attending → charge nurse → nursing supervisor → laboratory director.
3. Communicate using a structured format:
   - Patient name and identifiers
   - Test name and critical result value
   - Specimen type and collection time
   - Whether the result was repeat-confirmed
   - Any specimen integrity concerns
4. **Read-back**: The receiving clinician must read back the critical value to confirm accurate receipt per Joint Commission NPSG.
5. Document the notification immediately.

**Special situations:**
- **Outpatient/external**: Call the ordering provider's office. If unreachable, call the patient directly (if institutionally permitted) or route to an urgent care pathway.
- **Operating room**: Notify the anesthesiologist or circulating nurse. Do not page the surgeon during a procedure unless that is the only route.
- **After hours**: Use the on-call provider notification system. Never leave a critical value as a voicemail without live confirmation.

---

## Step 4: Documentation Requirements

Document every critical value notification per CAP GEN.41329 and institutional policy:

| Required Documentation Element | Example |
|---|---|
| Date and time of result verification | 2024-03-15, 14:32 |
| Critical value and analyte | Potassium 6.8 mEq/L |
| Repeat confirmation (if performed) | Repeat value: 6.7 mEq/L |
| Name of person notified | Dr. Jane Smith, PGY-3 |
| Date and time of notification | 2024-03-15, 14:38 |
| Read-back confirmed | Yes |
| Name of laboratorian making notification | John Doe, MT(ASCP) |
| Escalation (if primary provider unreachable) | First call to Dr. Jones unsuccessful at 14:33; escalated to covering resident Dr. Smith |

---

## Step 5: Quality Monitoring and Compliance Reporting

Track critical value notification performance metrics:

**Key performance indicators:**
- **Notification time**: Time from result verification to clinician notification (target: < 15-30 minutes per institutional policy).
- **Compliance rate**: Percentage of critical values with complete documentation (target: > 98%).
- **Escalation rate**: Frequency of escalation beyond primary provider (investigate if > 15%).
- **Repeat critical rate**: Frequency of repeat critical values on the same patient within 24 hours (may indicate inadequate clinical response or specimen issues).
- **False critical rate**: Critical values that were subsequently determined to be erroneous (specimen issues, instrument malfunction) — target: < 2%.

Report metrics monthly to laboratory leadership. Investigate individual cases where notification time exceeds the institutional threshold.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Was the critical value verified by repeat testing or specimen integrity assessment before notification?
2. Was the notification made to a responsible licensed provider (not a clerk or voicemail)?
3. Was a read-back obtained and documented?
4. Is the complete notification documentation in the LIS (result, provider name, time, read-back)?
5. Was the notification completed within the institutional time limit?

---

## Quality Audit

- [ ] Critical value identified against the institutional approved threshold list
- [ ] Repeat testing performed (or concurrent repeat initiated for immediately life-threatening values)
- [ ] Specimen integrity verified before notification (hemolysis, clotting, labeling)
- [ ] Delta check performed against previous patient results
- [ ] Notification made to a licensed responsible provider (not unit clerk)
- [ ] Read-back obtained and confirmed
- [ ] Notification completed within institutional time limit (typically 15-30 minutes)
- [ ] Complete documentation entered in LIS (result, provider, time, read-back, laboratorian)
- [ ] Escalation pathway followed when primary provider unreachable
- [ ] Outpatient critical values routed through appropriate notification pathway
- [ ] Monthly compliance metrics reviewed by laboratory leadership
- [ ] Individual cases exceeding time thresholds investigated with root cause analysis
- [ ] Critical value list reviewed and updated at least annually by laboratory director

---

## Guidelines

- Never leave a critical value notification as a voicemail or written message without live verbal confirmation and read-back from a licensed provider
- Verify specimen integrity before reporting; a critically elevated potassium in a hemolyzed specimen should be investigated, not blindly reported as critical
- Do not delay notification of immediately life-threatening values (K > 7.0, glucose < 30, pH < 7.10) for repeat confirmation — call immediately and repeat concurrently
- Apply the institutional critical value list, which should be reviewed and approved annually by the laboratory director in collaboration with clinical leadership
- Document every element of the notification: who was called, when, what was communicated, who acknowledged, and whether read-back was confirmed
- Track notification times as a key quality metric; CAP expects laboratories to demonstrate continuous monitoring and improvement in critical value reporting timeliness
- For repeat critical values on the same patient within 24 hours, institutional policy should define whether re-notification is required (most institutions require re-notification unless the clinician has acknowledged awareness)
- Maintain the critical value list as a living document; review annually and update thresholds based on clinical consensus, patient population, and current medical evidence
