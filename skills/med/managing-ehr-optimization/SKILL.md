---
name: managing-ehr-optimization
description: Identifies EHR optimization opportunities through usage analysis and workflow improvement. Use when optimizing EHR workflows, reducing click burden, or improving EHR usability.
tags:
  - management
  - health-informatics
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

# Managing EHR Optimization

Identifies EHR optimization opportunities through usage analytics, workflow analysis, and clinician feedback to reduce documentation burden, improve usability, and enhance clinical efficiency. This skill covers post-implementation optimization using EHR signal data, clinician experience measurement, and structured improvement cycles.

## Why This Skill Exists

Post-go-live EHR environments accumulate inefficiency: order sets become outdated, alert fatigue builds as CDS rules are added without retirement, documentation templates grow unwieldy, and workarounds become embedded in clinical culture. Studies consistently show that physicians spend 2 hours on EHR documentation for every 1 hour of direct patient care. The AMA's "Reimagining Residency" initiative, the Surgeon General's advisory on healthcare worker burnout, and ONC's Strategy on Reducing Regulatory and Administrative Burden cite EHR usability as a primary contributor. Systematic EHR optimization reclaims clinical time, reduces burnout risk, and improves data quality.


The 25th Anniversary of Patient Safety report (2024) and the National Academy of Medicine's clinician burnout reports consistently identify EHR usability as a modifiable contributor to both clinician burnout and patient safety events. Organizations that systematically optimize their EHR environment measurably reduce documentation burden and improve clinical data quality.
---

## Checkpoint A --- Intake & Scoping

Answer every question before proceeding. Mark unknowns with [VERIFY].

1. **EHR platform and version** --- Which system? (Epic 2024, Cerner Millennium, MEDITECH Expanse) Current version and upcoming upgrade timeline
2. **Optimization scope** --- Enterprise-wide or specific department/specialty? Which clinical workflows are highest priority?
3. **Available data** --- What EHR usage analytics are accessible? (Epic Signal/Cogito, Cerner Lights On Network, vendor-specific audit logs, time-motion study data)
4. **Known pain points** --- What are clinicians' top complaints? (Documentation time, click burden, alert fatigue, search difficulties, slow system performance)
5. **Previous optimization efforts** --- What has been tried? What worked, what did not?
6. **Governance structure** --- Is there a clinical informatics optimization committee? Who approves build changes?
7. **Burnout data** --- Are there provider satisfaction or burnout survey results (Mini-Z, Maslach Burnout Inventory) that correlate with EHR usage?

### Required Documents

- EHR usage analytics reports (Epic Signal dashboard, time-in-system metrics, note authoring time)
- Current CDS alert inventory with override rates
- Active order set catalog with last-reviewed dates
- Documentation template catalog with utilization rates
- Clinician satisfaction survey results related to EHR
- IT ticket history related to EHR usability (last 12 months)

8. **Vendor optimization programs** --- Has the organization participated in vendor-sponsored optimization programs (Epic Boost, Cerner Optimization Services)? What recommendations were implemented?
9. **Regulatory constraints** --- Are there regulatory requirements that constrain optimization (Promoting Interoperability measures, eCQM data capture, state reporting mandates)?

### EHR Burden Benchmarks

| Metric | Published Benchmark | Target |
|---|---|---|
| Total EHR time per day (physician) | 4.5 hours (AMA) | < 4 hours |
| After-hours EHR time (pajama time) | 1.5 hours/day | < 1 hour |
| Alerts per provider per day | 50-100 | < 50 |
| Alert override rate (interruptive) | 80-95% | < 70% for retained alerts |
| Inbox messages per provider per day | 50-80 | < 50 |
| Note length (primary care, characters) | 8,000-15,000 | < 8,000 |
---

## Step 1 --- Measure Current State

Quantify the optimization opportunity with data:

- **Time-in-system analysis** --- Extract per-provider time metrics: total time in EHR per day, time in notes, time in orders, time in inbox, after-hours (pajama time) usage. Benchmark against peer cohorts within the organization and published benchmarks
- **Click and navigation analysis** --- For targeted workflows, count the number of clicks and screen transitions required to complete common tasks: admission order entry, medication reconciliation, discharge workflow, result review. Compare against EHR vendor's recommended workflow
- **Alert burden quantification** --- Calculate per-provider alert volume: total alerts per session, alerts per order, override rate by alert category. Identify alerts with > 90% override rates as immediate candidates for revision or retirement
- **Documentation analysis** --- Measure: average note length by specialty, percentage of note content from copy-forward, percentage of note content from auto-populated templates, time from encounter start to note completion
- **Inbox burden** --- Quantify messages per provider per day by message type: patient messages, staff messages, result notifications, refill requests, administrative tasks. Identify the highest-volume categories
- **System performance** --- Measure page load times, search response times, and system availability. Technical slowness creates perceived usability problems independent of workflow design

