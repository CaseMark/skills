---
name: ecp-manual
description: Drafts a comprehensive Export Compliance Program (ECP) Manual governing U.S. export control compliance under EAR, ITAR, and OFAC sanctions programs. Covers management commitment, risk assessment, classification methodology (ECCN/USML), licensing determinations, restricted party screening, recordkeeping, training architecture, internal audits, and voluntary self-disclosure procedures. Use when creating or updating an authoritative export compliance policy document, international trade compliance program, or enforcement defense preparation for regulatory review.
tags:
  - drafting
  - policy
  - regulatory
  - research
---

# Export Compliance Program (ECP) Manual

Drafts a tailored, audit-ready ECP Manual establishing policies, procedures, and controls for full compliance with U.S. export control laws (EAR, ITAR, OFAC) and applicable foreign regimes.

## Prerequisites

1. **Company profile** — legal name, corporate structure, business units involved in export activities
2. **Product/technology inventory** — catalog, technical specifications, or item descriptions for classification analysis
3. **Export footprint** — current destination countries, customer list, and restricted-market exposure
4. **Existing compliance posture** — prior export licenses, commodity jurisdiction rulings, VSD history, audit findings, or known violations
5. **Organizational structure** — compliance personnel, reporting lines, and ECP ownership (CCO, GC, EMPD)

Search any uploaded organizational documents for: org charts, product catalogs, customer lists, prior licenses, agency correspondence, and prior audit findings. Use extracted details to tailor the manual rather than produce a generic template.

## Output Structure

### 1. Management Commitment Statement
- CEO/senior executive authorship; zero-tolerance policy language
- Explicit grant of authority to compliance personnel to halt non-compliant transactions
- Consequence statement: civil/criminal penalties, denial of export privileges, debarment, personal liability for individuals
- Resource commitment: personnel, systems, training, external counsel

### 2. Risk Assessment Framework

| Dimension | Key Factors |
|---|---|
| Item sensitivity | Dual-use (EAR/ECCN), defense article (ITAR/USML), technology/technical data, deemed export exposure |
| Destination risk | Country tier, embargoed/restricted status, proliferation concerns, active sanctions programs |
| End-user/end-use | Business activities, ownership structure, diversion indicators, willingness to provide end-use information |

**Cadence:**
- Enterprise-level: annually + triggered by new product lines, market entry, acquisitions, or major regulatory changes
- Transaction-level: per-deal with documented escalation criteria

**Red Flags (trigger enhanced due diligence):**
- Customer reluctant to provide end-use information
- Product inconsistent with customer's known business
- Unusual routing, shipping, or payment instructions
- Freight forwarders in high-risk jurisdictions
- Customer proximity to sensitive facilities or free trade zones
- Requests for export packaging inconsistent with stated destination

### 3. Classification Procedures

**EAR Classification:**
1. Determine whether subject to EAR, ITAR, or another regime
2. Review Commerce Control List (CCL) → assign ECCN (product group, technical parameters, reasons for control)
3. Evaluate "specially designed" provisions; apply de minimis rules for foreign-made items incorporating U.S. content
4. No CCL match → designate EAR99 and document determination

**ITAR Classification:**
1. Review U.S. Munitions List (USML) categories for defense article/defense service status
2. Dual-use/dual-jurisdiction ambiguity → file Commodity Jurisdiction (CJ) request to DDTC
3. Document all CJ rulings and advisory opinions; re-evaluate when products evolve

**Documentation:** Retain classification worksheets, technical analysis, CJ determinations, and advisory opinions. Review classifications periodically as products or regulations change.

### 4. Licensing Determination Procedures

| Scenario | Action |
|---|---|
| EAR-controlled item | Check Commerce Country Chart (ECCN × destination) for license requirement |
| License exception potentially available | Verify all conditions met; document exception basis and rationale |
| EAR99 / unrestricted destination | No license required; document EAR99 determination |
| ITAR-controlled item/service | Determine DSP-5, DSP-73, TAA, or MLA applicability; submit via DECCS |
| OFAC sanctions nexus | Confirm general license applicability or obtain specific OFAC license |

Special licensing considerations: temporary exports, re-exports, deemed exports of controlled technology to foreign nationals, encryption items, multi-country transactions.

Track all license conditions, validity periods, and shipment reporting obligations. Maintain license compliance records throughout the authorization period.

### 5. Restricted Party Screening

**Required Lists (minimum):**
- OFAC Specially Designated Nationals & Blocked Persons (SDN) List
- BIS Entity List
- BIS Denied Persons List
- BIS Unverified List
- BIS Military End User (MEU) List
- State Department AECA Debarred List
- Consolidated Screening List (CSL) — aggregates most BIS/DDTC/OFAC lists

**Screening Protocol:**
- Screen at: customer onboarding, order entry, pre-shipment, and periodic refresh for ongoing relationships
- Screen all parties: customer, consignee, end-user, freight forwarder, financial institutions
- Use fuzzy-logic matching to catch name variants, aliases, and address variations
- Document: date/time of screening, lists searched, results, false-positive analysis and rationale
- Confirmed match → transaction prohibited; escalate to legal counsel immediately

**OFAC ownership rule:** Entities owned 50% or more (individually or in aggregate) by an SDN are treated as blocked even if not separately listed.

### 6. Recordkeeping Requirements

