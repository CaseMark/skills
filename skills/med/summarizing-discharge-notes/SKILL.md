---
name: summarizing-discharge-notes
language: en
description: Transforms hospital discharge paperwork into structured patient summaries with medications, follow-up appointments, activity restrictions, and warning signs. Use when processing discharge documents, creating patient handoffs, or preparing transition-of-care summaries.
tags:
  - summarization
  - hospital-medicine
  - patient-care
metadata:
  author: casemark
  practice_areas:
    - Hospital Medicine
    - Internal Medicine
  document_types:
    - Summary Report
  skill_modes:
    - Summarization
---

# Summarizing Discharge Notes

## Why This Skill Exists

Discharge is the single highest-risk handoff in acute care. Nearly 20% of Medicare patients are readmitted within 30 days, and CMS penalizes hospitals with excess readmission rates under the Hospital Readmissions Reduction Program (HRRP). The Joint Commission's National Patient Safety Goals require structured, reconciled discharge communication. When discharge summaries are incomplete — missing a medication change, omitting a pending lab, burying a critical follow-up in narrative prose — the downstream provider flies blind and the patient pays the price. A structured, reconciled discharge summary is the single most effective artifact for preventing avoidable readmissions, closing care gaps, and satisfying regulatory requirements.

This skill transforms raw discharge paperwork (physician discharge summaries, nursing discharge instructions, medication administration records, after-visit summaries) into a structured, actionable summary that serves two audiences: the receiving provider (PCP, SNF, home health) and the patient or caregiver. For the output template, read `references/DISCHARGE-OUTPUT-TEMPLATE.md`.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Source documents available** — physician discharge summary, nursing instructions, medication administration record (MAR), after-visit summary (AVS), lab/imaging results, consultant notes. Which of these does the user have?
2. **Target audience** — receiving PCP, skilled nursing facility (SNF), home health agency, patient/caregiver, or multiple
3. **Patient complexity tier** — straightforward (single diagnosis, few meds), moderate (2-3 active problems, polypharmacy), complex (ICU stay, multiple comorbidities, device/drain management, pending workup)
4. **Specific concerns** — any known care transition risks the user wants emphasized (e.g., new anticoagulation, insulin regimen change, wound vac, pending biopsy)
5. **Output format preference** — full structured summary, condensed handoff card, or both

**If the user doesn't respond**, apply and clearly label these defaults: target audience is receiving provider; complexity is moderate; full structured summary format; no specific concerns flagged.

### Documents to Request

Request these materials — they substantially improve quality:

- Physician discharge summary / H&P with hospital course
- Discharge medication list (ideally the reconciled list, not just the last MAR)
- Admission medication list or home medication list (for reconciliation)
- Lab and imaging results from the last 48 hours of admission
- Active consultant notes (especially ID, cardiology, surgery if relevant)
- Nursing discharge instructions / patient education sheets
- Pending orders, referrals, or scheduled follow-ups

If materials are missing, flag them explicitly in the "Open Items" section. Proceed with labeled assumptions rather than stalling, but never silently infer a medication dose or result — mark with `[VERIFY FROM SOURCE]`.

---

## Step 1: Extract the Clinical Narrative Spine

Read all source documents and extract the core clinical story. This is not a copy-paste exercise — it requires reconciliation across documents that often contradict each other (the discharge summary may list a medication the MAR shows was discontinued 2 days prior).

Build the narrative spine:

- **Admission trigger** — what brought the patient in (chief complaint, ED presentation, transfer reason)
- **Hospital course** — what happened, in clinical sequence. Focus on decision points: why was a medication started, why was a procedure done, why was a consult called
- **Discharge status** — clinical condition at discharge compared to admission. Improving, stable, or with residual issues requiring outpatient management

Flag any inconsistencies between source documents immediately. Example: "Discharge summary lists lisinopril 10mg; MAR shows lisinopril was held on hospital day 3 and not restarted `[RECONCILE]`."

---

## Step 2: Medication Reconciliation (Critical — Most Common Error Source)

Medication errors at discharge cause more preventable readmissions than any other single factor. This step is non-negotiable.

### Required Deliverable: Discharge Medication Table

| Medication | Dose | Route | Frequency | Status | Change Reason | Special Instructions |
|---|---|---|---|---|---|---|
| | | | | NEW / CHANGED / CONTINUED / DISCONTINUED | | |

