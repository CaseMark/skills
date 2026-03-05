---
name: analyzing-clinical-data-warehouses
description: Structures clinical data warehouse queries for quality measurement, research, and operational analytics. Use when querying clinical data, building analytics reports, or extracting research datasets.
tags:
  - analysis
  - health-informatics
  - clinical
  - research
metadata:
  author: casemark
  practice_areas:
    - Health Informatics
    - Health IT
    - Clinical Informatics
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing Clinical Data Warehouses

Structures clinical data warehouse queries for quality measurement, research, and operational analytics using OMOP CDM, i2b2, PCORnet, and proprietary warehouse schemas.

## Why This Skill Exists

Clinical data warehouses (CDWs) aggregate billions of patient records from EHRs, claims, registries, and lab systems. Analysts who query these warehouses without understanding data provenance, ETL transformations, or common data model semantics produce misleading results — misidentified cohorts, inflated denominators, duplicated encounters, or concept sets that silently exclude relevant patients. Wrong CDW output directly harms quality measurement (CMS Star Ratings, HEDIS), clinical trial feasibility, and population health interventions.

This skill encodes the analytical discipline required to extract defensible datasets. It covers schema selection, concept mapping, ETL validation, cohort definition, temporal logic, and output attestation — the full pipeline from warehouse query to actionable analytic artifact.

---

## Checkpoint A: Pre-Query Intake (Mandatory)

Before writing any SQL or configuring any extract, the analyst must answer:

1. What is the business or research question in one declarative sentence?
2. Which CDW platform and version is the target (Epic Caboodle/Clarity, Cerner HealtheIntent, OMOP v5.4, i2b2, PCORnet CDM v6, custom)?
3. What date range and refresh cadence does the analysis require?
4. What patient population is in scope (age, payer, geography, clinical condition)?
5. Which outcome, exposure, or quality measure defines the primary variable?
6. Are there IRB/HIPAA limitations — limited dataset, de-identified, or identified access?
7. What is the target output format (flat file, dashboard feed, REDCap import, registry submission)?
8. Who is the downstream consumer (quality team, research PI, C-suite, payer)?

### Documents to Request

- Data dictionary or schema documentation for the target CDW
- ETL specification or mapping document (source-to-target)
- IRB protocol or data use agreement (if research)
- Quality measure specification (NQF, HEDIS, CMS) if applicable
- Previous versions of the analytic query or report (if iteration)
- Concept set definitions or value set OIDs from VSAC
- Data quality report from most recent ETL refresh

---

## Step 1: Schema Reconnaissance and Data Profiling

### Identify the Common Data Model

| CDM | Key Tables | Concept System | Notes |
|-----|-----------|----------------|-------|
| OMOP v5.4 | condition_occurrence, drug_exposure, measurement, visit_occurrence, person | SNOMED, RxNorm, LOINC via concept table | Vocabulary-driven; always join through concept_id |
| i2b2 | observation_fact, patient_dimension, visit_dimension, concept_dimension | Local ontology cells | Star schema; facts pivot on concept_cd |
| PCORnet CDM v6 | DIAGNOSIS, PROCEDURES, ENCOUNTER, DEMOGRAPHIC | ICD-10-CM, CPT, HCPCS directly | Flat structure; includes HARVEST metadata table |
| Epic Clarity | PAT_ENC, ORDER_PROC, CLARITY_SER, HSP_ACCOUNT | Internal Epic IDs mapped to standard codes | Proprietary; requires Chronicles → Clarity mapping |
| Epic Caboodle | FactEncounter, DimPatient, BridgeDiagnosis | Same Epic IDs with dimensional model | Kimball-style; use bridge tables for many-to-many |

### Data Profiling Checklist

- Run row counts on core tables; compare to expected patient volume
- Check NULL rates on critical columns (visit_start_date, concept_id, person_id)
- Validate date ranges — confirm ETL includes the analysis window
- Profile concept_id distributions; flag unmapped (concept_id = 0 in OMOP) rows
- Confirm referential integrity (every condition_occurrence.person_id exists in person table)
- Examine the ETL log for load errors, truncation warnings, or skipped source rows
- Document the data refresh date — never present stale data as current

