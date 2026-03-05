---
name: managing-charge-capture
description: Reviews charge capture completeness with missed charge identification and revenue recovery. Use when auditing charge capture, identifying missing charges, or improving revenue integrity.
tags:
  - management
  - medical-coding-and-billing
  - audit
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

# Managing Charge Capture

Reviews charge capture completeness across clinical departments, identifies missed charges through reconciliation of documented services against billed charges, and implements systematic charge capture improvement processes. Covers professional and facility charge capture, chargemaster maintenance, charge lag monitoring, and revenue integrity programs.

## Why This Skill Exists

Missed charges represent 1–5% of net revenue in most healthcare organizations — translating to millions of dollars annually for mid-size and large facilities. The most common missed charges are supplies, implants, observation hours, infusion/injection services, and procedures performed but not billed. Charge capture errors arise from provider workflow gaps, EMR configuration issues, chargemaster inaccuracies, and lack of reconciliation between clinical documentation and billing systems. A structured charge capture program recovers lost revenue while preventing overbilling that creates compliance risk.

---

## Checkpoint A — Intake

### Questions to Confirm Before Starting

1. What service lines or departments are in scope for charge capture review?
2. Is this a prospective (real-time) or retrospective charge capture audit?
3. What is the time period under review?
4. What charge capture mechanisms exist? (EMR-integrated, paper charge tickets, charge capture apps)
5. What is the current charge lag (days from service to charge entry)?
6. Are there known missed charge categories from prior audits or benchmarking?
7. What EMR and billing system are in use?

### Documents Required

- Clinical documentation for the review period (encounter notes, procedure notes, nursing records)
- Charge detail files from the billing system for the same period
- Chargemaster with CDM codes, CPT/HCPCS mappings, and pricing
- Department-specific charge capture workflows and policies
- Supply and implant logs (for facility charge capture)
- Infusion and injection administration records
- Observation status orders and hour logs
- Prior charge capture audit findings and corrective actions

---

## Step 1 — Reconcile Documentation Against Charges

Compare what was documented against what was billed, service by service.

**Professional fee reconciliation:**
- Pull all encounter notes for the review period and compare against submitted claims.
- Verify every documented E/M service has a corresponding professional charge.
- Verify every documented procedure has a corresponding CPT code on the claim.
- Check for undercoded services — procedures documented but billed at a lower level or not billed at all.
- Flag encounters with documentation but no charge (complete charge miss) and encounters with charges but no documentation (phantom charges — compliance risk).

**Facility fee reconciliation:**
- Compare clinical orders, administration records, and procedure logs against facility charges.
- Verify all administered medications have corresponding J-codes or HCPCS charges.
- Verify all diagnostic tests ordered and resulted have corresponding technical charges.
- Check supply and implant logs against billed supply charges.
- Verify observation hours are charged correctly (per-hour billing with minimum documentation).

## Step 2 — Identify High-Risk Missed Charge Categories

Focus on service categories with the highest missed charge rates.

**Infusion and injection services (96360–96549):**
- IV infusion coding requires start/stop times for each drug/substance.
- Initial infusion (96365) vs. sequential infusion (96366) vs. concurrent infusion (96368) — each has different rules.
- Hydration infusions (96360–96361) are separately billable only when they are not merely the vehicle for drug delivery.
- Push injections (96372–96376) are time-dependent: if administration takes ≤15 minutes, use push code; if >15 minutes, use infusion code.
- Missed charges are common when nursing documentation captures times but the charge entry process does not translate them to the correct infusion hierarchy.

**Observation services:**
- Observation hours must be actively charged — many facilities miss observation time charges or charge incorrect hours.
- Verify observation start time (when the physician orders observation status) matches the charge start.
- Charge per-hour to the nearest hour for most payers.
- Observation charges stop when the patient is discharged, admitted to inpatient, or transferred.

**Surgical supplies and implants:**
- High-cost implants (orthopedic hardware, cardiac devices, tissue grafts) should generate separate charges with appropriate HCPCS codes.
- Compare the operative report's implant documentation against the implant log and the billed charges.
- Verify pass-through status for Medicare — certain devices qualify for separate APC payment under OPPS.

**Emergency department procedures:**
- ED procedures are frequently missed because providers focus on clinical care and may not enter charges for every procedure.
- Common missed ED charges: laceration repair, splinting/casting, incision and drainage, foreign body removal, conscious sedation.
- Reconcile ED nursing procedure documentation against billed charges.

