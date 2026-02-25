---
name: damages-calculator
description: >
  Builds auditable personal injury damages calculations separating special damages
  (medical expenses, wage loss, out-of-pocket) from general damages (pain and
  suffering) using multiplier and per diem methodologies. Use this skill when the
  user mentions PI damages calculation, personal injury valuation, demand package
  damages, mediation damages summary, special damages compilation, general damages
  multiplier, per diem pain and suffering, collateral source analysis, comparative
  fault adjustment, lien accounting, or net-to-client modeling. Also trigger when
  the user asks about billed vs. paid medical expenses, future care present value
  analysis, or needs to build a damages section for a demand letter or mediation
  statement.
tags:
  - analysis
  - drafting
  - letter
  - litigation
---

# Personal Injury Damages Calculator

## Why This Skill Exists

Damages calculations are the quantitative engine of every PI demand, mediation statement, and trial presentation. But they fail in predictable ways: medical specials don't reconcile between billed and paid columns, wage loss calculations ignore fringe benefits, future damages lack evidentiary foundation, general damages multipliers are asserted without justification, and lien accounting is deferred until it blows up the net-to-client number. A damages calculation that can't survive defense scrutiny undermines the entire case valuation.

This skill produces a defensible, auditable damages model with every figure traced to a source document, both billed and paid columns carried, general damages justified by methodology, and adjustments (comparative fault, liens, caps) applied transparently.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Incident & liability context** — date, mechanism, parties, comparative fault allegations, prior similar injuries, jurisdiction/forum
2. **Insurance information** — BI limits, med-pay/PIP, UM/UIM, coverage disputes
3. **Medical billing file** — itemized bills, EOBs (billed vs. paid vs. adjusted), lien statements (Medicare, Medicaid, ERISA, hospital), pharmacy receipts, DME invoices
4. **Medical records** — EMS, ER, imaging, operative reports, PT notes, pain management, discharge summaries
5. **Wage/employment docs** — employer verification, 13+ weeks pre-incident pay stubs, W-2s/1099s (3 years), disability notes, work restrictions, FMLA/STD paperwork, used PTO/sick time
6. **Replacement services** — invoices for home care, childcare, cleaning, transportation
7. **General damages support** — pain journal, family/coworker statements, injury photos, mental health records, functional limitation timeline
8. **Future care documentation** — life care plan, surgeon recommendations, PT plan, vocational evidence

**If the user doesn't respond**, apply and clearly label these defaults: carry both billed and paid columns; present multiplier and per diem methods for general damages; note comparative fault and lien issues for attorney resolution; flag jurisdictional rules for verification.

Pause and request any missing category before finalizing numbers.

---

## Step 1: Build the Auditable Model Structure

Structure the model as a line-item table with: date, provider/source, amount billed, amount paid, causation notes.

**Critical decision — medical expense measure:**

| Measure | When to Use |
|---|---|
| Billed charges | Jurisdictions applying collateral source rule (e.g., NY) |
| Paid/incurred amounts | *Howell v. Hamilton Meats*, 52 Cal. 4th 541 (2011) jurisdictions |
| Reasonable value | Jurisdictions using reasonable value standard |

If counsel cannot specify, carry both billed and paid columns and flag for attorney determination.

**Model sections:**
- A. Special damages: past medical, future medical, past wages, future wages/earning capacity, out-of-pocket, replacement services
- B. General damages: pain/suffering, emotional distress, loss of enjoyment, disfigurement, loss of consortium
- C. Adjustments: comparative fault, offsets/credits, policy-limit constraints, lien resolution, statutory caps

---

## Step 2: Calculate Past Medical Specials

For each bill line item, extract: service date, provider, CPT/DRG code, amount billed, amount paid/adjusted.

**Causation screen (all three required):**
- [ ] **Temporality** — treatment began promptly, relates to complained-of body parts
- [ ] **Consistency** — records document injury complaints throughout
- [ ] **Medical necessity** — care plausibly related to diagnosis and mechanism

Flag items failing any criterion as "potentially contested."

**Compute columns:** (a) gross billed, (b) contractual adjustments/write-offs, (c) insurer payments, (d) patient responsibility, (e) outstanding balances/liens.

**Include ancillary costs:** co-pays, Rx, OTC (if documented), DME, mileage to appointments, parking, childcare for treatment visits.

---

## Step 3: Calculate Wage Loss Specials

1. Establish disability period from work notes/restrictions — flag gaps between incident and first visit
2. Calculate wage base by employment type:

| Type | Method |
|---|---|
| Hourly | Avg weekly hours × rate from pay stubs |
| Salaried | Annual ÷ 52 |
| Tipped/commission | Historical earnings documentation |
| Self-employed | Tax returns + P&L (gross revenue ≠ earnings); flag for expert if large claim |

3. Add: lost overtime, lost bonuses, used PTO/sick time (compensable fringe benefit loss), lost employer benefits (retirement match, health premiums)
4. State gross vs. net methodology explicitly — compute gross, disclose method, flag tax treatment for jurisdictional review

---

## Step 4: Calculate Future Economic Damages

Only calculate when evidentiary foundation exists. Typically requires expert testimony for admissibility.

| Source | Approach |
|---|---|
| Life care plan | Use plan categories and totals directly |
| Specific recommendation (e.g., "12 more PT sessions") | Current unit cost × recommended quantity; label as assumption-based |
| Vague reference ("may need surgery") | Do NOT assign dollar figure; flag for medical opinion development |

**Present value:** Discount projected annual costs using appropriate rate; account for medical inflation. Flag discount methodology for jurisdictional verification.

