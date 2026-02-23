---
name: enterprise-api-addendum
description: Negotiates bespoke enterprise API addenda that override standard click-wrap API terms for high-value partners. Covers document architecture and precedence, indemnification and liability cap redlining, custom SLA and service-credit design, exclusivity and competitive restrictions, API versioning and deprecation governance, data rights, and internal alignment. Use when negotiating enterprise API agreements, API addenda, click-wrap overrides, API SLAs, or API licensing terms.
tags:
  - agreement
  - drafting
  - transactional
---

# Enterprise API Addendum Negotiation

Negotiates a bilateral API addendum that overrides standard click-wrap terms for enterprise partners, delivering negotiation tables, clause snippets, and decision trees.

## Prerequisites

1. **Standard click-wrap API Terms of Service** already in production
2. **Governing contract(s)** — order form/SOW, any existing MSA
3. **API specification** — endpoints, rate limits, versioning policy, mission-criticality assessment
4. **Data classification** — personal data, PCI/PHI, export-controlled, authentication/SSO, telemetry
5. **Commercial parameters** — fees, term, liability posture, exclusivity asks, MFN requests
6. **Partner requirements** — SLA metrics, indemnity expectations, audit rights, insurance demands

## Default Assumptions

Override any of these; otherwise they apply throughout.

| Parameter | Default |
|---|---|
| Governing law / venue | Delaware / Delaware courts |
| Data sensitivity | No PCI/PHI; limited personal data; no special category |
| SLA | 99.9% monthly uptime; 24×5 support; scheduled maintenance excluded |
| Liability cap | 12 months' fees; exclude indirect; super-cap 2× for confidentiality/privacy |
| Exclusivity | None; allow "preferred partner" marketing only |
| Breaking changes | 90 days' notice; security patches exempt |

## Output Structure

### Phase 1: Deal Architecture & Delta Analysis

**1A. Delta Analysis Table**

Map gaps between click-wrap and enterprise requirements:

| Clause | Click-Wrap Default | Enterprise Requirement | Strategy |
|---|---|---|---|
| SLA / Uptime | "As-Is" / No guarantee | 99.9–99.99% with credits | Credits; exclude beta + scheduled maintenance |
| Indemnity | None or limited | Broad IP and data breach | Cap at ACV multiple; standard exclusions; control of defense |
| Liability Cap | $100 or 1 month's fees | 12–24 months' fees; super-caps | Tiered: general cap + super-cap for data/IP |
| Breaking Changes | At will; no notice | 90–180 days' notice; sunset periods | Define "Breaking Change" narrowly; exempt security patches |
| Data Rights | Broad license to aggregate | Limited to service delivery; strict anonymization | Grant aggregate rights with precise "Anonymized" definition |
| Termination | Provider may terminate at will | For-cause only; wind-down | For-cause with cure period; add transition assistance |
| Audit Rights | None | Annual security/compliance audit | Once/year at Customer's expense; more if breach occurs |

**1B. Architecture Checklist**

- [ ] Click-wrap incorporated by reference or restated/attached?
- [ ] Addendum applies to one entity or also affiliates/subsidiaries?
- [ ] Covers production only or also sandbox/beta?
- [ ] Multiple documents (Order Form, DPA, Security Exhibit, SLA Schedule)?
- [ ] MFN precedence clause accidentally elevates click-wrap?
- [ ] Amendment-by-posting locked for this partner?

**1C. Precedence Matrix**

| Document | Precedence | Conflict Handling |
|---|---|---|
| Enterprise API Addendum | 1 (highest) | Controls over click-wrap |
| Order Form / SOW | 2 | Controls for commercial items |
| DPA | 2–3 | Higher for privacy conflicts |
| SLA Schedule | 3 | Controls for SLA topics |
| Security Exhibit | 3–4 | Must align with SLA and incident clause |
| Click-wrap API Terms | Lowest | Incorporated subject to addendum |

**Incorporation + Lock-In Clause:**

> "The Online API Terms are incorporated by reference solely as modified by this Addendum. In the event of conflict, this Addendum controls. For the Partner only, the Online API Terms will not be amended in a manner that materially diminishes Partner's rights or increases Partner's obligations without Partner's written consent."

---

### Phase 2: Indemnification & Liability

**Negotiation Table**

