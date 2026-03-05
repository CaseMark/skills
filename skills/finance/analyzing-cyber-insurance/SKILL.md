---
name: analyzing-cyber-insurance
description: Structures cyber insurance evaluation with coverage assessment, limit adequacy, and claims scenario analysis. Use when evaluating cyber coverage, analyzing policy terms, or assessing cyber insurance adequacy.
tags:
  - analysis
  - insurance
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Insurance
    - Actuarial Science
    - Reinsurance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Cyber Insurance

## When To Use

- Evaluating a new or renewal cyber insurance policy for coverage adequacy
- Comparing competing cyber policy quotes across carriers
- Assessing whether existing cyber limits align with the insured's risk profile
- Running claims scenarios to stress-test policy response under breach events
- Reviewing policy language for sublimit traps, retroactive date gaps, or exclusion pitfalls
- Advising on tower structure or excess placement for large cyber programs

## Inputs To Gather

- **Policy documents**: Full policy form including declarations page, endorsements, and any manuscript amendments
- **Insured profile**: Industry vertical, annual revenue, record count (PII/PHI/PCI), geographic footprint, and IT infrastructure summary
- **Loss history**: Prior cyber claims, near-misses, and any regulatory actions or litigation
- **Risk assessment data**: Most recent penetration test results, SOC 2 or ISO 27001 status, incident response plan maturity
- **Program structure**: Primary and excess layers, attachment points, carrier line-up, and any shared/quota arrangements
- **Benchmark data**: Peer company limits, industry loss trends (e.g., Advisen, NetDiligence claims studies), and broker market intelligence
- **Coverage requirements**: Contractual insurance obligations, regulatory mandates, and board risk appetite statements

## Workflow

1. **Map coverage grants against risk exposures**
   - Parse insuring agreements for first-party (business interruption, data restoration, extortion, forensic costs, notification/credit monitoring, crisis management/PR) and third-party (network security liability, privacy liability, regulatory defense and penalties, media liability, PCI-DSS fines) coverages
   - Flag any coverage grants that are absent given the insured's exposure profile
   - Note whether coverage triggers are occurrence-based, claims-made, or claims-made-and-reported, and confirm retroactive date adequacy

2. **Analyze key policy terms and conditions**
   - Identify sublimits that effectively cap high-frequency loss categories (e.g., ransomware/extortion sublimit, dependent business interruption sublimit, voluntary notification sublimit)
   - Review waiting period / hours clause for business interruption — compare against insured's actual RTO expectations
   - Examine consent requirements for breach counsel, forensic vendors, and ransom payments [VERIFY carrier panel requirements]
   - Assess war/terrorism and nation-state exclusions — note whether carve-backs for cyberterrorism exist
   - Review infrastructure/cloud exclusion wording — confirm coverage extends to hosted environments (AWS, Azure, SaaS dependencies)
   - Check prior acts, pending/prior litigation, and prior knowledge exclusions for gaps

3. **Evaluate limit adequacy**
   - Model loss scenarios across severity tiers:
     - **Low**: Single employee credential compromise, limited data exposure (~5K records)
     - **Medium**: Ransomware event with 72-hour operational downtime, partial data exfiltration (~500K records)
     - **High**: Systemic breach with regulatory investigation across multiple jurisdictions, class action exposure (~5M+ records)
   - For each scenario, stack estimated costs: forensic investigation, notification, credit monitoring, legal defense, regulatory fines, business interruption loss, and reputational/crisis management spend
   - Compare modeled losses against aggregate and per-occurrence limits, noting erosion risk from sublimited coverages
   - Benchmark limits against industry peers by revenue band and data volume [VERIFY current benchmark sources]

4. **Assess program structure and pricing**
   - If tower program: evaluate attachment points, follow-form consistency across excess layers, and any differences in conditions (DIC) or differences in limits (DIL) issues
   - Flag anti-stacking provisions, batch/related-claims clauses, and interrelated wrongful acts definitions that could consolidate multiple events into a single limit
   - Compare premium-per-million across layers and against market benchmarks
   - Identify retention (SIR/deductible) appropriateness relative to the insured's balance sheet and incident frequency

5. **Review exclusions and conditions for coverage disputes risk**
   - Catalog exclusions most likely to generate coverage disputes: failure to maintain minimum security standards, criminal/fraudulent acts, contractual liability, bodily injury/property damage, unencrypted device exclusions
   - Assess notice/reporting requirements — identify strict compliance conditions that could void coverage
   - Note any cooperation and subrogation obligations that impose operational burdens during active incidents

## Output

Structure the analysis report with the following sections:

- **Executive Summary**: One-page overview of coverage adequacy rating (Strong / Adequate / Gaps Identified / Inadequate), top three findings, and priority recommendations
- **Coverage Matrix**: Table mapping each insuring agreement to the insured's risk exposures, noting sublimits, retentions, and waiting periods per coverage part
- **Limit Adequacy Analysis**: Scenario-based loss modeling results with comparison to purchased limits and benchmark data
- **Terms and Conditions Review**: Annotated list of policy provisions with risk ratings (Green / Yellow / Red) based on potential to restrict or deny coverage
- **Exclusion Risk Assessment**: Ranked list of exclusions by likelihood and severity of coverage dispute
- **Program Structure Evaluation**: Visual or tabular representation of tower structure with commentary on layering efficiency and pricing
- **Recommendations**: Prioritized action items — coverage enhancements to negotiate, limit increases to pursue, endorsements to request, and alternative market options

## Quality Checks

- Every sublimit, retention, and waiting period from the declarations page is accounted for in the coverage matrix
- Loss scenarios use defensible cost assumptions with sources cited (NetDiligence, Ponemon/IBM, Verizon DBIR) [VERIFY latest study year and figures]
- Exclusion analysis references specific policy section numbers and endorsement form numbers
- Retroactive date, extended reporting period (tail), and policy period are confirmed and noted
- All jurisdictional regulatory exposure is identified — GDPR, CCPA/CPRA, HIPAA, state breach notification statutes as applicable [VERIFY relevant jurisdictions for insured's footprint]
- Recommendations distinguish between items achievable in current negotiation vs. next renewal cycle
- Report flags any areas where actuarial loss modeling or independent broker review is warranted beyond the scope of this analysis
