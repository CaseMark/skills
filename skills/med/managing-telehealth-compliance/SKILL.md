---
name: managing-telehealth-compliance
description: Evaluates telehealth program compliance with state licensing, prescribing, and reimbursement requirements. Use when assessing telehealth compliance, reviewing licensure requirements, or managing virtual care regulations.
tags:
  - management
  - healthcare-compliance
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Healthcare Compliance
    - HIPAA
    - Healthcare Regulation
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Telehealth Compliance

A structured framework for managing telehealth program compliance across state licensing, prescribing restrictions, HIPAA technical safeguards, reimbursement rules, informed consent requirements, and the evolving post-public health emergency regulatory landscape.

## Why This Skill Exists

Telehealth utilization has permanently expanded beyond pre-pandemic levels, but the regulatory framework remains fragmented across federal and state jurisdictions. Providers face a patchwork of state medical practice acts that define where the practice of medicine occurs (typically the patient's location), varying telehealth-specific licensing requirements, state-specific prescribing rules for telehealth encounters, and differing informed consent mandates. CMS telehealth reimbursement rules change frequently—many pandemic-era flexibilities have been extended through legislation (Consolidated Appropriations Act) but are not permanent. HIPAA's technology requirements apply to telehealth platforms, and the OCR enforcement discretion for non-HIPAA-compliant platforms that existed during the PHE has ended. State medical boards actively investigate unlicensed telehealth practice across state lines. Non-compliance exposes providers to state board discipline, malpractice liability (practicing without a valid license eliminates malpractice insurance coverage), federal reimbursement risk, and HIPAA enforcement. A structured compliance program is essential for any organization operating telehealth services.

---

## Checkpoint A — Program Scope Assessment

### Intake Questions

1. What telehealth modalities does the organization use—synchronous video, audio-only, asynchronous/store-and-forward, remote patient monitoring (RPM)?
2. In which states are patients located when receiving telehealth services? This determines which states' laws govern the encounter.
3. Are providers licensed in every state where patients are located, or does the organization rely on interstate licensure compacts (IMLC, NLC, PSYPACT)?
4. What telehealth technology platform is in use, and has it been verified as HIPAA-compliant with a BAA from the vendor?
5. Does the organization prescribe controlled substances via telehealth, and is DEA registration current for applicable states?
6. What payers reimburse telehealth services—Medicare, Medicaid (state-specific), commercial, employer-sponsored?
7. Does the organization obtain telehealth-specific informed consent?
8. What are the organization's credentialing and privileging procedures for telehealth providers?
9. Has the organization assessed malpractice insurance coverage for telehealth services across all states served?
10. Does the organization serve patients in states with specific telehealth practice standards (e.g., establishing patient-provider relationship requirements)?

### Required Documents

- Telehealth policies and procedures
- State-by-state licensure status for all telehealth providers
- Interstate medical licensure compact participation documentation
- Technology platform vendor contracts and BAAs
- HIPAA security risk assessment for telehealth infrastructure
- Telehealth-specific informed consent forms
- Credentialing and privileging documentation for telehealth providers
- Payer enrollment and reimbursement policies for telehealth
- DEA registrations for controlled substance prescribing via telehealth
- Malpractice insurance policy declarations showing telehealth coverage
- State telehealth regulatory requirement matrix

---

## Step 1 — Licensure and Scope of Practice Compliance

- **Patient Location Rule**: Confirm the organization applies the rule that the practice of medicine occurs where the patient is physically located at the time of the telehealth encounter. The provider must hold a valid, unrestricted license in that state (with limited exceptions for consultations and emergencies).
- **Interstate Medical Licensure Compact (IMLC)**: For physicians, assess eligibility for the IMLC, which provides an expedited pathway to licensure in member states. Note that IMLC issues a full license in each state—it is not a single multi-state license.
- **Nurse Licensure Compact (NLC)**: For nurses and APRNs, verify whether the provider holds a multistate license through the NLC and whether the patient's state is a compact member.
- **PSYPACT**: For psychologists, assess eligibility for PSYPACT (Psychology Interjurisdictional Compact) for telepsychology across member states.
- **State-Specific Telehealth Registrations**: Some states require separate telehealth registration or notification even with an active license (e.g., certain states require registration to provide telehealth to their residents).
- **Scope of Practice**: Verify that the services provided via telehealth are within the provider's scope of practice in the patient's state. Scope of practice for APRNs, PAs, and other non-physician providers varies significantly by state.
- **Corporate Practice of Medicine**: Assess whether the organization's telehealth structure complies with the patient's state corporate practice of medicine doctrine (CPOM restrictions prohibit non-physician entities from employing physicians in many states).

---

## Step 2 — Technology and HIPAA Compliance

- **Platform Assessment**: Verify the telehealth platform meets HIPAA Security Rule requirements—encryption in transit (TLS 1.2+) and at rest, access controls, audit logging, automatic session timeout, and data integrity protections.
- **Business Associate Agreement**: Confirm a BAA is executed with the telehealth platform vendor covering all HIPAA requirements per § 164.504(e).
- **Post-PHE Enforcement**: Confirm the organization is not relying on pandemic-era OCR enforcement discretion for non-HIPAA-compliant platforms (e.g., FaceTime, Skype consumer version). OCR has returned to standard enforcement.
- **Patient Authentication**: Verify processes for authenticating patient identity at the start of each telehealth encounter to prevent unauthorized access to PHI.
- **Recording and Storage**: If telehealth sessions are recorded, verify patient consent for recording (per state wiretapping/recording consent laws—one-party vs. all-party consent) and that recordings are stored in HIPAA-compliant systems with appropriate retention and destruction policies.
- **RPM Device Security**: For remote patient monitoring, assess the security of RPM devices and data transmission pathways—IoT medical devices may introduce vulnerabilities not present in standard platforms.

---

## Step 3 — Prescribing and Controlled Substances

- **Telehealth Prescribing Standards**: Verify the organization's telehealth prescribing practices comply with each patient-state's requirements for establishing a valid provider-patient relationship before prescribing. Many states require at least one synchronous encounter (video or in-person) before prescribing.
- **Controlled Substance Prescribing**: The Ryan Haight Act (21 U.S.C. § 829(e)) generally requires an in-person evaluation before prescribing controlled substances via telemedicine. Assess whether any exceptions apply—DEA-registered telemedicine practitioners, public health emergencies, VA providers, or Indian Health Service providers.
- **DEA Telemedicine Registrations**: Monitor DEA's evolving telemedicine prescribing regulations. The DEA has proposed special registration requirements for telemedicine prescribing of controlled substances.
- **State Prescribing Restrictions**: Some states impose additional restrictions on telehealth prescribing—specific medication categories prohibited, prescription quantity limits, or mandatory follow-up requirements.
- **EPCS Compliance**: If using electronic prescribing for controlled substances (EPCS), verify compliance with DEA EPCS requirements including two-factor authentication and application certification.

---

## Step 4 — Reimbursement Compliance

- **Medicare Telehealth**: Verify services meet CMS telehealth requirements for the applicable period. Key requirements include: service is on the Medicare Telehealth Services list, appropriate place of service code (POS 02 for telehealth, POS 10 for patient's home), modifier 95 for synchronous telehealth, and compliance with originating site requirements (if applicable for the service type).
- **Audio-Only Services**: Assess whether audio-only (telephone) services are billable—CMS has extended audio-only coverage for certain services but with specific requirements and limitations.
- **Medicaid Telehealth**: Medicaid telehealth coverage and reimbursement vary dramatically by state. Verify the patient's state Medicaid program covers the specific service via the specific modality (video, audio-only, store-and-forward, RPM).
- **Commercial Payer**: Review commercial payer telehealth policies and state telehealth parity laws that may require commercial insurers to cover and/or reimburse telehealth services on parity with in-person services.
- **Documentation Requirements**: Verify telehealth encounter documentation meets the same E/M documentation standards as in-person encounters. Document the technology used, patient location, provider location, and any technology limitations encountered.
- **Billing Compliance**: Ensure coding and billing for telehealth services uses correct CPT codes, modifiers, and place-of-service codes to avoid false claims risk.

---

## Step 5 — Informed Consent and Clinical Standards

- **Telehealth-Specific Consent**: Verify the organization obtains telehealth-specific informed consent addressing: the nature of telehealth, technology risks (connection failure, privacy limitations), alternatives to telehealth, right to refuse telehealth, and any state-specific consent requirements.
- **State Consent Requirements**: Map state-specific telehealth consent requirements—some states require written consent, some allow verbal consent documented in the record, and some require specific disclosures.
- **Standard of Care**: Verify that clinical protocols for telehealth encounters maintain the same standard of care as in-person encounters. The standard of care is not lowered because the encounter is virtual—if a condition cannot be adequately assessed via telehealth, the provider must refer for in-person evaluation.
- **Emergency Protocols**: Verify the organization has protocols for managing emergencies that arise during telehealth encounters—including verifying the patient's physical location at the start of each encounter to enable emergency dispatch if needed.
- **Documentation**: Confirm telehealth encounters are documented in the medical record with the same completeness as in-person encounters, plus telehealth-specific elements (modality, platform, patient/provider locations, technology issues).

---

## Checkpoint B — Program Validation

1. Confirm all telehealth providers are licensed in every state where patients are located at the time of service.
2. Verify the telehealth platform has a current BAA and meets HIPAA Security Rule requirements.
3. Confirm controlled substance prescribing complies with the Ryan Haight Act and applicable state requirements.
4. Verify telehealth-specific informed consent is obtained and documented per state requirements.
5. Confirm billing and coding for telehealth services uses correct codes, modifiers, and POS codes.
6. Verify malpractice insurance coverage extends to telehealth services in all states served.
7. Confirm credentialing and privileging processes address telehealth per CMS requirements.
8. Verify emergency protocols include patient location verification for emergency dispatch capability.

---

## Quality Audit

- [ ] State-by-state licensure matrix current for all telehealth providers
- [ ] Interstate compact participation documented where applicable (IMLC, NLC, PSYPACT)
- [ ] Telehealth platform BAA executed and HIPAA security assessment completed
- [ ] Post-PHE platform compliance verified (no reliance on expired enforcement discretion)
- [ ] Ryan Haight Act compliance verified for controlled substance prescribing
- [ ] DEA registrations current for applicable states and prescribing activities
- [ ] State prescribing restrictions mapped and provider workflows updated
- [ ] Medicare telehealth billing uses correct CPT codes, modifiers, and POS codes
- [ ] State Medicaid telehealth coverage verified for each service and modality
- [ ] Telehealth-specific informed consent obtained per state requirements
- [ ] Emergency protocols include patient location verification
- [ ] Malpractice insurance confirmed for telehealth across all service states

---

## Guidelines

- The practice of medicine occurs where the patient is located—this is the foundational principle of telehealth licensure compliance. Providers who treat patients in states where they lack licensure are practicing medicine without a license, which exposes them to state board discipline, criminal liability, and malpractice insurance voidance.
- HIPAA applies fully to telehealth. The pandemic-era OCR enforcement discretion for non-compliant platforms has ended. Organizations must use HIPAA-compliant platforms with BAAs in place.
- Telehealth reimbursement rules are in flux. Medicare flexibilities enacted through legislation have specific expiration dates and may not be renewed. Build compliance monitoring into the reimbursement process to adapt as rules change.
- The standard of care for telehealth is the same as for in-person care. Telehealth is a modality, not a lower standard. When a condition cannot be adequately assessed via telehealth, the provider must arrange in-person evaluation.
- Controlled substance prescribing via telehealth remains heavily regulated. The Ryan Haight Act in-person requirement has narrow exceptions, and DEA's telemedicine registration framework continues to evolve. Monitor DEA rulemaking closely.
- State telehealth laws change frequently—what was accurate last year may be outdated today. Maintain a current state regulatory matrix and review it quarterly.
- This skill produces telehealth compliance assessment output, not legal advice. Telehealth regulatory decisions should involve qualified healthcare regulatory counsel familiar with the specific states involved.
