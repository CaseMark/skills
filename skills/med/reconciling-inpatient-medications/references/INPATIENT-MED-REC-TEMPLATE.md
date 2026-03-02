# Inpatient Medication Reconciliation Template

Use this template to produce the final reconciled medication list. Every field is required — no blanks permitted in the final output.

---

## Header

```
===============================================================
MEDICATION RECONCILIATION REPORT
===============================================================
Patient:              [Patient ID / Name]
Date of Birth:        [DOB]
Encounter:            [Encounter/MRN]
Transition Type:      [ ] Admission   [ ] Transfer   [ ] Discharge
Transition Detail:    [Home → Inpatient / ICU → Floor / Inpatient → Home/SNF/LTAC]
Date/Time:            [YYYY-MM-DD HH:MM]
Reconciler:           [Name, Credentials]
Verifier:             [Name, Credentials]
Allergies/ADRs:       [List with reaction type and severity]
Renal Function:       [CrCl/eGFR and date]
Hepatic Function:     [Child-Pugh / MELD if applicable]
Weight:               [kg]
===============================================================
```

---

## Section 1: Reconciled Medication List

| # | Medication (Generic) | Dose | Route | Frequency | Indication | Disposition | Rationale for Change |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | Continued / Modified / Substituted / Held / Discontinued / New | |
| 2 | | | | | | | |
| 3 | | | | | | | |

**Disposition Key:**
- **Continued** — Same medication, dose, route, frequency; no change
- **Modified** — Same medication; dose, route, or frequency changed (state what changed)
- **Substituted** — Therapeutic swap; state original drug and confirm dose equivalence
- **Held** — Temporarily paused; state reason and restart plan
- **Discontinued** — Permanently stopped; state reason
- **New** — Started during this encounter; state indication and intended duration

---

## Section 2: Discrepancy Log

| # | Medication | Discrepancy Type | Source vs. Target Detail | Severity | Recommended Action | Status |
|---|---|---|---|---|---|---|
| D1 | | Omission / Duplication / Dose Mismatch / Route Mismatch / Interaction / Unaddressed Hold | | Critical / Major / Minor | | Open / Resolved / Escalated |
| D2 | | | | | | |

**Severity Definitions:**
- **Critical** — High-risk medication class involved OR immediate potential for patient harm; requires resolution before transition
- **Major** — Clinically significant discrepancy that could affect treatment outcomes; resolve within transition window
- **Minor** — Documentation gap or low-risk inconsistency; resolve within 24 hours

---

## Section 3: High-Risk Medication Verification

Complete one row for each high-risk medication present. Every high-risk medication must appear here even if disposition is "Continued" with no changes.

| Medication | Class | Home Dose | Current Inpatient Dose | Discharge/Transfer Dose | Level/Lab (if applicable) | Verified By |
|---|---|---|---|---|---|---|
| | Anticoagulant / Insulin / Cardiac / Seizure / Immunosuppressant / Opioid / Corticosteroid | | | | | |

---

## Section 4: Held Medications — Restart Plan

| Medication | Reason Held | Restart Criteria | Restart Dose | Restart Date/Timing | Responsible Provider |
|---|---|---|---|---|---|
| | | | | | |

If a held medication is NOT being restarted, move it to Section 1 with disposition "Discontinued" and document rationale.

---

## Section 5: New Medications — Patient Education Checklist

| Medication | Indication | Duration | Key Counseling Points | Prescriber |
|---|---|---|---|---|
| | | Definite end date / Ongoing / Until follow-up | | |

---

## Section 6: I-PASS Medication Handoff Summary

Use when reconciliation accompanies a care transition handoff.

```
I — Illness Severity:
    Medication complexity: [ ] Low (≤5 meds, no high-risk)
                           [ ] Moderate (6-12 meds OR 1 high-risk class)
                           [ ] High (13+ meds OR 2+ high-risk classes)

P — Patient Summary:
    Key diagnoses driving regimen: ___________________________
    Relevant organ function: Renal ___ Hepatic ___ Cardiac ___

A — Action List:
    Unresolved discrepancies: ________________________________
    Pending medication decisions: _____________________________
    Labs to follow: __________________________________________

S — Situation Awareness:
    High-risk medications to monitor: ________________________
    Drug levels pending: _____________________________________
    Anticipated changes next 12-24h: _________________________

S — Synthesis:
    Biggest medication risk for this patient: _________________
    Contingency if [condition]: ______________________________
```

---

## Section 7: Reconciliation Attestation

```
I have reviewed the medication lists from all available sources,
identified and addressed discrepancies, and verified the reconciled
list is accurate and complete to the best of available information.

Reconciler Signature: ___________________  Date/Time: ___________
Verifier Signature:   ___________________  Date/Time: ___________

Unresolved items escalated to: ________________________________
```

---

## Completion Checklist

- [ ] All source medications have an explicit disposition in Section 1
- [ ] All discrepancies logged in Section 2 with severity and recommended action
- [ ] Every high-risk medication verified in Section 3
- [ ] All held medications have a restart plan or are moved to Discontinued
- [ ] New medications have indication, duration, and education points
- [ ] I-PASS summary completed (if handoff transition)
- [ ] No [VERIFY] tags remain — all resolved or escalated
- [ ] Allergies confirmed consistent across all sources
- [ ] No Joint Commission "Do Not Use" abbreviations in document
- [ ] Attestation signed by reconciler and verifier
