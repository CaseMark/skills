---
name: analyzing-social-determinants-of-health
language: en
description: Maps social determinants affecting health outcomes with intervention strategy development. Use when analyzing SDOH, mapping community resources, or designing social health interventions.
tags:
  - analysis
  - public-health
metadata:
  author: casemark
  practice_areas:
    - Public Health
    - Epidemiology
    - Preventive Medicine
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---

# Analyzing Social Determinants of Health

## Why This Skill Exists

Social determinants of health (SDOH) — the conditions in which people are born, grow, live, work, and age — account for an estimated 30-55% of health outcomes, dwarfing the contribution of healthcare delivery (~20%). Healthy People 2030 places SDOH as one of five overarching goals and organizes social determinants into five domains: Economic Stability, Education Access and Quality, Healthcare Access and Quality, Neighborhood and Built Environment, and Social and Community Context. Failing to analyze SDOH means treating symptoms while ignoring root causes — a pattern that perpetuates health inequities across generations. This skill provides the structured framework for systematically assessing SDOH conditions, quantifying their association with health outcomes, and developing upstream intervention strategies using established indices (CDC SVI, Area Deprivation Index, USDA Food Access Research Atlas) and federal data infrastructure.

---

## Checkpoint A — Intake and Scoping

### Intake Questions

1. What is the analytic purpose — community health assessment, grant application, intervention design, policy brief, or health equity evaluation?
2. What is the geographic unit of analysis — state, county, census tract, zip code, or neighborhood?
3. Which SDOH domains are in scope — all five Healthy People 2030 domains, or a subset?
4. What health outcomes are being linked to SDOH conditions (e.g., premature mortality, diabetes prevalence, infant mortality, mental health ED visits)?
5. What existing data infrastructure is available — ACS, AHR, BRFSS, SVI, ADI, EHR-based Z-codes?
6. Is this a descriptive analysis (profiling conditions) or an analytic study (testing SDOH-outcome associations)?
7. Will the analysis feed into a Community Health Needs Assessment or a grant proposal with specific SDOH measures required?
8. Who is the audience — health department, hospital community benefit, policymakers, or community coalition?

### Required Documents

- American Community Survey (ACS) 5-year estimates for the target geography
- CDC/ATSDR Social Vulnerability Index (SVI) data by census tract
- County Health Rankings model data (health factors and health outcomes)
- USDA Food Access Research Atlas (food desert designations)
- BRFSS prevalence estimates for health behaviors and outcomes
- Area Deprivation Index (ADI) data from the Health Resources & Services Administration
- EHR or claims data with ICD-10 Z-codes (Z55-Z65: Persons with potential health hazards related to socioeconomic and psychosocial circumstances) if available
- Healthy People 2030 SDOH objectives and baselines

---

## Step 1 — Map SDOH Conditions Across the Five Domains

For each Healthy People 2030 domain, compile indicators:

**Economic Stability**:
- Poverty rate (% below 100% FPL, % below 200% FPL) — ACS Table B17001
- Median household income — ACS Table B19013
- Unemployment rate — Bureau of Labor Statistics / ACS Table B23025
- Food insecurity rate — Feeding America Map the Meal Gap
- Unbanked/underbanked rate — FDIC National Survey

**Education Access and Quality**:
- High school graduation rate — NCES or state education department
- Post-secondary enrollment rate — ACS Table B15003
- Early childhood education enrollment (pre-K) — ACS or state data
- Health literacy estimates — NAAL or proxy from education attainment

**Healthcare Access and Quality**:
- Uninsured rate by age group — ACS Table B27001
- Primary care provider-to-population ratio — HRSA Area Health Resource File
- Mental health provider shortage designation — HRSA HPSA
- Preventable hospitalization rate (AHRQ PQI composite) — state hospital discharge data

**Neighborhood and Built Environment**:
- Housing cost burden (% paying >30% income on housing) — ACS Table B25070/B25091
- Severe housing problems (overcrowding, lack of plumbing/kitchen) — CHAS data
- Broadband internet access — ACS Table B28002
- Air quality (PM2.5 annual average) — EPA AQS / CDC PLACES
- Food desert designation (low access at 1 mile urban / 10 miles rural) — USDA FARA

**Social and Community Context**:
- Social association rate — County Health Rankings (organizations per 10,000 population)
- Violent crime rate — FBI UCR / state crime data
- Residential segregation index (dissimilarity or isolation index) — Census data
- Single-parent household rate — ACS Table B09002
- Voter participation rate — state election data (proxy for civic engagement)

---

## Step 2 — Construct Composite Indices and Identify Vulnerable Populations

- **CDC/ATSDR Social Vulnerability Index (SVI)**: Uses 16 Census variables grouped into four themes (Socioeconomic Status, Household Characteristics and Disability, Racial and Ethnic Minority Status and Language, Housing Type and Transportation). Identify census tracts with overall SVI ≥ 0.75 (most vulnerable quartile).
- **Area Deprivation Index (ADI)**: National percentile ranking at the census block group level. Identify block groups in the most deprived decile (ADI ≥ 90th percentile).
- **Create custom composite scores** when required by a specific analytic framework: weight indicators by domain using PCA (principal component analysis) or equal weighting, and validate against known health outcome gradients.
- Overlay vulnerability indices with health outcome data to identify geographic areas where high SDOH burden and poor health outcomes co-occur (spatial concordance).

