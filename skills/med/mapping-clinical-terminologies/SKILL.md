---
name: mapping-clinical-terminologies
description: Maps between clinical terminologies (ICD-10, SNOMED CT, LOINC, RxNorm) with semantic equivalence validation. Use when mapping medical codes, converting between terminologies, or validating code mappings.
tags:
  - analysis
  - health-informatics
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Health Informatics
    - Health IT
    - Clinical Informatics
  document_types:
    - Mapping Document
  skill_modes:
    - Analysis
    - Mapping
---

# Mapping Clinical Terminologies

Maps between clinical terminologies (ICD-10, SNOMED CT, LOINC, RxNorm) with semantic equivalence validation. This skill ensures that coded clinical data retains its meaning when translated across terminology systems used in EHRs, claims processing, quality reporting, and clinical research.

## Why This Skill Exists

Healthcare systems use multiple overlapping terminology standards. A single patient encounter may require ICD-10-CM codes for billing, SNOMED CT concepts for clinical documentation, LOINC codes for lab results, and RxNorm CUIs for medication reconciliation. Incorrect mappings cause claim denials, corrupted research datasets, patient safety events from misidentified allergies, and USCDI non-compliance. This skill provides a structured approach to cross-terminology mapping that preserves clinical semantics and flags cases requiring human adjudication.

---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Source terminology and version** --- Which system are you mapping from? (e.g., SNOMED CT International Edition 2024-01-01, ICD-10-CM FY2024, LOINC 2.77, RxNorm 2024-AA)
2. **Target terminology and version** --- Which system is the destination?
3. **Concept scope** --- How many source codes require mapping? Is this a full value-set or a targeted subset?
4. **Use-case context** --- Is the mapping for billing/claims, clinical decision support, quality measurement (eCQM), research cohort identification, or USCDI data exchange?
5. **Directionality** --- Is the mapping one-way or bidirectional? Bidirectional maps require independent validation in each direction.
6. **Existing map sets** --- Are there available crosswalks (UMLS, NLM VSAC value sets, WHO mapping tables, GEMs for ICD-9 to ICD-10)?
7. **Governance requirements** --- Does the organization require mapping committee review? What is the approval workflow?

### Required Documents

- Source code list with descriptions (spreadsheet or FHIR ValueSet)
- Target terminology browser access (UMLS Metathesaurus, SNOMED CT Browser, LOINC search)
- Any prior mapping files or crosswalk tables
- Business rules document specifying mapping constraints
- Value set definition if targeting eCQM or HEDIS measures

---

## Step 1 --- Profile Source Concepts

For each source code, extract and document:

- **Code identifier** --- The alphanumeric code (e.g., SNOMED CT 73211009)
- **Preferred term** --- The FSN or preferred display name
- **Semantic category** --- SNOMED CT hierarchy position (Clinical Finding, Procedure, Observable Entity), ICD-10 chapter, LOINC class
- **Concept status** --- Active, inactive, or deprecated. Inactive SNOMED concepts must be mapped to their replacement per the component history table
- **Defining relationships** --- For SNOMED CT, capture the is-a hierarchy, finding site, associated morphology, and causative agent attributes
- **Context dependencies** --- Does meaning change with context (e.g., SNOMED CT "suspected" qualifier vs. confirmed diagnosis)?

Flag any source codes that are pre-coordinated expressions requiring post-coordinated decomposition in the target system.

---

## Step 2 --- Identify Candidate Targets

For each source concept, generate candidate mappings using:

1. **UMLS Metathesaurus lookup** --- Search by CUI to find atoms in the target system. Record the CUI, target code, term type (PT, SY, SN), and source asserted relationship
2. **NLM VSAC value sets** --- Check if the concept appears in existing value sets that already establish the mapping context
3. **Lexical matching** --- Normalized string matching between source and target preferred terms. Use word-boundary tokenization, not substring matching
4. **Semantic matching** --- Compare defining attributes. For SNOMED-to-ICD-10, use the SNOMED CT to ICD-10-CM map maintained by NLM (released with each SNOMED CT US Edition)
5. **Hierarchical navigation** --- When no exact match exists, traverse the is-a hierarchy in the target system to find the closest ancestor or narrower concept

Document all candidates per source code. Minimum two candidates when available.

---

## Step 3 --- Classify Map Relationships

Assign an equivalence type to each candidate mapping per ISO 12300 map relationship categories:

| Equivalence Type | Definition | Action Required |
|---|---|---|
| Exact (1:1) | Identical clinical meaning in both systems | Accept with documentation |
| Broader (source narrower) | Target concept is more general | Document information loss; flag for CDS impact |
| Narrower (source broader) | Target concept is more specific | Requires disambiguation rules or human selection |
| Partial overlap | Concepts share some but not all meaning | Map with qualifier documentation |
| No match | No semantically acceptable target | Create local extension code or escalate |

