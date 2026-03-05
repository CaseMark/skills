---
name: managing-digital-health-evaluations
description: Evaluates digital health tools and apps with clinical evidence assessment and integration planning. Use when evaluating health apps, assessing digital therapeutics, or planning digital health integration.
tags:
  - management
  - health-informatics
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Health Informatics
    - Health IT
    - Clinical Informatics
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Digital Health Evaluations

Evaluates digital health tools including mobile health apps, digital therapeutics (DTx), remote monitoring platforms, and patient-facing technologies using structured clinical evidence assessment, technical evaluation, regulatory classification, and integration planning frameworks.

## Why This Skill Exists

The digital health market includes over 350,000 health-related apps and a rapidly growing category of FDA-authorized digital therapeutics. Healthcare organizations receive constant vendor pitches and clinician requests to adopt new digital health tools, but lack structured evaluation processes. Without systematic evaluation, organizations adopt tools with insufficient clinical evidence (marketing claims vs. peer-reviewed outcomes), unknown regulatory status (many digital health tools require FDA oversight but operate without it), poor EHR integration (creating data silos and workflow disruption), inadequate privacy protections (consumer-grade apps sharing PHI with third parties), and unproven patient engagement (high download, low sustained use). This skill provides the evaluation framework to separate beneficial digital health innovations from costly distractions.


The digital therapeutics (DTx) category has matured from experimental to clinically validated, with FDA-authorized products for substance use disorders (reSET, reSET-O), insomnia (Somryst/Pear-004), ADHD (EndeavorRx), and chronic pain (RelieVRx). Simultaneously, the market for non-regulated wellness apps continues to grow unchecked. Structured evaluation frameworks separate clinically meaningful tools from costly distractions.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Product description** --- What is the digital health tool? (Mobile app, web platform, connected device, digital therapeutic, AI-enabled tool, patient engagement platform)
2. **Clinical use case** --- What clinical problem does the tool address? (Chronic disease management, medication adherence, behavioral health, physical rehabilitation, patient education, symptom monitoring)
3. **Target population** --- Which patients would use this tool? (Diagnosis, age range, digital literacy requirements, device requirements)
4. **Proposed integration** --- How would the tool connect to existing systems? (Standalone, EHR-integrated, patient portal-embedded, prescribed through e-prescribing)
5. **Requestor and champion** --- Who is requesting the evaluation? Is there a clinical champion?
6. **Vendor status** --- Vendor name, funding stage, market tenure, reference customers in healthcare
7. **Budget and funding** --- Who pays? (Patient out-of-pocket, insurance coverage, organizational budget, grant-funded pilot)

### Required Documents

- Vendor product documentation (capabilities, technical specifications, data flow diagrams)
- Clinical evidence package (peer-reviewed publications, clinical trial results, real-world evidence)
- FDA regulatory status documentation (510(k) clearance, De Novo, Breakthrough Device designation, or Cures Act software exclusion analysis)
- Privacy policy and BAA (if handling PHI)
- Technical integration documentation (API specifications, FHIR support, data formats)
- Pricing and contracting terms
- Patient-facing materials (app screenshots, user instructions, consent forms)

8. **Existing digital health tools** --- What digital health tools is the organization currently using? What has been evaluated and rejected in the past?
9. **Payer coverage landscape** --- Is there payer coverage for the tool type? (Medicare coverage for RPM CPT codes, commercial payer DTx coverage, employer-sponsored programs)

### Digital Health Evidence Level Reference

| Evidence Level | Description | Minimum for Clinical Claims | Minimum for Wellness Claims |
|---|---|---|---|
| Level 1 | Systematic review of RCTs | Preferred | Not required |
| Level 2 | Individual RCT or large cohort study | Required | Preferred |
| Level 3 | Case-control or case series | Insufficient alone | Acceptable |
| Level 4 | Expert opinion or vendor claims only | Not acceptable | Acceptable with caution |
---

## Step 1 --- Assess Clinical Evidence

Evaluate the evidence supporting the tool's clinical claims:

- **Evidence hierarchy** --- Classify the available evidence: Level 1 (systematic reviews, RCTs), Level 2 (cohort studies, case-control studies), Level 3 (case series, expert opinion), Level 4 (marketing claims only, no published evidence). For tools making clinical outcome claims, require at least Level 2 evidence
- **Study quality assessment** --- For each clinical study: sample size adequacy, control group design (active comparator, usual care, waitlist control), outcome measures (clinically meaningful vs. surrogate endpoints), follow-up duration (sustained engagement, not just 30-day outcomes), and generalizability to the target population
- **Digital therapeutic-specific criteria** --- For FDA-authorized DTx (e.g., reSET, Somryst, EndeavorRx): verify the FDA authorization covers the specific indication being proposed, review the pivotal trial results against the FDA's determination letter, and assess whether real-world effectiveness matches trial conditions
- **Patient engagement evidence** --- Clinical evidence alone is insufficient if patients do not use the tool. Assess: user retention rates (% still using at 30, 60, 90 days), session completion rates, patient satisfaction data, and dropout analysis (who stops using and why)
- **Comparator assessment** --- How does the tool compare to existing alternatives? (Standard care, existing digital tools, non-digital interventions). A tool that is marginally better than existing options may not justify implementation cost

