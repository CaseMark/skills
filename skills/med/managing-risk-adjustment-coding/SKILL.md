---
name: managing-risk-adjustment-coding
language: en
description: Captures HCC codes for risk adjustment with annual assessment and documentation requirements. Use when coding for risk adjustment, capturing HCC conditions, or managing RAF scores.
tags:
  - management
  - medical-coding-and-billing
  - risk
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Risk Adjustment Coding

Captures HCC-eligible ICD-10-CM codes for CMS-HCC risk adjustment models with compliant annual documentation, MEAT criteria validation, and RAF score impact analysis. Covers Medicare Advantage (Part C), ACA marketplace, PACE, and ESRD risk adjustment programs.

## Why This Skill Exists

Risk adjustment determines per-member-per-month capitation payments to Medicare Advantage plans and ACA marketplace insurers. Each Hierarchical Condition Category (HCC) mapped from an ICD-10-CM code adds to the patient's Risk Adjustment Factor (RAF) score, directly increasing plan revenue. CMS estimates that improper risk adjustment payments exceed $15 billion annually. RADV (Risk Adjustment Data Validation) audits are intensifying, with CMS finalizing extrapolation rules for MA plans. Accurate, documentation-supported HCC capture is both a revenue opportunity and a compliance imperative — overcoding triggers False Claims Act liability; undercoding leaves legitimate revenue uncaptured.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What risk adjustment model applies? (CMS-HCC V24, V28, ESRD, RxHCC, ACA-HCC)
2. What is the payment year and data collection period?
3. Is this a prospective chart review, retrospective coding audit, or provider encounter review?
4. What is the patient's demographic profile? (age, sex, Medicaid dual-eligible status, institutional status)
5. Does the patient have conditions from the prior year that need annual recapture?
6. Which HCCs are currently captured for this member and what is the current RAF score?
7. Is this for Medicare Advantage, ACA marketplace, or another risk-adjusted program?

### Documents Required

- Complete medical record for encounters within the data collection period
- Patient problem list and medication list
- Prior year's HCC profile and RAF score
- CMS-HCC model coefficient tables (current payment year version)
- ICD-10-CM to HCC crosswalk (current model version)
- MEAT documentation criteria reference
- Provider attestation templates (if applicable for chart reviews)

---

## Step 1 — Understand the CMS-HCC Model Structure

Map the relationship between diagnosis codes, HCCs, and RAF scores.

- ICD-10-CM codes map to HCCs through the CMS crosswalk. Not all ICD-10-CM codes map to HCCs — only those indicating chronic, significant, or predictive conditions.
- **CMS-HCC V28** (phased in starting 2024): Reduced from 86 to 115 HCCs with recalibrated coefficients. New model increases specificity requirements for many conditions.
- **CMS-HCC V24** (being phased out): The legacy model used through 2023. During transition, CMS blends V24 and V28 scores (67% V24 / 33% V28 for 2024, shifting annually).
- HCCs are hierarchical — when a patient has multiple related conditions, only the highest-severity HCC in each hierarchy counts. Example: HCC 17 (Diabetes with Acute Complications) supersedes HCC 18 (Diabetes with Chronic Complications) which supersedes HCC 19 (Diabetes without Complications).
- Disease interaction factors: Certain HCC combinations generate additional RAF value (e.g., diabetes + CHF, HCC 85 + HCC 18).
- Demographics (age, sex, dual-eligible status, institutional/community status) generate base RAF components independent of diagnosis codes.

## Step 2 — Validate Documentation with MEAT Criteria

Every HCC-eligible condition must be supported by MEAT in the encounter note.

- **M — Monitor**: The provider documents monitoring activities — reviewing labs, assessing symptoms, tracking progression. "Patient's HbA1c reviewed at 7.8%, up from 7.2% last visit."
- **E — Evaluate**: The provider documents assessment of the condition's status. "CHF is currently compensated, no peripheral edema, weight stable."
- **A — Assess**: The provider documents clinical judgment about the condition. "COPD with acute exacerbation, likely triggered by viral URI."
- **T — Treat**: The provider documents treatment or management. "Continue metformin 1000mg BID, add glipizide 5mg daily for worsening glucose control."

**MEAT validation rules:**
- At least ONE MEAT element must be present in the encounter for the condition to be coded.
- A problem list entry alone does NOT satisfy MEAT — the condition must be actively addressed in the encounter note.
- Historical conditions (e.g., "history of stroke") should be coded only if the residual condition is still being managed.
- Each HCC-eligible condition must be recaptured annually — HCCs do not carry forward from year to year.

## Step 3 — Map ICD-10-CM Codes to HCCs

Select the most specific code that maps to the highest appropriate HCC.

