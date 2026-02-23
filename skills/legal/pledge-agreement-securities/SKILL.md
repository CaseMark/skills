---
name: pledge-agreement-securities
description: Drafts institutional-quality Pledge Agreements for securities collateral, creating perfected security interests under UCC Article 9 to secure loans or credit facilities. Covers certificated and uncertificated securities, control agreements, perfection mechanics, enforcement remedies, and margin/LTV covenants. Use when drafting securities pledge agreements, collateral assignments, stock pledge documents, or security interest grants in investment property.
tags:
  - agreement
  - drafting
  - transactional
---

# Pledge Agreement (Securities)

Drafts a perfected-security-interest pledge agreement for certificated or uncertificated securities securing a loan, credit facility, or other obligation.

## Prerequisites

1. **Underlying credit documents** — credit agreement, promissory note, or facility terms (principal, rate, maturity, commitment amount)
2. **Party details** — full legal names, entity types, jurisdictions of formation, addresses, signing authority
3. **Securities details** — issuer, type (common/preferred/bonds), share count or principal amount, certificate numbers, CUSIPs, account numbers, intermediary info
4. **Existing encumbrances** — any prior liens, shareholder agreements, transfer restrictions, rights of first refusal
5. **Related security package** — guarantees, intercreditor agreements, other collateral docs (for cross-reference consistency)

## Output Structure

### Document Skeleton

| Section | Key Contents |
|---|---|
| **Title & Preamble** | "Pledge Agreement (Securities)"; execution date; full party identification with entity type, jurisdiction, address; representative capacity if acting as agent |
| **Recitals** | Reference underlying obligation by title/date/parties; state principal or commitment amount; note that pledge is required under credit docs |
| **Definitions** | "Pledged Securities," "Secured Obligations" (all principal, interest, fees, indemnities, extensions, refinancings), "Collateral," "Event of Default" |
| **Collateral Description** | See Collateral Checklist below |
| **Grant of Security Interest** | Pledgor grants, pledges, assigns, and transfers continuing first-priority security interest in all Collateral to secure Secured Obligations |
| **Perfection & Delivery** | Method-specific mechanics (see Perfection Table) |
| **Representations & Warranties** | See R&W Checklist |
| **Covenants** | Affirmative + negative covenants; voting/distribution rights; LTV/margin requirements |
| **Events of Default** | Payment default; rep breach; covenant breach; cross-default/cross-acceleration; bankruptcy/insolvency; material adverse change in collateral value; delisting/trading suspension |
| **Remedies** | UCC Art. 9 disposition rights; commercially reasonable sale; application of proceeds; credit bidding; deficiency liability; voting/governance takeover |
| **Valuation & Substitution** | Valuation methodology; substitution conditions; simultaneous exchange requirement |
| **Release & Termination** | Full release on payment; partial release criteria (LTV thresholds); pledgee obligation to return certificates, terminate control agreements, file UCC-3s |
| **General Provisions** | Governing law; notices; amendments/waivers; severability; successors/assigns; integration; counterparts; pledgee standard of care; indemnification; expense reimbursement |
| **Signature Blocks** | Entity name, signatory name/title, date; notarial certificates if needed |

### Collateral Description Checklist

- [ ] Security type (common stock, preferred, bonds, debentures, notes)
- [ ] Issuer full legal name
- [ ] Number of shares or principal amount
- [ ] Certificate numbers (certificated) or account number (uncertificated)
- [ ] CUSIP / ISIN identifiers
- [ ] Class or series designation
- [ ] Securities intermediary name and address (if book-entry)
- [ ] All proceeds, products, dividends, distributions, interest, redemption proceeds, subscription rights, stock splits, stock dividends, liquidation proceeds

### Perfection Mechanics

