---
name: managing-patient-portal-content
description: Creates patient-facing health information content with health literacy and accessibility standards. Use when developing portal content, writing patient communications, or managing digital health tools.
tags:
  - management
  - health-informatics
  - patient-care
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

# Managing Patient Portal Content

Creates patient-facing health information content that meets health literacy standards, accessibility requirements, and ONC patient access mandates. This skill covers content creation, USCDI data presentation, portal configuration, and patient engagement optimization.

## Why This Skill Exists

The 21st Century Cures Act requires that patients have electronic access to their health information without special effort (ONC 170.315(e)(1)). Patient portals are the primary channel for this access, but raw clinical data displayed without context confuses patients and generates unnecessary clinical calls. Meanwhile, portal adoption stalls at 40-60% in most organizations because content is written at clinical literacy levels rather than the recommended 6th-8th grade reading level. This skill structures content creation that is clinically accurate, patient-comprehensible, and compliant with information blocking rules.


Patient portal engagement directly affects clinical outcomes. Studies show that patients who actively use portals have better chronic disease control, higher medication adherence, and greater satisfaction with care. However, portal adoption is inequitable: older adults, patients with limited English proficiency, and low-income populations have lower activation rates, creating a digital divide that mirrors existing health disparities.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Portal platform** --- Which patient portal is in use? (MyChart, FollowMyHealth, Cerner Patient Portal, custom)
2. **Content scope** --- What content is being created or revised? (Lab result explanations, medication instructions, discharge summaries, appointment prep, preventive care reminders)
3. **Target population** --- Patient demographics relevant to content design: primary languages, age distribution, chronic disease prevalence, digital literacy assessment results
4. **USCDI display requirements** --- Which USCDI v4 data classes will patients see? (Clinical Notes release per Cures Act, lab results, medications, immunizations)
5. **Accessibility requirements** --- WCAG 2.1 AA compliance level? State or organizational accessibility mandates?
6. **Regulatory context** --- Cures Act clinical notes release timeline, state-specific result release rules, 42 CFR Part 2 considerations for substance use data
7. **Current portal metrics** --- Activation rate, login frequency, message volume, patient satisfaction scores

### Required Documents

- Current portal content inventory (all patient-facing text, FAQs, instructions)
- Portal configuration documentation (result release rules, note release settings)
- Patient population demographic and language profile
- Health literacy assessment data (if available)
- ONC certification requirements for patient portal features (170.315(e)(1))
- ADA/Section 508 compliance checklist

---

## Step 1 --- Audit Existing Content

Evaluate current portal content systematically:

- **Readability scoring** --- Run all patient-facing text through validated readability tools: Flesch-Kincaid Grade Level (target: 6th-8th grade), SMOG Index, and Suitability Assessment of Materials (SAM)
- **Clinical accuracy review** --- Verify that explanatory content matches current clinical guidelines. Outdated content (e.g., old cholesterol targets, retired screening recommendations) must be flagged
- **USCDI completeness** --- Verify that all required USCDI v4 data classes are surfaced in the portal: Allergies, Assessment/Plan, Care Team, Clinical Notes, Encounter Information, Health Insurance, Immunizations, Laboratory, Medications, Patient Demographics, Problems, Procedures, Vital Signs, Clinical Tests, Diagnostic Imaging
- **Language availability** --- Identify content available only in English. Prioritize translation for the top 3 non-English languages in the patient population
- **Accessibility gaps** --- Test portal with screen reader (JAWS, NVDA), keyboard-only navigation, and high-contrast mode. Document failures against WCAG 2.1 AA criteria

- **Engagement analytics** --- Analyze current portal usage patterns: which features are most/least used, time spent per session, pages per visit, search queries (what are patients looking for but not finding?), and abandonment points in key workflows (messaging, appointment scheduling, bill pay)
---

## Step 2 --- Design Content Architecture

Structure content for progressive disclosure:

- **Result display hierarchy** --- Show: result name (plain language, not LOINC code), value with units, reference range, interpretation flag (normal, abnormal, critical), and expandable plain-language explanation
- **Clinical notes presentation** --- Per Cures Act, clinical notes (History & Physical, Progress Notes, Consultation Notes, Discharge Summaries, Imaging Narratives, Lab Report Narratives, Pathology Report Narratives, Procedure Notes) must be available to patients. Add contextual headers explaining what each note type contains
- **Medication content** --- Display: medication name (both generic and brand), dose, route, frequency, prescriber, purpose (linked to problem list entry when available), and patient-friendly side effect summary
- **Alert and flag design** --- Define how abnormal results, overdue preventive care, and medication interaction warnings are visually presented. Use color coding that passes WCAG contrast ratios (4.5:1 minimum for normal text)
- **Navigation taxonomy** --- Organize content by patient mental model ("My Test Results," "My Medications," "My Visits"), not by clinical system architecture

---

## Step 3 --- Write Patient-Facing Content

Apply health literacy principles to every content item:

- **Plain language rules** --- Use active voice, short sentences (< 20 words), common words (e.g., "high blood sugar" not "hyperglycemia"), and define medical terms on first use
- **Teach-back structure** --- End action-oriented content with a question: "Can you describe what you should do if your blood sugar is above 250?"
- **Numeracy support** --- Present lab values with visual context: "Your HbA1c is 7.2%. Your target is below 7%. This means your average blood sugar over the past 3 months is slightly above your goal."
- **Cultural sensitivity** --- Avoid idioms, cultural assumptions, and imagery that does not represent the patient population. Use person-first language ("person with diabetes" not "diabetic patient")
- **Action orientation** --- Every content piece should answer: "What does this mean for me?" and "What should I do next?" If no patient action is needed, state that explicitly

