---
name: managing-proficiency-testing
description: Tracks proficiency testing results with remediation for unacceptable performance. Use when managing PT programs, analyzing PT results, or documenting corrective actions for PT failures.
tags:
  - management
  - pathology
metadata:
  author: casemark
  practice_areas:
    - Pathology
    - Laboratory Medicine
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---

# Managing Proficiency Testing

Tracks proficiency testing results with remediation for unacceptable performance.

## Why This Skill Exists

Proficiency testing (PT) is the primary mechanism by which external regulatory bodies verify that a clinical laboratory produces accurate results. CLIA 42 CFR 493.801-865 mandates participation in an approved PT program for every analyte for which PT is available, and defines specific criteria for acceptable performance. Failure to participate, failure to achieve acceptable scores, or referral of PT samples to another laboratory are among the most serious violations a laboratory can commit — CLIA sanctions for PT failures escalate from mandated corrective action to suspension of the right to test the specific analyte after two consecutive or two of three testing events with unsatisfactory performance.

CAP accreditation requires enrollment in CAP Proficiency Testing Surveys and defines additional requirements beyond CLIA for PT sample handling, result review, and corrective action documentation. The laboratory director bears personal responsibility for PT program oversight. This skill provides a systematic framework for managing PT participation, analyzing results, investigating failures, and maintaining compliance.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **PT program** — Which PT provider (CAP, AABB, API, state program, alternative assessment)? Default: CAP Surveys.
2. **Analyte/discipline** — Which test or discipline is being evaluated? Default: not specified; flag [VERIFY].
3. **Testing event** — Which survey event (e.g., C-A 2024, Set 1 of 3)? Default: current event.
4. **Current result status** — Acceptable, unacceptable, or not graded? Default: awaiting results.
5. **Previous PT history** — Results from the prior two testing events for the same analyte? Default: satisfactory.
6. **Method/instrument** — What is the current test system and method? Default: per current SOPs.
7. **PT sample handling** — Were PT samples treated as patient specimens (same operators, same process)? Default: yes.

### Documents to Request

- PT program enrollment documentation for all regulated analytes
- PT challenge result certificates (current and prior two events)
- PT sample handling documentation (chain of custody, testing dates, operators)
- Grading criteria for the specific PT program (CLIA target values, peer group statistics)
- Corrective action reports from prior PT failures (if any)
- Laboratory's PT policy and procedure document
- CLIA-mandated PT performance criteria (42 CFR 493.923-959)
- Instrument and method SOP for the tested analyte

---

## Step 1: PT Sample Handling and Testing Compliance

Verify that PT samples are handled in compliance with CLIA and CAP requirements:

**Mandatory handling rules:**
- PT samples must be tested by the **same personnel** using the **same methods** as patient specimens (42 CFR 493.801(b)).
- PT samples must be **integrated into the routine workflow** — not separated for special handling, retesting, or consultation.
- Results must be submitted to the PT program **before** the deadline and **without** knowledge of the intended result.
- **Prohibited behaviors** (CLIA sanctions including revocation):
  - Sending PT samples to another laboratory for analysis
  - Communicating PT results to another laboratory before submission deadline
  - Intentional misrepresentation of PT results
  - Retesting PT samples after initial submission unless as part of a documented investigation

**Documentation checklist:**
- Date of PT sample receipt
- Date of testing (within the survey timeframe)
- Operator(s) who performed the testing
- Instrument and method used
- QC results on the day of PT testing
- Date and time of result submission

---

## Step 2: PT Result Evaluation and Grading

Analyze PT results against CLIA and CAP grading criteria:

### CLIA Fixed-Criteria Grading (42 CFR 493.923-959)

| Analyte | Acceptable Performance Criteria |
|---|---|
| Glucose | Target value +/- 6 mg/dL or +/- 10%, whichever is greater |
| Potassium | Target value +/- 0.5 mmol/L |
| Sodium | Target value +/- 4 mmol/L |
| Calcium (total) | Target value +/- 1.0 mg/dL |
| Chloride | Target value +/- 5% |
| BUN | Target value +/- 2 mg/dL or +/- 9%, whichever is greater |
| Creatinine | Target value +/- 0.3 mg/dL or +/- 15%, whichever is greater |
| Total protein | Target value +/- 10% |
| Hemoglobin | Target value +/- 7% |
| WBC count | Target value +/- 15% |
| Platelet count | Target value +/- 25% |
| PT (prothrombin time) | Target value +/- 15% |
| TSH | Target value +/- 3 SD from peer group mean |

### CAP Peer Group Grading

- CAP uses peer group comparison (same instrument/method/reagent) with acceptable range typically defined as +/- 2 SD or +/- 3 SD from the peer group mean.
- SDI (Standard Deviation Index) = (Lab result - Peer group mean) / Peer group SD.
  - SDI +/- 1.0: Acceptable
  - SDI +/- 1.5-2.0: Marginal, investigate
  - SDI > +/- 2.0: Review required
  - SDI > +/- 3.0: Unacceptable

---

## Step 3: Failure Investigation and Root Cause Analysis

When a PT result is scored as unacceptable, perform a systematic investigation:

