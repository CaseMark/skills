---
name: conducting-literature-reviews-systematic
language: en
description: Performs systematic literature review following PRISMA guidelines with search strategy documentation. Use when conducting systematic reviews, documenting search strategies, or performing PRISMA analyses.
tags:
  - process
  - clinical-research
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Biostatistics
    - Regulatory Affairs
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---

# Conducting Systematic Literature Reviews

## Why This Skill Exists

Systematic reviews form the highest level of clinical evidence and are required for regulatory submissions (ICH M4E CTD Module 2.5 Clinical Overview), health technology assessments, and clinical guideline development. Unlike narrative reviews, systematic reviews follow a reproducible, auditable methodology that minimizes selection bias. This skill implements the PRISMA 2020 statement (Page et al., BMJ 2021), Cochrane Handbook methodology, and PROSPERO registration standards to produce reviews that meet journal, regulatory, and HTA body requirements.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What is the review question structured using PICOS (Population, Intervention, Comparator, Outcomes, Study design)?
2. Is this review for a regulatory submission (NDA/BLA clinical overview), HTA dossier, clinical guideline, or publication?
3. Has the protocol been registered in PROSPERO, OSF, or another registry?
4. Are there existing systematic reviews on this topic that need updating rather than replication?
5. What databases must be searched (PubMed/MEDLINE, Embase, Cochrane CENTRAL, CINAHL, PsycINFO, Web of Science)?
6. Is grey-literature searching required (ClinicalTrials.gov, WHO ICTRP, conference abstracts, FDA reviews)?
7. What date range and language restrictions (if any) apply?
8. How many reviewers are available for dual independent screening?
9. Is a meta-analysis planned, or is this a qualitative synthesis only?
10. What is the target completion date?

### Required Source Documents
- Draft PICOS framework
- Preliminary search results or scoping search
- PROSPERO registration (or draft protocol)
- Relevant prior systematic reviews in the same therapeutic area
- Funder/sponsor requirements for evidence review scope
- Journal submission guidelines (if publication-targeted)

---

## Step 1 — Develop the Search Strategy

Build a reproducible search strategy with a medical librarian or information specialist:

1. **Identify key concepts**: Break the PICOS question into 2-4 search concept blocks
2. **Term selection**: For each concept, compile controlled vocabulary (MeSH terms for MEDLINE, Emtree for Embase) AND free-text synonyms, variant spellings, abbreviations
3. **Boolean logic**: Combine terms within concepts using OR; combine concepts using AND
4. **Filters**: Apply validated study-design filters only when justified (e.g., Cochrane RCT filter for MEDLINE); avoid over-filtering that may miss relevant studies
5. **Documentation**: Record the exact search string, database, date of search, and number of results for each database — this is a PRISMA requirement
6. **Sensitivity testing**: Run the search and verify it captures known key studies (a priori reference set of 5-10 publications)
7. **Peer review**: Submit the search strategy for peer review using the PRESS (Peer Review of Electronic Search Strategies) checklist

---

## Step 2 — Screen and Select Studies

Apply the pre-defined eligibility criteria through a two-phase screening process:

### Phase 1: Title/Abstract Screening
- Two independent reviewers screen all retrieved records
- Use reference management software (Covidence, Rayyan, EPPI-Reviewer, or equivalent)
- Apply liberal inclusion at this stage (when in doubt, include for full-text review)
- Record reasons for exclusion at the title/abstract level only in aggregate

