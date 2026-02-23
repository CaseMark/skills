---
name: vendor-security-assessment
description: Drafts a comprehensive Vendor Security Assessment Questionnaire to evaluate third-party vendors' cybersecurity practices, data handling, and regulatory compliance before contract execution. Aligns with GDPR, CCPA, HIPAA, SOX, GLBA, FERPA, and industry frameworks. Vendor responses become binding contractual representations with executive certification. Use during vendor due diligence, third-party risk management, procurement security review, or subprocessor evaluation.
tags:
  - checklist
  - drafting
  - regulatory
---

# Vendor Security Assessment Questionnaire

Drafts a due-diligence questionnaire for evaluating third-party vendor cybersecurity posture, data handling practices, and regulatory compliance prior to contract execution.

## Prerequisites

1. **Vendor scope definition** — data types vendor will access (PII, PHI, PCI, financial, proprietary), processing activities, and anticipated data flows
2. **Applicable regulatory frameworks** — GDPR, CCPA, HIPAA, SOX, GLBA, FERPA, or industry-specific requirements
3. **Organization's data classification standards** and vendor management policies (if any)
4. **Contract templates** — to align questionnaire with security provisions that will be incorporated into the agreement
5. **Risk tolerance thresholds** — what constitutes acceptable vs. disqualifying vendor risk

## Output Structure

### Document Framework

| Section | Purpose |
|---|---|
| Cover page & instructions | Completion is mandatory pre-contract; responses are binding representations incorporated by reference |
| Executive certification | Senior officer (CISO/CTO/CLO) attests to accuracy; signature block required |
| Submission deadline | 10–15 business days |
| Ongoing notification obligation | Vendor must notify within 5 business days of material security posture changes |
| Confidentiality statement | Questionnaire and responses treated as confidential business information |

### Assessment Domains

Draft numbered questions for each domain. Use a consistent format: question, response field, and evidence-request field where applicable.

**1. Information Security Governance**
- Dedicated CISO/equivalent with certifications (CISSP, CISM, CISA)
- Security policy framework alignment (NIST CSF, ISO 27001, CIS Controls, COBIT)
- Policy review cadence and update process
- Security awareness training program (all-staff + specialized for devs/admins)
- Board-level security metrics and reporting frequency

**2. Data Classification & Lifecycle Management**
- Data classification taxonomy and compatibility with client's scheme
- All geographic locations of data storage/processing (primary, DR, backup, cloud regions)
- Cross-border transfer mechanisms (SCCs, adequacy decisions, BCRs)
- Data residency commitments and jurisdictional restrictions
- Retention periods post-termination, destruction methods, certificates of destruction
- Backup frequency, encryption of backup media, tested RTO/RPO

**3. Access Control & Privileged Access Management**
- MFA enforcement (all access; specify supported factors)
- Password/passkey policies; passwordless authentication status
- RBAC implementation and least-privilege enforcement
- Segregation of duties controls
- Privileged access management (JIT elevation, session recording, auto-deprovisioning)
- Access recertification frequency and remediation process
- Audit trail retention period and anomalous-access alerting

**4. Vulnerability Management & Security Testing**
- Vulnerability scanning tools, frequency, and patching SLAs by severity:

| Severity | Patch SLA |
|---|---|
| Critical | ≤ 24–72 hrs |
| High | ≤ 7 days |
| Medium | ≤ 30 days |
| Low | ≤ 90 days |

- Annual third-party penetration testing (external + internal lateral movement)
- Application security testing (SAST, DAST, SCA) for custom software
- Bug bounty / responsible disclosure program participation
- Request: summary of most recent pentest findings and remediation status

**5. Incident Response & Business Continuity**
- Documented IR plan with defined roles, escalation, and communication protocols
- IR testing frequency (tabletop exercises, simulations) and most recent results
- Notification timeline — must allow client to meet its own regulatory deadlines (GDPR 72 hrs, HIPAA 60 days, state breach laws)
- Information provided at initial notification and during investigation
- Cooperation commitment with client's IR team and legal counsel
- Cyber insurance: policy limits, third-party liability coverage, adequacy for data volume
- BCP/DR: tested RTO/RPO, backup geographic diversity, multi-scenario resilience

