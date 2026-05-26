# Automated Medical Record Chronology Generation

## Prerequisites
- Complete set of client medical records (PDFs, scanned documents)
- Scope definition (full history vs. date range, specific providers)

## Workflow
1. Ingest all records and index by document type, date, and authoring provider
2. Extract clinical events from each document:
   - Visits/admissions and discharge summaries
   - Physician and nursing notes, progress reports
   - Diagnostic orders and results (labs, imaging, EKG)
   - Medication administrations and changes
   - Surgical/procedure notes and operative reports
3. Compile a master timeline:
   - Sort all events chronologically
   - Identify key milestones (diagnosis, treatment start, adverse events, discharge)
   - Flag inconsistencies (date conflicts, missing entries, duplicate records)
4. Generate the chronology document:
   - Date | Time | Provider | Document Type | Event Description | Source Citation
   - Color-code by severity/clinical significance
   - Include a summary of events with pattern indicators
5. Output a court-ready chronology with page citations for evidentiary use

## Pitfalls
- Scanned documents may have incorrect dates — cross-reference with other records
- Different providers use different date formats — normalize to YYYY-MM-DD
- Nursing notes vs. physician notes may describe the same event differently — reconcile
- Lab results are time-stamped but dates on the page may differ — use the report date
- Missing entries are as important as present entries — document gaps in the chronology

## Tags
practice_area: litigation
document_type: summary
skill_mode: summarization
