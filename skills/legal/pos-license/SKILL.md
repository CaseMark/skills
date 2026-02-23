---
name: pos-license
description: Drafts Software and Point of Sale (POS) System License Agreements governing licensor-licensee relationships for proprietary software use. Covers license grants, scope limitations, financial terms, IP protections, data security (PCI-DSS), SLAs, and termination with transition provisions. Use when drafting POS software licenses, SaaS subscription agreements, franchise technology licenses, or software distribution agreements in transactional contexts.
tags:
  - agreement
  - drafting
  - transactional
---

# Software & POS System License Agreement

Drafts a license agreement governing access, installation, and operation of proprietary software and POS system technology between a licensor and licensee.

## Prerequisites

1. **Party information** — full legal names, entity types, jurisdictions of organization, and any affiliates bound by or benefiting from the agreement
2. **Software/POS specifications** — deployment model (cloud/on-premises), components licensed, documentation, source vs. object code access
3. **Commercial terms** — pricing model, payment schedule, renewal structure, user/location counts
4. **Technical requirements** — hardware integration, payment processing, inventory management, multi-location needs
5. **Applicable regulations** — PCI-DSS requirements, GDPR/CCPA applicability, state-specific software licensing rules

## Output Structure

### 1. Recitals & Definitions

- Identify parties with entity type, principal place of business, jurisdiction
- Establish licensor ownership context and licensee's business need
- Define all capitalized terms in a dedicated section or on first use

### 2. Grant of License

| Parameter | Options to Specify |
|---|---|
| Exclusivity | Exclusive / Non-exclusive |
| Term | Perpetual / Fixed term / Renewable |
| Scope | Internal use only / Third-party service permitted |
| Users | Named users / Concurrent / Unlimited |
| Locations | Single-site / Multi-location / Geographic limits |
| Code access | Object code only / Source code included |
| Deployment | Cloud / On-premises / Hybrid |
| Updates | Included / Separate fee / Major vs. minor |
| Sublicensing | Prohibited / With consent / Affiliate carve-out |

Explicitly restrict: reverse engineering, decompilation, disassembly, derivative works (unless negotiated).

### 3. Financial Terms

- **Fee structure**: one-time / subscription / per-user / per-transaction / hybrid
- **Payment schedule**: due dates, accepted methods, currency
- **Late payments**: interest rate, grace period
- **Renewal pricing**: auto-renewal terms, escalation cap (fixed % or index-tied), notice period for changes
- **Taxes**: allocate responsibility for sales/use/VAT
- **Audit rights**: licensor right to verify user-count/transaction-volume compliance; underpayment reconciliation procedure

### 4. Intellectual Property

- [ ] Licensor retains all ownership; license conveys no title
- [ ] Derivative works / customizations — specify ownership (typically licensor)
- [ ] Licensee feedback/suggestions assigned to licensor without compensation
- [ ] Licensee business data remains licensee property; system architecture remains licensor property

### 5. Confidentiality & Data Protection

- Mutual NDA with standard carve-outs (public knowledge, independent development, third-party disclosure)
- Confidentiality survives termination (specify duration)
- **POS-specific requirements**:
  - PCI-DSS compliance for payment card data
  - Encryption standards (transit + at rest)
  - Breach notification timeline and procedure
  - GDPR/CCPA roles: identify controller vs. processor
  - Data processing addendum if required

### 6. Warranties & SLAs

**Limited warranty** (typically 90 days):
- Software substantially conforms to published specifications
- Exclusive remedy: defect correction → refund if correction not commercially reasonable

**POS performance SLAs** (if applicable):

| Metric | Target | Remedy |
|---|---|---|
| Uptime | 99.X% | Service credits |
| Transaction speed | < X seconds | Escalation path |
| Support response | X hours | Penalty/credit |

**Disclaimers**: Disclaim implied warranties (merchantability, fitness for particular purpose, non-infringement) to maximum extent permitted by law. No warranty of uninterrupted/error-free operation.

### 7. Liability & Indemnification

- **Exclusion**: consequential, incidental, indirect, special, punitive damages (including lost profits, lost data, business interruption)
- **Cap**: lesser of (a) fees paid in preceding 12 months or (b) total fees paid
- **Carve-outs from cap**: confidentiality breach, IP infringement, gross negligence, willful misconduct, violation of law
- **Mutual indemnity**: each party indemnifies against third-party claims from its breach, negligence, or legal violations
- **Procedure**: prompt notice → cooperation → indemnifying party controls defense/settlement

### 8. Term & Termination

| Trigger | Notice Period | Cure Period |
|---|---|---|
| Convenience | 30–90 days | N/A |
| Material breach | Immediate after cure | 15–30 days |
| Insolvency/bankruptcy | Immediate | N/A |

**Post-termination obligations**:
- [ ] Immediate cessation of all usage rights
- [ ] Return or certified destruction of software and confidential information
- [ ] Final payment of outstanding fees
- [ ] POS system deactivation
- [ ] Transition period for data extraction/migration (specify duration)
- [ ] Prorated refund terms (if termination without cause)
- [ ] Early termination penalties (if applicable)

**Survival**: confidentiality, IP ownership, liability limitations, indemnification, governing law.

### 9. Dispute Resolution

- **Governing law**: specified state, excluding conflict-of-laws principles
- **Venue**: exclusive jurisdiction in designated state/federal courts
- **ADR ladder** (recommended):
  1. Executive negotiation (15–30 days)
  2. Mediation (AAA or JAMS rules)
  3. Litigation or binding arbitration
- **Fee shifting**: prevailing party recovers reasonable attorneys' fees (or each bears own — specify)

### 10. General Provisions

Include: severability, entire agreement/merger, amendment (written, signed by authorized reps), assignment restrictions (licensee restricted; licensor may assign to affiliates or in M&A), notice methods and deemed-receipt timelines, non-waiver, force majeure, signature blocks with authority confirmation.

## Guidelines

- Use plain language; avoid "witnesseth," "whereas," "party of the first part"
- Maintain consistent defined terms throughout; capitalize on each use
- Number all sections/subsections for cross-reference
- Adapt standard license terms for POS-specific concerns: hardware integration, payment processing, inventory management, multi-location deployment
- Verify compliance with applicable UCC Article 2/2A provisions, consumer protection laws, and industry-specific regulations
- Flag any jurisdiction-specific requirements with `[JURISDICTION NOTE]`
- For franchise contexts, cross-check consistency with FDD Item 11 (franchisor's obligations re: technology) and any franchise agreement technology provisions
