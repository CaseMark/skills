---
name: incident-response-plan
description: Drafts a comprehensive Incident Response Plan and Playbook for legal organizations managing cybersecurity incidents, data breaches, and regulatory compliance events. Adapts NIST SP 800-61 to legal practice contexts including attorney-client privilege preservation, ethics obligations, and state breach notification compliance. Use when creating IR plans, cybersecurity playbooks, breach response policies, or data incident procedures for law firms or legal departments.
tags:
  - checklist
  - drafting
  - memo
  - regulatory
---

# Incident Response Plan and Playbook

Drafts a legally defensible incident response plan adapted for legal organizations, covering cybersecurity incidents, data breaches, privilege preservation, and professional responsibility compliance.

## Prerequisites

1. **Organization profile** — firm structure, practice areas, office locations, jurisdictions of operation
2. **Existing policies** — current infosec policies, business continuity plans, professional responsibility guidelines
3. **Regulatory landscape** — applicable state breach notification statutes, sector-specific requirements (HIPAA, GLBA, CMMC if relevant)
4. **Technology environment** — case management systems, DMS, email platforms, backup infrastructure
5. **Insurance coverage** — cyber insurance policy details, carrier contact, claim procedures

## Output Structure

### 1. Jurisdictional Analysis

Identify and document:

| Factor | Details |
|--------|---------|
| Operating jurisdictions | States/federal where firm practices |
| Breach notification statutes | Per-state triggers, timeframes (typically 30-90 days), AG notification requirements |
| Professional conduct rules | State-specific versions of ABA Model Rules 1.1 (tech competence), 1.4 (communication), 1.6 (confidentiality) |
| Sector overlays | HIPAA, GLBA, CMMC, SEC if applicable to practice areas |
| Ethics opinions | Relevant state bar opinions on cybersecurity duties |

### 2. Incident Taxonomy

Classify using four severity tiers:

| Tier | Criteria | Examples | Response Time |
|------|----------|----------|---------------|
| **Critical** | Widespread client data compromise; privilege breach affecting case outcomes; mandatory reporting triggered | Ransomware on DMS during active litigation; mass exfiltration of client files | Immediate (24/7) |
| **High** | Multi-matter client data exposure; attorney email compromise | BEC targeting partner in M&A negotiation; unauthorized case file access | ≤2 hours (business hours) |
| **Medium** | Isolated access attempts; contained inadvertent disclosure | Single phishing compromise; misdirected privileged email | ≤4 hours (business hours) |
| **Low** | Blocked attempts; policy violations without data exposure | Failed intrusion attempt; unauthorized software installation | Next business day |

Legal-specific incident types to address:
- Inadvertent disclosure of privileged communications
- Unauthorized access to case management systems
- Conflicts-of-interest data exposure
- Email account compromise of attorneys
- Ransomware affecting document management
- Physical breach of client file storage

### 3. Governance Structure

Define these roles with specific responsibilities per response phase:

| Role | Function | Key Authorities |
|------|----------|-----------------|
| **IR Coordinator** | Activates plan, convenes team, operational decisions | Authority to isolate systems, engage external resources |
| **General Counsel / Ethics Counsel** | Legal/ethical analysis, privilege protection | Directs privileged investigation, approves client notifications |
| **CISO / IT Director** | Technical response, forensics | System isolation, evidence preservation, restoration |
| **Managing Partner** | Strategic decisions, resource allocation | Approves expenditures, client relationship decisions |
| **Communications Director** | Internal/external messaging | Media responses (with counsel approval) |
| **Practice Group Leaders** | Client-specific context | Matter-level impact assessment |

Include:
- After-hours contact roster (multiple channels per person)
- Escalation chain when primary contacts unavailable
- External resource engagement criteria and contacts

### 4. Phased Response Procedures

Structure around NIST SP 800-61 phases adapted for legal practice:

**Phase 1 — Preparation**
- Preventive controls inventory
- Security awareness training schedule (annual minimum)
- External expert relationships (forensics, breach counsel, PR)
- Tabletop exercise program (annual minimum)

**Phase 2 — Identification**
- [ ] Validate incident (distinguish from false positive)
- [ ] Preliminary scope assessment — systems and data affected
- [ ] Determine if client confidential or privileged materials involved
- [ ] Assign severity tier
- [ ] Activate response team per severity level
- [ ] Initiate investigation under counsel direction to preserve privilege

**Phase 3 — Containment**

Short-term (immediate):
- [ ] Isolate affected systems
- [ ] Disable compromised accounts
- [ ] Block malicious IPs/domains
- [ ] Secure physical access points