**Status definitions:**
- **NEW** — started during this admission, not on the home med list
- **CHANGED** — was on home meds but dose, route, or frequency changed
- **CONTINUED** — same as home, no changes
- **DISCONTINUED** — was on home meds, now stopped

### Reconciliation Rules

1. Compare admission med list to discharge med list line by line. Every difference must be tagged with a status and a change reason.
2. PRN medications must be listed separately from standing orders with clear indications (e.g., "ondansetron 4mg PO PRN nausea, max 3 doses/day").
3. High-alert medications require explicit callouts: anticoagulants, insulin, opioids, immunosuppressants, narrow therapeutic index drugs (digoxin, phenytoin, lithium, theophylline).
4. If the source documents don't specify whether a home medication should continue, mark it `[VERIFY — not addressed in discharge documents]`. Never assume continuation.
5. Include any bridging therapy context (e.g., "enoxaparin bridge until INR therapeutic on warfarin").

---

## Step 3: Pending Results and Incomplete Workup

Pending labs, pathology, cultures, and imaging reads are among the most commonly dropped items during care transitions. Extract every pending item.

### Required Deliverable: Pending Items Table

| Item | Ordered Date | Expected Result Date | Responsible Provider for Follow-Up | Action if Abnormal |
|---|---|---|---|---|
| | | | | |

Common items to actively look for:

- Blood cultures (especially if antibiotics were started empirically)
- Pathology / biopsy results
- Outpatient imaging ordered but not yet completed
- Pending subspecialty referrals
- Repeat labs ordered for outpatient draw (e.g., recheck creatinine in 1 week)

If no pending items are identified, state explicitly: "No pending results identified in available source documents." Do not leave this section blank — the absence of pending items is itself clinically meaningful and must be affirmatively stated.

---

## Step 4: Diagnoses, Procedures, and Hospital Course Summary

### Required Deliverable: Diagnosis Table

| # | Diagnosis | ICD-10 (if available) | Status at Discharge | Follow-Up Plan |
|---|---|---|---|---|
| 1 | Primary diagnosis | | | |
| 2+ | Secondary / comorbid diagnoses | | Active / Stable / Resolved | |

### Required Deliverable: Procedures Table

| Procedure | Date | Performing Provider | Findings / Outcome | Follow-Up Needed |
|---|---|---|---|---|

### Hospital Course

Write a concise narrative (target 3-8 sentences for moderate complexity, up to 15 for complex) that answers: Why admitted? What happened? What's the plan going forward? Avoid restating the entire chart — synthesize the clinical reasoning.

---

## Step 5: Follow-Up, Restrictions, and Condition-Specific Instructions

### Required Deliverable: Follow-Up Appointments Table

| Provider / Specialty | Timeframe | Purpose | Scheduled (Y/N) | Contact Info |
|---|---|---|---|---|

### Activity and Diet Restrictions

- Specify duration and conditions for each restriction (e.g., "No lifting >10 lbs for 6 weeks post-surgery" not just "activity restriction")
- Diet changes with rationale (e.g., "2g sodium restriction — new CHF diagnosis")
- Driving restrictions if applicable (post-sedation, seizure, new narcotic)
- Work/school return guidance if relevant

### Wound / Device / Drain Care

If applicable, include: site description, dressing change instructions with frequency, signs of infection to monitor, supplies needed, and who to call for issues. If no wounds/devices, omit this section entirely rather than writing "N/A."

### Return Precautions (Warning Signs)

List condition-specific warning signs that should prompt the patient to seek immediate care. These must be:

- Specific to the discharge diagnoses (not generic boilerplate)
- Actionable (tell the patient what to DO — "call your doctor" vs. "go to the ER" vs. "call 911")
- Written at a patient-accessible level if the audience includes patients/caregivers

Example for new CHF diagnosis: "Seek emergency care if you experience sudden shortness of breath at rest, cannot lie flat to sleep, gain more than 3 pounds in one day or 5 pounds in one week, or develop new chest pain."

---

## Step 6: Produce the Deliverables

Output a structured summary using the template in `references/DISCHARGE-OUTPUT-TEMPLATE.md`. Two output lanes:

### Lane 1: Full Structured Discharge Summary

