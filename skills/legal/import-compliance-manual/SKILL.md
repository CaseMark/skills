---
name: import-compliance-manual
description: Drafts a comprehensive U.S. Import Compliance Manual serving as both an operational guide and evidence of reasonable care under 19 U.S.C. § 1484. Covers CBP compliance policy, HTS classification procedures, customs valuation under 19 U.S.C. § 1401a, country of origin determinations, recordkeeping under 19 C.F.R. Part 163, Partner Government Agency (PGA) compliance, internal audit programs, employee training, and corrective action protocols. Use when creating or overhauling an importer-of-record compliance program, preparing for a CBP audit or focused assessment, or establishing written procedures to demonstrate reasonable care.
tags:
  - checklist
  - drafting
  - memo
  - regulatory
---

# Import Compliance Manual

Drafts a U.S. customs import compliance manual that functions as an operational policy document and demonstrates reasonable care under 19 U.S.C. § 1484.

## Prerequisites

1. **Company profile** — importer name, EIN/CBP importer number, principal ports of entry, product categories
2. **Organizational chart** — identify who owns compliance (CCO, compliance committee, import manager)
3. **Trade programs in use** — FTAs (USMCA, bilateral), GSP, drawback, FTZ, TIB, carnet
4. **PGA exposure** — which agencies regulate your products (FDA, USDA/APHIS, EPA, CPSC, etc.)
5. **Existing procedures** — any current SOPs, broker agreements, classification databases to incorporate

## Output Structure

Generate each section below as a numbered chapter with sub-sections. Use a professional document format with a version control block, table of contents, and executive signature line.

---

### Chapter 1 — Corporate Policy Statement

| Element | Required Content |
|---|---|
| Statutory basis | Commitment to Tariff Act of 1930, as amended; all CBP-administered regulations |
| Reasonable care | Explicit acknowledgment of 19 U.S.C. § 1484 standard |
| Zero tolerance | No willful violations or gross negligence; civil/criminal penalties cited |
| Scope | All entries, all ports, all entry types, all values |
| Responsibility | Named executive role or compliance committee with defined authority |
| Covered parties | Employees, agents, brokers, freight forwarders, third-party providers |
| Review cycle | Annual minimum; triggered by regulatory change or business change |

---

### Chapter 2 — HTS Classification Procedures

**Designated classifier:** Named role with technical and legal authority.

**Classification methodology (apply in order):**
1. Identify product characteristics and end use
2. Apply GRI 1–6 in hierarchical sequence
3. Consult Explanatory Notes, CBP rulings (CROSS database), and relevant court decisions
4. Document rationale in classification worksheet

**Documentation requirements per SKU:**
- [ ] Technical specifications / material composition
- [ ] Lab test reports (where applicable)
- [ ] Written GRI analysis citing specific heading/subheading
- [ ] Supporting CBP rulings or Explanatory Note references
- [ ] Classification database entry with entry number cross-reference

**Binding rulings:** Submit to CBP via CROSS when classification is uncertain or duty impact is significant; implement ruling on receipt; track expiration.

**Monitoring:** Designate reviewer for CBP ruling updates, USITC tariff schedule amendments, and court decisions (e.g., CIT, CAFC); reassess affected SKUs within 30 days of material change.

**Broker disagreements:** Company retains IOR responsibility regardless of broker recommendation; escalation process to legal counsel for unresolved disputes.

---

### Chapter 3 — Customs Valuation Procedures

**Primary method:** Transaction value under 19 U.S.C. § 1401a(b).

**Elements always reviewed before entry:**

| Item | Include in Value? |
|---|---|
| International freight & insurance | Yes (CIF) / No (FOB) — per contract terms |
| Packing costs | Yes |
| Buying commissions | No |
| Selling commissions | Yes |
| Assists (tooling, materials, engineering) | Yes — prorate per 19 C.F.R. § 152.103(e) |
| Royalties/license fees related to imported goods | Yes if condition of sale |
| Proceeds of subsequent resale to seller | Yes if contractually required |

**Related-party transactions (19 C.F.R. § 152.102(g)):**
1. Document relationship (org chart, ownership ≥ 5%)
2. Perform circumstances-of-sale analysis
3. If price influenced: apply test values (identical/similar goods, deductive, or computed value)
4. Maintain transfer pricing studies and intercompany agreements

**Valuation hierarchy (when transaction value unavailable):**
Transaction value of identical → similar goods → deductive value → computed value → fallback (19 U.S.C. § 1401a(f))

