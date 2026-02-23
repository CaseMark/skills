---
name: information-security-policy
description: Drafts a binding Information Security Policy document for organizations subject to HIPAA, GDPR, CCPA, GLBA, FERPA, or PCI DSS. Produces a formal governance document covering data classification, access controls, encryption standards, incident response, breach notification, and enforcement. Tailored by industry (healthcare, financial services, education) and regulatory environment. Use when drafting or overhauling an organization's foundational information security governance framework, cybersecurity policy, or data protection policy.
tags:
  - drafting
  - policy
  - regulatory
  - research
---

# Information Security Policy

Drafts a formal, board-approvable Information Security Policy that satisfies multi-framework regulatory requirements and provides enforceable operational guidance.

## Prerequisites

1. **Org profile** — industry sector, number of employees, jurisdictions of operation
2. **Regulatory triggers** — which frameworks apply (HIPAA, GDPR, CCPA, GLBA, FERPA, PCI DSS, SOC 2, ISO 27001, NIST CSF)
3. **Existing governance docs** — current policies, data classification schemes, incident response plans, acceptable use policies
4. **Data inventory** — categories of sensitive data handled (PHI, PII, payment card data, student records, trade secrets)
5. **Approving authority** — CEO, Board, CISO, General Counsel signature blocks needed

## Output Structure