**Immediate actions:**
1. Review the QC data from the day PT samples were tested. Were any Westgard violations present?
2. Examine patient results run on the same day. Were any clinically discordant results identified?
3. Check the PT sample handling: was it properly reconstituted, tested within stability limits, and not contaminated?
4. Review the instrument maintenance log: was any maintenance performed around the testing date?

**Root cause categories:**

| Category | Investigation Steps | Common Causes |
|---|---|---|
| Analytical | Review QC, calibration, reagent lot, instrument maintenance | Calibration drift, reagent degradation, instrument malfunction |
| Pre-analytical (PT-specific) | Review reconstitution, timing, storage, matrix effects | Improper reconstitution, exceeding stability, matrix interference |
| Clerical | Review result transcription, unit conversion, submission entry | Transcription error, wrong analyte entered, decimal point error |
| Methodological | Compare method-specific peer group performance | Method bias, known matrix effect with PT material |
| Operator | Review competency, training, testing compliance | New operator, unfamiliar with PT protocol |

---

## Step 4: Corrective Action and Documentation

Document the investigation and corrective actions per CAP and CLIA requirements:

**Required documentation elements:**
1. PT event identification (survey, analyte, challenge, result, target, peer group data)
2. Root cause analysis findings
3. Corrective action taken (specific and measurable)
4. Verification that corrective action resolved the issue (subsequent QC, patient result review, repeat testing)
5. Preventive measures to avoid recurrence
6. Laboratory director review and signature
7. Timeline: Investigation should be completed before the next PT event

**CLIA escalation for repeated failures:**

| Failure Pattern | CLIA Consequence |
|---|---|
| 1 unacceptable event | Corrective action required; document investigation |
| 2 consecutive unsatisfactory events for same analyte | Directed plan of correction; may require on-site inspection |
| 2 of 3 consecutive unsatisfactory events | Sanctions applied; laboratory may lose right to test that analyte |
| Unsuccessful PT program participation overall | Risk of CLIA certificate suspension or revocation |

---

## Step 5: Ongoing Monitoring and Compliance Reporting

Maintain continuous PT program oversight:

1. **Enrollment audit**: Annually verify enrollment in PT for all regulated analytes. Analytes without available PT must have an alternative assessment program (42 CFR 493.1236).
2. **Result tracking**: Maintain a PT result database with SDI trending for each analyte. Flag analytes with SDI trending toward marginal performance before formal failure.
3. **Corrective action tracking**: Monitor completion of corrective actions from prior failures. Verify that preventive measures remain in place.
4. **Annual PT summary**: Prepare an annual report for laboratory leadership summarizing overall PT performance, failure rate, corrective actions, and trend analysis.
5. **Inspector readiness**: Maintain organized PT files with result certificates, handling documentation, investigation reports, and corrective action records. CAP inspectors will review PT records for every surveyed analyte.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Were PT samples handled as routine patient specimens (same operators, same methods, integrated into workflow)?
2. Is the root cause analysis documented with specific findings (not "no assignable cause" as a default)?
3. Are corrective actions specific, measurable, and verified by subsequent QC or testing data?
4. Is the laboratory director's review and signature documented on the investigation?
5. Is the PT enrollment current for all regulated analytes?

---

## Quality Audit

- [ ] PT enrollment active for all CLIA-regulated analytes
- [ ] PT samples handled per CLIA requirements (same personnel, methods, routine workflow)
- [ ] PT results submitted before program deadline
- [ ] No prohibited PT behaviors (inter-lab referral, result communication, retesting for submission)
- [ ] All acceptable results documented and filed
- [ ] Unacceptable results investigated with root cause analysis
- [ ] Corrective actions documented with verification of resolution
- [ ] Laboratory director review and signature on all PT investigations
- [ ] SDI trending monitored for all analytes
- [ ] Analytes without available PT covered by alternative assessment
- [ ] Annual PT performance summary prepared for laboratory leadership
- [ ] PT records organized and accessible for CAP/CLIA inspection
- [ ] CLIA escalation tracking current for any analytes with prior failures

---

## Guidelines

- Treat PT samples exactly as patient specimens — any deviation in handling, testing, or result review constitutes a CLIA violation and may invalidate the entire testing event
- Never communicate PT results to other laboratories or reference the expected results before submission — this is grounds for CLIA certificate revocation
- Investigate every unacceptable PT result with a structured root cause analysis; "no assignable cause found" should be the conclusion of an exhaustive investigation, not a default
- Track SDI trends continuously; an SDI drifting toward +/- 2.0 should trigger proactive investigation before a formal failure occurs
- Maintain awareness of CLIA's two-consecutive or two-of-three failure rule; after a first failure, the next event is critical and warrants heightened review before submission
- For analytes without an available PT program, implement and document an alternative assessment per CLIA 42 CFR 493.1236 (split-sample testing with a reference laboratory, blind testing from a validated source, or clinical correlation review)
- Complete PT investigations before the next testing event; delayed investigations risk compounding failures
- Review PT enrollment comprehensively at least annually to capture new analytes, retired tests, and changes in PT program offerings
