---
name: court-rules
language: en
description: >-
  Looks up U.S. federal court rules, district local rules, judge standing
  orders, and judge-specific filing requirements through the Court Rules MCP
  server (mcp.courtrules.app/mcp), and checks a document against a judge's
  rules. Use when a task needs a specific district's local rules, a judge's
  standing order, a brief page limit, a court holiday, or a pre-filing
  compliance check. Trigger keywords: court rules, local rules, standing
  orders, federal court, FRCP, judge rules, page limit, filing requirements,
  check compliance, court holidays.
metadata:
  author: courtrules
  practice_areas:
    - Litigation
  document_types:
    - Research
  skill_modes:
    - Research
    - Analysis
---

# Court Rules

Answers questions about U.S. federal court practice from structured rule data: district local rules, individual judge standing orders, and court holidays. Every rule is traced to a source document, so an answer can be verified instead of taken on trust.

The same data powers the free web reference and deadline calculator at [courtrules.app](https://www.courtrules.app/). The MCP server exposes the lookups; the calculator counts calendar, business, and court days with each district's holidays applied.

## Prerequisites

1. An MCP client (Claude Desktop, Claude Code, Cursor, or any HTTP MCP client)
2. A one-time sign-in through `console.courtrules.app`

## Quick Start

Add the server.

Claude Code:

```bash
claude mcp add --transport http court-rules https://mcp.courtrules.app/mcp
```

Claude Desktop or claude.ai: open Settings > Connectors > Add custom connector and paste `https://mcp.courtrules.app/mcp`.

Sign in once: run `/mcp` in Claude Code and choose Authenticate, or click Connect in Claude Desktop. The browser opens `console.courtrules.app`; approve the connection.

Ask a question:

> What is the page limit for summary judgment briefs in EDNY before Judge Brown?

The agent calls `search_judges`, then `get_judge_rules`, and answers from the standing order instead of defaulting to the FRCP's 25 pages.

## Tools

| Tool | Returns | Use for |
|---|---|---|
| `list_courts` | Federal district courts with status | Resolving a district before any other call |
| `search_judges` | Judges by district, name, or type | Finding the judge for a case |
| `get_judge_rules` | All rules for a judge: page limits, format, procedures | Page limits, font and spacing, motion practice, courtesy copies |
| `check_compliance` | Violations found in a document against judge-specific rules | Pre-filing checks |

The server also exposes enforcement-data tools (`search_enforcement_actions`, `get_enforcement_details`, `get_enforcement_stats`) for federal and state privacy enforcement actions.

## Examples

### Page limit for a filing

1. `list_courts` to confirm the district code, for example `EDNY`.
2. `search_judges` with `{"district": "EDNY", "query": "Brown"}`.
3. `get_judge_rules` with the judge id from step 2.

The answer includes the rule text and its source. District local rules apply when the judge's standing order is silent; state the source for each.

### Pre-filing compliance check

Call `check_compliance` with the document text and the judge id. The response lists each rule the document violates, for example a brief over the standing order's page limit or an incorrect font size. Fix the violations before filing and run the check again.

### Court holidays

Ask the agent whether a court is open on a given date. Court holidays feed deadline calculations on courtrules.app and are listed per district.

## Troubleshooting

- **401 or "authentication required" after adding the server** — the one-time sign-in is incomplete. Run `/mcp` and choose Authenticate, or reconnect in the client; the browser opens `console.courtrules.app`.
- **`search_judges` returns nothing** — check the district code with `list_courts`. Judges are indexed by district, and a misspelled district returns an empty list.
- **The agent answers with FRCP defaults** — it skipped the tools. Ask again and require `get_judge_rules`; standing orders override the FRCP baseline, and the whole point of the lookup is the difference.
- **`check_compliance` reports a rule the document seems to satisfy** — read the cited section in the response. Formatting rules often apply to the body only, not to the caption or certificate of service.
