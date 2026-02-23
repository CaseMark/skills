---
name: telemedicine-consent
description: Drafts comprehensive telemedicine consent and policy documents covering HIPAA compliance, informed consent, prescribing limitations, privacy architecture, and patient acknowledgment sections. Ensures compliance with federal and state telemedicine regulations, DEA prescribing rules, and Interstate Medical Licensure Compact requirements. Use when drafting telehealth consent forms, telemedicine policies, remote patient monitoring agreements, or virtual care informed consent documents.
tags:
  - agreement
  - drafting
  - regulatory
---

# Telemedicine Consent and Policy Document

Drafts a dual-purpose document functioning as both informed consent instrument and operational policy framework for telehealth service delivery.

## Prerequisites

1. **Provider information** — legal entity name, professional designations, state licensure details
2. **Jurisdiction** — state(s) where patients are located during consultations
3. **Technology stack** — platforms used (video, store-and-forward, RPM devices, mHealth apps)
4. **Existing policies** — any institutional consent forms, privacy notices, or credentialing requirements
5. **Prescribing scope** — whether controlled substances will be prescribed via telemedicine
6. **Billing model** — insurance-based, self-pay, or hybrid

## Output Structure

### Section 1: Patient Consent & Telemedicine Explanation

| Element | Requirements |
|---|---|
| Patient ID | Full legal name, DOB |
| Provider ID | Legal entity name, professional designations |
| Modalities | Enumerate each: synchronous video, asynchronous store-and-forward, RPM, mHealth |
| Plain-language definition | Explain telemedicine without jargon; maintain legal sufficiency for informed consent |
| Benefits acknowledged | Access, convenience, scheduling flexibility |
| Limitations acknowledged | No physical exam, limited emergency response, technology dependency |

### Section 2: Risk Disclosures

Draft explicit patient acknowledgments for each risk category:

- [ ] Cannot perform hands-on examination or palpation
- [ ] Limited emergency response capability during/after sessions
- [ ] Transmission interruptions (audio/video)
- [ ] Potential unauthorized access despite encryption
- [ ] Technical failures requiring rescheduling
- [ ] Technology limitations may delay diagnosis

### Section 3: Patient Responsibilities

- [ ] Private, quiet location free from unauthorized listeners
- [ ] Adequate bandwidth and device functionality; test in advance
- [ ] Backup communication method available
- [ ] Complete, accurate medical history, medications, allergies
- [ ] Emergency contact information readily accessible
- [ ] Understanding of when to call 911 vs. use telemedicine

### Section 4: Privacy & Security (HIPAA Compliance)

| Topic | Required Content |
|---|---|
| Encryption | End-to-end for video; encrypted storage for recordings/transmitted data |
| Data retention | Duration, storage location, access controls |
| Session recording | Policy on recording, pre-recording notification, patient copy requests |
| Security limitations | Acknowledge no absolute guarantee despite administrative/physical/technical safeguards |
| Breach notification | Per HIPAA Breach Notification Rule, 45 CFR §§ 164.400–414 [VERIFY] |

### Section 5: Regulatory Compliance & Licensure

- Confirm provider licensure in patient's physical location state
- If interstate: address Interstate Medical Licensure Compact participation or individual state licenses
- State that telemedicine is held to same standard of care as in-person practice
- Preserve patient right to file complaints with state medical boards

### Section 6: Third-Party Participation

- Enumerate who may be present: family, caregivers, interpreters, students, residents, care team
- Patient must be informed of all participants and may object
- Interpretation services at no cost for limited English proficiency patients
- Right to refuse telemedicine at any time without prejudice to in-person care

### Section 7: Prescribing Policy

| Constraint | Detail |
|---|---|
| Clinical discretion | All prescribing at provider's professional judgment |
| DEA controlled substances | In-person exam generally required before prescribing Schedules II–V; note authorized exceptions (21 USC § 831) [VERIFY] |
| State restrictions | Incorporate state-specific rules if more stringent than federal |
| Excluded categories | Identify medication classes requiring in-person eval (opioids, benzodiazepines, stimulants) |

### Section 8: Clinical Scope Limitations

Conditions **unsuitable** for telemedicine (include but not limited to):

- Acute chest pain, severe abdominal pain, significant trauma
- Altered mental status
- Conditions requiring physical exam techniques (palpation, manipulation)
- Presentations requiring immediate diagnostic testing/imaging
- Any situation where provider determines standard of care cannot be met remotely

### Section 9: Care Coordination & Billing

- Documentation standards match in-person visit requirements
- Records available to other treating providers with authorization
- Follow-up protocols: in-person triggers, lab/imaging result timelines
- Billing: telemedicine-specific CPT codes and modifiers
- Patient responsible for copays, coinsurance, deductibles, non-covered services
- Cancellation/no-show policy for telemedicine appointments

### Section 10: Acknowledgment & Signatures

**Patient certification block** — patient certifies:
- [ ] Read entire document (or had it read to them)
- [ ] Adequate opportunity to ask questions
- [ ] Understands nature, benefits, risks, and limitations
- [ ] Voluntarily consents
- [ ] Understands right to withdraw consent at any time

**Signature blocks:**

```
Patient Signature: ___________________  Date: ___________
Printed Name: _______________________  DOB: ____________

Guardian/Legal Representative (if applicable):
Signature: __________________________  Date: ___________
Printed Name: _______________________  Relationship: ___________
Legal Authority: _____________________

Witness (if required by state law):
Signature: __________________________  Date: ___________

Provider Acknowledgment:
Signature: __________________________  Date: ___________
```

**Savings clause** — include verbatim:
> Execution of this consent does not waive any legal rights or remedies under federal or state law, does not limit the right to file complaints with medical licensing boards or privacy officers, and does not restrict the ability to pursue legal action. This document supplements rather than replaces other consent forms or agreements. In the event of conflict, the interpretation most protective of patient rights and safety prevails.

## Guidelines

- Use plain language accessible to patients with varying health literacy; define technical terms on first use
- Active voice throughout
- Adapt prescribing section to jurisdiction — DEA federal rules are the floor; state rules may be stricter
- If provider participates in Medicare/Medicaid telehealth, verify current CMS coverage policies
- Mark any statutory citation not independently verified with `[VERIFY]`
- Do not include fee schedules or specific dollar amounts — reference billing department
- Minor consent: require guardian signature plus specify state-specific age-of-consent exceptions (e.g., reproductive health, mental health, substance abuse treatment)
- Electronic signatures must comply with ESIGN Act (15 USC § 7001) [VERIFY] and applicable state UETA adoption