**Future earning capacity:** Use BLS work-life expectancy tables; applies even if plaintiff returned to work but has limited promotion potential/physical stamina. Without expert input, produce explicitly labeled "scenario analysis" (conservative/aggressive) with all assumptions marked.

---

## Step 5: Calculate General Damages

Build harm narrative from record facts before calculating:
- Duration and intensity of pain
- Objective findings (imaging, documented spasm, ROM limits)
- Treatment invasiveness (injections, surgery)
- Daily life disruption (specific examples from records)
- Permanency or scarring

### Method A: Multiplier

Total economic damages × severity factor = general damages.

| Severity Level | Multiplier Range | Indicators |
|---|---|---|
| Mild/full recovery | 1.5–2× | Soft tissue, short treatment, full resolution |
| Moderate | 2–3× | Extended treatment, residual symptoms, functional limits |
| Severe | 3–5× | Surgery, permanent impairment, disfigurement, prolonged disability |

**Articulate the severity factors explicitly** — never select a multiplier without justification.

### Method B: Per Diem

Assign daily rate by recovery phase:

| Phase | Rate Basis | Example |
|---|---|---|
| Acute (highest pain) | Higher daily rate | $200–400/day |
| Subacute recovery | Moderate rate | $100–200/day |
| Residual/chronic | Lower rate | $50–100/day |

Common benchmark: plaintiff's daily earnings (a day of pain ≥ a day of work).

**Present both methods.** Convergence strengthens the demand; divergence requires reassessment. Flag per diem trial permissibility for jurisdictional review — some courts prohibit per diem closing arguments.

---

## Step 6: Apply Adjustments and Produce Final Summary

**Double-counting check:**
- [ ] Wage loss not also counted as diminished earning capacity
- [ ] No overlapping facility/global charges
- [ ] Non-economic subcategories presented as single total with narrative components, not additive line items (unless jurisdiction treats as distinct)

**Comparative fault adjustment:**

| Regime | Rule |
|---|---|
| Pure comparative | Recovery reduced by plaintiff's % fault |
| 50%-bar modified | No recovery if plaintiff ≥ 50% at fault |
| 51%-bar modified | No recovery if plaintiff ≥ 51% at fault |

Present gross damages, then risk-adjusted settlement range if fault is disputed.

**Collateral source/write-offs:** Show both billed and paid; flag recoverable measure for attorney confirmation.

**Liens:** Include net-to-client sensitivity analysis when lien data available. Flag lien resolution steps (Medicare conditional payments, ERISA reimbursement).

**Statutory caps:** Compute uncapped value + capped maximum as separate lines. Common caps: med-mal (e.g., MICRA, Cal. Civ. Code § 3333.2 `[VERIFY]`), government entity claims.

**Policy limits:** Present full case value separately; explain how limits affect demand posture.

### Final Output Structure

1. Past medical expenses (billed/paid distinction)
2. Future medical (if supported)
3. Past wage loss
4. Future wage loss / diminished earning capacity (if supported)
5. Other out-of-pocket
6. Non-economic damages (method described and justified)
7. **Total demand**
8. Notes: liens, caps, jurisdiction-dependent issues

Every figure must trace to a document. If a document is missing, state so and label as estimate.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial calculation, ask:

1. Should we use billed or paid medical expenses as the primary measure (jurisdiction-dependent)?
2. Is the comparative fault estimate accurate, or does counsel have a different assessment?
3. Are there additional lien holders we haven't accounted for?
4. Does the general damages multiplier/per diem result align with counsel's case valuation?

If the user doesn't answer, recommend resolving the billed-vs-paid question (highest-impact variable) and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- [ ] Every dollar figure traces to a source document (or labeled as estimate)
- [ ] Both billed and paid medical columns carried until counsel selects measure
- [ ] Causation screen applied to each medical charge (temporality, consistency, necessity)
- [ ] Wage loss calculated with correct methodology for employment type
- [ ] Future damages supported by evidentiary foundation (not speculation)
- [ ] General damages justified by both multiplier and per diem methods
- [ ] No double-counting between categories
- [ ] Comparative fault adjustment applied correctly for jurisdiction
- [ ] Lien accounting complete with net-to-client analysis
- [ ] Statutory caps identified and applied where applicable
- [ ] All legal-rule statements verified or flagged `[VERIFY]`
- [ ] Assumptions and limitations documented prominently

---

## Guidelines

**Jurisdiction Adaptation Checklist** — flag and resolve before finalizing:

- [ ] Collateral source / billed vs. paid rule
- [ ] Comparative negligence regime and threshold
- [ ] Non-economic damages caps (by case type)
- [ ] No-fault/PIP serious injury threshold (if applicable)
- [ ] Per diem argument permissibility at trial
- [ ] Present value discount requirements and methodology
- [ ] Joint and several liability rules (economic vs. non-economic)
- [ ] Wrongful death damages framework (if applicable)
- [ ] Loss of consortium availability and requirements

**Anti-Hallucination:**
- Do not invent case citations, verdict data, or "average settlement values" — use `[VERIFY]` for any citation not independently confirmed
- Do not assign future damages figures without medical support
- All legal-rule statements (caps, collateral source, comparative negligence) must be verified or flagged

**Ethics:** ABA Model Rules 1.1 (competence), 3.1 (meritorious claims), 4.1 (truthfulness in negotiation), 3.3 (candor if used in filings)

**Scope notice:** "Attorney work product draft requiring review. Jurisdictional rules must be verified. Figures based on provided documentation and stated assumptions."
