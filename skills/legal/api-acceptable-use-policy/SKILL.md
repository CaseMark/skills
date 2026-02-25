---
name: api-acceptable-use-policy
description: >
  Drafts a standalone API Acceptable Use Policy (AUP) designed to be incorporated
  by reference into a master API license or terms-of-service agreement. Produces
  a publication-ready AUP template covering prohibited uses, AI/ML training
  restrictions, credential security requirements, rate-limit compliance,
  monitoring disclosure, graduated enforcement, and versioned change management.
  Includes a prohibited-use matrix, developer security checklist, AUP-to-license
  mapping, and versioning playbook. Use when drafting or updating an API AUP,
  separating behavioral rules from core API terms, adding enforcement and
  change-management mechanics, or when a user mentions acceptable use, prohibited
  API uses, developer security requirements, or API enforcement policy.
tags:
  - drafting
  - policy
  - transactional
---

# API Acceptable Use Policy

## Why This Skill Exists

API acceptable use policies need to be updated more frequently than master license agreements — new abuse patterns emerge, AI/ML training restrictions evolve, and security requirements tighten. Embedding these rules in the master agreement means every update requires re-acceptance or risks enforceability challenges. A standalone AUP incorporated by reference allows the behavioral and security rules to be updated on a faster cadence while the commercial and legal terms remain stable. But the separation creates its own risks: conflicting notice periods, unclear precedence, enforcement triggers that don't match the master's suspension rights, and change mechanics that inadvertently modify material terms. This skill produces a modular AUP with explicit contract-linkage mechanics and a versioning playbook.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Company and product identifiers** — legal name, API/product name(s)
2. **Authentication method** — API keys, OAuth 2.0, JWT, mTLS, or combination
3. **Access model** — public/self-service, partner-vetted, or internal-only
4. **Use model** — internal use only, or commercial redistribution via developer apps
5. **Data categories** — personal data, PHI, PCI, children's, biometric, or none
6. **Policy positions** — whether to allow: scraping, benchmarking, AI/ML training of outputs, caching (and max duration), security research/bug bounty
7. **Operational contacts** — `[SECURITY_EMAIL]`, `[SUPPORT_EMAIL]`, `[LEGAL_EMAIL]`
8. **Rate-limit documentation URL** — reference link (avoid hard-coding numbers in the AUP)

**If the user doesn't respond**, apply and clearly label these defaults:

| Parameter | Default |
|---|---|
| Governing law | U.S. (state TBD); B2B developers |
| API category | General SaaS |
| Access model | Public / self-service |
| Data scope | Personal data possible; no PHI/PCI/children's |
| AI/ML training | Prohibited unless expressly authorized in writing |
| Effective date — routine | Upon posting |
| Effective date — material adverse changes | 30 days' advance notice |
| Effective date — security/emergency | Immediate |
| Enforcement posture | Graduated; immediate suspension for severe/security violations |

---

## Step 1: AUP-to-License Mapping

| Topic | AUP | Master Agreement | Note |
|---|---|---|---|
| Incorporation by reference | No | **Yes** | Master references AUP URL |
| Prohibited use categories | **Yes** (detailed) | Optional summary | Keep detail in AUP for easy updates |
| AI/ML training restrictions | **Yes** | Optional summary | AUP updateable as AI landscape evolves |
| Data handling / security | **Yes** | Optional baseline | Coordinate with any Security Addendum or DPA |
| Rate limits and caching | **Yes** (link to docs) | No | Never hard-code numbers; reference docs URL |
| Monitoring disclosure | **Yes** (detail) | Yes (high-level) | Master discloses generally; AUP details signals/uses |
| Suspension right | **Yes** (process/triggers) | **Yes** (contractual right) | Master grants right; AUP describes triggers and process |
| Change / notice mechanics | **Yes** | **Yes** | Ensure consistent notice periods; no conflicting clauses |
| Canonical definitions | Incorporate by reference | **Yes** | Define API, Developer App, Credentials in Master |

---

## Step 2: Prohibited Use Matrix

| Category | Examples | Severity | Default Enforcement |
|---|---|---|---|
| Illegal activity | Violate laws; facilitate fraud; sanctions evasion | High | Immediate suspension / termination |
| Security abuse | Vulnerability scanning; credential stuffing; malware; reverse engineering; fuzzing | High | Immediate suspension |
| Interference / DDoS | Excessive calls; denial-of-service; bypassing rate limits via multi-key distribution | High | Throttle → suspend |
| Circumvention | Bypassing auth, paywalls, or metering; obfuscation to avoid detection | High | Suspension |
| Data misuse | Unlawful collection; re-identification; doxxing; cross-dataset identification | High | Suspension + data deletion |
| Prohibited content | CSAM; threats; non-consensual intimate imagery; hate speech | High | Immediate suspension; legal escalation |
| AI/ML training | Training/fine-tuning/distilling competing models; bulk extraction for synthetic datasets | Medium–High | Throttle → suspend |
| Scraping / bulk extraction | Large-scale automated extraction replicating core data or service | Medium–High | Throttle → suspend |
| Spam / unsolicited outreach | Automated messaging without consent | Medium–High | Throttle → suspend |
| Misrepresentation | Impersonation; false affiliation; deceptive app naming | Medium | Require changes → suspend |
| Caching violations | Retaining API data beyond permitted duration | Medium | Warning → suspend |
| Benchmarking abuse | Publishing performance benchmarks without permission | Medium | Takedown → suspend |

