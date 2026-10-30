# Output Template

Produce the header and the sections below in order. Put detail in tables. Every value names its source and date. Every dose, interval or agent appears as label or guideline content with its citation, never as an instruction for the patient.

## Contents

1. Header
2. Declined part (only when part of the request was declined)
3. Section 1. Review summary
4. Section 2. Source register and anticoagulant ledger
5. Section 3. Eligibility and dose check
6. Section 4. Renal function worksheet
7. Section 5. Interaction screen
8. Section 6. Warfarin INR and dose review (when warfarin is involved)
9. Section 7. Periprocedural timeline (when a procedure is planned)
10. Section 8. Transition and duplication check
11. Section 9. Reversal readiness or event review
12. Section 10. Reconciliation table
13. Section 11. Gaps and questions for the prescriber
14. Section 12. Hand-offs
15. Section 13. Open items and `[VERIFY]` list

## Header

- Patient identifier (de-identified unless the environment requires otherwise), age, sex, setting (inpatient, clinic, transition, procedure planning, event review), review date.
- Question as asked, restated in one line.
- Indication(s) for anticoagulation with source.
- Sources applied, each with version: for example "Eliquis label rev. 06/2026", "CHEST perioperative guideline 2022", "2023 ACC/AHA/ACCP/HRS AF guideline", "facility anticoagulation protocol dated <date>".
- Preparer line: "Draft for clinician and pharmacist review. Not an order."

## Declined part (only when part of the request was declined)

Place this block directly under the header whenever Checkpoint A's "decline that part" rule applied; the rest of the review follows as usual. Use one row per declined request and exactly one of these labels:

| Label | Use when the request was for |
|---|---|
| `Declined part: order or prescription` | An order, discharge prescription or medication change written for this patient |
| `Declined part: patient instructions` | A dosing, holding or restart plan addressed to the patient |
| `Declined part: order-set or protocol text` | An order sentence, order-set entry or protocol wording for adoption |
| `Declined part: undocumented assessment` | Recording or back-dating a bleeding-risk or hemostasis assessment not in the record |

| Label | What was asked | Why declined (Ground Rule 1 or 2) | Provided instead | Routed to |
|---|---|---|---|---|

"Provided instead" names the section of this review that gives the label or guideline comparison. "Routed to" names a role (prescriber, proceduralist, P&T committee), not a skill.

## 1. Review summary

| # | Item | Result | Basis in one line | Who decides |
|---|---|---|---|---|
| 1 | Agent eligibility | Consistent with label / Discrepancy / Source conflict / Cannot determine / Not applicable | | Prescriber |
| 2 | Dose against label | | | Prescriber |
| 3 | Interactions | | | Prescriber with pharmacist |
| 4 | Periprocedural plan | | | Prescriber with proceduralist |
| 5 | Transition and duplication | | | Prescriber |
| 6 | Reversal readiness or event | | | Treating team; P&T for protocol |

"Cannot determine" always names the missing fact and who can supply it. Lead with the discrepancy that carries the highest risk.

## 2. Source register and anticoagulant ledger

Source register, one row per document:

| Source | Type | Date | Status | Note |
|---|---|---|---|---|
| | MAR, home list, prescription, lab report, echo report, procedure schedule, op note, INR log, protocol, other | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

Anticoagulant ledger, one row per drug exposure, including parenteral and prophylactic doses:

| Drug | Dose and frequency | Start | Stop or last dose | Indication | Source (MAR, list, prescription) | Active now? |
|---|---|---|---|---|---|---|

## 3. Eligibility and dose check

| Check | Patient fact and source | Label or guideline content and citation | Result |
|---|---|---|---|
| Mechanical valve, moderate or greater mitral stenosis, TAVR, bioprosthetic valve | | | |
| Triple-positive APS | | | |
| Edoxaban CrCl > 95 (NVAF) | | | |
| HIT history (heparin, enoxaparin, 4F-PCC) | | | |
| Enoxaparin CrCl < 30 regimen, weight extremes | | | |
| Administration route (tube, crushing, post-bariatric) | | | |
| Concurrent antiplatelets after PCI (aspirin duration) | | | |
| Dose-adjustment criteria, listed one by one | | | |
| Interaction-driven adjustment | | | |

