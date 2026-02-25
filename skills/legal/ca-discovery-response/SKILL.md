---
name: ca-discovery-response
description: >
  Drafts service-ready California responses to Requests for Production under
  CCP § 2031.010 et seq. Use this skill when the user mentions California RFP
  responses, requests for production responses, CCP 2031, California discovery
  drafting, compliance statements, inability to comply, discovery objections,
  privilege objections, privacy objections, or California Superior Court
  discovery. Also trigger when the user references Bates numbering for
  California productions, verification requirements for RFPs, or asks for help
  responding to document requests in California state court. Even if the user
  just says "draft responses to these RFPs" or "help me respond to this
  production request in CA," use this skill. California Superior Court only —
  not for federal court without substantial modification.
tags:
  - drafting
  - litigation
  - pleading
---

# California Discovery Response Builder

## Why This Skill Exists

California RFP responses are governed by a rigid three-option statutory framework (compliance, inability, objection) under CCP §§ 2031.210–2031.320. Getting it wrong invites motions to compel and sanctions, but the most common failure is not outright error — it is boilerplate objections that lack factual specificity, over-objecting that signals obstruction, and under-responding that creates binding admissions. Each response must be drafted for the judge who will review it on a motion to compel, not just the opposing counsel who receives it.

This skill produces code-compliant responses with attorney-confirmed details at marked placeholders, ready for verification and service.

**Scope**: California state court RFP responses only. For federal court (FRCP 34), warn the user and do not proceed without substantial modification.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Full RFP set** — including all definitions, instructions, and attachments
2. **Case metadata** — exact caption, case number, county, department, assigned judge
3. **Attorney information** — name, bar number, firm, address, phone, fax, email (both sides)
4. **Service details** — date served, method (email/mail/personal) → determines deadline
   - 30 days after service (CCP § 2031.260)
   - Extensions for mail (CCP § 1013) and electronic service (CCP § 1010.6)
   - `[ATTORNEY: CONFIRM RESPONSE DEADLINE — MISSED DEADLINE MAY WAIVE ALL OBJECTIONS]`
5. **Document universe** — what categories exist, where stored, who controls, sensitivity
6. **Privilege status** — documents withheld on privilege/work product grounds? Privilege log timing?
7. **Formatting preference** — pleading paper (28-line) vs. clean service format
8. **Case type** — personal injury, employment, contract, coverage/bad faith, etc. (objection strategies differ)

**If the user doesn't respond**, apply and clearly label these defaults: hybrid objection + conditional compliance approach; clean service format; personal injury case type; standard privacy and overbreadth objections.

---

## Step 1: Parse and Reproduce Requests

Reproduce every request **verbatim** including subparts, defined terms, and time limits. Mirror the propounding party's numbering convention. Include definitions section if extensive.

---

## Step 2: Classify Each Request

Select response per CCP § 2031.210(a):

| Response Type | Statute | When to Use |
|---|---|---|
| Compliance (full/partial) | § 2031.220 | Documents exist, no valid objection |
| Inability to comply | § 2031.230 | Documents don't exist or aren't in possession/custody/control |
| Objection | § 2031.240 | Request is improper, overbroad, or seeks privileged material |
| Objection + conditional compliance | Common | Object to scope but still produce non-privileged responsive documents |

---

## Step 3: Draft Objections

Objections must be **specific to the request, fact-tethered, and legally grounded**. No boilerplate.

**Objection Modules** (adapt to each request — never paste blindly):

- **Overbreadth/proportionality**: Explain why not limited by time/subject/custodians. State the reasonable construction under which you will search.
- **Vagueness**: Identify specific unclear terms. State the construction under which you respond.
- **Attorney-client privilege**: Evid. Code § 954. State documents are withheld and privilege log will be provided per CCP § 2031.240(c)(1).
- **Work product**: CCP § 2018.030. Distinguish qualified (impressions/opinions) from other work product.
- **Privacy**: Cal. Const., Art. I, § 1. Limit production to injuries/damages at issue. Propose protective order.
- **Insurance** (case-type dependent): In routine PI, insurance generally irrelevant. In coverage/bad faith, fully discoverable — don't object.
- **Lien-related** (case-type dependent): Collateral source rule, privacy. Tailor to specific lien situation.
- **Expert materials**: Draft communications and consulting expert materials get stronger protection. Testifying expert reports must be disclosed.

