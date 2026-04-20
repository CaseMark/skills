---
name: investigating-disease-outbreaks
language: en
description: Guides outbreak investigation using CDC steps with case definition, epidemiologic curve, and control measures. Use when investigating outbreaks, analyzing epidemic curves, or implementing control measures.
tags:
  - investigation
  - public-health
metadata:
  author: casemark
  practice_areas:
    - Public Health
    - Epidemiology
    - Preventive Medicine
  document_types:
    - Investigation Report
  skill_modes:
    - Investigation
---

# Investigating Disease Outbreaks

## Why This Skill Exists

Outbreak investigation is the field-defining discipline of applied epidemiology. The CDC's 10-step outbreak investigation framework — codified in MMWR's Principles of Epidemiology in Public Health Practice and operationalized through EIS training — is the gold standard. Delays in investigation directly translate to additional cases, hospitalizations, and deaths. This skill provides the structured protocol an agent needs to support an epidemiologist through the complete arc of a field investigation, from initial report through final MMWR publication.

---

## Checkpoint A — Intake and Scoping

### Intake Questions

1. What is the initial report — who reported, when, and what was the clinical presentation?
2. How many cases are currently identified, and over what time period?
3. What is the geographic scope — single facility, community, multi-jurisdictional?
4. Has a pathogen been identified or suspected? Any lab results available?
5. Are control measures already in place (isolation, quarantine, facility closure)?
6. What is the jurisdiction's legal authority for investigation (state epi authority statute)?
7. Is multi-jurisdictional coordination needed (PulseNet, CaliciNet, CDC Emergency Operations Center)?
8. Are there environmental samples or food specimens available for testing?

### Required Documents

- Initial case reports or line listing (even if preliminary)
- Laboratory results (culture, PCR, whole-genome sequencing data if available)
- Facility inspection reports (if foodborne or healthcare-associated)
- Syndromic surveillance alerts that triggered the investigation
- Prior outbreak reports for the same pathogen or setting in the jurisdiction
- Institutional Review Board (IRB) exemption documentation for emergency investigation

---

## Step 1 — Verify the Diagnosis and Confirm the Outbreak

Before mobilizing resources, verify that cases are real and that the observed number exceeds the expected background rate.

- Confirm clinical diagnoses with laboratory evidence where possible.
- Compare current case count to historical baseline for the same condition, place, and time period (use 5-year weekly average from surveillance data).
- Distinguish a true outbreak from a surveillance artifact (change in reporting practices, new lab test deployment, media-driven testing surge).
- Apply the operational definition: an outbreak exists when the observed number of cases exceeds the expected number for the given place and time.

If confirmed, formally declare the investigation and notify the state epidemiologist and CDC program (if nationally notifiable).

---

## Step 2 — Establish a Case Definition

Construct a case definition with four components:

- **Clinical criteria**: Signs, symptoms, and their required duration or severity.
- **Laboratory criteria**: Specific tests and result thresholds (e.g., culture-confirmed Salmonella Enteritidis; PCR Ct value ≤ 35 for SARS-CoV-2).
- **Epidemiologic criteria**: Time, place, and person linkage (e.g., ate at Restaurant X between March 1–7).
- **Classification**: Confirmed, Probable, Suspected — tiered to allow early case capture while maintaining specificity.

Start broad (sensitive) in the early investigation phase. Narrow (specific) as the investigation matures and hypothesis-testing begins. Document every revision to the case definition with date and rationale.

---

## Step 3 — Find Cases and Build the Line Listing

Systematically identify all cases through:

- Active case finding: contact healthcare facilities, laboratories, and pharmacies in the affected area.
- Enhanced surveillance: alert providers via Health Alert Network (HAN) notification.
- Record review: search hospital discharge data, ED chief complaints, and poison control logs.
- Community outreach: for outbreaks in congregate settings, conduct symptom surveys.

Build a line listing with columns for: case ID, demographics (age, sex, race/ethnicity), onset date, symptoms, laboratory results, exposure history, hospitalization status, and outcome. This line listing is the analytic backbone of the investigation.

---

## Step 4 — Orient Data by Person, Place, and Time

**Person**: Calculate attack rates by age group, sex, occupation, and other relevant strata. Identify the population at highest risk.

**Place**: Plot case residences or exposure locations on a spot map. For foodborne outbreaks, map food distribution chains. For respiratory outbreaks, map seating charts or ventilation zones.

