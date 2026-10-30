# Reconciliation Rules: BPMH, Comparison and Discrepancy Vocabulary

Rules for building the best possible medication history (BPMH), comparing it with the list at the transition point, and labeling every row. Sources and dates are in the primary-sources file; anything marked `[VERIFY]` there stays flagged here.

## Contents

1. What counts as a medication
2. BPMH sources and what each one proves
3. BPMH line verification labels
4. Interview prompts for commonly omitted products
5. Comparison pairs by transition point
6. Row status vocabulary
7. Discrepancy types
8. Review priority tiers
9. High-alert medications
10. Look-alike and sound-alike names
11. Formulary substitution, holds and duplication

## 1. What counts as a medication

Use the Joint Commission glossary definition: prescription, sample, herbal remedies, vitamins, nutraceuticals, vaccines and over-the-counter drugs; diagnostic and contrast agents; radioactive medications; respiratory therapy treatments; parenteral nutrition; blood derivatives; IV solutions; and any product the FDA designates as a drug. It excludes enteral nutrition, oxygen and other medical gases. Hospital NPG.14.05.01 EP 1, Note 1: current medications include scheduled and as-needed (PRN) medications.

WHO High 5s adds recreational drugs and non-prescribed products to the BPMH. Record recreational and non-prescribed use when the patient discloses it; it is part of what the patient takes.

## 2. BPMH sources and what each one proves

The BPMH is a snapshot of what the patient actually takes, which may differ from what was prescribed (WHO High 5s SOP, Step 2). Verify with more than one source (WHO High 5s; AHRQ MATCH). Other sources never replace an interview with a patient or family who can take part (WHO; MATCH).

| Source | Proves | Does not prove |
|---|---|---|
| Patient or caregiver interview | What the person says is taken, how, and when last taken | Exact strength or formulation when recalled from memory; doses stated as "about" a number |
| Pill bottles, pens, inhalers, patches brought in | A product was dispensed with a label sig and date | That the patient follows the label (MATCH: a patient may take a drug differently from the label) |
| Pharmacy fill or claims history | A prescription was dispensed or billed on a date | That the patient takes it, at that dose, now; it misses samples, cash fills at other pharmacies, VA or mail-order fills outside the feed, OTC products and auto-refills after a stop |
| Prior discharge list, transfer form or after-visit summary | What a prior team intended on that date | Anything that changed since; it repeats any error it contained |
| Outside MAR (SNF, other hospital) | What was administered there, by date and time | The pre-facility home regimen |
| Prescriber office or clinic note | What the prescriber started, stopped or changed, and why | Whether the patient followed the change |
| Prescription drug monitoring program (PDMP) | Controlled-substance dispensing in that state's database | Use; dispensing in other states unless shared; query mandates vary by state `[VERIFY]` |

## 3. BPMH line verification labels

Label every BPMH line:

- **Confirmed**: two or more independent sources agree on drug, strength, dose, route and frequency. Two printouts of the same fill feed are one source.
- **Single source**: only one source supports the line, including a patient-reported dose not checked against a label, pharmacy or prescriber.
- **Conflicting sources**: sources disagree on any of drug, strength, dose, route, frequency or formulation. Record each source's version; do not choose one.

A home list built from one source type is labeled single source at the list level as well as line by line.

## 4. Interview prompts for commonly omitted products

From AHRQ MATCH Figure 9: ask open and closed questions by condition and by prescriber type; ask about non-oral routes (creams, ointments, patches, eye and ear drops, nebulizers, inhalers); ask about infrequent schedules (weekly, monthly injections); ask what the patient takes for headache, allergies, sleep, colds and heartburn; ask about recent starts, stops and changes; capture strength, formulation (extended release), dose, route, frequency and last dose.

## 5. Comparison pairs by transition point

| Transition | Baseline | Compared with |
|---|---|---|
| Admission | BPMH | Admission medication orders |
| Internal transfer (ICU to floor, service change) | Active orders before transfer, plus the BPMH for home drugs held or not ordered | Orders after transfer |
| External transfer in | BPMH, plus the sending facility's MAR and transfer list (MATCH: three sources) | Orders at the receiving hospital |
| Discharge | BPMH and the active inpatient orders at discharge | Discharge medication list, discharge summary and prescriptions |
| Discharge to next provider | Reconciled discharge list | What the next provider actually receives |

## 6. Row status vocabulary

Use these labels verbatim for each comparison row:

