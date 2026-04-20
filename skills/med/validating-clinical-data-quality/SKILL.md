---
name: validating-clinical-data-quality
language: en
description: Structures data quality assessment with completeness, accuracy, and consistency validation. Use when auditing clinical data, assessing data quality, or validating data integrity.
tags:
  - validation
  - health-informatics
  - clinical
  - audit
metadata:
  author: casemark
  practice_areas:
    - Health Informatics
    - Health IT
    - Clinical Informatics
  document_types:
    - Validation Report
  skill_modes:
    - Validation
---

# Validating Clinical Data Quality

Structures data quality assessment across the dimensions of completeness, accuracy, consistency, timeliness, and conformance for clinical datasets derived from EHRs, claims, registries, and health information exchanges. This skill applies frameworks from AHIMA, AMIA, and ONC data quality guidance.

## Why This Skill Exists

Clinical data drives patient safety decisions, quality measurement, reimbursement, research, and regulatory compliance. Poor data quality cascades: an incorrect allergy code triggers false CDS alerts; incomplete problem lists undercount chronic disease for risk adjustment; inconsistent lab units cause misinterpreted results. Organizations that fail to systematically validate clinical data quality face CMS audit findings, inaccurate Hierarchical Condition Category (HCC) risk scores, flawed research conclusions, and patient safety events. This skill provides a repeatable framework for data quality validation that can be applied to any clinical dataset.

---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Dataset under review** --- What clinical dataset is being validated? (EHR production database, clinical data warehouse extract, registry submission, FHIR API output, C-CDA document set)
2. **Data quality dimensions in scope** --- Which dimensions are being assessed? (Completeness, accuracy, consistency, timeliness, conformance, plausibility, uniqueness)
3. **Intended use of the data** --- What decisions will this data support? (Quality reporting, clinical care, research, payer submission, public health reporting)
4. **Source system(s)** --- Which systems generated the data? Are there known data quality issues documented by the source system team?
5. **Reference standard** --- What is the "truth" source for accuracy validation? (Chart review, external registry, reference lab, manual audit sample)
6. **Time frame** --- What date range does the dataset cover? When was the most recent ETL refresh?
7. **Regulatory context** --- Does validation support CMS quality reporting, ONC certification testing, HEDIS audit, or research IRB requirements?

### Required Documents

- Data dictionary defining all fields, data types, value domains, and required/optional status
- ETL specification documenting transformation rules from source to target
- Previous data quality assessment reports (for trend comparison)
- Reference standard dataset or chart review sample
- Known data quality issue log from the source system team
- Applicable data quality frameworks (AHIMA data quality model, Kahn harmonized DQ framework)

---

## Step 1 --- Assess Completeness

Measure the presence of expected data elements:

- **Element-level completeness** --- For each field, calculate: (non-null records / total records) x 100. Flag fields below 80% completeness for investigation
- **Record-level completeness** --- Assess whether each patient record contains the minimum required data elements for its intended use (e.g., a quality measure denominator patient missing the required lab result)
- **USCDI completeness** --- For FHIR or C-CDA datasets, validate presence of all USCDI v4 required data classes: Patient Demographics (name, DOB, sex, race, ethnicity, preferred language), Problems, Medications, Allergies, Lab Results, Vital Signs, Procedures, Immunizations, Clinical Notes
- **Temporal completeness** --- Check for gaps in time-series data (e.g., missing months of lab results that suggest an ETL pipeline interruption rather than a clinical absence)
- **Expected-value completeness** --- For elements with known expected values (e.g., every inpatient encounter should have a discharge disposition), measure the rate of missing values

---

## Step 2 --- Validate Accuracy

Compare data values against a reference standard:

- **Manual chart review sampling** --- Select a stratified random sample (minimum 30 records per data category) for chart review. Compare coded data against the source clinical documentation
- **External reference validation** --- Cross-reference against authoritative external sources: immunization registries, state death indexes, lab reference values, pharmacy dispensing records
- **Code accuracy** --- Verify that coded data (ICD-10-CM, SNOMED CT, LOINC, RxNorm) correctly represents the clinical concept documented in the source record. Check for common miscoding patterns:
  - Specificity errors (ICD-10-CM E11.9 used when E11.65 retinopathy documentation exists)
  - Laterality omissions (ICD-10-CM codes missing 7th character)
  - Mapping errors from legacy codes during system migration
- **Value plausibility** --- Apply physiological plausibility checks: systolic BP 40-300 mmHg, heart rate 20-250 bpm, temperature 90-110 F, hemoglobin 2-20 g/dL, glucose 20-1500 mg/dL. Values outside these ranges are likely data errors
- **Identity accuracy** --- Validate patient matching accuracy by comparing demographics across merged records. Incorrect MRN merges create composite patient records with mixed clinical data

---

## Step 3 --- Check Consistency

Identify contradictions within and across data elements:

