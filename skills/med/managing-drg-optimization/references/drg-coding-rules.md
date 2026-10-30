# DRG Coding Rules

Rules for validating an MS-DRG assignment on one inpatient claim. Each rule names its authority and the place it was read; `references/primary-sources.md` gives the URL and date. Coding Clinic is paywalled and was not read; where a Coding Clinic answer would decide a case, mark it `[VERIFY]`.

## Contents

1. Version lock and FY 2027 changes
2. Principal diagnosis (Section II and UHDDS)
3. Secondary diagnoses (Section III) and who may document them
4. CC, MCC and the CC exclusion list
5. DRG families confirmed in Grouper V44
6. Sepsis coding and payer sepsis definitions
7. POA indicators and the HAC payment provision
8. Inpatient status, payer basis and transfers
9. Inpatient versus outpatient guideline sections

## 1. Version lock and FY 2027 changes

- Select the grouper by discharge date. ICD-10 MS-DRG Grouper and Medicare Code Editor Version 44 apply to discharges on or after October 1, 2026 (MLN MM14592; V44 errata). Version 43 applied to FY 2026 discharges. The ICD-10-CM Official Guidelines FY 2027 apply to October 1, 2026 through September 30, 2027.
- FY 2027 IPPS/LTCH PPS final rule (CMS-1849-F, 91 FR 49570, Aug. 4, 2026; effective Oct. 1, 2026): 768 MS-DRGs (18 deleted, 14 created; MM14592; 91 FR 49919). Examples: MS-DRGs 466-468 and 485-487 deleted (91 FR 49620); 258-262 deleted and 210-211 created (91 FR 49595); 736-741 deleted and 731-733 created (91 FR 49635).
- Severity changes finalized for FY 2027: ten housing codes (Z59.00, Z59.01, Z59.02, Z59.10, Z59.11, Z59.12, Z59.19, Z59.811, Z59.812, Z59.819) moved from CC to NonCC (91 FR 49648; Table 6J.2). The V44 Appendix C CC list, read in full for the Z codes, lists no Z59 code.
- Requests to change severity that CMS declined: R53.2 functional quadriplegia stays an MCC; E40, E41, E42 and E43 stay MCCs; P01.7 and P03.0 stay NonCC; O63.0 stays NonCC and O63.9 stays a CC (91 FR 49648-49652).
- Severity lists for FY 2027: Tables 6I (MCC), 6I.1, 6J (CC), 6J.1, 6J.2; CC exclusion changes: Tables 6G.1, 6G.2, 6H.1, 6H.2 (91 FR 49653). New codes and their severity: Table 6A.
- The correcting notice of Sept. 29, 2026 (FR Doc. 2026-19946) recalculated Table 5 relative weights. Use corrected weights for any payment estimate, and mark any weight not read from corrected Table 5 `[VERIFY]`.
- A worksheet, encoder table or CDI tip sheet built on an earlier version is a secondary source. When it disagrees with V44 for an FY 2027 discharge, V44 controls and the conflict goes in the reconciliation table.

## 2. Principal diagnosis (Section II and UHDDS)

- UHDDS (50 FR 31038-40, July 31, 1985): principal diagnosis is "the condition established after study to be chiefly responsible for occasioning the admission of the patient to the hospital for care."
- The circumstances of inpatient admission always govern; Tabular and Index conventions take precedence over the guidelines (Section II, opening paragraphs).
- II.A: a Chapter 18 symptom code is not principal when a related definitive diagnosis has been established. PIM 100-08, ch. 6, 6.5.3 applies the same rule in DRG validation.
- II.B: two interrelated conditions that each meet the definition may be sequenced either way unless the circumstances of admission, therapy, Tabular or Index direct otherwise.
- II.C: only in the unusual instance when two or more diagnoses equally meet the definition (circumstances of admission, workup, therapy) and nothing else directs sequencing may either be first. A condition that arose after admission never equally meets the definition.
- II.D: comparative or contrasting "either/or" diagnoses are coded as if confirmed and sequenced by the circumstances of admission.
- II.F: original treatment plan not carried out; II.G: complication of care as the reason for admission is principal; II.H: uncertain diagnoses at discharge coded as established (inpatient short-term acute, long-term care and psychiatric hospitals only).
- II.I and II.J: admission from observation or outpatient surgery; II.K: rehabilitation.
- Relative weight never selects the principal diagnosis. Where II.B or II.C truly applies, record the clinical facts that make the conditions equal; payment is not one of them.

