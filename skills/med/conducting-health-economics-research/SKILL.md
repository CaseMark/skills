---
name: conducting-health-economics-research
language: en
description: Structures cost-effectiveness and health economic analyses with QALY calculations and model validation. Use when conducting health economics research, calculating QALYs, or building economic models.
tags:
  - process
  - clinical-research
  - research
metadata:
  author: casemark
  practice_areas:
    - Clinical Research
    - Biostatistics
    - Regulatory Affairs
  document_types:
    - Process Documentation
  skill_modes:
    - Process Management
---

# Conducting Health Economics Research

## Why This Skill Exists

Health economics and outcomes research (HEOR) provides the evidence that payers, HTA bodies, and policy-makers use to determine drug coverage, pricing, and reimbursement. A well-structured cost-effectiveness analysis (CEA) can secure formulary placement and market access; a poorly designed one can exclude an otherwise effective therapy from coverage. Regulatory bodies (NICE, CADTH, PBAC, ICER, AMNOG) each have specific methodological requirements, and analyses that fail to meet these standards are rejected. This skill implements the CHEERS 2022 reporting standards, ISPOR modeling guidelines, and major HTA-body requirements to produce analyses that withstand technical and methodological scrutiny.

---

## Checkpoint A — Intake and Scoping

### Required Intake Questions
1. What is the target decision-maker (NICE, CADTH, PBAC, ICER, US payer, hospital formulary committee)?
2. What is the intervention and comparator(s)?
3. What is the perspective (societal, healthcare-system, payer, patient)?
4. What is the time horizon (trial-duration, lifetime, fixed period)?
5. What type of economic evaluation is required (cost-effectiveness, cost-utility, cost-benefit, cost-minimization, budget-impact)?
6. What clinical data are available (pivotal trial results, systematic review, observational data)?
7. What are the primary outcome measures (QALYs, LYs, clinical events avoided)?
8. What discount rate applies (3% US/ICER, 3.5% NICE, 1.5% CADTH)?
9. Is a budget-impact analysis (BIA) also required?
10. What is the submission deadline?

### Required Source Documents
- Clinical trial data (efficacy and safety results for intervention and comparator)
- Systematic review of clinical evidence (for model inputs)
- Published cost data (drug acquisition costs, administration costs, monitoring costs, hospitalization costs, AE-management costs)
- Health-state utility values (EQ-5D, SF-6D, or disease-specific utility studies)
- Epidemiologic data (incidence, prevalence, natural history)
- Target HTA body's reference case methodology and submission template
- CHEERS 2022 checklist
- ISPOR modeling guidance documents

---

## Step 1 — Define the Decision Problem

Structure the economic question using the PICOS-T framework adapted for HEOR:

| Element | Specification |
|---------|--------------|
| **Population** | Target patient population; align with label indication and clinical-trial population |
| **Intervention** | Drug/device/procedure with dose, schedule, and duration |
| **Comparator(s)** | Current standard of care; include all relevant comparators per HTA-body requirements |
| **Outcomes** | QALYs (primary for CEA/CUA), LYs, clinical events, costs |
| **Setting** | Healthcare system, country, care setting |
| **Time Horizon** | Sufficient to capture all relevant costs and outcomes (lifetime for chronic conditions) |
| **Perspective** | As specified by target decision-maker |
| **Discount Rate** | Per target-country guidelines |

Document the decision problem explicitly — this is Section 1 of most HTA submissions.

---

## Step 2 — Select and Build the Economic Model

Choose the appropriate model structure:

### Decision Tree
- **Best for**: Short-term decisions with few health states (acute events, surgical choices, diagnostic strategies)
- **Structure**: Branching pathways with probabilities at each node; terminal nodes with costs and outcomes
- **Limitation**: Cannot model recurrent events or time-varying transitions

### Markov Cohort Model
- **Best for**: Chronic diseases with distinct health states and transitions over time (oncology, cardiovascular, autoimmune)
- **Structure**: Health states (e.g., stable disease, progressed disease, death) with transition probabilities per cycle
- **Cycle length**: Typically 1 month or 1 year; half-cycle correction required
- **Limitation**: Memoryless (transition probabilities do not depend on how long a patient has been in a state — unless tunnel states are used)

