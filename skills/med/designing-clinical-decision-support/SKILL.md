---
name: designing-clinical-decision-support
description: Creates CDS rule specifications with trigger conditions, evidence base, and alert fatigue mitigation. Use when designing CDS alerts, specifying clinical rules, or optimizing alert systems.
tags:
  - design
  - health-informatics
  - clinical
metadata:
  author: casemark
  practice_areas:
    - Health Informatics
    - Health IT
    - Clinical Informatics
  document_types:
    - Design Document
  skill_modes:
    - Design
---

# Designing Clinical Decision Support

Creates CDS rule specifications with trigger conditions, evidence base, and alert fatigue mitigation strategies. This skill covers the design lifecycle from clinical need identification through post-deployment monitoring for rules implemented in certified EHR systems.

## Why This Skill Exists

Poorly designed CDS is worse than no CDS at all. Alert fatigue from excessive, low-value interruptions causes clinicians to override 49-96% of drug interaction alerts, including clinically significant ones. Meanwhile, the absence of evidence-based CDS at critical decision points contributes to preventable adverse events. This skill structures CDS design to maximize clinical value while minimizing cognitive burden, following the CDS Five Rights framework: right information, right person, right format, right channel, right time in workflow.

---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **Clinical problem statement** --- What patient safety risk, quality gap, or regulatory requirement does this CDS address?
2. **Evidence base** --- What clinical guidelines, systematic reviews, or regulatory mandates support this rule? (Cite specific sources: USPSTF grade, ACC/AHA class, FDA safety communication)
3. **Target users** --- Which clinician roles should receive this alert? (Attending physician, resident, nurse, pharmacist, all prescribers)
4. **EHR platform and CDS engine** --- Which system will execute the rule? (Epic BPA, Cerner MPages, vendor-neutral CDS Hooks implementation)
5. **Workflow insertion point** --- At what point in the clinical workflow should the CDS fire? (Order entry, note signing, medication reconciliation, scheduling)
6. **Current override rate** --- If replacing or modifying an existing alert, what is the current override rate and documented reasons?
7. **CDS governance committee approval** --- Has the clinical informatics committee approved the concept?

### Required Documents

- Clinical guideline or evidence source document
- Current alert inventory for the target clinical domain (to assess overlap and fatigue burden)
- EHR CDS capability matrix (available trigger types, data elements accessible at runtime)
- Override reason code taxonomy currently in use
- Baseline quality measure data if the CDS targets an eCQM or HEDIS measure

---

## Step 1 --- Define Trigger Logic

Specify the computable conditions that activate the CDS rule:

- **Patient inclusion criteria** --- Demographics (age, sex), problem list entries (SNOMED CT concepts), active medication list (RxNorm CUIs), lab results (LOINC codes with value thresholds), encounter type
- **Action trigger** --- What user action initiates evaluation? (New order for drug class X, opening a patient chart, completing a flowsheet row)
- **Temporal conditions** --- Time-based logic (e.g., "no HbA1c result in past 90 days" requires date arithmetic against LOINC 4548-4)
- **Exclusion criteria** --- Conditions that suppress the alert: documented allergy contraindication, active hospice status, patient refusal on file
- **Boolean logic structure** --- Write the full trigger as a structured boolean expression:
  ```
  IF (active_medication IN [RxNorm class]) 
  AND (lab_result[LOINC] < threshold OR lab_result_age > 90d) 
  AND NOT (problem_list CONTAINS [SNOMED exclusion concept])
  THEN fire_alert
  ```

---

## Step 2 --- Design the Intervention

Structure the CDS output following the CDS Five Rights:

- **Alert type classification** --- Interruptive (hard stop, soft stop) vs. non-interruptive (info button, dashboard indicator, inbox message). Default to non-interruptive unless evidence supports interruption
- **Content specification** --- Write the exact alert text. Include: (a) what was detected, (b) why it matters with severity, (c) recommended action, (d) link to evidence. Keep below 3 sentences for interruptive alerts
- **Action options** --- Define the response buttons: Accept recommendation (with pre-populated order), Override with reason (from coded reason list), Defer/snooze (with time limit), Cancel triggering action
- **CDS Hooks integration** --- For SMART on FHIR CDS Hooks implementations, specify the hook type (patient-view, order-select, order-sign, medication-prescribe), the prefetch query, and the card response structure
- **Suggested actions** --- For order-based CDS, pre-populate the recommended order with appropriate defaults (dose, route, frequency) to minimize clinician effort

---

## Step 3 --- Assess and Mitigate Alert Fatigue

Before deployment, evaluate the fatigue impact:

