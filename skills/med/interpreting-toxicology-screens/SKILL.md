---
name: interpreting-toxicology-screens
description: Structures drug screen interpretation with confirmation testing and clinical correlation. Use when interpreting drug screens, managing confirmatory testing, or documenting toxicology results.
tags:
  - analysis
  - pathology
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Interpretation Report
  skill_modes:
    - Analysis
    - Interpretation
---

# Interpreting Toxicology Screens

Structures drug screen interpretation with confirmation testing and clinical correlation.

## Why This Skill Exists

Toxicology testing spans clinical emergency management, workplace drug testing, forensic investigation, pain management compliance, and therapeutic drug monitoring. The interpretation of drug screens is fraught with pitfalls: immunoassay cross-reactivity produces false positives (dextromethorphan triggering PCP assays, sertraline triggering benzodiazepine assays), and limited assay panels create false negatives (standard opiate screens do not detect fentanyl, oxycodone, or methadone). Misinterpretation of toxicology results can lead to unjust employment termination, inappropriate psychiatric holds, missed poisoning diagnoses, or opioid prescription violations.

SAMHSA (Substance Abuse and Mental Health Services Administration) Mandatory Guidelines govern federal workplace drug testing programs, requiring specific cutoff concentrations and a Medical Review Officer (MRO) process. CAP accreditation (Toxicology/TDM TOX checklist) requires validated cutoff concentrations, documented confirmation procedures, and quality control per CLIA standards. Forensic toxicology follows SWGTOX (Scientific Working Group for Forensic Toxicology) and SOFT/AAFS guidelines for chain of custody and reporting. This skill ensures systematic and defensible toxicology interpretation across all settings.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Testing context** — Clinical (emergency), workplace (SAMHSA-regulated or non-regulated), forensic (postmortem or DUI), pain management compliance, or therapeutic drug monitoring? Default: clinical emergency.
2. **Specimen type** — Urine, blood/serum, oral fluid, hair, meconium, or other? Default: urine.
3. **Screen method** — Immunoassay (enzyme, CEDIA, EMIT, KIMS), point-of-care cup, or initial definitive (LC-MS/MS)? Default: immunoassay screen.
4. **Confirmation available** — Has confirmatory testing (GC-MS, LC-MS/MS) been performed? Default: pending.
5. **Clinical context** — Presenting symptoms (altered mental status, respiratory depression, seizures, cardiac symptoms), medications, medical history? Default: not provided; flag [VERIFY].
6. **Chain of custody** — Is chain of custody required (workplace, forensic)? Default: no (clinical).
7. **Cutoff concentrations** — Which cutoff thresholds are in use (SAMHSA federal, institutional clinical, pain management)? Default: institutional clinical.

### Documents to Request

- Drug screen results with method and cutoff concentrations
- Confirmatory test results (GC-MS or LC-MS/MS) with quantitative levels
- Patient medication list (prescription and OTC)
- Clinical notes (presenting symptoms, vital signs, physical exam)
- Chain-of-custody form (if applicable)
- Institutional drug testing policy with cutoff tables
- SAMHSA Mandatory Guidelines (if federal workplace testing)
- Prior drug testing results for comparison

---

## Step 1: Immunoassay Screen Interpretation

Interpret the initial screen recognizing the inherent limitations of immunoassay:

### Standard Urine Drug Screen Panels and SAMHSA Cutoffs

| Drug Class | SAMHSA Screen Cutoff | SAMHSA Confirm Cutoff | Common Cross-Reactants/Limitations |
|---|---|---|---|
| Amphetamines | 500 ng/mL | 250 ng/mL (d-amp/meth) | Pseudoephedrine, bupropion, labetalol, ranitidine, phentermine |
| Barbiturates | (clinical only) | Analyte-specific | Phenobarbital immunoassay may not detect short-acting barbiturates |
| Benzodiazepines | (clinical only) | Analyte-specific | Sertraline, efavirenz; oxazepam-based assays miss clonazepam, lorazepam at low levels |
| Cocaine metabolite (BZE) | 150 ng/mL | 100 ng/mL | Very few cross-reactants; high specificity |
| Marijuana (THC-COOH) | 50 ng/mL | 15 ng/mL | CBD products may contain trace THC; hemp exposure unlikely to exceed 50 ng/mL |
| Opiates | 2000 ng/mL | 2000 ng/mL (codeine/morphine) | Standard assay detects morphine, codeine; does NOT reliably detect oxycodone, fentanyl, methadone, buprenorphine |
| PCP | 25 ng/mL | 25 ng/mL | Dextromethorphan, ketamine, diphenhydramine, venlafaxine |
| MDMA | 500 ng/mL | 250 ng/mL | Cross-reactivity with MDA, MDEA |