**Citation integrity**: Rely on statutory citations (CCP, Evid. Code) over case law. Mark any case citation `[VERIFY CITATION BEFORE SERVICE]`.

---

## Step 4: Draft Substantive Responses

**Compliance**:
> Subject to and without waiving the foregoing objections, Responding Party will comply with this Request. Responsive, non-privileged documents are being produced concurrently herewith as Bates Nos. [INSERT BATES RANGE: _____ to _____].

State whether production is "as kept in ordinary course of business" or "organized and labeled to correspond" (CCP § 2031.280(a)).

**Inability to comply** (CCP § 2031.230):
> After a diligent search and reasonable inquiry, Responding Party is unable to comply. [SPECIFY: documents have never existed / are not in possession, custody, or control / were in possession of [IDENTIFY]]. Search included [DESCRIBE REPOSITORIES — ATTORNEY/CLIENT TO CONFIRM].

**ESI-specific**: Specify production format per CCP § 2031.280(c) — form ordinarily maintained or reasonably usable form.

---

## Step 5: Assemble Document

1. **Attorney information block**
2. **Court caption** — "SUPERIOR COURT OF THE STATE OF CALIFORNIA, COUNTY OF [COUNTY]"
3. **Case name and number** exactly as in operative pleading
4. **Document title**: "RESPONSES TO REQUESTS FOR PRODUCTION OF DOCUMENTS (SET [NUMBER])"
5. **Preliminary statement** — reservation of rights, ongoing investigation, supplementation reserved
6. **Numbered responses** — "REQUEST FOR PRODUCTION NO. [X]:" (verbatim) → "RESPONSE TO REQUEST FOR PRODUCTION NO. [X]:" (objections + response)
7. **Footer on every page**: "[PARTY]'S RESPONSES TO REQUESTS FOR PRODUCTION PROPOUNDED BY [PARTY] (SET [NUMBER])"

---

## Step 6: Add Verification and Proof of Service

**Verification** (CCP § 2031.250) — required unless response contains only objections:
> I, [NAME], am a party to this action. I have read the foregoing Responses and know the contents thereof. The matters stated therein are true of my own knowledge, except as to those matters stated on information and belief, and as to those I believe them to be true.

`[CLIENT MUST SIGN — ATTORNEY SIGNATURE IS NOT SUFFICIENT FOR VERIFIED RESPONSES]`

**Proof of service** — California format matching service method (email/mail/personal service). Include `[INSERT SERVICE LIST]` placeholder.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial responses, ask:

1. Are the response classifications (compliance / inability / objection) correct for each request?
2. Do the objections match your litigation strategy for this case type?
3. Are there any documents you want to produce that I haven't accounted for?
4. Should I generate the verification page and proof of service now, or will those be handled separately?

If the user doesn't answer, recommend reviewing the objection strategy against the case type and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Every response fits CCP § 2031.210 (compliance, inability, or objection)
- Requests reproduced verbatim — no paraphrasing
- Factual assertions based on user-provided information (not assumed)
- Bates range placeholders clearly marked `[INSERT BATES RANGE]`
- Party names, case number, set number consistent throughout
- Verification page included (if any substantive responses)
- Proof of service included
- All citations verified or marked `[VERIFY]`
- No "none exist" claims without described search
- Case-type-appropriate objections (not PI objections in a contract case)
- Hybrid responses include both objection and conditional compliance language
- ESI production format specified where applicable

---

## Guidelines

- Draft for the judge who will review on a motion to compel
- Hybrid responses (objection + conditional production) are the most common and defensible approach
- Over-objecting invites motions to compel and sanctions (CCP § 2031.310, § 2023.010)
- Under-responding creates admissions and constrains later testimony
- Adapt objection strategy to case type — insurance, lien, and privacy objections vary dramatically
- **Anti-hallucination** — all case citations must be verified or left as explicit placeholders; no plausible-sounding but unverified citations; rely on statutory citations over case law
- **Attorney review required** — all output is practice-support work product; it must be reviewed by supervising counsel before service or filing
- Ethics: comply with CRPC duties of competence, candor, and confidentiality [VERIFY specific rule numbers]
