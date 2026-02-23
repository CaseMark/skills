---
name: breach-summary
description: >-
  Summarizes cybersecurity breach incidents into a structured legal and
  compliance record for US legal teams, security leadership, and executive
  decision-makers. Use when synthesizing incident reports, forensics, logs,
  notifications, and related records into a defensible chronology,
  scope-impact analysis, response ledger, and regulatory-risk assessment.
  Trigger keywords: cybersecurity breach, data breach, incident response,
  unauthorized access, ransomware, exfiltration, notification obligations,
  GDPR, CCPA, HIPAA.
tags:
  - regulatory
  - summarization
  - summary
---

# Cybersecurity Breach Summary

Produces a fact-based breach incident summary for leadership, counsel, and regulator-facing communications with preserved evidence links and explicit uncertainty handling.

## Prerequisites

1. Collect governing documents: incident ticket, forensics reports, SOC/SIEM logs, threat-notification logs, legal notices, board/investor updates, and insurance correspondence.
2. Confirm a current data map showing affected systems, data types, and affected populations (customers, employees, partners, patients, etc.).
3. Confirm jurisdiction mapping of impacted individuals/entities and any contractual/processor obligations.
4. Confirm privileges and confidentiality constraints before summarizing legal review material.
5. Confirm notification status and timeline already triggered (internal, regulator, affected persons, law enforcement).

## Output Structure / Process

| Phase | Required sections |
| --- | --- |
| 1 | Intake matrix: source list, creator, date range, reliability, and key gaps |
| 2 | Executive overview: discovery timing, attack type, severity, current status |
| 3 | Chronology: compromise window, detection point, response milestones, evidence anchors |
| 4 | Scope and impact: technical vectors, compromised assets, data classes, affected population |
| 5 | Response ledger: containment, eradication, remediation, communications, ownership |
| 6 | Legal/regulatory analysis: notification triggers, timing calculations, litigation risk |
| 7 | Forward remediation: root causes, control failures, action owners, verification steps |

Output requirements:
- Include only sourced facts in declarative statements.
- Distinguish `Verified`, `Corroborated`, and `Unverified`.
- Use ranges or confidence scores when exact counts remain unknown.
- Include citations per statement: `(document name, timestamp, section/page)`.

```text
Cybersecurity Breach Summary

Incident ID:
Reporting period:
Primary custodians (security/counsel/compliance):
Severity: High | Medium | Low
Current status: Ongoing | Contained | Remediated
```

```text
Executive Overview
- Discovery date/time:
- Attack type and likely entry point:
- Systems/environments impacted:
- Data sensitivity exposed:
- Immediate business impact:
```

```text
Chronology
- Initial compromise date/time and confidence:
- Detection source:
- Key forensic milestones:
- Containment actions:
- Notification milestones:
```

```text
Scope & Impact
- Attack vector and exploit chain:
- Systems and databases affected:
- Data categories accessed/exfiltrated/altered:
- Estimated affected records/persons (min-max):
- Evidence of secondary spread or persistence:
```

```text
Response Actions
- Actions taken:
- Actions pending:
- Law enforcement/third-party involvement:
- Stakeholder notifications by date/method:
- Security patches/hardening completed:
```

```text
Legal & Regulatory Assessment
- Jurisdictions with potential statutory impact:
- Triggered obligations (if known):
- Compliance deadlines and whether currently met:
- Pending legal/commercial exposure:
- Insurance and contractual notice status:
```

```text
Open Issues
- Facts still under investigation:
- Data still not collected:
- Next evidence needed:
```

```text
Forward-Looking Remediation
- Root causes:
- Process/policy control fixes:
- Verification and test plan:
- Responsible owners and target dates:
```

| Framework | Prescriptive checks | Core evidence |
| --- | --- | --- |
| GDPR | Breach notifications and supervisory-authority obligations (including timeliness) [VERIFY] | Breach triage memo, impacted-EU-persons index |
| CCPA/CPRA | Consumer notice scope and timing for California data subjects [VERIFY] | Data-location mapping, consumer notification content draft |
| HIPAA | PHI-specific reporting and breach-notification duties [VERIFY] | PHI inventory, HITECH/HIPAA risk assessment inputs |
| State laws (US) | State-specific deadlines, consumer notice thresholds, media notice rules | State-by-state population map, attorney-confirmed matrix |
| Contractual duties | SaaS/cloud processor notices, indemnity, and reporting clauses | Core agreements, SLAs, contract addenda |

## Guidelines

- Do not overstate certainty; label unknowns as `unverified` and describe next validation step.
- Separate legal analysis from factual log to preserve evidentiary utility.
- Keep chronology time-zone explicit and consistent.
- Flag any missing records that could alter legal exposure.
- Separate completed tasks from planned tasks; include owners for all open items.
- For potentially privileged material, preserve evidence indexes without quoting legal advice.
- If a jurisdictional deadline is missed or uncertain, escalate with impact and corrective plan first, details second.
