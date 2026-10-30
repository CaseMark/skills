# Periprocedural, Transition and Reversal Rules

Guideline and label content for comparison with a plan written by the treating team. Nothing here is an order. Every interval in Section 2 has its own trigger event; never compute one element from another element's anchor.

## Contents

1. Inputs a timeline needs
2. Interruption and resumption clocks, one trigger per element
3. How to count "days off"
4. Where the sources disagree
5. Bridging: when the evidence says no
6. Restart documentation
7. Transitions of care and duplicate anticoagulation
8. Reversal agents by drug class (status as of 2026-10-30)
9. Accreditation requirement: Joint Commission NPG.14.04.01

## 1. Inputs a timeline needs

- Procedure date and scheduled start time, from the schedule, not the referral.
- Procedural bleeding-risk category assigned by the proceduralist (CHEST 2022 Table 2: high, low-to-moderate, minimal). The reviewer does not assign it.
- Drug, dose, dosing times and the documented time of the last dose taken (MAR or patient report, labeled as which).
- CrCl from the worksheet in `references/label-dosing-rules.md` (needed for dabigatran; the CHEST and AF guideline DOAC tables assume CrCl above stated floors).
- Thromboembolic risk category (CHEST 2022 Table 1) with its inputs: valve type and position, CHA2DS2-VASc, stroke or TIA within 3 months, VTE timing, thrombophilia, cancer.
- Neuraxial anesthesia or a neuraxial catheter planned or not.

## 2. Interruption and resumption clocks, one trigger per element

| Element | Trigger event (anchor) | Interval content | Source |
|---|---|---|---|
| Warfarin, last dose | Procedure date | Stop 5 days or more before (conditional) | CHEST 2022 rec 1 |
| Warfarin, pre-procedure INR | Procedure date | INR immediately before the procedure; routine vitamin K for INR > 1.5 one to two days before is suggested against (conditional) | Warfarin label 2.4; CHEST 2022 rec 4 |
| Warfarin, resumption | End of procedure, with hemostasis documented | Within 24 hours (usually the evening of the procedure), at the usual dose, not doubled | CHEST 2022 recs 2, 3 |
| Apixaban, rivaroxaban, edoxaban, last dose | Procedure day | 1 day off before low-to-moderate bleed risk; 2 days off before high bleed risk | CHEST 2022 recs 22, 24, 25; AF guideline Table 18 |
| Dabigatran, CrCl 50 or more, last dose | Procedure day | 1 day off (low-to-moderate); 2 days off (high) | CHEST 2022 rec 23 |
| Dabigatran, CrCl below 50, last dose | Procedure day | 2 days off (low-to-moderate); 4 days off (high) | CHEST 2022 rec 23; AF guideline Table 18 (CrCl 30 to 50) |
| DOAC, resumption | End of procedure, with hemostasis documented | At least 24 hours after low-to-moderate; 48 to 72 hours after high bleed risk | CHEST 2022 rec 27; AF guideline periprocedural rec 5 |
| LMWH bridging (only where bridging is chosen), last pre-procedure dose | Procedure start time | About 24 hours before; half the total daily dose the day before | CHEST 2022 recs 18, 20 |
| LMWH bridging, first post-procedure dose | End of procedure | At least 24 hours (low-to-moderate); 48 to 72 hours (high) | CHEST 2022 rec 19 |
| IV UFH bridging, stop | Procedure start time | 4 hours or more before | CHEST 2022 rec 16 |
| IV UFH bridging, resume | End of procedure | 24 hours or more after, no bolus, lower-intensity infusion | CHEST 2022 rec 17 |
| Label minimums before surgery | Procedure time | Apixaban: at least 48 hours (moderate or high bleeding risk) or 24 hours (low); rivaroxaban and edoxaban: at least 24 hours; dabigatran: 1 to 2 days (CrCl 50 or more) or 3 to 5 days (CrCl below 50) | Eliquis 2.4; Xarelto 2.4; Savaysa 2.5; Pradaxa 2.8 |

