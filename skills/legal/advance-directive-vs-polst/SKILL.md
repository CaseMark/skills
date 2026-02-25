---
name: advance-directive-vs-polst
description: >
  Produces a client-ready plain-language comparison of advance directives (legal
  planning documents) and POLST/MOLST forms (clinician-signed medical orders),
  explaining legal status, clinician signature requirements, emergency precedence,
  clinical appropriateness, and how both documents work together. Use this skill
  when the user asks about advance directive vs. POLST, living will vs. DNR,
  which document EMS follows, how healthcare planning documents interact in
  emergencies, POLST vs. MOLST vs. POST, or whether a healthy person needs a
  POLST. Also trigger for elder law, estate planning, and serious illness planning
  contexts involving document coordination.
tags:
  - analysis
  - drafting
  - litigation
  - memo
  - summary
  - transactional
---

# Advance Directive vs. POLST/MOLST Comparison

## Why This Skill Exists

Clients — and sometimes clinicians — routinely confuse advance directives with POLST forms, leading to dangerous gaps. A healthy 45-year-old signs a POLST at a nursing home admission and gets denied lifesaving intubation after a car accident. A terminally ill patient relies solely on an advance directive that EMS can't act on at the scene. These are real failure modes. The two documents occupy different legal and clinical lanes, and when they conflict, the result is ambiguity at the worst possible moment.

This skill produces a calibrated comparison that helps clients (and their attorneys) understand which document does what, when each is appropriate, and how to keep them consistent.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Client's state(s) of residence** — required before making any state-specific claim about form names, execution requirements, or EMS recognition
2. **Existing documents** — whether client has a current advance directive, POLST/MOLST, or neither
3. **Health status** — generally healthy / chronic illness / serious illness / advanced frailty / terminal (determines whether POLST is clinically appropriate)
4. **Care settings** — home, hospital, SNF, assisted living (affects which forms matter most)
5. **Named healthcare agent** — whether appointed, available, and whether successors are named
6. **Client's primary question** — tailor output to the specific concern: "Which form wins in an emergency?", "Do I need a doctor's signature?", "Will this be honored out of state?", "Are my documents consistent?"

**If the user doesn't respond**, apply and clearly label these defaults: general comparison without state-specific claims; healthy adult context; educational memo format.

> If state is unknown, ask before making any jurisdiction-specific statement.

---

## Step 1: Build the Core Distinction Table

| Feature | Advance Directive | POLST / MOLST |
|---|---|---|
| **Nature** | Legal planning document | Clinician-signed medical order |
| **Purpose** | Appoints agent; expresses values and instructions | Translates current preferences into actionable orders |
| **Who signs** | Principal (+ witnesses/notary per state law) | Clinician (MD/DO; NP/PA in many states `[VERIFY]`) + patient or rep |
| **Who it instructs** | Agents, families, downstream clinicians | EMS, hospitals, facilities — immediately actionable |
| **Scope** | Broad: values, agent authority, end-of-life wishes | Specific: CPR, hospitalization, ventilation, artificial nutrition |
| **Appropriate for** | All competent adults | Patients with serious illness, advanced frailty, or limited life expectancy |
| **EMS usability** | Generally not — cannot be acted on at scene | Yes — designed for portability across care settings |
| **Clinician signature required?** | No | **Yes — without it, the form is not a valid order** |

---

## Step 2: Explain Emergency Precedence

Operational reality: **POLST/MOLST takes practical precedence in the field.**

- EMS is trained to look for medical orders, not legal documents. A multi-page living will in a file cabinet will not be reviewed during active resuscitation.
- If a POLST says "Do Not Attempt Resuscitation," EMS will generally follow it. If only an advance directive is present, EMS may default to treatment.
- **Once the patient reaches the hospital and the named agent is present**, the agent has legal authority (from the advance directive) to request the physician revoke or modify the POLST.
- If the patient is conscious and has capacity, their contemporaneous wishes generally control, regardless of prior documents.

> Do not promise that "EMS will always follow" any specific form. Availability, local protocol, and validity determine what gets followed. Some states maintain electronic POLST registries; some require specific colored paper (often bright pink or lime green) for EMS recognition. Verify via state program or local EMS authority.

---

## Step 3: Assess Clinical Appropriateness

POLST is **not** a universal planning tool for healthy adults.

