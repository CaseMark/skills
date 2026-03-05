---
name: assessing-drug-interactions
description: Identifies clinically significant drug-drug, drug-food, and drug-disease interactions with severity grading and management recommendations. Use when checking drug interactions, evaluating polypharmacy risks, or managing medication combinations.
tags:
  - assessment
  - pharmacy
  - risk
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Clinical Pharmacy
    - Pharmacy
  document_types:
    - Assessment Report
  skill_modes:
    - Assessment
---

# Assessing Drug Interactions

Identifies clinically significant drug-drug, drug-food, and drug-disease interactions with severity grading and management recommendations.

## Why This Skill Exists

Drug interactions account for approximately 3-5% of all in-hospital medication errors and are a leading cause of preventable adverse drug events. The clinical consequences range from therapeutic failure (e.g., reduced efficacy of oral contraceptives with rifampin) to life-threatening toxicity (e.g., serotonin syndrome from SSRI-MAOI combinations, QT prolongation from concurrent QTc-prolonging agents). Polypharmacy patients—particularly elderly individuals on 5+ medications—face exponentially increasing interaction risk.

Pharmacists are the final safety net before a drug reaches the patient. Robust interaction assessment requires knowledge of cytochrome P450 enzyme systems (CYP3A4, CYP2D6, CYP2C19, CYP1A2), P-glycoprotein transport, renal tubular secretion competition, and pharmacodynamic synergism/antagonism. Regulatory bodies including the Joint Commission (NPSG.03.05.01) and CMS Conditions of Participation mandate prospective drug utilization review for every dispensed prescription. Failure to identify a clinically significant interaction constitutes a deviation from the standard of care and carries malpractice liability.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What is the complete active medication list, including OTC, herbals, and supplements? (Default: request MAR or pharmacy profile)
2. What is the patient's age, sex, weight, and relevant organ function (hepatic/renal)? (Default: assume normal organ function if unspecified, flag as [VERIFY])
3. What is the clinical indication for each medication under review? (Default: pull from problem list)
4. Is there a specific new medication being added, or is this a comprehensive polypharmacy review? (Default: comprehensive)
5. What interaction databases are available? (Default: Lexicomp, Clinical Pharmacology, Micromedex)
6. Are there known patient-specific sensitivities or prior ADR history? (Default: none documented)
7. What is the care setting—inpatient, outpatient, or transitions of care? (Default: inpatient)
8. Is pharmacogenomic data available (CYP2D6, CYP2C19 phenotype)? (Default: not available)

### Documents to Request

- Current medication administration record (MAR) or e-prescribing profile
- Recent lab values: INR, serum drug levels, LFTs, SCr/BUN, electrolytes (K+, Mg2+, QTc if relevant)
- Pharmacogenomic panel results if available
- Allergy and ADR history
- Problem list with active diagnoses
- Recent ECG if QTc-prolonging agents are involved

---

## Step 1: Catalog All Active Substances

List every active pharmaceutical ingredient the patient is receiving. Include:

