---
name: api-license-agreement
description: >-
  Drafts a clickwrap-ready US API License Agreement for technology companies
  licensing proprietary APIs to third-party developers. Covers license grants,
  usage tiers, prohibited conduct, data rights, IP ownership, liability
  limitations, indemnification, and termination. Produces three output modes:
  full agreement (17 sections), condensed terms (3-6 pages), or developer
  quick-reference summary. Use when drafting API terms of service, developer
  agreements, API access agreements, or click-through API license terms.
  Cross-references data processing addendum, SLA, acceptable use policy,
  trademark guidelines, and privacy policy modules.
tags:
  - agreement
  - drafting
  - transactional
---

# API License Agreement (US)

Drafts a comprehensive, clickwrap-enforced API License Agreement for US technology companies licensing proprietary APIs to developers and third-party integrators.

## Prerequisites

1. **Parties** — Provider legal name, state of incorporation, entity type, notice email/address
2. **API identification** — API/product name, Documentation URL, Developer Portal URL
3. **Acceptance mechanism** — Clickwrap ("I Agree" at API key issuance) or browsewrap (footer link only)
4. **Business model** — Free, paid, or tiered; rate limits, quotas, overage handling, billing terms
5. **Permitted use scope** — Commercial use allowed? Developer may charge end users? Revenue share?
6. **Data sensitivity** — Personal data? Regulated data (HIPAA/GLBA/FERPA/COPPA)? DPA required?
7. **Governing law / dispute resolution** — Preferred state, venue, arbitration (AAA/JAMS), class-action waiver?
8. **Competition restriction** — Prohibit building a replacement for Provider's core service?
9. **Branding** — Attribution required ("Powered by")? Trademark guidelines URL?
10. **Deprecation policy** — Notice period for breaking changes; supported deprecation window

## Output Structure / Process

### Step 1 — Intake Snapshot

If user does not answer, apply defaults below and mark every default with `[DEFAULT]` in the draft.

| # | Item | Default | Placeholder if Customized |
|---|---|---|---|
| 1 | Acceptance mechanism | Clickwrap at API key issuance | [INSERT UX DETAILS] |
| 2 | Tiers / pricing | Free + paid tiers | [INSERT TIERS / RATES] |
| 3 | Commercial use | Allowed; no resale of API access | [INSERT LIMITS] |
| 4 | Data category | May include personal data; DPA optional | [SPECIFY DATA TYPES] |
| 5 | Governing law / venue | Delaware / DE courts / no arbitration | [CHANGE IF NEEDED] |
| 6 | Liability cap (paid) | Fees paid in prior 12 months | [INSERT CAP] |
| 7 | Liability cap (free) | US $100 | [INSERT CAP] |
| 8 | Breaking-change notice | 30 days | [INSERT PERIOD] |
| 9 | Competition restriction | No replacement for Provider's core service | [DEFINE CORE SERVICE] |

### Step 2 — Clause Elections Matrix

Apply **Balanced** default for any unelected topic.

| Topic | Permissive | Balanced (Default) | Protective |
|---|---|---|---|
| License scope | Any lawful use | Interoperability with Provider services only | Narrow field-of-use |
| Commercialization | Unrestricted | Allowed; no resale of API access | Requires separate commercial license |
| Competition | Allowed | No replacement product for core service | Strict non-compete |
| Rate limit breach | Soft limits / courtesy notice | Throttle → suspension → termination | Immediate suspension + overage fees |
| Termination (free) | 30-day mutual notice | Provider at-will; Developer 30-day notice | Provider immediate at-will |
| Termination (paid) | 60-day mutual notice | 30-day mutual notice | Provider at-will; refund pro rata |
| Indemnity | Limited mutual | Developer indemnifies Provider | Expanded + IP cross-indemnity |
| Liability cap (paid) | 24-month fees | 12-month fees | 6-month fees + broad exclusions |

### Step 3 — Data Map

