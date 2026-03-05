---
name: conducting-technical-due-diligence
description: Structures technology diligence with architecture review, code quality assessment, scalability analysis, and technical debt evaluation. Use when evaluating startup technology, assessing engineering teams, or reviewing technical infrastructure.
tags:
  - process
  - venture-capital
  - valuation
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---
# Conducting Technical Due Diligence

Structures technology diligence for venture and growth-stage investments, covering architecture review, code quality assessment, scalability analysis, technical debt quantification, and engineering team evaluation.

## When To Use

- Pre-term-sheet or post-term-sheet diligence on a software-intensive target company
- Assessing a startup's technical infrastructure before seed, Series A, or later rounds
- Evaluating acqui-hire candidates where engineering talent is the primary asset
- Follow-on investment decisions where product has scaled since initial diligence
- LP or co-investor requests for independent technical assessment

## Inputs To Gather

- **Architecture artifacts**: System diagrams, infrastructure-as-code repos, cloud provider dashboards (AWS/GCP/Azure), CI/CD pipeline configs
- **Codebase access**: Primary repositories, commit history (12+ months preferred), branch/merge strategy documentation
- **Engineering org data**: Team roster with tenure, hiring plan, reporting structure, attrition history
- **Operational metrics**: Uptime/SLA history, incident post-mortems (last 12 months), deploy frequency, mean time to recovery (MTTR)
- **Product roadmap**: Feature backlog, technical roadmap items vs. product-driven items, deferred maintenance list
- **Third-party dependencies**: Vendor contracts, open-source license inventory, API integrations list
- **Security posture**: Penetration test reports, SOC 2 / ISO 27001 status, vulnerability scan results [VERIFY: request NDA-gated reports directly from target]

## Workflow

1. **Scope the engagement**
   - Define diligence depth: lightweight (2–3 day review) vs. comprehensive (1–2 week deep dive)
   - Identify red-line issues specific to the deal thesis (e.g., "Can this platform handle 100x current load?" or "Is the ML model defensible IP?")
   - Establish data room access and NDA coverage for code review

2. **Architecture review**
   - Map the system topology: monolith vs. microservices, data stores, message queues, external integrations
   - Assess cloud infrastructure design: redundancy, auto-scaling configuration, disaster recovery plan
   - Evaluate data architecture: schema design, data pipeline reliability, storage costs at projected scale
   - Flag single points of failure and vendor lock-in risks

3. **Code quality assessment**
   - Review commit history for contribution patterns (bus factor), code review discipline, and merge hygiene
   - Analyze static analysis metrics: test coverage percentage, linting compliance, cyclomatic complexity
   - Sample-review critical modules (auth, payments, core business logic) for code clarity and correctness
   - Identify copy-paste duplication, dead code, and abandoned feature branches

4. **Scalability analysis**
   - Review load testing results or request a load test against projected 12–24 month user growth
   - Evaluate database query performance at scale: indexing strategy, N+1 queries, read/write split architecture
   - Assess whether current infrastructure costs scale linearly or super-linearly with users
   - Identify architectural ceilings that would require a rewrite vs. incremental optimization

5. **Technical debt quantification**
   - Catalog known debt items from issue trackers, tech-debt tags, and developer interviews
   - Estimate remediation cost in engineer-months for critical items
   - Classify debt as: (a) blocking scale, (b) increasing operational risk, (c) slowing velocity, or (d) cosmetic
   - Compare debt load against company stage — early-stage debt is expected; Series B+ debt warrants scrutiny

6. **Engineering team evaluation**
   - Assess team composition: seniority distribution, specialization gaps, key-person dependencies
   - Review hiring pipeline and employer brand signals (Glassdoor, GitHub presence, conference talks)
   - Evaluate engineering culture indicators: documentation habits, on-call practices, blameless post-mortems
   - Benchmark compensation against market to assess retention risk [VERIFY: use current comp data for target geography]

7. **Security and compliance review**
   - Verify authentication/authorization implementation (OAuth, RBAC, token management)
   - Check secrets management practices (no hardcoded credentials, proper vault usage)
   - Review open-source license compliance — flag copyleft licenses in proprietary distribution paths [VERIFY: license obligations depend on distribution model]
   - Assess data privacy controls relative to applicable regulations (GDPR, CCPA, HIPAA if applicable) [VERIFY: regulatory scope depends on target's markets and data types]

## Output

Structure the technical diligence report with:

- **Executive summary**: 1-page investment-grade overview with go/no-go recommendation and confidence level
- **Risk matrix**: Categorize findings as Critical / High / Medium / Low with estimated remediation effort
- **Architecture scorecard**: Rate each domain (infrastructure, data, security, scalability, code quality) on a standardized scale (e.g., 1–5)
- **Technical debt ledger**: Itemized list with severity, estimated fix cost, and business impact if unaddressed
- **Team assessment**: Strengths, gaps, and key-person risk summary
- **Deal-specific answers**: Direct responses to the red-line questions defined in scoping
- **Recommended post-close actions**: Prioritized technical initiatives for the first 90 days if the investment proceeds

## Quality Checks

- Every critical finding is supported by specific evidence (code snippets, metrics, configuration references) — no unsupported assertions
- Scalability claims are grounded in load test data or architecture analysis, not founder assertions
- Technical debt estimates use engineer-month units with stated assumptions about team productivity
- Security findings reference specific CWE/OWASP categories where applicable
- The report distinguishes between stage-appropriate trade-offs and genuinely concerning deficiencies
- All jurisdiction-dependent or regulation-dependent findings are marked with [VERIFY]
- The executive summary is understandable by non-technical investment partners