| Record Category | Minimum Retention |
|---|---|
| Export licenses & authorizations | Permanent (or life of license + 5 years) |
| Classification determinations | Life of product + 5 years |
| Restricted party screening results | 5 years from transaction date |
| Shipping documents (invoice, B/L, EEI/AES filing) | 5 years from date of export |
| License exception documentation | 5 years from date of export |
| Technology transfer agreements (TAA, MLA, WDA) | 5 years from expiration |
| Training records | 5 years (or duration of employment + 5) |
| VSD correspondence & investigation records | Permanent |

Regulatory minimums: EAR = 5 years [15 C.F.R. § 762.6 [VERIFY]]; ITAR = 5 years [22 C.F.R. § 122.5 [VERIFY]]; OFAC = 5 years [31 C.F.R. § 501.601 [VERIFY]].

Records must be organized for efficient retrieval; electronic systems require access controls, backup, and disaster recovery. Designate a coordinator for responding to government records requests; involve legal counsel before production.

### 7. Training Program

| Tier | Audience | Core Topics |
|---|---|---|
| Awareness | All employees | Export controls overview, consequences of violations, how to report concerns, no-retaliation policy |
| Intermediate | Sales, purchasing, shipping, customer service | Red flags, screening procedures, when to escalate, documentation requirements |
| Advanced | Compliance specialists, ECP owners | Classification, licensing/exceptions, deemed exports, encryption controls, sanctions analysis |
| Technical | Engineers, scientists, IT | Deemed export rules, definition of technology/technical data, controlled technical assistance, authorization before sharing |

- Delivery methods: instructor-led, web-based modules, scenario exercises, just-in-time briefings for emerging risks
- Metrics: pre/post knowledge assessments, periodic retention testing, behavioral compliance monitoring
- Documentation: attendee name, date, topics covered, assessment scores, completion certificates — retained as audit evidence

### 8. Internal Audit Program

**Audit Scope:**
- Classification accuracy — sample review of determinations with supporting technical analysis
- License compliance — conditions/limitations observed, shipment reporting met
- Screening completeness — all parties screened at required points; match analysis documented
- Recordkeeping adequacy — required records created, maintained, and retained per policy
- Procedural adherence — personnel interviews and transaction document testing

**Cadence:**
- Comprehensive program audit: annually
- Focused high-risk audits: triggered by new market entry, new product line, or significant regulatory change
- Transaction testing: statistically valid, risk-weighted sample

**Audit Methodology:** Develop checklists; examine documents; interview personnel; test compliance systems; compare actual practices against established procedures.

**Output:** Written report with severity-rated findings → root cause analysis → corrective action plan with named owners and firm deadlines → follow-up verification of implementation.

**Reporting Line:** Findings reported to CCO, GC, and relevant business unit leaders; material or systemic findings escalated to CEO and board/audit committee.

### 9. Violation Response & Voluntary Self-Disclosure (VSD)

**Reporting Channels:** Direct supervisor, dedicated compliance hotline/email, anonymous third-party reporting mechanism. No-retaliation policy mandatory; violations of no-retaliation policy subject to separate discipline.

**Upon Discovery:**
1. Preserve all evidence; implement litigation hold
2. Interview witnesses promptly; reconstruct complete transaction history
3. Conduct root cause analysis (procedure gap, system failure, training gap, human error, intentional misconduct)
4. Implement interim holds on similar transactions
5. Engage export control counsel immediately

**VSD Decision Factors:**
- Nature and severity of violation; inadvertent vs. willful
- National security harm; sanctioned-party involvement
- Likelihood of independent government discovery
- Mitigating factors: effective program, prompt detection, remediation, cooperation
- Prior violation history

**VSD Submission by Agency:**

| Regime | Agency | Mechanism |
|---|---|---|
| EAR violations | BIS Office of Export Enforcement | Written narrative + supporting documentation |
| ITAR violations | DDTC | Written VSD per 22 C.F.R. Part 127 [VERIFY] |
| OFAC sanctions | OFAC | Written VSD per OFAC Enforcement Guidelines |

VSD contents must address: what happened, how, why, when discovered, full scope of violations, and corrective actions taken/planned.

**Discipline Matrix:**

| Severity | Response |
|---|---|
| Minor / inadvertent | Additional training, counseling |
| Moderate | Written warning, performance improvement plan |
| Serious / intentional | Suspension, termination, referral for prosecution |

Discipline applied consistently across all levels; senior personnel held to same or higher standards.

## Guidelines

- **Living document**: Review annually and upon regulatory change, organizational change, or material audit finding; maintain version control; remove obsolete versions from circulation
- **Mandatory language**: Use "must/shall" for required actions; "should" for best practices; "may" for permissible options only
- **Counsel involvement**: VSD decisions, license applications, CJ requests, and investigations require export control attorney oversight
- **Deemed exports**: Screen all foreign national hires and collaborators for controlled technology access under EAR and ITAR deemed export rules before granting access
- **Encryption controls**: Apply EAR §§ 740.17 and 742.15 [VERIFY] for encryption items; conduct annual encryption reviews and file required reports
- **OFAC 50% rule**: Treat entities 50%+ owned by SDNs as blocked even if not separately listed on the SDN List
- **EAR99 caution**: EAR99 designation does not eliminate license requirements for embargoed destinations or prohibited end-uses under part 744
- **Foreign regimes**: Note applicable foreign export control obligations (e.g., EU Dual-Use Regulation, UK Export Control Order) where the organization operates abroad
