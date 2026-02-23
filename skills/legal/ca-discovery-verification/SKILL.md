---
name: ca-discovery-verification
description: Drafts California Superior Court discovery verification pages for interrogatory responses (CCP 2030.250) and inspection/RPD responses (CCP 2031.250), including CCP 2015.5 perjury declarations, entity vs individual capacity language, and personal-knowledge vs information-and-belief options. Use when drafting discovery verifications, response verification pages, CCP 2015.5 declarations, or fixing unverified CA discovery responses.
tags:
  - drafting
  - litigation
---

# California Discovery Verification

Builds California-compliant discovery verification pages tied to interrogatory or RPD/inspection responses.

## Prerequisites

1. Discovery device type and exact response title as it will appear on the responses
2. Court name, case number, and party names for the caption
3. Responding party type and exact legal name
4. Signer name, title/role, and authority basis (entity/agent)
5. Knowledge basis for responses (personal knowledge vs information and belief)
6. Execution details: date, city, state, signature method
7. Finalized response set to be verified

## Output Structure / Process

**Decision Matrix**

| Decision | Use | Statute |
| --- | --- | --- |
| Interrogatories (Form/Special) | Interrogatory Verification | CCP 2030.250 |
| Inspection demand / RPD | Inspection/RPD Verification | CCP 2031.250 |
| Federal court | Do not use CCP form; use FRCP 33/34 + 28 U.S.C. 1746 | [VERIFY] |

**Knowledge Basis Clause**

| If | Use this clause |
| --- | --- |
| All responses are truly personal knowledge | “The matters stated in the foregoing responses are true of my own knowledge.” |
| Any response relies on records, employees, or collected information | “The matters stated in the foregoing responses are true of my own knowledge, except as to those matters stated on information and belief, and as to those matters I believe them to be true.” |

**Required Elements Checklist**

- [ ] Verification title matches the response title verbatim
- [ ] Signer capacity stated and authority clear (entity/agent)
- [ ] CCP 2015.5 perjury declaration is verbatim
- [ ] Execution date and city/state included
- [ ] Signature block includes name and capacity
- [ ] No statement that the signer verifies objections

**Templates**

Interrogatory Verification (Individual)
```text
[CAPTION BLOCK]

VERIFICATION OF [PARTY NAME] TO [EXACT RESPONSE TITLE]

I am the [plaintiff/defendant] in this action. I have read the foregoing responses and know the contents thereof.
[CHOOSE KNOWLEDGE BASIS CLAUSE]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

___________________________
[SIGNER NAME]
[Plaintiff/Defendant]
```

Interrogatory Verification (Entity)
```text
[CAPTION BLOCK]

VERIFICATION OF [ENTITY NAME] TO [EXACT RESPONSE TITLE]

I am the [TITLE] of [ENTITY NAME], a party to this action, and am authorized to make this verification for and on its behalf. I have read the foregoing responses and know the contents thereof.
[CHOOSE KNOWLEDGE BASIS CLAUSE]
[OPTIONAL: “I am informed by the employees and records of [ENTITY NAME] regarding the matters stated.”]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

[ENTITY NAME]
By: _______________________
    [SIGNER NAME]
    Its: [TITLE]
```

Inspection/RPD Verification (Individual)
```text
[CAPTION BLOCK]

VERIFICATION OF [PARTY NAME] TO [EXACT RESPONSE TITLE]

I am the [plaintiff/defendant] in this action. I have read the foregoing responses and know the contents thereof.
[CHOOSE KNOWLEDGE BASIS CLAUSE]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

___________________________
[SIGNER NAME]
[Plaintiff/Defendant]
```

Inspection/RPD Verification (Entity)
```text
[CAPTION BLOCK]

VERIFICATION OF [ENTITY NAME] TO [EXACT RESPONSE TITLE]

I am the [TITLE] of [ENTITY NAME], a party to this action, and am authorized to make this verification for and on its behalf. I have read the foregoing responses and know the contents thereof.
[CHOOSE KNOWLEDGE BASIS CLAUSE]
[OPTIONAL: “I am informed by the employees and records of [ENTITY NAME] regarding the matters stated.”]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

[ENTITY NAME]
By: _______________________
    [SIGNER NAME]
    Its: [TITLE]
```

## Guidelines

- Match the verification title to the response title exactly; mismatches invite motions to compel.
- Do not use attorney-signed verifications except in narrow CCP 446 circumstances [VERIFY].
- Do not state “personal knowledge” if the signer relied on records or others; use information-and-belief clause when needed.
- Do not verify legal objections; attorney signs the response document for objections.
- Use CCP 2015.5 declaration verbatim; include date and city/state of execution.
- Do not add notarization unless a court order or client policy requires it.
- Unverified responses can be treated as no response, risking waiver and sanctions (Appleton v. Superior Court (1988) 206 Cal.App.3d 632) [VERIFY].
- Perjury exposure applies to false verifications (Cal. Penal Code § 118) [VERIFY].
- Federal court requires FRCP 33/34 and 28 U.S.C. 1746, not CCP 2015.5 [VERIFY].
- Confirm local rules and entity signing authority before finalizing.
- Attorney review required before any verification is sent for signature or served.