| Topic | Typical Customer Ask | Vendor Default | Fallback |
|---|---|---|---|
| IP indemnity | Broad indemnity | Unmodified API infringes U.S. IP only | Exclude foreign patents; cap to fees; modify/replace/refund remedy |
| Data breach indemnity | All losses/fines | Only vendor's failure per Security Exhibit | Super-cap 2× fees; limit to direct damages |
| Customer misuse | Silent | Customer indemnifies for unlawful use/apps/content | Narrow to third-party claims from Customer's apps |
| Cap amount | 2–5× fees or uncapped | 12 months' fees paid/payable | 24 months' fees; fixed dollar amount |
| Indemnity vs. cap | Outside cap | Inside cap (except possibly IP) | IP outside general cap with separate cap |
| Excluded damages | Some consequential | Exclude all indirect/consequential/punitive | Direct damages only; limited confidentiality carve-out |
| Confidentiality carve-out | Uncapped | Super-cap 2× | Separate fixed cap or cap to insurance limits |

**IP Indemnity Clause (balanced vendor form):**

> "Provider will defend Partner against any third-party claim alleging that the unmodified API, when used in accordance with this Agreement and Documentation, infringes such third party's U.S. copyright, U.S. trade secret, or U.S. patent, and will pay damages finally awarded or agreed in settlement, provided Partner (a) promptly notifies Provider, (b) allows Provider sole control of defense and settlement, and (c) reasonably cooperates."

**IP Exclusions:**

> "Provider has no obligation to the extent a claim arises from: (i) Partner Data or Partner Applications; (ii) modifications not made by Provider; (iii) combination with items not provided by Provider; (iv) use outside scope or contrary to Documentation; (v) failure to use updates made available to avoid infringement."

**Limitation of Liability (core):**

> "Except for Excluded Claims, each party's aggregate liability will not exceed the fees paid or payable under the applicable Order Form in the 12 months preceding the event giving rise to the claim ('General Cap'). In no event will either party be liable for indirect, incidental, special, consequential, exemplary, or punitive damages."

**Excluded Claims / Super-Cap:**

> "'Excluded Claims' means: (a) Customer's payment obligations; (b) Customer's indemnification obligations; (c) either party's breach of confidentiality (capped at 2× General Cap); (d) Provider's IP indemnification (capped at 2× General Cap); (e) gross negligence or willful misconduct."

---

### Phase 3: SLA / Support / Credits

**SLA Schedule Template**

| Metric | Value |
|---|---|
| Monthly Uptime % | 99.9% |
| Downtime definition | API not responding HTTP 2xx for ≥5 consecutive minutes |
| Measurement | Provider monitoring + logs |

**Exclusions:** Scheduled maintenance (72h notice), emergency maintenance, force majeure, Partner's systems/network, rate-limit throttling from exceeding limits, beta features.

**Service Credit Table (sole and exclusive remedy):**

| Monthly Uptime % | Credit (% of Monthly Fees) |
|---|---|
| < 99.9% and ≥ 99.5% | 5% |
| < 99.5% and ≥ 99.0% | 10% |
| < 99.0% | 20% |

- Request within 30 days; max aggregate 20% of monthly fees; apply to future invoices (fallback: cash refund if no future invoices).

**Support Defaults:**

| Item | Default | Premium Option |
|---|---|---|
| Support hours | 24×5 (Mon–Fri) | 24×7 at additional cost |
| P1 response | 1 hour | 30 minutes |
| P2 response | 4 hours | Negotiable |
| Dedicated TAM | Not included | Top-tier deals |

> **Critical:** Distinguish response times from resolution times. Resolution commitments should be "commercially reasonable efforts" only — never SLA credits for resolution.

**Chronic Failure:** Termination right only if uptime < 99.0% for 2 consecutive months after documented cure plan.

**Negotiation Map:**
- *Tradable:* Faster response times, 24×7, dedicated TAM, higher uptime tier, custom dashboards
- *Protect:* Credits as sole remedy, exclusions, Provider-controlled measurement, aggregate credit cap

---

### Phase 4: Exclusivity & Competitive Restrictions

**Decision Tree Checklist:**

- [ ] What consideration supports exclusivity? (minimum spend, committed volume, co-development)
- [ ] Scope: which endpoints, use cases, verticals, territories?
- [ ] Term: short duration, renewable on performance milestones?
- [ ] Exceptions: existing customers, strategic accounts, affiliates, acquisitions?
- [ ] Remedy for breach: termination of exclusivity only (not broad damages)?
- [ ] Antitrust review needed? (especially EU/UK competition law)

