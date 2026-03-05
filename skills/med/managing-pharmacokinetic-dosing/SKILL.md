---
name: managing-pharmacokinetic-dosing
description: Calculates individualized drug doses using pharmacokinetic parameters (vancomycin, aminoglycosides, phenytoin). Use when performing PK calculations, adjusting drug levels, or calculating loading/maintenance doses.
tags:
  - management
  - pharmacy
metadata:
  author: casemark
  practice_areas:
    - Clinical Pharmacy
    - Pharmacy
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Pharmacokinetic Dosing

Calculates individualized drug doses using pharmacokinetic parameters for narrow therapeutic index drugs including vancomycin, aminoglycosides, and phenytoin.

## Why This Skill Exists

Pharmacokinetic (PK) individualized dosing is essential for drugs with narrow therapeutic indices where the margin between efficacy and toxicity is small. Vancomycin nephrotoxicity increases significantly when AUC exceeds 600 mg·h/L, while subtherapeutic exposure (AUC <400) drives treatment failure and resistance. Aminoglycoside dosing errors contribute to irreversible ototoxicity and nephrotoxicity. Phenytoin's nonlinear (Michaelis-Menten) kinetics make empiric dose changes unpredictable without mathematical modeling.

The 2020 ASHP/IDSA/SIDP vancomycin consensus guidelines shifted monitoring from trough-based to AUC/MIC-guided dosing, requiring pharmacists to perform Bayesian or first-order PK calculations. This represents a fundamental change in clinical pharmacy practice. Institutions are expected to implement AUC-guided vancomycin dosing, and pharmacists are the primary clinicians performing these calculations. Competent PK dosing directly reduces drug toxicity, improves clinical outcomes, and decreases length of stay.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. Which drug requires PK dosing? (Default: vancomycin; alternatives: gentamicin, tobramycin, amikacin, phenytoin)
2. What are the patient demographics: age, sex, height, actual body weight? (Default: request)
3. What is the current renal function (SCr, CrCl by Cockcroft-Gault)? (Default: calculate)
4. Is this an initial dose calculation or a dose adjustment from measured levels? (Default: initial)
5. If adjusting, what are the measured serum drug levels with exact draw times and dose administration times? (Default: request)
6. What is the patient's fluid status (euvolemic, fluid overloaded, dehydrated)? (Default: euvolemic)
7. What is the infection site and suspected/confirmed pathogen with MIC? (Default: assume MRSA MIC 1 mcg/mL for vancomycin)
8. Is Bayesian PK software available (e.g., DoseMeRx, InsightRX, PrecisePK)? (Default: use first-order PK equations)

### Documents to Request

- Patient demographics: age, sex, height, actual body weight
- Labs: SCr (ideally 2+ values for trend), BUN, albumin (for phenytoin binding)
- Serum drug levels with exact collection times (date/time)
- Medication administration times (exact dose, route, infusion duration)
- Fluid balance and hemodynamic status
- Dialysis status and schedule if applicable
- Concomitant nephrotoxins (amphotericin B, contrast, loop diuretics, piperacillin-tazobactam)

---

## Step 1: Calculate Baseline Pharmacokinetic Parameters

**Creatinine Clearance (Cockcroft-Gault):**
CrCl = [(140 - age) × weight(kg)] / [72 × SCr(mg/dL)] (× 0.85 for females)

**Weight selection:**
- Use actual body weight (ABW) if within 20% of ideal body weight (IBW)
- Use adjusted body weight if ABW > 120% IBW: AdjBW = IBW + 0.4 × (ABW - IBW)
- IBW (male) = 50 + 2.3 × (height in inches - 60)
- IBW (female) = 45.5 + 2.3 × (height in inches - 60)

**Volume of distribution estimates:**

| Drug | Vd Estimate | Notes |
|---|---|---|
| Vancomycin | 0.7 L/kg (ABW) | Range 0.5-1.0; higher in fluid overload |
| Gentamicin/Tobramycin | 0.25 L/kg (AdjBW if obese) | Hydrophilic, distributes to ECF |
| Amikacin | 0.25 L/kg | Same principles as other aminoglycosides |
| Phenytoin | 0.65 L/kg | Highly protein-bound (~90%) |

---

## Step 2: Drug-Specific Initial Dosing

### Vancomycin (AUC/MIC-Guided per 2020 Guidelines)

**Target:** AUC₂₄ 400-600 mg·h/L (assuming MRSA MIC ≤ 1 mcg/mL)

**Loading dose:** 25-30 mg/kg ABW (for serious infections, round to nearest 250 mg, max 3 g)

**Maintenance dosing estimation:**
1. Estimate ke: ke = 0.00083 × CrCl + 0.0044
2. Estimate clearance: Cl = ke × Vd
3. Target AUC = 400-600: Dose/day = AUC_target × Cl
4. Divide daily dose into q8h, q12h, or q24h based on CrCl

| CrCl (mL/min) | Typical Frequency | Common Starting Dose |
|---|---|---|
| >90 | q8h or q12h | 15-20 mg/kg per dose |
| 50-89 | q12h | 15-20 mg/kg per dose |
| 20-49 | q24h | 15-20 mg/kg per dose |
| <20 | q48h or per levels | 15-20 mg/kg per dose |

### Aminoglycosides (Extended-Interval Dosing)