- **Real-world evidence (RWE)** --- For tools with RCT evidence, also assess real-world performance: are outcomes achieved outside controlled trial settings? What is the observed vs. trial adherence rate? Are there post-market surveillance reports or FDA MAUDE adverse event reports?
---

## Step 2 --- Evaluate Regulatory Status

Determine the regulatory classification and compliance requirements:

- **FDA classification** --- Apply the FDA's Digital Health Policy framework: Is the tool a medical device? Does it meet SaMD criteria? Is it a Clinical Decision Support tool excluded under the Cures Act? Is it a general wellness product not subject to FDA oversight? Document the classification analysis with specific regulatory citations
- **FDA authorization verification** --- For tools claiming FDA clearance/approval: verify the listing in the FDA's 510(k), De Novo, or PMA databases. Confirm the authorized indication matches the proposed clinical use. FDA clearance for "patient engagement" does not equal clearance for "clinical decision support"
- **Digital therapeutic pathway** --- For DTx: verify the Prescription Digital Therapeutic (PDT) status, prescribing pathway (e-prescribing via pharmacy benefit vs. medical benefit vs. direct-to-patient), and coverage/reimbursement status (Medicare, commercial payers, employer programs)
- **FTC and state requirements** --- For non-FDA-regulated health apps: assess compliance with FTC Health Breach Notification Rule (for non-HIPAA-covered entities), FTC Act deceptive practices provisions (misleading health claims), and state-specific consumer health data privacy laws (Washington My Health My Data Act, etc.)

- **State consumer health data laws** --- Assess compliance with emerging state health data privacy laws beyond HIPAA: Washington My Health My Data Act, Connecticut SB 3, Nevada SB 370, and similar statutes that regulate consumer health data handling by non-HIPAA-covered entities
---

## Step 3 --- Conduct Technical Evaluation

Assess the technical fitness for enterprise deployment:

- **EHR integration capability** --- Evaluate: FHIR R4 API support (what resources? Patient, Observation, CarePlan, Questionnaire/QuestionnaireResponse?), SMART on FHIR launch capability (EHR launch, standalone launch), HL7 v2 interface support, or proprietary API only. Tools that require manual data re-entry into the EHR will not be adopted
- **Data standards** --- Assess whether the tool uses standard clinical terminologies: LOINC for observations and questionnaires, SNOMED CT for clinical findings, RxNorm for medications, ICD-10-CM for conditions. Non-standard data reduces interoperability and analytics value
- **Data ownership and portability** --- Review the vendor's data policies: who owns the patient data? Can data be exported in standard formats? What happens to patient data if the contract terminates? Can the organization access raw data for analytics?
- **Security assessment** --- Conduct security review: SOC 2 Type II report, penetration test results, encryption (at rest and in transit), authentication mechanisms, and HIPAA BAA availability. For patient-facing apps, assess: data sharing with third parties, advertising SDK presence, and analytics SDK data collection practices
- **Scalability and reliability** --- Evaluate: uptime SLA, system architecture (cloud infrastructure, redundancy), maximum concurrent users, and disaster recovery capability. A patient-facing tool that goes down during a chronic disease management program creates clinical gaps

- **Interoperability assessment** --- Evaluate the tool's interoperability maturity: does it use standard FHIR resources, participate in health information exchange, support standard clinical terminologies, and enable data portability in standard formats? Non-interoperable tools create clinical data silos that reduce care quality
---

## Step 4 --- Evaluate Patient Experience and Equity

Assess the tool's accessibility and usability:

- **Digital literacy requirements** --- What is the minimum technology capability required? Smartphone required? Specific OS version? Broadband internet? Bluetooth for connected devices? Assess against the target patient population's digital access profile
- **Accessibility compliance** --- Test against WCAG 2.1 AA criteria: screen reader compatibility, keyboard/switch navigation, high contrast mode, text resizing, closed captioning for video content. Assess ADA compliance for patients with disabilities
- **Language support** --- What languages are supported? Are translations clinically reviewed or machine-generated? Does the app support right-to-left languages if relevant to the patient population?
- **Health literacy** --- Evaluate patient-facing content readability: target 6th-8th grade reading level, use of plain language, visual aids for complex concepts, and culturally appropriate imagery and examples
- **Digital divide impact** --- Assess whether recommending this tool would exacerbate health disparities: are there alternative pathways for patients who cannot use the tool? Would adoption create a two-tiered care experience?

- **Caregiver and family considerations** --- Assess the tool's support for caregivers and family members: proxy access for children or dependent adults, caregiver notifications, family engagement features, and privacy controls for shared devices
---

## Step 5 --- Design the Pilot and Evaluation Plan

Structure a rigorous pilot before enterprise commitment:

