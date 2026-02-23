---
name: npdes-permit-application
description: Drafts comprehensive NPDES Permit Applications under the Clean Water Act (33 U.S.C. § 1342) for facilities discharging pollutants into U.S. waters. Covers initial, renewal, and modification applications including discharge characterization, treatment system descriptions, water quality analysis, monitoring programs, and certification requirements. Incorporates EPA and state-delegated program requirements, effluent limitation guidelines, and Section 303(d) TMDL compliance. Use when drafting NPDES permit applications, discharge permits, point source authorizations, or Clean Water Act compliance filings.
tags:
  - drafting
  - regulatory
---

# NPDES Permit Application

Drafts a complete National Pollutant Discharge Elimination System permit application suitable for submission to EPA or an authorized state agency.

## Prerequisites

1. **Facility identification** — legal entity name, FEIN, SIC/NAICS code, geographic coordinates (decimal degrees, 4+ places)
2. **Existing permit data** — current permit number, expiration date, compliance history, NOVs, consent orders
3. **Discharge monitoring reports** — minimum 1 year (preferably 3 years) of historical DMR data
4. **Site plans & process flow diagrams** — outfall locations, treatment system layout, water balance
5. **Receiving water information** — water body name, segment ID, state classification, designated uses, 303(d) status
6. **Treatment system specifications** — unit operations, design capacities, operating parameters
7. **Permitting authority confirmation** — EPA Regional Office or delegated state agency, applicable forms (EPA Form 1 / Form 2 series or state equivalents), fee schedule, submission portal

## Output Structure

### Section 1: Applicant & Facility Information

| Field | Requirement |
|-------|-------------|
| Legal name | Exactly as registered with state corporate authorities |
| Owner vs. operator | Identify both if different; describe relationship per 40 CFR § 122.22 |
| Location | Street address + lat/long (decimal degrees, ≥4 places) |
| Receiving water | Official name, segment ID, state WQ classification, designated uses |
| SIC/NAICS code | Determines applicable effluent limitation guidelines (40 CFR Parts 405–471) |
| Existing permit | Number, expiration, compliance history, modifications since issuance |

### Section 2: Discharge Characterization

For each outfall, provide:

- **Outfall ID** — unique identifier with geographic coordinates
- **Discharge type** — continuous vs. intermittent; describe triggers for intermittent discharges
- **Flow data** — average daily flow and maximum daily flow (gpd or mgd); seasonal variations
- **Water balance diagram** — inputs, internal reuse, distribution among outfalls

**Pollutant Data Table** (per outfall):

| Parameter | Method (40 CFR 136) | Detection Limit | n Samples | Min | Max | Avg | Mass (lb/day) |
|-----------|---------------------|-----------------|-----------|-----|-----|-----|---------------|
| BOD | | | | | | | |
| TSS | | | | | | | |
| pH | | | | | | | |
| Fecal coliform | | | | | | | |
| Oil & grease | | | | | | | |
| Heavy metals (Cd, Cr, Cu, Pb, Hg, Ni, Ag, Zn) | | | | | | | |
| Organics (per 40 CFR 401 toxic list) | | | | | | | |
| Industry-specific parameters | | | | | | | |

Cross-reference all data to lab reports, site plans, and process flow diagrams attached to the application.

### Section 3: Treatment Systems & Pollution Prevention

**Process flow diagram requirements:**
- Trace wastewater from generation → each treatment unit → final discharge
- Include all recycle streams, bypass provisions, emergency overflows
- Label each component with unique ID, design flow rate, retention time

**Treatment unit descriptions** — for each unit, provide:

| Treatment Type | Required Details |
|----------------|-----------------|
| Physical (screening, sedimentation, filtration) | Dimensions, hydraulic loading rates, removal efficiencies |
| Biological (activated sludge, trickling filter, lagoon) | Reactor volume, aeration capacity, MLSS, F/M ratio, sludge age |
| Chemical (coagulation, precipitation, disinfection) | Chemicals used, dosing rates, reaction times |
| All units | Design capacity vs. current loading |

**Technology-based compliance demonstration:**
- Existing sources → BPT or BCT compliance (40 CFR industry-specific parts)
- New sources → NSPS / BADCT compliance
- Cite specific ELG sections supporting treatment approach