---

## Step 3: Developer Security Checklist

- [ ] Unique credentials per environment (dev / staging / prod) and per application
- [ ] Secrets in vault or environment variables — never hard-coded in client-side code, public repos, or mobile binaries
- [ ] Key rotation on regular schedule; revoke compromised keys immediately
- [ ] Least-privilege scopes; no shared credentials across teams or applications
- [ ] TLS 1.2+ for all API connections; request signing or mTLS if documented
- [ ] Accurate, non-misleading User-Agent string or App ID in all requests
- [ ] Audit logs sufficient to investigate misuse; provide to Company upon request
- [ ] Comply with rate limits and back-off requirements; do not distribute requests to evade limits
- [ ] Report suspected compromise to `[SECURITY_EMAIL]` promptly (within `[X]` hours)
- [ ] If Developer App serves end users: maintain a compliant privacy policy

---

## Step 4: Enforcement Framework

| Trigger type | Response | Notes |
|---|---|---|
| Minor / first-time violation | Notice + cure window | Define cure period (e.g., 10–30 days) |
| Repeated or uncured violation | Throttle → suspend | Escalate after failed cure |
| Security, illegal, or high-risk violation | Immediate suspension without prior notice | No cure required |
| Termination | Per master agreement | AUP breach = termination trigger in Master |
| Appeal | Contact `[SUPPORT_EMAIL]`; respond within commercially reasonable time | |

---

## Step 5: Versioning & Notice Playbook

| Item | Recommendation |
|---|---|
| Version label | Date-based (e.g., 2026-02-23) |
| Change log | Short bullets on developer site; version-controlled repo |
| Notice channels | Email to account admin + developer dashboard banner |
| Material change standard | Changes that materially reduce developer rights or impose new material obligations |
| Effective date — routine | Upon posting |
| Effective date — material adverse | 30 days after posting (or longer if required by law) |
| Effective date — emergency | Immediate for security or legal compliance |
| Archive | Publicly accessible prior versions at `[ARCHIVE_URL]` |

---

## Step 6: Publication-Ready AUP Template

> Replace all `[BRACKETED]` placeholders. Publish as a standalone web page with version and effective date at top.

---

**API Acceptable Use Policy**
**Effective date:** [DATE] | **Version:** [VERSION]

This AUP governs your access to and use of the APIs, developer tools, and credentials made available by **[COMPANY NAME]** ("Company"). This AUP is incorporated into and forms part of the Agreement governing your API use. Capitalized terms not defined here have the meanings in the Agreement.

**1. Scope.** This AUP applies to (a) your use of the API, (b) your applications or services that access the API ("Developer App"), and (c) all activity under your API keys, tokens, OAuth client IDs, or other access credentials ("Developer Credentials").

**2. General Responsibilities.** You are responsible for all use of the API under your Developer Credentials, your Developer App's compliance with this AUP and applicable law, and ensuring your personnel and permitted third parties comply with this AUP.

**3. Prohibited Uses.** You will not use (or allow others to use) the API, Developer Credentials, or data obtained through the API to:

1. **Violate Law or Rights.** Violate any applicable law or regulation, or infringe, misappropriate, or otherwise violate any person's or entity's rights.
2. **Compromise Security.** Probe, scan, test the vulnerability of, or compromise the security or availability of the API or related systems; introduce malware; reverse engineer or fuzz the API; or bypass authentication, authorization, or usage limits.
3. **Interfere or Abuse.** Interfere with or disrupt the API or related systems, including through denial-of-service attacks, excessive automated requests, or circumventing rate limits.
4. **Circumvent Controls.** Access the API in a manner intended to avoid fees, evade usage limits, or bypass technical measures.
5. **Misuse Data.** Collect, use, disclose, or store API data in a manner that is unlawful or violates applicable privacy or data-protection requirements, including by re-identifying de-identified data.
6. **Train Models Without Authorization.** Use API output, responses, or data to train, fine-tune, distill, or otherwise develop machine-learning or AI models, unless expressly authorized in writing by the Company.
7. **Engage in Harmful or Deceptive Conduct.** Engage in phishing, spamming, impersonation, deception, or other conduct that harms end users, third parties, or the Company.
8. **Exceed Caching Limits.** Cache or store API responses beyond the duration permitted in the developer documentation.
9. **High-Risk Activities.** Use the API where failure could lead to death, personal injury, or severe physical or environmental harm, unless expressly permitted in writing.

