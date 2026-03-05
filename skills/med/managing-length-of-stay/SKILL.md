---
name: managing-length-of-stay
description: Tracks admission milestones against expected LOS benchmarks with barrier identification. Use when managing length of stay, identifying discharge barriers, or optimizing bed utilization.
tags:
  - management
  - hospital-medicine
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Length of Stay

Tracks admission milestones against expected LOS benchmarks with barrier identification to optimize throughput and patient outcomes.

## Why This Skill Exists

Length of stay (LOS) is the single most impactful metric in hospital medicine, affecting patient safety, hospital finances, and regulatory compliance simultaneously. Each additional inpatient day increases the risk of hospital-acquired conditions (HAIs, falls, deconditioning, VTE) by 5-10%. CMS uses LOS relative to the geometric mean for each MS-DRG as a core measure for hospital efficiency, and LOS outliers trigger utilization review, denial risk, and Case Mix Index scrutiny.

The national average medical LOS is 4.5 days, but avoidable days (days without clinical justification for inpatient stay) account for 15-25% of total hospital days in most facilities. Common causes include delayed discharge planning, pending authorization, social placement barriers, and failure to anticipate discharge needs on admission. Hospitalists who actively manage LOS milestones reduce avoidable days by 30-40% and generate measurable improvements in bed availability, patient throughput, and hospital margin.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before initiating LOS management for a patient or census, confirm:

1. What is the **MS-DRG** (or anticipated DRG) and its **geometric mean LOS**? *(Default: Look up in CMS IPPS Final Rule tables)*
2. What **hospital day** is the patient currently on? *(Default: Calculate from admission timestamp)*
3. What is the **estimated discharge date** set at admission? *(Default: Admission H&P or initial care plan)*
4. Are there **active discharge barriers** documented? *(Default: Check case management tracking board)*
5. Has **utilization review** flagged this patient for medical necessity review? *(Default: Check UR queue)*
6. What is the patient's **insurance type** — Medicare, Medicaid, commercial, uninsured? *(Default: Registration/insurance verification)*
7. Is this a **readmission** within 30 days of prior discharge? *(Default: Check ADT history)*

### Documents to Request

- CMS MS-DRG geometric mean LOS reference for the assigned DRG
- Admission care plan with initial estimated discharge date
- Case management barrier tracking log
- Utilization review determinations and pending reviews
- Consultant completion status (consults requested vs. completed)
- PT/OT functional assessment and discharge recommendations
- Social work psychosocial assessment
- Insurance authorization status for post-acute placement

---

## Step 1: Establish LOS Benchmarks on Admission

On day of admission, document the following LOS framework:

| Element | Value | Source |
|---------|-------|--------|
| Admitting diagnosis | [Diagnosis] | H&P |
| Expected MS-DRG | [DRG number] | Coding/CDI |
| Geometric mean LOS | [X.X days] | CMS IPPS tables |
| Target discharge date | [Date] | Clinical judgment + GMLOS |
| Discharge disposition | Home / SNF / Rehab / LTACH / Hospice | Case management assessment |

**Common GMLOS benchmarks (medical DRGs):**
- CHF exacerbation (DRG 291-293): 3.8 - 5.6 days
- COPD exacerbation (DRG 190-192): 3.2 - 4.8 days
- Community-acquired pneumonia (DRG 177-179): 3.5 - 5.8 days
- Cellulitis (DRG 602-603): 3.5 - 5.0 days
- UTI (DRG 689-690): 3.2 - 4.5 days
- GI bleed (DRG 377-379): 3.0 - 5.2 days
- Sepsis (DRG 870-872): 4.5 - 7.8 days

---

## Step 2: Daily Milestone Tracking

At each daily round, assess progress against discharge milestones:

**Hospital Day 1 (Admission Day)**
- [ ] Diagnosis confirmed, initial workup ordered
- [ ] Estimated discharge date set and communicated to patient/family
- [ ] Case management and social work notified if post-acute needs anticipated
- [ ] VTE prophylaxis initiated
- [ ] Discharge criteria defined (what must be true for this patient to go home?)

**Hospital Day 2**
- [ ] Initial workup results reviewed and treatment adjusted
- [ ] Consultant recommendations received and incorporated
- [ ] IV-to-PO medication conversion assessed
- [ ] PT/OT evaluation completed (if indicated)
- [ ] Discharge barriers identified and assigned

