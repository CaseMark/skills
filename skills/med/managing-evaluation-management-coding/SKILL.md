---
name: managing-evaluation-management-coding
description: Applies 2021+ E/M guidelines with medical decision-making or time-based code selection. Use when coding E/M services, determining MDM level, or selecting E/M codes.
tags:
  - management
  - medical-coding-and-billing
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

# Managing Evaluation and Management Coding

Applies the 2021+ CMS/AMA E/M documentation framework to select the correct E/M code level based on medical decision-making (MDM) complexity or total physician/qualified health professional (QHP) time on the date of encounter. Covers office/outpatient (99202–99215), inpatient/observation (99221–99223, 99231–99236), consultations, and subsequent care services.

## Why This Skill Exists

The 2021 E/M restructure eliminated history and exam as code-level determinants for office/outpatient visits, making MDM or time the sole drivers. In 2023, CMS extended similar logic to inpatient and observation services. Misapplication of MDM elements — especially risk table interpretation and data element counting — is the most common source of E/M level errors. CMS CERT data consistently shows E/M services among the highest-error service categories, with improper payments exceeding $2 billion annually for E/M alone.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What E/M category is being coded? (office new/established, inpatient initial/subsequent, observation, consultation, ED)
2. Is the provider selecting code level by MDM or by time?
3. What is the date of service and patient status (new vs. established, initial vs. subsequent)?
4. Is there a separately reportable procedure on the same date requiring modifier 25 consideration?
5. Does the encounter involve shared/split visit rules (physician + NPP)?
6. Are there prolonged services to consider (99417 for office, 99418 for inpatient)?
7. Is the payer Medicare, Medicaid, or commercial (commercial may not recognize all CMS rules)?

### Documents Required

- Complete encounter note (HPI, ROS, exam, assessment/plan)
- Problem list with status of each condition addressed
- Orders placed during the encounter (labs, imaging, referrals, prescriptions)
- Time documentation if time-based coding is used (total time on date of encounter)
- Prior visit notes if referenced for data review
- Test results reviewed during the encounter
- Any care coordination or consultation documentation

---

## Step 1 — Determine E/M Category and Patient Status

Identify the correct code family before assessing level.

- **New patient**: No professional services from the same provider or same-specialty/same-group provider in the prior 3 years.
- **Established patient**: Any professional service within 3 years from same provider or same-specialty/same-group.
- **Office/Outpatient**: 99202–99205 (new), 99211–99215 (established). Note: 99201 was deleted in 2021.
- **Inpatient/Observation**: 99221–99223 (initial), 99231–99233 (subsequent), 99234–99236 (same-day admit/discharge).
- **ED visits**: 99281–99285 — still use the 1995/1997 guidelines (MDM, history, exam) until CMS updates. New/established distinction does not apply.
- **Consultations**: 99241–99245 (office), 99251–99255 (inpatient). Medicare does not recognize consultation codes — use initial visit codes with modifier AI for teaching physicians.

## Step 2 — Assess Medical Decision-Making

MDM has three elements; the level is determined by meeting or exceeding the threshold in 2 of 3.

### Element 1: Number and Complexity of Problems Addressed

| MDM Level | Problem Types |
|-----------|---------------|
| Straightforward | 1 self-limited or minor problem |
| Low | 2+ self-limited problems; 1 stable chronic illness; 1 acute uncomplicated illness |
| Moderate | 1+ chronic illness with mild exacerbation; 2+ stable chronic illnesses; 1 undiagnosed new problem with uncertain prognosis; 1 acute illness with systemic symptoms |
| High | 1+ chronic illness with severe exacerbation; 1 acute/chronic illness posing threat to life or bodily function |

- A "problem addressed" must have assessment, plan, or management documented — listing it in the problem list alone is insufficient.
- Stable chronic conditions count only when the provider documents management actions taken during the visit.

### Element 2: Amount and/or Complexity of Data Reviewed and Analyzed

| MDM Level | Data Requirements |
|-----------|-------------------|
| Straightforward | Minimal or none |
| Low | Review of prior external note/test OR order of test |
| Moderate | Order and review of tests; review of prior external notes with independent interpretation of an image/tracing/specimen; discussion of management with external physician |
| High | As moderate, PLUS independent interpretation of test performed by another physician/QHP |

- "Independent interpretation" means the provider personally reviews the raw data (image, tracing, specimen) and documents their own findings — not simply reading another provider's report.
- Each unique test ordered = 1 data point. A panel (e.g., CMP) = 1 test, not 14 individual analytes.

### Element 3: Risk of Complications, Morbidity, or Mortality