---

## Step 3 — Analyze SDOH-Health Outcome Associations

- **Descriptive**: Produce stratified tables and maps showing health outcomes by SDOH quintile or composite index category. Use choropleth maps overlaying SVI with health outcomes.
- **Bivariate**: Calculate correlation coefficients (Pearson or Spearman) between SDOH indicators and health outcomes at the appropriate geographic unit. Test with scatter plots.
- **Multivariable**: Use ecological regression (when unit of analysis is a geographic area) or individual-level regression (when linked individual data is available) to assess independent associations.
  - For ecological analysis: negative binomial or Poisson regression with offset for population, adjusting for confounders.
  - For individual-level: logistic regression for binary outcomes, adjusting for demographic and clinical covariates.
- **Mediation analysis**: Test whether specific SDOH domains mediate the pathway between structural conditions (e.g., residential segregation) and health outcomes (e.g., infant mortality).
- Report effect sizes (rate ratios, odds ratios) with 95% confidence intervals. Emphasize practical significance for public health action.

---

## Step 4 — Identify Upstream Intervention Points

Based on analytic findings, map intervention strategies to the causal pathway:

- **Upstream (structural/policy)**: Minimum wage increases, affordable housing policy, Medicaid expansion, earned income tax credit, paid family leave. These address root causes but require legislative action.
- **Midstream (community/organizational)**: Community health worker programs, food prescription programs, medical-legal partnerships, healthcare system screening for SDOH (Z-code documentation), and referral to community resources via closed-loop systems (e.g., Unite Us, Aunt Bertha/findhelp).
- **Downstream (individual)**: Direct service provision — housing vouchers, food assistance enrollment (SNAP, WIC), transportation vouchers, utility assistance (LIHEAP).

Prioritize interventions by: evidence base (Community Guide, What Works for Health), scalability, equity impact, cost-effectiveness, and alignment with Healthy People 2030 objectives.

---

## Step 5 — Report and Translate for Action

- Write the SDOH analysis report with: executive summary, methods, findings by domain, composite vulnerability mapping, SDOH-outcome association results, recommended interventions, and data limitations.
- Produce data visualizations: SVI maps, SDOH-outcome scatter plots, forest plots of association measures, and community asset maps.
- Translate findings for non-technical audiences: plain-language fact sheets for community members, policy briefs for elected officials, data dashboards for health department staff.
- Connect findings to actionable levers: which findings are addressable through health department programs, which require cross-sector partnerships, and which require policy change.

---

## Checkpoint B — Analysis Review

- [ ] All five Healthy People 2030 SDOH domains assessed with at least 2 indicators per domain
- [ ] Data sources documented with year, geography, and methodology
- [ ] Composite vulnerability index (SVI, ADI, or custom) applied and mapped
- [ ] SDOH-outcome associations tested with appropriate statistical methods
- [ ] Equity lens applied — disparities by race/ethnicity, income, and geography highlighted
- [ ] Intervention recommendations linked to specific findings and evidence base
- [ ] Data limitations documented (ecological fallacy, data currency, geographic mismatch)
- [ ] Report reviewed by epidemiologist and community stakeholders

---

## Quality Audit

- [ ] ACS data uses 5-year estimates for small-area analysis (1-year estimates only for geographies with population > 65,000)
- [ ] SVI version year matches the analysis period (SVI is updated biennially with new ACS data)
- [ ] Food desert designations use current USDA FARA release
- [ ] Z-code analysis acknowledges low documentation rates (~1-2% of encounters) and resulting selection bias
- [ ] Ecological analysis does not make individual-level causal claims (ecological fallacy caveat stated)
- [ ] Correlation does not imply causation — language throughout the report reflects appropriate inferential limits
- [ ] Intervention recommendations cite evidence from the Community Guide, What Works for Health, or peer-reviewed literature
- [ ] All maps include data source, year, classification method, and suppression notes

---

## Guidelines

- SDOH analysis is inherently political. Data about poverty, racism, and structural inequality can provoke defensive reactions from decision-makers. Present findings with precision and empathy, but do not soften evidence to avoid discomfort.
- The ecological fallacy is the single greatest analytic risk in area-level SDOH analysis. Never infer that individuals living in high-poverty census tracts are themselves poor. State the unit of analysis explicitly.
- When using EHR Z-codes, acknowledge that documentation rates are extremely low and biased toward health systems that have implemented SDOH screening. Z-code data is useful for demonstrating proof-of-concept but not for prevalence estimation.
- Residential segregation is a root cause that operates through multiple SDOH domains simultaneously (employment, education, food access, environmental exposure, healthcare access). Analyze it as a structural factor, not just another SDOH indicator.
- Community asset mapping is as important as deficit mapping. Document strengths (community organizations, cultural resources, mutual aid networks) alongside needs.
- For grant applications, align SDOH metrics exactly with the funder's required measures. HRSA, CDC, and RWJF each define and measure SDOH differently.
- Escalate to senior analyst or health equity director when: findings reveal an unexpected disparity pattern, data gaps prevent meaningful analysis for a specific population, or recommended interventions require cross-sector partnerships that do not yet exist.