For CrCl below the floors in AF guideline Table 18 (apixaban 25, rivaroxaban 30, edoxaban 15, dabigatran 30 mL/min), the guideline says few data exist and suggests considering 1 to 3 additional days, especially before high-bleed-risk procedures. Neuraxial procedures carry the boxed spinal/epidural hematoma warning on every DOAC label; anesthesia timing rules belong to the anesthesia team `[VERIFY]` against the current regional anesthesia guidance.

## 3. How to count "days off"

AF guideline Table 18 footnote: the number of days is the number of full days before the day of surgery on which no dose is taken, and no dose is taken on the day of surgery. For a twice-daily drug held "1 day" with the last dose at 20:00 and surgery at 08:00, 36 hours have passed. PAUSE used the same design: 1 day off gave a 36 to 42 hour interval (about 3 half-lives) and 2 days off a 60 to 68 hour interval (about 5 half-lives).

Worked count for a 08:00 procedure on day 0: 1 day off means last dose on day -2; 2 days off, day -3; 4 days off, day -5. Write the calendar date and weekday of the last permitted dose and the hours from last dose to procedure. A plan that says "hold 2 days" without a last-dose date is incomplete.

## 4. Where the sources disagree

- Apixaban label: at least 48 hours before procedures with a moderate or high bleeding risk. CHEST 2022 groups low and moderate together (1 day off, about 36 to 42 hours). For a procedure the team calls moderate risk, the two do not agree; name the conflict and leave the choice to the prescriber under the facility protocol.
- Dabigatran label gives ranges (3 to 5 days for CrCl below 50); CHEST and the AF guideline give point values. Report both.
- PAUSE excluded apixaban users with CrCl below 25 and dabigatran or rivaroxaban users below 30, and did not study edoxaban. The CHEST edoxaban schedule rests on extrapolation (very low certainty).

## 5. Bridging: when the evidence says no

- BRIDGE (NEJM 2015;373:823-833): AF on warfarin, warfarin stopped 5 days before; no bridging was noninferior for arterial thromboembolism (0.4% vs 0.3%) and bridging caused more major bleeding (3.2% vs 1.3%). Mechanical valves, stroke or TIA within 12 weeks and CrCl below 30 were excluded.
- PAUSE (JAMA Intern Med 2019;179:1469-1478): 3,007 AF patients on apixaban, dabigatran or rivaroxaban managed by a fixed schedule with no bridging and no pre-procedure coagulation testing; 30-day major bleeding 0.90% to 1.85% and arterial thromboembolism 0.16% to 0.60% across cohorts.
- CHEST 2022: against bridging in AF on VKA (strong, moderate certainty); against bridging for VTE as the sole indication, for mechanical valves, and for low-to-moderate thromboembolic risk (conditional); for bridging in high-risk VKA patients (conditional, very low certainty); against bridging during DOAC interruption (conditional).
- 2023 AF guideline: no bridging when interrupting warfarin or a DOAC, excluding recent stroke or TIA or a mechanical valve (Class 1); LMWH bridging during warfarin interruption is "3: Harm" except with a mechanical valve or recent stroke or TIA.

A bridging plan passes review only when the high-risk feature that justifies it is documented and sourced. A DOAC plan with bridging is a discrepancy unless the prescriber records a reason.

## 6. Restart documentation

Before a resumption time is accepted as planned, the record should show: the proceduralist's note that hemostasis is adequate (label wording for apixaban and edoxaban), the bleeding-risk category the interval was chosen from, any drain output or transfusion, neuraxial catheter status, and whether the patient can take oral medication (edoxaban label: give a parenteral anticoagulant first if not). A restart time with none of these is "Cannot determine", not "Consistent".

## 7. Transitions of care and duplicate anticoagulation

Check at admission, transfer, procedure, discharge and agent switch:

