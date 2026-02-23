---
name: procedural-rule-summary
description: Generates structured summaries of procedural rules from federal, state, local, or administrative sources for quick reference during litigation or hearings. Organizes rules by procedural stage with actions, deadlines, responsibilities, and non-compliance consequences. Use when summarizing court rules, civil procedure rules, criminal procedure rules, local rules, administrative hearing procedures, or building procedural checklists for case preparation and motion practice.
tags:
  - litigation
  - research
  - summarization
  - summary
---

# Procedural Rule Summary

Generates a concise, structured summary of procedural rules that serves as a quick-reference guide for compliance during litigation, administrative hearings, or regulatory proceedings.

## Prerequisites

1. **Identified rule set** — specific rules to summarize (e.g., FRCP, FRCrP, state rules, local rules, administrative procedure acts)
2. **Jurisdiction** — federal, state, or administrative body
3. **Proceeding type** — civil, criminal, administrative, appellate
4. **Any uploaded rule texts, court orders, or standing orders** to extract from

## Process

### Step 1: Identify and Verify Sources

- Determine the exact rule set, jurisdiction, and court
- Confirm the version is current — note any recent amendments with effective dates
- If user provides documents, extract procedural requirements from those first
- Cross-reference multiple sources when available; flag conflicts

### Step 2: Organize by Procedural Stage

Structure the summary following case chronology. Use only the stages relevant to the requested rules:

| Stage | Typical Coverage |
|-------|-----------------|
| **Initiation/Filing** | Complaint requirements, filing fees, service of process |
| **Responsive Pleadings** | Answer deadlines, motions to dismiss, affirmative defenses |
| **Discovery** | Scope, initial disclosures, written discovery, depositions, ESI |
| **Motions Practice** | Filing requirements, briefing schedules, page limits, meet-and-confer |
| **Pre-Trial** | Conferences, exhibit/witness lists, motions in limine, proposed jury instructions |
| **Trial** | Jury selection, presentation order, evidentiary objections, directed verdict |
| **Post-Trial** | JMOL, new trial motions, costs/fees |
| **Appeal** | Notice of appeal, record designation, briefing schedule, standards of review |

### Step 3: For Each Rule, Capture These Elements

Use this template per rule or procedural requirement:

```
### [Rule Number] — [Short Title]

**Action required:** [What must be done]
**Responsible party:** [Who must act]
**Deadline:** [Specific timeframe + calculation method]
**Method/Format:** [How — e.g., ECF, personal service, specific form]
**Mandatory vs. Discretionary:** [Whether court has discretion]
**Non-compliance consequence:** [Waiver, sanctions, dismissal, default]
**Extensions:** [Whether/how deadline can be extended + standard applied]
**Cross-references:** [Related rules, local rules, standing orders]
```

### Step 4: Deadline Calculation Details

For every timing requirement, specify:

- Calendar days vs. business days vs. court days
- Trigger event (filing, service, entry of order)
- Weekend/holiday rules (e.g., FRCP 6(a) — if last day is Saturday/Sunday/holiday, deadline extends to next business day)
- Service-method additions (e.g., FRCP 6(d) — 3 days added for mail service)
- Whether "from" date is included or excluded

### Step 5: Common Pitfalls Section

Include a brief section flagging frequent practitioner errors specific to the summarized rules, such as:

- Service vs. filing deadline confusion
- Meet-and-confer prerequisites before motion filing
- Local rule formatting requirements (font, margins, page limits)
- Certificate of service requirements
- E-filing technical requirements and deadlines (midnight vs. clerk's office hours)

## Output Format

```markdown
# Procedural Rule Summary: [Rule Set Name]

**Jurisdiction:** [Jurisdiction]
**Proceeding type:** [Type]
**Rules version:** [Date/version]
**Prepared:** [Date]

## Overview
[1-2 sentences identifying scope]

## [Stage 1 Heading]
### [Rule X] — [Title]
[Structured content per template above]

...

## Deadline Quick-Reference Table
| Action | Rule | Deadline | Calculated From | Days Type |
|--------|------|----------|-----------------|-----------|
| ...    | ...  | ...      | ...             | ...       |

## Common Pitfalls
- [Pitfall 1]
- [Pitfall 2]

## Cross-References
- [Related rule sets, standing orders, local rules]
```

## Guidelines

- Cite specific rule numbers and subsections — never paraphrase without attribution
- Mark any rule citation you cannot verify with `[VERIFY]`
- Note where case law has materially altered rule application (brief parenthetical only — not full case briefs)
- Flag where practice varies by judge or division within a court
- Distinguish mandatory requirements from permissive/discretionary provisions
- When rules interact (e.g., discovery rules + ESI protocols + local rules), show the interplay explicitly
- Do not editorialize on policy or fairness — summarize what the rules require
- If the user's jurisdiction has both state and local rules that modify general rules, address both layers
