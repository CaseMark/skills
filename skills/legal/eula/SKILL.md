---
name: eula
description: Drafts comprehensive End-User License Agreements (EULAs) for software licensors across desktop, mobile, SaaS, and cloud deployment models. Enforces click-wrap formation requirements, IP ownership preservation, layered liability limitations, GDPR/CCPA/COPPA compliance triggers, export control representations, and jurisdiction-calibrated enforceability. Use when drafting software license agreements, app store terms, SaaS subscription agreements, or trial/freemium license terms for digital products.
tags:
  - agreement
  - drafting
  - transactional
---

# End-User License Agreement (EULA)

Drafts an enforceable EULA that protects the licensor's IP, limits liability, and satisfies consumer protection standards across key jurisdictions.

## Prerequisites

1. **Software description** — product name, version, deployment model (desktop / mobile / SaaS / cloud / embedded firmware)
2. **License model** — perpetual one-time fee, annual subscription, monthly subscription, usage-based, freemium, or evaluation/trial
3. **User population** — B2C consumers, B2B enterprise, or mixed; any users under 13 (COPPA trigger)
4. **Distribution geography** — US-only, EU, global (determines GDPR, CCPA, and other mandatory law applicability)
5. **Data collected** — categories of personal data; any PHI (HIPAA), financial data (GLBA), student data (FERPA), or payment data (PCI-DSS)
6. **Third-party components** — proprietary licensed components or open-source (identify copyleft vs. permissive licenses)
7. **App store distribution** — Apple App Store, Google Play, or direct (affects payment, refund, and content provisions)
8. **Risk posture** — arbitration/class-action waiver desired? IP indemnification to users? Benchmark publication restrictions?

## Output Structure

### 1. Header & Acceptance Mechanism

- Title: "END-USER LICENSE AGREEMENT" prominently displayed
- Acceptance block specifying the triggering act (install / account creation / first use)
- Click-wrap: full text in scrollable window; accept button activates only after scroll opportunity (*ProCD v. Zeidenberg*; avoid passive browse-wrap per *Specht v. Netscape*)
- Mobile: present in app-store listing + first launch; must not contradict App Store/Play Store terms
- Version date + amendment notice procedure (30-day advance notice for material changes; affirmative re-acceptance for paid tier changes that reduce rights)

### 2. Definitions

| Term | Define As |
|---|---|
| Software | Exact product name, version, included modules |
| Updates | Bug fixes / security patches (included in license) |
| Upgrades | Major versions with new functionality (may require separate fee) |
| Authorized Users | Named users / concurrent users / site license scope |
| Documentation | Manuals, API docs, specs |
| Confidential Information | Source code, algorithms, benchmarks, designated confidential materials |

### 3. License Grant

- **Scope**: non-exclusive, non-transferable, revocable (for breach), [perpetual / subscription-term]
- **Permitted installations**: specify device count or concurrent user cap
- **Permitted use**: internal business purposes / personal use; in accordance with Documentation
- **Backup copies**: one archival copy; all proprietary notices intact
- **SaaS framing**: grant as access right to hosted environment, not installation right
- **Trial licenses**: designate evaluation-only, non-production, time-limited (specify end date); auto-terminate at expiry

### 4. Restrictions

| Category | Prohibited Conduct |
|---|---|
| Reverse engineering | Decompile, disassemble, derive source code — except to minimum extent required by law for interoperability (EU Directive 2009/24/EC) |
| Derivative works | Modify, translate, adapt, or create works based on Software |
| Distribution | Sublicense, rent, lease, lend, transfer, service-bureau use, hosted offering to third parties |
| Circumvention | Bypass license enforcement, DRM, or security features (17 U.S.C. § 1201 [VERIFY]) |
| Notices | Remove or alter copyright, trademark, or proprietary legends |
| Competitive use | Benchmark for competitive analysis or replicate features in competing product; publish benchmark results without consent |
| Safety-critical | Use in aircraft nav, nuclear, life support, weapons, or other high-risk applications |
| Export | Export/re-export in violation of EAR, ITAR, or OFAC sanctions |
| Illegal use | Violation of applicable law, third-party IP, or privacy rights |

### 5. Intellectual Property Ownership