**Time**: Construct an epidemic curve (epi curve) with case counts by date or time of onset. The shape of the epi curve reveals:
- Point source: steep rise, tight peak, rapid decline.
- Propagated (person-to-person): successive waves separated by one incubation period.
- Continuous source: plateau pattern with ongoing exposure.
- Intermittent source: irregular peaks corresponding to exposure events.

Calculate the incubation period from the epi curve (median onset minus median exposure time) to narrow the pathogen hypothesis.

---

## Step 5 — Develop and Test Hypotheses

Generate hypotheses from descriptive epidemiology and test with analytic methods:

- **Cohort study** (when population at risk is defined, e.g., wedding attendees): Calculate relative risk (RR) for each exposure. Use chi-square or Fisher's exact test. Multivariable analysis with log-binomial or Poisson regression.
- **Case-control study** (when population at risk is undefined or large): Calculate odds ratios (OR) for each exposure. Match controls by age, sex, geography. Use conditional logistic regression for matched designs.
- Integrate laboratory evidence: PFGE, WGS (whole-genome sequencing), or cgMLST cluster analysis via PulseNet or state public health labs.
- Apply Hill's criteria for causation: strength, consistency, specificity, temporality, biological gradient, plausibility, coherence, experiment, analogy.

---

## Step 6 — Implement Control Measures

Do not wait for analytic confirmation to implement initial control measures. Control measures should be proportionate to the suspected source and transmission mode:

- **Source control**: Remove contaminated product (FDA recall), close implicated facility, treat contaminated water.
- **Transmission interruption**: Isolation of cases, quarantine of exposed contacts, enhanced hand hygiene, respiratory precautions.
- **Host protection**: Post-exposure prophylaxis, vaccination (ring vaccination for smallpox/Ebola), immune globulin.
- **Communication**: Issue public health advisories via HAN, coordinate with public information officer for media messaging.

Document control measures with dates of implementation and assessment of compliance.

---

## Step 7 — Communicate Findings

- Prepare an Epi-Aid trip report or outbreak investigation summary per CDC format.
- If publishable, draft for MMWR Morbidity and Mortality Weekly Report — including epi curve, attack rate table, analytic results, and control measures.
- Brief elected officials, facility administrators, and the public as appropriate through the jurisdiction's risk communication protocol.
- Enter final case data into NORS (National Outbreak Reporting System) for foodborne/waterborne, or NHSN for healthcare-associated outbreaks.

---

## Checkpoint B — Investigation Closure Review

- [ ] Case definition documented with revision history
- [ ] Line listing complete with all identified cases classified
- [ ] Epi curve generated with onset dates (not report dates)
- [ ] Analytic study completed with measures of association and confidence intervals
- [ ] Laboratory evidence linked to epidemiologic findings
- [ ] Control measures documented with implementation dates and effectiveness assessment
- [ ] NORS/NHSN/state outbreak database entry completed
- [ ] After-action review (AAR) conducted with investigation team
- [ ] Final report reviewed by supervising epidemiologist

---

## Quality Audit

- [ ] Case definition follows CSTE four-component structure (clinical, lab, epi, classification)
- [ ] Attack rates calculated with correct denominators (population at risk, not total population)
- [ ] Epi curve uses onset date, not report date, on the x-axis
- [ ] Analytic study design is appropriate for the outbreak setting (cohort vs. case-control)
- [ ] Confounders and effect modifiers addressed in analysis
- [ ] Control measures initiated before analytic confirmation where indicated by precautionary principle
- [ ] WGS/PFGE cluster data cited with BioNumerics or Enterobase analysis parameters
- [ ] All data points marked [VERIFY] have been resolved before final report
- [ ] Personally identifiable information (PII) redacted from all external communications

---

## Guidelines

- Never delay initial control measures while waiting for laboratory confirmation or analytic results. Precautionary action saves lives.
- Case definitions must evolve as the investigation progresses, but every revision must be documented with the date, rationale, and impact on case counts.
- Epi curves should always use date of symptom onset. Using report date introduces reporting artifacts that distort the curve shape.
- For multi-jurisdictional outbreaks, coordinate through CDC's Emergency Operations Center and use standardized line listing templates to ensure cross-jurisdictional comparability.
- When whole-genome sequencing is available, integrate allele-difference thresholds (typically 0-7 alleles for Salmonella, 0-3 for Listeria) into the case definition for confirmed cluster membership.
- All outbreak investigation records are subject to state public records laws. Consult legal counsel before releasing records that may contain PII or proprietary facility information.
- Escalate to senior epidemiologist or CDC field assistance when: pathogen is novel, case fatality rate exceeds historical norms, attack rate suggests ongoing uncontrolled transmission, or multi-state spread is identified.
