---
name: managing-vendor-due-diligence-compliance
language: en
description: Structures regulatory vendor due diligence with risk assessment and ongoing monitoring requirements. Use when conducting vendor DD, assessing outsourcing risk, or managing third-party compliance.
tags:
  - management
  - financial-compliance
  - compliance
  - regulatory
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
# Managing Vendor Due Diligence Compliance

## When To Use

- Onboarding a new third-party vendor that will access customer data, perform regulated functions, or handle material outsourced activities
- Conducting periodic reassessment of existing vendor relationships (annual review cycles, contract renewals)
- Responding to a regulatory exam finding or audit deficiency related to third-party risk management
- Evaluating whether a vendor qualifies as "critical" or "significant" under applicable regulatory guidance (OCC Bulletin 2013-29, FDIC FIL-44-2008, Federal Reserve SR 13-19/CA 13-21, or Interagency Guidance on Third-Party Relationships) [VERIFY applicable framework for institution type]
- Assessing outsourcing arrangements for compliance with DORA, EBA Guidelines on Outsourcing, or equivalent non-US regimes [VERIFY jurisdiction]

## Inputs To Gather

- **Vendor identification**: Legal entity name, jurisdiction of incorporation, ultimate beneficial ownership, DUNS/LEI numbers
- **Service description**: Exact functions being performed, whether the activity is customer-facing, and whether it involves access to NPI/PII or regulated data
- **Criticality classification criteria**: Institution's internal tiering framework (critical, high, moderate, low) and the factors driving classification (revenue impact, regulatory exposure, data sensitivity, substitutability)
- **Existing documentation**: Prior DD reports, SOC 2 Type II or equivalent audit reports, financial statements, insurance certificates, BCP/DR plans, information security policies
- **Regulatory context**: Which regulators oversee the institution, any open MRAs/MRIAs related to vendor management, consent order requirements
- **Contract terms**: Current or proposed SLA metrics, termination and transition provisions, subcontracting restrictions, audit rights, data handling obligations

## Workflow

1. **Classify vendor risk tier**
   - Apply the institution's criticality matrix against the service scope
   - Determine whether the vendor performs a "critical activity" or "significant outsourcing" under applicable guidance [VERIFY definition thresholds]
   - Document the rationale for the assigned tier — this drives the depth of remaining DD steps

2. **Conduct financial and operational due diligence**
   - Review audited financial statements (minimum 2 years) for solvency indicators, going-concern qualifications, and material contingencies
   - Obtain and evaluate SOC 2 Type II report (or SOC 1 if financially relevant processing); flag any qualified opinions or exceptions
   - Assess BCP/DR capabilities: RTO/RPO commitments, testing frequency, last test results
   - For critical vendors: request on-site or virtual assessment if audit reports are insufficient

3. **Assess regulatory and compliance posture**
   - Confirm vendor holds required licenses, registrations, or certifications for the services provided [VERIFY by jurisdiction and service type]
   - Screen against OFAC SDN list, BIS Entity List, and other applicable sanctions/debarment databases
   - Review vendor's own compliance program: AML/BSA policies (if applicable), privacy program, information security framework (SOC, ISO 27001, NIST CSF alignment)
   - Check litigation history and regulatory enforcement actions via PACER, state AG databases, and industry-specific registries

4. **Evaluate information security and data privacy**
   - Map data flows: what data the vendor receives, stores, processes, and transmits
   - Review vendor's incident response plan and breach notification commitments against contractual and statutory requirements (state breach notification laws, GLBA Safeguards Rule, GDPR Art. 33-34 if applicable) [VERIFY applicable data privacy regime]
   - Assess fourth-party (subcontractor) risk: identify material subcontractors and confirm oversight controls
   - Validate encryption standards, access controls, and penetration testing cadence

5. **Establish ongoing monitoring framework**
   - Define monitoring frequency by risk tier (critical: quarterly metrics + annual full reassessment; high: semi-annual review; moderate/low: annual attestation)
   - Specify trigger events requiring off-cycle reassessment: material breaches, financial deterioration, M&A activity, regulatory action against vendor, significant service failures
   - Set SLA performance tracking mechanisms and escalation thresholds
   - Schedule next periodic review date and assign responsible owner

6. **Compile DD report and recommendations**
   - Summarize findings by risk category (financial, operational, regulatory, information security, reputational)
   - Assign residual risk rating after accounting for mitigating controls and contract protections
   - Identify open items requiring remediation, with responsible parties and target dates
   - State approval recommendation: approve, approve with conditions, or reject

## Output

The final deliverable is a **Vendor Due Diligence Report** containing:

- **Executive summary**: Vendor name, service description, risk tier, overall residual risk rating, and approval recommendation
- **Criticality classification**: Tier assignment with supporting rationale
- **DD findings matrix**: Organized by risk domain (financial, operational, regulatory, infosec, reputational) with finding severity (satisfactory / needs improvement / unsatisfactory)
- **Open items tracker**: Each item with owner, due date, and status
- **Ongoing monitoring schedule**: Frequency, metrics, trigger events, and responsible parties
- **Appendices**: Supporting documents reviewed, screening results, and any vendor-provided certifications

## Quality Checks

- Confirm the criticality classification aligns with the institution's board-approved third-party risk management policy
- Verify that all required screening databases were checked and results documented with date stamps
- Ensure contract terms (audit rights, termination provisions, data handling) are cross-referenced against DD findings — flag gaps
- Validate that the monitoring cadence meets or exceeds the minimum frequency required by the institution's primary regulator [VERIFY regulatory minimum]
- Check that fourth-party/subcontractor risks are addressed, not just direct vendor risks
- Confirm that the residual risk rating accounts for both inherent risk and the effectiveness of mitigating controls
- Mark any data point sourced from vendor self-attestation (rather than independent verification) with [VERIFY]