- Use the current year's ICD-10-CM to HCC crosswalk — mappings change with each model year.
- **Specificity matters**: E11.9 (Type 2 diabetes without complications) maps to HCC 19 (RAF ~0.105), while E11.65 (Type 2 diabetes with hyperglycemia) maps to HCC 18 (RAF ~0.302). Ensure documentation supports the more specific code.
- **Common high-value HCCs**: Major depressive disorder (HCC 59), Vascular disease (HCC 108), COPD (HCC 111), CHF (HCC 85), CKD Stage 4 (HCC 138), Morbid obesity (HCC 48 in V28).
- **V28 changes to watch**: Dementia (reclassified), Substance use disorders (new HCCs), Obesity (now mapped), Depression (recalibrated).
- Never assign a more specific code than documentation supports — "coding to the highest HCC" without documentation is fraud.
- Conditions that are resolved, inactive, or not being managed should not be coded.

## Step 4 — Analyze RAF Score Impact

Calculate the financial impact of HCC capture decisions.

- RAF score = sum of all applicable HCC coefficients + demographic factors + disease interaction factors.
- The payment is: (RAF score × county base rate × plan-specific adjustment) = monthly capitation.
- Each 0.100 RAF increment represents approximately $1,000–$1,200 in annual revenue per member (varies by county).
- Calculate the marginal RAF impact of capturing vs. not capturing each HCC — this drives prioritization for chart reviews.
- Track suspecting vs. confirming: "suspected" HCC gaps (conditions from prior year not yet recaptured) should be prioritized for provider education.
- Monitor recapture rates by HCC category — target >85% annual recapture for chronic conditions.

## Step 5 — Conduct Retrospective Chart Reviews

Audit coded encounters for missed HCC opportunities and overcoded conditions.

- Pull all encounter records for the member during the data collection period.
- Compare coded diagnoses against the medical record documentation.
- Identify missed HCC-eligible conditions that are documented and meet MEAT but were not coded.
- Identify overcoded conditions where HCCs are assigned without adequate MEAT documentation.
- For missed conditions, determine whether an addendum or retrospective chart review attestation is compliant under the plan's policies.
- For overcoded conditions, submit deletions to avoid RADV audit findings.
- Document all chart review findings with specific record citations.

## Step 6 — Prepare for RADV Audit Defense

Ensure documentation withstands CMS audit scrutiny.

- RADV auditors require the original medical record to support every HCC submitted for the member.
- Each diagnosis must be supported by a face-to-face encounter with an eligible provider type (MD, DO, NP, PA — not all provider types qualify).
- Acceptable documentation sources: physician office notes, hospital records, diagnostic reports interpreted by a physician. Lab results alone without physician interpretation do not support HCC coding.
- The encounter must occur within the data collection period for the payment year.
- Provider signature (electronic or physical) and credentials must be present on the encounter note.
- Ensure all chart review addenda follow CMS guidelines — addenda must be dated, signed, and reference the original encounter.

---

## Checkpoint B — Review

- [ ] Every HCC-eligible code is supported by MEAT documentation in the encounter note
- [ ] ICD-10-CM codes are assigned at the highest specificity supported by documentation
- [ ] HCC hierarchy rules are correctly applied — only the highest HCC per hierarchy is counted
- [ ] Disease interaction factors are identified for qualifying HCC combinations
- [ ] Annual recapture is verified for all chronic conditions from the prior payment year
- [ ] RAF score calculation is accurate with current model coefficients
- [ ] No conditions are coded based solely on problem list entries, medication lists, or lab results without provider assessment
- [ ] Chart review findings distinguish between missed HCCs and overcoded HCCs

---

## Quality Audit

- [ ] MEAT criteria validation is documented for every HCC code submitted
- [ ] Recapture rates for chronic HCCs are tracked by provider and condition category
- [ ] RAF score trends per member are monitored for unexpected spikes (potential overcoding) or drops (undercoding)
- [ ] Chart review findings are reconciled with corrective action — deletions submitted for unsupported codes, additions submitted for documented but uncaptured conditions
- [ ] Provider education is targeted based on HCC capture gaps by condition type
- [ ] RADV-readiness assessments are conducted on a sample of members annually
- [ ] V24 to V28 transition impact is tracked — identify conditions that gain or lose HCC status under the new model

---

## Guidelines

- Follow CMS Risk Adjustment Data Technical Assistance for Medicare Advantage Organizations document (current year)
- Apply ICD-10-CM Official Guidelines for Coding and Reporting — risk adjustment coding must follow the same rules as all other coding
- Reference the CMS-HCC Risk Adjustment Model software and crosswalk files for current mappings
- Follow AHIMA Practice Brief on Risk Adjustment Coding for documentation and compliance standards
- Never code a condition for HCC capture that is not documented and managed in the encounter — this is a False Claims Act violation
- Never prompt or lead providers to document conditions that do not exist — CDI queries in risk adjustment must be non-leading
- Mark with [VERIFY] any HCC assignment where MEAT documentation is marginal
- Include disclaimer that risk adjustment coding must be documentation-supported and does not constitute guidance to maximize revenue beyond what clinical evidence supports