**Post-entry corrections:** File CF-7501 amendment or prior disclosure under 19 U.S.C. § 1592(c)(4) upon discovery of underpayment; involve legal counsel before submission.

---

### Chapter 4 — Country of Origin Procedures

**Non-preferential origin (marking — 19 U.S.C. § 1304):**
- Apply substantial transformation test: name, character, and use before/after processing
- Identify ultimate purchaser; confirm marking exceptions do not apply
- Textiles/apparel: apply Section 334, Uruguay Round Agreements Act rules [VERIFY citation for specific fiber/yarn/fabric categories]

**Preferential origin — required documentation by program:**

| Program | Certificate/Claim | Key Rule |
|---|---|---|
| USMCA | Importer, exporter, or producer certification | Tariff shift + RVC or specific process rule |
| CAFTA-DR / other bilateral FTAs | Certificate of origin | Agreement-specific PSR |
| GSP | No formal cert required; maintain supplier affidavit | 35% RVC; substantial transformation |

**Supplier validation:**
- Obtain origin certification before first entry
- Conduct periodic supplier audits (risk-tiered: high-value/high-duty-differential = annual; low-risk = biennial)
- Reassess immediately upon change in sourcing country, manufacturing location, or BOM

**Documentation per product:**
- [ ] Bill of materials (origin and value of all inputs)
- [ ] Manufacturing process description
- [ ] Supplier affidavit or FTA certification
- [ ] RVC calculation worksheet (if applicable)

---

### Chapter 5 — Recordkeeping Requirements

**Governing authority:** 19 U.S.C. § 1509; 19 C.F.R. Part 163; the "Mod Act" list of required records (the "(a)(1)(A) list").

**Retention periods:**

| Record Type | Retention |
|---|---|
| Entry records (CF-7501, invoices, BOL, packing lists) | 5 years from entry date |
| Drawback records | 3 years after drawback payment or entry liquidation |
| FTZ records | 5 years from zone admission |
| Trade preference claim support | 5 years from date of claim |

**System requirements:**
- Paper, electronic, or hybrid — must produce hard copy on CBP request
- Electronic records must be unalterable after creation; audit trail required
- Backup and disaster recovery protocols documented

**Designated Part 163 recordkeeper:** Named individual; serves as CBP point of contact; responds to record requests within 30 calendar days (or shorter as directed).

**Third-party records:** Contracts with brokers and forwarders must require Part 163 compliance and grant company access to records on demand.

---

### Chapter 6 — Partner Government Agency Compliance

**PGA identification matrix (complete for each product category):**

