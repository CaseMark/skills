---
name: analyzing-servicer-performance
description: Evaluates master and special servicer performance with delinquency management, modification outcomes, and loss mitigation effectiveness. Use when assessing servicer quality, monitoring servicing metrics, or evaluating servicer transfers.
tags:
  - analysis
  - structured-finance
metadata:
  author: casemark
  practice_areas:
    - Structured Finance
    - Securitization
    - ABS/MBS/CLO
  document_types:
    - Analysis Report
  skill_modes:
    - Analysis
---
# Analyzing Servicer Performance

## When To Use

- Periodic review of master or special servicer performance against PSA benchmarks and rating agency criteria
- Evaluating a servicer prior to a servicing transfer, appointment, or termination recommendation
- Assessing delinquency management effectiveness across CMBS, RMBS, ABS, or CLO portfolios
- Monitoring loss mitigation outcomes (modifications, forbearance, short sales, REO liquidation) relative to pool expectations
- Responding to investor complaints, rating agency inquiries, or trustee escalation regarding servicing deficiencies
- Benchmarking servicer metrics against industry peers or historical performance

## Inputs To Gather

- **Servicing agreement**: PSA, sub-servicing agreement, or special servicing agreement defining performance obligations, advancing requirements, and termination triggers
- **Remittance reports**: Monthly distribution date statements, servicer certificates, and advancing reconciliation
- **Delinquency data**: Loan-level delinquency rolls (30/60/90+ day buckets), roll-rate migration tables, and cure rates over trailing 3-, 6-, and 12-month periods
- **Modification/workout data**: Loan modification terms, trial period conversion rates, re-default rates, NPV test results, and timeline from default to resolution
- **Loss severity data**: Liquidation proceeds, REO carrying costs, advancing recoveries, and net loss severity by vintage and collateral type
- **Servicer ratings**: Current and historical ratings from Fitch, S&P, Moody's, or DBRS for master, primary, and special servicing [VERIFY: confirm which agencies currently rate the servicer]
- **Compliance records**: Regulatory exam findings, consent orders, CFPB actions, or state AG settlements affecting the servicer
- **Peer benchmarks**: Intex, Bloomberg, or Trepp data for comparable servicer performance across similar deal structures

## Workflow

1. **Define scope and servicer role**
   - Clarify whether the review covers master servicing, primary servicing, special servicing, or all three
   - Identify the deal type (conduit CMBS, single-borrower, RMBS prime/non-prime, auto ABS, CLO) as performance expectations differ materially
   - Determine the review period and whether this is routine surveillance or triggered by a specific event

2. **Analyze delinquency management**
   - Build roll-rate tables showing month-over-month migration between current, 30, 60, 90+, foreclosure, and REO buckets
   - Calculate cure rates and compare to pool-level and vintage-level benchmarks
   - Identify loans with extended delinquency (180+ days) without resolution and assess whether timelines comply with PSA requirements and applicable foreclosure timelines [VERIFY: state-specific foreclosure timeline requirements]
   - Flag any delinquency reporting inconsistencies between servicer reports and trustee remittance data

3. **Evaluate modification and workout outcomes**
   - Assess modification volume as a percentage of eligible delinquent loans
   - Review trial-to-permanent conversion rates (target: above 60% for performing programs)
   - Track re-default rates at 6, 12, and 24 months post-modification
   - For special servicers: measure time from transfer to resolution, compare against PSA-mandated timelines, and evaluate whether workout strategies (modification vs. foreclosure vs. discounted payoff vs. note sale) maximized net present value to the trust
   - Confirm NPV test methodology aligns with governing documents and investor reporting

4. **Assess loss mitigation effectiveness**
   - Calculate net loss severity by disposition type (foreclosure, short sale, REO, note sale, DPO)
   - Compare realized losses to original appraisal values and updated BPOs
   - Evaluate REO management: time from foreclosure to listing, days on market, sales price vs. list price ratio, carrying costs as percentage of liquidation proceeds
   - Review advancing practices: confirm servicer is advancing P&I and T&I per PSA requirements, identify any advancing shortfalls or stop-advance determinations and their justification

5. **Review operational and compliance performance**
   - Check investor reporting accuracy and timeliness (distribution date statements, CREFC reporting for CMBS, Reg AB compliance for SEC-reporting deals)
   - Assess borrower communication practices, complaint volume trends, and regulatory compliance posture
   - Review any rating agency surveillance actions (affirmations, downgrades, or outlook changes on servicer ratings)
   - Identify any servicing transfer triggers that may have been activated under the PSA (performance thresholds, rating downgrades, change of control)

6. **Compile comparative scoring**
   - Score performance across categories: delinquency management, workout execution, loss mitigation, advancing compliance, reporting accuracy, and regulatory standing
   - Benchmark against peer servicers handling comparable asset classes and deal structures
   - Assign overall assessment (strong/acceptable/below standard/unsatisfactory) with supporting data for each category

## Output

- **Executive summary**: One-page overview of servicer identity, review period, deal coverage, and overall performance rating with key findings
- **Delinquency analysis**: Roll-rate tables, cure rate trends, and comparison to pool/vintage benchmarks
- **Workout scorecard**: Modification volumes, conversion rates, re-default rates, resolution timelines, and NPV compliance assessment
- **Loss severity analysis**: Net loss severity by disposition channel, REO performance metrics, and advancing reconciliation
- **Compliance and operational review**: Reporting accuracy findings, regulatory status, and rating agency actions
- **Recommendations**: Specific actions — continued monitoring, enhanced reporting requirements, remediation demands, or servicer replacement recommendation with transfer considerations
- **Appendices**: Loan-level data tables, methodology notes, and source documentation references

## Quality Checks

- Confirm all delinquency and loss figures tie back to trustee remittance reports and servicer certificates — reconcile any discrepancies before finalizing
- Verify that PSA performance thresholds and termination triggers cited are from the correct governing document version
- Ensure loss severity calculations use consistent methodology (gross vs. net, inclusion/exclusion of advancing recoveries) throughout
- Check that peer benchmarks are drawn from comparable asset types, vintages, and geographic concentrations
- Confirm all servicer rating references are current [VERIFY: check rating agency websites for most recent servicer rating actions]
- Flag any data gaps (missing months, unreported loans, inconsistent loan counts) explicitly rather than interpolating
- Validate that workout timeline calculations account for judicial vs. non-judicial foreclosure state distinctions [VERIFY: applicable state foreclosure frameworks]