- **Pilot scope** --- Define: target patient population (diagnosis, volume, site), pilot duration (minimum 90 days for chronic disease tools), enrollment target (minimum 50 patients for usability evaluation, larger for outcome evaluation), and comparison group (concurrent usual-care patients)
- **Outcome measures** --- Define primary and secondary endpoints: clinical outcomes (HbA1c change, PHQ-9 improvement, blood pressure reduction), process measures (visit completion, medication adherence), patient experience (satisfaction, NPS, ease of use), and operational metrics (clinical staff time impact, EHR documentation burden)
- **Data collection plan** --- Specify how pilot data will be collected: EHR-extracted outcomes, tool-generated engagement data, patient surveys, clinician interviews, and cost data
- **Go/No-Go criteria** --- Define pre-specified criteria for pilot success: minimum patient engagement threshold (e.g., > 60% active at 90 days), minimum clinical outcome improvement, no safety signals, acceptable technical reliability, and positive clinician feedback
- **Financial evaluation** --- Model the total cost of ownership: license/subscription fees, implementation cost, EHR integration cost, clinical staff training, ongoing support, and expected ROI from improved outcomes, avoided utilization, or payer incentives

- **Sustainability planning** --- Before enterprise commitment, define the long-term sustainability plan: ongoing license costs, internal support requirements, vendor viability assessment (funding runway, market position, competitive landscape), and exit strategy if the vendor fails or the tool underperforms
---

## Checkpoint B --- Evaluation Completeness Review

Before making a procurement/deployment decision:

- [ ] Clinical evidence assessment is complete with evidence level classification
- [ ] FDA regulatory classification is documented with supporting analysis
- [ ] Technical evaluation covers EHR integration, data standards, security, and scalability
- [ ] Patient experience and equity assessment identifies no disqualifying barriers
- [ ] Pilot results (if conducted) meet pre-specified Go/No-Go criteria
- [ ] Financial model demonstrates acceptable ROI or strategic value
- [ ] Privacy and security review is complete with BAA executed (if applicable)
- [ ] Clinical champion and operational owner are identified

- [ ] Vendor financial viability has been assessed (funding status, customer base, market position)
- [ ] Exit strategy is defined for vendor failure or contract termination
- [ ] Payer coverage landscape is documented for applicable billing scenarios
---

## Quality Audit

- [ ] Evidence assessment distinguishes peer-reviewed research from vendor-supplied marketing data
- [ ] FDA classification analysis is documented with specific regulatory citations
- [ ] Security review includes SOC 2, penetration testing, and data sharing practices
- [ ] EHR integration is validated using standard protocols (FHIR, SMART on FHIR)
- [ ] Patient-facing content meets health literacy standards (6th-8th grade readability)
- [ ] Accessibility is tested against WCAG 2.1 AA criteria
- [ ] Health equity impact is assessed for the target patient population
- [ ] Vendor contract includes data portability, termination provisions, and performance guarantees
- [ ] Post-deployment monitoring plan defines metrics and review cadence

- [ ] State consumer health data privacy laws are assessed for compliance
- [ ] Interoperability evaluation covers FHIR, clinical terminologies, and data portability
- [ ] Caregiver and family engagement features are assessed for population appropriateness
- [ ] Sustainability plan addresses vendor viability and long-term cost of ownership
---

## Guidelines

- Clinical evidence is the primary evaluation criterion. A beautifully designed app with no evidence of clinical effectiveness is an expensive distraction. Require at least Level 2 evidence for tools making outcome claims
- Vendor demonstrations are marketing events, not evaluations. Require hands-on testing by clinicians and patients representative of the target population before procurement decisions
- EHR integration is a requirement, not a nice-to-have. Digital health tools that operate outside the EHR create documentation gaps, clinician workflow disruption, and data silos that reduce rather than enhance care quality
- Regulatory classification is the organization's responsibility, not just the vendor's. If a vendor claims their tool is not an FDA-regulated device, verify that classification independently. Using an uncleared medical device exposes the organization to liability
- Patient engagement is the Achilles heel of digital health. The majority of health apps are abandoned within 30 days. Demand evidence of sustained engagement, not just initial adoption, before committing to implementation
- Privacy risk extends beyond HIPAA. Many consumer health apps share data with advertising networks, analytics companies, and data brokers. Review the tool's privacy practices from the patient's perspective, not just the regulatory minimum
- Digital health tools should reduce health disparities, not amplify them. If a tool is only accessible to patients with smartphones, broadband, and high digital literacy, it risks widening outcome gaps for vulnerable populations
- Pilot before committing. The digital health landscape is littered with tools that performed well in controlled trials but failed in real-world clinical workflows. A 90-day pilot with pre-specified success criteria protects against costly failures

- The fastest-growing risk in digital health is scope creep: a tool procured for patient engagement gradually becomes a clinical decision support tool without undergoing the regulatory and clinical evaluation that use case requires
- For remote patient monitoring (RPM) tools, separate the device evaluation from the platform evaluation. The clinical accuracy of the measurement device and the workflow integration of the data platform are independent assessment dimensions