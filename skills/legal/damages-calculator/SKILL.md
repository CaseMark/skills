---
name: damages-calculator
description: Builds auditable personal injury damages calculations separating special damages (medical expenses, wage loss, out-of-pocket) from general damages (pain and suffering) using multiplier and per diem methodologies. Includes causation screening, present value analysis, comparative fault adjustments, lien accounting, and net-to-client modeling. Use when calculating PI damages, building demand packages, preparing mediation statements, or valuing personal injury cases.
tags:
  - analysis
  - drafting
  - letter
  - litigation
---

# Personal Injury Damages Calculator

Produces a defensible, auditable damages calculation for personal injury matters — supporting demand packages, mediation statements, and internal case valuation.

## Prerequisites

1. **Incident & liability context** — date, mechanism, parties, comparative fault allegations, prior similar injuries, jurisdiction/forum
2. **Insurance information** — BI limits, med-pay/PIP, UM/UIM, coverage disputes
3. **Medical billing file** — itemized bills, EOBs (billed vs. paid vs. adjusted), lien statements (Medicare, Medicaid, ERISA, hospital), pharmacy receipts, DME invoices
4. **Medical records** — EMS, ER, imaging, operative reports, PT notes, pain management, discharge summaries
5. **Wage/employment docs** — employer verification, 13+ weeks pre-incident pay stubs, W-2s/1099s (3 years), disability notes, work restrictions, FMLA/STD paperwork, used PTO/sick time
6. **Replacement services** — invoices for home care, childcare, cleaning, transportation
7. **General damages support** — pain journal, family/coworker statements, injury photos, mental health records, functional limitation timeline
8. **Future care documentation** — life care plan, surgeon recommendations, PT plan, vocational evidence

Pause and request any missing category before finalizing numbers.

## Process

### Step 1: Build Auditable Damages Model

Structure the model as a line-item table with: date, provider/source, amount billed, amount paid, causation notes.

**Critical decision — medical expense measure:**

| Measure | When to Use |
|---------|------------|
| Billed charges | Jurisdictions applying collateral source rule (e.g., NY) |
| Paid/incurred amounts | *Howell v. Hamilton Meats*, 52 Cal. 4th 541 (2011) jurisdictions |
| Reasonable value | Jurisdictions using reasonable value standard |

If counsel cannot specify, carry both billed and paid columns and flag for attorney determination.

**Model structure:**
- A. Special damages: past medical, future medical, past wages, future wages/earning capacity, out-of-pocket, replacement services
- B. General damages: pain/suffering, emotional distress, loss of enjoyment, disfigurement, loss of consortium
- C. Adjustments: comparative fault, offsets/credits, policy-limit constraints, lien resolution, statutory caps

### Step 2: Past Medical Specials

For each bill line item, extract: service date, provider, CPT/DRG code, amount billed, amount paid/adjusted.

**Causation screen (all three required):**
- [ ] **Temporality** — treatment began promptly, relates to complained-of body parts
- [ ] **Consistency** — records document injury complaints throughout
- [ ] **Medical necessity** — care plausibly related to diagnosis and mechanism

Flag items failing any criterion as "potentially contested."

**Compute columns:** (a) gross billed, (b) contractual adjustments/write-offs, (c) insurer payments, (d) patient responsibility, (e) outstanding balances/liens.

**Include ancillary costs:** co-pays, Rx, OTC (if documented), DME, mileage to appointments, parking, childcare for treatment visits.

### Step 3: Wage Loss Specials

1. Establish disability period from work notes/restrictions — flag gaps between incident and first visit
2. Calculate wage base by employment type:

| Type | Method |
|------|--------|
| Hourly | Avg weekly hours × rate from pay stubs |
| Salaried | Annual ÷ 52 |
| Tipped/commission | Historical earnings documentation |
| Self-employed | Tax returns + P&L (gross revenue ≠ earnings); flag for expert if large claim |

3. Add: lost overtime, lost bonuses, used PTO/sick time (compensable fringe benefit loss), lost employer benefits (retirement match, health premiums)
4. State gross vs. net methodology explicitly — compute gross, disclose method, flag tax treatment for jurisdictional review

### Step 4: Future Economic Damages

Only calculate when evidentiary foundation exists. Typically requires expert testimony for admissibility.

| Source | Approach |
|--------|----------|
| Life care plan | Use plan categories and totals directly |
| Specific recommendation (e.g., "12 more PT sessions") | Current unit cost × recommended quantity; label as assumption-based |
| Vague reference ("may need surgery") | Do NOT assign dollar figure; flag for medical opinion development |

**Present value:** Discount projected annual costs using appropriate rate; account for medical inflation. Flag discount methodology for jurisdictional verification.

