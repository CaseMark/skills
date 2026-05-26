# Medical Record Summarization for Billing Defense

## Prerequisites
- Patient medical records (encounter notes, orders, labs, imaging reports)
- Applicable CPT codes and billing period
- Carrier/payer guidelines (CMS manuals, state Medicaid, commercial plan rules)

## Workflow
1. Ingest medical records and index by date, provider, service type
2. For each encounter:
   - Extract diagnoses (ICD-10), procedures (CPT/HCPCS), modifiers
   - Map services to clinical guidelines and coverage determinations
   - Identify documentation gaps (missing medical necessity, lack of supporting notes)
   - Flag encounters with coding inconsistencies (upcoding, unbundling signals)
3. Generate an encounter-by-encounter summary:
   - Clinical narrative in plain language
   - Coding compliance assessment per payer guidelines
   - Supporting evidence citations (CMS manual sections, carrier bulletins)
4. Produce an overall audit summary: risk score, recovery potential, top issue categories
5. Output attorney-ready summaries with cite-ready references

## Pitfalls
- CMS guidelines change annually — verify the applicable year's manuals
- Modifier usage (25, 59, X{EPSU}) must match current AMA conventions
- Medical necessity determinations require specific documentation — vague notes = denial risk
- Don't conflate professional vs. facility billing rules — they differ by setting
- Coding guidelines (ICD-10-CM, CPT, HCPCS) have different versioning cycles

## Tags
practice_area: regulatory
document_type: summary, analysis
skill_mode: summarization
