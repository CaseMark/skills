---
name: analyzing-digital-infrastructure-assets
description: Evaluates data centers, fiber networks, and tower assets with capacity analysis, tenant credit, and technology obsolescence risk. Use when analyzing digital infrastructure, evaluating tower portfolios, or assessing data center investments.
tags:
  - analysis
  - infrastructure-and-project-finance
  - risk
  - investment
metadata:
  author: casemark
  practice_areas:
    - Project Finance
    - Infrastructure Investment
    - PPP
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Digital Infrastructure Assets

## When To Use

- Evaluating a data center acquisition or development financing (single-site or portfolio)
- Analyzing a wireless tower portfolio for purchase, sale, or lease-up valuation
- Assessing fiber network assets (lit or dark fiber) for infrastructure fund deployment
- Conducting due diligence on colocation, hyperscale, or edge data center investments
- Reviewing digital infrastructure assets within a broader PPP or project finance structure

## Inputs To Gather

- **Asset inventory**: Site addresses, facility types (tower/data center/fiber route), owned vs. leased land, build year, and remaining useful life estimates
- **Capacity and utilization data**: Total MW/rack capacity vs. current load (data centers), available tenancy slots vs. occupied (towers), lit vs. dark fiber strand counts
- **Tenant and revenue detail**: Tenant roster with contract terms, escalation schedules, renewal options, and credit ratings; revenue concentration by tenant
- **Capital expenditure history and projections**: Maintenance capex, expansion capex, technology refresh cycles, and deferred maintenance backlog
- **Operating metrics**: Power Usage Effectiveness (PUE) for data centers, average revenue per tower (ARPT), fiber route miles and density metrics
- **Regulatory and permitting status**: Zoning, FCC/FAA compliance (towers), local power and water entitlements (data centers), right-of-way agreements (fiber) [VERIFY jurisdiction-specific requirements]
- **Debt and financing terms**: Existing securitization structures (e.g., tower ABS), project-level debt covenants, DSCR requirements

## Workflow

1. **Classify asset type and scope** — Determine whether the analysis covers towers, data centers, fiber, or a mixed portfolio. Identify the investment thesis (yield play, growth/lease-up, development) as this drives which metrics matter most.

2. **Analyze physical capacity and utilization**
   - Data centers: Calculate current vs. total MW capacity, rack density, cooling headroom, and PUE trends. Flag facilities above 85% utilization as capacity-constrained.
   - Towers: Count tenancy ratio (tenants per tower), identify co-location capacity remaining, and assess ground space for additional equipment.
   - Fiber: Map lit vs. dark strand utilization, route redundancy, and proximity to demand anchors (enterprise campuses, wireless towers, data centers).

3. **Evaluate tenant credit and revenue quality**
   - Build a tenant concentration table: top 5 tenants by revenue share, weighted-average remaining lease term (WALT), and credit ratings.
   - Flag single-tenant concentration above 25% of revenue or any tenant below investment-grade credit.
   - Assess contractual escalators (CPI-linked vs. fixed) and mark-to-market opportunity on below-market leases.

4. **Assess technology obsolescence risk**
   - Towers: Evaluate 5G densification impact — will small-cell deployments reduce macro tower demand, or drive amendment revenue? Assess carrier consolidation risk. [VERIFY current carrier M&A landscape]
   - Data centers: Review power and cooling architecture against current hyperscaler requirements. Facilities built pre-2015 with air-cooled designs may require significant retrofit for AI/ML workload density.
   - Fiber: Assess whether existing fiber plant supports current wavelength standards; evaluate competitive overbuild risk in the service area.

5. **Model cash flows and valuation**
   - Build a 10-year discounted cash flow with explicit assumptions for: tenant churn, new lease-up pace, escalators, capex, and terminal value.
   - Apply sector-appropriate cap rates: towers (low-to-mid single digits), data centers (mid-single digits, varies by tier), fiber (varies by lit vs. dark economics). [VERIFY current market cap rates]
   - Stress-test for: 20% tenant churn scenario, power cost escalation (data centers), interest rate sensitivity on leveraged returns.

6. **Identify structural and regulatory risks**
   - Review ground lease terms for towers (remaining term, renewal risk, rent escalation).
   - Assess power and water availability and long-term pricing for data centers, especially in constrained markets.
   - Evaluate right-of-way renewal risk and municipal franchise requirements for fiber. [VERIFY local franchise/ROW renewal terms]

## Output

Structure the analysis report with the following sections:

- **Executive Summary**: Asset type, investment thesis, headline valuation range, and top 3 risks
- **Asset Overview**: Inventory table with key physical attributes and geographic distribution
- **Capacity and Utilization Analysis**: Current utilization, expansion runway, and capacity constraints
- **Tenant and Revenue Analysis**: Concentration table, WALT, credit quality summary, and escalator profile
- **Technology Obsolescence Assessment**: Risk rating (low/medium/high) per asset class with supporting rationale
- **Financial Model Summary**: Base case IRR/MOIC, key assumptions table, and sensitivity analysis output
- **Risk Matrix**: Ranked risks with likelihood, impact, and proposed mitigants
- **Appendix**: Detailed assumptions, data sources, and items marked [VERIFY]

## Quality Checks

- Confirm that utilization metrics are sourced from operator-provided data, not estimates; flag any interpolated figures
- Verify that tenant credit ratings are current (within 12 months) and sourced from recognized agencies
- Ensure cap rates and discount rates reflect the specific asset sub-type, not generic "digital infrastructure" benchmarks
- Check that technology obsolescence assessment references specific technical standards (e.g., power density per rack in kW, fiber wavelength capacity) rather than vague trend commentary
- Validate that the DCF model ties to the tenant-by-tenant revenue build-up, not a top-down growth assumption
- Confirm all jurisdiction-dependent items (zoning, FCC/FAA, ROW, franchise) are marked [VERIFY] with the relevant authority identified
