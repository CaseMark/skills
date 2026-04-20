---
name: managing-environmental-health-assessments
language: en
description: Structures environmental health evaluations with exposure assessment and risk communication. Use when assessing environmental health risks, evaluating contamination, or communicating environmental findings.
tags:
  - management
  - public-health
  - risk
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Public Health
    - Epidemiology
    - Preventive Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Environmental Health Assessments

## Why This Skill Exists

Environmental health assessments evaluate how chemical, physical, and biological agents in the environment affect human health. When a community is exposed to contaminated drinking water, air pollution from industrial facilities, lead in housing, or a hazardous waste site, the public health response requires a structured evaluation of exposure pathways, dose-response relationships, and population risk — followed by clear risk communication. The Agency for Toxic Substances and Disease Registry (ATSDR) Public Health Assessment (PHA) framework, EPA's human health risk assessment paradigm (1983 NRC Red Book), and state environmental health programs provide the authoritative methodology. Errors in environmental health assessment can result in either unnecessary panic (overestimating risk) or preventable illness (underestimating exposure). This skill codifies the structured approach for managing these assessments.

---

## Checkpoint A — Intake and Scoping

### Intake Questions

1. What is the environmental concern — contaminated site, air quality complaint, water quality issue, occupational exposure, or consumer product?
2. What contaminants are known or suspected? Are there analytical results (environmental sampling, biomonitoring)?
3. What is the exposed population — residents, workers, children, pregnant women, recreational users?
4. Is this assessment triggered by a regulatory requirement (CERCLA/Superfund, RCRA, Safe Drinking Water Act), a community complaint, or a disease cluster investigation?
5. What is the geographic extent of potential contamination — single property, neighborhood, plume extent, watershed?
6. Is ATSDR involved or has a PHA been requested (Congressional mandate, community petition, EPA referral)?
7. What exposure pathways are potentially complete — ingestion, inhalation, dermal contact?
8. What community engagement has occurred to date?

### Required Documents

- Environmental sampling data (soil, water, air, biota) with chain-of-custody documentation
- Site characterization report or Remedial Investigation (RI) from EPA/state environmental agency
- ATSDR Toxicological Profiles for identified contaminants
- EPA Integrated Risk Information System (IRIS) values for reference doses (RfD) and cancer slope factors
- Biomonitoring data if available (blood lead levels, urinary metabolites)
- Demographic profile of the potentially exposed population (Census/ACS, SVI)
- Health outcome data for the community (cancer registry, vital records, hospital discharge)
- Community concerns documentation (complaint logs, meeting minutes, media coverage)

---

## Step 1 — Evaluate Exposure Pathways

For each contaminant, assess whether the exposure pathway is complete using the five-element model:

1. **Source**: Where does the contaminant originate (industrial facility, landfill, agricultural operation, natural deposit)?
2. **Environmental transport**: How does it move through the environment (groundwater flow, air dispersion, soil migration, surface water runoff)?
3. **Exposure point**: Where does human contact occur (drinking water well, residential soil, ambient air at property boundary, indoor air via vapor intrusion)?
4. **Route of exposure**: How does the contaminant enter the body (ingestion, inhalation, dermal absorption)?
5. **Receptor population**: Who is exposed (residents, workers, children playing in contaminated soil)?

Classify each pathway as:
- **Completed**: All five elements present — exposure is occurring or has occurred.
- **Potential**: Pathway could become complete if conditions change.
- **Eliminated**: One or more elements are absent and cannot become present.

Focus the assessment on completed and potential pathways.

---

## Step 2 — Estimate Exposure Doses

For each completed pathway, calculate the estimated exposure dose:

**Chronic Daily Intake (CDI)** = (Concentration × Intake Rate × Exposure Frequency × Exposure Duration) / (Body Weight × Averaging Time)

Use EPA Exposure Factors Handbook values for standard assumptions:
- Adult body weight: 80 kg; Child (1-6 years): 15 kg
- Drinking water ingestion: 2.5 L/day (adult), 0.78 L/day (child 1-6)
- Soil ingestion: 100 mg/day (adult), 200 mg/day (child)
- Inhalation rate: 16 m³/day (adult), 10 m³/day (child)
- Residential exposure frequency: 350 days/year
- Residential exposure duration: 26 years (adult), 6 years (child)

Compare calculated CDI to ATSDR Minimal Risk Levels (MRLs) and EPA Reference Doses (RfDs) for non-cancer effects.

For carcinogens, calculate excess lifetime cancer risk:
**Risk** = CDI × Cancer Slope Factor (CSF)
- Acceptable risk range: 1 × 10⁻⁶ to 1 × 10⁻⁴ (one in a million to one in ten thousand).

---

## Step 3 — Characterize Health Risk

Integrate exposure assessment with toxicological evidence:

