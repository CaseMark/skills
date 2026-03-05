---
name: managing-correspondent-banking
description: Structures correspondent banking analysis with relationship assessment, risk evaluation, and regulatory requirements. Use when managing correspondent relationships, evaluating partner banks, or assessing correspondent risk.
tags:
  - management
  - commercial-banking
  - regulatory
  - risk
metadata:
  author: casemark
  practice_areas:
    - Commercial Banking
    - Trade Finance
    - Lending
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Correspondent Banking

## When To Use

- Onboarding a new correspondent bank or evaluating an existing relationship for renewal
- Conducting periodic risk reassessment of correspondent banking partners
- Responding to regulatory inquiries or exam findings related to correspondent relationships
- Assessing whether a correspondent's risk profile has materially changed (sanctions exposure, adverse media, jurisdiction risk)
- Preparing management reporting on the correspondent banking portfolio

## Inputs To Gather

- **Correspondent profile**: Legal name, LEI, SWIFT/BIC, domicile jurisdiction, ownership structure, and organizational chart
- **Relationship scope**: Services used (clearing, FX, trade finance, cash management, nostro/vostro accounts), transaction volumes, and revenue attribution
- **Due diligence package**: Most recent KYC/CDD file, audited financials, regulatory licenses, AML/CFT program documentation, and Wolfsberg questionnaire responses
- **Risk indicators**: FATF mutual evaluation of correspondent's jurisdiction, Transparency International CPI score, sanctions screening results, adverse media findings, and prior SARs filed on the relationship
- **Regulatory context**: Applicable guidance (e.g., BCBS guidelines on correspondent banking, FinCEN advisories, local regulator expectations) [VERIFY — requirements vary by home jurisdiction]
- **Historical performance**: Payment processing SLAs, error/rejection rates, prior compliance incidents, and relationship tenure

## Workflow

1. **Map the relationship structure**
   - Identify all accounts (nostro, vostro, mirror) and the services each supports
   - Document the payment corridors and currencies involved
   - Flag any nested or downstream correspondent access (payable-through accounts, respondent banks using the correspondent as an intermediary)

2. **Perform risk assessment**
   - Score the correspondent across standard risk dimensions: jurisdiction risk, product/service risk, customer-type risk, transaction risk, and sanctions exposure
   - Apply the institution's correspondent banking risk matrix to assign an overall risk tier (e.g., low / medium / high / prohibited)
   - Identify red flags: opaque ownership, jurisdictions on FATF grey/black lists, history of enforcement actions, or inability to provide requested documentation [VERIFY — risk matrix categories per internal policy]

3. **Evaluate due diligence adequacy**
   - Confirm CDD/EDD documentation is current (typically refreshed every 1–3 years based on risk tier)
   - Verify the correspondent's AML/CFT program covers: customer identification, transaction monitoring, sanctions screening, and SAR filing obligations
   - Assess whether the correspondent conducts its own due diligence on downstream respondents (to mitigate "nesting" risk)
   - Review Wolfsberg questionnaire or equivalent for completeness and consistency with independent findings

4. **Analyze financial and operational performance**
   - Review correspondent's capital adequacy, liquidity ratios, and credit ratings
   - Benchmark transaction processing metrics (STP rates, rejection rates, cut-off times) against SLA targets
   - Calculate relationship profitability: fee income vs. operational cost, balance benefits, and ancillary revenue

5. **Prepare management report**
   - Summarize risk tier, key findings, and any open remediation items
   - Include a recommendation: maintain, enhance monitoring, restrict services, or terminate
   - Document escalation triggers that would require interim reassessment (e.g., sanctions designation, material adverse event, regulatory action against correspondent)

## Output

The deliverable is a **Correspondent Banking Relationship Report** containing:

- **Executive summary** — Risk tier, recommendation, and key action items
- **Relationship overview** — Correspondent profile, services, volumes, and revenue
- **Risk assessment matrix** — Scored dimensions with supporting rationale
- **Due diligence status** — Documentation inventory, gaps, and next renewal dates
- **Financial and operational analysis** — Credit quality indicators and SLA performance
- **Recommendations and conditions** — Maintain/restrict/terminate with specific conditions (e.g., enhanced transaction monitoring, volume caps, geographic restrictions)
- **Escalation triggers** — Events requiring immediate reassessment outside the regular cycle

## Quality Checks

- Confirm all risk scoring dimensions align with the institution's approved correspondent banking risk framework [VERIFY — internal policy reference]
- Verify sanctions screening was run against current OFAC SDN, EU Consolidated List, UN Sanctions List, and any locally mandated lists [VERIFY — applicable lists per jurisdiction]
- Ensure nested/downstream respondent risk is explicitly addressed, not just direct correspondent risk
- Cross-check adverse media findings against at least two independent sources
- Validate that the recommendation is consistent with the assigned risk tier and any regulatory constraints
- Confirm revenue and volume data reconciles to core banking system records
- Flag any correspondent where CDD refresh is overdue or documentation requests remain outstanding beyond 60 days
