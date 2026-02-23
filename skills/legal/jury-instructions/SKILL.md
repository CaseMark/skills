---
name: jury-instructions
description: Drafts complete jury instruction sets for U.S. litigation, covering preliminary instructions, case statements, legal definitions, elements, burden of proof, evidence evaluation, and verdict forms. Adapts to jurisdiction-specific pattern instructions and balances legal precision with lay-juror accessibility. Use when drafting proposed jury instructions, jury charges, verdict forms, or special interrogatories during trial preparation.
tags:
  - brief
  - drafting
  - litigation
  - pleading
---

# Jury Instructions

Drafts a complete set of proposed jury instructions tailored to the case, jurisdiction, and claims at issue.

## Prerequisites

1. **Pleadings and pretrial order** — complaint, answer, counterclaims, stipulated facts, motions in limine rulings
2. **Jurisdiction identified** — state/federal, specific court, to determine applicable pattern instructions
3. **Claims and defenses** — all causes of action, affirmative defenses, and counterclaims with statutory/common-law basis
4. **Proposed verdict forms** — general verdict, special verdict, or interrogatories
5. **Key evidence inventory** — expert witnesses, documentary exhibits, stipulated facts

## Output Structure

Draft instructions in this order, using numbered paragraphs with descriptive headings:

### 1. Preliminary Instructions

| Topic | Content |
|-------|---------|
| Role of jury | Exclusive judges of fact; must accept law as given by court |
| Evidence limitation | Verdict based solely on admitted evidence and instructions; no sympathy, prejudice, outside research |
| Conduct rules | No discussion outside jury room, no independent investigation, no internet research |
| Deliberation overview | Respectful discussion, open-mindedness, individual conscience |

- [ ] Pull jurisdiction's standard preliminary pattern instructions
- [ ] Adapt boilerplate to case type (civil/criminal)

### 2. Case Statement

- Neutral, non-argumentative summary drawn **only** from undisputed facts, pleadings, and stipulations
- Identify parties by name and role
- State the nature of the dispute and basic chronology
- **Never** use characterizations favorable to either side (e.g., "recklessly" → "entered the intersection")

### 3. Legal Definitions

- Define every legal term jurors must apply before it appears in elements instructions
- Source hierarchy: (1) statutory definitions, (2) pattern instruction definitions, (3) controlling case law
- Build definitions progressively — foundational terms first, compound concepts second

| Claim Type | Typical Terms to Define |
|------------|------------------------|
| Negligence | Duty, breach, causation, proximate cause, damages |
| Contract | Offer, acceptance, consideration, material breach, substantial performance |
| Fraud | Misrepresentation, scienter, reliance, materiality |
| Criminal | Knowingly, willfully, recklessly, specific intent |

### 4. Elements Instructions

For **each** claim/charge/defense:

1. State every element in numbered list
2. Identify which party bears the burden for each element
3. Explain what each element means in case-specific context
4. Address how mental-state elements may be inferred from circumstantial evidence
5. If claims are contingent on each other, make the logical sequence explicit

- [ ] Cite controlling statute or case law for each element
- [ ] Cross-reference pattern instructions where available
- [ ] Flag affirmative defenses and burden-shifting

### 5. Burden of Proof

| Standard | Applies When | Instruction |
|----------|-------------|-------------|
| Preponderance | Most civil claims | More likely true than not; tips the scales even slightly |
| Clear and convincing | Punitive damages, fraud (some jurisdictions) | Substantially more likely true; high probability |
| Beyond reasonable doubt | Criminal charges | High degree of certainty; doubt based on reason, not speculation |

- Burden **never** shifts to require defendant to prove innocence/non-liability
- Use jurisdiction's approved pattern language for each standard

### 6. Evidence Evaluation

**Types of evidence:**
- Direct vs. circumstantial — both equally valid; instruct accordingly
- Stipulated facts — must be accepted as true without further proof

**Witness credibility factors:**
1. Opportunity and ability to observe (distance, lighting, duration, impairments)
2. Memory and consistency of recollection
3. Bias, interest, or motive
4. Manner and demeanor (note: nervousness ≠ dishonesty)
5. Corroboration by other evidence

**Expert testimony:** Evaluate qualifications, basis of opinions, methodology, and support in evidence. Jurors not required to accept expert opinions; weigh conflicting experts on same factors.

### 7. Deliberation and Verdict

- [ ] State unanimity requirement (or supermajority rule if applicable)
- [ ] Explain foreperson selection and role
- [ ] Walk through each verdict form question with routing logic

Template for special verdict routing:

```
QUESTION 1: Has Plaintiff proved [Claim A] by a preponderance of the evidence?
  YES → proceed to Question 2
  NO  → proceed to Question 3

QUESTION 2: What is the total amount of damages Plaintiff proved for [Claim A]?
  $_______ → proceed to Question 3
```

**If damages are at issue:** Explain each category (compensatory, consequential, punitive) and calculation guidance. For punitive damages, instruct on the separate finding and relevant factors.

## Guidelines

- **Follow pattern instructions** — use jurisdiction's model/pattern jury instructions as the baseline; deviate only when the case requires it and note departures
- **Plain language** — formal but accessible; avoid jargon where possible; define every technical term before use
- **Internal consistency** — terms defined in §3 must match usage in §4; burden instructions in §5 must align with element assignments in §4
- **Neutral throughout** — no argumentative, conclusory, or prejudicial language anywhere
- **Verify all citations** — confirm every statute, rule, and case cite is current and binding in the jurisdiction; mark uncertain cites with [VERIFY]
- **Appellate durability** — instructions must withstand challenge for abuse of discretion; when in doubt, hew closer to approved pattern language
- **Number every paragraph** — for easy reference during charge conferences and trial