## Step 3 — Audit Chargemaster Accuracy

Verify the CDM maps correctly to CPT/HCPCS codes and pricing.

- Every charge description number (CDN) should map to a valid CPT or HCPCS code.
- Verify CPT/HCPCS code mappings are current — codes change annually. Deleted codes create claim rejections.
- Check pricing against the fee schedule — charges should be set above the highest payer reimbursement to avoid leaving money on the table.
- Verify revenue codes are appropriate for each charge (revenue code + CPT code must be a valid combination for UB-04 billing).
- Identify duplicate CDM entries that could lead to double-billing.
- Check for "exploding" charges (one CDN triggers multiple charges) to ensure all component charges are accurate.
- Chargemaster review should occur at least annually and whenever CMS releases code updates.

## Step 4 — Measure and Reduce Charge Lag

Track the time between service delivery and charge posting.

- **Target**: Professional charges entered within 2–3 business days of service; facility charges entered within 1–2 business days.
- Calculate average charge lag by department, provider, and service type.
- Identify bottlenecks: Is the lag in clinical documentation, charge entry, coding, or charge review/approval?
- Implement real-time charge capture tools (mobile apps, EMR integrated charge entry) to reduce lag.
- Charge lag beyond 5 business days increases the risk of missed charges — memory fades and records become harder to reconcile.
- Track charges entered after initial bill drop — these represent late charges that may require rebilling.
- Late charges that exceed timely filing deadlines represent permanent revenue loss.

## Step 5 — Implement Charge Capture Controls

Build systematic processes to prevent missed charges.

- **Daily charge reconciliation**: Compare clinical schedules (OR schedule, clinic schedule, infusion appointments) against charges posted each day.
- **Nurse/tech charge validation**: Require nursing or technical staff to verify charges before the encounter is closed in the EMR.
- **Automated charge rules**: Configure the EMR to auto-generate charges from documented activities (e.g., when a nurse documents IV infusion start/stop times, the system generates the infusion charge).
- **Missing charge alerts**: Set up system alerts when encounters are documented but no charges are posted within the expected timeframe.
- **Provider charge capture scorecards**: Report charge capture completeness by provider monthly. Identify providers with consistently low capture rates for targeted education.
- **Charge capture rounding**: Periodic walkthroughs by revenue integrity staff to observe clinical workflows and identify charge capture gaps in real-time.

---

## Checkpoint B — Review

- [ ] Every documented service has been reconciled against posted charges
- [ ] Missed charges are quantified by category, department, and dollar amount
- [ ] Chargemaster CPT/HCPCS mappings are current and revenue codes are valid
- [ ] Charge lag metrics are calculated and benchmarked against targets
- [ ] High-risk missed charge categories (infusions, observation, implants, ED procedures) are specifically audited
- [ ] Overbilled charges (phantom charges without documentation) are identified and corrected
- [ ] Revenue recovery opportunity is calculated for identified missed charges
- [ ] Corrective actions include specific process changes, not just education

---

## Quality Audit

- [ ] Charge capture rate by department is tracked monthly (charges posted / services documented)
- [ ] Missed charge recovery rate (percentage of identified missed charges actually rebilled) is monitored
- [ ] Chargemaster is reviewed and updated at least annually for code changes
- [ ] Charge lag trends by department are improving or at target
- [ ] Auto-generated charges from EMR are audited for accuracy (auto-charges can overcharge if not configured correctly)
- [ ] Provider charge capture education is delivered at least annually
- [ ] Revenue integrity program ROI is calculated (program cost vs. recovered revenue)

---

## Guidelines

- Follow CMS OPPS guidelines for facility charge capture and APC packaging rules
- Apply CMS Medicare Claims Processing Manual Chapter 4 for billing/payment requirements
- Reference HFMA Revenue Integrity standards for charge capture program design
- Use AMA CPT and CMS HCPCS code updates effective January 1 annually for chargemaster maintenance
- Never bill charges for services not documented in the medical record
- Never automatically generate charges without a documented clinical service to support them
- Mark with [VERIFY] any charge where documentation support is ambiguous
- Include disclaimer that charge capture recommendations are based on documentation review and payer-specific billing rules may affect payability