- **Peer comparison** --- Where available, benchmark provider-level metrics against organizational peers (same specialty, similar panel size). Providers significantly above the median for time-in-system may benefit from targeted workflow coaching, while those significantly below may have data quality concerns
---

## Step 2 --- Identify Optimization Opportunities

Categorize findings into actionable improvement areas:

- **Order set rationalization** --- Identify order sets that are: rarely used (< 5 uses/month), outdated (not reviewed in > 12 months), redundant (multiple order sets for the same clinical scenario), or non-compliant with current formulary/guidelines. Flag order sets with high modification rates (clinicians consistently changing defaults) for redesign
- **Alert optimization** --- Apply the CDS alert optimization framework: retire alerts with > 90% override rates and no documented patient safety events, convert interruptive alerts to passive notifications where clinically safe, consolidate duplicate/overlapping alerts, add suppression rules for repeat firings
- **Documentation efficiency** --- Identify opportunities for: SmartPhrase/dot-phrase standardization, template redesign to reduce unnecessary fields, note-bloat reduction (removing auto-populated content that adds length without value), specialty-specific documentation shortcuts
- **Inbox management** --- Design routing rules to direct messages to appropriate team members (nurse vs. physician vs. scheduler), implement patient message auto-responses for common requests, enable prescription refill automation for eligible medications
- **Navigation shortcuts** --- Build specialty-specific navigator or sidebar configurations, create quick-access buttons for frequently used functions, optimize chart search to surface commonly needed data first

---

## Step 3 --- Prioritize and Plan

Rank optimizations by impact and feasibility:

- **Impact scoring** --- Estimate time savings per provider per day for each optimization. Weight by: number of affected providers, frequency of the optimized workflow, and severity of the current pain point
- **Feasibility scoring** --- Assess implementation complexity: configuration-only change (low effort), build with testing (moderate effort), custom development or vendor request (high effort). Also assess governance complexity: standard change (analyst approval), clinical content change (informatics committee approval), workflow redesign (department approval)
- **Risk classification** --- Tag each optimization for patient safety risk: high-risk (changing CDS alerts, modifying medication workflows), moderate-risk (order set changes, documentation template changes), low-risk (navigation shortcuts, display preferences)
- **Sprint planning** --- Organize optimizations into 2-4 week sprint cycles. Each sprint should include a mix of quick wins (< 4 hours to implement, immediate impact) and planned improvements (require testing and approval)
- **Provider champion identification** --- For each major optimization, identify a physician or nurse champion who will validate the change, communicate to peers, and provide feedback during implementation

- **Optimization governance** --- Establish a standing EHR optimization committee with representation from clinical informatics, IT, nursing, pharmacy, and physician leadership. Define change approval authority levels: minor changes (analyst approval), moderate changes (committee review), major changes (executive approval). Meet biweekly during active optimization cycles
---

## Step 4 --- Implement and Test

Execute optimizations with quality controls:

- **Build standards** --- Follow EHR vendor best practices for build: naming conventions, folder organization, record ownership, version documentation. Every build change gets a change control ticket with: description, rationale, approver, build date, effective date
- **Testing protocol** --- For each optimization: unit test (does the configuration work as designed?), workflow test (does the optimized workflow improve the target metric?), regression test (does the change break adjacent workflows?)
- **Clinician validation** --- Before production deployment, have 2-3 representative clinicians walk through the optimized workflow in a test environment. Capture feedback and iterate before release
- **Change communication** --- Notify affected users before each change: what is changing, why, how to use the new workflow, and who to contact with questions. Use multiple channels (email, huddle announcements, EHR tip sheets)
- **Rollback plan** --- For every optimization, document the rollback procedure. High-risk changes should have a tested rollback that can execute within 15 minutes

---

## Step 5 --- Measure Outcomes

Validate that optimizations achieved their intended effect:

- **Pre/post metric comparison** --- Re-measure the same metrics from Step 1 after optimization deployment. Allow 4-6 weeks for clinicians to adapt before measuring. Use statistical significance testing for small populations
- **Provider feedback survey** --- Conduct targeted surveys 4-6 weeks post-implementation: "Has this change improved your workflow?" "Are there unintended consequences?" Use Likert scale plus free-text feedback
- **Unintended consequence monitoring** --- Watch for: increased calls to the help desk about the changed workflow, new workarounds developing, downstream data quality issues (e.g., template changes affecting data capture for quality measures)
- **Sustained improvement tracking** --- Continue monitoring metrics quarterly to ensure improvements persist. Some optimizations degrade over time as new content is added or workflows evolve
- **ROI calculation** --- Translate time savings into financial and operational impact: FTE-equivalent time saved, potential additional patient encounters, reduced pajama-time hours, provider satisfaction improvement

- **Longitudinal tracking dashboard** --- Maintain a standing optimization dashboard tracking: total time-in-system trend, after-hours usage trend, alert volume and override rate, inbox volume, patient satisfaction correlation, and provider satisfaction/burnout scores. Review at least quarterly with organizational leadership
---

## Checkpoint B --- Optimization Cycle Review

After each optimization sprint:

- [ ] All planned optimizations were implemented or deferred with documented rationale
- [ ] Testing was completed for every change with documented results
- [ ] Clinician validation was obtained before production deployment
- [ ] Change communication reached all affected users
- [ ] Pre/post metrics demonstrate measurable improvement
- [ ] No unintended consequences require rollback or remediation
- [ ] Learnings are documented for the next optimization cycle
- [ ] Backlog is updated with new optimization opportunities identified during this cycle

- [ ] Vendor optimization program recommendations (if applicable) have been evaluated and implemented or deferred with rationale
- [ ] Regulatory constraints on optimization have been identified and documented
- [ ] Longitudinal optimization dashboard is operational with quarterly leadership review
---

## Quality Audit

- [ ] Optimization priorities are data-driven (EHR analytics, not anecdotal complaints alone)
- [ ] Alert optimization follows published alert fatigue reduction frameworks
- [ ] Order sets are reviewed against current clinical guidelines and formulary
- [ ] Documentation template changes are validated against quality measure data capture requirements
- [ ] High-risk optimizations (CDS, medication workflows) have clinical informatics committee approval
- [ ] Every change has a documented change control ticket with rollback procedure
- [ ] Post-implementation metrics are measured and reported
- [ ] Optimization program reports to organizational leadership on quarterly cadence
- [ ] Provider burnout/satisfaction metrics are included as outcome measures

- [ ] EHR burden metrics are benchmarked against published industry data (AMA, KLAS)
- [ ] Optimization governance committee is chartered with defined change authority levels
- [ ] Ambulatory and inpatient optimization priorities are balanced and tracked separately
- [ ] Vendor release notes are reviewed within 30 days of release for optimization-relevant features
---

## Guidelines

- Optimization is continuous, not a project. Establish a standing optimization program with dedicated clinical informatics FTE, not one-time initiatives
- Let data drive priorities. Provider complaints are valuable signals, but EHR analytics often reveal larger time savings from workflows that providers have adapted to and no longer complain about
- Every alert retired saves more clinical time than most build improvements. Alert fatigue reduction should be the highest-priority optimization category
- Protect quality measure data capture when optimizing documentation templates. A shorter note that fails to capture structured data for eCQM reporting trades documentation efficiency for financial penalty
- Copy-forward is a clinical risk, not just an efficiency tool. Notes with > 50% copied content should be flagged for clinical review and template redesign
- After-hours EHR usage ("pajama time") is a burnout indicator with direct patient safety implications. Prioritize optimizations that reduce pajama time even if they do not reduce total time-in-system
- Vendor release notes should trigger optimization review. New features in EHR upgrades often address existing pain points, but only if someone evaluates and activates them
- Involve nursing, pharmacy, and allied health in optimization, not just physicians. EHR burden affects all clinical roles, and optimizing one role's workflow at the expense of another creates no net improvement

- Measure optimization impact in clinician-meaningful terms: minutes saved per day, fewer clicks for common tasks, fewer unnecessary alerts. Abstract metrics ("we retired 50 alerts") mean nothing without demonstrating the downstream time and cognitive load reduction
- Nursing and pharmacy EHR burden is often overlooked in optimization programs dominated by physician voice. Ensure optimization governance includes nursing informatics and pharmacy informatics representation with equal standing