## 3. Secondary diagnoses (Section III) and who may document them

- UHDDS item 11-b: other diagnoses are "all conditions that coexist at the time of admission, that develop subsequently, or that affect the treatment received and/or the length of stay"; conditions from an earlier episode with no bearing on this stay are excluded.
- Section III reportability: clinical evaluation, therapeutic treatment, diagnostic procedures, extended length of stay, or increased nursing care and/or monitoring.
- III.A: resolved or historical conditions with no bearing are not reported; history Z codes may be. III.B: abnormal findings (laboratory, x-ray, pathology) are not coded unless the provider indicates their clinical significance; when they are abnormal and the provider ordered tests or treatment, asking the provider is appropriate. III.C: uncertain diagnoses at discharge are coded as established (inpatient only).
- I.A.19: assignment rests on the provider's diagnostic statement; it is not based on the clinical criteria the provider used. Conflicting documentation is queried.
- I.B.14: codes are assigned from the patient's provider (physician or qualified practitioner legally accountable for the diagnosis). Exceptions where other clinicians' documentation may be used: BMI, depth of non-pressure chronic ulcers, pressure ulcer stage, coma scale, NIHSS, SDOH (Chapter 21), laterality, blood alcohol level, underimmunization status, firearm injury intent. The associated diagnosis (obesity, pressure ulcer, acute stroke, alcohol-related disorder) must still come from the provider. Malnutrition, encephalopathy and acute respiratory failure are not exceptions: a dietitian's, nurse's or therapist's note is a clinical indicator for a query, not a code.
- Consultants, specialists, advanced practice providers and ED providers may supply reportable diagnoses without a query unless they conflict with the attending, who is then queried (ACDIS/AHIMA 2026, Section VII).

## 4. CC, MCC and the CC exclusion list

- A secondary diagnosis acts as a CC or MCC only if it is on the V44 CC or MCC list and is not excluded with the principal diagnosis. V44 Appendix C Part 1 gives, for each CC or MCC, a PDX collection: when the principal diagnosis is in that collection, the CC or MCC counts as a non-CC. Part 2 lists codes that are a CC or MCC only if the patient is discharged alive. Part 3 lists codes that do not act as a CC or MCC within named MS-DRGs (for example 177-179, 280-285, 974-976).
- The excluded code is still reported when Section III and the classification require it; only its severity effect is removed.
- Confirmed V44 entries (Appendix C Part 1): R65.20 MCC, PDX collection 0072 (includes A41.9, A41.51 and the other A40-A41 sepsis codes); R65.21 MCC; J18.9 MCC, collection 0113 (129 codes; does not include A41.9, A41.51 or K26.4); J96.01, J96.02, J96.21 MCC; G93.41 MCC; E43 MCC; E44.0 and E46 CC; N17.0 MCC; N17.9 CC; N39.0 CC (HAC category 6); D62 CC; E87.1 CC; J44.1 CC; R78.81 CC; I50.21, I50.23, I50.33 MCC; R53.2 MCC. I10, E11.9, E78.5 and K21.9 are not on the CC or MCC lists.
- Split logic matters as much as severity. Families split "MCC / CC / neither" (193-195, 190-192, 377-379) move on a CC; families split only on MCC (871 versus 872) do not. Read the family's split in the Definitions Manual before stating an impact.
- Confirm any code not listed here against V44 Appendix C before stating its severity or exclusion; otherwise mark it `[VERIFY]`.

## 5. DRG families confirmed in Grouper V44

| Family | Split | MS-DRGs | Example principal diagnoses confirmed |
|---|---|---|---|
| Septicemia or Severe Sepsis | MV more than 96 hours; else MCC | 870 (MV more than 96 hours), 871 (with MCC), 872 (without MCC) | A41.9, A41.51, R65.20, R65.21, R78.81 |
| Simple Pneumonia and Pleurisy | MCC / CC / neither | 193, 194, 195 | J18.9, J13, J15.9 |
| Chronic Obstructive Pulmonary Disease | MCC / CC / neither | 190, 191, 192 | J44.0, J44.1, J44.9 |
| Gastrointestinal Hemorrhage | MCC / CC / neither | 377, 378, 379 | K26.4, K92.1, K92.2 |
| Pulmonary Edema and Respiratory Failure | none | 189 | |

