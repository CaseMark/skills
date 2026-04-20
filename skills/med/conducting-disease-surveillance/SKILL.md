---
name: conducting-disease-surveillance
language: en
description: Structures disease surveillance systems with case definitions, reporting requirements, and trend analysis. Use when monitoring disease trends, managing surveillance data, or analyzing reportable conditions.
tags:
  - process
  - public-health
metadata:
  author: casemark
  practice_areas:
    - Public Health
    - Epidemiology
    - Preventive Medicine
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---

# Conducting Disease Surveillance

## Why This Skill Exists

Disease surveillance is the backbone of public health action. Without systematic, continuous collection, analysis, and interpretation of health-related data, jurisdictions cannot detect outbreaks, measure disease burden, evaluate intervention effectiveness, or allocate resources rationally. CDC's National Notifiable Diseases Surveillance System (NNDSS) mandates reporting for over 120 conditions, and every state/territory operates its own legally defined reportable conditions list. This skill provides the structured workflow an agent needs to stand up, operate, or audit a surveillance system that meets CSTE position statements, NNDSS technical requirements, and PHAB Domain 2 accreditation standards.


The COVID-19 pandemic exposed critical weaknesses in U.S. disease surveillance infrastructure: fragmented data systems, inconsistent electronic laboratory reporting, delayed case reporting, and inadequate workforce capacity. The CDC's Data Modernization Initiative (DMI) and the Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) standards are driving modernization. Electronic Case Reporting (eCR) via the eICR standard (HL7 CDA) is replacing manual provider reporting for an expanding list of conditions.
---

## Checkpoint A — Intake and Scoping

Before any surveillance activity begins, confirm the following with the requesting epidemiologist or health officer:

### Intake Questions

1. What condition(s) or syndrome(s) are under surveillance? List ICD-10-CM codes if available.
2. Is this passive surveillance (provider-reported), active surveillance (health department–initiated), sentinel surveillance, or syndromic surveillance?
3. What is the jurisdictional authority — state, tribal, local, or territorial (STLT)?
4. Which case definition applies — CSTE/CDC standard, or a jurisdiction-specific variant?
5. What electronic laboratory reporting (ELR) feeds are in place? HL7 2.5.1 or FHIR-based?
6. What is the reporting timeframe — immediate (within 24 hours), weekly, or monthly?
7. Is this surveillance linked to a specific grant (e.g., ELC, PHEP, STD Prevention)?
8. Who are the end users of the surveillance outputs — state epidemiologist, CDC program, local health officer?

### Required Documents

- Current CSTE case definition for the target condition(s)
- Jurisdiction's list of reportable conditions with timelines
- Data-use agreements (DUAs) covering lab and clinical data feeds
- Data dictionary for the surveillance information system (e.g., NBS, MAVEN, ESSENCE)
- Prior MMWR or state epi reports for baseline comparison
- Organizational chart showing reporting chain from provider to STLT to CDC

---

## Step 1 — Establish or Verify Case Definitions

Apply the CSTE/CDC case classification hierarchy exactly:

- **Suspected**: Clinical criteria met without laboratory confirmation.
- **Probable**: Clinical criteria met plus epidemiologic linkage OR use of a supportive lab test.
- **Confirmed**: Laboratory-confirmed with an approved diagnostic method per CSTE position statement.

For syndromic surveillance (e.g., via ESSENCE or BioSense Platform), define the syndrome query using chief-complaint free-text terms, ICD-10 discharge codes, or a combination. Document the query logic verbatim.

Cross-check the case definition vintage. CSTE updates position statements annually; confirm the active year. A mismatched definition produces incomparable trend data.


### Case Classification Reference for Common Conditions

| Condition | Confirmed Criteria | Probable Criteria | Reporting Timeline |
|---|---|---|---|
| COVID-19 | Positive NAAT or antigen + clinical criteria | Clinical criteria + epi link | Within 24 hours |
| Mpox | Orthopoxvirus PCR positive | Clinically compatible + epi link | Within 24 hours |
| Tuberculosis | Culture positive M. tuberculosis | AFB smear positive + clinical | Within 1 business day |
| Measles | IgM positive or culture/PCR | Clinical criteria + epi link | Immediately |
| Salmonellosis | Culture or CIDT positive | Clinical + epi link | Within 1 business day |
| Hepatitis C (acute) | IgM anti-HCV or seroconversion | ALT elevation + epi link | Within 1 business day |
---

## Step 2 — Map Data Flows and Reporting Pathways

Document the complete data pipeline:

1. **Source** — Laboratories (ELR via HL7 messages), hospitals (syndromic via ADT feeds), providers (case report forms).
2. **Transmission** — PHIN Messaging System (PHIN MS), state health information exchange (HIE), or manual entry.
3. **Staging** — Jurisdiction surveillance information system (NBS, MAVEN, Epi-Trax, NEDSS Base System).
4. **Deduplication** — Match algorithm (deterministic vs. probabilistic) applied before case counting.
5. **Transmission to CDC** — NNDSS case notification via Message Mapping Guides (MMGs) per condition.
6. **Feedback loop** — CDC publishes provisional counts in MMWR weekly tables; jurisdiction reconciles.

Flag any segment that is manual, delayed, or known to have data quality issues.

---

## Step 3 — Collect and Validate Surveillance Data

For each reporting period:

- Pull case notifications from the surveillance system.
- Validate completeness: percent of required fields populated (target ≥ 90% for key variables).
- Validate timeliness: median days from specimen collection to case notification at CDC (benchmark varies by condition; for immediately notifiable conditions, target < 24 hours).
- Run deduplication logic and document duplicates removed.
- Apply case classification algorithm — assign Confirmed, Probable, Suspected, or Not a Case.
- Reconcile with laboratory data: match positive lab results to case reports; flag orphan labs (lab-confirmed positives with no matching case report).

