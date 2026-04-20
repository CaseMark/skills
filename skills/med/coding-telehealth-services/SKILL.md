---
name: coding-telehealth-services
language: en
description: Assigns telehealth-specific codes with place of service, modifier, and technology requirements. Use when coding virtual visits, applying telehealth modifiers, or documenting telemedicine services.
tags:
  - coding
  - medical-coding-and-billing
metadata:
  author: casemark
  practice_areas:
    - Medical Coding
    - Revenue Cycle
    - Health Information Management
  document_types:
    - Coded Record
  skill_modes:
    - Coding
    - Classification
---

# Coding Telehealth Services

Assigns telehealth-specific codes with correct place of service (POS), modifier application (95, GT, FQ, FR, G0), technology requirements, and originating/distant site billing. Covers synchronous audio-video visits, audio-only services, remote patient monitoring, asynchronous (store-and-forward) services, and interprofessional consultations.

## Why This Skill Exists

Telehealth coding rules change frequently — CMS releases updates through annual fee schedule rules, transmittals, and interim final rules. The post-pandemic permanent telehealth expansions differ significantly from temporary flexibilities. Key complexities include: POS code selection (02 vs. 10 vs. original POS), modifier requirements varying by payer, geographic and originating site restrictions for Medicare, audio-only eligibility limits, and the distinction between telehealth services and remote evaluation/monitoring services. Incorrect POS or missing modifiers result in claim denials; incorrect service-type classification creates compliance risk.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What type of telehealth service was provided? (synchronous audio-video, audio-only, store-and-forward, remote monitoring)
2. What technology platform was used? Is it HIPAA-compliant with real-time audio-video capability?
3. Where was the patient located during the encounter? (home, clinic, hospital, nursing facility)
4. Where was the provider located? (office, home, hospital)
5. Is the service on the CMS Telehealth Eligible Services List (for Medicare)?
6. What payer covers this service? (Medicare FFS, Medicare Advantage, Medicaid, commercial)
7. What is the patient's state of residence? (state telehealth parity laws vary significantly)

### Documents Required

- Encounter note documenting the telehealth service (same documentation standards as in-person)
- Technology/platform documentation (audio-video vs. audio-only)
- Patient consent for telehealth (required by most states and Medicare)
- Patient location documentation (state and setting)
- Provider location and licensure in the patient's state
- CMS Telehealth Eligible Services List (current calendar year)
- Payer-specific telehealth policies

---

## Step 1 — Determine the Service Category

Classify the telehealth service type — each has different coding rules.

**Synchronous audio-video telehealth:**
- Real-time interactive audio and video communication between patient and provider.
- Uses the same CPT/HCPCS codes as in-person services (E/M, psychotherapy, consultations, etc.).
- Must be on the CMS Telehealth Eligible Services List for Medicare reimbursement.
- Requires interactive audio AND video — audio-only does not qualify (with limited exceptions).

**Audio-only services:**
- **99441**: 5–10 minutes of medical discussion (telephone E/M).
- **99442**: 11–20 minutes.
- **99443**: 21–30 minutes.
- Medicare allows audio-only for certain behavioral health services (90832–90838, 90839, 90845) and E/M services in limited circumstances for established patients.
- Audio-only eligibility varies significantly by payer and state.

**Remote evaluation and management:**
- **G2010**: Remote evaluation of recorded video/images submitted by an established patient (store-and-forward). Not a real-time service.
- **G2012**: Virtual check-in — brief communication (5–10 minutes) via synchronous technology initiated by an established patient. Not a separately billable E/M.
- **99421–99423**: Online digital E/M service (patient portal communication over 7-day period). Time-based: 5–10 min, 11–20 min, 21+ min cumulative.

**Remote Patient Monitoring (RPM):**
- **99453**: Initial setup and patient education on RPM devices (one-time).
- **99454**: Device supply with daily recording and programmatic alerts, per 30 days.
- **99457**: RPM treatment management, first 20 minutes per calendar month.
- **+99458**: Each additional 20 minutes per calendar month.
- **99091**: Collection and interpretation of physiologic data, 30+ minutes per 30 days (cannot bill with 99457 in the same month).

## Step 2 — Select the Correct Place of Service

POS determines payment rates and modifier requirements.

**Medicare POS rules (post-PHE permanent policy):**
- **POS 02 — Telehealth provided other than in patient's home**: Patient is at an originating site (clinic, hospital, SNF, etc.). Facility rate applies.
- **POS 10 — Telehealth provided in patient's home**: Patient is at home. Non-facility rate applies.
- When the patient is at home, use POS 10. When at a healthcare facility, use POS 02.
- For audio-only services, use POS 02 or 10 based on patient location.

**Commercial payer POS rules:**
- Some commercial payers require the original POS (11 for office, 22 for hospital outpatient) with modifier 95 to indicate telehealth.
- Others use POS 02/10 following the Medicare model.
- Check payer-specific policy before claim submission.

**Originating site requirements (Medicare):**
- For services still subject to geographic restrictions, the originating site must be in a rural HPSA or non-MSA county.
- Mental health and behavioral health telehealth services were permanently exempted from geographic restrictions (effective 2025).
- An originating site facility fee (Q3014) can be billed by the facility where the patient is located (not the distant site provider).