### Partitioned Survival Model (PartSA)
- **Best for**: Oncology (most common model type for NICE/CADTH oncology submissions)
- **Structure**: Area under the curve between overall-survival and progression-free-survival KM curves defines health-state occupancy
- **Requires**: Survival-curve extrapolation beyond trial data (exponential, Weibull, log-logistic, log-normal, Gompertz, generalized gamma)
- **Limitation**: Transition probabilities are implicit, not explicit; PFS gains must translate to OS gains for the model to be coherent

### Microsimulation / Discrete Event Simulation
- **Best for**: Complex patient pathways, heterogeneous populations, treatment sequences
- **Structure**: Individual patients simulated with attributes that affect transitions and outcomes
- **Limitation**: Computationally intensive; harder to validate and debug

### Model Selection Criteria
- Structural assumptions must be clinically plausible and documented
- Model structure should be validated against published models in the same disease area
- Target HTA body preferences should inform model choice (NICE prefers PartSA for oncology; CADTH is more flexible)

---

## Step 3 — Populate the Model with Data

Source and document all model inputs:

### Clinical Inputs
- **Treatment efficacy**: Hazard ratios, response rates, or survival curves from pivotal trials or meta-analysis
- **Survival extrapolation** (for models extending beyond trial data): Fit multiple parametric distributions; select based on AIC/BIC, visual fit, clinical plausibility, and external validation against registry data
- **Adverse events**: Incidence rates from clinical trials; include only AEs with meaningful cost or utility impact (grade ≥3, or frequent grade 1-2 AEs with significant QoL impact)
- **Treatment duration and discontinuation**: Model treatment duration from trial data; define stopping rules

### Cost Inputs
- **Drug acquisition**: WAC, ASP, or net price per dosing cycle; account for vial sharing, wastage, weight-based dosing
- **Administration**: Infusion costs, office-visit costs, self-administration training
- **Monitoring**: Routine lab tests, imaging, office visits per treatment guidelines
- **Adverse-event management**: Cost per AE episode (hospitalization, outpatient treatment, supportive care)
- **Disease management**: Costs by health state (stable vs. progressed disease); distinguish direct medical costs, direct non-medical costs (transportation, home care), and indirect costs (productivity loss) based on perspective
- **Terminal care**: End-of-life costs for fatal conditions

### Utility Inputs
- **Health-state utilities**: EQ-5D values mapped from clinical-trial data (preferred by NICE, CADTH); SF-6D or direct elicitation as alternatives
- **Utility decrements**: For AEs (applied for duration of the AE) and disease progression
- **Disutility of treatment**: If treatment itself affects QoL (e.g., injection-site reactions, infusion time)
- **Mapping**: If EQ-5D was not collected in the trial, use validated mapping algorithms from disease-specific instruments

Document every input with: value, distribution (for PSA), source, and justification.

---

## Step 4 — Run the Base-Case Analysis

Execute the model and report:

1. **Total costs**: Per arm, broken down by component (drug, administration, monitoring, AE management, disease management)
2. **Total QALYs** (or LYs): Per arm, broken down by health state
3. **Incremental Cost-Effectiveness Ratio (ICER)**: (Cost_intervention − Cost_comparator) / (QALY_intervention − QALY_comparator)
4. **Interpret against willingness-to-pay thresholds**:
   - NICE: £20,000–£30,000 per QALY (£50,000 for end-of-life)
   - CADTH: No explicit threshold (but ~$50,000 CAD/QALY commonly cited)
   - ICER: $50,000–$200,000 per QALY (context-dependent)
   - US: No official threshold (but $50,000–$150,000/QALY commonly referenced)

### Dominance
- **Dominant**: Intervention is less costly AND more effective (ICER is negative with better outcomes)
- **Dominated**: Intervention is more costly AND less effective (ICER is negative with worse outcomes)
- **Extended dominance**: Intervention is dominated by a linear combination of two other strategies (in multi-comparator analyses)

---

## Step 5 — Conduct Sensitivity and Uncertainty Analyses

Quantify how robust the conclusions are to parameter uncertainty:

### Deterministic Sensitivity Analysis (DSA)
- One-way: Vary each parameter individually across its plausible range; present results as a tornado diagram
- Multi-way: Vary 2-3 correlated parameters simultaneously; present scenario results

### Probabilistic Sensitivity Analysis (PSA)
- Assign distributions to all uncertain parameters:
  - Beta distribution: Probabilities (bounded 0-1)
  - Gamma/log-normal: Costs (bounded >0, right-skewed)
  - Beta: Utilities (bounded 0-1)
  - Log-normal: Hazard ratios, relative risks