| Data Type | Owner | License to Other Party | Key Restrictions | Post-Termination |
|---|---|---|---|---|
| Developer Data (API payloads) | Developer | Provider: process solely to deliver API | Lawful; properly consented | Delete / return within 30 days |
| Provider Data (responses, datasets) | Provider | Developer: use within Developer Application only | No scraping, caching beyond TTL, resale | Developer deletes per Documentation |
| End-User Data (PII) | End user / Developer | Per DPA and end-user consents | Privacy law compliance; obtain consents | Delete per applicable law / DPA |
| Usage Analytics (logs, metrics) | Provider | Provider: aggregate / de-identified use | De-identify where possible | Retained for security/operations |

### Step 4 — Draft the Agreement

Generate a complete agreement with these sections; apply all elections and defaults from Steps 1–3:

**Clickwrap Header** (bold/caps, before Table of Contents):
> IMPORTANT — PLEASE READ CAREFULLY. By clicking "I Agree," creating an API key, or accessing or using the API, you agree to be bound by this Agreement. If you do not agree, do not access or use the API.

**Section outline with required drafting notes:**

| § | Title | Key Drafting Notes |
|---|---|---|
| 1 | Definitions | Define: API (endpoints + SDKs + docs + credentials + updates), Documentation, Developer Application, Developer Data, Provider Data, Usage Limits, Confidential Information |
| 2 | License Grant; Reservation of Rights | Non-exclusive, non-transferable, non-sublicensable, revocable; scope per Step 2 election; Provider retains all IP |
| 3 | Accounts & Credentials | Registration; Developer responsible for credential security and all activity under credentials |
| 4 | Usage Limits; Tiers; Fees | Tier schedule by reference to [PRICING URL]; overages; auto-upgrade or suspension trigger; free-tier fee-introduction notice (30 days) |
| 5 | Acceptable Use; Prohibited Conduct | Include full prohibited conduct list below |
| 6 | API Changes; Versioning; Availability | Breaking-change notice per election; emergency exception (security/legal); no uptime guarantee unless SLA addendum attached (see @draft-service-level-agreement) |
| 7 | Support | No obligation unless separate support plan; status page at [STATUS URL] optional |
| 8 | Data, Privacy & Security | Developer data responsibilities; privacy law compliance (CCPA/CPRA, state laws, GDPR if applicable); DPA trigger clause; security baseline; 72-hour breach notification; usage analytics rights; 30-day post-termination deletion + certification |
| 9 | IP; Feedback; Branding | Provider owns API/docs/Provider Data; Developer owns Developer Application; Feedback: perpetual irrevocable royalty-free license to Provider; trademark use per Brand Guidelines at [URL]; attribution if required |
| 10 | Term & Termination | Commences on first use; termination for convenience per tier election; immediate suspension/termination for cause (breach, security risk, IP infringement, AUP violation); survival clause |
| 11 | Confidentiality | Mutual; standard exclusions (public domain, prior knowledge, independent development, rightful third-party receipt); compelled-disclosure carve-out with prior notice |
| 12 | Representations; Disclaimers | Developer: authority, legal compliance, data rights; Provider: AS IS / AS AVAILABLE in full caps; no warranty of uptime, accuracy, fitness |
| 13 | Limitation of Liability | Consequential damages excluded (both parties); cap per tier election; basis-of-the-bargain acknowledgment; caps apply even if limited remedy fails essential purpose |
| 14 | Indemnification | Developer indemnifies Provider Indemnitees for: Developer Application, Developer Data, breach, unlawful use, IP infringement; procedural mechanics: prompt notice, sole control, settlement consent required |
| 15 | Export Controls & Sanctions | Comply with BIS/OFAC/State; Developer reps: not SDN-listed, not in sanctioned territory |
| 16 | General Terms | Governing law; venue; [optional arbitration + class-action waiver]; modification mechanics (post + notice + continued use = acceptance); no assignment by Developer; severability; waiver; force majeure; notices; entire agreement; order of precedence: (1) Agreement → (2) DPA → (3) AUP → (4) Documentation; independent contractors |
| 17 | Acceptance | Repeat clickwrap/browsewrap block; entity authority representation |

### Step 5 — Prohibited Conduct Checklist (§ 5)

