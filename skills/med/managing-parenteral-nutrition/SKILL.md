---
name: managing-parenteral-nutrition
description: Structures TPN order review with macronutrient calculations, compatibility checks, and monitoring protocols. Use when reviewing TPN orders, calculating nutrition requirements, or managing parenteral feeding.
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

# Managing Parenteral Nutrition

Structures TPN order review with macronutrient calculations, compatibility checks, electrolyte management, and metabolic monitoring protocols.

## Why This Skill Exists

Parenteral nutrition (PN) is a complex, high-alert therapy that provides macronutrients, electrolytes, vitamins, and trace elements directly into the bloodstream for patients unable to meet nutritional needs enterally. ISMP classifies parenteral nutrition as a high-alert medication due to the risk of compounding errors, electrolyte imbalances, infectious complications (catheter-related bloodstream infections), and metabolic derangements (refeeding syndrome, hyperglycemia, hepatic steatosis).

ASPEN (American Society for Parenteral and Enteral Nutrition) guidelines require pharmacist involvement in PN order review, compatibility assessment, and metabolic monitoring. Errors in PN formulation—excessive dextrose concentration causing osmolarity-related phlebitis through peripheral lines, calcium-phosphate precipitation causing fatal pulmonary emboli, or zinc deficiency from omitted trace elements—have caused patient deaths. The pharmacist's role encompasses caloric requirement calculation, macronutrient distribution, electrolyte balancing, compatibility verification, stability assessment, and monitoring for metabolic complications. This is one of the most calculation-intensive and clinically consequential pharmacy services.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the indication for PN (bowel obstruction, short bowel syndrome, severe pancreatitis, post-surgical ileus)? (Default: document indication)
2. Is enteral nutrition completely impossible, or is this supplemental PN? (Default: confirm EN trial attempted per ASPEN)
3. What is the patient's current weight (actual), height, and BMI? (Default: use measured values)
4. What is the patient's estimated caloric and protein requirement? (Default: 25-30 kcal/kg/day, 1.2-2.0 g protein/kg/day)
5. What venous access is available (central line vs. peripheral)? (Default: central for >900 mOsm/L or >14 days)
6. What are current electrolyte values (Na, K, Mg, Phos, Ca, CO2)? (Default: request comprehensive metabolic panel)
7. Is the patient at risk for refeeding syndrome (malnourished, NPO >7 days, BMI <18.5, alcoholism)? (Default: screen risk factors)
8. What is the patient's glucose control status? (Default: review recent blood glucose values and insulin orders)

### Documents to Request

- Current labs: BMP, Mg, Phos, prealbumin/albumin, triglycerides, LFTs, CBC
- Current weight (measured) and height
- Fluid balance records (intake/output)
- Current IV fluid orders (to account for additional fluid and electrolytes)
- Insulin orders and blood glucose monitoring results
- Central line placement confirmation and tip position
- Prior PN orders if transitioning from another formulation
- Dietary/nutrition consult with caloric goal documentation

---

## Step 1: Calculate Macronutrient Requirements

**Caloric goals (ASPEN/SCCM guidelines):**
- Non-critically ill: 25-30 kcal/kg/day (use actual body weight; use IBW if BMI >30)
- Critically ill: 12-25 kcal/kg/day (permissive underfeeding in early critical illness, days 1-7)
- Obese (BMI >30): 11-14 kcal/kg actual body weight OR 22-25 kcal/kg IBW

**Protein goals:**
- General adult: 1.2-1.5 g/kg/day
- Critical illness/trauma/burns: 1.5-2.0 g/kg/day
- Hepatic encephalopathy: Do NOT restrict protein (outdated practice); maintain 1.0-1.5 g/kg/day
- Renal failure (non-dialysis): 0.6-0.8 g/kg/day; on dialysis: 1.2-1.5 g/kg/day

**Macronutrient distribution:**

| Component | Caloric Density | Typical Provision | Maximum Rate |
|---|---|---|---|
| Dextrose | 3.4 kcal/g | 50-70% of non-protein calories | GIR ≤5 mg/kg/min (adults) |
| Amino acids | 4.0 kcal/g | Per protein goal | As calculated |
| Lipids (IVFE 20%) | 2.0 kcal/mL | 20-30% of total calories | ≤2.5 g/kg/day; infuse over ≥8-12h |

**Glucose infusion rate (GIR):**
GIR (mg/kg/min) = [Dextrose(g) × 1000] / [weight(kg) × 1440 min/day]
- Target: ≤4-5 mg/kg/min to prevent hyperglycemia and hepatic steatosis

---

## Step 2: Electrolyte and Micronutrient Formulation

**Standard adult daily electrolyte ranges in PN:**

| Electrolyte | Usual Daily Range | Monitoring Trigger |
|---|---|---|
| Sodium | 1-2 mEq/kg | Adjust for fluid status; hypo/hypernatremia |
| Potassium | 1-2 mEq/kg | Check daily; replace aggressively if low |
| Calcium (gluconate) | 10-15 mEq | Monitor ionized calcium; precipitation risk with phosphate |
| Magnesium | 8-20 mEq | Replace before potassium correction |
| Phosphate | 20-40 mmol | Critical for refeeding syndrome prevention |
| Acetate/Chloride | Adjust for acid-base | Increase acetate for metabolic acidosis; chloride for alkalosis |

**Additives:**
- MVI (adult multivitamin for injection): 10 mL daily
- Trace elements (zinc, copper, manganese, chromium, selenium): per standard formulation
- Thiamine 100 mg IV × 3 days before PN initiation in refeeding risk patients
- Vitamin K 10 mg SC/IM weekly (not added to PN due to stability concerns)