For SNOMED CT to ICD-10-CM specifically, apply GEM (General Equivalence Mappings) relationship flags: approximate, no map, combination required, or choice list.

---

## Step 4 --- Apply Mapping Rules

Execute rule-based resolution for non-exact mappings:

- **One-to-many splits** --- When a single source code maps to multiple target codes (common in SNOMED-to-ICD-10), define the selection criteria. Prioritize by: (a) clinical specificity, (b) laterality preservation, (c) episode-of-care alignment
- **Many-to-one merges** --- When multiple source codes collapse to one target, document which distinctions are lost and whether downstream processes depend on them
- **Context-dependent rules** --- Apply map advice from the SNOMED CT map (e.g., "Map of source concept is context dependent" requires encounter-level data to resolve)
- **Gender/age constraints** --- ICD-10-CM codes with gender-specific or age-specific edit rules must be validated against the patient population
- **Laterality handling** --- SNOMED CT laterality attributes must propagate to ICD-10-CM 7th character or laterality-specific codes

---

## Step 5 --- Validate Semantic Preservation

Run validation checks on the completed mapping set:

1. **Round-trip test** --- Map source-to-target, then target-to-source using the reverse crosswalk. Concepts that fail round-trip have semantic drift; document the variance
2. **Hierarchy consistency** --- If source code A is-a source code B, then target(A) should be-a target(B) or the mapping breaks hierarchical inference
3. **Value set integrity** --- Confirm mapped codes are members of required value sets (e.g., VSAC value sets for eCQMs). A valid SNOMED code mapped to an ICD-10 code not in the denominator value set will break measure calculation
4. **Clinical review sampling** --- Select 10-15% of mappings stratified by equivalence type for clinical informaticist review. 100% review for "no match" and "partial overlap" categories
5. **Negation and qualifier check** --- Ensure negated concepts (e.g., "No evidence of malignancy") do not map to positive assertion codes

---

## Step 6 --- Build the Mapping Artifact

Structure the final deliverable:

- **Format** --- FHIR ConceptMap resource (preferred for interoperability), CSV crosswalk, or Excel with structured columns
- **Required columns** --- Source system, source version, source code, source display, target system, target version, target code, target display, equivalence type, map advice, reviewer, review date, status (draft/active/retired)
- **Provenance** --- Record the mapping method (automated UMLS lookup, manual clinical review, NLM-published map)
- **Version control** --- Tag the map with source and target terminology release dates. Maps expire when either terminology updates

---

## Checkpoint B --- Mapping Review

Before releasing the mapping artifact:

- [ ] Every source code has at least one target or is explicitly flagged "no map" with justification
- [ ] All "no match" codes have been escalated to the terminology governance committee
- [ ] Equivalence types are assigned for every mapping pair
- [ ] Round-trip validation has been run and exceptions documented
- [ ] Clinical reviewer has signed off on the sampled subset
- [ ] FHIR ConceptMap validates against the R4 specification (if applicable)
- [ ] Map advice text is present for all non-exact mappings

---

## Quality Audit

- [ ] Source terminology version matches the current production system version
- [ ] Target terminology version matches the receiving system version
- [ ] No deprecated or inactive codes appear in the target column without replacement documentation
- [ ] Mapping covers 100% of source codes in scope
- [ ] Semantic equivalence classifications follow ISO 12300 categories consistently
- [ ] Gender/age-specific ICD-10-CM codes are validated against applicable patient population
- [ ] Value set membership is confirmed for all eCQM-relevant mappings
- [ ] Map artifact is version-tagged with date and terminology edition identifiers
- [ ] Clinical review coverage meets the minimum 10% sample threshold

---

## Guidelines

- Use UMLS as the primary cross-reference backbone; do not rely on display-name string matching as primary evidence
- Treat the NLM-published SNOMED CT to ICD-10-CM map as authoritative when available; document deviations explicitly
- Never assume bidirectional equivalence from a unidirectional map. SNOMED 73211009 (Diabetes mellitus) maps to multiple ICD-10 codes; the reverse path is not 1:1
- Flag all approximate mappings for downstream CDS and analytics teams so they can apply compensating logic
- Re-validate mappings on every terminology release cycle (SNOMED CT: biannual US Edition; ICD-10-CM: annual October updates; LOINC: biannual; RxNorm: monthly)
- For RxNorm mappings, distinguish between SCD (Semantic Clinical Drug), SBD (Semantic Branded Drug), and GPCK (Generic Pack) term types --- mapping at the wrong level introduces prescribing errors
- Maintain a mapping exception log for concepts that require ongoing committee review
- Comply with USCDI v4 terminology requirements when mappings support Cures Act data exchange