**6. Encryption & Key Management**
- Data at rest: algorithm/key length (minimum AES-256), scope (production, dev/test, backups, portable media)
- Database encryption approach (TDE, column-level, application-layer)
- Data in transit: TLS versions supported, deprecated protocol status, enforced cipher suites
- Data in use: confidential computing / secure enclave capabilities (if applicable)
- Key management: generation method, storage (HSM/KMS), access controls, rotation frequency
- Key backup, recovery, and secure destruction procedures

**7. Network Security & Segmentation**
- Network segmentation: customer isolation, production vs. corporate separation
- Zero-trust architecture implementation status
- Perimeter controls: firewalls, IDS/IPS, WAF, DDoS protection
- Threat intelligence feed integration
- Remote access security: VPN, NAC/device posture, MFA
- Network security assessment cadence (external scans, internal pentests, wireless)

**8. Third-Party / Subprocessor Risk Management**
- Complete subprocessor inventory: role, data access type, geographic location, security assessments conducted
- Flow-down of security requirements (contractually at least as stringent as client's)
- Subprocessor approval process and ongoing monitoring/audit activities
- Client notification and approval rights before engaging new subprocessors
- Right to terminate non-compliant subprocessors

**9. Certifications & Compliance**
- SOC 2 Type II: report date, principles covered, opinion status, auditor, scope alignment with contracted services
- ISO 27001: certificate dates, scope, certification body
- PCI DSS Attestation of Compliance (if applicable)
- FedRAMP / StateRAMP authorization (if applicable)
- Industry-specific: HITRUST, TISAX, etc.
- Regulatory compliance confirmation for applicable data types (HIPAA, FERPA, GLBA, export controls)
- Commitment to provide updated reports/certifications annually

**10. Physical Security & Environmental Controls**
- Data center access controls: MFA, visitor logs, video surveillance, security personnel
- Background checks for personnel with physical access
- Environmental: fire suppression, UPS, generators, climate control, water detection
- Facility certifications (SSAE 18 SOC 1, Uptime Institute tier)
- Third-party data center validation if using colocation

**11. HR Security & Insider Threat**
- Background check scope and periodic re-investigation for sensitive roles
- Security training before system access; policy acknowledgment requirement
- Offboarding: access revocation timeline, exit procedures, property return
- Insider threat monitoring: anomalous access detection, large download alerts
- DLP technologies for unauthorized exfiltration prevention

### Risk Assessment Framework

After receiving vendor responses, produce a formal assessment report:

| Rating | Criteria |
|---|---|
| Low | Controls meet or exceed requirements; evidence provided |
| Moderate | Minor gaps; addressable via contractual provisions |
| High | Significant gaps; requires remediation plan with deadlines |
| Critical | Fundamental deficiencies; disqualifying absent remediation |

Report must include:
- Per-domain risk rating with justification
- Overall vendor risk rating
- Recommended contractual controls (audit rights, insurance minimums, SLAs, monitoring obligations)
- Evidence gaps requiring follow-up (certifications, audit reports, IR test results, sample policies)
- Go/no-go recommendation with conditions
- Flagged inconsistencies between vendor responses and other known information

## Guidelines

- Vendor responses are **contractually binding representations** — state this explicitly in the questionnaire preamble
- Incomplete, inaccurate, or misleading responses constitute grounds for disqualification or material breach
- Tailor framework requirements to the **sensitivity of data and criticality of services** — not every vendor needs every question
- Align notification timelines with the **most restrictive applicable breach notification law**
- Flag any vendor that refuses to disclose subprocessors or share certification reports as elevated risk
- All legal citations to specific regulatory provisions should be verified against current law [VERIFY]
- Cross-reference vendor claims against publicly available information (e.g., published certifications, breach history)
- Mark questions as required vs. conditional based on data type (e.g., PCI questions only if payment data involved)
