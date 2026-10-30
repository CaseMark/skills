# Clinical Definitions and Surviving Sepsis Campaign Standards

Clinical frameworks that are often confused with SEP-1. Use this file to label which framework a document, alert or note is applying, and to write the clinical guideline overlay. Guideline statements are population recommendations with a strength and a year; never restate one as an order for a patient.

## Contents

1. Framework comparison
2. Sepsis-3 definitions
3. SOFA and SOFA-2
4. Screening tools
5. SSC Hour-1 Bundle (2018)
6. SSC adult guidelines 2026: statements that touch bundle elements
7. Clinical context to keep with the record

## 1. Framework comparison

| Question | CMS SEP-1 (v5.18a, 2026 discharges) | SSC Hour-1 Bundle (2018) | Sepsis-3 (2016) |
|---|---|---|---|
| What it is | Chart-abstracted process measure; all-or-none | Quality-improvement bundle | Clinical definition |
| Sepsis identified by | Infection plus 2 or more SIRS plus 1 or more organ dysfunction within 6 hours, or provider documentation of severe sepsis | Clinical recognition of sepsis or septic shock | Suspected infection plus acute rise in SOFA of 2 or more |
| Shock identified by | Initial lactate 4 or more, persistent hypotension after 30 mL/kg, or provider documentation | Hypotension or lactate 4 or more triggers fluids | Vasopressor needed for MAP 65 or more and lactate over 2 despite adequate volume |
| Time zero | Severe sepsis presentation time (Section 3 of the SEP-1 rules file) | ED triage time, or earliest chart annotation consistent with all elements if not from the ED | None defined |
| Antibiotic timing | Within 3 hours of presentation | Begin within the hour | None defined |
| Fluids | 30 mL/kg crystalloid started within 3 hours of the earlier of initial hypotension and septic shock presentation | Begin rapid 30 mL/kg for hypotension or lactate 4 or more | None defined |

A case can pass SEP-1 and miss the hour-1 bundle, or meet Sepsis-3 and never enter the SEP-1 denominator. Report each framework separately.

## 2. Sepsis-3 definitions

Singer et al., JAMA 2016;315(8):801-810.

- Sepsis: life-threatening organ dysfunction caused by a dysregulated host response to infection. Organ dysfunction is represented clinically by an acute change in total SOFA score of 2 points or more consequent to the infection; baseline is assumed to be zero without known pre-existing dysfunction.
- Septic shock: vasopressor requirement to maintain MAP of 65 mm Hg or more and serum lactate over 2 mmol/L in the absence of hypovolemia.
- "Severe sepsis" is retired in Sepsis-3 but remains a SEP-1 and ICD-10-CM term (R65.20 severe sepsis without septic shock; R65.21 severe sepsis with septic shock; code the underlying systemic infection first).

## 3. SOFA and SOFA-2

Original SOFA, as tabulated in Sepsis-3 (points 0 to 4):

| Organ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Respiration, PaO2/FiO2 mm Hg | 400 or more | under 400 | under 300 | under 200 with respiratory support | under 100 with respiratory support |
| Coagulation, platelets x10^3/uL | 150 or more | under 150 | under 100 | under 50 | under 20 |
| Liver, bilirubin mg/dL | under 1.2 | 1.2-1.9 | 2.0-5.9 | 6.0-11.9 | over 12.0 |
| Cardiovascular | MAP 70 or more | MAP under 70 | dopamine 5 or less or any dobutamine | dopamine over 5, or epinephrine or norepinephrine 0.1 or less | dopamine over 15, or epinephrine or norepinephrine over 0.1 |
| CNS, Glasgow Coma Scale | 15 | 13-14 | 10-12 | 6-9 | under 6 |
| Renal, creatinine mg/dL or urine output | under 1.2 | 1.2-1.9 | 2.0-3.4 | 3.5-4.9 or under 500 mL/day | over 5.0 or under 200 mL/day |

Catecholamine doses in mcg/kg/min given for at least 1 hour.