- Licensor retains all right, title, and interest — copyright, patents, trademarks, trade secrets, and all other IP rights
- Agreement is a **license, not a sale**; first-sale doctrine does not apply
- **User data**: user retains ownership; licensor receives limited license to process solely to provide the service, support, and comply with law
- **Aggregated/anonymized data**: licensor owns insights and analytics derived from de-identified data
- **Feedback**: user assigns all rights in suggestions/enhancement requests to licensor; licensor may use without obligation or compensation; moral rights waived to extent permitted by law
- **Third-party components**: designated as intended third-party beneficiaries for IP provisions; open-source notices provided separately; confirm no GPL copyleft contamination of proprietary code
- **Trademarks**: no right granted to use licensor marks except to identify the Software; all goodwill inures to licensor

### 6. Payment & Renewals

- State fees in specific currency amounts (not by reference to pricing page)
- Specify payment timing, accepted methods, and auto-charge authorization for subscriptions
- **Auto-renewal**: disclose clearly and conspicuously pre-purchase per California Automatic Renewal Law (Cal. Bus. & Prof. Code § 17600 et seq. [VERIFY]) and similar state laws; provide easy cancellation; send advance renewal reminder
- **Non-payment**: notice + 5–10 day cure period → suspension; 10–15 day cure period → termination
- **Refund policy**: state non-refundable / pro-rata / trial-period refund terms explicitly; app-store refunds governed by platform policy
- **Taxes**: fees exclusive of taxes; user bears sales/use/VAT; user must provide valid exemption certificate; address EU VAT reverse charge for B2B

### 7. Term & Termination

- **Licensor termination for cause**: immediate upon material breach (IP violation, non-payment, export violation, insolvency)
- **Licensor termination without cause**: free licenses — 30 days notice; paid perpetual — generally not permitted absent statutory right
- **User termination**: cancel subscription per stated procedure; cease use and destroy all copies
- **Post-termination obligations**:
  - Immediate cessation of use; uninstall from all devices
  - Destroy all copies (including backup, cached, temporary)
  - Written destruction certification upon request
  - SaaS: 30-day data export window, then licensor deletes all user data
  - Accrued fees survive termination
- **Survival**: IP ownership, restrictions, confidentiality (3–5 years or indefinitely for trade secrets), warranty disclaimers, liability limitations, indemnification, governing law, dispute resolution

### 8. Warranty Disclaimer

> **PRESENT IN ALL-CAPS OR BOLD TO SATISFY CONSPICUOUSNESS REQUIREMENT**

- Limited warranty (if offered): Software substantially conforms to Documentation for [30/60/90] days from delivery; exclusions for user-modified software, misuse, unauthorized combinations
- Exclusive remedy for warranty breach: patch → replacement → pro-rata refund + termination
- **Disclaimer**: EXCEPT AS EXPRESSLY SET FORTH ABOVE, SOFTWARE PROVIDED "AS IS" AND "AS AVAILABLE." LICENSOR DISCLAIMS ALL WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE, INCLUDING IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT, TITLE, QUIET ENJOYMENT, AND ACCURACY. LICENSOR DOES NOT WARRANT UNINTERRUPTED OR ERROR-FREE OPERATION, FREEDOM FROM VIRUSES, OR THAT SOFTWARE MEETS USER'S REQUIREMENTS.
- Savings clause for jurisdictions prohibiting warranty exclusions (implied warranties limited to shortest period permitted by law)
- Magnuson-Moss Warranty Act compliance for consumer products [VERIFY applicability]

### 9. Limitation of Liability

> **PRESENT IN ALL-CAPS OR BOLD**

- **Consequential damages exclusion**: IN NO EVENT SHALL LICENSOR BE LIABLE FOR INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, EXEMPLARY, OR PUNITIVE DAMAGES, INCLUDING LOST PROFITS, LOST DATA, BUSINESS INTERRUPTION, OR LOSS OF GOODWILL, REGARDLESS OF CAUSE OF ACTION OR WHETHER ADVISED OF POSSIBILITY OF SUCH DAMAGES.
- **Aggregate cap**: total liability shall not exceed fees paid in the 12 months preceding the claim; for free software, cap at $[50–100] or maximum extent permitted by law
- Cap applies collectively to all claims; does not reset per claim
- **Carve-outs** (narrow; only where legally required): gross negligence / willful misconduct; death or personal injury from negligence; fraud; mandatory statutory rights
- **Temporal limit**: claims must be brought within 1 year of accrual
- Savings clause for jurisdictions limiting damage exclusions

### 10. Indemnification

**Licensor → User (IP infringement, if offered)**:
- Defend/indemnify against third-party claims that unmodified Software infringes registered patents, copyrights, or trademarks in specified territory
- Conditions: prompt notice (≤10 days); licensor controls defense/settlement; user cooperates
- Exclusions: user-modified Software; unauthorized combinations; non-current version where current version would avoid infringement; use outside agreement scope
- Remedies (in order): procure license; modify to non-infringe; replace; refund pro-rata + terminate — constitutes exclusive remedy

