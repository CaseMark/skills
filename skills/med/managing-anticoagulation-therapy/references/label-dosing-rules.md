# Label Dosing Rules for Review

Every dose, threshold and interval below is FDA label or guideline content, quoted so a reviewer can compare a regimen against it. None of it is an order or a dose for a particular patient. Labels change; each table names the label revision read on 2026-10-30 (see `references/primary-sources.md`). Re-check the current label before relying on a row.

## Contents

1. Eligibility screens before any dose check
2. Renal function: which number each label uses
3. Apixaban (Eliquis, label revised 06/2026)
4. Rivaroxaban (Xarelto, label revised 03/2026)
5. Dabigatran (Pradaxa capsules, label revised 6/2025)
6. Edoxaban (Savaysa, label revised 10/2023)
7. Warfarin (generic label, DailyMed version updated May 29, 2026)
8. Interacting drugs named in the labels
9. Switching between anticoagulants (label conversion rules)
10. Guideline overlays on dose and agent choice

## 1. Eligibility screens before any dose check

| Screen | Label or guideline content | Source |
|---|---|---|
| Mechanical heart valve | Dabigatran: contraindicated. Apixaban, rivaroxaban: use not recommended with prosthetic heart valves. Edoxaban: not recommended with mechanical valves | Pradaxa sec. 4, 5.4; Eliquis 5.4; Xarelto 5.8; Savaysa 5.5 |
| Moderate to severe mitral stenosis | Edoxaban label: not recommended. AF guideline: with rheumatic MS or MS of moderate or greater severity and AF, warfarin over DOACs (Class 1, B-R) | Savaysa 5.5; 2023 AF guideline 6.8.5 |
| TAVR | Rivaroxaban not recommended after TAVR (GALILEO) | Xarelto 5.8 |
| Bioprosthetic valve | Dabigatran: use not recommended (highlights). Other valve disease that is not moderate or greater MS or a mechanical valve: DOAC over VKA (AF guideline Class 1, B-NR) | Pradaxa highlights; AF guideline 6.8.5 |
| Triple-positive antiphospholipid syndrome | All four DOAC labels: not recommended. CHEST 2021 VTE: adjusted-dose VKA (target INR 2.5) over DOAC in confirmed APS (weak) | Eliquis 5.6; Xarelto 5.10; Pradaxa 5.6; Savaysa 5.6; CHEST 2021 statement 17 |
| Hemodynamically unstable PE or planned lysis | Apixaban, rivaroxaban: not recommended as an alternative to UFH for initial treatment | Eliquis 5.5; Xarelto 5.9 |
| Edoxaban in NVAF with high CrCl | Do not use when CrCl > 95 mL/min (boxed warning) | Savaysa 1.1, 5.1 |
| Active pathological bleeding | Contraindication on all four DOAC labels | Section 4 of each |

"Nonvalvular" in a DOAC indication is read against these rows, not against the word alone. An echo that grades the valve is the source; a problem-list entry is not.

## 2. Renal function: which number each label uses

| Drug and indication | Renal input the label uses | What the label says about the method |
|---|---|---|
| Apixaban, NVAF | Serum creatinine (mg/dL) as one of three criteria; not CrCl | Dose-reduction rule names SCr, age and weight (2.1, 8.6) |
| Rivaroxaban, all adult indications | CrCl bands | "Calculate CrCl based on actual weight" (Table 1 footnote) |
| Dabigatran, all adult indications | CrCl bands | Equation not named in the sections read `[VERIFY]` |
| Edoxaban, NVAF and VTE | CrCl bands | "Cockcroft-Gault CrCL = (140-age) x (weight in kg) x (0.85 if female) / (72 x creatinine in mg/dL)" (2.1); weight type not specified `[VERIFY]` |

Rules for the worksheet:

- An eGFR in mL/min/1.73 m2 from a lab report is not a CrCl and never fills a CrCl band.
- Show the inputs: age, sex, weight with its source and date, SCr with its collection date, and the result. The AF guideline's monitoring figure defines CrCl as based on actual body weight.
- Where a facility policy uses ideal or adjusted weight, run both, show whether the band changes, and record the difference as a policy election in conflict with the label (rivaroxaban) or with the guideline figure.
- Note when the SCr is not at steady state (acute kidney injury, dialysis day) and treat the band as provisional.

## 3. Apixaban (Eliquis, label revised 06/2026)

