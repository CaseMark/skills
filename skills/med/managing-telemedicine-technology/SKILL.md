---
name: managing-telemedicine-technology
description: Evaluates and implements telemedicine technology platforms with clinical workflow integration. Use when selecting telehealth platforms, integrating virtual care technology, or managing telemedicine infrastructure.
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

# Managing Telemedicine Technology

Evaluates and implements telemedicine technology platforms with clinical workflow integration, regulatory compliance, and quality measurement. This skill covers platform selection, EHR integration design, remote monitoring device management, and telehealth program operations.

## Why This Skill Exists

Telemedicine has transitioned from pandemic emergency to permanent care delivery model, but technology implementation remains fragmented. Organizations often deploy multiple telehealth platforms without EHR integration, creating documentation silos, billing complexity, and patient confusion. The regulatory landscape (CMS telehealth waivers, state licensure compacts, DEA prescribing rules, ADA accessibility requirements) adds compliance burden. Meanwhile, patient experience suffers when virtual visits require separate portals, manual appointment coordination, and disconnected health records. This skill structures the technology evaluation and implementation process to deliver integrated, compliant, and high-quality virtual care.


The permanent telehealth landscape post-pandemic is defined by CMS rulemaking that has made many pandemic waivers permanent, the expansion of the Interstate Medical Licensure Compact (IMLC) to 40+ states, DEA's evolving telehealth prescribing rules for controlled substances, and the emergence of asynchronous and AI-augmented virtual care models. Organizations must build sustainable telehealth infrastructure, not pandemic-era temporary solutions.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Telehealth modalities** --- Which modalities are in scope? (Synchronous video visits, asynchronous store-and-forward, remote patient monitoring, e-consults/e-referrals, digital triage, chatbot-based intake)
2. **Clinical programs** --- Which clinical services will use telehealth? (Primary care, behavioral health, dermatology, post-surgical follow-up, chronic disease management, ICU tele-critical care)
3. **Current technology** --- What telehealth platforms are currently in use? How are they integrated (or not) with the EHR?
4. **EHR platform** --- Which EHR and patient portal are in use? What native telehealth capabilities does the EHR offer? (Epic Telehealth, Cerner Video Visit, etc.)
5. **Patient population** --- Demographics, digital literacy levels, device access (smartphone vs. computer), broadband availability, language needs
6. **Regulatory context** --- State licensure requirements for providers, CMS telehealth billing rules (originating site, eligible services, modifiers), DEA prescribing for controlled substances via telehealth, state parity laws
7. **Quality and outcome goals** --- What metrics define telehealth program success? (Visit completion rate, patient satisfaction, no-show rate comparison, clinical outcomes, cost per visit)

### Required Documents

- Current telehealth platform inventory with contract terms and utilization data
- EHR telehealth configuration documentation
- CMS telehealth services list (eligible CPT codes and place of service requirements)
- State telehealth regulations summary for operating states
- Patient technology access survey results
- Clinical workflow documentation for target telehealth services

---

## Step 1 --- Evaluate Platform Requirements

Define the technology requirements based on clinical needs:

- **EHR integration depth** --- Prioritize platforms that integrate at the workflow level, not just the data level. Target: single-click visit launch from the EHR scheduling module, automatic documentation of telehealth encounter type, structured data capture during virtual visit, and seamless transition between in-person and virtual encounters
- **Video and audio quality** --- Define minimum requirements: 720p video resolution, adaptive bitrate for low-bandwidth connections, audio-only fallback for poor video connectivity, HIPAA-compliant recording capability for specified use cases
- **Patient experience** --- Evaluate from the patient perspective: no app download required (browser-based preferred), one-click join from the patient portal or text/email link, mobile-optimized, waiting room functionality, interpreter integration for LEP patients, accessibility for hearing-impaired (live captioning) and vision-impaired patients
- **Remote patient monitoring (RPM)** --- For RPM programs, evaluate: supported device types (blood pressure cuff, glucometer, pulse oximeter, weight scale, continuous glucose monitor), data transmission reliability, EHR integration for vitals flowsheet population, alert thresholds and escalation workflow
- **Provider tools** --- Assess provider-facing features: screen sharing for patient education, peripheral device support (digital stethoscope, dermatoscope, otoscope for remote presenter models), multi-party capability (interpreter, caregiver, specialist), and documentation tools

- **AI-augmented telehealth** --- Evaluate emerging AI capabilities: AI-powered triage before virtual visits, ambient documentation during video encounters, automated post-visit summary generation, and AI-assisted clinical decision support during the encounter. Each capability requires separate governance review (see managing-health-ai-governance)
---

