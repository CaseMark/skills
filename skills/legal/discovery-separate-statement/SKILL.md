---
name: discovery-separate-statement
description: >
  Drafts and quality-controls a California-compliant discovery Separate Statement
  for motions to compel under Cal. Rules of Court rule 3.1345. Use this skill
  when the user mentions California motion to compel, further responses, Separate
  Statement, Rule 3.1345, CCP 2023.030 sanctions, discovery motion support,
  interrogatory disputes, RFP disputes, RFA disputes, or deposition-question
  disputes in California Superior Court. Also trigger when the user references
  verbatim request-response formatting, meet-and-confer documentation for CA
  motions, or asks for help with California discovery motion practice. Even if
  the user just says "I need a sep stat" or "help me with this compel motion
  in California," use this skill.
tags:
  - analysis
  - drafting
  - litigation
  - motion
  - pleading
---

# California Discovery Separate Statement Generator

## Why This Skill Exists

California motions to compel further responses require a Separate Statement under Cal. Rules of Court rule 3.1345 — without it, the motion is procedurally defective and may be denied on that basis alone. The Separate Statement must reproduce verbatim text of each disputed request and response, making it the most labor-intensive and error-prone document in California discovery motion practice. Paraphrasing, misquoting, or omitting adverse language creates ammunition for opposition and risks sanctions.

This skill produces a request-by-request Separate Statement that is complete, quote-accurate, and aligned with the rest of the motion package — memorandum, declaration, and proposed order.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Governing discovery set** — discovery requests at issue (propounding text, all instructions, relevant definitions) and latest served responses, including objections, qualifications, subject-to language, verification status, and any production references
2. **Meet-and-confer record** — all notices, emails, letters, and declarations with dates; any concessions, narrowing, or supplements
3. **Case framing** — complaint and answer (claims, theories, defenses tied to each request); protective orders, ESI protocols, confidentiality agreements, sealing orders
4. **Motion posture** — motion type (compel further responses, failure-to-respond, etc.); proposed relief and hearing date; deadline calculation method including service method for 45-day filing windows
5. **Court requirements** — department/county local preferences (IDC/JCCP requirements, exhibit format preferences, filing quirks); judicial preferences for tables vs. sequential text

**If the user doesn't respond**, apply and clearly label these defaults: motion to compel further responses; all disputed requests included; sequential text format; sanctions requested under CCP § 2023.030.

> If verbatim request/response text is missing, halt and request it before drafting. This is non-negotiable for a Separate Statement.

---

## Step 1: Validate Intake and Classify Motion

Produce a single-line taxonomy memo and compliance gap check:

| Input | Required Output |
|---|---|
| Motion theory | Single-line taxonomy memo |
| Motion scope | Discovery set list and item identifiers |
| Relief targets | Specific item-level remedies |
| Compliance gaps | Missing text/date conflicts identified before drafting |

Template: `Taxonomy: Motion to compel further responses to [device/set]: Nos. [range], plus [relief/sanctions].`

Decision rule:
- Further-response motion with served response and deficiencies: generally requires Separate Statement (Cal. R. Ct. 3.1345(a)) [VERIFY].
- Pure failure-to-respond contexts may use alternate CCP tracks [VERIFY].

---

## Step 2: Build the Disputed-Item Ledger

Create one row per disputed item — this is the source-lock table that prevents drift:

| Item ID | Discovery Device | Request Text Source | Response Source | Last Service Date | Dispute Type |
|---|---|---|---|---|---|
| RFA-1-8 | RFA | RFA Set One No. 8 | Response served 3/01/2026 | 3/01/2026 | Evasive response |
| RFP-2-12 | RFP | RFP Set Two No. 12 | Supplemental response 3/15/2026 | 3/15/2026 | No definitive production statement |

Rules:
- Copy request and response verbatim, punctuation included
- If response references another response, include referenced text inline
- Preserve "subject to and without waiving" language and all qualifications
- If only "no response at all" exists, flag as failure-to-respond posture and branch logic

---

## Step 3: Draft Per-Item Micro-Structure

Use the same structure for every disputed item:

