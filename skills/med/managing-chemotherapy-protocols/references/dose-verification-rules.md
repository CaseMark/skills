# Dose Verification Rules

Rules for checking a prescriber's antineoplastic order against the regimen it claims to follow. Every number here is protocol or label content to compare against an order; none of it is a dose for a patient. Where the institution's order set or a trial protocol states a different rule, that document governs for the order it covers; record the difference.

## Contents

1. Body-size variables: height, weight and BSA
2. BSA caps and alternative weights
3. Carboplatin and the Calvert formula
4. Cumulative-dose tracking
5. Cycle day and interval
6. Hold and modify parameters
7. Dose comparison and tolerance
8. Time-bound checks

## 1. Body-size variables: height, weight and BSA

- Height and weight are measured and documented in metric units (kg, cm). Before a newly prescribed treatment plan is prepared and administered, both the measurement and the documentation are verified by two individuals, one of them a licensed clinician. Re-measurement frequency is set by organization policy (ASCO-ONS 2024, Standard 1.7).
- Do not accept a stated, estimated or historical weight, or a weight from a previous encounter, as the dosing weight (ISMP Targeted Medication Safety Best Practices for Hospitals 2026-2027, Best Practice 3).
- Look for pound-kilogram errors: a weight that is about 2.2 times the last recorded weight, or an order header that shows pounds.
- The order must state the calculation methodology, the variables used, how often they are re-evaluated, and the change that triggers recalculation (ASCO-ONS 2024, Standards 3.9.8.1-3.9.8.4). If the order set gives a recalculation threshold (for example a weight change of a stated percentage), apply that threshold; if it gives none, record the gap as a policy election.
- BSA formula: ASCO 2021 finds no evidence favoring one standard formula (Recommendation 6). Use the formula the order set names. Mosteller: BSA (m²) = square root of [height (cm) × weight (kg) / 3600] (Mosteller, N Engl J Med 1987;317:1098, as defined in the NCI Thesaurus). If the order set names DuBois or another formula, use it and say so.
- Show the arithmetic: inputs with date, time and source; unrounded BSA; rounded BSA under the order set's rounding rule.

## 2. BSA caps and alternative weights

- ASCO 2021, Recommendation 1: full weight-based dosing of cytotoxic chemotherapy should be offered regardless of obesity status (evidence-based; evidence quality low; strength moderate). The panel notes that historical capping or idealized-weight dosing lacks support and that underdosing is associated with inferior outcomes in retrospective data.
- Recommendation 2: fixed dosing is limited to select cytotoxic agents (for example bleomycin).
- Recommendations 3 and 4: checkpoint inhibitors and targeted therapies follow FDA-approved prescribing information regardless of obesity status.
- Recommendation 5: after high-grade toxicity, dose reduction follows the same guidelines for all patients regardless of obesity.
- The panel states that limiting vincristine to 2.0 mg in trial protocols is not supported by data, and that FDA prescribing information does not limit vincristine doses. Many protocols still state a 2 mg maximum. Verify the order against the protocol in use; never add or remove a cap on your own.
- A BSA capped at 2.0 m², or a dose on ideal or adjusted weight, is a discrepancy unless the order or note documents a clinical reason (for example prior toxicity, a protocol that specifies the cap, or a stated palliative choice). Classify a documented reason as a prescriber decision, not an error; classify a missing reason as "Discrepancy: clarification required".

## 3. Carboplatin and the Calvert formula

- Label formula: Total dose (mg) = target AUC (mg/mL·min) × (GFR + 25). The dose is in mg, not mg/m². The original studies measured GFR by 51Cr-EDTA clearance (carboplatin labels on DailyMed and Pfizer Medical). The 2025 KYXATA label states that GFR is commonly calculated as estimated creatinine clearance by Cockcroft-Gault.
- GFR cap: the NCI CTEP letter of October 22, 2010 states that the GFR used in the Calvert formula should not exceed 125 mL/min when the dose rests on an estimated GFR, giving a maximum dose of target AUC × 150 mL/min (AUC 6: 900 mg; AUC 5: 750 mg; AUC 4: 600 mg). For an abnormally low serum creatinine, it allows estimating GFR with a minimum creatinine of 0.6 mg/dL or capping estimated GFR at 125 mL/min, and says that once the initial dose is set it need not be recalculated for later cycles unless toxicity requires a lower dose. The FDA issued an October 2010 notice on the same point (reported by CAP Today, January 2011); the FDA page itself was not readable `[VERIFY]`. The current US labels read do not state the cap. Apply the cap the order set or protocol states; if it states none, flag the cap question as a policy election and show both doses.
- Cockcroft-Gault: CrCl (mL/min) = (140 − age) × weight (kg) × (0.85 if female) / (72 × serum creatinine in mg/dL) (StatPearls, Creatinine Clearance). Use the weight type the order set names (actual, ideal, adjusted).
- A lab-reported eGFR (CKD-EPI or MDRD) is in mL/min/1.73 m². Do not place it in the Calvert formula unless the order set says how to convert it to mL/min; flag it otherwise.
- A measured GFR (nuclear or iohexol) or a measured 24-hour creatinine clearance is a different input from an estimate. Use it only if the order set allows that input, and record which input was used. CTEP states that label dosing is designed around measured GFR.
- Carboplatin dose-adjustment table in the label (single agent or with cyclophosphamide, from the prior course nadir): platelets over 100,000 and neutrophils over 2,000: 125 percent; 50,000-100,000 and 500-2,000: no adjustment; under 50,000 and under 500: 75 percent. Escalations above 125 percent were not recommended. This is label content; the order set governs the order.

