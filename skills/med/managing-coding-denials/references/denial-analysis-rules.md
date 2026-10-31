# Denial Analysis Rules

How to classify a denial, which standard answers it, and which arguments fail. Checked October 30, 2026 against `references/primary-sources.md`.

## Contents

1. Classify the denial before arguing it
2. Code assignment and the provider's statement
3. Clinical definitions written into payer contracts
4. Inpatient status and the 2-midnight rule
5. Medicare Advantage coverage criteria
6. Record integrity and evidence timing
7. Peer-to-peer and discussion periods
8. Appeal, rebill, reopen or accept

## 1. Classify the denial before arguing it

| Denial type | What the reviewer says | Controlling standard | Evidence that answers it | Argument that fails |
|---|---|---|---|---|
| Coding validation (DRG validation) | The codes, sequencing or discharge status do not match the provider's documentation | ICD-10-CM Official Guidelines, UHDDS definitions, CMS clarifications (PIM ch. 6, 6.5.3) | The provider's documentation and the guideline section that assigns the code | Clinical severity alone; a reviewer who agrees the patient was sick is not answering whether the code follows the documentation |
| Clinical validation | The documented diagnosis is not clinically supported: the patient did not truly have the condition | The clinical definition the payer may apply under its contract or policy, read against the record's clinical indicators | Sourced indicators (values, times, authors) measured against that definition | "The physician wrote it, so it must be coded" (I.A.19) offered as the whole answer |
| Medical necessity or patient status | Inpatient admission or a service was not reasonable and necessary | 42 CFR 412.3; PIM ch. 6, 6.5.2; for MA, 422.101(b)-(c) | Admitting practitioner's expectation and the complex medical factors known at the order | Arguing the codes were correct |
| Technical or administrative | Timely filing, authorization, duplicate, missing records, eligibility | The filing, authorization or ADR rule | Transmission reports, authorization numbers, ADR response receipts | Clinical or coding argument |

One letter may contain more than one type; answer each in its own section. Route the DRG grouping itself (principal diagnosis selection, CC/MCC capture, the resulting MS-DRG) to managing-drg-optimization and use its validated result.

## 2. Code assignment and the provider's statement

- I.A.19 (FY 2027 Guidelines): code assignment is based on the provider's diagnostic statement that the condition exists; it is not based on the clinical criteria the provider used; conflicting documentation is queried.
- I.B.14: code assignment rests on the documentation of the patient's provider, with listed exceptions (BMI, ulcer depth, pressure ulcer stage, and others).
- I.A.19 answers a coding validation denial that removed a code the provider documented. It does not by itself answer a clinical validation denial, because the payer is questioning whether the condition was present, not how it was coded. Pair the two: the code follows the statement, and the record shows the clinical picture under the definition the payer may apply.
- RACs may not perform clinical validation (RAC SOW). A RAC finding that the patient "did not meet criteria" for a documented condition is outside its scope; raise that first, then the merits.

## 3. Clinical definitions written into payer contracts

- Sepsis-3 (Singer et al., JAMA 2016): sepsis is life-threatening organ dysfunction caused by a dysregulated host response to infection; organ dysfunction is an acute change in total SOFA score of 2 or more points consequent to the infection; baseline SOFA is assumed to be zero unless preexisting organ dysfunction is known. Septic shock: vasopressor requirement to keep MAP at 65 mm Hg or more and lactate above 2 mmol/L without hypovolemia. qSOFA (respiratory rate 22 or more, altered mentation, systolic BP 100 or less) is a bedside prompt, not the definition.
- SOFA points used most often in appeals (Sepsis-3, Table 1): creatinine below 1.2 mg/dL is 0, 1.2-1.9 is 1, 2.0-3.4 is 2, 3.5-4.9 is 3; platelets 150 or more is 0, below 150 is 1, below 100 is 2, below 50 is 3; bilirubin below 1.2 is 0, 1.2-1.9 is 1, 2.0-5.9 is 2; MAP 70 or more is 0, below 70 is 1, any vasopressor is 2 or more by dose; GCS 15 is 0, 13-14 is 1; PaO2/FiO2 400 or more is 0, below 400 is 1, below 300 is 2.
- Sepsis-2 is the SIRS-based 2001 consensus definition; its criteria were not read in a primary source for this skill `[VERIFY]`. SEP-1 is a CMS quality measure with its own SIRS-based criteria; it governs neither coding nor payment (route to managing-sepsis-bundles).
- Rule: read the contract, amendment or provider manual in force on the date of service for the definition the payer may apply, its effective date, and whether the payer may apply it to clinical validation at all. Argue under that definition. If the contract is not supplied, list the definition as a policy election `[VERIFY]` and show the record under each candidate definition. Never answer a Sepsis-3 contract with SIRS criteria, or a SIRS-based contract with SOFA, as the main argument.
- Other conditions (acute respiratory failure, malnutrition, encephalopathy, acute kidney injury) follow the same rule: the payer's contractual definition, the indicators in the record, and the provider's statement, kept separate.