- [ ] No reverse engineering, decompiling, or disassembly of the API
- [ ] No circumvention of rate limits, authentication, access controls, or metering
- [ ] No interference with or disruption of API infrastructure or other users
- [ ] No transmission of malware or unauthorized load/stress testing
- [ ] No unlawful use or violation of third-party rights (privacy, IP, export controls)
- [ ] No scraping, bulk-download, or caching beyond TTL to build a competing dataset
- [ ] No resale, sublicensing, or acting as API intermediary/aggregator
- [ ] No sharing of API credentials with unauthorized parties
- [ ] No use to build a product replacing Provider's core service (if restriction elected)
- [ ] No misrepresentation of affiliation with Provider
- [ ] Incorporate AUP at [AUP URL] by reference (see @draft-acceptable-use-policy)

### Step 6 — Liability & Indemnity Matrix (§§ 13–14)

| Feature | Provider Position | Developer Obligation |
|---|---|---|
| Warranty | AS IS / AS AVAILABLE; no uptime guarantee | Acknowledge and accept risk |
| Cap (paid) | Fees paid in prior 12 months | Full indemnity for breach, unlawful use, third-party claims |
| Cap (free) | US $100 | Full indemnity for breach, unlawful use, third-party claims |
| Consequential damages | Excluded (both parties) | Excluded (both parties) |
| Indemnity triggers | N/A | Developer Application; Developer Data; breach; IP infringement; unlawful use |

### Step 7 — Clickwrap Presentation & Policy Cross-Reference Table

**Recommended checkbox text:**
> ☐ I have read and agree to the [API License Agreement](link), [Acceptable Use Policy](link), and [Privacy Policy](link).

**Browsewrap fallback** (if no checkbox): Place bold conspicuous notice directly above "Create API Key" button: **"By creating an API key or using the API, you agree to the [API License Agreement]."** Link must also appear in documentation sidebar and account settings.

| Incorporated Policy | Cross-Reference | URL |
|---|---|---|
| Documentation | — | [INSERT] |
| Acceptable Use Policy | @draft-acceptable-use-policy | [INSERT] |
| Privacy Policy | @draft-privacy-policy-us | [INSERT] |
| Data Processing Addendum | @draft-data-processing-agreement | [INSERT] |
| Brand Guidelines | @draft-trademark-usage-guidelines | [INSERT] |
| SLA Addendum (optional) | @draft-service-level-agreement | [INSERT] |

### Output Modes

| Mode | Description |
|---|---|
| **Mode 1 — Full Agreement** (default) | Complete 17-section clickwrap-ready agreement with all deliverables; suitable for developer portal |
| **Mode 2 — Condensed Terms** | 3–6 page short-form retaining: acceptance, license grant, prohibited conduct, data/privacy, IP, termination, disclaimers, liability cap, indemnity, governing law |
| **Mode 3 — Quick Reference** | One-page developer-facing table: permitted use, tier overview, key restrictions, data rules, termination triggers, liability cap, support model, policy links |

## Guidelines

- **Clickwrap enforceability**: Conspicuous presentation (bold/caps header) + affirmative act (checkbox/button) + clear link to full terms + timestamp/IP logging recommended
- **Browsewrap risk**: Courts scrutinize browsewrap strictly; if only footer link is available, add enhanced conspicuous notice adjacent to every "Get Started" / "Create Key" CTA
- **DPA trigger**: Always include a conditional DPA trigger clause even if DPA is not immediately executed; activates automatically if personal data is processed
- **Regulated data**: If HIPAA, GLBA, FERPA, COPPA, or biometric data is in scope, flag for separate compliance review before finalizing; insert [VERIFY — regulated data addendum needed]
- **Export controls**: Do not remove § 15; APIs with encryption or dual-use functionality may require EAR classification review
- **Modification mechanics**: "Posting + continued use = acceptance" is generally enforceable for material changes with advance notice; 15-day minimum notice recommended
- **Change log**: Maintain public version archive at a stable URL; note effective date and summary of material changes for each revision
- **Cross-references**: @draft-data-processing-agreement · @draft-service-level-agreement · @draft-acceptable-use-policy · @draft-trademark-usage-guidelines · @draft-privacy-policy-us · @negotiate-enterprise-api-addendum