SOFA-2 (JAMA, published online October 29, 2025; corrected January 29, 2026) revises the score, keeps six organ systems and renames some (brain, kidney). A note that says "SOFA" without the version is ambiguous after late 2025; record which version was used. Whether Sepsis-3 or SSC 2026 adopted SOFA-2 for the definition is `[VERIFY]`.

SOFA points never establish SEP-1 severe sepsis: SEP-1 has its own organ dysfunction thresholds (for example platelets under 100,000 and creatinine over 2.0), and GCS is not one of them.

## 4. Screening tools

- qSOFA (Sepsis-3): respiratory rate 22 or more, altered mentation, systolic BP 100 or less; 2 or more flags higher risk of poor outcome. It is a prognostic flag, not a diagnosis.
- SSC 2026 recommends against qSOFA as a single screening tool compared with SIRS, NEWS, NEWS2 or MEWS, because of poor sensitivity.
- An EHR sepsis alert is a screening event. Its fire time is not SEP-1 time zero and not Sepsis-3 onset.

## 5. SSC Hour-1 Bundle (2018)

Levy, Evans, Rhodes. The Surviving Sepsis Campaign Bundle: 2018 Update. Crit Care Med 2018;46(6):997-1000. Combined the earlier 3-hour and 6-hour bundles. Elements to begin within the hour (completion within the hour is not required):

1. Measure lactate; remeasure if the initial lactate is over 2 mmol/L.
2. Obtain blood cultures before antibiotics.
3. Administer broad-spectrum antibiotics.
4. Begin rapid administration of 30 mL/kg crystalloid for hypotension or lactate of 4 mmol/L or more.
5. Apply vasopressors if hypotensive during or after fluid resuscitation to maintain MAP of 65 mm Hg or more.

Time zero: triage time in the ED, or, for patients not presenting through the ED, the earliest chart annotation consistent with all elements of sepsis or septic shock.

## 6. SSC adult guidelines 2026: statements that touch bundle elements

Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2026, published March 23, 2026 in Critical Care Medicine (doi 10.1097/CCM.0000000000007075), with a companion publication in Intensive Care Medicine. 129 statements; replaces the 2021 edition. Statements below were confirmed from the SCCM guideline page and journal excerpts; quote the full text for exact wording.

| Topic | 2026 statement (strength) |
|---|---|
| Antimicrobials, possible, probable or definite septic shock | Administer immediately, ideally within 1 hour of recognition (recommend) |
| Antimicrobials, possible sepsis without shock | Time-limited rapid investigation; if concern persists, antimicrobials within 3 hours of first recognition (suggest) |
| Antimicrobials, probable or definite sepsis without shock | Administer immediately, ideally within 1 hour of recognition (recommend; unchanged from 2021 apart from wording) |
| Initial fluids | At least 30 mL/kg IV crystalloid in the first 3 hours for sepsis-induced hypoperfusion or septic shock (suggest) |
| Fluid type | Balanced crystalloids over 0.9 percent saline for initial resuscitation |
| Lactate | Serial lactate to guide resuscitation with elevated lactate or septic shock (suggest) |
| Capillary refill time | Adjunct to other perfusion measures (suggest) |
| Vasopressors | Norepinephrine first line over vasopressin or angiotensin II (suggest); add vasopressin on escalating norepinephrine (suggest); against terlipressin |
| MAP target | 65 mm Hg initial target; a 60-65 range for adults 65 or older reported in summaries `[VERIFY]` |
| Corticosteroids | IV corticosteroids for septic shock (suggest); agent, dose and start threshold `[VERIFY]` |
| Screening | Against qSOFA as a single screening tool |

## 7. Clinical context to keep with the record

- Cultures before antibiotics should not meaningfully delay antibiotics; when they are deferred, the reason belongs in the record.
- Heart failure or end-stage kidney disease may justify a smaller fluid volume; the clinical rationale and the volume ordered belong in a provider note in the window.
- Lactate is not specific to hypoperfusion: beta-agonists, epinephrine, liver failure and seizure raise it. Interpret it in context; SEP-1 still counts the number.
- Antibiotic choice, de-escalation and duration are stewardship questions; route them, do not score them here.