| MDM Level | Risk Examples |
|-----------|---------------|
| Straightforward | OTC medications, minor surgery with no risk factors |
| Low | Prescription drug management, minor surgery with identified risk factors, diagnostic procedures with no identified risk factors |
| Moderate | Prescription drug management requiring monitoring for toxicity; decision for minor surgery with identified risk factors; diagnosis/treatment significantly limited by social determinants of health |
| High | Drug requiring intensive monitoring (e.g., chemotherapy, immunosuppressants); decision for major surgery; decision for emergency major surgery; DNR decision; parenteral controlled substances |

- Risk is assessed based on the decision made at THIS encounter, not outcomes.
- Social determinants of health can raise the risk level to moderate when they significantly limit diagnosis or treatment.

## Step 3 — Apply Time-Based Code Selection (Alternative Path)

If the provider documents total time, time alone determines the code level.

- **Office/Outpatient time ranges (established)**:
  - 99211: Not time-based (typically nurse visit)
  - 99212: 10–19 minutes
  - 99213: 20–29 minutes
  - 99214: 30–39 minutes
  - 99215: 40–54 minutes
  - 99417: Each additional 15 minutes beyond 99215 (55+ minutes)
- **Office/Outpatient time ranges (new)**:
  - 99202: 15–29 minutes
  - 99203: 30–44 minutes
  - 99204: 45–59 minutes
  - 99205: 60–74 minutes
  - 99417: Each additional 15 minutes beyond 99205 (75+ minutes)
- Time includes face-to-face and non-face-to-face activities on the date of encounter: reviewing records, ordering tests, care coordination, documentation, counseling.
- Time documentation must state the total time — "approximately 45 minutes" is acceptable; vague statements like "extended visit" are not.
- For prolonged services (99417), the first unit requires the minimum threshold time for the base code to be exceeded by at least 15 minutes.

## Step 4 — Handle Split/Shared Visits

Apply when a physician and NPP both provide services in the same encounter.

- The billing provider must perform a substantive portion of the visit.
- For time-based coding: combine the time of both providers, but the billing provider must have performed the substantive portion.
- For MDM-based coding: the billing provider must personally perform one of the three MDM elements.
- Document who performed which elements and which provider is billing.
- Medicare requires the physician to bill if using the split/shared visit rules in facility settings.

## Step 5 — Evaluate Modifier 25 Necessity

When a procedure is performed on the same date, assess whether a separately identifiable E/M is supported.

- The E/M must represent a significant, separately identifiable service beyond the typical pre-operative and post-operative work of the procedure.
- The documentation must support the E/M through a distinct problem or distinct MDM elements not related to the procedure decision.
- Do not automatically append modifier 25 to every E/M billed with a procedure — this is a top OIG audit target.

---

## Checkpoint B — Review

- [ ] Correct E/M category and code family selected for the encounter type
- [ ] MDM grid applied correctly — 2 of 3 elements meet or exceed the billed level
- [ ] Each problem counted is actually addressed with documented management
- [ ] Data elements counted are supported by documentation showing review/order
- [ ] Risk level matches the CMS risk table — not over-interpreted
- [ ] If time-based: total time is explicitly documented and falls within the correct range
- [ ] Split/shared visit rules applied correctly if applicable
- [ ] Modifier 25 used only when documentation clearly supports a separately identifiable service

---

## Quality Audit

- [ ] Code level is supportable by either MDM OR time (not mixing elements from both)
- [ ] New vs. established patient status verified against 3-year rule
- [ ] All problems counted as "addressed" have documented assessment/plan entries
- [ ] Independent interpretation of data is documented with the provider's own findings
- [ ] Risk table application does not conflate overall patient risk with encounter-specific risk
- [ ] Prolonged service add-on codes (99417) meet the minimum time threshold
- [ ] Documentation timestamps are internally consistent (not contradicted by schedule or other notes)

---

## Guidelines

- Apply AMA/CMS 2021+ E/M guidelines for office/outpatient visits (99202–99215)
- Apply CMS 2023+ guidelines for hospital inpatient/observation services (99221–99236)
- Reference the AMA MDM grid published in CPT Professional Edition Appendix for MDM element definitions
- Follow CMS MLN Matters articles for Medicare-specific interpretations of E/M rules
- For ED visits (99281–99285), continue applying 1995/1997 Documentation Guidelines until CMS issues revised criteria
- Never upcode based on assumed complexity — the documented MDM elements or documented time must support the level selected
- Mark with [VERIFY] and escalate any encounter where MDM elements are borderline between two levels
- Include disclaimer that E/M code selection is based on documentation as presented and does not constitute legal compliance advice
