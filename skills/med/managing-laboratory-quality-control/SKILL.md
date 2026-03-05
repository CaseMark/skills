---
name: managing-laboratory-quality-control
description: Tracks QC data with Westgard rules and corrective action documentation. Use when managing lab QC, interpreting Westgard violations, or documenting corrective actions.
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

# Managing Laboratory Quality Control

Tracks QC data with Westgard rules and corrective action documentation.

## Why This Skill Exists

Quality control is the foundation of every reliable laboratory result. A single undetected QC failure can affect hundreds of patient results before discovery, leading to misdiagnoses, inappropriate treatments, and patient harm. CLIA 42 CFR 493.1256 mandates that laboratories perform quality control procedures as specified by the test system manufacturer or establish an equivalent QC program that provides equal or better assurance of accurate and reliable results. CAP accreditation (Chemistry/Toxicology CHM checklist, General checklist GEN) requires documentation of QC rules, corrective actions, and review processes.

The Westgard multi-rule system is the industry standard for statistical QC in clinical laboratories. It provides a structured decision framework that balances error detection (sensitivity) with false rejection rate (specificity). Laboratories that fail to implement and follow Westgard rules consistently face CAP citations, CLIA sanctions (from directed plans of correction to suspension of testing), and liability exposure from reporting results that were out of control.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

1. **Analyte/test system** — Which test or instrument is being monitored? Default: chemistry analyzer, general chemistry panel.
2. **QC material** — What levels are run (Level 1/low, Level 2/normal, Level 3/high)? Default: two levels per CLIA minimum.
3. **QC frequency** — When are QC materials run (each shift, daily, each analytical run, weekly)? Default: at minimum once per 24 hours per CLIA.
4. **QC rule set** — Which Westgard rules are applied (1-2s warning, 1-3s, 2-2s, R-4s, 4-1s, 10x)? Default: standard Westgard multi-rule.
5. **Current issue** — Is this routine QC review, a specific violation investigation, or method validation QC establishment? Default: routine review.
6. **Peer group data** — Are CAP proficiency testing or AACC peer group statistics available? Default: CAP survey results on file.
7. **EQC/IQCP status** — Is this test system on an Individualized Quality Control Plan (IQCP) or standard QC? Default: standard QC.

### Documents to Request

- Levey-Jennings charts for the past 30-60 days
- Current mean and SD values for each QC level
- Westgard rule violation log with corrective action documentation
- Manufacturer QC ranges and acceptable limits
- CAP peer group statistics for the analyte
- Instrument maintenance and calibration logs
- IQCP risk assessment (if applicable)
- Previous CAP/CLIA inspection findings related to QC

---

## Step 1: Establishing QC Parameters

Set up or verify QC statistical parameters for each analyte:

1. **Target mean**: Calculated from at least 20 data points (preferably 20 independent runs over 20+ days per CLSI C24-A4).
2. **Standard deviation (SD)**: Calculate from the same 20+ data points. Assess for outliers using Dixon or Grubbs test before finalizing.
3. **Coefficient of variation (CV)**: CV% = (SD/Mean) x 100. Compare to manufacturer claims, CLIA allowable total error (TEa), and CAP peer group CV.
4. **Control limits**: Set at mean +/- 2SD (warning) and mean +/- 3SD (rejection).

| QC Metric | Acceptable | Investigate | Unacceptable |
|---|---|---|---|
| CV% vs. manufacturer claim | <= manufacturer stated CV | 1-1.5x manufacturer CV | > 1.5x manufacturer CV |
| CV% vs. CAP peer group | <= peer group median CV | Between median and 90th percentile | > 90th percentile |
| Bias vs. peer group mean | < 0.5 x TEa | 0.5-1.0 x TEa | > TEa |

---

## Step 2: Applying Westgard Multi-Rules

Apply the Westgard multi-rule algorithm to each QC run:

| Rule | Detection | Action | Error Type |
|---|---|---|---|
| 1-2s | One control > 2SD from mean | WARNING only — do not reject | Alert for trend monitoring |
| 1-3s | One control > 3SD from mean | REJECT run | Random error |
| 2-2s | Two consecutive controls > 2SD same direction | REJECT run | Systematic error (shift) |
| R-4s | One control > +2SD and another > -2SD (range > 4SD) | REJECT run | Random error |
| 4-1s | Four consecutive controls > 1SD same direction | REJECT run | Systematic error (trend) |
| 10x | Ten consecutive controls on same side of mean | REJECT run | Systematic error (bias) |

**Decision tree for violations:**
1. 1-2s triggered → Inspect Levey-Jennings chart for trends. Do NOT reject patient results. Continue monitoring.
2. 1-3s, 2-2s, R-4s, 4-1s, or 10x triggered → REJECT the analytical run. Hold all patient results from that run. Investigate root cause. Repeat QC after corrective action.
3. Corrective action succeeds (QC in range) → Release patient results from the new run only.
4. Corrective action fails → Escalate per institutional protocol (supervisor, service engineer, laboratory director).

---

## Step 3: Root Cause Investigation and Corrective Action

When a Westgard rule violation occurs, investigate systematically:

**Immediate actions:**
- Repeat the QC with a fresh aliquot of the same QC lot.
- If still out, try a new vial of QC material (rule out QC material degradation).
- Check reagent expiration dates, lot numbers, and storage conditions.
- Review instrument maintenance logs for pending or overdue maintenance.

**Root cause categories:**

| Category | Examples | Corrective Action |
|---|---|---|
| QC material | Expired, improperly stored, contaminated | Replace QC material; review storage protocol |
| Reagent | Expired, wrong lot, degraded, contaminated | Replace reagent; verify lot |
| Calibration | Calibration drift, expired calibrator, wrong calibrator | Recalibrate; verify calibrator lot and expiration |
| Instrument | Lamp aging, probe clog, temperature drift | Perform maintenance; call service if needed |
| Operator | Incorrect pipetting, wrong QC assigned | Retrain; assess competency |
| Environmental | Temperature excursion, humidity, power fluctuation | Address environmental control |

**Documentation requirements** (per CAP GEN.20375):
- Date and time of violation
- Westgard rule triggered
- QC values and control limits
- Investigation steps performed
- Root cause identified (or "no assignable cause" if resolved by repeat)
- Corrective action taken
- Follow-up QC results confirming resolution
- Impact assessment on patient results (were any patient results reported during the out-of-control period?)

---

## Step 4: Levey-Jennings Chart Review and Trend Analysis

Perform regular (at minimum monthly) review of Levey-Jennings charts:

- **Shifts**: Six or more consecutive points on one side of the mean indicate a systematic change. Investigate even if within 2SD.
- **Trends**: Six or more consecutive points moving in one direction (up or down) indicate a progressive systematic error.
- **Increasing SD**: Compare monthly CV to the established CV. An increasing CV may indicate reagent degradation, instrument aging, or loss of precision.
- **Mean migration**: Compare monthly means to the established mean and to CAP peer group means. Drift may indicate calibration issues.

Document the review with: reviewer name, date, time period reviewed, findings, and any actions taken.

---

## Step 5: QC Program Reporting and Compliance

Generate QC compliance reports for laboratory leadership:

1. **Monthly QC summary**: Number of runs, number of violations by rule, corrective actions, resolution status.
2. **Analyte-specific trending**: CV% over time, mean stability, bias vs. peer group.
3. **Turnaround for corrective actions**: Time from violation to resolution.
4. **Patient impact assessment**: Number of patients potentially affected by out-of-control results and notification status.
5. **Regulatory readiness**: Compliance with CLIA QC frequency requirements, CAP checklist items, and IQCP documentation (if applicable).

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Are QC means and SDs based on at least 20 independent data points per CLSI C24-A4?
2. Is every Westgard rule violation documented with root cause investigation and corrective action?
3. Were patient results from out-of-control runs assessed for impact and recollected/re-run if necessary?
4. Are Levey-Jennings charts reviewed at least monthly with documented reviewer sign-off?
5. Does the QC program meet CLIA minimum frequency requirements (at minimum two levels per 24 hours for non-waived testing)?

---

## Quality Audit

- [ ] QC means and SDs established from minimum 20 data points
- [ ] Two levels of QC run at minimum per 24 hours per CLIA requirements
- [ ] Westgard multi-rule algorithm applied consistently to all QC data
- [ ] 1-2s used as warning only; no patient results rejected on 1-2s alone
- [ ] All 1-3s, 2-2s, R-4s, 4-1s, 10x violations documented with corrective action
- [ ] Root cause investigation documented for every out-of-control event
- [ ] Patient result impact assessment performed for every out-of-control run
- [ ] Levey-Jennings charts reviewed monthly with signed documentation
- [ ] QC material storage conditions monitored and documented
- [ ] Reagent and calibrator lot changes documented with crossover QC
- [ ] CV% compared to manufacturer claims and CAP peer group statistics
- [ ] IQCP risk assessment current (if applicable)
- [ ] QC records available for CAP/CLIA inspection (minimum 2-year retention)

---

## Guidelines

- Never release patient results from a run that failed a Westgard rejection rule (1-3s, 2-2s, R-4s, 4-1s, 10x) until the cause is resolved and QC passes
- The 1-2s rule is a WARNING only; it is not a rejection rule and should not trigger corrective action unless it occurs in conjunction with other rules
- When a new QC lot is introduced, run the old and new lots in parallel for at least 5 days (20 data points) to establish the new mean and SD before using the new lot for patient result validation
- Document every corrective action with enough detail that a CAP inspector can reconstruct the investigation from the written record
- Review Levey-Jennings charts at least monthly and look for shifts (6 consecutive same-side) and trends (6 consecutive directional) even when no rejection rules are triggered
- Compare your laboratory's CV% and bias to CAP peer group statistics at least semi-annually; persistent outlier performance requires method review
- Maintain all QC records for a minimum of 2 years per CLIA retention requirements; CAP recommends retention for the life of the instrument
- For tests on IQCP (Individualized Quality Control Plan), ensure the risk assessment is reviewed annually and updated when changes occur to personnel, environment, reagents, or specimen types
