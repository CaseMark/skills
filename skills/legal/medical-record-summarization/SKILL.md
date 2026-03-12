---
name: medical-record-summarization
description: Extracts and organizes medical records into chronological timelines for litigation. Processes medical PDFs, identifies treatments and diagnoses, and produces attorney-ready summaries.
tags:
  - litigation
  - summary
  - summarization
---

# Medical Record Summarization

Processes medical records into organized chronological summaries for litigation.

## Prerequisites

1. **Medical records** — treatment records, imaging, surgical notes, discharge summaries in vault
2. **OCR capability** — many records are scanned PDFs
3. **Case context** — incident date, claimed injuries, treating providers

## Workflow

### 1. Ingest
Upload to vault. OCR scanned documents. Flag illegible pages. Organize by provider and date.

### 2. Extract
Per record: date/provider, diagnosis (ICD codes), treatment/medications, objective findings, prognosis, causation opinions.

### 3. Build Chronology
Date-order across providers. Highlight treatment gaps. Flag pre-existing conditions. Note inconsistencies.

### 4. Summarize
Executive summary: injury overview, timeline, status. Chronology table. Red flags: gaps, inconsistencies, pre-existing conditions.

## Pitfalls
- Document pre-existing conditions — opposing counsel will find them
- Note treatment gaps >30 days with explanations from the record
- Distinguish "consistent with" from "caused by" — legally different
- Flag illegible records rather than guessing — wrong interpretation can torpedo a case
