---
name: converting-medication-routes
language: en
description: Calculates IV-to-oral conversions and opioid equianalgesic dosing. Use when converting medication routes, calculating equianalgesic doses, or transitioning IV to oral therapy.
tags:
  - pharmacy
metadata:
  author: casemark
  practice_areas:
    - Clinical Pharmacy
    - Pharmacy
  document_types:
    - Report
  skill_modes:
    - Analysis
---

# Converting Medication Routes

Calculates IV-to-oral conversions and opioid equianalgesic dosing for safe medication route transitions.

## Why This Skill Exists

Intravenous-to-oral (IV-to-PO) conversion is one of the most impactful pharmacist interventions in the inpatient setting. IV medications cost 2-5 times more than their oral equivalents, require nursing time for administration, carry catheter-related infection risk, and may prolong hospital stay. Studies demonstrate that systematic IV-to-PO conversion programs reduce IV antibiotic days by 20-40%, decrease length of stay, and save institutions hundreds of thousands of dollars annually.

However, incorrect conversion carries serious risk. Not all drugs have 1:1 bioavailability (e.g., oral morphine is only 30% bioavailable compared to IV), and some medications require different doses by different routes (e.g., metoprolol IV:PO ratio is 1:2.5). Opioid equianalgesic dosing errors are a leading cause of preventable overdose deaths in hospitals—the ISMP has issued multiple alerts about fatal errors in opioid conversions, particularly involving methadone and fentanyl patches. Pharmacists must apply pharmacokinetic principles, bioavailability data, and conservative dosing strategies (including safety reductions) when converting routes.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. What medication is being converted and what is the current dose, route, and frequency? (Default: specify)
2. What is the target route of administration? (Default: IV to PO unless otherwise specified)
3. Why is the conversion being performed (step-down therapy, discharge, cost savings)? (Default: clinical step-down)
4. Can the patient tolerate oral medications (swallowing, GI function, absorption)? (Default: verify with nursing/clinical team)
5. What is the patient's current pain score or clinical status on the existing regimen? (Default: assess efficacy)
6. Does the patient have renal or hepatic impairment affecting drug metabolism? (Default: check labs)
7. Is this an opioid conversion (equianalgesic calculation required)? (Default: determine)
8. Are there formulation-specific considerations (extended-release, enteric-coated, liquid availability)? (Default: review available dosage forms)

### Documents to Request

- Current medication orders with dose, route, frequency, and duration
- Patient's ability to take oral medications (swallow function, NPO status, GI motility)
- Current symptom control assessment (pain scores, infection markers, vitals)
- Renal function (SCr, CrCl) and hepatic function (LFTs)
- Allergy profile (some oral formulations contain different inactive ingredients)
- Available oral formulations in the institutional formulary
- Discharge planning timeline if conversion is related to transitions of care

---

## Step 1: Assess Conversion Eligibility

The patient must meet ALL of the following for IV-to-PO conversion:

- Able to swallow or receive medications via functioning enteral tube
- GI tract is functional (no ileus, bowel obstruction, severe vomiting, malabsorption)
- Hemodynamically stable (not in shock or requiring vasopressors)
- Afebrile for ≥24 hours (for antibiotic conversions)
- Clinical improvement documented (labs trending appropriately)
- Oral formulation is available for the drug or a therapeutic equivalent
- Drug has adequate oral bioavailability for the indication

**Drugs NOT appropriate for simple IV-to-PO conversion:**
- Amphotericin B (no oral bioavailability for systemic infection)
- Vancomycin (for systemic MRSA infection; oral vancomycin only treats C. diff colitis)
- Aminoglycosides (negligible oral absorption)
- Acyclovir (poor oral bioavailability for serious infections; use valacyclovir as PO alternative)

---

## Step 2: Apply Bioavailability-Based Conversion Ratios

**High Bioavailability (≥80%) — 1:1 Dose Conversion:**

| Drug | IV Dose | PO Dose | Oral Bioavailability |
|---|---|---|---|
| Fluoroquinolones (levofloxacin, moxifloxacin) | 500 mg IV | 500 mg PO | ~99% |
| Metronidazole | 500 mg IV | 500 mg PO | ~100% |
| Fluconazole | 400 mg IV | 400 mg PO | ~90% |
| Linezolid | 600 mg IV | 600 mg PO | ~100% |
| TMP-SMX | 5 mg/kg IV q6h | 1 DS tab PO q12h (equivalent) | ~95% |
| Clindamycin | 600 mg IV q8h | 300-450 mg PO q6-8h | ~90% |
| Doxycycline | 100 mg IV q12h | 100 mg PO q12h | ~93% |
| Voriconazole | 4 mg/kg IV q12h | 200 mg PO q12h | ~96% |

**Moderate Bioavailability — Dose Adjustment Required:**

| Drug | IV Dose | PO Dose | Conversion Notes |
|---|---|---|---|
| Pantoprazole | 40 mg IV q12-24h | 40 mg PO daily | PO adequate for most non-ICU indications |
| Metoprolol | 5 mg IV | 12.5-25 mg PO | IV:PO ratio ~1:2.5 |
| Labetalol | 20 mg IV | 100-200 mg PO | ~25% bioavailability |
| Furosemide | 40 mg IV | 80 mg PO | ~50% oral bioavailability |
| Diazepam | 5 mg IV | 5 mg PO | ~100% but different onset |
| Hydralazine | 10 mg IV | 25-50 mg PO | Variable first-pass metabolism |