**4. Security Requirements.** You must: (a) protect Developer Credentials using industry-standard controls, including TLS 1.2+ in transit and secure secret storage; (b) not embed credentials in client-side code, public repositories, or mobile app binaries; (c) use least-privilege access and rotate credentials as appropriate; (d) include an accurate, non-misleading User-Agent or App ID in API requests; and (e) notify the Company at **[SECURITY_EMAIL]** promptly upon any actual or suspected credential compromise or security incident affecting the API.

**5. Rate Limits; Caching; Fair Use.** You will comply with all rate limits, quotas, and usage limits described in the developer documentation or communicated by the Company. You may cache API responses only as permitted in the documentation; unless otherwise specified, cached data must not be retained for more than **[24]** hours. The Company may throttle or suspend access to protect the API, other customers, or the Company.

**6. Monitoring; Enforcement.** The Company may monitor and analyze API usage to operate and secure the API, prevent abuse, comply with law, and enforce this AUP. If you violate this AUP, the Company may: notify you and request remediation; throttle or restrict access; suspend or disable Developer Credentials; require deletion of improperly obtained data; or terminate access per the Agreement. The Company may act immediately (including suspending without prior notice) to protect the API, users, third parties, or the Company, or to comply with law. To appeal, contact **[SUPPORT_EMAIL]**.

**7. Changes.** The Company may update this AUP from time to time. Updates are effective upon posting at **[AUP_URL]**, unless a later effective date is indicated. For changes that materially and adversely affect your obligations, the Company will provide at least **30 days'** advance notice, except where an earlier effective date is necessary for legal compliance or to address an imminent security risk. Continued use of the API after the effective date constitutes acceptance. Prior versions: **[ARCHIVE_URL]**.

**8. Contact.**
- General questions: **[LEGAL_EMAIL]**
- Security reports: **[SECURITY_EMAIL]**
- Enforcement appeals: **[SUPPORT_EMAIL]**

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial draft, ask:

1. Do the prohibited use categories and severity levels match your enforcement capabilities and intent?
2. Should AI/ML training be permitted for any use cases (e.g., non-competing academic research)?
3. Are the operational contact emails ([SECURITY_EMAIL], [SUPPORT_EMAIL], [LEGAL_EMAIL]) staffed and ready?
4. Does the notice period for material changes align with what's in your master agreement?

---

## Quality Audit

- AUP-to-License mapping complete with no conflicting provisions
- All prohibited use categories addressed with severity and enforcement action
- Developer security checklist covers credential management, TLS, and incident reporting
- Enforcement framework has graduated responses with immediate suspension for severe violations
- Versioning playbook specifies notice channels, material change standard, and archive URL
- Template AUP has all `[BRACKETED]` placeholders clearly marked
- AI/ML training restriction present and aligned with commercial intent
- Rate limits reference documentation URL — no hard-coded numbers
- Monitoring disclosure present and coordinated with master agreement
- No conflicting notice periods between AUP and master agreement

---

## Guidelines

- **Separate fast-changing rules from the Master.** Prohibited uses, security controls, rate limits, and AI/ML restrictions belong in the AUP; license grant, fees, IP, liability caps, and dispute resolution belong in the Master Agreement
- **Never hard-code rate-limit numbers.** Reference a documentation URL engineering can update independently
- **AI/ML prohibition.** Include only if you intend to detect and enforce; consider a written-permission carve-out for non-competing academic research
- **Immediate suspension.** Ensure the Master Agreement grants the contractual right; the AUP describes only operational triggers and process
- **Precedence.** Specify which document controls on conflict; avoid circular references
- **Assent mechanism.** Browsewrap (posting) is common for B2B; affirmative clickwrap may be required for material changes in certain jurisdictions. [VERIFY jurisdiction requirements with local counsel]
- **Regulated data.** If PHI, PCI, COPPA, GLBA, or FERPA data is in scope, draft a separate regulated-data annex
- **EU/UK.** GDPR and EU Digital Services Act obligations require separate drafting; coordinate with local counsel
- **Export controls.** Add export-control language if the API or data is subject to EAR, ITAR, or OFAC restrictions. [VERIFY applicability]
- **Operational readiness.** Confirm contact emails route to staffed queues and that an internal enforcement playbook exists before publishing

**Required disclaimer on every output:**

> THIS POLICY IS A DRAFTING AID AND REQUIRES REVIEW BY QUALIFIED LEGAL COUNSEL BEFORE PUBLICATION. IT DOES NOT CONSTITUTE LEGAL ADVICE.
