---
name: structuring-fund-vehicle-architecture
language: en
description: Designs fund legal structures with master-feeder, parallel fund, and blocker entity configurations for tax-efficient investor access. Use when designing fund structures, selecting vehicle types, or optimizing multi-jurisdictional access.
tags:
  - fund-formation-and-structuring
  - tax
metadata:
  author: casemark
  practice_areas:
    - Fund Formation
    - Fund Structuring
    - Partnership Law
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Fund Vehicle Architecture

Designs fund legal structures with master-feeder, parallel fund, and blocker entity configurations for tax-efficient investor access.

## When To Use

- Sponsor is launching a new fund and needs to select or compare vehicle architectures
- Existing fund is adding investor channels (e.g., onboarding tax-exempt, ERISA, or non-U.S. investors)
- Evaluating whether to convert a standalone fund to master-feeder or parallel structure
- Assessing blocker entity necessity for specific investor categories
- Restructuring vehicles for a successor fund with changed investor mix

## Inputs To Gather

- **Investment strategy and asset class** — determines flow-through vs. entity-level tax treatment needs
- **Investor base composition** — U.S. taxable, U.S. tax-exempt, ERISA plan assets, non-U.S. (by jurisdiction), sovereign wealth, fund-of-funds
- **Target fund size and number of investors** — impacts cost-benefit of multi-vehicle complexity
- **Domicile preferences** — Delaware LP, Cayman exempted limited partnership, Luxembourg SCSp, etc. [VERIFY jurisdiction-specific formation and regulatory requirements]
- **UBTI/ECI sensitivity** — whether strategy generates unrelated business taxable income or effectively connected income
- **ERISA threshold tolerance** — target percentage for benefit plan investors and whether 25% threshold management is needed
- **Management company and GP entity locations** — affects withholding, permanent establishment, and treaty access
- **Side letter commitments** — MFN provisions, co-investment rights, or structural accommodations already promised

## Workflow

1. **Profile the investor mix** — Categorize prospective LPs into tax-status buckets: U.S. taxable individuals/corps, U.S. tax-exempt (endowments, foundations, pension plans), ERISA-subject plans, non-U.S. investors by treaty jurisdiction, sovereign entities. Estimate capital allocation per bucket.

2. **Assess tax leakage risks** — Determine whether the fund's strategy produces UBTI (e.g., debt-financed real estate, operating businesses) or ECI. If so, identify which investor categories are exposed and quantify the impact of unblocked flow-through. [VERIFY current IRS guidance on UBTI siloing under IRC 512(a)(6)]

3. **Select primary architecture pattern:**
   - **Standalone LP** — Suitable when investor base is homogeneous (e.g., all U.S. taxable). Lowest cost and complexity.
   - **Master-feeder** — Domestic feeder LP + offshore feeder (typically Cayman) investing into a master fund (often Cayman LP or LLC). Use when mixing U.S. and non-U.S. investors who need different reporting and withholding treatment.
   - **Parallel funds** — Separate domestic and offshore vehicles investing side-by-side on a pro-rata basis. Preferred when master-feeder aggregation creates regulatory, ERISA, or tax complications, or when investors require segregated NAVs.
   - **Hybrid (master-feeder + parallel sidecar)** — Combines structures for complex investor bases or co-investment programs.

4. **Design blocker entities** — For tax-exempt and non-U.S. investors exposed to UBTI or ECI, interpose a domestic C-corporation blocker (or offshore equivalent). Decide between investor-level blockers vs. fund-level blockers based on number of affected investors and cost allocation. Evaluate check-the-box elections for intermediate entities. [VERIFY state-level tax implications of blocker domicile choice — Delaware vs. other states]

5. **Address ERISA compliance** — If benefit plan investors participate, determine whether the fund will operate below the 25% threshold (with venture capital or other exemptions) or register as an ERISA-compliant vehicle. Structure feeder or parallel vehicles to isolate plan asset calculations. [VERIFY DOL plan asset regulation applicability and available exemptions]

6. **Map GP/carry vehicle structure** — Align carried interest and management fee entities with the fund architecture. Ensure GP entities sit at the correct level (master vs. feeder) to avoid duplicative withholding or misallocation of economics. Address IRC 1061 holding-period requirements for carried interest.

7. **Evaluate domicile and regulatory overlay** — For offshore vehicles, confirm exempted fund status (Cayman SIBL registration, Luxembourg RAIF/SIF qualification, etc.). For onshore vehicles, confirm state LP/LLC formation and securities filing requirements (Form D, blue sky). [VERIFY local regulatory registration thresholds and exemptions per domicile]

8. **Cost-benefit stress test** — Estimate incremental legal, accounting, and administration costs of multi-vehicle structures against tax savings and investor access benefits. Simplify where marginal vehicles serve de minimis capital.

## Output

Produce a **Fund Vehicle Architecture Report** containing:

- **Architecture diagram** — Visual showing all entities, ownership lines, capital flow, and fee/carry flow
- **Vehicle schedule** — Table listing each entity with: name, jurisdiction, entity type, tax classification, investor categories served, and regulatory status
- **Tax analysis summary** — UBTI/ECI exposure by investor bucket, blocker effectiveness, withholding treaty positions
- **ERISA analysis** — Plan asset percentage calculations per vehicle, applicable exemptions
- **Cost estimate** — Formation, annual maintenance, and dissolution costs per vehicle
- **Recommendation** — Preferred architecture with rationale, alternatives considered, and conditions that would trigger restructuring

## Quality Checks

- Every investor category in the intake has a clear path into the structure without unintended tax leakage
- Blocker entities are justified by quantified tax savings exceeding their carrying costs
- ERISA thresholds are calculated correctly with identified monitoring triggers
- GP/carry entities are positioned to avoid double taxation or withholding mismatches
- Architecture accommodates anticipated fund scaling (successor funds, co-invest vehicles) without requiring full restructuring
- All jurisdiction-dependent conclusions are marked with [VERIFY] for local counsel confirmation
- Diagram and vehicle schedule are internally consistent (no orphaned entities, no missing flow lines)