| Indication | Label dose content | Adjustment rule |
|---|---|---|
| NVAF | 5 mg twice daily for most patients | 2.5 mg twice daily only with at least two of: age 80 or older; weight 60 kg or less; SCr 1.5 mg/dL or higher |
| NVAF, ESRD on hemodialysis | Usual recommended dose per 2.1 (PK-based; outcomes unknown) | Label 8.6 |
| DVT/PE treatment | 10 mg twice daily for 7 days, then 5 mg twice daily | No renal adjustment |
| Reduce recurrence after at least 6 months of treatment | 2.5 mg twice daily | No renal adjustment |
| Combined P-gp and strong CYP3A4 inhibitor | Reduce 5 mg or 10 mg twice-daily doses by 50%; avoid if already on 2.5 mg twice daily | Clarithromycin: no adjustment (7.1) |

One criterion is never enough. Age alone, weight alone or SCr alone leaves the label dose at 5 mg twice daily. The AF guideline (6.3 supportive text) reports that inappropriately low DOAC doses were associated with higher stroke or systemic embolism risk without lower bleeding.

## 4. Rivaroxaban (Xarelto, label revised 03/2026)

| Indication | CrCl band (actual weight) | Label dose content |
|---|---|---|
| NVAF | > 50 mL/min | 20 mg once daily with evening meal |
| NVAF | 50 mL/min or less | 15 mg once daily with evening meal |
| DVT/PE treatment | 15 mL/min or more | 15 mg twice daily for 21 days, then 20 mg once daily, with food |
| DVT/PE treatment | < 15 mL/min | Avoid use |
| Reduce recurrence after at least 6 months | 15 mL/min or more | 10 mg once daily |
| CAD or PAD (with aspirin) | No CrCl adjustment | 2.5 mg twice daily |

ESRD on dialysis, NVAF: label 8.6 states 15 mg once daily gives concentrations similar to ROCKET AF; outcomes unknown.

## 5. Dabigatran (Pradaxa capsules, label revised 6/2025)

| Indication | CrCl band | Label dose content |
|---|---|---|
| NVAF | > 30 mL/min | 150 mg twice daily |
| NVAF | 15 to 30 mL/min | 75 mg twice daily |
| NVAF | < 15 mL/min or dialysis | Dosing recommendations cannot be provided |
| NVAF | 30 to 50 mL/min with dronedarone or systemic ketoconazole | Reduce to 75 mg twice daily |
| NVAF | < 30 mL/min with a P-gp inhibitor | Avoid coadministration |
| DVT/PE treatment and recurrence | > 30 mL/min | 150 mg twice daily (treatment after 5 to 10 days of parenteral therapy) |
| DVT/PE | 30 mL/min or less, or dialysis | Cannot be provided; avoid P-gp inhibitors when CrCl < 50 |

Capsule forms are not interchangeable mg for mg with other dabigatran forms (2.1). Use aPTT or ECT, not INR, when activity must be assessed (2.4).

## 6. Edoxaban (Savaysa, label revised 10/2023)

| Indication | Rule | Label dose content |
|---|---|---|
| NVAF | CrCl > 50 to 95 mL/min | 60 mg once daily |
| NVAF | CrCl 15 to 50 mL/min | 30 mg once daily |
| NVAF | CrCl > 95 mL/min | Do not use |
| NVAF | P-gp inhibitor | No dose reduction (7.3) |
| DVT/PE after 5 to 10 days of parenteral therapy | Standard | 60 mg once daily |
| DVT/PE | CrCl 15 to 50 mL/min, weight 60 kg or less, or certain P-gp inhibitors (any one) | 30 mg once daily |

The DVT/PE reduction is "any one" of three; the apixaban NVAF reduction is "two of three". Do not carry one rule to the other drug.

## 7. Warfarin (generic label, DailyMed version updated May 29, 2026)

- Monitoring: INR daily after the first dose until stable in range, then every 1 to 4 weeks (2.4). INR immediately before any dental or surgical procedure.
- Pharmacodynamics: effect within 24 hours, peak may be delayed 72 to 96 hours; a single dose acts for 2 to 5 days (12.2). An INR therefore reflects doses taken over the preceding days, not the last dose.
- Targets in label 2.2 (for comparison only): bileaflet or Medtronic Hall mechanical aortic valve in sinus rhythm without left atrial enlargement, INR 2.5 (2.0 to 3.0); tilting-disk or bileaflet mechanical mitral valve, INR 3.0 (2.5 to 3.5); caged-ball or caged-disk valve, INR 3.0 (2.5 to 3.5). An INR above 4.0 adds no benefit in most patients and raises bleeding risk. Valve targets in the current valvular guideline are `[VERIFY]`.
- Genotype tables (CYP2C9, VKORC1) inform initial dose ranges (2.3).
- Heparin overlap: continue full-dose heparin and overlap warfarin for 4 to 5 days and until the INR is in range (2.8).

