---
name: analyzing-biodiversity-risk
description: Structures biodiversity risk assessment with nature-related dependency mapping and TNFD alignment. Use when analyzing biodiversity risk, mapping nature dependencies, or implementing TNFD disclosure.
tags:
  - analysis
  - sustainable-finance
  - risk
metadata:
  author: casemark
  practice_areas:
    - ESG
    - Impact Investing
    - Sustainable Finance
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Biodiversity Risk

## When To Use

- Evaluating a portfolio company or asset for nature-related financial risks (physical, transition, systemic)
- Mapping dependencies and impacts on ecosystem services for TNFD-aligned disclosure
- Screening investments against biodiversity loss thresholds or deforestation-free commitments
- Preparing biodiversity risk sections for ESG due diligence, impact reports, or fund-level disclosures
- Responding to LP or regulatory requests for nature-related risk data (e.g., EU SFDR Article 8/9, CSRD E4)

## Inputs To Gather

- **Entity profile**: Company name, sector (NACE/GICS), geographic footprint of operations and supply chain
- **Financial exposure**: AUM allocation, position size, or loan exposure to the entity
- **Existing disclosures**: Any prior ESG reports, CDP responses, sustainability policies, or TNFD pilot disclosures
- **Location data**: Facility coordinates, sourcing regions, concession boundaries (for proximity-to-sensitive-area analysis)
- **Sector materiality context**: Which ecosystem services the sector depends on (e.g., pollination for agriculture, water filtration for beverages, genetic resources for pharma)
- **Framework requirements**: Whether output must align with TNFD LEAP, SBTN, EU Taxonomy biodiversity criteria, or internal proprietary framework

## Workflow

1. **Scope the assessment**
   - Define the entity boundary (direct operations, upstream supply chain, downstream use, or full value chain)
   - Confirm which TNFD pillar applies: Locate, Evaluate, Assess, or Prepare
   - Identify the target audience (fund risk committee, LP reporting, regulatory filing)

2. **Map nature dependencies and impacts**
   - List ecosystem services the entity depends on using ENCORE or similar classification (provisioning, regulating, cultural)
   - Identify nature impacts: land-use change, pollution, resource exploitation, invasive species introduction, climate-driven habitat loss
   - Rate dependency severity (high/medium/low) based on substitutability and operational criticality
   - Rate impact severity based on scale, irreversibility, and proximity to Key Biodiversity Areas (KBAs) or protected areas [VERIFY against IBAT or Protected Planet data]

3. **Assess financial materiality**
   - Translate nature dependencies into financial risk channels:
     - **Physical risk**: Supply disruption from ecosystem degradation (e.g., pollinator collapse, water scarcity)
     - **Transition risk**: Regulatory costs from emerging biodiversity regulation (EU Deforestation Regulation, Kunming-Montreal GBF national action plans) [VERIFY jurisdiction-specific regulations]
     - **Systemic risk**: Sector-wide repricing if tipping points are crossed
     - **Litigation risk**: Liability from environmental damage claims or failure to disclose
   - Quantify where possible: estimated cost of supply chain disruption, compliance capex, stranded asset write-downs
   - Flag where data gaps prevent quantification and note proxy approaches used

4. **Evaluate against frameworks and thresholds**
   - Score alignment with TNFD recommended disclosures (Governance, Strategy, Risk Management, Metrics & Targets)
   - Check against Science Based Targets for Nature (SBTN) if the entity has committed [VERIFY target status]
   - Assess compliance with EU Taxonomy "Do No Significant Harm" biodiversity criteria if applicable [VERIFY taxonomy delegated act version]
   - Compare to sector benchmarks (e.g., Forest 500 rankings for commodity-linked sectors, FAIRR for protein sector)

5. **Synthesize and recommend**
   - Produce a risk rating (critical / high / moderate / low) with rationale
   - Identify top 3-5 biodiversity risk drivers ranked by financial materiality
   - Recommend engagement priorities or risk mitigation actions (e.g., require deforestation-free sourcing policy, request TNFD pilot disclosure, set nature-positive KPIs)
   - Flag data gaps that should be closed before next review cycle

## Output

Structure the analysis report with the following sections:

- **Executive Summary**: One-paragraph risk rating with key drivers
- **Entity & Sector Context**: Business description, sector materiality profile, geographic exposure
- **Nature Dependency & Impact Matrix**: Table mapping ecosystem services to dependency/impact ratings with evidence
- **Financial Risk Assessment**: Physical, transition, systemic, and litigation risk channels with estimated magnitude
- **Framework Alignment**: TNFD LEAP progress, SBTN status, regulatory compliance gaps
- **Recommendations**: Prioritized actions for risk mitigation, engagement, or portfolio adjustment
- **Data Gaps & Limitations**: Explicit list of missing data, proxy assumptions, and confidence levels

## Quality Checks

- Every dependency and impact rating is supported by a cited source or explicit assumption flagged with [VERIFY]
- Financial risk channels connect clearly from ecological mechanism to balance-sheet or cash-flow impact — no orphan ecological facts without financial translation
- Framework alignment assessments reference specific disclosure elements (e.g., TNFD Strategy B, Metric C3) rather than vague compliance statements
- Location-sensitive claims (proximity to KBAs, protected areas, high-deforestation fronts) are cross-referenced against spatial data [VERIFY using IBAT, Global Forest Watch, or equivalent]
- Sector classifications and materiality ratings are consistent with ENCORE, SASB, or the stated methodology throughout
- Recommendations are specific and actionable — avoid generic "improve biodiversity management" without concrete next steps