| Agency | Statutory Basis | Key Requirement | ACE Data Element |
|---|---|---|---|
| FDA (food) | FSMA; Bioterrorism Act | Prior notice; FSVP; facility registration | FDA Product Code; Prior Notice number |
| FDA (drugs/devices) | FDCA | Premarket approval/510(k); import alert check | FDA Product Code |
| USDA/APHIS | Plant Protection Act; Lacey Act | Import permit; Lacey Act declaration | APHIS indicator |
| USDA/FSIS | Federal Meat/Poultry Acts | Equivalence determination; re-inspection | FSIS establishment number |
| EPA (pesticides) | FIFRA | Registration; labeling compliance | EPA import certification |
| EPA (chemicals) | TSCA | Import certification (positive or negative) | TSCA certification |
| EPA (vehicles/engines) | Clean Air Act | Certificate of conformity | EPA declaration |
| CPSC (general) | CPSA | General Certificate of Conformity | CPSC indicator |
| CPSC (children's products) | CPSIA | Third-party testing; Children's Product Certificate | Lab report number |

**Pre-importation checklist:**
- [ ] All required permits/licenses obtained
- [ ] PGA data transmitted via ACE Partner Government Agency Message Set
- [ ] Import alerts checked for product/supplier
- [ ] Admissibility documentation in file before arrival

**Enforcement actions:** Designate response lead for FDA refusals, USDA holds, EPA detentions; determine within 5 business days whether to bring into compliance, re-export, or destroy.

---

### Chapter 7 — Internal Audit Program

**Frequency:** Annual comprehensive audit; focused reviews upon new product, supplier, or trade lane introduction.

**Scope per audit cycle:**
- [ ] HTS classification accuracy (statistical sample; minimum 50 entries or 10%, whichever greater)
- [ ] Valuation completeness (assists, royalties, related-party prices)
- [ ] Origin and FTA claims (certification validity, supplier audit status)
- [ ] Recordkeeping completeness and retrieval timeliness
- [ ] PGA compliance and ACE data accuracy
- [ ] Trade program integrity (drawback, FTZ, TIB)
- [ ] Training completion rates

**Audit findings classification:**

| Severity | Definition | Required Action |
|---|---|---|
| Critical | Revenue loss >$10K or ongoing violation | Immediate cessation; prior disclosure evaluation; legal counsel |
| Significant | Systemic procedural failure | Corrective action plan within 30 days |
| Moderate | Isolated error; documented | Corrective action within 90 days |
| Observation | Process improvement opportunity | Address in next planning cycle |

**Privilege:** Engage outside counsel to conduct audits requiring attorney-client privilege protection; label documents accordingly.

**Prior disclosure trigger:** Evaluate under 19 U.S.C. § 1592(c)(4) for any Critical finding involving duty underpayment; disclose before CBP commences formal investigation to obtain penalty mitigation.

---

### Chapter 8 — Employee Training Program

**Role-based curriculum matrix:**

| Role | Initial | Annual Refresh | Advanced Modules |
|---|---|---|---|
| Import manager | 8 hrs | 4 hrs | GRI application; valuation; FTA RVC |
| Purchasing/procurement | 4 hrs | 2 hrs | Assists; supplier origin validation |
| Product development | 4 hrs | 2 hrs | Classification at design stage |
| Logistics coordinator | 4 hrs | 2 hrs | Entry process; PGA data; recordkeeping |
| Senior management | 2 hrs | 1 hr | Penalty exposure; IOR obligations; program oversight |

**Mandatory initial training content:**
- Importer of record obligations and liability
- Overview of classification, valuation, origin
- Civil penalties (19 U.S.C. § 1592); criminal exposure; personal officer liability
- This manual — role-specific procedures

**Documentation required:**
- [ ] Attendance log (name, date, role)
- [ ] Training materials version-controlled
- [ ] Post-training assessment with passing score threshold
- [ ] Certificates of completion retained 5 years

**Trigger for off-cycle training:** Regulatory change, audit deficiency, new product category, role change.

---

### Chapter 9 — Corrective Action and Continuous Improvement

**Upon discovery of violation:**

1. **Contain** — halt affected transaction stream; interim controls within 2 business days
2. **Investigate** — root cause analysis; scope assessment (isolated vs. systemic); document findings
3. **Evaluate disclosure** — apply 19 U.S.C. § 1592(c)(4) criteria with legal counsel; submit prior disclosure before CBP investigation commences if warranted
4. **Remediate** — written corrective action plan: root cause addressed, named owners, firm deadlines
5. **Post-entry filing** — CF-7501 amendment, supplemental information, or protest as applicable
6. **Verify** — enhanced monitoring of corrected process (100% review for 90 days or until 3 clean audits)
7. **Communicate** — targeted training; updated SOPs distributed to all affected personnel
8. **Report** — status updates to senior management; escalate to board/audit committee for systemic failures

**Corrective action tracking log fields:** Issue ID | Discovery date | Root cause | Severity | Owner | Actions | Target date | Completion date | Verification result

---

## Document Administration

| Element | Requirement |
|---|---|
| Version control | Version number, effective date, revision history table |
| Executive approval | CCO or CEO signature; re-certification annually |
| Distribution tracking | Named recipient list; acknowledgment signatures |
| Review trigger | Annual; regulatory change; CBP inquiry; audit finding |
| CBP presentation | Format must be suitable for production to CBP on request |

## Guidelines

- **Reasonable care standard:** Every procedure must be defensible under the "reasonable person" standard of 19 U.S.C. § 1484; document the *why*, not just the *what*
- **Broker reliance:** Using a licensed broker does not transfer IOR liability; all procedures must confirm company retains classification and valuation responsibility
- **Jurisdiction:** U.S.-specific (CBP, ACE, U.S. federal statutes); adapt PGA section to actual product mix — do not include inapplicable agencies
- **Penalty exposure:** Civil penalties under 19 U.S.C. § 1592 range from 20% (negligence) to 4× unpaid duties (fraud); manual existence and adherence is a mitigation factor
- **Verify citations:** Confirm current HTS edition, active FTA rules of origin, and any USITC Section 301/232 tariff overlays at time of drafting — these change frequently [VERIFY current Section 301 list applicability]
- **Attorney review:** Recommend legal counsel review before finalizing; privilege may attach to counsel-directed compliance assessments
