---
name: contract-analysis
description: Analyzes contracts to identify key terms, obligations, risks, ambiguities, and negotiation opportunities. Produces structured risk assessments with executive summary, section-by-section review, risk matrix, and prioritized recommendations. Use when reviewing agreements before execution, during negotiation, at closing, or for ongoing compliance monitoring in transactional matters.
tags:
  - agreement
  - analysis
  - summary
  - transactional
---

# Contract Analysis

Extracts and evaluates all material provisions, risk allocations, and obligations across one or more contracts to support negotiation, execution, or remediation decisions.

## Prerequisites

1. **Contract document(s)** — fully executed or draft versions; note which
2. **Client role** — which party the analysis should favor (or neutral if comparative)
3. **Applicable jurisdiction** — governing law if known; flag if absent from contract
4. **Scope** — full review, specific provisions only, or comparative multi-contract analysis

## Output Structure

### 1. Executive Summary
- Parties, effective date, term, and governing law (1–2 sentences each)
- Top 3–5 critical risks or issues requiring immediate attention
- Overall favorability assessment (favorable / balanced / unfavorable)

### 2. Key Provisions Matrix

| Provision | Section | Summary | Risk Level | Notes |
|-----------|---------|---------|------------|-------|
| Term & Termination | § | | | Cure periods, notice, convenience rights |
| Payment Terms | § | | | Timing, late fees, set-off rights |
| Scope / Deliverables | § | | | Ambiguity, change-order mechanics |
| Indemnification | § | | | Mutual vs. one-sided, carve-outs |
| Limitation of Liability | § | | | Cap amount, excluded damages |
| Warranty / Disclaimer | § | | | Express vs. implied, remedy limits |
| Insurance | § | | | Required types, minimums, AI/WC |
| IP Ownership | § | | | Work-for-hire, license-back, background IP |
| Confidentiality | § | | | Term, carve-outs, residuals clause |
| Dispute Resolution | § | | | Arb vs. litigation, venue, fee-shifting |
| Auto-Renewal | § | | | Notice window, opt-out mechanics |
| Assignment / Change of Control | § | | | Consent requirements, deemed consent |
| Force Majeure | § | | | Scope, notice, extended FM termination right |
| Governing Law / Venue | § | | | |

### 3. Risk Matrix

| Issue | Section | Severity | Likelihood | Recommended Action |
|-------|---------|----------|------------|-------------------|
| | | High / Med / Low | High / Med / Low | |

Risk categories to assess:
- **Ambiguity** — language supporting multiple interpretations
- **Asymmetry** — one-sided obligations or liability allocation
- **Gaps** — material matters left unaddressed
- **Conflicts** — internal inconsistencies between sections
- **Unenforceability** — provisions likely void under applicable law

### 4. Comparative Analysis *(multi-contract only)*
Table comparing key terms across agreements; flag deviations from market standard.

### 5. Prioritized Recommendations

| Priority | Provision | Issue | Proposed Fix |
|----------|-----------|-------|-------------|
| 1 (Critical) | | | |
| 2 (High) | | | |
| 3 (Moderate) | | | |

## Guidelines

- Cite exact section numbers and quote key language verbatim when identifying risks
- Flag auto-renewal clauses with short opt-out windows as high-priority regardless of other risk factors
- Note all cross-references to external documents, exhibits, or incorporated standards — treat as additional obligations
- For ambiguous provisions, state the full range of plausible interpretations and their respective implications
- Do not assess enforceability under specific state law without verifying current precedent; use `[VERIFY]` on any statutory or case citations
- Jurisdiction caveat: UCC Article 2 applies to goods contracts; common law governs services — note if contract mixes both without specifying
- Flag any non-compete, non-solicit, or liquidated damages clauses for separate enforceability review under applicable state law