- Home anticoagulant and any inpatient anticoagulant active at the same time, including order-set VTE prophylaxis (enoxaparin, heparin subcutaneous) added to a patient already on therapeutic anticoagulation.
- Switch overlaps against the label conversion table (`references/label-dosing-rules.md`, Section 9): INR threshold to start a DOAC after warfarin; parenteral bridge when going from apixaban or rivaroxaban to warfarin, since the DOAC raises INR.
- Formulary substitution that changes the drug but leaves the home drug on the discharge list.
- Discharge list, MAR and prescription agree on drug, strength, frequency, indication, intended duration and the person who follows the INR or renal function.

Joint Commission NPG.14.05.01 (medication information) applies to the list itself; full list reconciliation goes to reconciling-medications or reconciling-inpatient-medications.

## 8. Reversal agents by drug class (status as of 2026-10-30)

| Anticoagulant | Agent and label status | Notes |
|---|---|---|
| Dabigatran | Idarucizumab (Praxbind): indicated in patients treated with Pradaxa for emergency surgery or urgent procedures, or life-threatening or uncontrolled bleeding; 5 g as two 2.5 g vials | Labeled for dabigatran only. AF guideline: Class 1; activated PCC reasonable if unavailable (2a) |
| Warfarin (VKA) | 4F-PCC (Kcentra): indicated for urgent reversal of VKA-induced factor deficiency with acute major bleeding or urgent surgery; dose by pre-treatment INR and weight (25, 35 or 50 units/kg for INR 2 to < 4, 4 to 6, > 6; capped at 100 kg); give vitamin K concurrently; repeat dosing not recommended | AF guideline Class 1 (A): 4F-PCC plus IV vitamin K over plasma |
| Apixaban, rivaroxaban, edoxaban | Andexanet alfa (Andexxa): AstraZeneca ended U.S. commercial sales by December 22, 2025, and requested withdrawal of the BLA; FDA judged risks to outweigh benefits (ANNEXA-I thrombosis 14.6% vs 6.9%). FDA CBER lists it discontinued January 2026 | 4F-PCC for factor Xa inhibitors is outside the Kcentra label; the AF guideline gives it Class 1 (C-LD) for life-threatening bleeding. VA PBM (January 2026): no FDA-approved product is indicated for factor Xa inhibitor reversal |
| Any DOAC | Protamine and vitamin K are not expected to affect apixaban (Eliquis label 5.2); hemodialysis does not substantially affect apixaban exposure (same section); VA PBM lists hemodialysis among supportive measures for dabigatran | Activated charcoal for recent ingestion per labels |

Source conflict to name whenever apixaban reversal is discussed: the Eliquis label revised 06/2026 still states "An agent to reverse the anti-factor Xa activity of apixaban is available" (highlights, 5.2 and 10), while FDA's Andexxa notice says U.S. sales ended December 22, 2025. The FDA notice governs availability; the label statement is stale.

Reversal review checklist: drug class matched to agent; time of last dose; renal function (dabigatran); whether bleeding met the agent's labeled indication; product actually available on the date; thromboembolic events after reversal; documented plan and timing for restarting anticoagulation.

## 9. Accreditation requirement: Joint Commission NPG.14.04.01

From January 1, 2026, the Hospital and Critical Access Hospital programs replaced National Patient Safety Goals with National Performance Goals. NPSG.03.05.01 became NPG.14.04.01: "The hospital reduces the likelihood of patient harm associated with the use of anticoagulant therapy." Its elements of performance in the January 2026 hospital chapter:

- EP 1: approved protocols and evidence-based guidelines for reversal and management of bleeding events for each anticoagulant.
- EP 2: approved protocols and guidelines for perioperative management of all patients on oral anticoagulants (bridging, stop timing, restart timing and dosing).
- EP 3: oral unit-dose products, prefilled syringes or premixed infusion bags when available.

The note excludes routine short-term prophylactic anticoagulation for VTE prevention. Where the other former NPSG.03.05.01 elements (baseline and ongoing INR, education, programmable pumps) now sit, and whether ambulatory and nursing care center programs still use NPSG.03.05.01, are `[VERIFY]`. A hospital protocol that still cites NPSG.03.05.01 or lists andexanet as available is a protocol-update finding, not a patient finding.