Use the **"Surprise Question"** heuristic: *Would you be surprised if this patient died in the next year?* If yes → POLST may be premature. A healthy client involved in a treatable accident could be denied lifesaving temporary intubation by a prematurely signed POLST.

> **Nursing home admission warning**: Facilities sometimes present POLST forms as routine intake paperwork. Clients should not sign without a meaningful goals-of-care discussion with their physician about actual prognosis.

---

## Step 4: Explain How They Work Together

Best practice: the advance directive provides the values framework and agent authority; the POLST reflects current clinical goals as orders. They must be consistent.

**If they conflict** (e.g., directive says "do everything," POLST says "DNR"): clinicians often follow the most current, most specific, properly signed order — but this is state-dependent and creates dangerous ambiguity. Treat inconsistency as an urgent update problem.

**Agent's role**: The agent named in the advance directive is a legally authorized representative who can participate in POLST discussions and request physician updates — but cannot unilaterally revoke a POLST. Modifying a POLST requires a clinician to cancel the prior order and issue a new one.

**Practical access**: Advance directive should be accessible to prove agent authority at the hospital. POLST must be physically accessible to EMS — posted on the refrigerator, at the front of the medical chart, or in a state registry if available.

---

## Step 5: Produce the Deliverable

Draft a short memo or client handout covering:

- Definitions of each document (plain language)
- Who signs each and why the clinician signature is essential for POLST
- What happens in an emergency (practical, scenario-based)
- Whether POLST is clinically appropriate given client's health status
- How to ensure consistency between both documents
- Concrete next steps (update directive / initiate POLST conversation with physician / void outdated POLST copies)

Use the advance directive = "constitution," POLST = "executive order" analogy to orient clients.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the comparison, ask:

1. Does this answer the specific question you had about your documents?
2. Do you have both documents, and are they consistent with each other?
3. Would you like help drafting or updating either document (separate skill)?
4. Are there out-of-state care scenarios we should address for portability?

If the user doesn't answer, recommend a consistency review if the client has both documents, and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- [ ] Core distinction table included and accurate
- [ ] Emergency precedence explained in practical, scenario-based terms
- [ ] Clinical appropriateness assessed based on client's health status
- [ ] No state-specific claims made without verified jurisdiction
- [ ] POLST form name matches state terminology (POLST/MOLST/MOST/POST/TPOPP)
- [ ] Agent role and limitations clearly explained
- [ ] Consistency between documents addressed
- [ ] All statutory citations verified or marked `[VERIFY]`
- [ ] Concrete next steps provided
- [ ] Disclaimer included: general legal information, not legal advice
- [ ] No medical advice given (e.g., which POLST boxes to check)

---

## Guidelines

**Terminology** — adapt to state's labels before finalizing output:

| State Acronym | States Using It |
|---|---|
| POLST | CA, OR, WA, and others |
| MOLST | NY, MD |
| MOST | NC, SC |
| POST | ID, TN, UT, WV, and others |
| TPOPP | MN |
| Out-of-Hospital DNR only | FL, TX (more limited scope) |

Verify via [National POLST program directory](https://polst.org/) before asserting any state's form name or program status.

**State-specific rules — do not guess:**
- Advance directive witnessing/notarization requirements vary materially — ask for state, then verify
- POLST signer eligibility (physician-only vs. NP/PA authorized) is state-specific `[VERIFY per jurisdiction]`
- Illustrative citations requiring verification:
  - CA: Cal. Probate Code § 4780 et seq. `[VERIFY]`
  - NY: Public Health Law Art. 29-CCC `[VERIFY]`
  - TX: Health & Safety Code Ch. 166 `[VERIFY]`

**Anti-Hallucination:**
- Do not draft either document (out of scope — use a separate drafting skill)
- Do not invent statutory citations or case names
- Do not state who can sign a POLST in a given state without verification
- Do not provide medical advice (e.g., which POLST boxes to check)
- Do not promise that any document "will always be honored"
- Do not advise one family member how to prevail over another in a dispute

**Scope boundary**: This skill explains and compares — it does not draft, determine capacity, or resolve validity disputes.

**ATTORNEY AND CLINICIAN REVIEW REQUIRED** — Include explicit disclaimer: *This is general legal information, not legal advice. Review with a licensed attorney before use in any client matter and with a licensed clinician before any medical decisions are implemented.*