### Critical Immunoassay Limitations

| What the Standard Screen MISSES | Required Separate Assay |
|---|---|
| Fentanyl and fentanyl analogues | Fentanyl-specific immunoassay or LC-MS/MS |
| Oxycodone/oxymorphone | Oxycodone-specific immunoassay or LC-MS/MS |
| Methadone | Methadone-specific immunoassay |
| Buprenorphine | Buprenorphine-specific immunoassay |
| Gabapentin/pregabalin | LC-MS/MS only |
| Synthetic cannabinoids (K2/Spice) | Specific panel (LC-MS/MS) |
| Designer stimulants (bath salts) | Specific panel (LC-MS/MS) |
| GHB | GHB-specific assay |

---

## Step 2: Confirmation Testing Interpretation

For all presumptive positive screens, confirmatory testing by a different analytical principle is required:

**Confirmation methods:**
- **GC-MS (Gas Chromatography-Mass Spectrometry)**: Gold standard for many drug classes. Identifies specific analyte by retention time and mass spectrum. Quantitative.
- **LC-MS/MS (Liquid Chromatography-Tandem Mass Spectrometry)**: Preferred for polar and thermolabile compounds. Higher throughput. Quantitative.

**Confirmation interpretation rules:**
- A positive screen with a **negative confirmation** = **NEGATIVE** (the screen was a false positive due to cross-reactivity)
- A positive screen with a **positive confirmation** = **CONFIRMED POSITIVE** (specific analyte identified)
- A negative screen with clinical suspicion = Consider ordering specific confirmatory testing; immunoassays have limited scope
- Report confirmed results with the specific analyte identified (e.g., "oxycodone confirmed" not just "opiate positive")

---

## Step 3: Clinical Correlation and Pharmacokinetic Context

Interpret confirmed results in the context of clinical presentation and pharmacokinetics:

**Detection windows (urine, approximate):**

| Substance | Detection After Single Use | Detection After Chronic Use |
|---|---|---|
| Amphetamine/methamphetamine | 1-3 days | 3-7 days |
| Cocaine (benzoylecgonine) | 2-4 days | Up to 14 days (heavy use) |
| Marijuana (THC-COOH) | 3-5 days (single) | Up to 30+ days (chronic, heavy) |
| Opiates (morphine, codeine) | 1-3 days | 3-5 days |
| Fentanyl | 1-3 days | 3-7 days |
| Benzodiazepines (short-acting) | 1-3 days | 5-7 days |
| Benzodiazepines (long-acting) | 5-7 days | Up to 30 days |
| PCP | 3-7 days | Up to 30 days |
| Methadone | 2-4 days | Up to 14 days |
| Buprenorphine | 2-6 days | Up to 11 days |

**Metabolic relationships critical for interpretation:**
- Codeine is metabolized to morphine; presence of both is expected after codeine use
- Heroin (6-MAM) is metabolized to morphine; 6-MAM detection (short window, < 8 hours) confirms heroin
- Hydrocodone can be a minor metabolite of codeine (CYP2D6-dependent)
- Oxycodone is metabolized to oxymorphone; presence of both is expected

---

## Step 4: Context-Specific Reporting

Tailor the report and interpretation to the testing context:

### Clinical Emergency Setting
- Report all positive results with clinical significance statement.
- Flag unexpected findings (e.g., fentanyl positive in a patient presenting with opioid overdose).
- Correlate with serum levels for therapeutic drug monitoring (acetaminophen, salicylate, ethanol, lithium, digoxin, anticonvulsants).