```text
REQUEST [ID]:
[verbatim request + relevant definitions]

RESPONSE:
[verbatim response + objections + any qualifications + supplemental text]

MEET-AND-CONFER:
[date, issue raised, cure requested, response, supplemental status]

FACTS AND LEGAL REASONS:
[device-specific deficiency analysis + relevance to pleadings + legal authority + burden/privacy handling]

ORDER SOUGHT:
[single, enforceable, narrow, date-certain remedy]
```

Formatting: Prefer clear labeled blocks for e-filing stability. Use two-column tables only if court preference supports it and consistent with PDF behavior.

---

## Step 4: Apply Device-Specific Reasons

| Device | Deficiency Focus | Typical Orderable Remedy |
|---|---|---|
| Interrogatory (CCP §§ 2030.210–2030.310) [VERIFY] | Non-verified, incomplete, evasive, unexplained unknowns | Further verified response; detailed inability statement |
| Production (CCP §§ 2031.210–2031.320) [VERIFY] | "Will comply" only, incomplete/no-search showing, privilege without log | Further production by custodian/date/topic/form; privilege log with required specificity |
| Admission (CCP §§ 2033.210–2033.300) [VERIFY] | Boilerplate objections, qualified/noncommittal admissions | Clear admit/deny response; strike unsupported objections |
| Deposition question disputes | Refusal/inadequate answer, privilege overreach | Further response or appearance stipulation/production order |

### Reasons and Privilege/Privacy Integration

- Tie every reasons paragraph to a pleaded issue (liability, damages, causation, impeachment)
- Privacy/trade secret claims: include narrowing, redaction, protective measures, or AEO language
- Burden objections: require evidentiary support before crediting the claim; flag lack of declaration/evidence

---

## Step 5: Draft Remedies and Sanctions

Keep relief narrow and court-enforceable:
- Further response without objections
- Duty-to-state existence of documents
- Production by fixed date
- Privilege log
- Verified inability-to-comply statement

If seeking sanctions under CCP § 2023.030 [VERIFY], identify conduct item-by-item and align with motion language. Avoid introducing new substantive requests not in original discovery unless explicitly narrowed with justification.

---

## Step 6: Run Consistency Pass

- Verify each quoted request/response matches exhibits page-accurate
- Cross-check that request IDs, dates, and relief language are identical across memorandum, declaration, and Separate Statement
- Remove moot/fully cured items after supplemental responses
- Keep chronology factual and non-hyperbolic

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial Separate Statement, ask:

1. Does the Separate Statement cover the correct set of disputed requests — any to add or remove?
2. Are the meet-and-confer summaries accurate and complete for each item?
3. Does the relief sought per item match what is requested in the memorandum and proposed order?
4. Are there any court-specific formatting requirements I should adjust for?

If the user doesn't answer, recommend a consistency cross-check against the memorandum and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- All requests and responses reproduced verbatim — no paraphrasing
- Motion type correctly identified and consistent throughout
- Every item has meet-and-confer support documented
- Deadline + service method verified and noted
- All statutory/case citations verified or marked `[VERIFY]`
- Relief language is enforceable and date-certain
- Request IDs, dates, and party names consistent across all motion documents
- No moot or fully cured items remaining
- Device-specific deficiency analysis applied correctly
- Privacy/privilege handling includes narrowing proposals
- Attorney verification flags present for all uncertainties

---

## Guidelines

- Do not draft from paraphrased memory; use source documents only
- Do not include arguments better placed in the memorandum
- Do not overstate meet-and-confer efforts
- Do not omit adverse response portions that weaken your position
- Do not copy citations from memory without verification; flag doubtful law with `[VERIFY]`
- Use California terminology and avoid federal substitutions unless user confirms federal/local rules override
- Respect CRPC duties: competence (1.1) [VERIFY], candor (3.3) [VERIFY], confidentiality (1.6) [VERIFY], fairness (3.4) [VERIFY]
- **Anti-hallucination** — all case citations must be verified or left as explicit attorney-fill placeholders; no plausible-sounding but unverified citations
- **Attorney review required** — all output is practice-support work product; it must be reviewed by supervising counsel before filing or service
