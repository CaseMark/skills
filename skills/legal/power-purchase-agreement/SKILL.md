---
name: power-purchase-agreement
description: >-
  Drafts U.S. power purchase agreements (PPAs) between generators and
  offtakers with complete terms for delivery, pricing, metering, performance,
  credit support, RECs/carbon attributes, defaults, and remedies. Use when
  drafting a PPA, renewable energy offtake, utility power sale, or long-term
  energy supply agreement; triggers: "PPA", "power purchase agreement",
  "offtaker", "generator", "REC", "net output", "interconnection", "capacity",
  "energy payment".
tags:
  - agreement
  - drafting
  - regulatory
---

# Power Purchase Agreement (PPA)

Drafts a commercially balanced, regulation-aware PPA for sale and purchase of electric energy.

## Prerequisites

1. **Parties and authority** — legal names, jurisdictions, signatory authority, affiliates/guarantors.
2. **Project specifics** — facility type, location, capacity (MW), technology, COD targets, interconnection status.
3. **Delivery framework** — delivery point, ISO/RTO or utility service territory, scheduling/dispatch model.
4. **Commercial terms** — term length, pricing model, escalators, payment cycle, taxes.
5. **Attributes** — RECs/carbon attributes ownership, transfer mechanics, certification requirements.
6. **Risk allocation** — curtailment, force majeure, change in law, credit support, insurance.
7. **Operational data** — metering standards, testing cadence, data interfaces.
8. **Finance constraints** — lender requirements, step-in rights, consent rights.

## Output Structure / Process

### 1) Agreement Outline (use as table of contents)

| Section | Required Content |
| --- | --- |
| Parties/Recitals | Project purpose, facility description, regulatory context, effective date. |
| Definitions/Interpretation | Technical, pricing, performance, metering, default terms. |
| Term/Conditions Precedent | Start date, COD, satisfaction deadlines, consequences. |
| Sale/Purchase Obligations | Quantity, delivery point, scheduling, curtailment. |
| Pricing/Payment | Price type, invoicing, late fees, taxes. |
| Metering/Measurement | Meter specs, testing, data disputes. |
| RECs/Attributes | Ownership, delivery, retirement, replacement. |
| Performance/LDs | Availability, output guarantees, LDs, cure. |
| Representations/Covenants | Authority, compliance, permits, reporting. |
| Defaults/Remedies | Cure periods, termination, damages. |
| Force Majeure | Events, notice, mitigation, duration. |
| Insurance/Security | Coverage, limits, proof, credit support. |
| Disputes/Governing Law | Escalation, arbitration/litigation, venue. |
| Miscellaneous | Assignment, confidentiality, notices, entire agreement. |
| Exhibits/Schedules | Technical, pricing, notices, credit forms. |

### 2) Definitions Checklist (include as table)

| Term | Required Definition Points |
| --- | --- |
| Contract Capacity | MW/kW, net of parasitic load. |
| Energy/Delivered Energy | kWh/MWh at delivery point. |
| Net Output | Adjustments for losses/auxiliary load. |
| Commercial Operation Date | Objective tests and certification. |
| Force Majeure | Scope and exclusions. |
| Scheduled Maintenance | Notice windows, limits. |
| Availability | Calculation method and exclusions. |
| REC/Environmental Attributes | Registry, certification, transfer. |

### 3) Conditions Precedent (checklist with deadlines)

- [ ] Permits/licenses obtained and in force.
- [ ] Interconnection agreement executed and effective.
- [ ] Construction milestones met; COD evidence.
- [ ] Insurance in place with required endorsements.
- [ ] Credit support posted and accepted.
- [ ] Regulatory approvals obtained (if required).

### 4) Pricing Model Selector (choose and fully specify)

| Model | Key Inputs |
| --- | --- |
| Fixed energy price | `$/MWh`, escalator, pricing start date. |
| Indexed price | Index, reset frequency, floor/ceiling. |
| Time-of-delivery | Peak/off-peak bands, seasonal tables. |
| Capacity + energy | Capacity payment, availability test. |
| Pay-as-produced | Output-based with curtailment rules. |

### 5) Metering and Data

- Meter accuracy requirement (e.g., ±0.5%).
- Testing/calibration frequency and standards.
- Data delivery method and timing.
- Meter dispute process and true-up timeline.
- Loss factor allocation between POI and delivery point.

### 6) Performance and Liquidated Damages

| Metric | Standard | Measurement | Remedy |
| --- | --- | --- | --- |
| Availability | `%` annual | Defined formula | LDs per shortfall |
| Energy guarantee | MWh/period | Net Delivered | LDs or make-whole |
| COD delay | Days late | Milestone dates | LDs per day |

### 7) Default/Remedy Framework

- Cure periods by default type (payment, non-monetary, insolvency).
- Termination rights and effective date mechanics.
- Damages framework: cover costs, replacement power, termination payment.
- Step-in or cure rights for lenders (if applicable).

### 8) Drafting Skeleton (core clause headers)

```text
1. Parties; Recitals
2. Definitions and Interpretation
3. Term; Conditions Precedent
4. Sale and Purchase; Delivery; Scheduling
5. Pricing; Invoicing; Taxes
6. Metering; Measurement; Data
7. Environmental Attributes
8. Representations and Warranties
9. Covenants; Reporting; Compliance
10. Performance Standards; Liquidated Damages
11. Events of Default; Remedies
12. Force Majeure
13. Insurance; Credit Support
14. Termination; Consequences
15. Dispute Resolution; Governing Law
16. Miscellaneous
Exhibits A–E
```

### 9) Exhibits/Schedules (minimum set)

- Exhibit A: Facility description; POI; single-line diagram.
- Exhibit B: Pricing tables; escalation; example invoices.
- Exhibit C: Metering specs; testing protocol; data format.
- Exhibit D: Form notices; designated recipients.
- Exhibit E: Credit support forms (LOC/guarantee).

## Guidelines

- Confirm jurisdiction-specific regulatory approvals, ISO/RTO tariffs, and interconnection rules before finalizing [VERIFY].
- Align REC/carbon attribute transfer language with registry requirements and buyer compliance targets.
- Ensure LDs are a reasonable pre-estimate of loss, not a penalty.
- Keep curtailment rights symmetrical or clearly allocated to avoid implied take-or-pay conflicts.
- Tie COD, availability, and performance tests to objective, auditable criteria.
- Avoid contradictory delivery point definitions across main body and exhibits.
- Ensure confidentiality and public announcement clauses match financing and regulatory disclosure obligations.
- Include lender consent/step-in rights only if finance structure requires it.
