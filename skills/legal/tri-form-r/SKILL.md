---
name: tri-form-r
description: Drafts EPA Toxic Release Inventory (Form R) reports compliant with EPCRA Section 313 and 40 CFR Part 372. Covers facility identification, chemical threshold determinations, release quantification across all media, off-site transfers, source reduction reporting, and certification. Use when preparing TRI filings, Form R reports, toxic chemical release disclosures, or annual EPCRA Section 313 submissions for manufacturing or processing facilities.
tags:
  - drafting
  - memo
  - regulatory
---

# Toxic Release Inventory (Form R) Report

Drafts a complete, certifiable Form R report for EPA submission under EPCRA Section 313, covering toxic chemical releases, waste management, and pollution prevention for a reporting year.

## Prerequisites

1. **Facility records** — legal name, address, TRI Facility ID, RCRA ID, NPDES permit numbers, SIC/NAICS codes, parent company Dun & Bradstreet number
2. **Chemical inventory data** — purchase records, production logs, CAS numbers for all listed toxic chemicals manufactured, processed, or otherwise used
3. **Release/emission data** — CEMS data, stack tests, discharge monitoring reports, waste manifests, emission factor calculations
4. **Prior TRI submissions** — for consistency review and trend analysis
5. **Pollution prevention records** — process modifications, material substitutions, recycling data

## Output Structure

### Part 1: Facility Identification

| Field | Requirements |
|---|---|
| Facility name | Exact legal name as registered with EPA |
| Address | Physical operational address (no PO boxes) |
| County | Determines state/local agency recipients |
| Parent company | Legal name + Dun & Bradstreet number |
| SIC/NAICS codes | Primary code by revenue/production volume — determinative of reporting obligation |
| Owner/Operator | Names, titles, phone, email for highest-ranking officials |
| Facility IDs | Cross-reference TRI ID, RCRA ID, NPDES permit, air permit numbers |
| Federal facility? | Yes/No — triggers special reporting procedures |

Flag any ownership, operational control, or classification changes since prior reporting year with narrative explanation.

### Part 2: Chemical Identification & Threshold Determination

For each reportable chemical, document:

- **Chemical name** — exact EPA EPCRA Section 313 list name
- **CAS number** — definitive identifier
- **Activity type and thresholds:**

| Activity | Definition | Annual Threshold |
|---|---|---|
| Manufacture | Produce, prepare, import, or coincidentally produce as byproduct | 25,000 lbs |
| Process | Prepare after manufacture for distribution in commerce | 25,000 lbs |
| Otherwise use | Any use not manufacturing/processing (cleaning, degreasing, etc.) | 10,000 lbs |

- **Estimation methodology** — actual measurements, mass balance, engineering estimates, or published emission factors
- **Exemptions evaluated:**

| Exemption | Criteria |
|---|---|
| De minimis | <1% concentration (carcinogens: <0.1%) in mixtures/trade name products |
| Article | Formed into specific shape; no release under normal conditions |
| Laboratory | Routine analytical/QC operations only |

For chemical categories: provide aggregation table showing each member compound, CAS number, quantities by activity, and category total.

### Part 3: Environmental Releases

Quantify all releases by medium. Assign EPA range codes (1 = high confidence/direct measurement; higher = increasing uncertainty).

#### Air Emissions
- **Stack/point source** — process vents, storage tank vents, combustion sources
- **Fugitive/non-point** — equipment leaks, building ventilation, material handling
- **Separate routine vs. catastrophic/upset releases**
- Preferred data hierarchy: CEMS > stack tests > mass balance > AP-42 emission factors > engineering judgment

#### Water Releases
- Identify receiving water body
- **Direct discharge** — report NPDES permit number; reconcile with discharge monitoring reports
- **POTW transfers** — report separately with POTW name/location
- Document pretreatment measures and removal efficiency

