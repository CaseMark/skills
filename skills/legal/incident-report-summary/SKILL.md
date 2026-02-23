---
name: incident-report-summary
description: Generates structured, litigation-ready summaries from police reports, workplace incident reports, or similar investigative documents. Extracts parties, officer narratives, citations, witness details, contributing factors, and diagram descriptions into a standardized analytical format. Use when summarizing police reports, accident reports, incident reports, crash reports, or investigative documentation for case assessment, discovery planning, or liability evaluation.
tags:
  - litigation
  - summarization
  - summary
---

# Police/Incident Report Summary

Produces a structured, litigation-ready summary from police or incident reports optimized for case assessment, discovery planning, and liability evaluation.

## Prerequisites

1. **Source report** — police report, crash report, workplace incident report, or similar investigative document (PDF, scan, or text)
2. **All attachments** — supplemental reports, continuation sheets, witness statement forms, diagrams, photos
3. **Matter identifier** — case name or number for document labeling

## Output Structure

Produce a summary with the following sections in order:

### 1. Header

| Field | Extract |
|-------|---------|
| Report/Case Number | Official identifier from document |
| Incident Date/Time | With time zone if available |
| Report Filed Date | If different from incident date |
| Location | Full address, intersection, or mile marker |
| Agency | Name, officer/investigator, badge number |
| Report Type | Collision, criminal, workplace, etc. |

### 2. Parties Involved

For each party, extract into a structured block:

- **Role**: Driver / Passenger / Pedestrian / Victim / Suspect / Reporting Party / Employee
- **Name**: Full legal name
- **DOB / Age**
- **Address**
- **Contact**: Phone, email
- **ID**: Driver's license number + state, or employee ID
- **Vehicle** (if applicable): Year, make, model, color, VIN, plate number
- **Insurance** (if applicable): Carrier, policy number, agent
- **Injuries noted**: As described in report

### 3. Narrative Summary

Provide two versions:

- **Complete narrative**: Preserve the officer/investigator's full account
- **Key facts extract**: Condensed list of legally significant facts only:
  - Admissions of fault
  - Observations of impairment, recklessness, distraction
  - Physical evidence (skid marks, distances, measurements)
  - Injury descriptions
  - Safety equipment use or non-use
  - Environmental conditions at time of incident

Flag: ambiguities, contradictions, or temporal gaps in the narrative.

### 4. Citations / Charges / Violations

| Person Cited | Statute/Code | Violation Description | Issued At Scene? | Court Date | Fine/Penalty |
|---|---|---|---|---|---|

### 5. Witness Information

For each witness:

| Field | Detail |
|-------|--------|
| Name | Full name |
| Contact | Phone, address, email |
| Relationship | Independent / party-related |
| Location at incident | Where they were, what direction they faced |
| Statement summary | Key observations in their words |

Note:
- Preserve direct quotes verbatim (potential excited utterances / hearsay exceptions)
- Flag witnesses identified but not interviewed
- Flag references to unidentified potential witnesses

### 6. Contributing Factors

Categorize each factor and note its evidentiary basis:

| Category | Factor | Evidence Source |
|----------|--------|-----------------|
| Environmental | Weather, lighting, road surface, visibility | Physical evidence / narrative |
| Human | Speed, inattention, impairment, fatigue, violations | Witness / admission / observation |
| Equipment | Mechanical failure, defects, maintenance | Inspection / narrative |
| Systemic | Training gaps, supervision, hazardous conditions | Report findings |

Flag factors suggesting:
- **Third-party liability** (road design defects, product defects, employer violations)
- **Affirmative defenses** (comparative negligence, assumption of risk, intervening cause)

### 7. Visual Documentation

For each diagram, sketch, or photo in the report, provide a textual description covering:

- **Collision diagrams**: Road configuration, lanes, traffic controls, vehicle positions (pre/during/post impact), direction of travel, point of impact, final rest positions, measurements
- **Photos**: Subject depicted, perspective, visible damage/injuries, environmental conditions, evidence markers
- Note any information in visuals not mentioned in the narrative

### 8. Gaps and Follow-Up Items

Checklist of missing or unclear information requiring further investigation:

- [ ] Missing party contact information
- [ ] Uninterviewed or unidentified witnesses
- [ ] Narrative contradictions needing deposition clarification
- [ ] Missing supplemental reports referenced but not attached
- [ ] Unclear measurements or diagram elements
- [ ] Pending lab results, toxicology, or reconstruction reports

## Guidelines

- Every fact in the summary must trace to specific language in the source report — no inference or speculation
- Distinguish between officer's direct observations and information relayed by others
- Use consistent date format (MM/DD/YYYY) and time format (12h or 24h) throughout
- Adapt extraction fields to report type — not all fields apply to all incident types (e.g., vehicle info irrelevant for workplace incidents)
- Protect sensitive PII not relevant to liability or damages
- Format for immediate incorporation into case files: clear headings, tables for repetitive data, scannable structure
- The summary must be self-sufficient — an attorney should understand essential facts, parties, and issues without the original report
