---
name: health-care-agent-letter
description: >
  Drafts a non-binding instruction letter (values letter / legacy letter) from a
  client to their designated health care agent, translating personal values,
  quality-of-life definitions, spiritual commitments, and scenario-based treatment
  preferences into operational bedside guidance for substituted judgment. Use this
  skill when the user mentions health care agent letter, values letter, legacy
  letter, substituted judgment guidance, instruction letter to healthcare proxy,
  agent decision-making guide, or asks how to communicate treatment wishes to a
  designated agent. Also trigger when the user wants to supplement a formal advance
  directive with personal guidance or needs to address family conflict around
  medical decisions.
tags:
  - drafting
  - letter
  - litigation
  - transactional
---

# Instruction Letter to Health Care Agent

## Why This Skill Exists

Formal advance directives appoint an agent and set legal parameters, but they rarely give that agent enough information to make hard bedside decisions with confidence. When a crisis hits, agents face questions the legal form never anticipated — "Your mother's dementia has progressed; she has pneumonia; do you want antibiotics?" Without a values letter, agents guess, family members fight, and ethics consults multiply. In states applying a "clear and convincing evidence" standard (like New York), the letter also serves a critical evidentiary function.

This skill produces a client-voiced letter that translates values into operational guidance an agent can use at 2 AM in an ICU — not a legal document, but the most important supplement to one.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Executed legal documents** — health care power of attorney/proxy, living will or advance directive, POLST/MOLST, HIPAA authorization, organ donation directives. If unavailable, frame the letter as "supplemental, pending harmonization with signed directives"
2. **Identity and audience** — client's preferred name; primary agent and alternates (full names, relationships); whether to share the letter now or only upon incapacity
3. **Medical context (non-diagnostic)** — major diagnoses, chronic conditions, prior hospitalizations, cognitive baseline, formative experiences (e.g., caring for a parent with dementia, witnessing a hospice death)
4. **Values and tipping points** — what makes life meaningful; definitions of independence; cognitive function thresholds; longevity vs. comfort tradeoffs; tolerance for pain, sedation, dependence; home vs. institutional care preferences
5. **Treatment preferences** — views on CPR, ventilator support, dialysis, feeding tubes, antibiotics for recurrent infections, major surgery, time-limited trials, palliative sedation
6. **Religious/spiritual/cultural commitments** — rituals, sacraments, clergy contacts, dietary restrictions, modesty concerns, doctrinal positions affecting care decisions
7. **Family dynamics** — likely objectors, communication wishes, conflict-management preferences, who should be informed
8. **Desired tone** — intimate, direct, spiritual, humorous, or formal

**If the user doesn't respond**, apply and clearly label these defaults: supplement to existing advance directive; primary agent audience; comfort-focused values; moderate detail level; warm but direct tone.

---

## Step 1: Frame the Letter and Harmonize with Legal Documents

Draft the opening to establish the letter's legal posture and relationship to formal documents.

### Requirements

| Element | Requirement |
|---|---|
| Identify governing documents | By name and date (or `[DATE]` placeholder) |
| Non-binding statement | Explicitly state the letter supplements, does not supersede, formal directives |
| Substituted judgment explanation | Tell the agent: "You are being my voice, not making your own choice" |
| Terminology | Mirror the client's executed forms (Health Care Proxy / Medical POA / Advance Health Care Directive) |

**Template opening:**
> "This letter is not a legal document and does not replace my [Health Care Power of Attorney / Advance Directive dated ______]. I wrote it to help you understand what matters most to me so that, if you ever have to speak for me, you can make decisions the way I would make them."

- Flag any discrepancy between the letter and signed directives for attorney review
- Never present the letter as binding instructions

---

## Step 2: Translate Values into Operational Decision-Making Principles

Address the "Big Three" functional thresholds that drive most bedside decisions:

| Threshold | Address |
|---|---|
| Cognitive function | What level of awareness/recognition is essential? |
| Physical independence | What dependence is tolerable vs. unacceptable? |
| Pain experience | What is the comfort vs. alertness tradeoff? |

- **Dementia specifically**: address whether life-prolonging care is wanted at various stages of cognitive decline — use plain language, not clinical scales
- Distinguish temporary impairment (post-surgical delirium) from permanent loss (advanced dementia)
- Pair every values statement with a concrete scenario to prevent misinterpretation

---

## Step 3: Draft Scenario-Based Treatment Guidance

Organize under plain-language headings. For each category, state the general preference + conditional scenarios:

| Category | Cover |
|---|---|
| CPR and intensive care | Frailty context vs. otherwise healthy |
| Breathing machines | Short trial vs. indefinite support |
| Feeding tubes | Temporary recovery aid vs. permanent dependence |
| Infections and antibiotics | Curative vs. comfort-only contexts |
| Pain control and sedation | Comfort priority even if life-shortening |
| Time-limited trials | Duration, reassessment criteria, who decides to stop |
| Hospice and care setting | Home vs. facility preferences |
| Sensory/environmental | Music, touch, outdoors, lighting |

