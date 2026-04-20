---
name: conducting-health-equity-analyses
language: en
description: Analyzes health disparities with demographic stratification and equity-focused intervention planning. Use when analyzing health disparities, assessing equity, or designing health equity interventions.
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

# Conducting Health Equity Analyses

## Why This Skill Exists

Health equity — the principle that everyone has a fair and just opportunity to be as healthy as possible — is the central ethical commitment of public health. Disparities in health outcomes by race/ethnicity, socioeconomic status, geography, disability, sexual orientation, gender identity, and other social positions are well-documented, persistent, and largely attributable to structural factors rather than individual behavior. Healthy People 2030 defines achieving health equity as an overarching goal. CDC declared racism a serious public health threat in 2021. PHAB accreditation standards require health departments to assess and address health disparities. Yet many analyses that claim to address "equity" merely report stratified data without interrogating the structural causes, quantifying the gap, tracking progress, or designing interventions that target root causes. This skill provides the rigorous analytic framework needed to move beyond descriptive disparities to actionable equity analysis.

---

## Checkpoint A — Intake and Scoping

### Intake Questions

1. What health outcome(s) are being assessed for equity — mortality, morbidity, access to care, quality of care, health behaviors, or social determinants?
2. What dimensions of equity will be analyzed — race/ethnicity, income/poverty, education, geography (urban/rural, neighborhood), sex/gender, sexual orientation/gender identity, disability, immigration status, language?
3. What is the geographic scope — national, state, county, census tract, or neighborhood?
4. What comparison framework is being used — advantaged vs. disadvantaged group comparison, gradient analysis, Healthy People 2030 target comparison, or peer jurisdiction comparison?
5. What data sources are available with the necessary demographic stratification variables?
6. Is this analysis for a CHNA, a grant application, an accreditation report, a legislative brief, or a program evaluation?
7. What is the organizational readiness for equity work — has leadership made public commitments, are staff trained, is there a health equity officer?
8. What community engagement mechanism exists to validate findings with affected communities?

### Required Documents

- Health outcome data stratified by the equity dimensions in scope
- Census/ACS demographic data for the study population
- CDC Minority Health and Health Disparities strategic plan
- CDC/ATSDR Social Vulnerability Index (SVI) data
- Healthy People 2030 health disparities data and objectives
- MMWR health disparities and inequalities reports
- Organizational health equity assessment (e.g., BARHII Organizational Self-Assessment for Addressing Health Inequities)
- Community input from priority populations

---

## Step 1 — Define and Operationalize Equity Dimensions

For each equity dimension in scope, define how it will be measured and categorized:

- **Race/ethnicity**: Use OMB 1997 standards (5 minimum race categories + Hispanic/Latino ethnicity). Disaggregate where data support (e.g., separate Asian subgroups, tribal-specific data). Acknowledge that racial categories are social constructs that proxy for the lived experience of racism, not biological difference.
- **Income/socioeconomic status**: Area-level (Census poverty rate, median household income by census tract) or individual-level (family income as % FPL, insurance status). Use the Area Deprivation Index for area-level SES.
- **Geography**: Urban-rural classification (NCHS Urban-Rural Classification Scheme for Counties, 6 categories), or census-tract level with SVI overlay.
- **Sex/gender/SOGI**: Distinguish sex (biological, as recorded on vital records) from gender identity. For SOGI data, use BRFSS sexual orientation and gender identity modules where implemented.
- **Disability**: Use ACS disability questions (six types: hearing, vision, cognitive, ambulatory, self-care, independent living) or standardized disability status from survey data.
- **Language**: Limited English Proficiency (LEP) status from ACS, or primary language from clinical/administrative data.

Document the operationalization decisions. These choices shape what disparities are visible and which remain hidden.

---

## Step 2 — Quantify Health Disparities

Calculate disparity measures that go beyond visual comparison of bar charts:

**Absolute measures** (magnitude of the gap):
- Rate difference = Rate in disadvantaged group − Rate in reference group
- Excess cases = Rate difference × Population of disadvantaged group ÷ multiplier

**Relative measures** (proportional gap):
- Rate ratio = Rate in disadvantaged group ÷ Rate in reference group
- Index of Disparity (ID) = average absolute percentage deviation of each group's rate from the overall rate

**Summary measures** (across the full social gradient, not just worst vs. best):
- Slope Index of Inequality (SII): absolute difference between the lowest and highest ends of the social gradient, estimated through regression across all groups.
- Relative Index of Inequality (RII): SII divided by the population mean rate. Accounts for group size differences.
- Concentration Index: Measures the inequality across the entire distribution on a scale from -1 to +1.
- Health Disparities Calculator (HD*Calc, NCI): Use this tool for computing multiple disparity measures with statistical testing.

Report both absolute and relative measures. They can tell different stories — a narrowing relative gap can co-exist with a widening absolute gap if overall rates are falling.

---

## Step 3 — Analyze Structural Drivers

Move beyond describing "what" the disparity is to explaining "why" it exists:

- **Decomposition analysis**: Use Blinder-Oaxaca decomposition or mediation analysis to quantify how much of the disparity is explained by differences in education, income, insurance, healthcare access, and neighborhood conditions.
- **Place-based analysis**: Map health outcomes by census tract overlaid with structural indicators (segregation indices, redlining history via HOLC maps, disinvestment indicators, pollution burden from CalEnviroScreen or EPA EJScreen). Residential segregation is a master determinant that drives disparities across multiple pathways.
- **Temporal analysis**: Track disparities over time. Are they narrowing, stable, or widening? Joinpoint analysis of disparity measures (rate ratios, rate differences) over 10-20 years reveals whether policies and programs are bending the curve.
- **Intersectionality analysis**: Examine how multiple dimensions of identity interact. A Black woman in a rural area experiences compounded disadvantage that cannot be captured by analyzing race, sex, and geography separately. Use stratified analysis or interaction terms in regression models.

---

## Step 4 — Assess Root Causes and Structural Interventions

Based on the structural driver analysis, identify intervention points:

- **Policies producing inequity**: Identify specific policies (current and historical) that create or maintain the disparity. Examples: exclusionary zoning, school funding tied to property tax, cash bail, occupational licensing barriers, Medicaid coverage gaps.
- **Systems producing inequity**: Healthcare system factors (implicit bias in clinical encounters, provider distribution, insurance network adequacy), education system factors (school segregation, discipline disparities), criminal legal system factors (incarceration health impact).
- **Upstream interventions**: Policy changes that address root causes — Medicaid expansion, earned income tax credit, affordable housing, environmental regulations, anti-discrimination enforcement.
- **Midstream interventions**: Organizational and community strategies — community health worker programs, patient navigation, cultural concordance in healthcare workforce, trauma-informed care, medical-legal partnerships.
- **Accountability mechanisms**: Disparity reduction targets with timelines, equity impact assessments for new policies, equity dashboards with public reporting, equity budget analysis.

---

## Step 5 — Report Findings with an Equity Frame

- Lead with the finding, not the methodology. Decision-makers need to understand the magnitude and consequence of the disparity before the technical details.
- Name racism, poverty, and structural disadvantage as causes — not just "social determinants." Euphemistic language obscures accountability.
- Present disaggregated data in tables and visualizations. Use equity-focused visualizations: slope graphs comparing groups over time, choropleth maps with SVI overlay, disparity dashboards with trend arrows.
- Include community voice: quotes from focus groups, stories from affected individuals (with consent), community priorities from engagement processes.
- Provide specific, actionable recommendations tied to the structural drivers identified. Vague recommendations ("address social determinants") are useless. Specific recommendations ("extend Medicaid postpartum coverage from 60 days to 12 months") are actionable.
- Benchmark against Healthy People 2030 targets and peer jurisdictions.

---

## Checkpoint B — Analysis Review

- [ ] All equity dimensions operationalized with documented measurement decisions
- [ ] Both absolute and relative disparity measures calculated
- [ ] Summary disparity measures (SII, RII, or Concentration Index) computed for gradient analysis
- [ ] Structural drivers analyzed — not just the disparity described
- [ ] Intersectionality considered for compounded disadvantage
- [ ] Temporal trend included (is the disparity narrowing or widening?)
- [ ] Recommendations linked to specific structural drivers
- [ ] Community validation conducted with affected populations
- [ ] Report reviewed by health equity officer and senior epidemiologist

---

## Quality Audit

- [ ] Race/ethnicity categories follow OMB 1997 standards with disaggregation where data support
- [ ] Reference group for disparity calculations explicitly stated and justified (best-rate group preferred over white/non-Hispanic as default)
- [ ] Disparity measures calculated using HD*Calc or equivalent validated tool
- [ ] Ecological analysis caveated for ecological fallacy when using area-level data
- [ ] Small numbers handled with appropriate suppression and statistical methods (no rates based on numerators < 20 without flagging instability)
- [ ] Redlining/segregation analysis uses validated historical data (HOLC digitized maps, dissimilarity index from Census)
- [ ] Intersectional analysis conducted or data limitation documented
- [ ] Report language reviewed for deficit framing — disparities are the result of unjust systems, not deficient populations

---

## Guidelines

- Health disparities are not natural variation. They are the predictable consequence of unequal distribution of power, money, and resources. The analysis should reflect this understanding.
- Never frame a disparity as a characteristic of the disadvantaged group ("Black people have higher infant mortality") without identifying the structural cause ("Structural racism — including residential segregation, insurance gaps, provider bias, and chronic stress from discrimination — drives higher infant mortality among Black infants").
- Use "best rate" as the reference group rather than automatically using white/non-Hispanic as the comparator. This avoids centering whiteness as the norm and instead asks: what rate is achievable, and who is failing to reach it?
- Disaggregate data whenever possible. Aggregated categories (e.g., "Asian," "Hispanic") mask enormous within-group variation. Hawaiian/Pacific Islander health outcomes differ dramatically from Chinese American outcomes; Guatemalan health outcomes differ from Cuban outcomes.
- Equity analysis without community engagement is extractive. Affected communities must be involved in defining the questions, validating the findings, and shaping the recommendations.
- When data do not exist for a population (e.g., SOGI data, undocumented immigrant health data, tribal health data), document the data gap as itself an equity issue — invisibility in data systems reflects and reinforces marginalization.
- Escalate to health equity leadership when: analysis reveals a worsening disparity that current programs are not addressing, structural driver analysis implicates the organization's own policies, or political resistance to naming structural causes threatens the integrity of the analysis.