Long-term (operational continuity):
- [ ] Enhanced monitoring on affected segments
- [ ] Apply emergency patches
- [ ] Migrate to backup systems if needed

**Phase 4 — Eradication**
- [ ] Remove malware/unauthorized access
- [ ] Close exploited vulnerabilities
- [ ] Verify no persistent backdoors
- [ ] Validate threat actor access eliminated

**Phase 5 — Recovery**
- [ ] Restore from verified clean backups
- [ ] Implement enhanced controls
- [ ] Conduct system integrity testing
- [ ] Gradual return to operations with heightened monitoring

**Phase 6 — Lessons Learned** (within 14 days of closure)
- [ ] Post-incident review meeting
- [ ] Document findings and timeline
- [ ] Update IR plan based on gaps identified
- [ ] Implement preventive measures

### 5. Scenario Playbooks

Draft step-by-step playbooks for each:

**Ransomware on DMS/Case Management:**
1. Isolate affected systems immediately
2. Notify cyber insurance carrier
3. Assess backup integrity and restoration timeline
4. Evaluate exfiltration indicators (double extortion)
5. Determine client notification obligations per jurisdiction
6. Consider law enforcement engagement (FBI IC3)
7. Document all decisions under privilege

**Attorney Email Compromise:**
1. Reset credentials; revoke active sessions
2. Review sent items, forwarding rules, mailbox rules
3. Identify client communications accessed/forwarded
4. Assess privilege implications per affected matter
5. Notify affected clients per Rule 1.4 obligations
6. Implement MFA if not already in place

**Inadvertent Privilege Disclosure:**
1. Notify opposing counsel immediately per FRE 502(b) [VERIFY]
2. Request return/destruction of materials
3. Document inadvertence circumstances
4. Assess waiver risk under applicable jurisdiction's law
5. File clawback motion if necessary

### 6. Communication Protocols

| Audience | Trigger | Timing | Approval Required | Template |
|----------|---------|--------|-------------------|----------|
| IR Team | Any confirmed incident | Immediate | IR Coordinator | Internal alert template |
| Senior Leadership | High/Critical severity | Within 1 hour | IR Coordinator | Executive briefing template |
| Affected Clients | Client data compromised | Per jurisdiction statute; ethics rules require "prompt" notice | General Counsel + Managing Partner | Client notification letter |
| State AG / Regulators | Statutory threshold met | Per state statute (varies 30-90 days from discovery) | General Counsel | Regulatory filing template |
| Law Enforcement | Criminal activity suspected; ransomware | Case-by-case | General Counsel | LEA referral template |
| Media | Public exposure or inquiry | Reactive only | General Counsel + Communications | Holding statement |

Key principles:
- All external communications reviewed by counsel before release
- Investigation communications marked "Privileged & Confidential — Attorney Work Product"
- Client notifications comply with both breach statutes AND professional conduct rules
- Need-to-know basis for internal distribution

### 7. Training and Testing Program

| Activity | Frequency | Audience | Documentation |
|----------|-----------|----------|---------------|
| Security awareness training | Annual | All personnel | Completion records |
| IR team specialized training | Annual | IR team members | Training log |
| Tabletop exercises | Annual minimum | IR team + leadership | Exercise report |
| Phishing simulations | Quarterly | All personnel | Results metrics |
| Backup restoration tests | Semi-annual | IT team | Test results |
| Plan review and update | Annual + post-incident | IR Coordinator | Version control log |

Track metrics: time to detect, time to contain, time to eradicate, time to recover, notification compliance.

### 8. Appendices

Include:
- [ ] Contact roster (internal IR team + external resources)
- [ ] Incident reporting form template
- [ ] Client notification letter templates (customize per jurisdiction)
- [ ] Regulatory filing templates
- [ ] Escalation matrix by severity tier
- [ ] Evidence preservation checklist
- [ ] Jurisdiction-specific breach notification quick-reference table
- [ ] Version control and approval log

## Guidelines

- **Privilege preservation**: All investigation activities must be directed by counsel; mark work product accordingly
- **Dual-purpose format**: Number all sections for rapid navigation during live incidents; include hyperlinked TOC
- **Jurisdiction specificity**: Map each operating state's breach notification statute — do not rely on generic summaries
- **Cite current authority**: Reference specific statutes, ABA Model Rules, and ethics opinions; mark uncertain citations with `[VERIFY]`
- **Modular design**: Structure sections for independent revision as regulations change
- **Professional conduct integration**: Every notification and communication procedure must satisfy both statutory AND ethics obligations
- **Document for defensibility**: The plan itself serves as evidence of reasonable security measures under Rule 1.1 competence duty
- **No legal advice to client**: This plan governs internal firm response — separate client advisory communications as needed