- **AI-generated content considerations** --- If using AI to generate patient-facing content or message responses, implement: human clinical review before publication, readability verification, hallucination detection, cultural appropriateness review, and clear disclosure that content was AI-assisted
---

## Step 4 --- Configure Result and Note Release

Implement release rules that comply with Cures Act while supporting clinical workflow:

- **Immediate release categories** --- Most lab results and clinical notes must be released without delay per information blocking rules. Configure default to immediate release
- **Permitted delay scenarios** --- Document and configure the narrow exceptions where delay is permitted: (a) results requiring further testing to confirm (e.g., pathology pending), (b) results where immediate release could cause harm per clinician assessment (must be individually determined, not blanket policy)
- **Sensitive result handling** --- Configure appropriate release rules for: HIV results (state law dependent), genetic test results (GINA considerations), substance use data (42 CFR Part 2), mental health notes (state-specific)
- **Proxy access** --- Configure caregiver proxy access with age-appropriate permissions (adolescent privacy protections vary by state; typically ages 12-17 have restricted proxy access)
- **Provider notification** --- Ensure clinicians are notified when results release to patients so they can proactively address questions before patients call

---

## Step 5 --- Implement Accessibility

Ensure portal content meets accessibility standards:

- **WCAG 2.1 AA compliance** --- All content perceivable (text alternatives for images, captions for video), operable (keyboard accessible, sufficient time limits), understandable (readable, predictable), and robust (compatible with assistive technology)
- **Mobile responsiveness** --- Test all content on mobile devices (iOS and Android) since 60%+ of portal access is mobile
- **Font and layout** --- Minimum 16px font for body text, 1.5 line spacing, maximum 80 characters per line, high-contrast color schemes
- **Alternative formats** --- Provide content in PDF (tagged for accessibility), audio, and video with closed captions for key educational materials
- **Translation workflow** --- Use certified medical translators (not machine translation alone) for patient-facing clinical content. Machine translation is acceptable only for non-clinical administrative content with human review

- **Digital navigation support** --- For patients with low digital literacy, implement: video tutorials for common portal tasks, tech support hotline with multilingual capability, in-person portal enrollment assistance at registration, and community health worker-led digital literacy programs
---

## Checkpoint B --- Content Release Review

Before publishing new or revised portal content:

- [ ] All content scores 8th grade or below on Flesch-Kincaid Grade Level
- [ ] Clinical accuracy is verified by a clinical reviewer
- [ ] USCDI v4 data classes are displayed correctly in the portal
- [ ] Result release rules comply with Cures Act information blocking rules
- [ ] Accessibility testing passes WCAG 2.1 AA criteria
- [ ] Content is available in the top languages for the patient population
- [ ] Proxy access rules comply with state adolescent privacy laws
- [ ] Patient feedback has been incorporated from usability testing

- [ ] Engagement analytics are tracked with identified improvement opportunities
- [ ] AI-generated content (if applicable) has human clinical review workflow
- [ ] Digital navigation support is available for low-digital-literacy patients
---

## Quality Audit

- [ ] Readability scores are documented for all patient-facing content
- [ ] Clinical notes release configuration matches Cures Act requirements (all 8 note types)
- [ ] Information blocking exceptions are individually documented, not applied as blanket policies
- [ ] Portal meets ONC certification criterion 170.315(e)(1) requirements
- [ ] Accessibility compliance documentation is current (VPAT or equivalent)
- [ ] Language access plan covers LEP (Limited English Proficiency) patient population
- [ ] Result release timing is configured per organizational policy and regulatory requirements
- [ ] Patient engagement metrics (activation, usage, satisfaction) are tracked and reported quarterly
- [ ] Content governance process defines review cadence and responsible owners for each content area

- [ ] Portal engagement metrics are stratified by demographics to identify equity gaps
- [ ] AI-generated patient content has documented review and approval workflow
- [ ] Digital navigation and literacy support programs are operational for underserved populations
- [ ] Patient feedback mechanisms are active with documented response to common themes
---

## Guidelines

- Default to immediate release for all results and notes. The Cures Act information blocking rules place the burden of justification on withholding, not on releasing
- Never use medical jargon in patient-facing content without a plain-language explanation. "Elevated troponin" means nothing to most patients; "a blood test that checks for heart damage" communicates effectively
- Test content with actual patients from the target population before publishing. Provider assumptions about patient comprehension are consistently inaccurate
- Treat portal content as clinical content requiring the same governance as order sets and clinical documentation templates
- Monitor patient call volume after content changes. Increased calls about a specific topic indicate the content failed to answer patient questions
- For lab result display, always show the reference range alongside the value. A potassium of 4.0 is meaningless without the 3.5-5.0 range context
- Comply with both federal Cures Act requirements and state-specific result release laws. State laws that are more protective of patients may impose additional requirements beyond federal mandates
- Review and update all portal content at least annually, and immediately when clinical guidelines change

- Portal design should follow universal design principles: if it works for the patient with the lowest digital literacy, it works for everyone. Design for the most challenged user, not the most capable
- Measure portal success by clinical outcomes (improved disease control, fewer unnecessary calls, timely preventive care) not just adoption metrics (activation rate, login count). High activation with no outcome improvement means the portal is being used but not effectively