- **Non-cancer hazard**: Calculate Hazard Quotient (HQ) = Exposure Dose / Reference Dose. HQ > 1 indicates potential for adverse non-cancer effects. Calculate Hazard Index (HI) = sum of HQs for all contaminants with same target organ.
- **Cancer risk**: Sum cancer risks across all pathways and contaminants. Total risk > 1 × 10⁻⁴ typically triggers remedial action under CERCLA.
- **Vulnerable populations**: Apply child-specific and pregnancy-specific exposure parameters. Lead exposure uses the Integrated Exposure Uptake Biokinetic (IEUBK) model for children.
- **Uncertainty**: Identify key sources of uncertainty — sampling representativeness, use of default exposure assumptions vs. site-specific data, toxicological data gaps, and synergistic effects of multiple contaminants.

Classify the site using ATSDR hazard categories:
- **Urgent Public Health Hazard**: Requires immediate action to prevent exposure.
- **Public Health Hazard**: Exposure at levels expected to cause adverse health effects.
- **Indeterminate Public Health Hazard**: Insufficient data.
- **No Apparent Public Health Hazard**: Exposure below concern levels.
- **No Public Health Hazard**: No exposure pathway.

---

## Step 4 — Communicate Risk to the Community

Environmental risk communication is a distinct discipline. Apply ATSDR/CDC communication principles:

- Present findings in plain language. Express risk in familiar terms (e.g., "The level of arsenic in your well water is 5 times higher than the safe drinking water standard" rather than "Arsenic exceeds the MCL of 10 μg/L").
- Acknowledge community concerns before presenting data. People process risk information through the filter of trust, fairness, and control.
- Distinguish between hazard (the property of a substance to cause harm) and risk (the probability of harm given actual exposure). A hazardous chemical with no complete exposure pathway poses no current risk.
- Provide actionable recommendations: what should residents do now (e.g., use bottled water, limit soil contact), what is the health department doing, and what is the timeline for remediation.
- Hold public availability sessions (not just one-way presentations). Allow open Q&A with technical staff available.
- Provide fact sheets in languages spoken by the community.

---

## Step 5 — Recommend Actions and Monitor

- For urgent hazards: recommend immediate exposure reduction (alternative water supply, relocation, access restriction).
- For non-urgent hazards: recommend remediation on a timeline consistent with risk level and regulatory framework.
- Establish a health monitoring plan: biomonitoring (blood/urine sampling), disease surveillance (cancer registry watch area), and environmental re-sampling schedule.
- Coordinate with EPA/state environmental agency for remedial action and ensure health department input into remedy selection.
- Track health outcomes in the exposed population over time. For cancer risks, monitoring may need to span decades.

---

## Checkpoint B — Assessment Completion Review

- [ ] All exposure pathways classified (completed, potential, eliminated) with rationale
- [ ] Exposure doses calculated using appropriate assumptions (site-specific preferred over defaults)
- [ ] Risk characterized with hazard quotients and cancer risk estimates
- [ ] ATSDR hazard category assigned with supporting evidence
- [ ] Community engagement conducted with plain-language communication
- [ ] Actionable recommendations provided for exposure reduction
- [ ] Monitoring plan established with indicators, frequency, and responsible parties
- [ ] Assessment reviewed by toxicologist or environmental health scientist

---

## Quality Audit

- [ ] Environmental sampling data meets QA/QC standards (chain of custody, method detection limits, field blanks, duplicates)
- [ ] Toxicological values sourced from ATSDR MRLs or EPA IRIS (not non-peer-reviewed sources)
- [ ] Exposure assumptions documented with source (EPA Exposure Factors Handbook edition, site-specific study)
- [ ] Child-specific exposure scenarios included for residential sites
- [ ] Uncertainty analysis addresses both exposure and toxicity uncertainties
- [ ] Risk communication materials reviewed for health literacy level (target: 6th-8th grade reading level)
- [ ] Environmental justice screening conducted (EJScreen or equivalent) to identify disproportionately affected communities
- [ ] Coordination with regulatory agencies documented

---

## Guidelines

- Never communicate environmental health risk using only numerical risk estimates (e.g., "1 × 10⁻⁵ lifetime cancer risk") without context. Numbers without narrative are meaningless to communities and invite misinterpretation.
- Default exposure assumptions overestimate risk by design (conservative/protective). When site-specific data are available, use them and explain the difference from default assumptions.
- Lead has no safe blood level in children. For lead exposure assessments, do not rely solely on comparison to the CDC blood lead reference value (3.5 μg/dL) — also assess the source and pathway for primary prevention.
- Environmental justice communities (low-income, minority, tribal) are disproportionately exposed to environmental hazards. Apply an equity lens to every assessment: who is most exposed, who has least capacity to mitigate, and who has historically been excluded from decision-making.
- When multiple contaminants are present, assess cumulative risk. Single-chemical assessment understates risk when communities face mixed exposures.
- Data gaps are inevitable. Document them explicitly, describe how they affect conclusions, and recommend actions to fill them. Never present an assessment as more certain than the data support.
- Escalate to ATSDR regional office or state toxicologist when: contaminant levels exceed action levels, a disease cluster is suspected in the exposed population, community conflict is escalating, or the site involves a contaminant without established toxicological values.
