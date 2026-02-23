---
name: ir-tabletop-exercise
description: Drafts a comprehensive tabletop exercise script to test an organization's Incident Response Plan for cybersecurity incidents. Incorporates regulatory compliance with data breach notification laws (GDPR, CCPA, HIPAA, GLBA, PCI DSS, NERC CIP, DFARS). Generates progressive scenario injects, participant role assignments, facilitation guides, and after-action report frameworks. Use when creating IR tabletop exercises, cybersecurity drills, breach response simulations, or incident preparedness assessments.
tags:
  - checklist
  - drafting
  - regulatory
---

# Tabletop Exercise Script for Incident Response Plan

Generates a ready-to-execute tabletop exercise script that stress-tests an organization's IR Plan against realistic cyber threats and regulatory notification obligations.

## Prerequisites

1. **Existing IR Plan** — current incident response plan, escalation hierarchies, severity classification framework
2. **Regulatory profile** — applicable frameworks (GDPR, CCPA, HIPAA, GLBA, PCI DSS, NERC CIP, DFARS, SEC) and notification deadlines
3. **Org context** — industry sector, data holdings (PII, PHI, PCI, IP), org chart for crisis roles, prior exercise after-action reports
4. **Participant list** — confirmed attendees with titles and IR Plan roles

## Output Structure

### 1. Document Research Phase

Before drafting, extract from provided materials:

| Element | Source |
|---|---|
| Notification deadlines | Regulatory docs (e.g., GDPR 72-hr, state-specific 30–90 day windows) |
| Escalation hierarchy | IR Plan org chart, decision-making authority matrix |
| Regulated data types | Data inventory (PII, PHI, PCI, classified/CUI) |
| Prior gaps | Previous after-action reports, audit findings |
| Contractual obligations | Vendor agreements, cyber insurance policies, customer DPAs |

### 2. Scenario Design

Select a threat scenario matched to the org's risk profile. Options:

| Scenario Type | Regulatory Triggers | Key Complexity |
|---|---|---|
| Ransomware + exfiltration | Breach notification + OFAC sanctions screening | Dual operational/legal pressure |
| Business email compromise | Wire fraud + credential harvesting | Financial + data exposure |
| Supply chain compromise | Multi-party notification, vendor coordination | Shared liability, scope ambiguity |
| Insider threat | Employee data, HR/legal coordination | Attribution, evidence preservation |
| APT campaign | IP theft, potential state-actor, law enforcement | Prolonged timeline, classification issues |

**Scenario brief must include:**
- Date/time and operational context
- First indicator of compromise (realistic: IDS alert, help desk ticket, third-party tip, customer complaint)
- Sufficient technical detail for discussion without requiring deep technical expertise
- 3–5 measurable exercise objectives tied to IR Plan and regulatory compliance

### 3. Participant Roles

Assign participants to these functional groups:

| Group | Roles | Key Responsibilities |
|---|---|---|
| **Core IR Team** | IR Manager, Security Analysts, IT Ops, Forensics | Triage, containment, evidence preservation, technical investigation |
| **Legal & Compliance** | General Counsel, DPO/CPO, Compliance Officer, Outside Counsel | Notification obligations, litigation hold, privilege, sanctions review |
| **Executive** | CEO/Crisis Authority, CISO, CFO, Business Unit Leads | Strategic decisions, business continuity, materiality assessment |
| **Communications** | PR/Comms Lead, Customer Service Lead, HR (if employee data), Investor Relations (if public) | Media, customer inquiries, internal messaging, SEC disclosure |

**Pre-exercise packet per participant:** relevant IR Plan sections, role card with decision authority, applicable notification templates/checklists, data holdings summary.

### 4. Progressive Scenario Injects

Design 4–5 injects using this structure per inject:

```
## Inject [N] — [Title]
**Timestamp:** T+[elapsed time]
**New Information:** [What participants learn]

### Discussion Questions
1. [Question testing specific IR Plan procedure]
2. [Question testing regulatory threshold/notification trigger]
3. [Question testing cross-functional coordination]

### Expected Outputs
- [ ] [Decision or action item participants should produce]
- [ ] [Document or notification they should initiate]

### Facilitator Notes
- Time allocation: [X] minutes
- Key points that must emerge: [list]
- Red flags to note: [gaps indicating IR Plan deficiencies]
```

