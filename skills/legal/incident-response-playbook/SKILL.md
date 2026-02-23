---
name: incident-response-playbook
description: >-
  Drafts U.S. legal-organization incident response plans and playbooks for
  cybersecurity incidents and data breaches, aligning NIST SP 800-61 Rev. 2
  with ABA Model Rules 1.1/1.4/1.6, client confidentiality, and privilege
  preservation. Use when creating or updating an incident response plan,
  breach response policy, ransomware playbook, or regulatory notification
  checklist. Trigger keywords: incident response plan, playbook, data breach,
  ransomware, cybersecurity policy, NIST 800-61, ABA Model Rules, client
  confidentiality.
tags:
  - checklist
  - drafting
  - memo
  - regulatory
---

# Incident Response Plan and Playbook

Produces a defensible, operational incident response plan and scenario playbooks tailored to legal organizations.

## Prerequisites

1. **Firm profile** — practice areas, jurisdictions, client types, office locations, critical systems.
2. **Current policies** — security, acceptable use, retention, BCP/DR, vendor management.
3. **Data map** — systems holding client confidential or privileged data, backups, cloud providers.
4. **Regulatory scope** — applicable data breach laws, ethics rules, sector regulations (HIPAA, GLBA, CMMC, etc.).
5. **Contacts** — internal response team and external vendors with after-hours channels.

## Output Structure / Process

1. **Confirm scope and standards** — NIST SP 800-61 Rev. 2 alignment; ABA Model Rules 1.1, 1.4, 1.6; state bar guidance.
2. **Build the plan** — governance, taxonomy, detection, phased response, communications, training.
3. **Add playbooks** — ransomware, email compromise, unauthorized case access, inadvertent disclosure.
4. **Add appendices** — contacts, templates, logs, escalation matrix, legal authority map.
5. **Quality check** — privilege posture, notification timeframes, role coverage, version control.

### 1) Plan Header and Governance

**Header Block (template)**  
Title, version, effective date, approvers, distribution, storage location, last review date, next review date.

**Governance Table**

| Role | Primary Duties | Decision Authority | Backups |
|---|---|---|---|
| Incident Response Coordinator | Activate plan, triage, oversee response | Yes | Named alternates |
| Legal/Ethics Counsel | Privilege, ethics, notifications, regulators | Yes | Named alternates |
| IT/Security Lead | Forensics, containment, eradication | Yes | Named alternates |
| Managing Partner/ED | Resourcing, client impact, business decisions | Yes | Named alternates |
| Comms Lead | Internal/external messaging | Yes | Named alternates |
| Practice Leaders | Client context, matter impact | Advisory | Named alternates |

**External Engagement Criteria (checklist)**  
- [ ] Forensics firm on retainer or pre-approved  
- [ ] Breach counsel on retainer  
- [ ] Cyber insurer notification triggers  
- [ ] Law enforcement criteria defined  
- [ ] PR firm criteria defined

### 2) Scope and Incident Taxonomy

**Scope Statement**  
Covered incidents include cyber events, confidentiality breaches, privilege risks, ethical violations affecting representation, and physical compromise of client data.

**Severity Matrix**

| Severity | Example Triggers | Required Actions | Notification Clock |
|---|---|---|---|
| Critical | Widespread client data exposure, ransomware impacting active matters, privilege compromise | Immediate activation, exec notification | Immediate |
| High | Targeted account takeover, multi-matter access | Activate response team | Within 2 hours |
| Medium | Single user phishing, limited exposure | IT + counsel review | Same business day |
| Low | Blocked attempts, policy violations | Log + monitor | Standard queue |

### 3) Detection and Reporting

**Detection Sources**  
SIEM, EDR, DLP, email security, user reports, vendor alerts, audit logs.

**Incident Report Intake (fields)**  
Date/time discovered, reporter, systems affected, data types, client matters impacted, actions taken, evidence preserved.

**Privilege Protocol**  
Investigations directed by counsel; mark communications “Privileged & Confidential”; separate factual incident log from legal analysis.

### 4) Phased Response (NIST-Aligned)

**Preparation**  
- [ ] Security controls baseline  
- [ ] Annual training and phishing simulations  
- [ ] Tabletop exercises  
- [ ] Vendor and insurer contacts verified  
- [ ] Backup restoration tests

**Identification**  
- [ ] Validate incident  
- [ ] Scope systems/data  
- [ ] Classify severity  
- [ ] Determine client/privilege impact

**Containment**  
- [ ] Short-term isolation actions  
- [ ] Account resets and access control  
- [ ] Long-term containment plan

**Eradication**  
- [ ] Remove malware  
- [ ] Patch vulnerabilities  
- [ ] Confirm adversary ejected

**Recovery**  
- [ ] Restore from clean backups  
- [ ] Validate integrity  
- [ ] Resume operations with monitoring

**Lessons Learned**  
- [ ] Post-incident review within 14 days  
- [ ] Update plan and controls  
- [ ] Metrics captured

### 5) Scenario Playbooks

**Ransomware Playbook**  
- [ ] Isolate affected systems  
- [ ] Notify insurer and breach counsel  
- [ ] Assess exfiltration indicators  
- [ ] Evaluate restore options and legal posture  
- [ ] Law enforcement decision

**Email Account Compromise**  
- [ ] Reset credentials and tokens  
- [ ] Review mailbox rules and sent items  
- [ ] Identify client communications affected  
- [ ] Notify clients if required  
- [ ] Harden MFA and mail security

**Unauthorized Case File Access**  
- [ ] Identify matters and data types  
- [ ] Assess privilege impact  
- [ ] Client notification determination  
- [ ] Access control remediation

**Inadvertent Privilege Disclosure**  
- [ ] Notify receiving party  
- [ ] Demand return/destruction  
- [ ] Document inadvertence  
- [ ] Evaluate waiver risks

### 6) Communications and Notifications

**Internal Comms Rules**  
Need-to-know distribution, secure channels, counsel-led updates.

**Client Notification Minimums**  
Incident summary, data types affected, timeline, remediation steps, client actions.

**Regulatory Notifications Matrix (template)**

| Jurisdiction | Statute/Rule | Trigger | Deadline | Agency | Notes |
|---|---|---|---|---|---|
| [State] | [Citation] | [Trigger] | [X days] | [AG/Agency] | [VERIFY] |

**Ethics Notification Considerations**  
ABA Model Rules 1.4 (client communication), 1.6 (confidentiality), 1.1 (tech competence).

### 7) Training, Testing, and Metrics

**Training Cadence**  
Annual all-hands security training; role-based IR team training.

**Testing**  
Annual tabletop; periodic phishing simulations; quarterly backup restore tests.

**Metrics**  
MTTD, MTTC, MTTR, notification deadline compliance.

### 8) Appendices

**Contact Roster**  
Internal team, vendors, insurer, law enforcement, regulators.

**Templates**  
Incident report form, client notice letter, regulator notice, media holding statement.

**Incident Log (template)**

```
Date/Time | Event | System | Action | Owner | Evidence Location | Privileged?
```

**Escalation Matrix**  
Severity thresholds and authority required for notifications and public statements.

## Guidelines

- Do not include jurisdiction-specific deadlines without verification; mark with `[VERIFY]`.
- Keep privilege intact: counsel directs investigations and reviews all outbound notices.
- Align with NIST SP 800-61 Rev. 2 and applicable ethics rules; cite local bar guidance when used.
- Avoid admissions of liability in external communications.
- Update annually and after material incidents, firm mergers, or major system changes.