**Graduated Clause Menu:**

| Option | Risk Level | Use When |
|---|---|---|
| No exclusivity (default) | None | Standard deals |
| Preferred partner marketing | Low | Customer wants recognition without restriction |
| Limited vertical exclusivity | High | Significant committed spend + milestones; bound by scope/term/territory |
| MFN | Medium-High | Use sparingly; limit to pricing only, similarly situated customers, with sunset |

**MFN Guardrails:** Limit to similarly situated customers + pricing only; exclude promotional/pilot/strategic deals; prospective credit (not retroactive repricing); sunset after 12 months.

---

### Phase 5: Technical Governance & Data Rights

**Breaking Change Definition:**

> "'Breaking Change' means any modification to the API that requires Partner to modify its code to maintain existing functionality, including removal of endpoints, changes to request/response schemas, or modification of authentication methods."

**Notice & Sunset Clause:**

> "Provider will give Partner at least [90] days' prior written notice before implementing a Breaking Change. Provider will maintain the prior version for at least [180] days following notice. This Section does not apply to changes required to address security vulnerabilities, comply with law, or prevent imminent harm."

- 90 days is vendor-friendly floor; partners often request 180 days
- Consider LTS versions for mission-critical integrations at premium pricing

**Audit Rights:** Once per calendar year at Partner's expense with 30 days' notice; scope limited to security + DPA compliance; additional audits if breach occurs; may satisfy via current SOC 2 Type II or ISO 27001.

**Data Rights:**
- Partner retains all rights in Partner Data; Provider retains all rights in API and derivatives
- Provider uses Partner Data solely to provide API Services
- Aggregate/anonymized use requires precise "Anonymized Data" definition (irreversibly de-identified; cannot be re-identified)
- If personal data in scope, incorporate DPA

---

### Phase 6: Consolidation & Internal Alignment

**Term Sheet Template**

| Category | Agreed/Proposed | Fallback | Owner |
|---|---|---|---|
| Scope of API + endpoints | | | Product |
| Fees / usage limits | | | Sales / Finance |
| SLA (uptime / support / credits) | | | SRE / Support |
| Indemnity (IP) | | | Legal |
| Indemnity (data breach) | | | Legal / Security |
| Liability cap & carve-outs | | | Legal / Finance |
| Exclusivity / MFN | | | BizDev |
| Breaking changes / versioning | | | Product / Engineering |
| Term / termination | | | Legal / Sales |

**Internal Readiness Checklist**

- [ ] SRE confirms monitoring supports SLA measurement; maintenance windows defined
- [ ] Support confirms hours, P1 definitions, escalation path, staffing achievable
- [ ] Security confirms controls and incident response match Security Exhibit
- [ ] Privacy confirms DPA necessity and cross-border transfer mechanism
- [ ] Finance confirms credit mechanism, revenue recognition impact, insurance adequacy
- [ ] Product/Engineering confirms breaking-changes notice period is feasible
- [ ] Legal confirms precedence clause prevents unilateral click-wrap changes
- [ ] Compliance confirms exclusivity reviewed for antitrust implications

## Guidelines

1. **Top 10 Red Flags to Reject or Escalate:**
   - Uncapped liability for confidentiality or privacy breaches
   - IP indemnity covering Partner's own applications or data
   - SLA termination right for any single-month miss
   - MFN covering legal terms (not just pricing)
   - Unilateral click-wrap amendment overrides negotiated terms
   - Resolution-time SLA commitments with credits attached
   - Uncapped service credits (no aggregate monthly maximum)
   - Broad exclusivity without consideration or milestones
   - Audit rights with no frequency limit or scope boundary
   - "Breaking Change" defined so broadly it covers bug fixes and security patches

2. Clarify "fees paid" vs. "fees payable" in every liability cap — the distinction significantly affects exposure
3. Always exempt security patches and legal compliance changes from breaking-change notice requirements
4. Service credits must be the sole and exclusive remedy for SLA breach; do not allow expansion into general damages
5. Regulatory fines as indemnifiable damages: enforceability varies by jurisdiction — flag for local counsel review
6. Cross-reference DPA when personal data is in scope
7. Verify all entity names, signature authority, and affiliate definitions before execution
8. This skill provides general negotiation guidance — not legal advice. Consult qualified counsel for jurisdiction-specific enforceability, regulatory obligations, and antitrust issues.