## Step 2 --- Design Clinical Workflows

Map telehealth into clinical operations:

- **Scheduling workflow** --- Define the scheduling process: telehealth visit type in the EHR scheduler, visit modality indicator (video, phone, asynchronous), pre-visit technology check (sent 24 hours before visit), and appointment reminder with join link
- **Check-in and intake** --- Design the virtual check-in: patient identity verification (DOB, address, photo ID for new patients), insurance verification, consent for telehealth (electronic, documented in EHR), intake questionnaires completed before the visit populates the chart
- **Clinical encounter** --- Structure the virtual encounter: provider workflow for launching the video session, structured documentation template for telehealth visits (including attestation of modality used, patient location, and provider location), peripheral device integration if applicable, and prescription workflow (e-prescribing with telehealth-specific considerations for controlled substances per DEA rules)
- **Post-visit workflow** --- Define post-visit processes: after-visit summary delivery via patient portal, follow-up scheduling (virtual or in-person), referral generation, lab order placement (patient directed to nearest lab draw site), and billing capture (correct CPT code, place of service 02 or 10, telehealth modifier 95 or GT per payer)
- **Escalation pathway** --- Define when a virtual visit must convert to in-person: clinical findings requiring physical examination, technology failure mid-visit, patient safety concerns. Document the escalation workflow including same-day scheduling capability

---

## Step 3 --- Implement Technical Infrastructure

Build the technology foundation:

- **Network and bandwidth** --- Ensure provider locations have symmetric bandwidth adequate for video (minimum 2 Mbps up/down per concurrent session). For hospital-based tele-programs (tele-ICU, tele-stroke), dedicate network capacity with QoS prioritization
- **HIPAA compliance** --- Verify platform compliance: BAA executed with telehealth vendor, end-to-end encryption for video/audio, compliant data storage, audit logging of all sessions, and no recording without explicit consent
- **Device management** --- For RPM programs, implement device lifecycle management: patient device provisioning, cellular or Bluetooth connectivity configuration, battery monitoring, device retrieval upon program completion, and infection control for shared devices
- **EHR interface build** --- Implement integration interfaces: appointment scheduling feed (EHR to telehealth platform), encounter documentation return (telehealth platform to EHR), RPM vitals feed (device gateway to EHR flowsheet), and billing data capture
- **Failover and redundancy** --- Design failover for telehealth infrastructure: audio-only fallback for video failure, alternative platform for primary platform outage, phone-based visit as last resort with documented protocol

- **Hybrid care model support** --- Design technology infrastructure to support seamless hybrid care: patient ability to convert between in-person and virtual mid-episode, shared care plans across modalities, continuous RPM data feeding into both virtual and in-person encounters, and scheduling systems that optimize visit modality based on clinical need and patient preference
---

## Step 4 --- Address Regulatory and Billing Compliance

Ensure the telehealth program operates within regulatory boundaries:

- **Provider licensure** --- Verify that all telehealth providers are licensed in the state where the patient is located at the time of service. Track multi-state licensure via Interstate Medical Licensure Compact (IMLC) or Psychology Interjurisdictional Compact (PSYPACT) where applicable
- **Billing compliance** --- Configure correct billing: CPT/HCPCS codes eligible for telehealth (reference the CMS Telehealth Services list updated quarterly), place of service codes (02 for telehealth into patient home, 10 for telehealth into healthcare facility), and modifiers (95 for synchronous real-time, GQ for store-and-forward, GT if required by payer)
- **Prescribing rules** --- For controlled substance prescribing via telehealth, comply with DEA requirements: Ryan Haight Act in-person examination requirement (unless a valid exception applies), DEA registration in patient's state, state-specific telehealth prescribing rules
- **Consent documentation** --- Document patient consent for telehealth in the EHR: acknowledgment of technology risks, agreement to virtual care modality, understanding of limitations compared to in-person care. Consent may be verbal (documented in the note) or electronic (portal-based)
- **Payer-specific rules** --- Map payer-specific telehealth policies: commercial payer telehealth parity laws vary by state, Medicaid telehealth coverage varies by state, Medicare rules differ from commercial and Medicaid. Maintain a payer matrix updated quarterly

---

## Step 5 --- Monitor and Optimize

Track telehealth program performance:

- **Utilization metrics** --- Monitor: telehealth visit volume by modality (video, phone, asynchronous), visit completion rate (completed/scheduled), no-show rate comparison (telehealth vs. in-person), conversion-to-in-person rate, and utilization by provider and specialty
- **Technical quality** --- Track: video connection success rate, average connection time, mid-visit disconnection rate, audio-only fallback rate, patient-reported technology difficulty, and help desk call volume for telehealth issues
- **Clinical quality** --- Measure clinical outcomes for telehealth patients vs. in-person comparators: HbA1c control for diabetes management, PHQ-9 improvement for behavioral health, 30-day readmission rates for post-discharge follow-up, and adherence to preventive care gaps
- **Patient experience** --- Deploy post-visit surveys: overall satisfaction, ease of technology use, perceived quality of clinical interaction, willingness to use telehealth again, Net Promoter Score comparison with in-person visits
- **Financial performance** --- Track revenue per telehealth visit, denial rate by payer, and cost per visit (technology platform cost + provider time + support staff time). Compare against in-person visit economics

- **Digital equity assessment** --- Conduct a formal digital equity assessment for the telehealth program: broadband access maps for the patient population, smartphone/computer ownership by demographic segment, digital literacy survey results, and language access capability. Use findings to design alternative access pathways (audio-only visits, community access points, device lending programs)
---

## Checkpoint B --- Telehealth Program Review

Before scaling the telehealth program:

- [ ] Platform is integrated with EHR for scheduling, documentation, and billing
- [ ] Clinical workflows are documented and validated for each telehealth service line
- [ ] Provider training is completed with competency verification
- [ ] Patient consent process is implemented in the EHR
- [ ] Billing configuration is validated against CMS and commercial payer rules
- [ ] Provider licensure is verified for all states where patients are located
- [ ] RPM device management process is operational (if applicable)
- [ ] Technical quality metrics meet minimum thresholds (connection success > 95%)

- [ ] AI-augmented telehealth capabilities (if deployed) have governance approval and monitoring
- [ ] Hybrid care model technology supports seamless transitions between modalities
- [ ] Digital equity assessment completed with alternative access pathways implemented
---

## Quality Audit

- [ ] Telehealth platform has executed BAA and meets HIPAA technical safeguard requirements
- [ ] EHR integration captures all required data elements for documentation and billing
- [ ] Provider licensure tracking covers all active telehealth states
- [ ] Billing compliance is validated with correct CPT codes, POS, and modifiers per payer
- [ ] DEA prescribing compliance is documented for controlled substance programs
- [ ] Patient accessibility is addressed (LEP interpretation, ADA compliance, low-bandwidth support)
- [ ] Clinical quality metrics are tracked and compared against in-person benchmarks
- [ ] Technology failure protocols are documented and tested
- [ ] Program economics are tracked with cost-per-visit and revenue analysis

- [ ] AI-augmented telehealth features have completed governance review per institutional AI policy
- [ ] Hybrid care workflows are validated for seamless in-person/virtual transitions
- [ ] Digital equity assessment is documented with remediation plan for identified gaps
- [ ] CMS telehealth services list is reviewed quarterly for billing compliance updates
---

## Guidelines

- EHR-integrated telehealth is non-negotiable. Standalone platforms that create parallel documentation workflows will be abandoned by clinicians and generate incomplete records
- Audio-only visits are a permanent modality, not a pandemic workaround. Design workflows that support phone visits for patients without video capability while maintaining documentation quality
- Telehealth does not eliminate health disparities; it can amplify them. Patients without smartphones, broadband, or digital literacy are excluded unless the program actively addresses access barriers
- Test the patient experience from the patient's device, not from the IT team's workstation. What works on a hospital-grade computer with enterprise internet may fail on a patient's 5-year-old smartphone with cellular data
- Billing complexity is the most common source of telehealth revenue loss. Invest in billing team training and automated charge capture validation
- RPM programs require clinical workflow design, not just device distribution. Sending a patient home with a blood pressure cuff without defining who reviews the data, what thresholds trigger action, and how the patient is contacted is a liability, not a program
- State telehealth regulations change frequently. Maintain a regulatory tracking process with at least quarterly review
- Telehealth consent should be lightweight and not burdensome. A 5-page consent form requiring wet signature defeats the purpose of convenient virtual care

- Telehealth technology selection should prioritize EHR-native solutions over best-of-breed standalone platforms. The documentation, billing, and workflow integration advantages of EHR-native telehealth outweigh the feature advantages of standalone platforms in most clinical settings
- Audio-only visits are not a lesser form of telehealth. For behavioral health, chronic disease check-ins, and medication management, audio-only visits may be clinically equivalent to video while being more accessible. Design billing and quality tracking to support audio-only as a permanent modality