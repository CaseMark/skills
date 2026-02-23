---
name: board-meeting-summary
description: Produces a structured, objective summary of corporate board meetings with required metadata, quorum, attendance, conflicts, agenda discussions, resolutions with vote counts, committee reports, and significant corporate actions. Use for board meeting summary, board minutes summary, corporate governance record, director meeting recap, or post-meeting record for officers, shareholders, or regulators.
tags:
  - corporate
  - summarization
  - summary
---

# Board Meeting Summary

Create an official, concise board meeting summary suitable for the corporate minute book.

## Prerequisites

1. **Meeting materials** — agenda, minutes or notes, presentations, written reports.
2. **Attendance list** — directors present/absent (excused or not), officers, guests/advisors.
3. **Quorum/notice facts** — quorum count, notice method, any waivers.
4. **Resolutions & votes** — text or precise summary, counts for/against/abstain/recused.
5. **Committee reports** — audit, compensation, governance, special committees.
6. **Action items** — approvals, authorizations, follow-ups, next meeting details.

## Output Structure / Process

Use the following structure and populate every section. If information is missing, mark as `UNKNOWN` and flag in the Issues list.

**1) Meeting Metadata (Table)**

| Field | Value |
|---|---|
| Date | |
| Time (start/end) | |
| Location | |
| Format (in-person/virtual/hybrid) | |
| Notice/Waiver | |
| Quorum (required/present) | |
| Chair | |
| Secretary/Recorder | |

**2) Attendance (Table)**

| Role | Name | Status | Notes |
|---|---|---|---|
| Director | | Present/Absent (Excused/Unexcused) | |
| Officer | | Present | |
| Guest/Advisor | | Present | |

**3) Conflicts & Recusals (Table)**

| Person | Matter | Disclosure | Recusal | Notes |
|---|---|---|---|---|
| | | Yes/No | Yes/No | |

**4) Agenda Items (Table)**

| Item | Topic | Summary of Discussion | Decision/Outcome | Follow-up |
|---|---|---|---|---|
| 1 | | | | |

**5) Resolutions (Table)**

| Resolution | Summary (or text if provided) | Vote (For/Against/Abstain/Recused) | Result |
|---|---|---|---|
| 1 | | | Approved/Denied/Tabled |

**6) Significant Corporate Actions (Checklist)**

- [ ] Approval of financial statements/audit reports
- [ ] Dividends or distributions
- [ ] Major contracts/transactions
- [ ] Stock issuance/repurchase
- [ ] Officer election/removal
- [ ] Bylaw or policy amendments
- [ ] M&A or asset sales
- [ ] Financing/borrowing authorization
- [ ] Litigation or claims decisions
- [ ] Other material actions

For each checked item, add a short action summary and any conditions or limits.

**7) Committee Reports (Table)**

| Committee | Key Findings/Recommendations | Board Action |
|---|---|---|
| Audit | | Accepted/Modified/Deferred |

**8) Executive Session**

Provide occurrence and general subject only. Do not disclose privileged content unless explicitly instructed.

**9) Closing**

Include announcements, next meeting date/time (if set), and adjournment time.

**10) Issues / Missing Information (Checklist)**

- [ ] Missing quorum/notice detail
- [ ] Missing vote counts
- [ ] Missing resolution text/summary
- [ ] Missing attendance confirmations
- [ ] Other: ___

## Guidelines

- Maintain neutral tone; do not editorialize or speculate.
- Use precise vote counts and identify abstentions/recusals.
- Summarize discussion; do not reproduce presentations verbatim.
- Confirm recordkeeping requirements against the company’s bylaws and governing law; do not state compliance unless verified.
- Preserve privilege: exclude attorney-client content or legal strategy unless specifically directed.
