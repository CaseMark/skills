---
name: itar-technology-control-plan
description: >-
  Drafts an ITAR Technology Control Plan (TCP) memo/plan for U.S. export
  control compliance, covering USML scoping, technical data controls, U.S.
  person screening, deemed export safeguards, cybersecurity, training, audits,
  and incident response suitable for DDTC-facing or internal implementation.
  Use when creating or updating an ITAR TCP, export control program, or
  compliance plan; trigger keywords: ITAR, TCP, DDTC, USML, deemed export,
  technical data, defense article.
tags:
  - drafting
  - memo
  - regulatory
  - research
---

# ITAR Technology Control Plan

Produces a defensible, organization-specific ITAR TCP that can be implemented and audited.

## Prerequisites

1. **Org profile** — legal entity names, DDTC registration status, empowered official identity, compliance contacts.
2. **Programs & scope** — contracts/programs, USML categories, items/technical data in scope, facility list.
3. **People & access** — roster of personnel, foreign nationals, visitor workflows, subcontractors/vendors.
4. **Systems & storage** — IT architecture, data repositories, collaboration tools, physical storage locations.
5. **Authorizations** — licenses/agreements (DSP-5/DSP-73/TAA/MLA), CJ determinations, prior disclosures.
6. **Existing policies** — security, HR screening, IT, visitor control, incident response, records retention.

## Output Structure / Process

**Section Outline (required content):**

| Section | Required Content |
|---|---|
| 1. Purpose & Authority | Binding TCP purpose, applicability, key regulatory authority (ITAR 22 CFR Parts 120-130) [VERIFY]. |
| 2. Definitions | Defense article, technical data, export, U.S. person, deemed export with citations [VERIFY]. |
| 3. Scope | Programs/contracts, USML categories (22 CFR 121.1) [VERIFY], facilities, remote work boundaries. |
| 4. Roles & Governance | Empowered official duties, compliance officer, IT/security, HR, program owners. |
| 5. Classification & Inventory | USML mapping, CJ workflow (22 CFR 120.4) [VERIFY], inventory/marking/version control. |
| 6. Access Controls | U.S. person verification, badge logic, visitor escorts, need-to-know. |
| 7. IT & Cybersecurity | Segmentation, MFA, encryption, logging, device/media restrictions. |
| 8. Handling & Transmission | Storage rules, transfer mechanisms, travel, remote access constraints. |
| 9. Training | Initial/annual training, role-based modules, records of completion. |
| 10. Audits & Monitoring | Annual audits, trigger-based reviews, corrective actions. |
| 11. Incident Response | Reportable events, containment, investigation, disclosure workflow (22 CFR 127.12) [VERIFY]. |
| 12. Records & Retention | Five-year retention (22 CFR 122.5) [VERIFY], record types, custody. |
| 13. Revision Control | Versioning, approvals, distribution, acknowledgment. |
| Appendices | Forms, checklists, logs, access roster, facility maps. |

**Role Responsibilities Matrix (fill-in):**

| Role | Key TCP Duties |
|---|---|
| Empowered Official | Approves TCP, oversees disclosures and licensing. |
| Export Compliance Officer | Maintains TCP, coordinates audits/training, classification oversight. |
| IT/Security | Implements segmentation, logging, encryption controls. |
| HR | U.S. person verification workflow, onboarding/offboarding. |
| Program Manager | Enforces scope, need-to-know access, reporting. |

**U.S. Person Verification Checklist (attach as appendix):**

- Verify status with original documents (passport, I-551, asylum/refugee/TPS evidence) [VERIFY].
- Record verifier, date, document type, expiration, and re-verification schedule.
- Deny access until verification completed and logged.

**Controlled Item/Data Inventory Schema (use table):**

| Asset ID | Type | USML Cat | Location/System | Owner | Classification Date | Marking Applied |
|---|---|---|---|---|---|---|

**Marking Legend (insert):**

`ITAR CONTROLLED — Export of this information to foreign persons is prohibited without authorization from the U.S. Department of State.`

**Access Control Rules (minimum controls):**

- Only verified U.S. persons may access controlled areas/systems.
- Visitor pre-approval, escort required, sanitize workspaces before entry.
- Deemed export prevention: cover/remove technical data, restrict conversations.

**Cybersecurity Minimums (state baseline):**

- Segmented network for ITAR data; no routing to general networks.
- MFA for all access; least-privilege enforced.
- Encryption at rest/in transit (AES-256 or equivalent) [VERIFY].
- Prohibit personal devices, removable media, and consumer cloud storage.

**Transmission Rules (state explicitly):**

- No standard email for ITAR data.
- Use approved secure transfer with recipient verification and need-to-know.
- Verify export authorization before any foreign disclosure.

**International Travel Rules:**

- Pre-approval and licensing for temporary exports (e.g., DSP-73) [VERIFY].
- No access to ITAR data abroad without specific authorization.

**Training Matrix (table):**

| Audience | Frequency | Core Topics |
|---|---|---|
| All with access | Initial + annual | ITAR basics, deemed export, TCP rules, reporting. |
| Empowered Official | Annual + updates | Licensing, disclosures, penalties. |
| IT/Security | Annual + updates | Segmentation, logging, incident response. |
| HR | Annual + updates | U.S. person screening, onboarding/offboarding. |

**Audit Plan (minimum):**

- Annual full TCP audit with sampling of access logs, training records, inventories.
- Triggered audits after org changes, new programs, incidents, or regulatory updates.
- Document findings, corrective actions, and closure dates.

**Incident Response Steps (checklist):**

1. Contain exposure and revoke access.
2. Preserve evidence and logs.
3. Identify data/items, USML category, persons involved, duration.
4. Assess authorization gap and potential export.
5. Escalate to empowered official/legal.
6. Consider voluntary disclosure timeline (22 CFR 127.12) [VERIFY].
7. Implement corrective actions and update TCP.

**Records Retention Table:**

| Record Type | Retention | Owner |
|---|---|---|
| Licenses/agreements | 5 years from expiration/export [VERIFY] | Compliance |
| CJ requests/determinations | 5 years [VERIFY] | Compliance |
| Access logs/visitor logs | 5 years [VERIFY] | Security |
| Training records | 5 years [VERIFY] | HR/Compliance |

**Signature Block (insert):**

```
Approved by: ____________________  Title: ____________________  Date: __________
Effective Date: __________  Version: ___  Supersedes: ___
```

## Guidelines

- Use exact program names, contract numbers, facilities, and system identifiers; no placeholders in final.
- Mark any public domain or EAR-controlled items explicitly and exclude them from ITAR controls (public domain 22 CFR 120.11) [VERIFY].
- If classification or jurisdiction is unclear, require interim ITAR controls pending CJ determination.
- Do not permit any foreign person access without an applicable authorization and documented approval.
- Maintain a single source of truth for inventory and access lists; reconcile quarterly.
- Escalate any ambiguity about definitions, penalties, or licensing to counsel; annotate with [VERIFY].
