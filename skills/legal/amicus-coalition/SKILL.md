---
name: amicus-coalition
description: >
  Manages end-to-end workflow for multi-organization amicus coalition briefs in
  appellate courts. Covers single-pen drafting governance, position alignment,
  controlled draft circulation, conflict resolution among diverse organizations,
  documented sign-offs, FRAP 29/Rule 37.6 funding and authorship disclosures,
  FRAP 26.1 corporate disclosures, technical cover/caption formatting for listing
  multiple amici, and compliant filing. Use this skill when coordinating coalition
  amicus briefs, managing amicus sign-offs, drafting joint friend-of-court briefs,
  handling multi-amici filing logistics, or resolving inter-organization drafting
  conflicts. Even if the user just says "we have 12 orgs joining this amicus"
  or "coordinate the coalition brief," use this skill.
tags:
  - brief
  - drafting
  - litigation
---

# Amicus Coalition Management

## Why This Skill Exists

Coalition amicus briefs amplify collective credibility — but they also multiply coordination failures. The most common disasters: unauthorized organizations listed on a filing, missed sign-off deadlines that force last-minute exclusions, disclosure statements that don't account for all members, version proliferation that creates confusion about the "real" draft, and unresolved policy disagreements that result in a brief that says nothing distinctive. A coalition brief that arrives late, lists an unauthorized amicus, or contains conflicting positions is worse than no brief at all.

This skill operationalizes the governance, drafting, conflict resolution, sign-off, and filing workflow so the brief ships on time with proper authorization from every listed organization.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Docket info** — court, case number, caption, all deadlines
2. **Parties' briefs** — opening, response, reply (as available); key orders
3. **Forum rules** — amicus brief rules (word/page limits, disclosure requirements, consent/leave rules, cover formatting, e-filing specs) `[VERIFY per forum]`
4. **Coalition roster** — full legal names, jurisdiction of incorporation, preferred display names, entity types
5. **Approval pathways** — authorized signatory per org, internal review chain, required lead time
6. **Red lines** — positions each org cannot support, factual assertions it cannot endorse
7. **Counsel-of-record details** — names, bar numbers, addresses; pro hac vice needs; filing system
8. **Funding/authorship disclosure inputs** — per FRAP 29(a)(4)(E) / Supreme Court Rule 37.6: (a) who authored, (b) who funded
9. **Posture** — supporting which party, or neither; consent status or need for motion for leave

**If the user doesn't respond**, apply and clearly label these defaults: FRAP 29 federal circuit rules; single-pen authority with lead counsel; hard sign-off cutoff 48 hours before filing deadline.

Do not proceed until all prerequisites are collected or gaps are flagged.

---

## Step 1: Establish Governance and Timeline

| Element | Action |
|---|---|
| Single-pen authority | Lead counsel controls final narrative and legal integrity; coalition provides input, not co-drafting |
| Authority map | For each org: who can commit to join, who approves final text, who can make public statements |
| Backward timeline | Build from filing deadline; include concept outline → near-final draft → final proof → sign-off cutoff |
| Hard cutoff | Orgs without sign-off by cutoff date are excluded — no "pending approval" listings |

Send a **Workflow Memo** to all members at kickoff:

```
To meet the filing deadline, please provide:
(1) One consolidated comment set by [DATE/TIME]
(2) Written authorization from an authorized approver to join by [DATE/TIME]
Absent authorization by that time, your organization will not be listed.
```

---

## Step 2: Align Positions and Identify Thesis

Before any full draft:

1. Gather each org's desired emphasis (economic, technical, historical, policy)
2. Cross-check against parties' briefs to eliminate duplication
3. Produce **Issue-Framing Memo** (1–2 pages): proposed argument headings, key factual propositions with reliable citations, proposed empirical/technical materials, brief's posture
4. Solicit red lines in writing:

```
Please confirm whether your organization can be listed in support of the
argument that [X]. Identify any positions you cannot endorse now.
```

---

## Step 3: Manage the Draft

| Rule | Rationale |
|---|---|
| One official draft, one sender | Prevents version proliferation |
| Naming: `AmicusCoalition_Brief_Draft[N]_YYYYMMDD` | Version integrity |
| One point person per org, one consolidated comment set | Avoids conflicting markups |
| Triage comments: (a) legal/argument, (b) factual/citation, (c) policy/branding | Legal clarity governs over branding |
| All internal markup confidential under Model Rule 1.6 | Do not forward outside coalition without permission |
| Late new sections require equal-length deletion proposal | Enforces word-limit discipline |

---

## Step 4: Resolve Conflicts

**Diagnose conflict type:**

| Type | Resolution |
|---|---|
| **Core** (org cannot be associated with the legal position) | Narrow the position, modularize language, or allow withdrawal |
| **Expressive** (disagreement on emphasis/phrasing) | Favor legal clarity and court credibility |

**Compromise patterns:**
- Statutory avoidance: *"This Court can and should resolve on statutory grounds; if it reaches constitutional issues, the proper framework is…"*
- Narrow consensus: *"Amici take no position on the precise outer bounds of [test], but submit that under any plausible formulation, [party] prevails here."*
- Procedural framing: Reframe around procedural deficiency rather than substantive policy validity