- **Intra-record consistency** --- Check for contradictions within a single record: male patient with pregnancy diagnosis, age 5 with Medicare insurance, deceased patient with future appointments
- **Cross-system consistency** --- Compare overlapping data elements across source systems: medication list in EHR vs. pharmacy dispensing system, diagnosis codes in EHR vs. claims
- **Temporal consistency** --- Verify that time-ordered events are logically sequenced: admission before discharge, order before result, birth before death, diagnosis before treatment
- **Referential integrity** --- Confirm that foreign key relationships are valid: every encounter references a valid patient, every result references a valid order, every medication references a valid prescriber
- **Terminology consistency** --- Ensure the same clinical concept is coded consistently across records. A patient with "Type 2 diabetes" should not have both E11.9 and E13.9 (other specified diabetes) in the same problem list

---

## Step 4 --- Measure Timeliness and Currency

Assess whether data is available when needed:

- **Data latency** --- Measure the time gap between clinical event and data availability in the target system. For quality reporting, lab results must be available within 24-48 hours of collection
- **ETL pipeline monitoring** --- Track ETL job execution times, success/failure rates, and data freshness indicators. An ETL job that ran but processed zero records indicates a silent failure
- **Result turnaround** --- For lab data specifically, measure the distribution of collection-to-result times. Outliers beyond normal TAT indicate data pipeline delays, not lab processing issues
- **Currency assessment** --- For standing data (problem lists, medication lists, allergy lists), assess the last-reviewed date. Problem lists not reviewed in > 12 months may contain outdated entries

---

## Step 5 --- Validate Conformance

Ensure data conforms to specified formats and standards:

- **Schema validation** --- Validate data against the target schema: correct data types (dates as dates, codes as codes), field length constraints, required field presence
- **Terminology conformance** --- Verify all coded values are members of the specified code system and version. An ICD-10-CM code not in the current FY release indicates a data error or version mismatch
- **FHIR resource validation** --- For FHIR outputs, validate against applicable profiles (US Core, Da Vinci) using the HL7 FHIR Validator. Check Must Support elements, required bindings, and cardinality constraints
- **C-CDA validation** --- Validate C-CDA documents against schema (XSD), Schematron rules, and vocabulary value set bindings using the ONC C-CDA Reference Validator
- **Value set conformance** --- For quality measure data, verify that all coded values fall within the measure's specified VSAC value sets

---

## Step 6 --- Produce the Data Quality Report

Structure the deliverable for action:

- **Dashboard summary** --- Overall DQ score by dimension, trend over time, comparison against benchmarks or previous assessment
- **Issue catalog** --- Each finding documented with: dimension, severity (critical/major/minor), affected field, affected record count, example records, root cause analysis, and recommended remediation
- **Root cause classification** --- Categorize issues: source system entry error, ETL transformation bug, terminology mapping error, system interface failure, documentation practice gap
- **Remediation roadmap** --- Prioritized action plan with responsible owner, target date, and expected impact on the DQ score
- **Re-assessment schedule** --- Define when each DQ dimension will be reassessed (e.g., completeness monthly, accuracy quarterly via chart review)

---

## Checkpoint B --- Validation Review

Before releasing the data quality assessment:

- [ ] All DQ dimensions in scope have been assessed with documented methodology
- [ ] Sample sizes meet statistical minimum for accuracy validation (30+ per category)
- [ ] Plausibility checks cover all numeric clinical data fields
- [ ] Consistency checks include both intra-record and cross-system comparisons
- [ ] Root causes are identified for all critical and major findings
- [ ] Remediation recommendations are specific and assigned to owners
- [ ] Report includes limitations of the DQ assessment itself
- [ ] Comparison to previous DQ assessment is included (if available)

---

## Quality Audit

- [ ] DQ dimensions align with a recognized framework (Kahn harmonized model, AHIMA, ISO 25012)
- [ ] Reference standard for accuracy validation is documented and justified
- [ ] Chart review methodology follows accepted sampling protocols
- [ ] USCDI v4 data class completeness is assessed for interoperability-destined data
- [ ] FHIR and C-CDA validation uses current version validators and profiles
- [ ] Terminology conformance checks cover all coded data elements
- [ ] Timeliness metrics are baselined for ongoing monitoring
- [ ] DQ findings are severity-classified with consistent criteria
- [ ] Report is version-dated and archived for trend analysis

---

## Guidelines

- Data quality is not a one-time project; it is an ongoing operational function. Build DQ checks into ETL pipelines as automated gates, not post-hoc manual reviews
- Never assume completeness means accuracy. A field that is 100% populated may be 100% populated with default values that do not reflect clinical reality
- Prioritize DQ dimensions by the data's intended use: accuracy matters most for clinical care decisions; completeness matters most for population health analytics; timeliness matters most for CDS
- Use the data quality issue log as a feedback mechanism to source system teams. Persistent problems in the CDW often originate from upstream documentation or configuration issues
- For quality measure data, validate against the specific eCQM value sets in VSAC. A clinically correct code that is not in the measure's value set will produce an incorrect quality score
- Distinguish between data quality issues and data governance issues. DQ is about the data values; governance is about policies, roles, and processes. Both are needed, but they require different interventions
- Document all exclusions from the DQ assessment (e.g., "records from System X were excluded due to known ETL migration in progress"). Undocumented exclusions create blind spots
- Treat critical DQ findings (identity errors, medication accuracy issues) as patient safety concerns requiring immediate escalation, not routine reporting cycle resolution