- **Match**: same drug, strength, dose, route, frequency and formulation in both lists.
- **Documented change**: the lists differ and a source states the reason (cite the note, author role and date). A checkbox, an order-set default or the word "intentional" with no reason is not a stated reason.
- **Unexplained discrepancy**: the lists differ, including an omission or an addition, and no source states the reason. Only the prescriber can classify it as intended or unintended.
- **Cannot determine**: the baseline line is Conflicting sources, or a needed source was not supplied; name the missing fact.

WHO High 5s names two categories for the prescriber's classification: undocumented intentional and unintentional. MATCH Table 3 calls a difference without supporting documentation an unintended discrepancy that requires physician follow-up. The skill labels the row Unexplained discrepancy and leaves the classification to the prescriber.

## 7. Discrepancy types

Adapted from MATCH (omission, commission, different dose, route or frequency, different medication) and NPG.14.05.01 EP 3 note (omissions, duplications, contraindications, unclear information, changes):

| Type | Definition |
|---|---|
| Omission | On the baseline, absent from the compared list |
| Commission | On the compared list, not on the baseline and not explained by a new order with a reason |
| Dose, route or frequency | Same drug, different dose, route or frequency |
| Formulation | Same drug, different release form (extended versus immediate release) or strength unit |
| Different drug, same class | Another agent of the class appears without a documented substitution |
| Therapeutic duplication | Two agents with the same action or two products with the same ingredient on one list |
| Held, not resumed | A hold order with a stated resume condition and no later resume or stop |
| Unclear information | Illegible, incomplete or ambiguous entry (no strength, "as directed", unit missing) |
| Document conflict | Two documents for the same transition (discharge list, summary, prescriptions) disagree |

## 8. Review priority tiers

This is the skill's triage convention, not a regulatory scale; facility policy on timing controls.

| Tier | Assign when |
|---|---|
| Critical | Any discrepancy, conflict or single-source line involving a high-alert medication (section 9); duplication of a high-alert drug; a conflict with a documented allergy |
| High | Unexplained discrepancy in a scheduled chronic medication; Conflicting sources on a scheduled medication; held, not resumed (non-high-alert); therapeutic duplication not involving a high-alert drug; a document conflict at discharge |
| Moderate | Omitted OTC, supplement or PRN product; single-source non-high-alert line |
| Low | Brand versus generic naming or sig wording with no change in drug, dose, route or frequency |

## 9. High-alert medications

ISMP List of High-Alert Medications in Acute Care Settings (2024), the classes most often met at transitions: antithrombotic agents (warfarin, low molecular weight and unfractionated heparin, direct oral anticoagulants and factor Xa inhibitors, direct thrombin inhibitors, glycoprotein IIb/IIIa inhibitors, thrombolytics); insulin, subcutaneous and IV (U-500 singled out); opioids by all routes, including transdermal; oral sulfonylurea hypoglycemics; oral and parenteral chemotherapy; oral methotrexate for non-oncologic use; IV inotropes, antiarrhythmics and adrenergic agents; concentrated potassium chloride and hypertonic sodium chloride; neuromuscular blockers. Reconcile each high-alert line individually; never batch-accept it with routine lines.

## 10. Look-alike and sound-alike names

Pairs on the ISMP List of Confused Drug Names (2024) that recur in reconciliation include hydrALAZINE and hydrOXYzine, HumaLOG and HumuLIN, glipiZIDE and glyBURIDE, CeleBREX and CeleXA, HYDROcodone and oxyCODONE. When two sources name members of a listed pair for what may be one product, mark the line Conflicting sources, name the pair, and ask which product the patient receives. Indication, appearance (for insulin, the pen and suspension) and the outside MAR are evidence, not proof.

## 11. Formulary substitution, holds and duplication

- A therapeutic interchange record explains the inpatient order (MATCH lists formulary substitution as an intended discrepancy). It does not explain the discharge list: at discharge, check that the home agent and the substitute are not both listed, and that the discharge list says which one continues.
- A hold order is a Documented change only for the hold. If it states a resume condition (after a procedure, when creatinine recovers), check the MAR and the discharge list for a resume or a documented stop. Absent both, the row is Unexplained discrepancy, type held, not resumed.
- A discharge line that matches an active inpatient order is not a Match when another drug of the same class, or another product with the same ingredient, is also on the discharge list; report the duplication.
- Check combination products for shared ingredients (acetaminophen in opioid combinations and OTC products). Compute the largest daily amount the listed sigs allow and give it to the prescriber; do not set the limit.
