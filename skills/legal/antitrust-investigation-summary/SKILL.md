---
name: antitrust-investigation-summary
description: Drafts a privilege-protective, board-ready executive summary memorandum of internal antitrust investigation findings for large technology companies under US federal law. Covers investigation scope, key findings organized by antitrust theory (monopolization, vertical restraints, acquisitions, FTC Act §5), risk assessment, remediation recommendations, and DOJ/FTC regulatory exposure. Emphasizes adversarial-resilient drafting, advisory language, tech-platform issue spotting (self-preferencing, ecosystem lock-in, killer acquisitions, tying), and anti-hallucination guardrails. Use when drafting antitrust investigation summaries, board memos on competition risk, or internal compliance investigation reports.
tags:
  - analysis
  - memo
  - regulatory
  - summarization
---

# Antitrust Internal Investigation Summary

Produces a privilege-protective, board-ready executive summary memorandum synthesizing internal antitrust investigation findings for technology platform companies under US federal law.

## Prerequisites

1. **Investigation charter** — who directed it (board committee, GC, CCO), who conducted it, dates, intended audience, privilege posture
2. **Key factual record** — triggering complaint; compliance policies; implicated contracts (distribution, API terms, MFN clauses, bundling); internal comms of key custodians; product decision docs (launch memos, algorithm changes, interoperability decisions); pricing/incentive docs; regulator correspondence (CIDs, subpoenas)
3. **Interview materials** — Upjohn-warned interview summaries or structured synopses (role, topics, key assertions, corroboration)
4. **Market context** — products/services implicated, monetization model, user groups, key rivals, switching costs, network effects, market studies, prior antitrust assessments, any existing consent decrees
5. **Remediation status** — stop-gap steps taken, policy updates, product changes, contract revisions, training, monitoring
6. **Procedural posture** — anticipated litigation, ongoing M&A, parallel civil suits, preservation holds, whistleblower counsel status

If critical inputs are missing, pause and request them before drafting. State: "To provide a competent risk assessment, I require [specific items]. Shall we proceed with a structural framework, or can you provide these details now?"

## Output Structure

The memo must contain all seven sections below in order.

### 1. Privilege Header

Apply to every page:

```
ATTORNEY–CLIENT PRIVILEGED / ATTORNEY WORK PRODUCT
Prepared at the direction of counsel to provide legal advice regarding
antitrust compliance and potential exposure. Intended solely for [Company]
senior leadership and the Board of Directors. Do not forward outside
those who need to know for purposes of receiving legal advice.
```

### 2. Executive Summary

Bottom-line-up-front format. Must address:

| Element | Content |
|---|---|
| Trigger | Why the investigation was opened |
| Scope | What was reviewed and its limits |
| Principal findings | Plain-English, tied to specific conduct and products |
| Risk assessment | Severity, likelihood, time horizon |
| Recommended actions | Prioritized next steps |

Frame each finding as: **Issue → Key Facts → Legal Significance → Risk Level → Recommended Action**

Anchor the "Three Pillars of Risk":
- **Legal Liability** — strength of potential claims under applicable statutes
- **Regulatory Scrutiny** — probability/intensity of DOJ/FTC enforcement
- **Reputational Impact** — downstream effects on partners, developers, public

### 3. Investigation Scope & Methodology

State precisely: triggering event, time period, products/business units, conduct categories, document sources, custodian count/selection logic, interview count/roles, quantitative analyses performed. Identify known gaps and mitigation steps. Keep credible and sufficiently specific without creating a discovery roadmap.

### 4. Key Findings

Organize by **issue**, not by witness or chronology. Map each finding to the relevant antitrust theory:

| Theory | Statute | Key Elements |
|---|---|---|
| Monopolization | Sherman Act § 2 | Monopoly power in relevant market + willful acquisition/maintenance (distinguished from superior product/acumen). *Grinnell Corp.*, 384 U.S. 563 (1966) [VERIFY] |
| Vertical restraints | Sherman Act § 1 | Agreement + unreasonable restraint of trade (rule of reason for most platform conduct) |
| Acquisitions | Clayton Act § 7 | Effect may substantially lessen competition; heightened scrutiny for dominant platform acquisitions per 2023 Merger Guidelines [VERIFY] |
| Unfair methods | FTC Act § 5 | Broader than Sherman/Clayton; reaches platform gatekeeping conduct. *FTC v. Sperry & Hutchinson*, 405 U.S. 233 (1972) [VERIFY] |

**Tech-platform issue checklist** — address each if relevant:
- [ ] Self-preferencing (ranking, defaults, API access)
- [ ] Tying / bundling
- [ ] De facto exclusivity (commitment rebates, defaults)
- [ ] Anti-steering provisions
- [ ] Interoperability / API restrictions
- [ ] MFN / parity clauses
- [ ] Killer acquisitions of nascent competitors
- [ ] Ecosystem lock-in / switching cost manipulation