INR review worksheet columns: date and time drawn, INR, warfarin doses taken on each of the prior 5 days (from the dose log, MAR or patient calendar, not the prescription), missed or extra doses, new or stopped interacting drugs with dates, diet or illness changes, and the dose change made after the result.

## 8. Interacting drugs named in the labels

| Drug | Combined P-gp and strong CYP3A4 inhibitor (e.g., ketoconazole, itraconazole, ritonavir) | Combined P-gp and strong CYP3A4 inducer (e.g., rifampin, carbamazepine, phenytoin, St. John's wort) |
|---|---|---|
| Apixaban | Reduce 5 or 10 mg twice daily by 50%; avoid at 2.5 mg twice daily | Avoid |
| Rivaroxaban | Avoid (ketoconazole, ritonavir); clarithromycin needs no precaution; with CrCl 15 to < 80 and a combined P-gp and moderate CYP3A inhibitor (e.g., erythromycin), do not use unless benefit justifies risk | Avoid |
| Dabigatran | P-gp inhibitors: see section 5 bands | P-gp inducer (e.g., rifampin): generally avoid |
| Edoxaban | NVAF: no reduction; DVT/PE: reduce for certain P-gp inhibitors | Avoid rifampin |

Antiplatelets, NSAIDs, SSRIs and SNRIs raise bleeding risk on every label. Other anticoagulants: Eliquis 7.3 says coadministration with heparin increases bleeding risk; Xarelto 7.4 says avoid concurrent use with other anticoagulants unless benefit outweighs risk; Savaysa 7.1 says long-term concomitant use is not recommended, short-term overlap only during transitions. A full interaction screen beyond these label pairs goes to assessing-drug-interactions.

## 9. Switching between anticoagulants (label conversion rules)

| From | To | Label rule |
|---|---|---|
| Warfarin | Apixaban | Start when INR is below 2.0 |
| Warfarin | Dabigatran | Start when INR is below 2.0 |
| Warfarin | Rivaroxaban | Start as soon as INR is below 3.0 (adults) |
| Warfarin | Edoxaban | Start when INR is 2.5 or less |
| Apixaban or rivaroxaban | Warfarin | Both affect INR; one approach: stop the DOAC and start a parenteral anticoagulant and warfarin at the time of the next DOAC dose |
| Edoxaban | Warfarin | Oral option with halved edoxaban and INR checks just before the daily dose, or the parenteral option |
| Dabigatran | Warfarin | Start warfarin 3, 2 or 1 days before stopping dabigatran for CrCl 50 or more, 30 to 50, or 15 to 30 |
| DOAC | Another non-warfarin anticoagulant | Start the new drug at the time of the next scheduled dose of the old one |
| UFH infusion | Edoxaban | Start 4 hours after stopping; rivaroxaban and dabigatran start when the infusion stops |

An overlap outside these rules, or a prophylactic heparin order running alongside a therapeutic anticoagulant, is a duplication finding.

## 10. Guideline overlays on dose and agent choice

- 2023 ACC/AHA/ACCP/HRS AF guideline: anticoagulation recommended at CHA2DS2-VASc 2 or more in men and 3 or more in women (Class 1); reasonable at 1 in men and 2 in women (2a); DOACs over warfarin unless moderate to severe rheumatic MS or a mechanical valve (Class 1); CKD stage 5 or dialysis: warfarin or an evidence-based apixaban dose might be reasonable (2b). Table 19 lists doses by CrCl.
- 2026 AHA/ACC AF performance and quality measures (built on the 2023 guideline): QM-4 counts DOAC use with a mechanical valve or mitral stenosis; QM-5 counts edoxaban or dabigatran in CKD stage 5 or dialysis.
- CHEST 2021 VTE (second update): DOAC over VKA for the 3-month treatment phase (strong); 3-month treatment phase then assess for extended therapy (strong); extended phase: reduced-dose apixaban 2.5 mg twice daily or rivaroxaban 10 mg daily over full dose (weak).
