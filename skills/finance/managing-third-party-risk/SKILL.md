---
name: managing-third-party-risk
description: Structures vendor and third-party risk assessment with due diligence, monitoring, and concentration analysis. Use when assessing vendor risk, conducting third-party due diligence, or monitoring outsourcing risk.
tags:
  - management
  - risk-management
  - risk
metadata:
  author: casemark
  practice_areas:
    - Risk Management
    - Enterprise Risk
    - Market Risk
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Third Party Risk

Structures vendor and third-party risk assessment with due diligence, monitoring, and concentration analysis.

## When To Use

- Onboarding a new vendor, outsourcing partner, or critical service provider
- Performing periodic re-assessment of existing third-party relationships
- Evaluating concentration risk across vendor portfolios (e.g., single cloud provider, dominant counterparty)
- Responding to a third-party incident, control failure, or regulatory finding
- Preparing for regulatory examinations that cover outsourcing and vendor management (OCC, FFIEC, EBA guidelines) [VERIFY jurisdiction-specific rules]

## Inputs To Gather

- **Vendor inventory**: Complete list of third parties including name, service category, contract value, contract term, and business owner
- **Criticality classification**: Whether the vendor supports a critical business function, handles sensitive data, or has customer-facing exposure
- **Due diligence package**: SOC 2 / ISO 27001 reports, financial statements, business continuity plans, insurance certificates, and any prior audit findings
- **Regulatory requirements**: Applicable guidance (e.g., OCC Bulletin 2013-29, DORA, APRA CPS 230) [VERIFY which frameworks apply]
- **Existing risk ratings**: Prior tiering, residual risk scores, and open remediation items
- **Concentration data**: Revenue share per vendor, geographic overlap, technology dependency mapping, fourth-party (subcontractor) disclosures

## Workflow

1. **Tier the vendor population**
   - Assign each third party to a risk tier (Critical / High / Medium / Low) based on data sensitivity, operational dependency, regulatory exposure, and substitutability
   - Critical-tier vendors trigger full due diligence; low-tier vendors require abbreviated assessment

2. **Conduct due diligence**
   - Collect and review SOC reports, financials, BCP/DR plans, and cybersecurity questionnaires
   - Flag gaps: missing reports, qualified audit opinions, declining financial ratios, unresolved findings
   - For critical vendors, assess fourth-party risk — identify key subcontractors and their controls

3. **Score inherent and residual risk**
   - Rate each vendor across dimensions: operational, financial, cyber/information security, regulatory/compliance, reputational, and geopolitical
   - Apply mitigating controls (contractual protections, SLA penalties, escrow, audit rights) to arrive at residual risk
   - Document risk acceptance rationale when residual risk exceeds appetite

4. **Analyze concentration risk**
   - Map vendor dependencies to business lines and geographies
   - Identify single points of failure: one vendor serving multiple critical functions, heavy reliance on one jurisdiction, shared technology stack
   - Calculate concentration metrics (e.g., top-5 vendor spend as % of total outsourced spend)

5. **Build monitoring and escalation framework**
   - Define KRIs per tier: SLA breach rate, financial health triggers, incident frequency, audit finding closure rate
   - Set review cadence: quarterly for critical, annually for high, biennial or event-driven for medium/low
   - Establish escalation paths: who is notified when a KRI breaches threshold, what triggers contract re-negotiation or exit planning

6. **Document and report**
   - Produce a third-party risk register with current tier, residual score, open issues, and next review date
   - Prepare board/committee-level summary: aggregate risk heatmap, concentration dashboard, material exceptions

## Output

- **Third-party risk register**: Vendor name, tier, inherent/residual risk scores, key findings, remediation status, next review date
- **Concentration analysis**: Dashboard showing spend concentration, geographic concentration, and fourth-party overlap
- **Due diligence summary per vendor**: Controls assessment, gap list, and recommended mitigants
- **Executive risk report**: Heatmap of vendor risk by category, trend vs. prior period, material exceptions requiring escalation
- **Monitoring plan**: KRI definitions, thresholds, review cadence, and escalation matrix

## Quality Checks

- Every critical-tier vendor has a completed due diligence file dated within the applicable review cycle [VERIFY required frequency per regulation]
- Concentration thresholds are defined and tested — no single vendor exceeds the board-approved limit without documented risk acceptance
- Risk scores use a consistent methodology across all vendors; scoring criteria are documented and repeatable
- Fourth-party dependencies are identified for all critical vendors; gaps are flagged rather than omitted
- Regulatory mapping is current — confirm the applicable supervisory guidance matches the entity's charter, jurisdiction, and license type [VERIFY]
- All open remediation items have assigned owners, target dates, and status tracking
- Mark any data point sourced from vendor self-attestation (vs. independent audit) with [VERIFY]