## 4. Cumulative-dose tracking

ASCO-ONS 2024, Standard 4.5.3: cumulative doses are tracked for agents associated with cumulative toxicity. Labels for the anthracyclines direct that prior doses of other anthracyclines or anthracenediones be included in the total (doxorubicin and idarubicin labels). Build the total from every source: this facility, outside records, earlier lines of therapy, trial participation and pediatric treatment.

| Agent (label read) | Label statement on cumulative dose |
|---|---|
| Doxorubicin (Sun Pharma, rev. 1/2022; Pfizer Medical) | Cardiomyopathy incidence 1 to 20 percent for cumulative doses of 300 to 500 mg/m² given every 3 weeks (Pfizer: 1-2% at 300, 3-5% at 400, 5-8% at 450, 6-20% at 500 mg/m²); cumulative doses above 550 mg/m² are associated with an increased risk of cardiomyopathy; include prior anthracyclines and anthracenediones |
| Epirubicin (Hospira, rev. 11/2015) | CHF about 0.9% at 550, 1.6% at 700 and 3.3% at 900 mg/m²; risk rises rapidly above 900 mg/m², which should be exceeded only with extreme caution; prior anthracycline treatment up to the maximum cumulative dose is a contraindication |
| Daunorubicin (Meitheal) | Myocardial toxicity increases after a total cumulative dose above 400 to 550 mg/m² in adults, 300 mg/m² in children over 2 years, or 10 mg/kg in children under 2 years |
| Idarubicin (Idamycin PFS, rev. 2/2026) | Increased CHF above 90 mg/m² in adults; include prior anthracyclines and anthracenediones; tolerable limit may be lower after mediastinal radiation |
| Mitoxantrone (Meitheal) | Cancer patients: symptomatic CHF risk about 2.6% up to 140 mg/m²; multiple sclerosis patients should not receive more than 140 mg/m² |

Converting one anthracycline to "doxorubicin equivalents" uses ratios that are not in these labels `[VERIFY]`; when the total mixes agents, list each agent's total separately and flag the combined assessment for the prescriber.

## 5. Cycle day and interval

- The order must carry the cycle number and day number (ASCO-ONS 2024, Standard 3.9.5); treatment day and cycle are part of the first verification (Standard 3.12.2.1.7).
- Count from the actual administration date of Day 1 of the current cycle, not the planned date. A delayed Day 1 moves every later day in that cycle and the next cycle's Day 1.
- Day 1 and mid-cycle days (Day 8, Day 15) often carry different hold parameters; apply the parameters for the day actually reached.
- Check the minimum interval the regimen states between doses and between cycles.

## 6. Hold and modify parameters

- The order set must list the parameters that require holding or modifying a dose: laboratory values, diagnostic results or a change in clinical status (ASCO-ONS 2024, Standard 3.9.13). The organization sets the interval for regimen-specific labs (Standard 4.3).
- Take thresholds from the order set or protocol for this regimen and this day. Do not substitute a generic table. If the order set lists none for a parameter the label addresses (for example the vincristine label's 50 percent reduction for direct bilirubin above 3 mg/100 mL), flag the gap.
- Check the lab collection time against the window the order set allows before treatment.
- A parameter that is met without a documented prescriber decision to treat is "Clarification required before preparation".

## 7. Dose comparison and tolerance

- Compare each ordered dose with the protocol-expected dose computed from verified variables. Report both, the difference in mg and as a percentage, and the order set's rounding or variance rule. If the order set states no variance rule, report the difference and classify the threshold as a policy election `[VERIFY]` against facility policy.
- A reduction documented in the order (dose level, percentage, reason) is compared with the protocol's dose-level table; an undocumented reduction is a discrepancy.

## 8. Time-bound checks

Each element has its own trigger. Do not run them all from the order date.

| Element | Trigger event that starts it | Rule and source |
|---|---|---|
| Two-person height and weight verification | Start of a newly prescribed treatment plan | Before preparation and administration of the new plan (ASCO-ONS 1.7) |
| Re-measurement of height and weight | The last verified measurement | Frequency per organization policy (ASCO-ONS 1.7) |
| Dose recalculation | A change in a dosing variable | The change that prompts recalculation, stated in the order (ASCO-ONS 3.9.8.4) |
| Laboratory clearance | Lab specimen collection time | Window per order set; interval per organization policy (ASCO-ONS 3.9.13, 4.3) |
| Cycle day | Actual administration date of the current cycle's Day 1 | Day count and next Day 1 from that date (ASCO-ONS 3.9.5) |
| Order validity | Order signature date | Number of cycles or time for which the order is valid (ASCO-ONS 3.9.16) |
| Prepared product use | Preparation date and time | Expiration on the label (ASCO-ONS 3.11.2.4) |
| Carboplatin dose recalculation | Initial dose calculation | Not required for later cycles unless toxicity requires a lower dose, per CTEP 2010; order set may differ |
| Cumulative anthracycline total | First anthracycline or anthracenedione dose at any facility | Lifetime total including other agents (labels; ASCO-ONS 4.5.3) |
| Oral refills | Each dispensing | Zero refills preferred default (ASCO-ONS 3.10.2) |