**User → Licensor**:
- Defend/indemnify against claims arising from: user's breach of agreement; violation of law or third-party rights; user content/data; user negligence or willful misconduct
- Not subject to aggregate liability cap

### 11. Governing Law & Disputes

- Governing law: [State] internal law, excluding conflict-of-law principles; exclude CISG
- Exclusive jurisdiction: [County, State] state and federal courts; parties waive inconvenient forum objection
- **Arbitration** (if included): binding arbitration under AAA Commercial Rules; [city]; [1 arbitrator <$100K / 3 arbitrators ≥$100K]; award final and enforceable as judgment; licensor pays costs for consumer claims
- **Class action waiver**: individual capacity only; waive class, collective, or representative proceedings [enforceability limited in CA and certain consumer contexts — confirm]
- **Carve-out**: either party may seek equitable/injunctive relief in court for IP or confidentiality violations
- **Consumer savings clause**: if choice-of-law/forum unenforceable as to a user, that user's dispute governed by their jurisdiction's law; does not affect other users

### 12. Data Protection & Privacy

**Trigger checklist — add provisions for each applicable regime:**

| Regime | Trigger | Key Obligations |
|---|---|---|
| GDPR | EU/EEA users | Lawful basis, data subject rights, 72-hr breach notice, SCCs for transfers, DPO if required |
| CCPA/CPRA | CA users | Categories disclosure, opt-out of sale/sharing, deletion/correction rights, global privacy control |
| COPPA | Users under 13 or directed-to-children | Verifiable parental consent before collection |
| HIPAA | PHI processed for covered entities | BAA required; Privacy & Security Rule compliance |
| GLBA | Financial data | Safeguards Rule compliance |
| FERPA | Student education records | Institutional consent; no unauthorized disclosure |

- Disclose: data collected, purpose, retention, third-party sharing, security measures
- Security disclaimer: reasonable measures implemented; no guarantee of absolute security; user responsible for credential security
- If software not designed for sensitive data: explicit prohibition + licensor disclaimer of liability for user violations

### 13. Export Controls

- Software subject to EAR (15 C.F.R. Parts 730–774 [VERIFY]); ITAR if defense application
- User represents: not located in / national of embargoed country (Cuba, Iran, North Korea, Syria, Crimea/Donetsk/Luhansk regions — verify current OFAC/BIS lists)
- User represents: not on SDN List, Denied Persons List, Entity List, or equivalent
- User must not export, re-export, or transfer without required licenses
- Violation = material breach → immediate termination; user indemnifies licensor for violations

### 14. General Provisions

| Provision | Key Points |
|---|---|
| Entire Agreement | Supersedes all prior representations; no reliance on extra-contractual statements |
| Amendment | Licensor may update by posting + 30-day notice; material changes to paid licenses require affirmative re-acceptance |
| Severability | Invalid provision reformed to minimum extent; invalidity in one jurisdiction doesn't affect others |
| Waiver | Must be written and signed; no implied waiver from non-enforcement |
| Assignment | User may not assign without consent; assignment void if attempted; licensor may assign freely including in M&A |
| Force Majeure | Licensor not liable for acts of God, war, pandemic, infrastructure failure, government action; termination right if event exceeds 60–90 days |
| No Partnership | Independent contractors; no agency, employment, JV, or franchise |
| Third-Party Beneficiaries | None except designated third-party component licensors for IP provisions |
| Notices | Email (with confirmation) or certified mail to addresses specified; posting in software for general user notices |
| Headings | For convenience only; not interpretive |
| Counterparts | Electronic signatures valid |

## Guidelines

- **Conspicuousness**: warranty disclaimers and liability caps must be in ALL CAPS or bold — do not bury in body text
- **Click-wrap over browse-wrap**: require affirmative acceptance action; do not use pre-checked boxes
- **EU consumer contracts**: Unfair Contract Terms Directive prohibits significant imbalance provisions; mandatory consumer law of user's habitual residence applies (Rome I Regulation) — disclaim only what is permissible
- **Class action waiver**: consult on enforceability in consumer context before including; may be unenforceable in CA under certain circumstances
- **Open-source audit**: confirm no GPL/AGPL copyleft components that could require making proprietary code available
- **App store overlay**: Apple/Google impose mandatory payment, refund, and content terms — EULA must complement, not contradict
- **Do not include**: specific damages amounts for hypothetical scenarios; representations about unlicensed third-party products; absolute security guarantees
