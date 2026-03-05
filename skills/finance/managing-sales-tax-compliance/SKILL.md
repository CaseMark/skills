---
name: managing-sales-tax-compliance
description: Structures sales tax analysis with nexus determination, taxability classification, and exemption management. Use when managing sales tax, determining nexus, or analyzing taxability.
tags:
  - management
  - tax
metadata:
  author: casemark
  practice_areas:
    - Tax Planning
    - Tax Compliance
    - International Tax
  document_types:
    - Management Report
  skill_modes:
    - Management
    - Coordination
---
# Managing Sales Tax Compliance

Structures sales tax analysis across nexus determination, product/service taxability classification, exemption certificate management, and multi-jurisdiction filing coordination.

## When To Use

- Evaluating whether a business has established sales tax nexus in new states or jurisdictions
- Classifying products or services for taxability across multiple jurisdictions
- Auditing exemption certificate files for completeness and validity
- Preparing for or responding to a state sales tax audit
- Onboarding a new entity or product line that triggers sales tax obligations
- Reviewing rate accuracy and filing cadence after legislative or regulatory changes

## Inputs To Gather

- **Entity profile**: Legal entity name, formation state, registered states, NAICS codes, and current sales tax registrations (state tax IDs, filing frequencies)
- **Transaction data**: Revenue by state, customer type (B2B vs. B2C), product/service categories, shipping/delivery methods, and digital vs. tangible goods breakdown
- **Nexus indicators**: Physical presence details (offices, warehouses, employees, inventory), economic nexus thresholds by state (gross revenue and transaction count), affiliate and marketplace relationships
- **Exemption certificates**: Existing certificate inventory, certificate types (resale, government, nonprofit, manufacturing), expiration dates, and missing-certificate log
- **Filing history**: Prior returns, assessed penalties, audit history, voluntary disclosure agreements (VDAs), and any pending disputes

## Workflow

1. **Nexus determination**
   - Map all physical presence touchpoints by jurisdiction (employees, property, inventory consignment, trade show attendance)
   - Compare economic activity against each state's economic nexus thresholds [VERIFY — thresholds vary by state and change frequently; confirm against current statute for each jurisdiction]
   - Flag click-through nexus, affiliate nexus, and marketplace facilitator obligations separately
   - Produce a nexus matrix: jurisdiction × nexus type × triggering factor × effective date

2. **Taxability classification**
   - Categorize each product and service using the destination state's tax code definitions — do not assume uniform treatment across states
   - Identify items requiring specific exemptions or reduced rates (e.g., SaaS taxability, digital goods, food/grocery, clothing) [VERIFY — SaaS and digital goods taxability varies significantly by state]
   - Document bundled transaction rules where tangible and non-tangible components are sold together
   - Cross-reference against the Streamlined Sales Tax (SST) Taxability Information Matrix where the state participates

3. **Exemption certificate management**
   - Audit certificate inventory against active customer accounts: flag missing, expired, or incomplete certificates
   - Validate that certificate types match transaction types (e.g., resale certificate used only for resale purchases, not end-use)
   - Establish renewal tracking cadence — most certificates require renewal every 3–5 years [VERIFY — renewal periods differ by state and certificate type]
   - Document good-faith acceptance standards and reasonable reliance defenses

4. **Filing and remittance coordination**
   - Confirm filing frequency per jurisdiction (monthly, quarterly, annual) and reconcile against registration records
   - Verify rate tables are current, including state, county, city, and special district rates
   - Calculate and apply vendor/seller discounts where available [VERIFY — discount availability and caps vary by state]
   - Track prepayment obligations in applicable states (e.g., Texas, California large-seller prepayments)
   - Reconcile returns against GL tax liability accounts before submission

5. **Ongoing monitoring and risk mitigation**
   - Set alerts for legislative changes affecting nexus thresholds, rate changes, and taxability reclassifications
   - Schedule periodic internal audits (quarterly recommended) comparing collected tax against filed returns
   - Maintain audit-ready documentation: transaction logs, nexus analysis workpapers, exemption certificate files, and correspondence with taxing authorities
   - Evaluate voluntary disclosure agreement (VDA) eligibility for states where nexus was established but registration was delayed

## Output

- **Nexus matrix**: Jurisdiction-by-jurisdiction summary with nexus type, triggering activity, effective date, and registration status
- **Taxability schedule**: Product/service classification by jurisdiction with applicable rates and exemption codes
- **Exemption certificate status report**: Inventory by customer with validity status, gaps, and renewal deadlines
- **Filing calendar**: Consolidated schedule of due dates, filing frequencies, prepayment dates, and estimated liability by jurisdiction
- **Risk register**: Open exposures ranked by estimated liability, including unregistered nexus states, missing certificates, and rate discrepancies
- **Action items**: Prioritized list of registrations to file, certificates to collect, rate table updates, and process improvements

## Quality Checks

- Nexus analysis references current economic nexus thresholds — confirm each state's threshold against the state's department of revenue website or authoritative source
- No taxability classification relies on analogy from another state without explicit verification
- Exemption certificates are validated for correct form, matching jurisdiction, and non-expired status
- Filing frequencies match state registration records and any recent change notices
- All estimated liabilities include supporting calculations with source transaction data
- Items marked [VERIFY] are clearly flagged and not presented as final conclusions