**Pollution prevention measures:**
- BMPs: housekeeping, preventive maintenance, material substitution, process modifications
- Employee training program: frequency, topics, documentation
- System reliability: backup equipment, redundancy, emergency storage, upset response procedures

### Section 4: Water Quality-Based Analysis

1. **Identify applicable WQ standards** — numeric criteria, narrative criteria, antidegradation provisions
2. **Reasonable potential analysis** — compare max projected discharge concentration to WQ criterion at critical low flow (7Q10)
3. **Mixing zone** (if authorized) — justify dimensions; describe receiving water characteristics, outfall configuration, diffuser design; reference modeling or dye studies
4. **303(d) impaired waters** — demonstrate consistency with TMDL wasteload allocation if established; address antidegradation policy if no TMDL exists

### Section 5: Monitoring, Recordkeeping & Reporting

**Monitoring program** (per parameter, per outfall):

| Element | Specification |
|---------|---------------|
| Frequency | Meet or exceed 40 CFR § 122.44(i) minimums |
| Analytical methods | EPA-approved per 40 CFR Part 136; detection limits sufficient for permit limits |
| Sample type | Grab or composite (time- or flow-proportional); specify interval |
| Sample location | Accessible, representative, upstream of any mixing |

**QA/QC requirements:**
- Certified/accredited laboratory
- Field blanks, trip blanks, duplicates, matrix spikes
- Data validation before regulatory submission

**Reporting obligations:**

| Report | Frequency | Method |
|--------|-----------|--------|
| DMRs | Monthly or quarterly | NetDMR or state portal |
| Noncompliance (health/environment endangerment) | Immediate oral + 5-day written | Per 40 CFR § 122.41(l)(6) |
| Record retention | ≥3 years (or longer per state/enforcement requirements) | Per 40 CFR § 122.41(j)(2) |

### Section 6: Certification & Signatory Authority

**Signatory requirements (40 CFR § 122.22):**

| Entity Type | Authorized Signatory |
|-------------|---------------------|
| Corporation | Responsible corporate officer (president, VP of principal function, or equivalent) |
| Partnership | General partner |
| Sole proprietorship | Proprietor |

**Required elements:**
- [ ] Certification statement: signatory personally examined information, believes it true, accurate, complete
- [ ] 18 U.S.C. § 1001 acknowledgment (false statements = federal crime)
- [ ] Printed name, title, date, contact information
- [ ] Authorized representative designation (40 CFR § 122.22(b)) if applicable — must specify scope and duration; permit applications and noncompliance reports cannot be delegated

### Section 7: Supporting Documentation

**Attachment checklist:**

- [ ] Topographic map (1:24,000) — facility, outfalls, receiving water ≥1 mile downstream, sensitive receptors
- [ ] Site plans (PE/surveyor prepared) — buildings, collection systems, treatment facilities, discharge points
- [ ] Process flow diagrams — production and treatment processes with flow rates and operating parameters
- [ ] Mass balance calculations
- [ ] Historical DMR data (tabular with summary statistics)
- [ ] Laboratory analytical reports
- [ ] Application fee payment confirmation
- [ ] Public notice documentation (if required by state)
- [ ] Cross-regulatory references (RCRA, air permits, TSCA)
- [ ] Enforcement action documentation and compliance status
- [ ] Attachment index with designation, description, page count, and cross-reference to application section

## Guidelines

1. **Completeness is critical** — incomplete applications are the primary cause of delays; the submission must allow tentative determination without substantial additional information requests
2. **Jurisdiction verification** — confirm whether state has NPDES primacy; use state-specific forms where they supplement or replace EPA Forms 1/2
3. **Units** — flow in gpd/mgd, concentrations in mg/L or µg/L, mass in lb/day; three significant figures
4. **Citations** — cite specific CFR sections (e.g., "40 CFR § 122.44(d)(1)(i)") and U.S.C. provisions throughout
5. **Format** — text-searchable PDF with bookmarks for electronic submission; respect portal file size limits
6. **Environmental justice** — if facility is in or near minority/low-income communities, address meaningful community input opportunities
7. **Internal consistency** — discharge volumes, pollutant concentrations, and treatment capacities must be consistent across all sections
8. **Do not** fabricate monitoring data, analytical results, or compliance history
9. **Mark all unverified statutory citations** with [VERIFY] — especially state-specific provisions