---

## Step 2: Concept Mapping and Value Set Construction

### Building Defensible Concept Sets

1. Start with the authoritative value set (VSAC OID for quality measures, study protocol appendix for research)
2. Map each source code to the CDM vocabulary — in OMOP, use the concept_relationship table to traverse hierarchies
3. Apply the INCLUDE_DESCENDANTS flag only when clinically justified (e.g., including all children of SNOMED "Diabetes mellitus" 73211009)
4. Manually review edge cases: "unspecified" codes, "history of" vs. active condition, laterality modifiers
5. Validate concept set against a known gold-standard cohort or chart-reviewed sample

### Common Pitfalls

| Pitfall | Impact | Mitigation |
|---------|--------|------------|
| Using ICD-10 codes directly in OMOP queries | Misses SNOMED-mapped records | Always query through standard concept_id |
| Including "history of" codes in active disease cohorts | Inflates prevalence | Filter on condition_status_concept_id |
| Ignoring source vocabulary version changes between ETL refreshes | Silent cohort drift | Pin vocabulary version in documentation |
| Treating drug_exposure as dispensing when source is prescribing | Overestimates adherence | Check drug_type_concept_id |
| Failing to deduplicate across source systems in multi-site warehouses | Double-counted patients | Use master person index or probabilistic linkage |

---

## Step 3: Cohort Definition and Temporal Logic

### Cohort Entry Criteria

Define each inclusion and exclusion criterion as a discrete, testable SQL predicate:

- **Index event**: The first qualifying occurrence (e.g., first inpatient visit with primary diagnosis of AMI)
- **Lookback window**: Period before index for baseline characteristics (typically 365 days)
- **Clean window**: Required observation time before index to confirm incident (not prevalent) cases
- **Follow-up window**: Required observation time after index for outcome ascertainment
- **Washout period**: Gap required between treatment episodes for new-user designs

### Temporal Logic Rules

1. Use observation_period (OMOP) or ENROLLMENT (PCORnet) to confirm continuous enrollment
2. Never assume absence of a record means absence of a condition
3. Apply era-building logic for chronic conditions — OMOP provides condition_era, drug_era tables
4. Handle multiple qualifying index events consistently (first, last, or all)
5. Document the gap allowance for era construction (default 30 days for condition, persistence gap for drugs)

---

## Step 4: Query Construction and ETL Validation

### SQL Standards for CDW Queries

- Use CTEs (WITH clauses) for readability; name each CTE after its logical role (eligible_patients, index_events, outcomes)
- Never use SELECT * in production queries — enumerate columns explicitly
- Cast dates consistently; use DATE type, not DATETIME, unless time precision matters
- Apply explicit JOIN types (INNER, LEFT) — avoid implicit comma joins
- Comment each CTE with the criterion it implements and the expected row count range

### ETL Validation Queries

Run these before trusting any extract:

1. **Completeness**: Compare CDW patient count to source system census for the same period
2. **Conformance**: Check that coded fields contain only valid vocabulary codes (no orphan concept_ids)
3. **Plausibility**: Verify that temporal ordering makes sense (no discharge before admission, no death before last visit)
4. **Uniqueness**: Confirm no duplicate primary keys in fact tables
5. **Timeliness**: Verify the most recent record date matches the documented ETL refresh date

---

## Step 5: Output Attestation and Documentation

### Required Output Metadata

Every analytic extract must include:

- Query execution date and CDW refresh date
- CDW platform, version, and vocabulary version
- Complete SQL or query logic (version-controlled)
- Row counts at each filtering step (attrition table)
- Concept sets used with all included codes
- Known data quality issues and their expected impact
- De-identification method applied (if applicable)

### Attrition Table Format