#### Land Disposal
- Distinguish: on-site landfill, land treatment, surface impoundment, other
- Report RCRA status (Subtitle C vs. D) for each disposal unit
- Explain any changes in disposal practices during reporting year

#### Underground Injection
- Classify well by SDWA class (I or V)
- Provide well location, regulatory status, injected quantity

**For all media:** Provide narrative explanation for significant year-to-year changes (production levels, process changes, new controls, or methodology changes).

### Part 4: Off-Site Transfers

For each receiving facility, document:

| Field | Detail |
|---|---|
| Facility name | Full legal name |
| Address | Complete street address |
| EPA ID | RCRA or other identifier |
| Waste management method | Disposal / Treatment / Recycling / Energy recovery |
| Chemical quantity | Pounds of reported chemical in waste transferred |
| Waste form | Aqueous, non-aqueous, solid, other |

Subtopics to address:
- **Recycling** — on-site vs. off-site; specific methods (solvent recovery, metals reclamation, acid regeneration); closed-loop vs. batch
- **Energy recovery** — on-site combustion devices vs. off-site cement kilns/waste-to-energy
- **Treatment** — method category (incineration, chemical, biological, physical); treatment efficiency; residuals management
- **Disposal** — reconcile with waste manifests and LDR notifications

Verify material balance: all chemical quantities must be accounted for across products, releases, transfers, and on-site management.

### Part 5: Source Reduction & Pollution Prevention

Per Pollution Prevention Act of 1990 requirements:

1. **Process modifications** — equipment upgrades, optimization, automation; quantify waste reduction per unit of production with before/after comparison
2. **Material substitutions** — toxic-to-less-toxic replacements; quantify reduction in use and waste
3. **Operational improvements** — inventory management, training, maintenance, housekeeping; estimate impact from waste tracking/spill records
4. **Recycling maximization** — on-site recovery systems, off-site arrangements, verification that materials are actually recycled
5. **Future plans** — projects in development, feasibility studies, identified barriers (technical, economic, regulatory)

### Part 6: Certification

**Certifying official requirements:**
- Must be owner/operator, senior management official with facility responsibility, or senior official with corporate environmental responsibility
- Identify by full name, title, phone, email

**Required certification language** (do not modify):
> "I hereby certify that I have reviewed the attached documents and that, to the best of my knowledge and belief, the submitted information is true, accurate, and complete. I am aware that there are significant penalties for submitting false information, including the possibility of fines and imprisonment."

**Penalty references:**
- Criminal: 18 U.S.C. § 1001 (false statements to federal agencies)
- Civil: EPCRA § 325 (up to $25,000/day per violation) [VERIFY current penalty amount — may be adjusted for inflation]

**Pre-certification checklist:**
- [ ] Technical review of calculations and data sources
- [ ] Compliance review against 40 CFR Part 372 requirements
- [ ] Management review of business implications and litigation risk
- [ ] Legal counsel review

**Recordkeeping:** Maintain all supporting documentation (inventory records, production data, waste manifests, calculation worksheets, monitoring data) for minimum 3 years from submission date.

## Submission

- **Deadline:** July 1 following the reporting year (covers Jan 1–Dec 31)
- **Method:** EPA TRI-MEweb online reporting system
- **Units:** Pounds per year for all chemical quantities and releases
- **Attachments:** Facility location map with release points, process flow diagrams, supplemental methodology documentation

## Guidelines

- Reconcile all data across EPA databases (Facility Registry Service, RCRA, NPDES, air permits) — inconsistencies trigger regulatory inquiry
- Ensure internal consistency: threshold calculations, release totals, transfer quantities, and material balance must reconcile
- Document estimation methodology for every release pathway — must withstand EPA audit scrutiny
- Do not paraphrase or modify the statutory certification language
- Flag any chemical where threshold status is borderline with conservative analysis
- Note that Form R is publicly disclosed — draft with awareness of community right-to-know and citizen suit exposure under EPCRA
- Include caveats that final certification requires facility management and legal counsel review
