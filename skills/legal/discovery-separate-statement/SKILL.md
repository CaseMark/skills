---
name: discovery-separate-statement
description: Drafts and quality-controls a California-compliant discovery Separate Statement for motions to compel under Cal. Rules of Court rule 3.1345 using verbatim discovery requests/responses, meet-and-confer history, and tailored orderable relief. Use when preparing motion support for interrogatories, inspections/requests for production, requests for admission, or deposition-question disputes. Supports trigger scenarios involving “motion to compel,” “further responses,” “California discovery,” “Rule 3.1345,” “separate statement,” and “2023.030 sanctions.”
tags:
  - analysis
  - drafting
  - litigation
  - motion
  - pleading
---

# California Discovery Separate Statement Generator

Produces a request-by-request Separate Statement that is complete, quote-accurate, and aligned with the rest of the motion package.

## Prerequisites

1. **Governing discovery set**
   - Discovery requests at issue (propounding text, all instructions, relevant definitions).
   - Latest served responses, including objections, qualifications, subject-to language, verification status, and any clarifying production references.

2. **Meet-and-confer record**
   - All notices, emails, letters, and declarations with dates.
   - Any concessions, narrowing, or supplements.

3. **Case framing**
   - Complaint and answer (including claims, theories, and defenses tied to each request).
   - Protective orders, ESI protocols, confidentiality agreements, and sealing orders.

4. **Motion posture**
   - Motion type (motion to compel further responses, failure-to-respond, etc.).
   - Proposed relief and hearing date.
   - Deadline calculation method (including service method) for 45-day filing windows (verify against CCP timing rules).

5. **Court requirements**
   - Department/county local preferences (IDC/JCCP requirements, exhibit format preferences, filing quirks).
   - Judicial preferences for tables vs sequential text.

If any required item is missing—especially verbatim request/response text—halt and request it before drafting.

## Output Structure / Process

### 1) Intake validation and motion taxonomy

| Input | Required output |
| --- | --- |
| Motion theory | Single-line taxonomy memo |
| Motion scope | Device set list and item identifiers |
| Relief targets | Specific item-level remedies |
| Compliance gaps | Missing text/date conflicts identified before drafting |

Template (first output paragraph):
`Taxonomy: Motion to compel further responses to [device/set]: Nos. [range], plus [relief/sanctions].`

Decision rule:
- Further-response motion with served response and deficiencies: generally requires Separate Statement (Cal. R. Ct. 3.1345(a)) [VERIFY].
- Pure failure-to-respond contexts may use alternate CCP tracks [VERIFY].

### 2) Build disputed-item ledger (source lock)

Create one row per disputed item.

| Item ID | Discovery device | Request text source | Response source | Last service date | Dispute type |
| --- | --- | --- | --- | --- |
| RFA-1-8 | RFA | RFA Set One No. 8 | Response served 3/01/2026 | Evasive response |
| RFP-2-12 | RFP | RFP Set Two No. 12 | Supplemental response 3/15/2026 | No definitive production statement |

Rules:
- Copy request and response verbatim, punctuation included.
- If response references another response, include referenced text inline.
- Preserve "subject to and without waiving" language and all qualifications.
- If only "no response at all" exists, flag as failure-to-respond posture and branch logic.

### 3) Per-item drafting micro-structure

Use the same structure for every item:

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

Formatting:
- Prefer clear labeled blocks for e-filing stability.
- If court preference supports it, use two-column tables where consistent with PDF behavior.

### 4) Device-specific reasons matrix

| Device | Deficiency focus | Typical orderable remedy |
| --- | --- | --- |
| Interrogatory (CCP §§2030.210–2030.310) [VERIFY] | Non-verified, incomplete, evasive, unexplained unknowns | Further verified response; detailed inability statement |
| Production (CCP §§2031.210–2031.320) [VERIFY] | “Will comply” only, incomplete/no-search showing, privilege without log | Further production by custodian/date/topic/form; privilege log with required specificity [VERIFY] |
| Admission (CCP §§2033.210–2033.300) [VERIFY] | Boilerplate objections, qualified/nonnoncommittal admissions | Clear admit/deny response, strike unsupported objections |
| Deposition question disputes | Refusal/inadequate answer, privilege overreach | Further response or appearance stipulation/production order |

### 5) Reasons and privilege/privacy integration

- Tie every reasons paragraph to a pleaded issue (liability, damages, causation, impeachments).
- Privacy/trade secret claims: do not ignore; include narrowing, redaction, protective measures, or AEO language.
- Burden objections: require evidentiary support before crediting the claim; flag lack of declaration/evidence.

### 6) Remedies, sanctions, and proportionality

- Keep relief narrow and court-enforceable:
  - further response without objections
  - duty-to-state existence of documents
  - production by fixed date
  - privilege log
  - verified inability-to-comply statement
- If seeking sanctions under CCP §2023.030 [VERIFY], identify conduct item-by-item and align with motion language.
- Avoid introducing new substantive requests not in original discovery unless explicitly narrowed with justification.

### 7) Final lock and consistency pass

- Verify each quoted request/response matches exhibits page-accurate.
- Cross-check that request IDs, dates, and relief language are identical across:
  - Memorandum
  - Declaration
  - Separate Statement
- Remove moot/fully cured items after supplemental responses.
- Keep chronology factual and non-hyperbolic.

## Output Artifact Template

| Section | Content requirement |
| --- | --- |
| Header | Case caption, motion title, date, hearing info |
| Disputed item rows/blocks | Full request/response and reasons in order |
| Remedies | Item-specific relief |
| Verbatim accuracy controls | Note that all text is quoted from served documents |
| Attorney verification flags | Unverified authorities, deadlines, court-specific preferences |

```text
REVIEW CHECKLIST (before handoff):
- All requests/responses verbatim? yes/no
- Motion type correct? yes/no
- Any item lacking meet-and-confer support? yes/no
- Deadline + service method verified? yes/no
- All statutory/case citations verified? yes/no
- Attorney approval completed? yes/no
```

## Guidelines

- Do not draft from paraphrased memory; use source documents only.
- Do not include arguments better placed in the memorandum.
- Do not overstate meet-and-confer efforts.
- Do not omit adverse response portions that weaken your position.
- Do not copy citations from memory without verification; flag doubtful law with `[VERIFY]`.
- Use California terminology and avoid federal substitutions unless user confirms federal/local rules override.
- Respect CRPC duties: competence (1.1) [VERIFY], candor (3.3) [VERIFY], confidentiality (1.6) [VERIFY], fairness (3.4) [VERIFY].
- Default output includes explicit attorney-verification flags for any uncertainty and must be reviewed before filing/service.