R65.20 and R65.21 are listed as principal diagnoses in the 870-872 logic, but I.C.1.d says a code from R65.2 can never be assigned as principal; follow the guideline. Use the V44 Definitions Manual for every other family.

Procedures: in the V44 Definitions Manual, a procedure code marked with an asterisk is non-O.R.; every other listed procedure is an O.R. procedure, which can move the case to a surgical DRG in the principal diagnosis's MDC (or to 981-989 when unrelated). Check each ICD-10-PCS code against the operative report for root operation, body part and approach; an unclear operative note is a query candidate. ICD-10-PCS guideline rules are `[VERIFY]` (not read for FY 2027).

## 6. Sepsis coding and payer sepsis definitions

- I.C.1.d: severe sepsis needs at least two codes, the systemic infection first and then R65.2-, plus codes for the associated acute organ dysfunction. Organ dysfunction attributed to another cause does not support R65.2-; unclear linkage is queried. With a localized infection present on admission, the systemic infection is sequenced first; if sepsis develops after admission, the localized infection is first.
- I.A.19 governs: code the provider's documented sepsis. Sepsis-2 (SIRS) and Sepsis-3 (SOFA) are clinical definitions, not coding rules. The FY 2027 final rule notes that no single consensus definition exists (91 FR 49891, footnote 209).
- A payer that applies Sepsis-3 in clinical validation does so through its contract or policy. Read that document; until read, treat the payer's definition as a policy election `[VERIFY]` and analyze both readings. The coding response is a clinical validation query when indicators look insufficient, not recoding. The denial response goes to managing-coding-denials. SEP-1 abstraction is a separate measure (managing-sepsis-bundles).

## 7. POA indicators and the HAC payment provision

- POA means present when the order for inpatient admission occurs; conditions that develop in the ED, observation or outpatient surgery before the order are POA (Guidelines, Appendix I).
- Indicators: Y (present), N (not present), U (documentation insufficient), W (provider clinically unable to determine); exempt codes are unreported. POA questions about timing or linkage are queried; a POA yes/no query must include "unable to determine" (ACDIS/AHIMA 2026).
- HAC payment provision (DRA 2005, section 5001(c)): for the 14 HAC categories, the case is paid as though the secondary diagnosis were not present when it was not present on admission. CMS pays Y and W, not N and U (MLN901046, FY 2015 chart; confirm no later change `[VERIFY]`). The HAC-POA provision is separate from the HAC Reduction Program (ACA section 3008).
- Never set POA to change payment or quality results. A POA error that removes or adds HAC treatment goes in the reconciliation table with its source.

## 8. Inpatient status, payer basis and transfers

- MS-DRG review applies only to an inpatient claim. Under 42 CFR 412.3 the patient is an inpatient when formally admitted on an inpatient order (412.3(a)) given at or before admission (412.3(c)); admission is generally appropriate when the admitting physician expects care crossing two midnights (412.3(d)(1)), for inpatient-only procedures (412.3(d)(2)), or by documented judgment for a shorter expected stay (412.3(d)(3)).
- Medicare Advantage plans must follow 412.3 (42 CFR 422.101(b)(2)). Whether a plan or commercial payer pays on MS-DRG, APR-DRG or another basis is contractual `[VERIFY]` per payer.
- Status disputes and observation conversion go to managing-observation-stays. Contractors that find the stay did not meet Part A requirements deny the claim; a deemed date of admission resets the principal diagnosis (PIM 100-08, ch. 6, 6.5.2).
- Transfers (42 CFR 412.4): an acute-care transfer (412.4(b)) or a post-acute care transfer from a qualifying DRG to an excluded hospital or unit, a SNF, home health starting within 3 days, or hospice (412.4(c)) is paid a graduated per diem (412.4(f)). The FY 2027 qualifying list is in the final rule tables `[VERIFY]` the count. A discharge against medical advice is not one of the transfer circumstances in 412.4(b)-(c).

## 9. Inpatient versus outpatient guideline sections

- Section IV applies to outpatient encounters. Its rules differ: IV.H says not to code "probable" or "suspected" diagnoses but to code symptoms, signs or findings instead, and III.B notes that outpatient practice differs for diagnostic-test encounters interpreted by a provider. Applying Section IV to an inpatient claim drops reportable uncertain diagnoses; applying II.H or III.C to an observation claim adds diagnoses that are not reportable.
- Check the claim type first, then apply the matching section.
