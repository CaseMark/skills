---
name: ca-discovery-verification
description: >
  Drafts California Superior Court discovery verification pages for interrogatory
  responses (CCP 2030.250) and inspection/RPD responses (CCP 2031.250). Use this
  skill when the user mentions California discovery verification, CCP 2015.5
  perjury declaration, verification page drafting, response verification, entity
  verification, individual verification, information-and-belief clause, or fixing
  unverified California discovery responses. Also trigger when the user references
  party vs. attorney signing requirements, penalty of perjury language for CA
  discovery, or asks for help with verification formatting. Even if the user
  just says "I need a verification page" or "draft the verification for these
  responses," use this skill. California Superior Court only — not for federal
  court without modification.
tags:
  - drafting
  - litigation
---

# California Discovery Verification

## Why This Skill Exists

Unverified California discovery responses are treated as no response at all — the responding party waives all objections and the propounding party can move to compel as if nothing was served (*Appleton v. Superior Court* (1988) 206 Cal.App.3d 632 [VERIFY]). Yet verification defects are rampant: attorneys sign where parties must, perjury language omits required jurisdictional references, verification titles don't match response titles, and entity signers lack stated authority. Each of these creates a fatal defect that hands the opponent a motion to compel on a silver platter.

This skill produces correctly formatted California verification pages with the right signer capacity, knowledge basis, and CCP § 2015.5 perjury declaration — ready for the party's signature.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Discovery device type** — interrogatories (Form/Special) or inspection demand/RPD
2. **Exact response title** — as it will appear on the responses (verification title must match verbatim)
3. **Court name, case number, and party names** — for the caption
4. **Responding party type** — individual or entity (corporation, LLC, partnership)
5. **Signer identity** — exact legal name, title/role, and authority basis (for entities)
6. **Knowledge basis** — personal knowledge only, or information and belief needed
7. **Execution details** — date, city, state, signature method

**If the user doesn't respond**, apply and clearly label these defaults: individual party; personal knowledge with information-and-belief clause; interrogatory verification.

> The finalized response set must exist before verification is drafted — do not verify responses that haven't been finalized.

---

## Step 1: Select Verification Type

| Decision | Use | Statute |
|---|---|---|
| Interrogatories (Form/Special) | Interrogatory Verification | CCP § 2030.250 |
| Inspection demand / RPD | Inspection/RPD Verification | CCP § 2031.250 |
| Federal court | Do not use CCP form; use FRCP 33/34 + 28 U.S.C. § 1746 | [VERIFY] |

---

## Step 2: Select Knowledge Basis Clause

| If | Use This Clause |
|---|---|
| All responses are truly personal knowledge | "The matters stated in the foregoing responses are true of my own knowledge." |
| Any response relies on records, employees, or collected information | "The matters stated in the foregoing responses are true of my own knowledge, except as to those matters stated on information and belief, and as to those matters I believe them to be true." |

---

## Step 3: Draft Verification Page

### Interrogatory Verification — Individual
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

### Interrogatory Verification — Entity
```text
[CAPTION BLOCK]

VERIFICATION OF [ENTITY NAME] TO [EXACT RESPONSE TITLE]

I am the [TITLE] of [ENTITY NAME], a party to this action, and am authorized to make this verification for and on its behalf. I have read the foregoing responses and know the contents thereof.
[CHOOSE KNOWLEDGE BASIS CLAUSE]
[OPTIONAL: "I am informed by the employees and records of [ENTITY NAME] regarding the matters stated."]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

[ENTITY NAME]
By: _______________________
    [SIGNER NAME]
    Its: [TITLE]
```

### Inspection/RPD Verification — Individual
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

### Inspection/RPD Verification — Entity
```text
[CAPTION BLOCK]

VERIFICATION OF [ENTITY NAME] TO [EXACT RESPONSE TITLE]

I am the [TITLE] of [ENTITY NAME], a party to this action, and am authorized to make this verification for and on its behalf. I have read the foregoing responses and know the contents thereof.
[CHOOSE KNOWLEDGE BASIS CLAUSE]
[OPTIONAL: "I am informed by the employees and records of [ENTITY NAME] regarding the matters stated."]

I declare under penalty of perjury under the laws of the State of California that the foregoing is true and correct.
Executed on [DATE], at [CITY], [STATE].

[ENTITY NAME]
By: _______________________
    [SIGNER NAME]
    Its: [TITLE]
```

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the verification page, ask:

1. Does the verification title match the response document title exactly?
2. Is the signer the correct person with proper authority (especially for entities)?
3. Is the knowledge basis clause appropriate — personal knowledge only, or information and belief?
4. Will the verification be executed in California, or does out-of-state execution require adjustment?

If the user doesn't answer, recommend double-checking the title match and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Verification title matches the response title verbatim
- Signer capacity stated and authority clear (entity/agent)
- CCP § 2015.5 perjury declaration is verbatim: "under the laws of the State of California"
- Execution date and city/state included
- Signature block includes name and capacity
- No statement that the signer verifies objections (attorney signs for objections)
- Knowledge basis clause matches the actual basis of the responses
- Entity verification includes authorization language
- Federal court not using CCP form (redirect to FRCP/28 U.S.C. § 1746)
- No attorney signature where party signature is required

---

## Guidelines

- Match the verification title to the response title exactly; mismatches invite motions to compel
- Do not use attorney-signed verifications except in narrow CCP § 446 circumstances [VERIFY]
- Do not state "personal knowledge" if the signer relied on records or others; use information-and-belief clause
- Do not verify legal objections; attorney signs the response document for objections
- Use CCP § 2015.5 declaration verbatim; include date and city/state of execution
- Do not add notarization unless a court order or client policy requires it
- Unverified responses can be treated as no response, risking waiver and sanctions (*Appleton v. Superior Court* (1988) 206 Cal.App.3d 632 [VERIFY])
- Perjury exposure applies to false verifications (Cal. Penal Code § 118) [VERIFY]
- Federal court requires FRCP 33/34 and 28 U.S.C. § 1746, not CCP § 2015.5 [VERIFY]
- Confirm local rules and entity signing authority before finalizing
- **Anti-hallucination** — all case citations must be verified or flagged `[VERIFY]`; do not invent case law
- **Attorney review required** — all output must be reviewed by supervising counsel before any verification is sent for signature or served
