---
name: medical-record-summarization
description: Extracts, organizes, and summarizes medical records into chronological timelines for litigation. Processes medical PDFs, identifies treatments and diagnoses, and produces attorney-ready summaries. Use when preparing personal injury, medical malpractice, or disability cases requiring medical record analysis.
tags:
  - medical-records
  - personal-injury
  - summarization
---

# Medical Record Summarization

Processes medical records into organized chronological summaries for litigation support.

## Prerequisites

1. **Medical records** — treatment records, imaging reports, surgical notes, discharge summaries uploaded to vault
2. **OCR capability** — many medical records are scanned PDFs or faxes
3. **Case context** — date of incident, claimed injuries, treating providers

## Workflow

### 1. Ingest and OCR

- Upload all medical records to vault
- OCR scanned documents; flag illegible pages for manual review
- Organize by provider and date

### 2. Extract Key Data

For each record, extract:
- Date of service and provider
- Chief complaint and diagnosis (ICD codes if present)
- Treatment provided and medications prescribed
- Objective findings (imaging, lab results, physical exam)
- Prognosis and follow-up recommendations
- Any causation opinions linking treatment to incident

### 3. Build Chronology

- Organize all entries in date order across providers
- Highlight gaps in treatment (defense will argue significance)
- Flag pre-existing conditions mentioned in records
- Note any inconsistencies between providers

### 4. Generate Summary

- Executive summary: injury overview, treatment timeline, current status
- Detailed chronology table: date, provider, diagnosis, treatment, notes
- Red flags section: gaps, inconsistencies, pre-existing conditions
- Store in vault linked to the matter

## Pitfalls

- **Pre-existing conditions** — don't hide them; opposing counsel will find them. Document and contextualize
- **Treatment gaps** — gaps >30 days will be attacked; note them with any explanations from the record
- **Causation language** — distinguish "consistent with" from "caused by" — they're legally different
- **Illegible records** — flag rather than guess; a wrong medical interpretation can torpedo a case
