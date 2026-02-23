---
name: terms-of-service
description: Drafts a U.S. online Terms of Service (Terms of Use) agreement for websites, apps, platforms, and SaaS offerings with privacy and cybersecurity compliance hooks, enforceable acceptance mechanics, liability limits, dispute resolution, and content/IP rules. Use for "terms of service", "terms of use", "TOS", "user agreement", "platform terms", "website terms", "app terms", "SaaS terms".
tags:
  - agreement
  - drafting
  - regulatory
---

# Terms of Service Agreement

Drafts a comprehensive, enforceable TOS tailored to the service model, data flows, and jurisdictional compliance needs.

## Prerequisites

1. **Service overview**: product type, core features, user types (consumer/business), age minimums, geos served
2. **Business model**: free/paid tiers, subscriptions, renewals, refunds, promotions
3. **Data & privacy**: data categories, purposes, sharing, processors, retention, security practices, privacy notice
4. **User content**: UGC types, moderation policy, takedown process, DMCA agent info (if applicable)
5. **Existing policies**: privacy policy, acceptable use, community guidelines, IP policy
6. **Dispute posture**: arbitration vs courts, venue, class action waiver stance, small claims carve-out

## Output Structure / Process

### 1) Intake Checklist

| Item | Required | Notes |
|---|---|---|
| Company legal name, address, contact email | Yes | Contracting entity |
| Service name and URL/app identifiers | Yes | Define "Service" |
| Eligibility/age | Yes | COPPA if under 13 [VERIFY] |
| Countries/states served | Yes | Trigger GDPR/CCPA/other |
| Payment terms | If paid | Auto-renew, cancellation |
| IP assets | Yes | Trademarks, content |
| UGC + moderation | If UGC | DMCA workflow |
| APIs/integrations | If any | Third-party terms |

### 2) Clause Matrix (include if applicable)

| Area | Include When | Key Points |
|---|---|---|
| Acceptance mechanism | Always | Clickwrap preferred; continued-use fallback |
| Accounts & security | Accounts exist | Credentials, MFA, responsibility |
| Acceptable use | Always | Prohibited conduct list |
| UGC license | UGC exists | Scope, duration, takedown |
| IP ownership | Always | Service IP, limited license |
| Payments | Paid tiers | Billing, taxes, refunds |
| Termination | Always | For cause/at will, effects |
| Disclaimers | Always | AS IS / AS AVAILABLE |
| Liability cap | Always | Cap, exclusions, carve-outs |
| Indemnity | B2B or UGC | IP claims, violations |
| Dispute resolution | Always | Governing law, venue/arbitration |

### 3) Drafting Sequence

1. **Definitions & acceptance** (clickwrap + versioning/effective date)
2. **Eligibility & authority** (age, entity authority)
3. **Account rules** (registration, security, accuracy)
4. **Acceptable use** (law compliance + prohibited conduct list)
5. **UGC & IP** (ownership, license, feedback)
6. **Third-party services** (links, integrations, no endorsement)
7. **Payment terms** (if applicable)
8. **Termination & suspension** (rights, effect, survival)
9. **Disclaimers & limitation of liability**
10. **Indemnification** (if applicable)
11. **Dispute resolution** (law, venue, arbitration)
12. **Boilerplate** (severability, assignment, notices)

### 4) Prohibited Conduct Checklist

- Illegal activity; fraud; misrepresentation
- Malware, phishing, or security bypass
- Unauthorized access, scraping, or rate-limit evasion
- IP infringement or circumvention of protections
- Harassment, hate, or abusive conduct
- Interference with service availability

### 5) UGC License Template (edit scope)

```
User Content License. You retain ownership of Your Content. You grant Company a worldwide, non-exclusive, royalty-free, sublicensable, transferable license to host, store, use, display, reproduce, modify for technical purposes, distribute, and create derivative works of Your Content solely to operate, improve, and promote the Service. License ends upon deletion except for content already shared or cached in ordinary operation.
```

### 6) Liability & Warranty Template (edit cap)

```
Disclaimer. THE SERVICE IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING MERCHANTABILITY, FITNESS, AND NON-INFRINGEMENT, TO THE MAXIMUM EXTENT PERMITTED BY LAW.

Limitation. TO THE MAXIMUM EXTENT PERMITTED BY LAW, COMPANY SHALL NOT BE LIABLE FOR INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES, OR LOSS OF DATA, PROFITS, OR REVENUE. TOTAL LIABILITY SHALL NOT EXCEED THE AMOUNTS PAID BY YOU TO COMPANY IN THE 12 MONTHS BEFORE THE CLAIM (OR $100 IF NONE). EXCEPTIONS: LIABILITY FOR DEATH/PERSONAL INJURY, FRAUD, OR WILLFUL MISCONDUCT WHERE PROHIBITED.
```

### 7) Dispute Resolution Options

| Option | Use When | Notes |
|---|---|---|
| Arbitration + class waiver | B2B or low-risk consumer | Include small-claims carve-out |
| Court litigation | High consumer scrutiny | Specify venue + jury waiver |
| EU consumer carve-out | Serving EU | Mandatory local rights |

### 8) Privacy & Data Hooks (reference Privacy Policy)

- Incorporation by reference to Privacy Policy
- Data processing roles (controller/processor)
- Security measures (high-level only)
- Cross-border transfers if applicable (EU SCCs [VERIFY])

### 9) Assembly Checklist (final QC)

- Definitions consistent, capitalization standardized
- Effective date + version history
- Notice method and update mechanism
- Survival clauses listed
- Hyperlinks to incorporated policies

## Guidelines

- Prefer clickwrap; avoid browsewrap unless unavoidable.
- If serving EU/UK, include GDPR-consistent rights hooks and consumer protections; avoid overbroad waiver language. [VERIFY]
- If serving California residents, include CCPA/CPRA notice hooks and no-sale/share language where relevant. [VERIFY]
- For UGC services, include DMCA agent and takedown procedure. [VERIFY]
- Avoid unconscionability risk: keep caps and waivers reasonable for consumer users.
- Do not promise security or uptime beyond actual controls/SLAs.
- Flag any regulated industry (health, finance, telecom) for additional statutory modules.