## 4. Inpatient status and the 2-midnight rule

- 412.3: inpatient order at or before admission; admission generally appropriate when the admitting practitioner expects medically necessary care crossing 2 midnights (412.3(d)(1)); inpatient-only procedures (412.3(d)(2)); case-by-case exception by documented judgment (412.3(d)(3)) (as confirmed by managing-drg-optimization).
- PIM ch. 6, 6.5.2: the 2-midnight presumption steers contractors away from reviewing stays of 2 or more midnights after the order; the 2-midnight benchmark judges the admitting practitioner's reasonable expectation at the time of the order; contiguous outpatient time before the order (ED, observation) counts toward the benchmark; later entries are used only to interpret what the practitioner knew and expected; stays under 24 hours rarely qualify for an exception.
- Medicare Advantage: plans must follow 412.3, including the benchmark (422.101(b)(2)); plans are not bound by the presumption, which is a medical review instruction for Medicare contractors (CMS FAQ, Feb. 6, 2024).
- Status disputes go to managing-observation-stays for status determination; this skill handles the denial and appeal.

## 5. Medicare Advantage coverage criteria

- A plan must make medical necessity decisions from the coverage criteria in 422.101(b) and (c), the enrollee's history, physician recommendations and clinical notes, and may not deny basic benefits on criteria not specified there (422.101(c)(1)).
- Internal coverage criteria are allowed only when Medicare criteria are not fully established, must rest on widely used treatment guidelines or qualifying clinical literature, and must be publicly accessible with an evidence summary and rationale (422.101(b)(6)); a commercial screening tool cited without that showing does not meet the rule (CMS FAQ, Feb. 6, 2024). Inpatient admission criteria are established in 412.3, so a screening-tool failure is not itself a basis to deny an admission that meets 412.3.
- Ask for the plan's posted criteria and evidence summary; if none is posted, say so in the appeal.
- An approved prior authorization or concurrent determination bars a later medical necessity denial except on a good-cause or fraud reopening (422.138(c)).
- These are coverage rules. A contracted hospital pursues them through its agreement's dispute process; a non-contracted hospital through 422.582 with a waiver of liability.

## 6. Record integrity and evidence timing

- Build the appeal on the record as it stood when the claim was billed. Entries made later are identified by date, time and author.
- PIM ch. 3, 3.3.2.5: services are expected to be documented when rendered; an amendment, correction or delayed entry must show its date and author and be clearly and permanently marked; reviewers refer potentially fraudulent entries to the UPIC.
- A query answered after billing is answered by an addendum dated when written (ACDIS/AHIMA 2026 brief); whether post-bill queries are allowed at all is set by organizational policy. A post-denial answer is a late entry, never part of the original note, and changes coding only through a corrected claim within the applicable window.
- Never draft, merge, backdate or re-date an entry, and never present a post-claim or post-denial entry as original. If asked, record a Declined request and continue with the record as it stands. If altered entries were already submitted, stop the appeal draft for that claim and route to conducting-false-claims-analysis and compliance.
- Medicare evidence timing: submit everything by the QIC level (405.966(a)); a provider's new evidence at OMHA is excluded without good cause (405.1028(a)).

## 7. Peer-to-peer and discussion periods

- Record for every call: date and time, payer reference number, participants and credentials, the denial issue discussed, the outcome stated, and whether the payer confirmed it in writing. An oral overturn without written confirmation is open, not won.
- A peer-to-peer or RAC discussion does not extend a written appeal deadline unless the contract or a written payer notice says so; diary the appeal deadline regardless.

## 8. Appeal, rebill, reopen or accept

| Situation | Usual route | Check first |
|---|---|---|
| Record supports the billed codes or status; denial is wrong | Appeal | Clock, level, amount in controversy, evidence complete by QIC |
| Hospital's own coding was wrong; correction lowers payment | Correct the claim or accept the adjustment | Whether an appeal is already pending (405.980(a)(4)); overpayment duties to conducting-false-claims-analysis |
| Hospital found a higher DRG after payment | DRG review request within 60 days of the DRG notice (412.60(d)) | Window from the DRG assignment notice; route DRG merits to managing-drg-optimization |
| Clerical or data-entry error | Reopening (405.980(a)(3)) | Not an appeal; the clerical label must fit |
| Part A inpatient denied as unnecessary, admission weak under 412.3 | Part B inpatient claim within 1 year of the through date, or appeal | Both readings of the pending-appeal rule; deadline of each route |
| Denied for no ADR response | Request is handled as a reopening (405.980(a)(2)) | Proof of the original ADR response, if any |
| No supportable argument on the record as billed | Accept denial | Write-off approval per policy; education item |
