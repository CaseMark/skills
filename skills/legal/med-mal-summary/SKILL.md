---
name: med-mal-summary
description: Analyzes medical records to produce structured medical malpractice case summaries for personal injury litigation. Extracts chronological care narratives, identifies potential breaches of standard of care, traces causation chains, assesses damages, and flags legal considerations including expert needs and statute of limitations issues. Use when evaluating medical negligence claims, onboarding med-mal matters, preparing for litigation, or assessing case merits during pre-filing or discovery phases.
tags:
  - analysis
  - litigation
  - summarization
  - summary
---

# Medical Malpractice Summary

Produces a comprehensive medical malpractice case summary from medical records and related documentation, structured for attorney case evaluation and litigation planning.

## Prerequisites

1. **Medical records** — hospital charts, physician notes, nursing notes, discharge summaries
2. **Diagnostic materials** — lab results, imaging/radiology reports, pathology reports
3. **Procedure documentation** — operative reports, anesthesia records, consent forms
4. **Pharmacy records** — medication administration records, prescription history
5. **Patient intake** — chief complaint, date of incident, treating providers, patient demographics

## Output Structure

### 1. Case Overview Table

| Field | Content |
|---|---|
| Patient | Name, DOB, relevant medical history |
| Date(s) of alleged negligence | Specific dates |
| Facility/Provider(s) | Names, specialties, roles |
| Chief complaint / Presenting condition | Initial presentation |
| Alleged injury/outcome | Summary of harm |
| SOL flag | Statute date + discovery rule considerations |

### 2. Chronological Care Narrative

For each treatment episode, document in table format:

| Date | Provider (Specialty) | Clinical Findings | Diagnosis | Treatment/Orders | Outcome/Notes |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Flag entries with `⚠` where potential standard-of-care issues exist.

### 3. Standard of Care Analysis

For each identified deviation:

- **Provider**: Name and specialty
- **Action/Omission**: What was done or not done
- **Expected standard**: What a reasonably competent provider in that specialty would have done
- **Supporting basis**: Clinical guidelines, protocols, or accepted practice (cite specific guidelines where identifiable)
- **Severity**: Critical / Significant / Minor

Checklist of common breach categories to evaluate:

- [ ] Diagnostic errors — missed, delayed, or wrong diagnosis
- [ ] Failure to order appropriate tests
- [ ] Misinterpretation of test results
- [ ] Treatment selection errors
- [ ] Surgical/procedural errors
- [ ] Medication errors (wrong drug, dose, interaction)
- [ ] Failure to obtain informed consent
- [ ] Monitoring failures (post-op, medication, vitals)
- [ ] Premature discharge
- [ ] Failure to refer to specialist
- [ ] Communication failures between providers
- [ ] Documentation gaps or alterations

### 4. Causation Analysis

For each identified breach, trace the chain:

```
Breach → Mechanism of Harm → Injury/Outcome
```

Distinguish:
- **Harm attributable to negligence** — injuries that would not have occurred but for the breach
- **Harm from underlying condition** — natural disease progression
- **Unavoidable complications** — known risks of necessary treatment
- **Concurrent/intervening causes** — other contributing factors

### 5. Damages Assessment

| Category | Details | Documentation Source |
|---|---|---|
| Additional medical treatment | Surgeries, hospitalizations, rehab, future care | Page/record refs |
| Physical impairment | Permanent injury, disability, functional limitations | Page/record refs |
| Pain and suffering | Duration, severity, ongoing nature | Page/record refs |
| Lost wages / Earning capacity | Work restrictions, vocational impact | Page/record refs |
| Life expectancy impact | If applicable | Page/record refs |

### 6. Legal & Evidentiary Flags

- **Expert specialties needed**: List by specialty based on providers and issues involved
- **Statute of limitations**: Calculate based on treatment dates; note discovery rule triggers
- **Record red flags**: Gaps, late entries, alterations, inconsistencies between providers
- **Provider admissions**: Any documented apologies, acknowledgments of error, incident reports
- **Applicable guidelines**: Cite specific clinical practice guidelines, hospital protocols, or standards referenced or implicated
- **Strengths**: Strongest facts supporting liability and damages
- **Weaknesses**: Defenses, contributory factors, documentation gaps undermining the claim

## Guidelines

- Cite every factual assertion to specific page numbers, dates, and document sources
- Use medical terminology with parenthetical plain-language explanations on first use
- Present balanced analysis — identify both strengths and weaknesses of the claim
- Do not render legal conclusions on ultimate liability; frame as "potential" breaches for attorney evaluation
- Flag any records that appear incomplete or were not provided
- If standard-of-care analysis requires subspecialty knowledge beyond the records, note that expert consultation is needed on that point
- Mark any cited clinical guidelines or statistics with `[VERIFY]` unless directly quoted from provided records
