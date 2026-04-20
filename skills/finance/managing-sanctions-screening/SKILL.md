---
name: managing-sanctions-screening
language: en
description: Structures OFAC and global sanctions screening with match investigation and escalation protocols. Use when screening for sanctions, investigating potential matches, or managing sanctions compliance.
tags:
  - management
  - financial-compliance
  - compliance
metadata:
  author: casemark
  practice_areas:
    - Regulatory Compliance
    - Financial Regulation
    - Compliance
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Sanctions Screening

## When To Use

- Setting up or auditing a sanctions screening program across OFAC SDN, Consolidated, Sectoral Sanctions, and non-SDN lists
- Investigating potential matches (hits) from automated screening against customer, counterparty, or transaction data
- Building or refining escalation protocols for true matches, partial matches, and false positives
- Coordinating screening across multiple sanctions regimes (OFAC, EU, UK OFSI, UN, OFAC secondary sanctions) [VERIFY jurisdiction-specific list requirements]
- Preparing management reports on screening volumes, match rates, disposition outcomes, and regulatory exam readiness

## Inputs To Gather

- **Screening universe**: Customer/counterparty database, transaction records, payment messages (MT103/MT202, ISO 20022), or trade finance documents subject to screening
- **Sanctions lists in scope**: OFAC SDN, Sectoral Sanctions Identifications (SSI), Non-SDN lists (e.g., CAPTA, NS-MBS, NS-PLC), EU Consolidated List, UK Sanctions List, UN Consolidated List [VERIFY which lists apply based on jurisdictional nexus]
- **Screening tool and configuration**: Vendor platform (e.g., Fircosoft, Actimize, LexisNexis), fuzzy matching thresholds, filter tuning parameters, and whitelisting/exclusion rules
- **Match investigation files**: Alert details including hit entity name, alias data, ID numbers, country of origin, screening score, and any prior disposition history
- **Risk tolerance and escalation matrix**: Institutional risk appetite, BSA/AML officer designation, escalation thresholds for OFAC vs. non-OFAC matches, and blocking/rejecting authority delegation
- **Regulatory guidance**: Most recent OFAC FAQs, enforcement actions, and any institution-specific consent orders or MRAs from examiners [VERIFY current OFAC guidance vintage]

## Workflow

1. **Define screening scope and list coverage**
   - Map all touchpoints requiring screening: onboarding (KYC/CDD), recurring batch screening, real-time transaction filtering, and beneficial ownership screening
   - Confirm which sanctions lists are screened at each touchpoint and the refresh frequency (OFAC publishes updates on irregular schedules; EU/UK have separate cadences) [VERIFY update frequency requirements]
   - Document interdiction points: where in the transaction lifecycle does a hit trigger a hold, block, or reject

2. **Assess screening tool calibration**
   - Review fuzzy matching thresholds and scoring algorithms — overly tight thresholds miss transliteration variants; overly loose thresholds generate excessive false positives
   - Evaluate filter tuning: are common false-positive names (e.g., "Ali," "Mohammed," geographic terms) handled via whitelisting, exclusion logic, or manual review?
   - Test screening against known SDN entries and known non-matches to validate detection rates
   - Document match scoring methodology and the rationale for current threshold settings

3. **Investigate and disposition alerts**
   - For each alert, compare hit entity data against sanctions list entry: full name, aliases, date of birth, nationality, passport/ID numbers, and vessel/aircraft identifiers where applicable
   - Classify disposition:
     - **True match**: Entity matches SDN or blocked-persons list entry → initiate blocking, file initial OFAC report within 10 business days [VERIFY current OFAC reporting deadline], notify BSA/AML officer
     - **Partial/possible match**: Insufficient data to confirm or deny → escalate for enhanced due diligence, request additional documentation from relationship manager or counterparty
     - **False positive**: Sufficient distinguishing data to rule out match → document reasoning, approve for processing, update whitelist if recurring
   - Record investigation steps, data sources consulted, and analyst rationale in the case management system

4. **Execute blocking and reporting obligations**
   - For confirmed SDN matches: block the property/transaction, do not release without OFAC license [VERIFY specific license requirements]
   - File blocked property report with OFAC within 10 business days of blocking
   - For rejected transactions (non-blocked): file reject report with OFAC annually [VERIFY annual reject reporting requirements]
   - Coordinate with legal counsel on voluntary self-disclosures if a sanctions violation is identified
   - Maintain a 5-year record retention period for all blocking actions and investigation files [VERIFY retention period per 31 CFR Part 501]

5. **Report and monitor program health**
   - Track key metrics: total screening volume, alert rate, false positive rate, true match rate, average disposition time, and aging of open alerts
   - Prepare management reports for BSA/AML committee showing trends, notable matches, and any changes to list coverage or tool calibration
   - Document any OFAC enforcement actions or guidance updates that affect the screening program
   - Flag screening gaps: new product lines, new geographies, or counterparty types not yet integrated into the screening workflow

## Output

- **Screening program summary**: Scope of coverage, lists screened, screening touchpoints, tool configuration, and refresh cadence
- **Alert investigation log**: Structured record of each alert with entity comparison, disposition decision (true match / partial / false positive), analyst name, and supporting documentation
- **Blocking/rejection report**: Details of any blocked property or rejected transactions, OFAC report filing status, and follow-up actions
- **Management dashboard**: Metrics on screening volume, alert rates, disposition outcomes, average investigation time, and program risk indicators
- **Remediation tracker**: Open items such as filter tuning adjustments, whitelist updates, coverage gaps, and regulatory exam findings requiring corrective action

## Quality Checks

- Every true match disposition includes documented comparison against at least two identifying data points (name alone is insufficient)
- False positive dispositions articulate specific distinguishing factors (e.g., different date of birth, different country of nationality, confirmed unrelated entity)
- Blocking reports are filed within OFAC's 10-business-day deadline [VERIFY current deadline]
- Screening list versions are current — confirm the SDN list publication date matches the most recent OFAC update
- Fuzzy matching thresholds are documented with business justification; any changes to thresholds are approved by the BSA/AML officer
- All [VERIFY] items are resolved against current OFAC regulations, institution-specific policies, and applicable non-US sanctions regimes before finalizing