### Workplace/Forensic Setting (SAMHSA-Regulated)
- All results reviewed by a certified Medical Review Officer (MRO) before reporting.
- MRO interviews the donor for legitimate medical explanations (valid prescription).
- Apply SAMHSA cutoff concentrations (not clinical cutoffs).
- Maintain chain of custody documentation throughout.
- Report as: Negative, Positive (with specific analyte), Substituted, Invalid, or Rejected for Testing.

### Pain Management Compliance
- Expected positives: Prescribed medications should be detected (absence may indicate diversion).
- Unexpected positives: Non-prescribed substances detected (indicates undisclosed use).
- Expected negatives: Non-prescribed substances should be absent.
- Report quantitative levels when available for consistency assessment (are levels consistent with prescribed dose?).

---

## Step 5: Report Construction

Structure the toxicology interpretation:

1. **Specimen information**: Type, collection date/time, chain of custody status.
2. **Screen results**: Each drug class tested with result (positive/negative) and cutoff used.
3. **Confirmation results**: Specific analytes confirmed with quantitative values and method.
4. **Cross-reactivity assessment**: For any positive screen that was not confirmed, explain the likely cross-reactant.
5. **Clinical interpretation**: Correlate results with medications, symptoms, and detection windows.
6. **Limitations**: State what the screen does NOT detect (fentanyl, synthetic opioids, etc.).
7. **Recommendations**: Suggest additional testing if clinical picture is unexplained by results.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are all presumptive positive screens confirmed by a secondary method (GC-MS or LC-MS/MS)?
2. Are immunoassay cross-reactivity limitations explicitly addressed for each positive class?
3. Is the specific confirmed analyte reported (not just the drug class)?
4. Are detection windows and metabolic relationships considered in the interpretation?
5. Are testing cutoffs appropriate for the context (SAMHSA for federal workplace, clinical for ED)?

---

## Quality Audit

- [ ] Immunoassay screen performed with documented cutoff concentrations
- [ ] All presumptive positives confirmed by a secondary analytical method
- [ ] Cross-reactivity sources identified for false-positive screens
- [ ] Specific analyte reported on confirmation (not drug class alone)
- [ ] Detection windows considered in interpreting positive and negative results
- [ ] Metabolic relationships addressed (codeine/morphine, heroin/6-MAM, hydrocodone)
- [ ] Standard immunoassay limitations stated (fentanyl, oxycodone, synthetics not detected)
- [ ] Chain of custody maintained for forensic/workplace specimens
- [ ] MRO review documented for SAMHSA-regulated testing
- [ ] SAMHSA cutoffs applied for federal workplace testing (not clinical cutoffs)
- [ ] QC materials run with each batch per CLIA/CAP requirements
- [ ] Clinical correlation provided for emergency toxicology cases
- [ ] Limitations section included in every report

---

## Guidelines

- Always confirm presumptive positive immunoassay results with GC-MS or LC-MS/MS before taking clinical, employment, or legal action based on drug testing
- Recognize that standard urine drug screen panels do NOT detect fentanyl, oxycodone, buprenorphine, methadone, or synthetic cannabinoids; order specific assays when these are clinically relevant
- Never report a drug screen result as "positive for opiates" — specify the confirmed analyte (morphine, codeine, 6-MAM, hydromorphone, etc.) since clinical and legal implications differ dramatically
- Be aware of common cross-reactants: dextromethorphan can trigger PCP assays, pseudoephedrine can trigger amphetamine assays, and sertraline can trigger benzodiazepine assays
- For pain management compliance, an unexpected NEGATIVE for a prescribed medication may be more significant than an unexpected positive — it may indicate non-compliance or diversion
- Apply SAMHSA Mandatory Guidelines cutoffs only for federally regulated workplace testing; clinical and forensic testing may use different, often lower, cutoff concentrations
- Document the detection window limitations in every report; a negative screen does not mean a substance was never used, only that it was not detected above the cutoff at the time of collection
- For postmortem toxicology, account for postmortem redistribution (drug levels in cardiac blood may be 2-5x higher than antemortem levels due to tissue release)