### Document Control Block
| Field | Content |
|-------|---------|
| Policy Title | Information Security Policy |
| Version | [#] |
| Effective Date | [Date] |
| Approved By | [Title] |
| Owner | CISO / [equivalent] |
| Next Review | [Date + 1 year] |
| Supersedes | [Prior version or N/A] |

---

### Section Outline

**1. Purpose & Authority**
- Business rationale (financial, reputational, regulatory, contractual risk)
- Authorizing resolution or executive directive
- Relationship to other organizational policies (hierarchy/supersession)

**2. Scope**
- **Entities:** parent, subsidiaries, affiliates, JVs
- **Personnel:** employees (FT/PT/temp), contractors, consultants, vendors, partners
- **Assets:** electronic data, physical records, IP, trade secrets, personal data, BYOD, remote/home environments
- **Exclusions:** publicly available information, de-identified data (define standard used)

**3. Definitions**
Define with legal precision; flag where definitions vary by jurisdiction:

| Term | Definition |
|------|-----------|
| Confidential Information | [Org-specific; include examples] |
| Personal Data / PII | Per applicable law (GDPR Art. 4, CCPA § 1798.140, HIPAA 45 C.F.R. § 160.103) |
| Data Breach | Unauthorized acquisition, access, use, or disclosure of protected information |
| Security Incident | Any event threatening CIA triad of organizational information |
| Data Owner | Business unit leader accountable for data; approves access |
| Data Custodian | IT/ops responsible for technical controls over data |
| Authorized User | Individual with approved access to specific systems/data |
| Classification Levels | Public / Internal / Confidential / Restricted (defined below) |

**4. Data Classification**

| Level | Description | Examples |
|-------|-------------|---------|
| Public | Approved for external release | Marketing materials, press releases |
| Internal | General business use; not for external distribution | Org charts, internal memos |
| Confidential | Sensitive; limited distribution; contractual/legal obligations | Customer PII, financial data, contracts |
| Restricted | Highest sensitivity; regulatory or legal protection | PHI, payment card data, trade secrets, credentials |

**5. Access Controls**
- **Least privilege:** access rights scoped to minimum necessary for job function
- **Separation of duties:** no single individual controls entire critical process
- **Lifecycle:** formal request → approval by data owner → provisioning → quarterly review → prompt revocation on role change or termination
- **Privileged access:** separate accounts for administrative functions; logged and audited

**6. Authentication Requirements**

| Requirement | Standard |
|-------------|---------|
| Minimum password length | 12+ characters |
| Complexity | Mixed case, numbers, symbols; no dictionary words |
| MFA required for | Remote access, privileged accounts, Restricted data systems, cloud admin consoles |
| Acceptable MFA factors | TOTP, hardware token, biometric; SMS discouraged for high-risk systems |
| Shared credentials | Prohibited |

**7. Encryption Standards**

| Context | Minimum Standard |
|---------|-----------------|
| Data at rest (Confidential/Restricted) | AES-256 |
| Data in transit | TLS 1.2+ (TLS 1.3 preferred) |
| Portable devices (laptops, USB, mobile) | Full-disk encryption required |
| Email (Restricted data) | End-to-end encryption or secure portal |
| Backup media | Encrypted with separate key management |

Encryption standards reviewed annually; superseded by organizational Security Standards document if more stringent.

**8. Acceptable Use**
- Prohibited: illegal activity, harassment, unauthorized commercial use, circumventing security controls, sharing credentials
- Personal use: [specify permitted/prohibited scope]
- Monitoring: org reserves right to monitor systems; no expectation of privacy on org systems
- BYOD: must enroll in MDM; encryption required; remote wipe authorized upon loss/termination

**9. Physical Security**
- Unattended devices must be locked/secured
- Clean desk: Confidential/Restricted materials not left visible
- Secure disposal: cross-cut shredding (paper); cryptographic erasure or physical destruction (media)
- Visitor access: escorted in secure areas; visitor logs maintained

**10. Data Retention & Disposal**

| Data Category | Retention Period | Legal Basis |
|---------------|-----------------|------------|
| PHI | 6 years from creation or last use | HIPAA 45 C.F.R. § 164.530(j) |
| Financial records | 7 years | IRS / GLBA |
| Student records | Per FERPA schedule | 34 C.F.R. § 99 |
| Employee records | [Per state law] | [Cite] |
| Incident logs | 3 years minimum | [Regulatory basis] |

Secure deletion required upon expiration; certificate of destruction for Restricted data.

**11. Roles & Responsibilities**

| Role | Key Obligations |
|------|----------------|
| Board / Executive Management | Policy approval; resource allocation; tone-at-top |
| CISO | Program ownership; standards; audit oversight; regulator/LE liaison |
| IT / Security | Control implementation; patching; monitoring; vulnerability management |
| Legal / Privacy Counsel | Breach notification decisions; regulatory liaison; contractual compliance |
| Managers | Access approval; team compliance; off-boarding enforcement |
| All Employees | Credential protection; incident reporting; training completion; policy adherence |
| Data Protection Officer | Required under GDPR Art. 37; advisory role on processing activities |

**12. Incident Response**

*Incident types:* unauthorized access, data breach, malware/ransomware, phishing compromise, lost/stolen devices, insider threat, denial-of-service, physical breach.

**Lifecycle:**
1. **Detect & Report** — employee reports within [1-4 hours] to [security hotline / email / on-call]
2. **Assess** — severity triage; activate IRT if Severity 1 or 2
3. **Contain** — isolate affected systems; preserve evidence; chain of custody maintained
4. **Eradicate** — remove threat; patch vulnerability
5. **Recover** — restore from clean backups; verify integrity
6. **Post-Incident Review** — within 14 days; root cause analysis; corrective action plan with owners and deadlines

**IRT composition:** CISO (lead), IT Security, Legal, HR, PR/Communications, Executive Sponsor.

**13. Breach Notification Obligations**

| Framework | Notification Trigger | Deadline | Recipients |
|-----------|---------------------|----------|-----------|
| HIPAA | Breach of unsecured PHI | 60 days from discovery (individuals); annual report to HHS for <500; 60 days HHS + media for 500+ | Individuals, HHS, media (if 500+ in state) |
| GDPR | Personal data breach, risk to individuals | 72 hours to SA; "without undue delay" to individuals if high risk | Supervisory Authority, affected individuals |
| CCPA / CPRA | Unauthorized access to nonencrypted/nonredacted PI | "Expedient time" / "without unreasonable delay" | Affected consumers; AG if 500+ Californians |
| State breach laws | Varies by state | Ranges 30–90 days | Residents, AGs, credit bureaus |
| PCI DSS | Card data compromise | Immediately | Card brands, acquiring bank |

Legal counsel must be notified immediately upon discovery of any incident involving personal data.

**14. Third-Party & Vendor Management**
- Security assessment required prior to vendor access to Confidential/Restricted data
- Mandatory contractual provisions: DPA / BAA / data processing addendum as applicable
- Vendors must comply with this policy or demonstrate equivalent controls
- Right-to-audit clause required for Restricted data vendors
- Vendor access revoked immediately upon contract termination

**15. Regulatory Framework Compliance**

| Framework | Applicability | Key Requirements Incorporated |
|-----------|--------------|-------------------------------|
| HIPAA Security Rule (45 C.F.R. §§ 164.302–318) | Healthcare / PHI | Admin, physical, technical safeguards; BAAs; breach notification |
| GLBA Safeguards Rule (16 C.F.R. § 314) | Financial institutions | Risk assessment; safeguards program; service provider oversight |
| FERPA (34 C.F.R. § 99) | Educational institutions | Student record protection; disclosure restrictions |
| GDPR | EU personal data processing | Lawful basis; data subject rights; DPIAs; SCCs for transfers |
| CCPA / CPRA | CA resident personal information | Consumer rights; opt-out; privacy notice |
| PCI DSS v4.0 | Payment card data | Detailed requirements in separate PCI compliance procedures |
| NIST CSF 2.0 | Voluntary framework / contractual | Identify, Protect, Detect, Respond, Recover, Govern |
| ISO 27001 | Voluntary / contractual | ISMS; Annex A controls |

**16. Training & Awareness**
- **All personnel:** at hire and annually; phishing simulation at least semi-annually
- **High-risk roles** (sysadmins, developers, finance, HR): role-specific training annually
- **Topics:** policy requirements, phishing/social engineering, incident reporting, data classification, secure remote work
- Completion tracked; non-completion escalated to manager; records retained 3 years

**17. Compliance Monitoring & Audit**
- Annual security risk assessment
- Vulnerability assessments: quarterly; penetration testing: annually (or post-significant change)
- Access reviews: semi-annual for Confidential; quarterly for Restricted
- Security audit: internal or third-party annually; findings remediated per risk-based SLAs (Critical: 30 days; High: 60 days; Medium: 90 days)
- Metrics reported to executive leadership quarterly

**18. Enforcement & Disciplinary Action**
Violations subject to progressive discipline up to and including:
- Retraining / written warning (inadvertent/minor)
- Suspension / termination of employment or contract
- Civil liability for damages
- Criminal referral (intentional misconduct / illegal activity)

Factors considered: intent, severity of harm, prior violations, self-reporting.

**19. Policy Administration**
- **Review cycle:** annually or upon: major incident, regulatory change, material org change, significant technology change
- **Approval authority:** [CEO / Board] on recommendation of CISO and General Counsel
- **Communication:** published to intranet; employees must acknowledge receipt in writing; records retained
- **Governing law:** [Jurisdiction]; disputes resolved in [designated forum]
- **Employment disclaimer:** this policy does not create a contract of employment or alter at-will status

---

### Signature Block
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Executive Officer | | | |
| Chief Information Security Officer | | | |
| General Counsel | | | |

### Employee Acknowledgment Form
*I acknowledge receipt of, have read, and agree to comply with the Information Security Policy (Version [#], effective [Date]).*

Name: _____________ Title: _____________ Date: _____________ Signature: _____________

---

## Guidelines

- **Jurisdiction-specific appendices:** if org operates in multiple states/countries with conflicting requirements, apply the most stringent standard or add jurisdiction-specific schedules
- **Encryption standards:** treat AES-256 / TLS 1.2+ as floor; note they are subject to revision per NIST guidance
- **GDPR DPO:** required if org is public authority, conducts large-scale systematic monitoring, or processes special category data at scale — confirm applicability before drafting [VERIFY org facts]
- **HIPAA BAAs:** policy cross-references but does not replace BAA; list BAA-required vendors in separate register
- **PCI DSS:** policy references PCI; detailed technical controls maintained in separate PCI compliance documentation to allow updates without policy re-approval
- **At-will disclaimer:** verify enforceability of disclaimer language under applicable state law before finalizing
- **Collective bargaining:** if workforce is unionized, confirm policy does not require bargaining before implementation
- **Do not fabricate citations:** use `[VERIFY]` for any statutory or regulatory citation not confirmed against primary source