For each finding, document:
1. What the conduct is
2. What the record shows (including "hot documents")
3. Company's asserted procompetitive rationale
4. Contrary evidence
5. What remains uncertain

### 5. Risk Assessment

Structure in three layers:

| Layer | Question |
|---|---|
| **Legal risk** | Does conduct fit a plausible statutory theory? |
| **Factual risk** | How strong is the evidence? What would discovery reveal? |
| **Enforcement risk** | Is DOJ/FTC likely to prioritize given current posture? [VERIFY] |

Must also address:
- Relevant product market and geographic market (at least high-level)
- Key pivots that could change the assessment
- Counterfactual analysis (competitive landscape absent the restraint)

Avoid pseudo-quantification ("70% chance"). Use clear risk drivers instead.

### 6. Remediation Recommendations

Frame as **strategic risk mitigation**, not admission of wrongdoing. Three tiers:

| Tier | Timeframe | Examples |
|---|---|---|
| Immediate containment | 0–30 days | Stop-gap changes, messaging updates |
| Structural fixes | 1–6 months | Policy/process changes, contract revisions, approval pathways |
| Monitoring & governance | Ongoing | Audit plans, training cadence, metrics |

Common tech-platform remediation items:
- Platform Access Review process for ranking/default/API changes (documented criteria, procompetitive rationale, Legal sign-off)
- Contract term revision (remove de facto exclusivity, anti-steering)
- Contemporaneous documentation requirements for access decisions
- Information barriers for competitor data
- Enhanced antitrust training for product, engineering, BD teams
- M&A protocol with early-stage antitrust risk assessment

Tie each recommendation to a specific finding. Assign ownership (Legal, Compliance, Product, etc.) and timeline. Use advisory language: "revise provisions that could be characterized as conditioning" not "cease illegal tying."

### 7. Regulatory Exposure & Readiness

| Element | Content |
|---|---|
| Current posture | Pending inquiries, prior decrees/commitments |
| Likely theories | Mapped to fact pattern and current agency priorities [VERIFY] |
| Key risk documents/witnesses | What creates the most exposure |
| Preparedness | Preservation holds, response team, messaging discipline |
| Strategic options | Proactive engagement vs. monitoring vs. preparing for compelled process |

Include readiness checklist:
- [ ] Preservation holds in place and functioning
- [ ] External counsel identified/retained
- [ ] Response protocol for CIDs, subpoenas, informal requests
- [ ] Messaging guidelines updated for high-risk topics
- [ ] HSR considerations addressed (if M&A dimension exists)

## Guidelines

**Privilege-protective drafting:**
- Use advisory language throughout ("the evidence could be interpreted as…" not "the company fixed prices")
- Separate factual findings from legal analysis from recommendations
- Never make conclusory admissions ("this violates Section 2") — characterize as "potential theories," "enforcement risk," "facts that could be argued to support"
- Limit content to what the Board needs for decision-making
- Privilege framework: *Upjohn Co. v. United States*, 449 U.S. 383 (1981) [VERIFY]; *Hickman v. Taylor*, 329 U.S. 495 (1947) [VERIFY]; Fed. R. Civ. P. 26(b)(3); Fed. R. Evid. 501

**Adversarial resilience:**
- Draft as if a regulator or plaintiff may read despite privilege claims
- Test every sentence: if quoted out of context in a complaint, would it be damaging?
- Address "hot documents" directly — acknowledge, contextualize, assess impact
- Balance every exclusionary finding against evidence-supported procompetitive benefits

**Anti-hallucination (non-negotiable):**
- Every case citation, agency guidance reference, and doctrinal statement must be verified via current sources or marked `[VERIFY]`
- Every factual assertion must be traceable to a document, interview, or dataset
- Clearly separate verified facts from counsel's assessment; identify uncertainties explicitly
- If adjectives like "systematic," "widespread," or "intentional" are used, confirm the record supports them

**Scope limitations:**
- US federal antitrust only — flag state AG / private class action exposure for specialist follow-up
- Flag international exposure (EU Article 102 TFEU, Digital Markets Act, UK competition law) for jurisdiction-specific analysis if company has significant non-US presence
- If venue-specific circuit standards matter, present risk in circuit-neutral terms unless circuit is specified and verified
- Counsel represents the organization (Model Rule 1.13), not individual executives — manage Upjohn warnings and conflicts accordingly

**Ethics guardrails:**
- Attorney must review all output before use — this is a drafting aid, not legal advice
- Model Rule 1.1 (competence including technology understanding) [VERIFY]
- Model Rule 1.6 (confidentiality) [VERIFY]
- Model Rule 4.1 (truthfulness) / 3.3 (candor to tribunals) [VERIFY]
- Do not input unnecessary personal data; follow organization's secure AI workflow