**Inject progression:**

| Inject | Focus | Tests |
|---|---|---|
| **1: Detection** | Initial alert, IR Plan activation | Severity classification, initial containment, evidence preservation, escalation |
| **2: Escalation** | Scope wider than expected (lateral movement, data access/exfil) | Notification threshold analysis, external forensics engagement, insurance carrier notice, legal coordination |
| **3: External Pressure** | Ransom demand / media leak / regulator inquiry / customer detection | Threat actor communication (OFAC screening), public messaging, regulatory response, consistent cross-team messaging |
| **4: Recovery & Notification** | Forensic conclusions, system restoration, notification deadlines arriving | Notification content sufficiency, individual notice method/content, credit monitoring decision, public disclosure (SEC 8-K if applicable) |
| **5 (optional): Special Complications** | Cross-border (multi-DPA notification), law enforcement delay request, third-party vendor coordination, sector-specific reporting (NERC CIP, CISA) | Jurisdiction conflicts, notification timing tensions, multi-party coordination |

### 5. Facilitation Guide

Include at the top of the script:

- **Ground rules:** Learning environment; honest discussion > perfect answers; no-fault; Chatham House Rule if desired
- **Timing:** Total duration (typically 2–4 hours), time per inject, break schedule
- **Facilitator role:** Present injects, ask probing follow-ups, ensure all groups participate, document observations without correcting in real-time
- **Materials needed:** Printed inject cards, IR Plan copies, regulatory quick-reference sheet, whiteboard/shared doc for decisions

### 6. Debrief & After-Action Report Framework

**Structured debrief agenda (30–45 min):**

1. What worked well — effective procedures, coordination, decisions
2. Gaps identified — use this checklist:
   - [ ] Unclear roles or decision authority
   - [ ] Missed or late notification triggers
   - [ ] Communication breakdowns (technical ↔ legal ↔ executive)
   - [ ] Evidence preservation failures
   - [ ] Unrealistic IR Plan assumptions
   - [ ] Resource/capability gaps
3. Root cause discussion per gap
4. Remediation actions with owner + target date

**After-action report sections:**

| Section | Content |
|---|---|
| Executive Summary | Scenario, objectives, overall assessment |
| Participants | Name, title, exercise role |
| Observations by IR Phase | Detection → Containment → Eradication → Recovery → Notification |
| Gap Analysis | Gap description, risk rating (H/M/L), root cause |
| Remediation Plan | Action, owner, deadline, success criteria |
| Recommendations | Future exercise topics, training needs, capability investments |

**Distribution:** Participants, executive leadership, board/audit committee, CISO office.

## Guidelines

- Tailor scenario complexity to participant experience — avoid overwhelming first-time participants
- Include at least one inject that forces a **regulatory notification deadline decision** with incomplete information
- Test **OFAC/sanctions compliance** if ransomware scenario involves payment demands
- Ensure the exercise tests **attorney-client privilege** preservation during incident response
- Do not assume participants know notification deadlines — build a quick-reference card:

| Regime | Deadline | Authority |
|---|---|---|
| GDPR Art. 33 | 72 hours to DPA | Supervisory Authority |
| HIPAA | 60 days to HHS OCR; immediate if 500+ | HHS OCR + media if 500+ |
| CCPA/CPRA | "Most expedient time possible" | CA AG |
| State AG (varies) | 30–90 days depending on state | State AG + affected individuals |
| SEC (public co.) | 4 business days (material incident, Item 1.05 Form 8-K) [VERIFY] | SEC |
| PCI DSS | Per card brand rules, typically 24–72 hrs | Card brands + acquiring bank |
| NERC CIP | 1 hour (CIP-008-6) [VERIFY] | NERC E-ISAC + CISA |

- Mark any citation or deadline you cannot confirm with `[VERIFY]`
- Avoid scripting "correct" answers — the exercise tests the org's plan, not a model plan
- Flag if the org lacks a severity classification framework — the exercise cannot function without one