| Step | Description | Patients Remaining | Excluded |
|------|-------------|-------------------|----------|
| 0 | All persons in CDW | N | — |
| 1 | With qualifying diagnosis | n₁ | N − n₁ |
| 2 | With continuous enrollment | n₂ | n₁ − n₂ |
| 3 | Meeting age criteria | n₃ | n₂ − n₃ |
| 4 | After exclusions | n₄ | n₃ − n₄ |

---

## Step 6: Common Quality Measure Patterns

### HEDIS / CMS Quality Measure CDW Implementation

| Measure Type | CDW Logic Pattern | Common Error |
|-------------|------------------|-------------|
| Process measure (e.g., HbA1c testing) | Look for LOINC code in measurement table within measurement period | Missing LOINC mappings for point-of-care results |
| Outcome measure (e.g., HbA1c control < 8%) | Identify most recent result value within measurement period | Using average instead of most recent; not handling non-numeric result values |
| Exclusion criteria (e.g., hospice, pregnancy) | Join to condition/encounter tables for exclusion diagnosis within relevant window | Exclusion codes change yearly; stale value sets miss eligible patients |
| Continuous enrollment | Verify observation_period or enrollment table covers the full measurement period | Gap tolerance not applied; patients lost during insurance transitions |
| Denominator definition | Intersection of age, condition, and enrollment criteria | Applying age at query date instead of age at measurement period start |

### Research Cohort vs. Quality Measure Differences

| Dimension | Research Cohort | Quality Measure |
|-----------|----------------|----------------|
| Population | Defined by protocol inclusion/exclusion | Defined by measure specification (NQF, HEDIS) |
| Time anchor | Index event (variable per patient) | Fixed measurement year (Jan 1 – Dec 31) |
| Outcome | Study-defined endpoint | Pre-specified numerator criteria |
| Exclusions | Protocol-driven, IRB-approved | Measure specification-driven, updated annually |
| Validation | Chart review sample | HEDIS hybrid audit methodology |

---

## Checkpoint B: Post-Extract Alignment (Mandatory)

Before releasing any analytic output:

1. Does the final cohort size fall within the expected range for the target population?
2. Have you reviewed a random sample of 20 patients against source charts or operational reports?
3. Is the attrition table complete with no unexplained large drops?
4. Have all concept sets been reviewed by a clinical subject matter expert?
5. Has the output been checked for PHI leakage (SSN, MRN, names) if de-identification was required?

---

## Quality Audit

| # | Criterion | Pass / Fail |
|---|-----------|-------------|
| 1 | Business question stated in one declarative sentence | |
| 2 | CDW platform and version documented | |
| 3 | ETL refresh date recorded and within acceptable staleness window | |
| 4 | Concept sets traceable to authoritative value sets or documented custom logic | |
| 5 | Data profiling results recorded (NULLs, row counts, concept_id = 0 rates) | |
| 6 | Cohort entry and exit criteria each expressed as testable SQL predicates | |
| 7 | Temporal logic (lookback, follow-up, washout) explicitly defined | |
| 8 | Attrition table present with counts at every filtering step | |
| 9 | SQL version-controlled and commented | |
| 10 | Random chart-review validation performed on sample | |
| 11 | PHI/de-identification check completed | |
| 12 | Output metadata header includes all required fields | |
| 13 | Results reviewed by clinical SME before release | |
| 14 | Known data quality limitations disclosed in output | |

---

## Guidelines

- Always query through the CDM vocabulary layer — never hard-code source codes in OMOP or i2b2 queries
- Treat every ETL as lossy until proven otherwise; validate before trusting transformed data
- Use the OHDSI Data Quality Dashboard or equivalent profiling tool on every new data source
- Document the exact vocabulary version and ETL date in every output artifact
- Never conflate prescribing data with dispensing data — they answer different clinical questions
- Build concept sets incrementally and review with a clinician; automated descendant expansion introduces false positives
- Apply the minimum necessary standard — extract only the columns and rows needed for the analysis
- When results seem too clean or too large, investigate before celebrating — CDW artifacts are more common than genuine signals
