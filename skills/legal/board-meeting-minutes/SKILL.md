---
name: board-meeting-minutes
description: >-
  Drafts U.S. corporate board-of-directors meeting minutes into a formal,
  defensible corporate record. Use for pre/post meeting drafting when source
  materials are available (agenda, attendance, bylaws, notices, reports, prior
  minutes, resolutions). Triggers: board minutes, directors meeting record,
  board resolutions, quorum validation, motion and vote capture, corporate
  secretary records, governance drafting.
tags:
  - corporate
  - drafting
  - memo
---

# Board of Directors Meeting Minutes

Produce legally structured minutes that document valid corporate action, accurate governance process, and an evidentiary timeline.

## Prerequisites

1. Corporation legal name and governing documents (charter/articles if available, bylaws, board/delegation policies).
2. Meeting materials: agenda, notices, attendance logs, meeting location/virtual details, any meeting calls/resolutions, reports, prior draft minutes.
3. Director roster with in-office counts and titles.
4. Relevant committee charter names and membership if committees report.
5. Any known conflicts or recusals and written waivers.
6. Corporate secretary or assigned preparer identity.
7. User confirms applicable state of incorporation and any local governance custom (e.g., board approvals, recording retention, notice and virtual attendance rules).

## Output Structure / Process

### Step 1 — Intake mapping table

| Field | Source | Required extraction |
| --- | --- | --- |
| Corporation legal name | Charter, prior minutes | Exact legal entity name |
| Meeting type | Notice/resolution | Regular, special, emergency, authority cited |
| Date/time | Notice/calendar | Start/end time, timezone |
| Venue/platform | Calendar/meeting link | Physical address or virtual platform |
| Notice method | Bylaws + distribution log | Required notice period/method and compliance |
| Attendance | Roll call/attendance sheet | Present/absent directors, officers, guests |
| Quorum | Bylaws + attendance | Quorum rule + actual count |
| Agenda items | Agenda/package | Ordered item summaries |
| Motions/resolutions | Motion text/discussion notes | Maker, seconder, text, vote, result |
| Conflicts/recusals | Disclosures | Nature + effect on discussion/vote |
| Attachments | Report packets | Exhibit/record references |
| Authentication | Signature block requirements | Preparer and board approval language |

### Step 2 — Draft in required sequence

1. **Meeting header**  
   Include exact corporation name, meeting type, date/time, location/platform, and that the meeting was properly called.

2. **Notice and calling authority**  
   Document who called the meeting, applicable bylaw/authority, notice period and method, and any waivers or attendance-based notice cure.

3. **Attendance, participation, and quorum**  
   List directors with titles and participation mode (in person/remote). Separate non-director attendees by role. State quorum requirement and actual number satisfied.

4. **Procedural matters**  
   Record call to order, presiding officer, agenda adoption, executive session calls, and any participant time-in/time-out affecting voting periods.

5. **Prior minutes approval**  
   Cite prior meeting date, motion maker, seconder, amendments (if any), and vote outcome.

6. **Reports and committee items**  
   Summarize material points from officers and committee reports; identify each report by presenter and committee. Mention distributed materials and whether attached as exhibits.

7. **Deliberations, motions, and resolutions**  
   For each agenda item, provide issue summary, discussion themes, decisions required, conflicts/recusals, and motion outcome.

8. **Adjournment and next steps**  
   Record adjournment time and next-meeting details if set; otherwise state board will set date in accordance with bylaws or chair.

9. **Authentication and approval**  
   Include preparer signature block and board approval language for a later session if requested.

### Step 3 — Standard motion log block

```text
Item:
Motion/Resolution (full or close-to-final text):
Maker:
Seconder:
Conflict/Recusal Disclosure:
Vote (For/Against/Abstain/Absent):
Result:
Condition/preconditions/required filings:
```

For material acts (interested-party deals, mergers, repurchases, article/bylaw changes, indemnification, major debt/equity actions, officer appointments/removals), include per-director vote records where practical.

### Step 4 — Final compliance checks

- Confirm notice compliance and waiver mechanics are accurate.
- Confirm quorum was present for each action requiring it.
- Confirm vote tallies by item and consistency with materials.
- Confirm conflict handling and recital language is complete and neutral.
- Confirm no attorney-client or work-product content is included unless expressly requested.
- Confirm state-specific requirements on record retention, inspection rights, and board action formalities are acknowledged.
- For any state-law default assumptions not tied to provided docs, mark as `[VERIFY]` in the final draft.

## Guidelines

1. Keep tone objective and record-oriented; avoid legal opinions and motive language.
2. Use present tense factual wording for actions and decisions.
3. Do not paraphrase confidential legal advice beyond what is necessary for governance record.
4. Never leave placeholders in final minutes (replace all bracketed notes with confirmed facts).
5. Prefer precise numbers, dates, and names over narrative summaries.
6. Do not over-document exploratory chatter; include only material, board-relevant deliberation.
7. If action requires heightened legal threshold, explicitly log the required threshold and whether met; if uncertain, apply `[VERIFY]`.
