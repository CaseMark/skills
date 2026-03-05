---
name: managing-health-ai-governance
description: Structures AI/ML governance for healthcare applications with validation, monitoring, and ethical frameworks. Use when governing health AI, validating clinical models, or managing AI ethics in healthcare.
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

# Managing Health AI Governance

Structures AI/ML governance for healthcare applications with inventory management, risk classification, validation requirements, bias assessment, regulatory compliance, and ongoing monitoring frameworks. This skill covers the organizational governance structure needed to safely adopt, deploy, and monitor AI/ML tools across clinical, operational, and administrative healthcare functions.

## Why This Skill Exists

Healthcare organizations are rapidly deploying AI/ML tools: EHR-embedded predictions (sepsis, deterioration, readmission), imaging AI (radiology CAD, pathology), ambient clinical documentation, coding/billing AI, operational AI (scheduling, staffing, capacity), and generative AI (clinical summarization, patient communication). Without governance, organizations face: patient safety risks from unvalidated models, health equity harms from biased algorithms, regulatory exposure (FDA SaMD, state AI transparency laws, CMS AI requirements), legal liability for AI-influenced clinical decisions, and reputational damage from publicized AI failures. Governance provides the organizational structure to manage these risks while enabling beneficial AI adoption.


High-profile AI failures in healthcare --- the Optum algorithm that systematically under-referred Black patients, Epic sepsis model performance questions, and concerns about ambient documentation hallucinations --- demonstrate that AI governance is not theoretical. President Biden's Executive Order 14110 on AI Safety (2023) and emerging state AI laws create regulatory obligations. The Coalition for Health AI (CHAI) and the AAMC are developing healthcare-specific AI governance standards that will shape expectations.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **AI inventory** --- How many AI/ML tools are currently in use or under evaluation? Categories: clinical decision support, imaging AI, ambient documentation, operational/administrative, research
2. **Governance structure** --- Does an AI governance committee exist? Who are the members? What is its authority (advisory vs. decision-making)?
3. **Regulatory posture** --- Which AI tools may be subject to FDA SaMD oversight? Are there state AI transparency laws applicable to the organization?
4. **Existing policies** --- Are there current policies covering AI procurement, validation, deployment, or monitoring?
5. **Risk tolerance** --- What is the organization's risk posture for AI adoption? (Early adopter, fast follower, conservative/evidence-required)
6. **Incident history** --- Have there been any adverse events, near-misses, or complaints related to AI tools?
7. **Vendor landscape** --- How many AI vendors does the organization work with? What contractual provisions exist for model transparency and performance guarantees?

### Required Documents

- AI/ML tool inventory (all deployed and under-evaluation tools)
- Current AI-related policies and procedures
- FDA SaMD classification assessments for applicable tools
- Vendor contracts with AI-specific terms (model transparency, performance guarantees, data rights)
- Institutional review processes for new technology adoption
- Relevant regulatory guidance (FDA AI/ML SaMD framework, ONC CDS criteria, state AI laws)

---

## Step 1 --- Establish the Governance Structure

Build the organizational framework:

- **AI Governance Committee** --- Charter a multidisciplinary committee with decision-making authority: CMIO (clinical informatics leadership), CIO/CISO (technology and security), Chief Medical Officer (clinical practice authority), Privacy Officer (HIPAA/compliance), General Counsel (legal and regulatory), Patient Safety Officer, Chief Equity Officer or designee, and Research leadership (for research-related AI)
- **Committee scope** --- Define what requires committee review: all new AI/ML tool procurement, all clinical AI deployments, significant updates to deployed models (retraining, new features), and AI-related incident review
- **Risk-tiered review process** --- Not all AI requires the same scrutiny. Define tiers: Tier 1 (clinical decision-influencing AI) requires full committee review with local validation, bias assessment, and clinical workflow design. Tier 2 (operational AI with indirect patient impact) requires abbreviated review. Tier 3 (administrative AI with no patient impact) requires notification only
- **Decision framework** --- Define the committee's decision options: Approve (with conditions), Approve pilot (limited deployment with monitoring requirements), Defer (requires additional information), Deny (unacceptable risk). Document decision rationale for every tool reviewed
- **Accountability model** --- Assign an AI system owner for each deployed tool: responsible for ongoing monitoring, incident reporting, vendor relationship, and compliance. The owner is a named individual, not a department

- **Generative AI policy** --- Develop a specific generative AI use policy addressing: approved use cases (clinical summarization, patient communication drafting, administrative tasks), prohibited use cases (autonomous clinical decision-making, unsupervised patient communication), PHI handling requirements (only BAA-covered platforms for PHI processing), and documentation requirements (clinician review and attestation of all AI-generated clinical content)
---