For the receiving provider. Contains all sections above with clinical detail, medication reconciliation, and pending items. This is the primary deliverable.

### Lane 2: Patient / Caregiver Summary (when audience includes patients)

Simplified version: plain-language diagnoses, medication list with purpose of each drug, appointment dates, activity restrictions in plain terms, and warning signs. No abbreviations. Reading level target: 6th grade.

### Mandatory Front Matter

At the top of every output, before any clinical content, include:

1. **Patient Identifiers** — name, DOB, MRN (if provided), admission date, discharge date, discharge disposition (home, SNF, rehab, home with services)
2. **Assumptions Used** — which source documents were available, target audience, complexity tier
3. **Open Items / Needed Inputs** — missing source documents, unreconciled medications, items marked `[VERIFY]`
4. **Allergies** — drug allergies with reaction type (always surface this prominently; if not documented, mark `[ALLERGY STATUS NOT DOCUMENTED — VERIFY]`)

This front matter is a critical safety guardrail: it tells the receiving provider exactly what was available, what was assumed, and what must be verified before acting.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial summary, ask:

1. Does the medication reconciliation match your understanding of the discharge plan?
2. Are there any pending results or follow-ups I missed?
3. Should I generate the patient/caregiver version (Lane 2)?
4. Are there condition-specific instructions or restrictions that need more detail?
5. Any `[VERIFY]` items you can now confirm or correct?

If the user doesn't answer, recommend the highest-value refinement based on complexity tier (for complex patients, recommend generating the patient summary and expanding wound care instructions) and proceed if authorized.

---

## Quality Audit

Before finalizing, self-check against these criteria:

- Every medication has a status (NEW / CHANGED / CONTINUED / DISCONTINUED) with change reason
- High-alert medications are explicitly called out
- PRN medications are separated from standing orders with indications
- Pending results section is present (even if "none identified")
- Allergies are surfaced in front matter (even if "not documented")
- Every `[VERIFY]` tag has enough context for the reviewer to resolve it
- Follow-up appointments include timeframe AND purpose
- Return precautions are diagnosis-specific, not generic
- Activity restrictions include duration and conditions
- No medication dose, lab value, or clinical finding is inferred without a source — if it's not in the documents, it's not in the summary
- Inconsistencies between source documents are flagged, not silently resolved
- Front matter lists all assumptions and open items
- Output is actionable: a provider unfamiliar with this patient could safely assume care using only this summary

---

## Reference Files

Read these when you need the detailed output template:

- `references/DISCHARGE-OUTPUT-TEMPLATE.md` — Full output template with markdown tables for each section of the structured discharge summary

---

## Guidelines

- Medication reconciliation completeness is the single highest-priority quality metric. Every home medication must have an explicit discharge disposition (NEW, CHANGED, CONTINUED, DISCONTINUED) — a medication without a status is an unresolved safety gap.
- Pending results (cultures, pathology, outpatient imaging) must always appear in a dedicated section even when none are identified. The explicit statement "no pending results" is itself a clinical assertion that must be documented rather than implied by omission.
- Return precautions must be specific to the discharge diagnoses and must not rely on generic boilerplate. Each warning sign should include the condition it suggests, the urgency level, and the specific action to take (call PCP vs. go to ED vs. call 911).
- Never infer a medication dose, lab value, or clinical finding that is not explicitly present in the source documents. If information is missing, mark it with `[VERIFY FROM SOURCE]` and surface it in the Open Items section.
- Discharge summaries for patients with new anticoagulation, insulin regimen changes, or narrow therapeutic index drug adjustments must include explicit monitoring parameters (e.g., "recheck INR in 3 days," "fasting glucose log daily for 1 week") with responsible provider assignment.
- When source documents conflict (e.g., discharge summary lists a medication the MAR shows was discontinued), flag the inconsistency explicitly rather than choosing one source. The receiving provider needs to see the conflict to resolve it safely.
- Patient-facing summaries (Lane 2) must be written at or below a 6th-grade reading level, avoid all medical abbreviations, and include a plain-language explanation of why each medication was started, changed, or stopped.
- Activity restrictions, dietary changes, and driving limitations must include specific durations and conditions for resumption — never use open-ended language like "as tolerated" without defining what "tolerated" means in measurable terms.