**Hospital Day 3 (GMLOS Alert for Short-stay DRGs)**
- [ ] If LOS approaching GMLOS: confirm remaining barriers and resolution timeline
- [ ] If discharge today: confirm discharge orders, prescriptions, follow-up, patient education
- [ ] If LOS will exceed GMLOS: document clinical justification for continued stay
- [ ] Utilization review notified if medical necessity may be questioned

**Hospital Day 4+ (LOS Outlier Territory for Most Medical DRGs)**
- [ ] Daily barrier analysis documented
- [ ] Attending-level escalation for unresolved barriers
- [ ] Case management escalation for placement delays
- [ ] Consider observation-status conversion if clinical criteria are marginal

---

## Step 3: Identify and Categorize Discharge Barriers

Use the following barrier taxonomy to systematically address delays:

| Category | Barrier | Mitigation Strategy |
|----------|---------|-------------------|
| **Clinical** | Awaiting procedure | Schedule within 24h or consider outpatient |
| **Clinical** | IV-only medications | Assess PO conversion or OPAT eligibility |
| **Clinical** | Pending cultures/path | Discharge with follow-up plan if not clinically urgent |
| **Insurance** | SNF authorization pending | Start process on admission, not at discharge |
| **Placement** | No SNF bed available | Expand search radius; escalate to CM leadership |
| **Social** | No safe discharge environment | Engage social work; assess respite or shelter options |
| **Patient** | Refusing discharge | Document capacity, involve patient advocate, address concerns |
| **System** | Awaiting consultant sign-off | Direct physician-to-physician communication |
| **Equipment** | DME not arranged | Order on admission if need is anticipated |

---

## Step 4: Utilization Review Collaboration

Work proactively with utilization review to prevent denials:

- **InterQual / Milliman criteria**: Understand the clinical criteria your UR team uses to justify inpatient status
- **Documentation requirements**: Ensure progress notes explicitly state severity of illness (SI) and intensity of service (IS) that meet inpatient criteria
- **Status changes**: If a patient no longer meets inpatient criteria, consider observation conversion before UR issues a denial
- **Appeal preparation**: If a denial is issued, provide clinical narrative addressing specific denial rationale within 24 hours

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

For each patient or census report:

1. Is the **estimated discharge date** current and documented in today's note?
2. Are all **discharge barriers** categorized with assigned owners and deadlines?
3. Has **utilization review status** been checked for patients approaching or exceeding GMLOS?
4. Has the patient/family been informed of the **discharge plan and timeline**?
5. Are there any patients who could be discharged **today** if remaining barriers were resolved?

---

## Quality Audit

- [ ] Estimated discharge date set within 24 hours of admission
- [ ] Discharge criteria (clinical milestones) explicitly defined
- [ ] Daily LOS tracking documented against GMLOS benchmark
- [ ] Discharge barriers identified, categorized, and assigned
- [ ] Case management engaged within 24 hours for patients needing post-acute care
- [ ] IV-to-PO conversion assessed by hospital day 2
- [ ] PT/OT evaluation completed within 48 hours if mobility is a discharge criterion
- [ ] Insurance authorization initiated proactively (not day of discharge)
- [ ] LOS outliers have documented clinical justification
- [ ] Utilization review notifications are addressed within 24 hours
- [ ] Patient/family informed of discharge plan at each daily round
- [ ] Discharge before noon rate tracked and optimized
- [ ] Avoidable day analysis completed for all LOS outliers

---

## Guidelines

- Set the estimated discharge date on admission day — studies show this single action reduces LOS by 0.5 days
- Start discharge planning on admission, not when the patient is "ready" — anticipate post-acute needs from day one
- Challenge every hospital day: "What is the one thing keeping this patient from going home today?"
- IV-to-PO conversion is the most commonly missed early-discharge opportunity — assess at every round
- Pending consultant recommendations should never be a reason for delayed discharge without direct physician communication
- Never discharge a patient without confirmed follow-up (appointment date, provider name, phone number)
- Track avoidable days as a quality metric — present at departmental M&M or quality meetings
- Communicate discharge timeline to nursing by 10 AM daily to enable afternoon discharges