## Step 2 --- Build the AI Inventory and Risk Classification

Catalog and classify all AI/ML tools:

- **Inventory template** --- For each tool, document: name, vendor, function, clinical domain, input data types, output type, deployment location, user population, patient population affected, FDA status, deployment date, system owner, and last validation date
- **Risk classification** --- Apply the FDA SaMD risk framework adapted for institutional governance: assess the significance of the information provided by the AI (treat, diagnose, drive clinical management, inform clinical management) crossed with the healthcare situation (critical, serious, non-serious). Higher risk = more stringent governance requirements
- **Cures Act CDS exclusion assessment** --- For each clinical AI tool, evaluate whether it meets the four criteria for exclusion from FDA device regulation under the Cures Act: (1) not intended to acquire, process, or analyze a medical image, signal, or pattern, (2) intended for use by a healthcare professional, (3) intended to enable the professional to independently review the basis for the recommendation, (4) intended as an aid rather than replacement for clinical judgment
- **Shadow AI detection** --- Identify AI tools adopted outside the governance process: departmental purchases, research tools used in clinical practice, vendor-activated features not formally reviewed, and clinician-initiated use of general-purpose AI (ChatGPT, Bard) for clinical purposes

---

## Step 3 --- Define Validation Requirements

Establish validation standards by risk tier:

- **Local validation** --- For Tier 1 clinical AI, require local validation on institutional data before deployment: discrimination metrics (AUROC, AUPRC), calibration assessment, and comparison against current practice baseline. Minimum sample sizes: 1,000 patients or 100 outcome events
- **Bias assessment** --- Require algorithmic bias evaluation for all Tier 1 AI: subgroup performance analysis across race, ethnicity, sex, age, insurance type, and primary language. Document any performance disparities and require mitigation plans before deployment
- **Clinical face validity** --- Subject matter expert review of model features and outputs. Do the predictions make clinical sense? Are there features that suggest proxy discrimination (cost-based predictions disadvantaging low-access populations)?
- **Vendor transparency requirements** --- Negotiate contractual requirements: model card or algorithm specification, training data demographics, performance metrics by subgroup, update notification obligations, and right to conduct independent validation
- **Generative AI validation** --- For ambient documentation, clinical summarization, and other generative AI: accuracy assessment via clinician review of output samples (minimum 100 samples per use case), hallucination rate measurement, and PHI handling validation

- **Model card requirements** --- For every AI tool in the inventory, require a model card (per Mitchell et al. framework) documenting: intended use, training data demographics, performance metrics by subgroup, known limitations, ethical considerations, and update history. Vendor-supplied model cards should be supplemented with local validation data
---

## Step 4 --- Implement Monitoring and Incident Management

Ongoing surveillance after deployment:

- **Performance monitoring** --- For each deployed AI tool, define monitoring metrics and measurement frequency: prediction accuracy (weekly for clinical AI), calibration drift (monthly), feature distribution shift (monthly), utilization rate (weekly), clinician override/acceptance rate (weekly), and patient outcome correlation (quarterly)
- **Drift detection** --- Implement statistical monitoring for model degradation: population stability index (PSI) for feature distributions, calibration error trending, and AUROC tracking over time. Define thresholds that trigger investigation and potential model deactivation
- **Incident reporting** --- Establish an AI-specific incident reporting pathway: patient safety events potentially related to AI output, clinician reports of incorrect or harmful AI recommendations, equity-related concerns (AI produces different quality output for different populations), and security incidents involving AI systems
- **Incident investigation** --- For each reported AI incident: determine whether the AI output was a contributing factor, assess the model's performance on similar cases, evaluate whether the incident represents a systematic issue or an isolated case, and determine corrective action (retrain, reconfigure, restrict, or retire)
- **Annual review** --- Conduct an annual review of every deployed AI tool: performance metrics trending, incident history, vendor updates, regulatory changes, and continued clinical value assessment. Retire tools that no longer meet governance standards

---

## Step 5 --- Address Regulatory and Ethical Requirements

Ensure compliance with evolving AI regulations:

- **FDA SaMD compliance** --- For AI tools classified as SaMD: verify FDA clearance/approval for the intended use, ensure the tool is used within its labeled indications, report malfunctions through MedWatch if applicable, and track FDA's evolving AI/ML regulatory framework (predetermined change control plans, real-world performance monitoring)
- **State AI laws** --- Monitor and comply with state-specific AI regulations: transparency requirements (informing patients when AI is used in their care), algorithmic bias audit mandates, and AI procurement requirements for state-funded programs
- **CMS requirements** --- Track CMS rulemaking related to AI: requirements for AI transparency in Medicare Advantage, prior authorization AI disclosure requirements, and quality measure implications of AI-assisted documentation
- **Ethical framework** --- Adopt organizational AI ethics principles: beneficence (AI must benefit patients), non-maleficence (AI must not harm patients, including through bias), autonomy (patients and clinicians retain decision authority), justice (AI must not exacerbate health disparities), transparency (AI use is disclosed and explainable), and accountability (humans are responsible for AI-influenced decisions)
- **Patient communication** --- Define how patients are informed about AI use in their care: general disclosure in consent documents, specific notification when AI significantly influences clinical decisions, and patient right to request human-only assessment

- **Insurance and liability considerations** --- Consult with legal counsel and risk management regarding: professional liability coverage for AI-assisted clinical decisions, vendor indemnification for model failures, informed consent requirements for AI-influenced care, and documentation standards that protect clinicians who override AI recommendations
---

## Checkpoint B --- Governance Program Review

Assess governance program maturity:

- [ ] AI Governance Committee is chartered with appropriate membership and authority
- [ ] AI inventory is complete and covers all deployed and under-evaluation tools
- [ ] Risk classification is applied to every inventoried tool
- [ ] Validation requirements are defined by risk tier and enforced before deployment
- [ ] Bias assessment is completed for all Tier 1 clinical AI tools
- [ ] Monitoring infrastructure is operational for all deployed tools
- [ ] Incident reporting pathway is established and communicated to all clinical users
- [ ] Regulatory compliance is assessed for FDA SaMD and applicable state laws
- [ ] Shadow AI policy is communicated and enforcement mechanism is defined

- [ ] Generative AI use policy is published and communicated to all clinical staff
- [ ] Model cards (or equivalent documentation) are on file for all inventoried AI tools
- [ ] Liability and insurance implications of AI use have been reviewed with legal counsel
---

## Quality Audit

- [ ] Governance committee meets regularly with documented decisions
- [ ] Every deployed clinical AI has a named system owner
- [ ] Local validation is documented for all Tier 1 AI tools
- [ ] Bias assessment covers race, ethnicity, sex, age, and insurance type at minimum
- [ ] FDA SaMD assessments are on file for all potentially regulated AI tools
- [ ] Vendor contracts include transparency, performance, and notification requirements
- [ ] Monitoring metrics are tracked and reviewed per defined schedule
- [ ] AI incident reports are investigated with documented findings and corrective actions
- [ ] Annual review is completed for all deployed tools with renewal or retirement decision

- [ ] CHAI (Coalition for Health AI) guidelines are referenced in governance framework development
- [ ] Generative AI policy covers approved/prohibited use cases, PHI handling, and attestation requirements
- [ ] Model card documentation is maintained for all deployed and under-evaluation AI tools
- [ ] Insurance coverage adequacy for AI-assisted clinical decisions has been verified with risk management
---

## Guidelines

- AI governance is a clinical safety function, not a technology approval function. Frame governance around patient safety and health equity, not around innovation facilitation or IT procurement
- Require local validation for all clinical AI tools regardless of vendor claims. Performance on your patient population is the only performance that matters
- Bias assessment is not a one-time checkbox. Patient populations change, clinical practices evolve, and data pipelines shift. Re-assess bias with every major model update and at least annually
- Treat shadow AI (unauthorized use of ChatGPT, Bard, or other general-purpose AI for clinical purposes) as a patient safety and compliance issue. Clinicians using non-validated, non-BAA-covered AI tools to process patient information creates HIPAA and clinical risk
- Generative AI for clinical documentation requires particular scrutiny. Ambient documentation and AI-generated summaries can fabricate clinical details ("hallucinations") that become part of the permanent medical record
- Vendor transparency is a contractual negotiation, not a request. If a vendor will not disclose model features, training data demographics, and subgroup performance, that is a risk signal that governance should weigh heavily
- Do not conflate FDA clearance with clinical validation. FDA clears devices for safety and effectiveness based on the manufacturer's submission; your institution must still validate performance on your population
- AI governance policies must explicitly address generative AI use by patients (AI-generated patient portal messages, AI health advice) as well as by clinicians

- AI governance frameworks must address the speed of AI adoption. The gap between a clinician discovering a useful AI tool and deploying it in patient care can be days, not months. Governance processes that take 6 months to approve a tool will be circumvented; design governance that is risk-proportionate and efficient
- Maintain a distinction between AI that augments clinical decisions (acceptable with governance) and AI that replaces clinical decisions (requires extraordinary scrutiny). The line between augmentation and automation blurs quickly in practice