1. **Estimated firing frequency** --- Query historical data to estimate how often the trigger criteria are met. Express as alerts per provider per shift
2. **Positive predictive value projection** --- Of estimated firings, what percentage represent truly actionable clinical situations?
3. **Tiering strategy** --- Classify severity: Tier 1 (hard stop, life-threatening), Tier 2 (soft stop, clinically significant), Tier 3 (informational, non-interruptive). Only Tier 1 and 2 justify interruption
4. **Duplicate/overlap check** --- Compare trigger logic against all existing active CDS rules. Identify rules that would fire on the same patient population and order type
5. **Suppression rules** --- Define auto-suppression for repeat firings (e.g., "do not re-fire this alert for the same patient within 24 hours if overridden")
6. **Override reason analysis plan** --- Design structured override reasons that produce analyzable data for post-deployment refinement

---

## Step 4 --- Specify Knowledge Maintenance

CDS rules are clinical content that requires lifecycle management:

- **Evidence review schedule** --- Define review frequency based on evidence velocity: annual for stable guidelines, quarterly for rapidly evolving domains (e.g., oncology protocols)
- **Trigger for urgent update** --- FDA safety communication, guideline withdrawal, formulary change, new contraindication
- **Version control** --- Each rule version gets a unique identifier with effective date, author, approving committee, and clinical evidence citation
- **Retirement criteria** --- Override rate > 90% for 3 consecutive months triggers mandatory review. Measure-based CDS retires when the quality measure is retired or topped out

---

## Step 5 --- Build and Test

Execute the CDS rule implementation:

- **Unit testing** --- Create test patients covering: positive trigger (alert fires correctly), negative trigger (alert correctly suppressed), boundary conditions (values at exact thresholds), exclusion criteria (alert suppressed for excluded populations)
- **Integration testing** --- Test within the full clinical workflow: place the triggering order, verify the alert appears at the correct workflow point, confirm the recommended action executes correctly
- **Performance testing** --- Measure alert rendering latency. CDS that takes > 2 seconds to display at order entry will be perceived as system slowness, not decision support
- **User acceptance testing** --- Have 3-5 representative clinicians walk through the alert in simulated encounters. Document feedback on clarity, actionability, and workflow disruption

---

## Step 6 --- Deploy and Monitor

Post-deployment surveillance is mandatory:

- **Phased rollout** --- Deploy to a pilot unit or provider group first. Monitor for 2 weeks before enterprise deployment
- **Monitoring metrics** --- Track daily: firing rate, override rate by reason code, acceptance rate, time-to-action after alert display, adverse events in the target population
- **Feedback channel** --- Establish a mechanism for clinicians to report CDS issues directly to the clinical informatics team (not just the IT help desk)
- **30-day review** --- Formal post-deployment review with the CDS governance committee. Present metrics, clinician feedback, and recommendations for tuning

---

## Checkpoint B --- Design Completeness Review

Before submitting for governance committee approval:

- [ ] Trigger logic is fully specified with coded data elements (SNOMED, LOINC, RxNorm)
- [ ] Evidence base is cited with guideline strength and quality rating
- [ ] Alert type (interruptive vs. non-interruptive) is justified with fatigue analysis
- [ ] Alert text is reviewed for clinical accuracy and health literacy
- [ ] Override reason codes are defined and mapped to the organization's taxonomy
- [ ] Suppression and de-duplication rules are specified
- [ ] Test cases cover positive, negative, boundary, and exclusion scenarios
- [ ] Knowledge maintenance schedule is defined with responsible owner
- [ ] Estimated firing frequency and PPV are documented

---

## Quality Audit

- [ ] CDS rule addresses a documented clinical need with evidence support (not vendor suggestion alone)
- [ ] Interruptive alerts are limited to Tier 1 and Tier 2 severity
- [ ] Estimated alert frequency does not exceed organizational threshold per provider per shift
- [ ] All coded elements use current terminology versions (SNOMED CT, ICD-10-CM, LOINC, RxNorm)
- [ ] CDS Hooks specification follows HL7 standards if applicable
- [ ] Override data capture is structured for post-deployment analysis
- [ ] Clinical informaticist and subject matter expert sign-off documented
- [ ] Post-deployment monitoring plan has defined metrics and review milestones
- [ ] Rule version is catalogued in the organizational CDS knowledge base

---

## Guidelines

- Default to non-interruptive CDS formats unless clinical evidence demonstrates that interruption prevents significant harm. The burden of proof is on the case for interruption, not against it
- Never deploy CDS rules without a defined retirement or review process. Orphaned rules are the primary driver of alert fatigue accumulation
- Use coded clinical data (SNOMED CT, LOINC, RxNorm) for all trigger criteria. Free-text triggers are fragile and unauditable
- Include the evidence citation in the alert display. Clinicians are more likely to accept recommendations they can verify
- Design CDS as a system, not individual rules. Every new rule must be evaluated against the existing rule inventory for interaction effects
- Track the override rate as a signal, not a problem. High override rates indicate poor rule design, not poor clinician behavior
- For CDS Hooks implementations, minimize prefetch data to what the rule actually needs. Over-fetching degrades FHIR server performance
- Maintain alignment with ONC certification criterion 170.315(a)(9) for CDS configuration requirements