**Escalation:** Written issue log (contested text, each org's position, proposed resolution, deadline) → escalate to lead attorney → coordinate with supported party's counsel if needed. Treat issue log as privileged work product.

Do **not** draft language suggesting consensus where none exists (Model Rule 3.3 risk).

---

## Step 5: Execute Sign-Off Protocol

**Two-step authorization:**

1. **Join authorization** on near-final draft — written, from authorized person:

```
On behalf of [Organization], I confirm I am authorized to approve
participation and that [Organization] joins the amicus brief in
[Case Name], substantially in the form circulated on [DATE].
[Organization] authorizes counsel to make non-substantive edits
(formatting, citations, typos) prior to filing.
```

2. **Final confirmation** on filing version (if time allows)

| Rule | Detail |
|---|---|
| Written only | No verbal approvals |
| Verify signatory authority | Policy staff enthusiasm ≠ institutional authorization |
| Track entity names precisely | Distinguish association from its foundation |
| Re-confirm if substantive changes after sign-off | |
| Default to exclusion if cutoff missed | |

---

## Step 6: Technical Presentation and Filing

**Cover format** (verify against forum rules `[VERIFY]`):

```
BRIEF OF [LEAD AMICUS] AND [N] OTHER ORGANIZATIONS AS AMICI CURIAE
IN SUPPORT OF [PARTY]
```

**Master roster table:**

| Legal Name | Display Name | Acronym | Entity Type | Corp Disclosure Required? |
|---|---|---|---|---|

**Disclosures checklist:**
- [ ] FRAP 29(a)(4)(E) / Rule 37.6 authorship and funding — for every member
- [ ] FRAP 26.1 corporate disclosure — for every corporate amicus
- [ ] Consent of parties stated, or motion for leave attached

**Consistency check:** Amicus list must match across cover, interest statement, signature block, and disclosure statement.

**Filing checklist:**
- [ ] Consent/leave requirements verified for specific forum `[VERIFY]`
- [ ] Service requirements confirmed (all parties, method, paper copies)
- [ ] Final cite-check — every case citation verified
- [ ] All listed amici have timely written authorization
- [ ] Counsel info complete; bar admissions satisfy forum requirements
- [ ] PDF technical requirements met (bookmarks, fonts, OCR, color covers)
- [ ] Word/page count within limits

**Internal filing certification:**

```
As of [TIMESTAMP]:
- Written authorization received from: [LIST]
- Removed for lack of timely sign-off: [LIST]
- Final PDF: [WORD COUNT/PAGE COUNT]
- Disclosures: included and verified
- Filed/served via: [METHOD]
```

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial coalition draft, ask:

1. Have all organizations confirmed their sign-off authority and internal review timeline?
2. Are there any remaining red-line conflicts that need escalation?
3. Does the cover/caption listing format match forum requirements?
4. Have all disclosure inputs (authorship, funding) been collected from every member?

---

## Quality Audit

Before filing, verify:

- Every listed organization has timely written authorization on file
- Amicus list matches across cover, interest statement, signature block, and disclosures
- Brief does not restate party arguments — delivers unique contribution
- All disclosure statements are complete and accurate per governing rules
- All adjudicative facts tied to record cites; legislative facts sourced
- Entity names verified character-by-character (including suffixes)
- No language suggesting consensus where disagreement exists
- Word count and formatting comply with forum rules
- Assumptions and open items listed prominently
- Internal filing certification completed

---

## Jurisdiction Notes

| Forum | Key Requirements |
|---|---|
| **Federal circuits** | FRAP 29; verify word limit per circuit; local rules on covers, e-filing, corporate disclosures; D.C. Circuit strict on non-duplication |
| **U.S. Supreme Court** | Rule 37, Rule 33.1 (booklet format), green cover for merits; Rule 37.3 timing strictly enforced |
| **State appellate** | Varies dramatically; many require motion for leave; different disclosure regimes; e.g., Cal. Rule of Court 8.520(f) `[VERIFY]` |
| **Admin tribunals** | Unique rules or customs; require rule-based confirmation, not inference |

**Always retrieve and cite current official rules for the specific forum. Flag all unverifiable procedural statements.**

---

## Guidelines

- **Ethics**: Treat each amicus as client for conflicts (Model Rules 1.7–1.10) and confidentiality (1.6); verify conflicts before accepting org into coalition
- **Candor**: Do not attribute positions to orgs that have not approved them (Model Rule 3.3); do not include unverifiable factual claims
- **Citations**: Every non-record factual claim needs a pinpoint citation to a reliable source; flag unverifiable citations with `[VERIFY]`
- **Adversarial lens**: Before filing, ask whether opponent could move to strike based on misstatements, undisclosed funding, or noncompliance
- **Unique contribution test**: Brief must say something the parties' briefs do not
- **Anti-hallucination**: Do not fabricate authorization status, forum rules, or filing requirements. Use `[VERIFY]` for all unconfirmed procedural details
- **Attorney review required**: All outputs require attorney review before filing