- Run 1,000-10,000 Monte Carlo iterations
- Present: cost-effectiveness scatter plot on CE plane, cost-effectiveness acceptability curve (CEAC), expected value of perfect information (EVPI)

### Scenario Analysis
- Vary structural assumptions (model type, time horizon, discount rate, comparator choice, perspective)
- Explore impact of survival-curve extrapolation choices (for oncology models — this is often the single most influential assumption)

### Value of Information Analysis (optional but increasingly requested)
- EVPI: Maximum value of removing all parameter uncertainty
- EVPPI: Value of resolving uncertainty in individual parameters
- Used to prioritize future research

---

## Step 6 — Conduct Budget Impact Analysis (if required)

BIA estimates the financial impact of adopting the new intervention on the payer's budget:

1. **Eligible population**: Estimate the number of patients eligible for the intervention (from epidemiology and market data)
2. **Market uptake**: Model the expected adoption curve over 3-5 years (current mix → projected mix with new therapy)
3. **Cost offsets**: Include cost savings from displaced comparator therapy, reduced hospitalizations, or reduced AE management
4. **Net budget impact**: Year-by-year and cumulative net cost to the payer
5. **Sensitivity**: Vary market uptake rates, eligible-population estimates, and pricing scenarios

Follow ISPOR BIA good-practice guidelines. Report is typically complementary to the CEA.

---

## Step 7 — Compile the HEOR Report

Structure per CHEERS 2022 and target HTA-body template:

- Title (identifying as economic evaluation)
- Abstract (structured per CHEERS)
- Introduction (decision problem, rationale)
- Methods (model structure, inputs, analytical methods)
- Results (base case, sensitivity analyses, scenario analyses)
- Discussion (limitations, generalizability, comparison with other models)
- Conclusions (ICER interpretation, policy implications)
- Technical appendix (model diagram, input tables, validation results, PSA distributions)

---

## Checkpoint B — HEOR Review

1. [ ] Decision problem is clearly specified (PICOS-T)
2. [ ] Model structure is justified and validated against clinical plausibility
3. [ ] All inputs are sourced, documented, and distributions are assigned for PSA
4. [ ] Survival extrapolation (if applicable) includes multiple distributions with selection justification
5. [ ] ICER is calculated correctly and interpreted against the relevant WTP threshold
6. [ ] DSA tornado diagram and PSA scatter plot/CEAC are generated
7. [ ] Scenario analyses cover key structural uncertainties
8. [ ] BIA (if required) uses realistic market-uptake assumptions
9. [ ] CHEERS 2022 checklist is completed
10. [ ] Report meets the target HTA body's submission requirements

---

## Quality Audit

- [ ] Model is internally validated (extreme-value testing, trace checks, hand calculations for simple cases)
- [ ] Model is externally validated against observed data (trial results, registry data, published models)
- [ ] Half-cycle correction is applied (for Markov models) or justified as unnecessary
- [ ] Discount rate matches the target jurisdiction's reference case
- [ ] QALYs are calculated correctly (utility × time in health state, summed across all health states)
- [ ] Cost-year and currency are stated; costs are inflated to a common year using appropriate index (CPI Medical)
- [ ] PSA runs ≥1,000 iterations with stable results
- [ ] No double-counting of costs or outcomes across model components
- [ ] All [VERIFY] flags have been resolved or escalated

---

## Guidelines

1. The model is a simplification of reality — document every simplifying assumption and its potential impact
2. Survival extrapolation is the most scrutinized element of oncology models — present all fitted curves, goodness-of-fit statistics, and clinical plausibility assessments
3. Use net prices (not list prices) when available — HTA bodies will apply their own price assumptions if not provided
4. QALYs should be based on patient-reported utility values (EQ-5D preferred by NICE); vignette-based utilities are less preferred
5. Budget-impact and cost-effectiveness analyses answer different questions — do not conflate them
6. Model transparency is essential — HTA bodies expect executable models with all inputs visible (no black boxes)
7. For multi-indication products, conduct separate analyses per indication — cross-indication averaging is not appropriate
8. Validate against competing published models; explain and justify any differences in conclusions
9. Escalate to health economist when structural uncertainty dominates (multiple plausible model structures yield different conclusions)
10. This skill produces HEOR analyses and reports — final conclusions and pricing/reimbursement recommendations require health-economics, clinical, and market-access team review