---

## Step 3: Compatibility and Stability Assessment

**Critical compatibility checks:**

1. **Calcium-phosphate solubility:** The most dangerous incompatibility. Precipitation of calcium phosphate can cause fatal pulmonary emboli.
   - Use calcium gluconate (not chloride) in PN
   - Apply institution-specific solubility curves based on amino acid concentration, pH, and temperature
   - Calcium and phosphate inversely related: higher amino acid concentration allows more of both
   - Final calcium × phosphate product should not exceed established limits (varies by amino acid brand)

2. **Lipid emulsion stability (3-in-1 admixtures):**
   - Final dextrose concentration should not exceed 23% (destabilizes lipid emulsion)
   - Monovalent cation concentration ≤150 mEq/L, divalent ≤20 mEq/L
   - pH should remain >5.0; low pH cracks lipid emulsion
   - Visual inspection for creaming, oiling out, or particulate matter

3. **Y-site compatibility:** If lipids run separately (2-in-1 system), verify Y-site compatibility of all piggybacked medications

**Osmolarity calculation:**
Osmolarity (mOsm/L) ≈ [Dextrose(g) × 5] + [Amino acids(g) × 10] + [Electrolytes(mEq) × 2] per liter
- Peripheral PN: ≤900 mOsm/L (risk of phlebitis above this threshold)
- Central PN: no osmolarity limit (central veins tolerate hyperosmolar solutions)

---

## Step 4: Monitoring Protocol

| Parameter | Frequency (Initiation) | Frequency (Stable) | Action Threshold |
|---|---|---|---|
| Blood glucose | q6h | Daily or per insulin protocol | >180 mg/dL: insulin; >300: hold PN, reassess |
| BMP (Na, K, Cl, CO2, BUN, Cr) | Daily | 2-3× weekly | Adjust PN electrolytes accordingly |
| Magnesium, Phosphorus | Daily | 2-3× weekly | Replace aggressively in refeeding |
| Triglycerides | Baseline + 24-48h after lipid initiation | Weekly | >400: reduce lipid; >500: hold lipid |
| LFTs (AST, ALT, ALP, bilirubin) | Baseline | Weekly | Rising trend: evaluate PN-associated liver disease |
| Prealbumin | Baseline | Weekly | Marker of visceral protein status (t½ = 2 days) |
| Fluid balance (I&O) | Daily | Daily | Adjust PN volume for fluid overload/deficit |
| Weight | Daily | Daily | Rapid gain suggests fluid retention, not nutrition |

**Refeeding syndrome prevention:**
- Start at 50% of caloric goal and advance over 3-5 days
- Supplement thiamine 100 mg IV daily × 3 days before or concurrent with PN initiation
- Aggressively replace phosphorus, potassium, and magnesium before and during PN
- Monitor electrolytes q6-12h for first 72 hours in high-risk patients

---

## Step 5: Transitioning and Discontinuation

- Begin enteral nutrition trial as soon as clinically feasible (PN is a bridge, not a destination)
- Taper PN as enteral intake increases: reduce PN by 50% when EN provides >50% of caloric goal
- Discontinue PN when EN provides ≥60-75% of caloric requirements
- Taper dextrose-containing PN (do not stop abruptly) to prevent rebound hypoglycemia
- Monitor blood glucose q1-2h for 6-12 hours after PN discontinuation
- Document final PN day, reason for discontinuation, and transition plan

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Has caloric goal been calculated using appropriate weight and ASPEN guideline targets?
2. Is the glucose infusion rate within acceptable limits (≤5 mg/kg/min)?
3. Has calcium-phosphate solubility been verified against the amino acid product curve?
4. Is the monitoring plan specific with parameters and frequencies for refeeding risk?
5. Has a transition-to-enteral plan been documented?

---

## Quality Audit

- [ ] Indication for PN is documented and enteral nutrition trial was attempted or contraindicated
- [ ] Caloric and protein goals are calculated and documented per ASPEN guidelines
- [ ] Glucose infusion rate calculated and within ≤5 mg/kg/min
- [ ] Lipid dose does not exceed 2.5 g/kg/day and triglycerides are monitored
- [ ] Calcium-phosphate compatibility verified using institution-specific solubility curves
- [ ] Osmolarity calculated and route-appropriate (peripheral ≤900 mOsm/L)
- [ ] Refeeding risk assessed and prevention protocol initiated if high risk
- [ ] Thiamine supplemented before or concurrent with PN in malnourished patients
- [ ] Electrolyte monitoring plan specified with frequencies
- [ ] Blood glucose monitoring and insulin protocol in place
- [ ] MVI and trace elements included in daily PN formulation
- [ ] PN labeled with complete component listing, rate, and beyond-use dating
- [ ] Transition plan to enteral nutrition documented with criteria for PN discontinuation
- [ ] PN prepared under aseptic conditions with USP <797> compliance

---

## Guidelines

- Always attempt enteral nutrition before parenteral nutrition; "if the gut works, use it" (ASPEN principle)
- Never exceed calcium-phosphate solubility limits—precipitation has caused patient deaths
- Start PN at 50% goal in malnourished patients and advance over 3-5 days to prevent refeeding syndrome
- Monitor triglycerides before and after lipid initiation; hold lipids if triglycerides >500 mg/dL
- Peripheral PN is limited to ≤900 mOsm/L and typically cannot meet full caloric requirements
- Do not restrict protein in hepatic encephalopathy—this practice is outdated and harmful
- Taper PN gradually (50% for 1-2 hours then discontinue) to prevent rebound hypoglycemia
- Review PN orders daily; nutritional needs change and static orders lead to metabolic complications