| Collateral Type | Perfection Method | UCC Basis | Required Actions |
|---|---|---|---|
| **Certificated securities** | Possession | § 9-313 | Deliver certificates + blank stock/bond powers (signature guaranteed if required) to pledgee/custodian |
| **Uncertificated (intermediary-held)** | Control | § 9-106, § 9-314 | Tri-party control agreement: intermediary complies with pledgee entitlement orders without pledgor consent |
| **Uncertificated (direct)** | Registration | § 8-301(b) | Register pledge on issuer's books/stock ledger; obtain issuer cooperation and consent |
| **Protective filing** | Filing | § 9-310 | UCC-1 financing statement (not required if possession/control achieved, but advisable as belt-and-suspenders) |

### R&W Checklist

- [ ] Good, valid, marketable title free of liens (except permitted liens)
- [ ] Full authority to pledge; all organizational approvals obtained
- [ ] No violation of law, regulation, order, charter, bylaws, shareholder agreement
- [ ] Securities duly authorized, validly issued, fully paid, non-assessable (equity)
- [ ] No third-party rights of first refusal, preemptive rights, or co-sale rights triggered by pledge
- [ ] Securities law compliance (pledge exempt from registration or properly registered)
- [ ] No pending/threatened litigation affecting pledged securities
- [ ] Information about securities is accurate and complete

### Covenant Framework

**Affirmative:**
- Maintain securities in good standing
- Pay taxes/assessments on securities
- Defend pledgee's security interest against all claims
- Deliver periodic valuations (market close for listed; independent appraisal for unlisted)
- Notify pledgee of material events affecting collateral

**Negative:**
- No sale, transfer, assignment, or disposition without pledgee consent
- No additional liens or encumbrances
- No amendment of issuer organizational documents that impair collateral value (if pledgor controls issuer)

**Voting & Distributions (bifurcated regime):**
- Pre-default: pledgor retains voting rights and receives dividends/distributions
- Post-default: all voting, consensual, and economic rights shift to pledgee; pledgee may vote, exchange securities in M&A, collect distributions

**LTV / Margin Maintenance:**
- Specify required LTV ratio and valuation methodology
- Cure mechanism: pledge additional securities or pay down principal within [X] business days
- Breach triggers Event of Default if uncured

### Remedies Template

```
Upon Event of Default, Pledgee may:
(a) Exercise all UCC Art. 9 secured-party remedies
(b) Sell Collateral at public or private sale (broker-dealer, exchange,
    OTC, private negotiation) on commercially reasonable terms
(c) Apply proceeds: (i) costs of enforcement including attorneys' fees →
    (ii) Secured Obligations in pledgee-determined order → (iii) surplus
    to Pledgor
(d) Credit bid at any sale
(e) Exercise all voting/governance rights
(f) Collect deficiency from Pledgor [unless non-recourse]

Notice: [10] days' notice before disposition deemed reasonable;
no notice required for exchange-traded securities [per agreement].
Pledgor may redeem by paying Secured Obligations in full plus
pledgee expenses at any time before disposition.
```

## Guidelines

- **UCC Art. 9 compliance is non-negotiable** — match perfection method to collateral type; possession for certificated, control for intermediary-held
- **Defined terms must be consistent** across pledge agreement and all related credit documents; cross-check party names, obligation definitions, default triggers
- **Securities law transfer restrictions** — confirm pledge does not trigger registration requirements; address Rule 144 and contractual lock-ups
- **Control agreement execution** — specify deadline and consequence if intermediary refuses or delays
- **Commercially reasonable disposition** — UCC § 9-610 standard; never draft provisions that waive commercial reasonableness
- **Closely held securities** — add issuer acknowledgment and consent provisions; address valuation difficulty with independent appraisal requirements
- **Multi-lender deals** — if pledgee acts as agent, clarify authority, lien-sharing, and coordination with intercreditor agreement
- **Governing law** — UCC §§ 9-301 to 9-307 choice-of-law rules may override contractual selection for perfection purposes; note this in drafting
- **Do not waive** pledgor's right of redemption before disposition or statutory notice requirements beyond what UCC permits
- **Mark uncertain citations** with `[VERIFY]` — especially state-specific variations in UCC adoption or securities transfer statutes