**Gentamicin/Tobramycin:** 5-7 mg/kg AdjBW q24h (if CrCl ≥60 mL/min)
**Amikacin:** 15-20 mg/kg AdjBW q24h (if CrCl ≥60 mL/min)

Use Hartford Nomogram: draw random level at 6-14 hours post-dose, plot on nomogram to determine interval (q24h, q36h, q48h).

### Phenytoin

**Loading dose:** 15-20 mg/kg IV (max rate 50 mg/min, or 25 mg/min if cardiac risk)
**Maintenance:** 4-6 mg/kg/day, adjusted by levels

**Corrected phenytoin formulas:**
- Hypoalbuminemia: Corrected level = Measured level / [(0.2 × albumin) + 0.1]
- Renal failure + hypoalbuminemia: Corrected level = Measured level / [(0.1 × albumin) + 0.1]

---

## Step 3: Level Interpretation and Dose Adjustment

### Vancomycin AUC Calculation (Two-Level Method)

1. Obtain trough (30 min pre-dose) and peak (1-2h post-infusion) at steady state (before 4th dose)
2. Calculate ke = ln(Cpeak/Ctrough) / Δt
3. Calculate t½ = 0.693 / ke
4. Calculate Vd = Dose / [Cpeak_extrapolated - Ctrough_extrapolated]
5. Calculate AUC₂₄ = Dose_daily / (ke × Vd)
6. Adjust dose proportionally: New dose = Current dose × (Target AUC / Calculated AUC)

### Aminoglycoside Traditional Dosing Adjustment

1. Measure peak (30 min post-infusion) and trough (30 min pre-dose)
2. Target peak: Gentamicin 8-10 mcg/mL (serious infection), Amikacin 25-35 mcg/mL
3. Target trough: Gentamicin <1 mcg/mL (extended interval), Amikacin <5 mcg/mL
4. Adjust dose for peak, adjust interval for trough

### Phenytoin (Michaelis-Menten Kinetics)

Phenytoin follows saturable metabolism. Small dose changes produce disproportionately large level changes.
- If at steady state with two different doses and their levels: apply Michaelis-Menten equation to solve for Vmax and Km
- Empiric adjustment: increase by no more than 30-50 mg/day when level is subtherapeutic
- Orbit graph method can be used as a clinical shortcut

---

## Step 4: Special Population Adjustments

| Population | Key Adjustments |
|---|---|
| Obesity (BMI >40) | Vancomycin: use ABW for Vd, cap loading at 3 g; Aminoglycosides: use AdjBW |
| Burns | Augmented renal clearance common; Vd increased; may need higher doses and shorter intervals |
| Critical illness/sepsis | Increased Vd, variable clearance; load aggressively, monitor frequently |
| Hemodialysis | Vancomycin: dose post-HD, redraw pre-next HD; Aminoglycosides: redraw post-HD |
| CRRT | Drug clearance depends on modality (CVVH, CVVHD, CVVHDF), filter type, and flow rates |
| Pediatrics | Weight-based dosing; different Vd and clearance allometry |
| Pregnancy | Increased Vd and renal clearance; therapeutic drug monitoring essential |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Were correct weight metrics used for each drug (ABW vs. AdjBW vs. IBW)?
2. Was CrCl calculated by Cockcroft-Gault (not CKD-EPI) and used for dosing?
3. Are serum level draw times verified as accurate (exact clock times)?
4. Has the AUC target (400-600) been used instead of trough-only for vancomycin?
5. Were special population adjustments applied where applicable?

---

## Quality Audit

- [ ] Cockcroft-Gault CrCl calculated with appropriate weight metric
- [ ] Volume of distribution estimated using correct body weight
- [ ] Loading dose calculated for drugs requiring it (vancomycin, phenytoin)
- [ ] Maintenance dose and interval matched to renal function
- [ ] Vancomycin dosing targets AUC 400-600 mg·h/L per 2020 consensus guidelines
- [ ] Aminoglycoside interval determined by nomogram or level-based calculation
- [ ] Phenytoin level corrected for albumin and renal status before interpretation
- [ ] Serum level draw times documented and verified for accuracy
- [ ] Steady-state confirmed before interpreting levels (4-5 half-lives)
- [ ] Concomitant nephrotoxins identified and noted
- [ ] Dose rounding follows institutional convention (e.g., vancomycin to nearest 250 mg)
- [ ] Special population factors addressed (obesity, dialysis, critical illness)
- [ ] Follow-up monitoring plan specified with next level draw time
- [ ] All calculations shown with units for reproducibility

---

## Guidelines

- Always verify serum level draw times with nursing documentation; incorrect times invalidate PK calculations
- Use Cockcroft-Gault for drug dosing (not CKD-EPI)—consistency with how dosing was studied in trials
- Vancomycin AUC/MIC-guided dosing is now standard of care; trough-only monitoring is outdated per 2020 guidelines
- Round vancomycin doses to the nearest 250 mg; do not exceed 4,500 mg/day without infectious disease consultation
- For phenytoin, always correct for albumin before making dose changes; free phenytoin level is gold standard
- Bayesian PK software (DoseMeRx, InsightRX) is preferred over manual calculations when available
- Document all PK calculations in the medical record with assumptions stated
- Reassess renal function daily in acutely ill patients; a stable CrCl today may change tomorrow