---

## Step 3: Opioid Equianalgesic Conversions

**Equianalgesic Dose Table (approximate equivalence to morphine 10 mg IV):**

| Opioid | IV/IM Dose | PO Dose | Conversion Factor (to PO morphine) |
|---|---|---|---|
| Morphine | 10 mg | 30 mg | 1.0 (reference) |
| Hydromorphone | 1.5 mg | 4 mg | PO: 4 mg = 30 mg PO morphine |
| Oxycodone | N/A (no IV in US) | 20 mg | PO: 20 mg = 30 mg PO morphine |
| Hydrocodone | N/A | 30 mg | PO: 30 mg = 30 mg PO morphine |
| Fentanyl | 100 mcg | N/A (transdermal/buccal) | See fentanyl patch conversion |
| Methadone | Variable | Variable | NON-LINEAR — use AMDG conversion |

**Critical safety rules for opioid conversion:**

1. **Calculate total 24-hour opioid consumption** in current route/drug
2. **Convert to oral morphine equivalents (OME)** using equianalgesic table
3. **Apply 25-50% safety reduction** for incomplete cross-tolerance (MANDATORY for any opioid rotation)
4. **Divide into appropriate dosing interval** for the new opioid
5. **Provide breakthrough dosing** at 10-15% of total 24-hour dose q1-2h PRN

**Methadone conversion (AMDG Guidelines):**
Methadone has a non-linear equianalgesic ratio that increases with higher morphine doses:

| Daily Oral Morphine Equivalent | Morphine:Methadone Ratio |
|---|---|
| <60 mg | 4:1 |
| 60-200 mg | 8:1 |
| 200-500 mg | 10:1 |
| 500-1000 mg | 12:1 |
| >1000 mg | 15-20:1 |

**Fentanyl transdermal patch conversion:**
Fentanyl 25 mcg/h patch ≈ 60-90 mg oral morphine/day (use conservative end)
- Do not initiate fentanyl patch in opioid-naive patients
- Patch onset is 12-24 hours; provide short-acting opioid coverage during titration
- Steady state requires 3-6 days; do not increase patch dose more frequently than q72h

---

## Step 4: Implement Conversion and Monitor

1. **Write new oral order** with specific dose, frequency, and PRN parameters
2. **Discontinue IV order** after first oral dose is administered and tolerated
3. **Overlap period for long-acting formulations:** Maintain IV for 12-24 hours after starting long-acting PO opioid or fentanyl patch
4. **Monitor for efficacy:** Reassess symptom control within 4-8 hours of conversion
5. **Monitor for toxicity:** Sedation scale (Pasero Opioid Sedation Scale), respiratory rate, pain scores
6. **Document conversion rationale:** Source drug/dose → equianalgesic calculation → safety reduction → final order

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Has oral tolerability been confirmed (swallowing, GI function, hemodynamic stability)?
2. Was the correct bioavailability ratio applied for the specific drug?
3. For opioid conversions, was the 25-50% cross-tolerance reduction applied?
4. Is breakthrough/PRN dosing provided during the transition period?
5. Is the monitoring plan in place for both efficacy and toxicity post-conversion?

---

## Quality Audit

- [ ] Oral tolerability criteria met before conversion (afebrile, stable, functional GI tract)
- [ ] Bioavailability ratio applied correctly for the drug being converted
- [ ] Dose calculation shown with units and conversion factor documented
- [ ] For 1:1 conversions, oral bioavailability ≥80% confirmed from pharmacokinetic data
- [ ] Opioid equianalgesic table used with appropriate reference source
- [ ] Safety reduction of 25-50% applied for opioid rotations
- [ ] Methadone conversion uses non-linear AMDG ratio tables (not simple equianalgesic)
- [ ] Fentanyl patch not initiated in opioid-naive patients
- [ ] Breakthrough dosing calculated and ordered (10-15% of 24h total)
- [ ] Overlap period defined for long-acting formulations
- [ ] Monitoring plan includes efficacy (symptom scores) and safety (sedation, respiratory rate)
- [ ] Conversion documented with calculation trail in medical record
- [ ] Formulary availability of oral formulation confirmed before conversion order placed

---

## Guidelines

- Always confirm GI function and oral tolerability before any IV-to-PO conversion
- Do not assume 1:1 conversion for all drugs; check drug-specific bioavailability data
- Opioid equianalgesic tables are APPROXIMATIONS; individual patient response varies significantly
- Always apply a 25-50% safety reduction when rotating between opioids due to incomplete cross-tolerance
- Methadone is NOT a simple equianalgesic conversion—its ratio changes with dose, and its long half-life (15-60 hours) creates delayed accumulation risk
- Fentanyl patch calculations should use the conservative end of the conversion range
- Monitor for both inadequate pain control (underdosing) and respiratory depression (overdosing) in the 24-72 hours post-conversion
- Document every conversion with the complete calculation trail: source dose → OME → safety reduction → target dose