- **Electronic Case Reporting (eCR)** --- For conditions with eCR implementation, verify: EHR trigger codes are configured per RCTC (Reportable Conditions Trigger Codes) value set, eICR messages are generated and transmitted to the AIMS platform, and reportability response (RR) messages are processed by the EHR. eCR reduces manual reporting burden and improves timeliness
---

## Step 4 — Analyze Trends and Generate Surveillance Outputs

Produce the standard epidemiologic outputs:

- **Person**: Age, sex, race/ethnicity distributions. Use BRFSS or Census denominators for rate calculation.
- **Place**: County-level or census-tract maps. Use CDC WONDER or EpiInfo for mapping.
- **Time**: Epidemic curves (epi curves) by week of onset. Calculate 5-year rolling averages for seasonal conditions.
- **Rates**: Incidence rate = (new cases / population at risk) × 100,000. Age-adjust using 2000 U.S. standard population where appropriate.
- **Trends**: Compare current period to prior 5-year mean with 95% confidence intervals. Flag exceedances using Poisson or negative binomial thresholds (as implemented in Farrington algorithm or CDC EARS methods C1/C2/C3).

Generate MMWR-style summary tables with case counts by jurisdiction and time period.

- **Genomic surveillance integration** --- For conditions with sequencing programs (COVID-19, influenza, TB, STIs with AMR), integrate genomic data with epidemiologic surveillance: link sequence data to case records, use phylogenetic analysis to identify transmission clusters, and report variant proportions alongside case counts
---

## Step 5 — Disseminate Findings and Act

- Produce surveillance summary reports for internal stakeholders at required cadence (weekly, monthly, annual).
- For notifiable conditions, ensure timely transmission to CDC per MMG specifications.
- When aberration detection flags a signal, trigger the outbreak investigation protocol (see skill: investigating-disease-outbreaks).
- Publish annual surveillance summaries aligned with MMWR Summary of Notifiable Diseases format.
- Feed surveillance data into Community Health Assessments (CHAs) and Community Health Improvement Plans (CHIPs) for PHAB accreditation.

- **Data modernization alignment** --- Align surveillance system improvements with CDC's Data Modernization Initiative priorities: cloud-based infrastructure, automated data pipelines, FHIR-based data exchange, real-time analytics dashboards, and interoperable systems that reduce manual data entry and reconciliation
---

## Checkpoint B — Surveillance System Review

Before finalizing any surveillance output or system change, verify:

- [ ] Case definitions match current CSTE position statement year.
- [ ] Data completeness exceeds 90% for key demographic and clinical fields.
- [ ] Timeliness metrics meet jurisdictional benchmarks (documented).
- [ ] Deduplication was applied and duplicate counts are logged.
- [ ] Aberration detection algorithm ran for the current period with results documented.
- [ ] Outputs have been reviewed by the supervising epidemiologist or state epi.
- [ ] Provisional vs. final case status is clearly labeled on all tables and reports.
- [ ] Data suppression rules applied for cell sizes < 5 to protect confidentiality.

- [ ] Electronic Case Reporting (eCR) is operational for applicable conditions with trigger codes configured
- [ ] Genomic surveillance data is integrated with epidemiologic case data (if applicable)
- [ ] Surveillance system modernization plan aligns with CDC DMI priorities
---

## Quality Audit

- [ ] NNDSS Message Mapping Guide version matches the condition being reported
- [ ] Case classification applied uniformly — no ad hoc reclassifications without documented rationale
- [ ] Denominator source documented (Census vintage, intercensal estimate, or BRFSS)
- [ ] Rate calculations use consistent population-at-risk definition across periods
- [ ] Orphan lab reports investigated and resolved or documented as unresolvable
- [ ] Surveillance system evaluated using CDC Updated Guidelines for Evaluating Public Health Surveillance Systems (MMWR 2001; 50(RR-13)) — attributes: simplicity, flexibility, data quality, acceptability, sensitivity, predictive value positive, representativeness, timeliness, stability
- [ ] Electronic reporting infrastructure tested per PHIN certification requirements
- [ ] All outputs marked DRAFT until epidemiologist sign-off

- [ ] eCR trigger codes match current RCTC value set version
- [ ] Genomic sequencing results are linked to epidemiologic case records for applicable conditions
- [ ] Surveillance data modernization roadmap documents planned improvements with timeline
- [ ] Syndromic surveillance queries are validated against known outbreak events for sensitivity assessment
---

## Guidelines

- Never release case-level data without verifying jurisdiction-specific confidentiality statutes and IRB/privacy board approval.
- Distinguish clearly between provisional and final counts in all outputs. Provisional data may change as case investigations close.
- When surveillance data is used for resource allocation, note the lag between event and report (reporting delay) and adjust projections accordingly.
- If a new condition is added to the reportable list, allow at least two reporting cycles before interpreting trends — initial spikes often reflect catch-up reporting, not true incidence increase.
- Syndromic surveillance signals require epidemiologic confirmation before public communication. False-positive rates in syndromic systems are high.
- Always cite the data source, extraction date, and case definition year in every table and figure.
- Escalate to human epidemiologist review whenever: aberration detection fires, a novel pathogen is suspected, or case counts in a single jurisdiction exceed 2 standard deviations above the 5-year mean.

- Electronic Case Reporting (eCR) is the future of disease surveillance. Jurisdictions should prioritize eCR implementation over manual case report form submission for all conditions in the RCTC trigger code set. eCR improves timeliness from days to hours.
- Genomic surveillance is now integral to communicable disease epidemiology. Whole-genome sequencing adds transmission network analysis and antimicrobial resistance tracking that traditional epidemiology alone cannot provide.