## Step 3 — Apply Telehealth Modifiers

Select the correct modifier based on service type and payer.

- **Modifier 95**: Synchronous telehealth service via real-time audio and video. CMS-preferred modifier for Medicare claims. Applied to the procedure code on the professional claim.
- **Modifier GT**: Telehealth via interactive audio and video telecommunications system. Used by some commercial payers instead of or in addition to modifier 95.
- **Modifier FQ**: Telehealth service provided using audio-only communication technology. Required by Medicare for eligible audio-only services.
- **Modifier FR**: Supervising practitioner present through real-time audio-video communication technology for services furnished by a resident. Used in teaching physician scenarios.
- **Modifier G0**: Telehealth service for diagnosis, evaluation, or treatment of symptoms of an acute stroke. Applied to acute stroke telehealth consultations.
- **Modifier 93**: Audio-only services (used by some state Medicaid programs instead of FQ).

**Key modifier rules:**
- Do NOT append telehealth modifiers to RPM codes (99453–99458) — RPM is not a telehealth service.
- Do NOT append telehealth modifiers to virtual check-ins (G2010, G2012) or e-visits (99421–99423).
- Medicare requires modifier 95 for all telehealth-eligible CPT codes and modifier FQ for audio-only eligible services.

## Step 4 — Validate Medicare Telehealth Eligibility

Confirm the service is on the CMS Telehealth Eligible Services List.

- CMS publishes an updated list annually (effective January 1) with additions from the Medicare Physician Fee Schedule Final Rule.
- Services on the list include: office/outpatient E/M (99202–99215), subsequent hospital care (99231–99233), psychiatric services (90791–90899), certain consultation codes (not recognized by Medicare FFS but relevant for MA plans), and specific procedure codes.
- Services NOT on the list cannot be billed as Medicare telehealth — they must be provided in-person.
- Some services were added temporarily during the PHE and may not be permanent — verify against the current list.
- Medicare Advantage plans may cover additional telehealth services beyond the FFS list — check the MA plan's supplemental benefits.

## Step 5 — Code Remote Patient Monitoring

Apply RPM coding rules for chronic condition monitoring.

- **Eligibility**: Patient must have a chronic condition requiring monitoring (e.g., hypertension, diabetes, CHF, COPD).
- **Minimum data requirement**: RPM requires at least 16 days of data collection within a 30-day period for 99454 to be billable.
- **99453 (initial setup)**: One-time code for setting up the RPM device and educating the patient. Billed once per episode of care.
- **99454 (device supply/data transmission)**: Billed per 30-day period. Requires daily recording or programmatic alerts.
- **99457 (treatment management)**: Requires at least 20 minutes of clinical staff time per calendar month interacting with the patient about the RPM data. Must include live interaction (phone, video, or in-person).
- **+99458 (additional time)**: Each additional 20-minute increment beyond the first 20 minutes.
- RPM can be furnished by clinical staff under general supervision of the billing provider.
- RPM is NOT telehealth — it does not require real-time audio-video and is not subject to telehealth POS/modifier rules.

---

## Checkpoint B — Review

- [ ] Service category correctly identified (synchronous A/V, audio-only, RPM, virtual check-in, e-visit)
- [ ] CPT/HCPCS code is on the CMS Telehealth Eligible Services List (for Medicare claims)
- [ ] Place of service matches patient location (POS 02 vs. POS 10 vs. original POS per payer)
- [ ] Correct telehealth modifier applied (95, GT, FQ, FR, G0) per payer requirements
- [ ] Audio-only services are limited to eligible codes with proper modifier FQ
- [ ] RPM codes are NOT modified with telehealth modifiers
- [ ] Patient consent for telehealth is documented
- [ ] Provider licensure in the patient's state is verified

---

## Quality Audit

- [ ] Telehealth claims use the correct POS for the payer (not defaulting to POS 11 for all telehealth)
- [ ] Audio-only vs. audio-video service type matches documentation and applied modifiers
- [ ] RPM data collection meets the 16-day minimum per 30-day period for 99454
- [ ] RPM treatment management (99457) includes documented live patient interaction
- [ ] Telehealth consent documentation is present for every telehealth encounter
- [ ] State telehealth parity law requirements are met for commercial payer claims
- [ ] Originating site fees (Q3014) are billed only when the patient is at an eligible originating site

---

## Guidelines

- Follow CMS Telehealth Eligible Services List (updated annually in the Medicare Physician Fee Schedule Final Rule)
- Apply CMS Medicare Claims Processing Manual Chapter 12 §190 for telehealth billing requirements
- Reference CMS MLN Matters articles for telehealth policy updates and clarifications
- Follow state telehealth parity laws for commercial payer coverage requirements
- Apply HIPAA security requirements for telehealth technology platforms
- Never bill a telehealth service as an in-person visit without telehealth modifiers — this misrepresents the service
- Mark with [VERIFY] any telehealth service where eligibility, POS, or modifier selection is uncertain
- Include disclaimer that telehealth coding rules change frequently and payer-specific policies must be verified at the time of billing