- Frame as guidance ("If my doctors believe… then I would prefer…"), not rigid orders
- Empower the agent to ask: "What are best/worst outcomes? What does recovery look like? What if we do nothing?"
- **Never draft to resemble a POLST/MOLST** — recommend that as a separate clinical/legal workflow

---

## Step 4: Address Religious, Spiritual, and Cultural Commitments

- State beliefs in the client's own words
- Translate into concrete requests (clergy contact info, specific sacraments, dietary needs, modesty requirements)
- Reference relevant doctrinal frameworks where the client identifies them
- Address conscientious-objection scenarios: instruct agent on facility transfer if needed
- If religiously significant refusals exist (e.g., blood products), ensure they are documented in formal legal/medical forms, not just this letter

---

## Step 5: Establish Agent Authority and Conflict Management Process

**Authorize the agent to:**
- Request ethics consults, palliative care consults, family meetings
- Obtain second opinions
- Rely on the treating team's recommendations when consistent with client values
- Make decisions without unanimous family agreement

**Address family conflict directly:**
> "You do not need unanimous agreement from the family to follow my wishes. If there is conflict, request a family meeting with the medical team and, if helpful, an ethics consult."

- If specific objectors are anticipated, name them and reinforce agent authority
- Do not create de facto co-agents by asking multiple people to "decide together"
- Address information-sharing boundaries (HIPAA implications)

---

## Step 6: Draft Closing and Distribution Plan

| Element | Include |
|---|---|
| Gratitude and emotional reassurance | Thank the agent; transfer moral responsibility back to client |
| Permission statement | "I grant you full permission… you are not 'doing this to me,' you are doing this for me" |
| Distribution instructions | Who gets copies; share now or only upon incapacity |
| Document location | Where formal legal documents are kept |
| Signature line and date | Optional witness/notary recommendation for evidentiary weight |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial draft, ask:

1. Does the letter accurately reflect your voice — would the agent recognize this as you?
2. Are the dementia-stage and cognitive-decline preferences correctly stated?
3. Is there anyone specific who might challenge the agent's decisions that we should address more directly?
4. Should this letter be shared now or sealed until incapacity?

If the user doesn't answer, recommend reviewing the dementia-specific guidance (most common gap) and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- [ ] Letter identifies governing documents correctly (or uses placeholders)
- [ ] No contradiction between letter and signed directives (discrepancies flagged prominently)
- [ ] Values are operational, not abstract — agent can answer: "What would you want if doctors say you won't recover?"
- [ ] No vague phrases ("no heroic measures," "vegetable") — replaced with functional descriptions
- [ ] All facts, dates, and relationships are user-provided, not inferred
- [ ] Legal citations verified or marked `[VERIFY]`
- [ ] Dementia-specific guidance included
- [ ] Agent explicitly granted emotional/moral authority
- [ ] Adversarial review: no sentence is easily weaponized out of context
- [ ] Written at accessible reading level in client's voice
- [ ] Family conflict management addressed
- [ ] Distribution plan included

---

## Guidelines

**Compliance:**
- **Model Rule 1.1**: Draft only as a supplemental narrative; never imply it changes legal rights
- **Model Rule 1.14**: If diminished capacity, coercion, or undue influence is suspected, advise attorney-conducted capacity-sensitive interview
- **Model Rule 1.6**: Client decides who receives the letter; warn that placement in medical records makes it broadly accessible
- **Model Rules 1.7/1.8(f)**: Do not take instructions from agents or family members; flag third-party steering

**Jurisdiction-Specific:**
- Match terminology to the client's executed forms and local usage
- In **New York** and similar jurisdictions applying a "clear and convincing evidence" standard (*In re Storar*, 52 N.Y.2d 363 (1981) `[VERIFY]`), draft with heightened specificity — the letter serves a critical evidentiary function
- In **CA, TX, FL** and states allowing attachments to statutory forms, note that the letter may be incorporated by reference (attorney decision)
- **MAID jurisdictions** (OR, WA, CA, etc.): An agent generally cannot request MAID on behalf of a principal — flag as a separate legal/clinical workflow; do not imply agent MAID authority

**Anti-Hallucination:**
- Do not invent facts, diagnoses, family relationships, document dates, or religious beliefs
- Do not draft language resembling a POLST/MOLST or medical order
- Do not use legalese ("principal," "attorney-in-fact") in the client-facing letter
- Do not include medical statistics without a citable source
- Do not state the letter is "legally binding"
- Do not invent registry names; ask the user if a state registry is in use

**ATTORNEY REVIEW REQUIRED** — This draft must be reviewed by a licensed attorney before use to ensure it does not contradict executed documents or conflict with state-specific medical consent laws.
