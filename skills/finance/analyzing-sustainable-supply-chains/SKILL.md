---
name: analyzing-sustainable-supply-chains
description: Structures supply chain sustainability assessment with Scope 3 attribution and risk identification. Use when analyzing supply chain ESG, mapping supplier risk, or assessing supply chain sustainability.
tags:
  - analysis
  - sustainable-finance
  - risk
  - esg
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
# Analyzing Sustainable Supply Chains

Structures supply chain sustainability assessment with Scope 3 attribution and risk identification for ESG due diligence, impact investing screening, and sustainable finance reporting.

## When To Use

- Evaluating a portfolio company's or issuer's supply chain for ESG risk exposure
- Attributing Scope 3 (upstream/downstream) greenhouse gas emissions across supplier tiers
- Mapping supplier concentration risk by geography, commodity, or social-risk factor
- Preparing supply chain sections of sustainability-linked loan or green bond frameworks
- Conducting pre-investment due diligence on supply chain resilience and labor practices

## Inputs To Gather

- **Supplier list or spend data** — tier 1 suppliers at minimum; tier 2+ if available
- **Scope 3 emissions data** — company-reported figures, CDP responses, or spend-based estimates
- **Industry/sector classification** — GICS, NACE, or ISIC codes for supplier categorization
- **Geographic footprint** — country-level supplier locations for regulatory and physical risk mapping
- **Existing disclosures** — sustainability reports, CSRD filings, TCFD/ISSB responses, EcoVadis or Sedex scores
- **Relevant standards context** — which frameworks apply (GHG Protocol Scope 3, EU CSRD/CSDDD, SFDR PAI indicators) [VERIFY jurisdiction-specific applicability]

## Workflow

1. **Define scope and materiality boundaries**
   - Confirm which Scope 3 categories (GHG Protocol Categories 1-15) are in scope
   - Identify material supplier segments by spend share, emissions intensity, or risk exposure
   - Agree on assessment framework: GHG Protocol, SBTi FLAG guidance, TNFD for nature, or SA8000/ILO for labor

2. **Map the supplier base**
   - Classify suppliers by tier, geography, commodity type, and sector
   - Flag high-risk jurisdictions using indices (e.g., Global Slavery Index, ND-GAIN for climate vulnerability, Transparency International CPI)
   - Identify supplier concentration — single-source dependencies, critical mineral bottlenecks

3. **Quantify Scope 3 emissions attribution**
   - Use supplier-specific data where available (primary data preferred under GHG Protocol)
   - Apply spend-based or activity-based estimation for gaps — document methodology and emission factors used (e.g., EXIOBASE, EEIO, DEFRA)
   - Allocate emissions across categories: purchased goods/services (Cat 1), upstream transportation (Cat 4), end-of-life treatment (Cat 12), etc.
   - Note data quality scores per category (1-5 scale per GHG Protocol guidance)

4. **Assess ESG risk factors across supplier tiers**
   - **Environmental**: deforestation exposure, water stress (WRI Aqueduct), biodiversity proximity (TNFD LEAP), chemical/waste intensity
   - **Social**: forced labor risk, living wage gaps, health and safety incident rates, freedom of association restrictions [VERIFY against EU CSDDD requirements if applicable]
   - **Governance**: supplier anti-corruption controls, beneficial ownership transparency, sanctions screening

5. **Score and prioritize**
   - Assign risk ratings (e.g., high/medium/low) per supplier segment using a consistent rubric
   - Rank suppliers by combined ESG risk score weighted by spend or emissions contribution
   - Identify engagement priorities — which suppliers need corrective action plans vs. monitoring vs. phase-out

6. **Link findings to financial and regulatory implications**
   - Map risks to SFDR Principal Adverse Impact (PAI) indicators where relevant [VERIFY which PAI indicators apply]
   - Quantify potential carbon cost exposure under pricing scenarios (e.g., EU CBAM, internal carbon price)
   - Assess alignment with sustainability-linked loan/bond KPIs if applicable
   - Flag any CSRD double-materiality implications for the reporting entity

## Output

Deliver a structured **Supply Chain Sustainability Assessment** containing:

- **Executive summary** — key risk exposures, Scope 3 hotspots, and recommended actions
- **Supplier risk heat map** — matrix of ESG risk vs. spend/emissions materiality by segment
- **Scope 3 emissions profile** — breakdown by GHG Protocol category with data quality annotations
- **High-risk supplier register** — flagged suppliers with specific risk factors and recommended engagement tier
- **Regulatory alignment table** — mapping of findings to applicable disclosure requirements (CSRD, SFDR, TCFD/ISSB)
- **Data gaps and limitations** — explicit list of assumptions, estimation methods, and areas needing primary data collection

## Quality Checks

- Verify Scope 3 methodology aligns with GHG Protocol Corporate Value Chain Standard — confirm calculation approach (spend-based vs. supplier-specific) is documented per category
- Ensure geographic risk flags cite current index data — outdated indices distort risk ratings
- Confirm emission factors match the reporting year and regional context [VERIFY emission factor source and vintage]
- Check that supplier risk scores use consistent weighting — no ad hoc adjustments without documented rationale
- Validate that all [VERIFY] markers have been reviewed against the applicable jurisdiction and reporting framework before finalizing
- Confirm double-counting is avoided when aggregating Scope 3 categories (e.g., upstream transport vs. purchased goods)
- Flag any supplier segments where data coverage falls below 60% of spend — these require explicit qualification in the executive summary