For apixaban in NVAF, list each of the three criteria with value, threshold and met or not met, then the count.

## 4. Renal function worksheet

```
Age:             <years>
Sex:             <female | male>
Weight used:     <kg> (<actual | ideal | adjusted>; source; date measured)
SCr:             <mg/dL> (collected <date>; steady state? <yes | no | unknown>)
CrCl (Cockcroft-Gault): <mL/min>   weight basis named by label: <actual | not named>
Other weight bases (only if a policy uses them): <value> mL/min each
eGFR on lab report: <value> mL/min/1.73 m2 (not used for a CrCl band)
Label band selected: <band> for <drug, indication>   changes with weight basis? <yes | no>
```

## 5. Interaction screen

| Interacting drug | Start date and source | Mechanism named in label | Label content for this anticoagulant | Result |
|---|---|---|---|---|

## 6. Warfarin INR and dose review

| Date and time drawn | INR | Doses taken prior 5 days (source) | Missed or extra doses | Interacting drug or diet change (date) | Dose change after result | Comment |
|---|---|---|---|---|---|---|

State the target range with its source, and whether each INR change can be attributed to a dose change made at least several days earlier (peak effect 72 to 96 hours per label 12.2).

## 7. Periprocedural timeline

| Element | Trigger event and time | Interval from source (citation) | Calendar date, weekday and time | Plan as written | Result |
|---|---|---|---|---|---|
| Last anticoagulant dose | Procedure day | | | | |
| Pre-procedure INR (warfarin) | Procedure date | | | | |
| Bridging start, last pre-op dose (only if justified) | Procedure start | | | | |
| Procedure | Schedule | | | | |
| Hemostasis documentation | End of procedure | | | | |
| Bridging restart (only if justified) | End of procedure | | | | |
| Anticoagulant resumption | End of procedure with hemostasis documented | | | | |

Record the bleeding-risk category and who assigned it, the thromboembolic risk category and its inputs, and hours from last dose to procedure. Each row carries its own trigger; never chain one row's time from another's.

## 8. Transition and duplication check

| Transition point | Drugs active before | Drugs active after | Overlap or gap (hours) | Label conversion rule | Result |
|---|---|---|---|---|---|

## 9. Reversal readiness or event review

| Item | Finding | Source | Content checked against | Result |
|---|---|---|---|---|
| Drug class and last dose time | | | | |
| Agent named in protocol or given | | | Agent label indication | |
| Agent availability on the date | | | FDA notice or pharmacy record | |
| Thromboembolic events after reversal | | | | |
| Restart plan documented | | | | |
| Protocol citation current | | | Joint Commission NPG.14.04.01 EP 1 (hospital) | |

## 10. Reconciliation table

| # | Fact | Source A says | Source B says | Controlling source and why | Effect on result |
|---|---|---|---|---|---|

Typical rows: home list dose against the MAR; EHR CrCl calculator against the worksheet; eGFR against CrCl; label interval against guideline interval; label reversal statement against the FDA availability notice; protocol citation against the current accreditation chapter.

## 11. Gaps and questions for the prescriber

| Gap or question | Item affected | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Who can resolve | Next step |
|---|---|---|---|---|

Questions are neutral ("The label criterion count is one of three; please confirm the intended dose"), never an instruction.

## 12. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| assessing-drug-interactions | Interactions beyond the label pairs | Medication list with dates | Did not grade non-label interactions |
| managing-renal-dose-adjustments | Other renally cleared drugs | CrCl worksheet | Did not adjust non-anticoagulant doses |
| reconciling-medications | Full list reconciliation across settings | Anticoagulant ledger | Did not reconcile non-anticoagulant drugs |
| managing-valvular-heart-disease | Valve type or stenosis grade unclear | Echo reports | Did not grade the valve |

## 13. Open items and `[VERIFY]` list

| # | Open item | Depends on | Owner | Next action | Changes a result? |
|---|---|---|---|---|---|

Then each `[VERIFY]` statement relied on, with what would settle it.

Close with: "Draft for clinician and pharmacist review. Not an order and not a dosing instruction."
