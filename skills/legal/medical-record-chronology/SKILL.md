---
name: medical-record-chronology
description: Creates chronological summaries of medical records for litigation. Extracts treatment timelines, provider details, diagnoses, medications, and causation evidence. Identifies gaps, inconsistencies, and missing records. Use when analyzing medical records in personal injury, medical malpractice, workers' compensation, or disability cases.
---

# Medical Record Chronology

Produces a structured, date-ordered summary of medical records for litigation — interleaving all providers chronologically. Extracts treatment details, causation evidence, and strategic insights.

## Quick Start

1. Gather case context: patient name, DOB, incident date, case type, claimed injuries, known pre-existing conditions
2. Build provider index listing each provider/facility, type, date range, and records-obtained status (Yes/Partial/No)
3. Summarize pre-incident history for same body parts, prior injuries, baseline function, and medications at time of incident
4. Create chronological entries for every encounter (see format below)
5. Compile diagnostic summary, medication history, and damages
6. Write strategic analysis covering favorable/adverse findings, gaps, and inconsistencies

## Encounter Entry Format

For each encounter, strictly ordered by date across all providers:

**[Date] — [Provider Name] — [Facility] — [Visit Type]**

- **Chief complaint**: Patient's stated reason
- **History**: Mechanism of injury, symptom onset
- **Examination findings**: Objective findings (vitals, physical exam, neurological)
- **Diagnostic studies**: Imaging, labs, EMG/NCV results
- **Diagnosis/Assessment**: ICD codes and narrative diagnoses
- **Treatment**: Procedures, medications prescribed, referrals
- **Restrictions/Limitations**: Work restrictions, activity limitations
- **Follow-up**: Next appointment, recommended further care
- **Causation language**: Provider statements linking injuries to incident — **flag prominently**
- **Source**: Bates number or provider record page reference

## Output Sections

### Case Header

Patient name, DOB, incident date, case type (PI / Med Mal / Workers Comp / Disability), pre-existing conditions, claimed injuries.

### Provider Index

Table: #, Provider/Facility, Type (ER/PCP/Specialist/PT), Date Range, Records Obtained (Yes/Partial/No).

### Pre-Incident Medical History

Chronological summary of: same body parts/conditions, prior injuries/accidents, medications at incident, baseline functional status.

### Treatment Timeline

Visual arrow diagram from incident through MMI:

```
[Incident] → ER → PCP → Ortho → MRI → PT (12x) → IME → Surgery → PT (24x) → MMI
```

### Diagnostic Summary

Table: Date, Study, Facility, Findings, Significance.

### Medication History

Table: Medication, Prescribed By, Start Date, End Date, Purpose.

### Damages Summary

- Total medical expenses by provider
- Lost work time with dates and documentation
- Functional limitations documented
- Permanency/MMI status
- Future treatment recommendations

## Strategic Analysis

- **Favorable findings**: Evidence supporting causation and damages
- **Adverse findings**: Pre-existing conditions, treatment gaps, inconsistent histories, non-compliance
- **Gaps in records**: Missing providers, unexplained treatment gaps, records to request
- **Inconsistencies**: Conflicting histories across providers, discrepancies between records
- **Follow-up needed**: Records to request, depositions to schedule, IME considerations

## Critical Rules

- Strict chronological order — interleave all providers by date
- Quote exact provider causation language in quotation marks with Bates/page citation
- Flag every mention of pre-existing conditions or prior treatment to same body part
- Note all treatment gaps — opposing counsel argues gap = no injury
- Track medication changes — escalation suggests worsening, discontinuation suggests resolution
- Distinguish objective findings (imaging, measurements) from subjective complaints
- Note every mechanism-of-injury description — inconsistencies are impeachment material
- Include both favorable and unfavorable entries — the attorney needs the complete picture

---

**Key changes made:**

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` in frontmatter)
- **Tightened description** — kept third-person, added workers' comp trigger, stayed under 1024 chars
- **Added Quick Start workflow** — 6 numbered steps giving the agent a clear execution path
- **Eliminated empty template tables** — replaced with concise field-list descriptions (Claude knows how to render tables)
- **Collapsed Output Structure into Output Sections** — each section described in 1-2 lines instead of full empty-row tables
- **Renamed Guidelines → Critical Rules** — stronger framing, same content condensed
- **Reduced from ~105 lines to ~85 lines** — well under 500-line budget while preserving all domain-specific legal knowledge