- Prescription medications with dose, route, frequency
- OTC medications (NSAIDs, antihistamines, PPIs)
- Herbal/dietary supplements (St. John's wort, grapefruit, ginkgo)
- PRN medications and recent as-needed use dates

Assign each substance its primary metabolic pathway:

| CYP Enzyme | Common Substrates | Common Inhibitors | Common Inducers |
|---|---|---|---|
| CYP3A4 | Simvastatin, cyclosporine, midazolam | Ketoconazole, clarithromycin, ritonavir | Rifampin, phenytoin, carbamazepine |
| CYP2D6 | Codeine, metoprolol, fluoxetine | Paroxetine, fluoxetine, bupropion | Not significantly inducible |
| CYP2C19 | Clopidogrel, omeprazole, voriconazole | Fluconazole, fluvoxamine, omeprazole | Rifampin, St. John's wort |
| CYP2C9 | Warfarin, phenytoin, losartan | Fluconazole, amiodarone, metronidazole | Rifampin |
| CYP1A2 | Theophylline, clozapine, caffeine | Fluvoxamine, ciprofloxacin | Smoking, omeprazole (minor) |

---

## Step 2: Screen and Classify Interactions

Run each combination through at least two independent drug interaction databases. Classify each identified interaction:

**Severity Grading (use Lexicomp/Micromedex concordance):**
- **Contraindicated (X):** Combination must not be used. Examples: linezolid + serotonergic agents, simvastatin + itraconazole
- **Major (D):** Modify therapy; combination may cause serious harm. Examples: warfarin + fluconazole, methotrexate + trimethoprim
- **Moderate (C):** Monitor therapy; adjust dose or timing as needed. Examples: ACE inhibitors + potassium supplements, digoxin + amiodarone
- **Minor (B):** No action needed for most patients. Examples: antacids + iron timing

**Mechanism Classification:**
- Pharmacokinetic: absorption, distribution, metabolism (CYP inhibition/induction), elimination
- Pharmacodynamic: additive, synergistic, or antagonistic effects at receptor/organ level
- Mixed: both PK and PD components

---

## Step 3: Evaluate Clinical Significance

Not all flagged interactions require intervention. Assess clinical significance by:

1. **Therapeutic index:** Narrow therapeutic index drugs (warfarin, digoxin, lithium, phenytoin, theophylline, aminoglycosides) demand higher vigilance
2. **Onset timing:** Immediate (within 24 hours) vs. delayed (days to weeks, e.g., enzyme induction)
3. **Dose-dependency:** Some interactions only manifest at higher doses (e.g., QTc prolongation)
4. **Patient vulnerability:** Age >65, hepatic/renal impairment, genetic polymorphisms increase risk
5. **Duration of co-administration:** Short-term concurrent use may not reach steady-state interaction
6. **Evidence quality:** Case reports vs. controlled studies vs. mechanistic extrapolation

---

## Step 4: Formulate Management Recommendations

For each clinically significant interaction, provide one of:

- **Avoid combination:** Recommend specific therapeutic alternative
- **Dose adjustment:** Specify percentage reduction or new target dose
- **Enhanced monitoring:** Define parameters (lab values, vital signs, symptoms) and frequency
- **Timing separation:** Specify administration interval (e.g., fluoroquinolones and cations separated by 2 hours)
- **Patient counseling points:** Symptoms to watch for and when to seek care

Document the supporting evidence level for each recommendation (clinical guideline, pharmacokinetic study, case series, or mechanistic rationale).

---

## Step 5: Generate Interaction Assessment Report

Structure the final output as:

1. **Patient identifier and date of review**
2. **Interaction summary table:** Drug pair | Severity | Mechanism | Recommendation | Evidence level
3. **Detailed narrative for each Major/Contraindicated interaction**
4. **Monitoring plan with timeline**
5. **Medications cleared with no significant interactions**
6. **Pharmacist attestation and limitations statement**

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Were all active medications including OTC/herbals accounted for in the screen?
2. Do severity ratings from the two databases agree, and were discrepancies resolved?
3. Has each Major or Contraindicated interaction received a specific management recommendation?
4. Are monitoring parameters clearly defined with lab/timing specifics?
5. Have narrow therapeutic index drugs been individually addressed regardless of screen results?

---

## Quality Audit

- [ ] Complete medication list was obtained and documented
- [ ] At least two independent interaction databases were queried
- [ ] Each interaction is classified by severity (X, D, C, B) and mechanism (PK, PD, mixed)
- [ ] Contraindicated combinations have clear stop-or-substitute directives
- [ ] Narrow therapeutic index drugs were individually reviewed
- [ ] CYP enzyme pathways are cited for pharmacokinetic interactions
- [ ] Pharmacogenomic status is addressed if data available
- [ ] Monitoring parameters include specific lab values, intervals, and escalation triggers
- [ ] Timing-sensitive interactions include administration scheduling guidance
- [ ] Patient-specific risk factors (age, organ function) are factored into significance assessment
- [ ] Evidence level is cited for each recommendation
- [ ] Report includes limitations and [VERIFY] flags for missing data
- [ ] QTc-prolonging combinations are flagged with ECG monitoring recommendation

---

## Guidelines

- Always screen against at least two interaction databases to reduce false negatives
- Classify by mechanism (PK vs. PD) before grading severity—mechanism informs management
- Prioritize narrow therapeutic index drugs for detailed review regardless of initial screen
- Never dismiss a contraindicated (X-rated) interaction without prescriber communication and documentation
- Include OTC and herbal products; St. John's wort is a potent CYP3A4/P-gp inducer often missed
- Factor in pharmacogenomic status when available—CYP2D6 poor metabolizers face amplified inhibition interactions
- Document clinical rationale when accepting a moderate interaction with monitoring rather than avoidance
- Time-stamp all assessments; interaction profiles change when medications are added or discontinued