**Future earning capacity:** Use BLS work-life expectancy tables; applies even if plaintiff returned to work but has limited promotion potential/physical stamina. Without expert input, produce explicitly labeled "scenario analysis" (conservative/aggressive) with all assumptions marked for verification.

### Step 5: General Damages

Build harm narrative from record facts before calculating:
- Duration and intensity of pain
- Objective findings (imaging, documented spasm, ROM limits)
- Treatment invasiveness (injections, surgery)
- Daily life disruption (specific examples from records)
- Permanency or scarring

#### Method A: Multiplier

Total economic damages × severity factor = general damages.

| Severity Level | Multiplier Range | Indicators |
|---------------|-----------------|------------|
| Mild/full recovery | 1.5–2× | Soft tissue, short treatment, full resolution |
| Moderate | 2–3× | Extended treatment, residual symptoms, functional limits |
| Severe | 3–5× | Surgery, permanent impairment, disfigurement, prolonged disability |

**Articulate the severity factors explicitly** — never select a multiplier without justification.

#### Method B: Per Diem

Assign daily rate by recovery phase:

| Phase | Rate Basis | Example |
|-------|-----------|---------|
| Acute (highest pain) | Higher daily rate | $200–400/day |
| Subacute recovery | Moderate rate | $100–200/day |
| Residual/chronic | Lower rate | $50–100/day |

Common benchmark: plaintiff's daily earnings (a day of pain ≥ a day of work).

**Present both methods.** Convergence strengthens the demand; divergence requires reassessment. Flag per diem trial permissibility for jurisdictional review — some courts prohibit per diem closing arguments.

### Step 6: Audit & Adjustments

**Double-counting check:**
- [ ] Wage loss not also counted as diminished earning capacity
- [ ] No overlapping facility/global charges
- [ ] Non-economic subcategories (pain/suffering, loss of enjoyment) presented as single total with narrative components, not additive line items (unless jurisdiction treats as distinct)

**Comparative fault adjustment:**

| Regime | Rule |
|--------|------|
| Pure comparative | Recovery reduced by plaintiff's % fault |
| 50%-bar modified | No recovery if plaintiff ≥ 50% at fault |
| 51%-bar modified | No recovery if plaintiff ≥ 51% at fault |

Present gross damages, then risk-adjusted settlement range if fault is disputed.

**Collateral source/write-offs:** Show both billed and paid; flag recoverable measure for attorney confirmation.

**Liens:** Include net-to-client sensitivity analysis when lien data available. Flag lien resolution steps (Medicare conditional payments, ERISA reimbursement).

**Statutory caps:** Compute uncapped value + capped maximum as separate lines. Common caps: med-mal (e.g., MICRA, Cal. Civ. Code § 3333.2 [VERIFY]), government entity claims.

**Policy limits:** Present full case value separately; explain how limits affect demand posture. Flag time-limited demand considerations for attorney review.

### Step 7: Format as Demand Section

**Structure:**
1. Past medical expenses (billed/paid distinction)
2. Future medical (if supported)
3. Past wage loss
4. Future wage loss / diminished earning capacity (if supported)
5. Other out-of-pocket
6. Non-economic damages (method described and justified)
7. **Total demand**
8. Notes: liens, caps, jurisdiction-dependent issues

Every figure must trace to a document. If a document is missing, state so and label as estimate.

## Jurisdiction Adaptation Checklist

Flag and resolve each before finalizing:

- [ ] Collateral source / billed vs. paid rule
- [ ] Comparative negligence regime and threshold
- [ ] Non-economic damages caps (by case type)
- [ ] No-fault/PIP serious injury threshold (if applicable)
- [ ] Per diem argument permissibility at trial
- [ ] Present value discount requirements and methodology
- [ ] Joint and several liability rules (economic vs. non-economic)
- [ ] Wrongful death damages framework (if applicable)
- [ ] Loss of consortium availability and requirements

## Guidelines

- Every dollar figure must trace to a source document; flag undocumented items as estimates
- Carry both billed and paid medical columns until counsel selects the jurisdictional measure
- Do not invent case citations, verdict data, or "average settlement values" — use [VERIFY] for any citation not independently confirmed
- Do not assign future damages figures without medical support; flag for expert development
- Preemptively address preexisting conditions, treatment gaps, and failure-to-mitigate arguments
- All legal-rule statements (caps, collateral source, comparative negligence) must be verified or flagged for attorney confirmation
- Include scope notice: "Attorney work product draft requiring review. Jurisdictional rules must be verified. Figures based on provided documentation and stated assumptions."
- Ethics: ABA Model Rules 1.1 (competence), 3.1 (meritorious claims), 4.1 (truthfulness in negotiation), 3.3 (candor if used in filings)
