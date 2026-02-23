---
name: cybersecurity-breach-summary
description: >-
  Produces structured cybersecurity breach summary documents for regulatory
  and compliance use, covering discovery, incident mechanics, affected
  systems, data scope, response actions, notification status, and legal
  exposure. Use for breach summaries, incident response report synthesis,
  forensic report summaries, board updates, and regulatory notification prep.
  Trigger keywords: data breach, cybersecurity incident, breach summary,
  incident report, forensic analysis, notification timeline, GDPR, CCPA/CPRA,
  HIPAA, state breach law.
tags:
  - regulatory
  - summarization
  - summary
---

# Cybersecurity Breach Summary

Produce a legally defensible, source-attributed incident summary suitable for executive, counsel, and regulator review.

## Prerequisites

1. Incident reports, forensic analyses, and relevant system logs.
2. Known discovery date/time, incident window, and current response status.
3. Inventory of affected systems/applications and data categories.
4. Known or estimated affected population counts and jurisdictions.
5. Response actions taken and planned, including containment and remediation.
6. Notification obligations and any notices already sent.
7. Contractual notice/cure requirements and cyber insurance details, if applicable.
8. Privilege boundaries and confidentiality flags from counsel.

## Output Structure / Process

Use the template below. Populate only with verified facts. Attribute each key fact to a source and date. Separate known facts from hypotheses or open questions.

````markdown
# Executive Overview
- Discovery date/time (timezone):
- Incident window (earliest to latest evidence):
- Incident type / attack vector:
- Affected systems:
- Data categories involved:
- Estimated affected individuals:
- Current status (contained/ongoing):
- Immediate actions taken:
- Material business impact:

# Incident Timeline
| Date/Time (TZ) | Event | Source (doc + date) | Owner | Confidence |
|---|---|---|---|---|

# Technical Summary
- Initial access vector:
- Vulnerability or control failure:
- Lateral movement evidence:
- Persistence mechanisms:
- Exfiltration evidence:
- Integrity/availability impacts:

# Systems Affected
| System/App | Environment | Data Stored | Impact | Status | Source |
|---|---|---|---|---|---|

# Data Impact
| Data Category | Regulated? | Population Type | Est. Count | Jurisdictions | Evidence/Source |
|---|---|---|---|---|---|

# Affected Population
| Population | Est. Count (range if needed) | Jurisdictions | Notes |
|---|---|---|---|

# Response Actions
| Action | Date | Owner | Status | Evidence/Source |
|---|---|---|---|---|

# Notifications
| Recipient | Legal Basis | Deadline | Sent Date | Method | Content Summary | Source |
|---|---|---|---|---|---|---|

# Legal/Regulatory Assessment
| Regime | Applicability Trigger | Deadline Rule | Status | Notes |
|---|---|---|---|---|
| GDPR Art. 33/34 [VERIFY] | | | | |
| HIPAA Breach Notification Rule (45 CFR 164.400–414) [VERIFY] | | | | |
| CCPA/CPRA [VERIFY] | | | | |
| State breach laws (list states) | | | | |

# Contractual / Litigation Exposure
- Key contracts with notice obligations:
- SLAs or security addenda implicated:
- Potential claims and venues:
- Preservation actions taken:

# Insurance
- Carrier/policy:
- Notice sent (date/time):
- Coverage issues or reservations:

# Open Issues / Ongoing Investigation
- 

# Remediation & Lessons Learned
| Gap/Root Cause | Corrective Action | Owner | Due Date | Status |
|---|---|---|---|---|

# Source Map
| Fact | Source Document | Date | Page/Section |
|---|---|---|---|
````

## Guidelines

- Maintain a factual, non-speculative tone; label unknowns explicitly.
- Use date/time with timezone and keep a single chronological basis of record.
- When scope is uncertain, use ranges and explain the basis.
- Attribute all material assertions to a specific source document and date.
- Keep privileged content in clearly marked sections if required by counsel.
- List all jurisdictions implicated by affected individuals, not just HQ location.
- If unsure about a legal citation or deadline, mark it `[VERIFY]`.
- Do not opine on liability; describe exposure factors and triggers only.
