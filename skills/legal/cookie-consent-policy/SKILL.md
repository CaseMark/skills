---
name: cookie-consent-policy
description: Drafts U.S./E.U. cookie-consent website policies and banner language for drafting teams. Converts a real cookie inventory and deployment model into a publication-ready policy and consent-flow copy with clear disclosures, lawful-basis mapping, granular opt-in controls, withdrawal mechanics, retention posture, and user-rights handling under GDPR/ePrivacy, CCPA/CPRA, and major U.S. state privacy laws. Use when asked for cookie policy, cookie banner, tracking notice, cookie preferences, do-not-sell, consent management, or privacy rights messaging.
tags:
  - drafting
  - memo
  - regulatory
---

# Cookie Consent Banner and Policy

Drafts a concise, enforceable cookie policy and compliant banner framework aligned to deployment facts and required jurisdictions.

## Prerequisites

1. Site inventory: all domains, subdomains, in-app endpoints.
2. Verified cookie/SDK inventory: names, hosts, providers, purpose, category, retention, data sharing paths.
3. Jurisdiction scope: EU/EEA applicability, California residents, and other state-law coverage.
4. Consent design details: banner UI behavior, consent states, default behavior, expiration/renewal, and withdrawal path.
5. Legal/operational contacts: privacy contact, DPO (if required), external processors, complaint channels.
6. Any planned updates: future cookie additions, experiments, or new ad/analytics tools.

## Output Structure / Process

1. Collect inputs and produce assumptions block
| Input | Required | Default if missing |
|---|---|---|
| Jurisdictions served | yes | US + EU |
| Cookie inventory | yes | [VERIFY] complete inventory required |
| Consent mechanism | yes | banner + preference center |
| User rights contact | yes | privacy@ [CLIENT TO SPECIFY] |
| Update cadence | yes | 6–12 months plus material-change notices |

2. Generate policy sections in order
| Section | Mandatory fields | EU/US Notes |
|---|---|---|
| Purpose & scope | organization, websites, users affected, last updated/version | include EEA processing basis and non-EU logic |
| What are cookies | definition + non-cookie identifiers + examples | mention pixels/web beacons/local storage |
| Cookie categories | strict table by category | Essential can be exempt from consent where lawful |
| How we use cookies | purpose + legal basis + processor/shared recipients | map each non-essential use to explicit consent where required |
| Your choices | accept/reject/customize flows | no bundling consent with account creation |
| Managing preferences | withdrawal and edits anytime | explain functional limits if opt-outs selected |
| Rights | GDPR, CCPA/CPRA, state-law rights | include agency contact + complaint route |
| Changes | versioning + notice method + effective date | if material changes, request renewed consent where needed |
| Contact | email/portal/address + response SLA | include U.S./EU contact as applicable |

3. Render mandatory machine-readable tables

```text
| Cookie | Type | Provider | Purpose | Legal Basis | Duration | Category | Third-Country Transfer | Retention | Opt-out/Withdrawal |
|---|---|---|---|---|---|---|---|---|
| [name] | first/third-party | [provider] | [specific] | [consent/legitimate interest/etc.] | [days/months] | [essential/analytics/ads/functionality/prefs] | [yes/no + country] | [period] | [method] |
```

4. Draft banner text block (separate from policy)
- Required labels include: Accept All, Reject Non-Essential, Cookie Settings/Customize.
- Keep banner copy within 150–200 words.
- Consent is not valid by passive scrolling or implicit behavior.
- Store consent proof: timestamp, choice state, source, policy version, user agent/IP hash (minimal needed fields).

5. Validate before final output
| Check | Pass/Fail |
|---|---|
| Essential cookies listed and justified |  |
| Consent-only categories not preselected |  |
| Granular toggles map to categories |  |
| Withdrawal equals same-effort path as consent |  |
| Retention and third-party sharing disclosed |  |
| Contact and rights pathways complete |  |
| Change log/versioning included |  |

6. Output required artifacts
- `Cookie Policy (publish-ready markdown/HTML)`
- `Cookie Inventory Table`
- `Banner Copy`
- `Preference Center FAQ`
- `Change Log Entry`
- `Open Items` (for unresolved client-specific details)

## Guidelines

- Use plain language first, legal precision second; keep enforceability in defined rights and consents.
- Do not invent cookie names, processors, retention periods, or legal claims.
- For non-essential cookies, require affirmative, granular consent under GDPR; do not treat inaction as opt-in.
- Include GDPR Art. 6(1), Art. 13, and ePrivacy Directive 2002/58/EC art. 5(3) references.
- Include CCPA/CPRA rights under Cal. Civ. Code §§ 1798.100, 1798.105, 1798.110, 1798.115 [VERIFY].
- Include Virginia, Colorado, Connecticut, Utah state-law notices as applicable; verify naming and enforcement hooks for current version [VERIFY].
- For users outside covered jurisdictions, still disclose practical retention and opt-out paths consistently.
- Insert `[CLIENT TO SPECIFY]` whenever deployment data, provider details, or response commitments are unknown.
- Never include non-compliant claims like “all users automatically consent” or “no tracking without consent for all countries.”