### Phase 2: Full-Text Screening
- Retrieve full text for all records passing Phase 1
- Two independent reviewers apply detailed eligibility criteria
- Record specific reason for exclusion for each excluded full-text article (required for PRISMA flow diagram)
- Resolve disagreements by discussion or third-reviewer adjudication
- Calculate inter-rater agreement (Cohen's kappa); report in the methods

### Reference Tracking
- Hand-search reference lists of included studies and relevant reviews
- Conduct forward citation tracking of key included studies
- Search clinical trial registries for unpublished results of completed trials

---

## Step 3 — Extract Data

Design and pilot the data extraction form:

1. **Study characteristics**: Author, year, country, study design, setting, funding source, registration number
2. **Population**: Sample size, demographics, inclusion/exclusion criteria, disease severity
3. **Intervention/Exposure**: Drug/device/procedure details, dose, duration, administration route
4. **Comparator**: Active comparator or placebo details, co-interventions
5. **Outcomes**: Primary and secondary outcome definitions, measurement instruments, timepoints, results (point estimates, measures of variability, sample sizes per group)
6. **Risk of bias domains**: Extracted alongside outcome data (not as a separate step)

Dual-independent extraction is required for at least primary outcomes. Pilot the form on 3-5 studies before full extraction. Resolve discrepancies by returning to the source paper.

---

## Step 4 — Assess Risk of Bias

Apply the appropriate validated tool based on study design:

| Study Design | Tool | Domains |
|--------------|------|---------|
| Randomized trials | Cochrane RoB 2.0 | Randomization, deviations, missing data, measurement, selection of reported result |
| Non-randomized interventional | ROBINS-I | Confounding, selection, classification, deviations, missing data, measurement, reporting |
| Observational (cohort/case-control) | Newcastle-Ottawa Scale | Selection, comparability, outcome/exposure ascertainment |
| Diagnostic accuracy | QUADAS-2 | Patient selection, index test, reference standard, flow and timing |

- Two reviewers independently assess each study
- Present results in a risk-of-bias summary figure (traffic-light plot) and graph (weighted bar chart)
- Use risk-of-bias judgments to inform sensitivity analyses (exclude high-risk studies) and GRADE certainty assessment

---

## Step 5 — Synthesize Results

Choose the appropriate synthesis method:

### Narrative Synthesis (when meta-analysis is not appropriate)
- Organize by outcome, population subgroup, or study design
- Use structured summary tables (Synthesis Without Meta-analysis — SWiM reporting guideline)
- Vote-counting based on direction of effect is acceptable only as a supplement

### Quantitative Synthesis (meta-analysis — see also the meta-analysis skill)
- Assess clinical and methodological heterogeneity before pooling
- If heterogeneity is acceptable (I² < 75% and clinical similarity), pool using random-effects model (DerSimonian-Laird or restricted maximum likelihood)
- Present forest plots with individual study estimates, pooled estimate, and 95% CI
- Conduct pre-specified subgroup analyses and sensitivity analyses

---

## Step 6 — Assess Certainty of Evidence

Apply the GRADE framework (Grading of Recommendations Assessment, Development and Evaluation):

1. **Risk of bias**: Downgrade if majority of evidence is at high risk
2. **Inconsistency**: Downgrade if I² is high and unexplained, or point estimates vary widely
3. **Indirectness**: Downgrade if population, intervention, comparator, or outcomes differ from the review question
4. **Imprecision**: Downgrade if confidence intervals cross the clinical decision threshold or optimal information size is not met
5. **Publication bias**: Downgrade if funnel plot is asymmetric, Egger's test is significant, or there are known unpublished studies

Present GRADE Summary of Findings (SoF) tables for each critical and important outcome.

---

## Step 7 — Compile PRISMA-Compliant Report

Structure the final report using the PRISMA 2020 27-item checklist:

- **Title**: Identify as systematic review (and meta-analysis if applicable)
- **Abstract**: Structured abstract per PRISMA for Abstracts
- **Methods**: Registration, eligibility, search strategy, selection process, data extraction, risk-of-bias assessment, synthesis methods
- **Results**: PRISMA flow diagram (identification → screening → eligibility → included), study characteristics table, risk-of-bias figures, forest plots, GRADE SoF tables
- **Discussion**: Summary of evidence, limitations of evidence and review process, implications for practice and research

---

## Checkpoint B — Pre-Submission Review

1. [ ] PRISMA 2020 checklist is completed with page/section references for all 27 items
2. [ ] PRISMA flow diagram numbers are internally consistent (identified − excluded = included at each stage)
3. [ ] Search strategy is fully reproducible (exact strings, databases, dates documented)
4. [ ] Inter-rater agreement is reported for screening and extraction
5. [ ] Risk-of-bias assessment uses the correct tool for each study design
6. [ ] GRADE SoF tables are completed for all critical outcomes
7. [ ] All forest plots display correct study weights, effect estimates, and CIs
8. [ ] Publication-bias assessment is included (for ≥10 studies per meta-analysis)
9. [ ] PROSPERO record is updated with final results
10. [ ] Funding sources and conflicts of interest are declared

---

## Quality Audit

- [ ] Search captures all studies in the a priori reference set
- [ ] No eligible study was excluded without documented reason
- [ ] Data extraction values match source publications (spot-check at least 20%)
- [ ] Statistical pooling uses appropriate effect measure (OR, RR, HR, MD, SMD) for the outcome type
- [ ] Heterogeneity is quantified (I², tau², prediction interval) and explored
- [ ] Sensitivity analyses are pre-specified in the protocol, not post-hoc
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. Register the protocol before beginning screening — unregistered reviews face scrutiny for reporting bias
2. Never modify eligibility criteria after seeing the search results without documenting and justifying the amendment
3. Use dual-independent processes for screening, extraction, and risk-of-bias assessment; single-reviewer shortcuts are unacceptable for publication-quality reviews
4. Report what was found, including null results — do not suppress non-significant findings
5. For living systematic reviews, define update frequency and methods in the protocol
6. When reviews are conducted for regulatory submissions, follow the EMA/FDA-specific evidence-synthesis requirements
7. Cite the PRISMA 2020 statement (not the original 2009 version) for reviews initiated after 2021
8. For network meta-analyses, use the PRISMA-NMA extension
9. Escalate to methodologist when transitivity or coherence assumptions are questionable
10. This skill produces review methodology and drafts — final synthesis interpretation requires clinical-domain expert review
