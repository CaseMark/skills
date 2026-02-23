---
name: written-consent-of-incorporator
description: Drafts a U.S. corporate formation Action by Written Consent of Incorporator used in place of an organizational meeting. Generates a corporate resolution document that records initial incorporator actions such as adopting bylaws, appointing initial directors, and other formation actions that must be executed after Articles of Incorporation filing. Use when the prompt includes "written consent," "incorporator," "formation filing," "adopt bylaws," "appoint initial directors," or "organize corporation."
tags:
  - agreement
  - corporate
  - drafting
---

# Action by Written Consent of Incorporator

Generates an execution-ready incorporator written-consent document for post-formation organizational actions and corporate minute-book filing.

## Prerequisites

1. Exact legal corporation name and state of incorporation.
2. State filing date of Articles of Incorporation.
3. Incorporator(s) full legal name(s) and execution authority.
4. Complete list of initial directors’ full legal names.
5. Bylaws text (or explicit instruction that bylaws will be attached separately).
6. Any nonstandard organizational actions requested (bank account authorization, fiscal year, stock issuance ratification, etc.).
7. Confirmation whether multiple incorporators are consenting jointly.

## Output Structure / Process

### 1) Input validation grid
| Item | Source | Required | Validation rule |
|---|---|---:|---|
| Corporation legal name | Articles/formation docs | Yes | Must match exactly across all captions and recitals |
| State of incorporation | Articles/formation docs | Yes | Use legal state name |
| Filing date | Secretary of State filing records | Yes | Must be in full date format |
| Incorporator identity | Formation packet | Yes | Match name(s) in incorporation records |
| Director names | User input / board list | Yes | Match requested board size and statutory/charter limits |
| Bylaws | Draft/bylaws file | Required unless deferred | If not attached, include explicit exhibit addendum instruction |

### 2) Required drafting sequence
1. Title page: `Action by Written Consent of Incorporator of [Corporation Name]`.
2. Preamble:
   - identify incorporator (sole or multiple),
   - cite corporation name, state, filing date,
   - state purpose of written consent under state corporation law.
3. Resolution list (numbered):
   - Adoption of bylaws, cited as Exhibit A (or note separate attachment).
   - Appointment/election of initial directors.
   - Optional additional organization resolutions only if requested.
4. Closing/organizational transition clause:
   - incorporator confirms completion of incorporator duties and transition of authority to board.
5. Execution block:
   - filing instruction for minute book,
   - signature block for each incorporator with printed name/title/date.

### 3) Template output
```text
ACTION BY WRITTEN CONSENT OF INCORPORATOR
of [Corporation Name], a [State] Corporation

[Effective Date]

The undersigned [sole incorporator / incorporators], [name(s)],
hereby adopt this written consent of incorporator on behalf of
[Corporation Name], a [State] corporation, pursuant to the filing of
its Articles of Incorporation on [Filing Date].

RESOLVED THAT:
1. [Adopt Bylaws as Exhibit A ...]
2. [The following persons are elected/appointed as the initial board of directors: ...]
3. [Additional organizational action(s) as requested.]

RESOLVED FURTHER THAT the undersigned incorporator(s) is deemed to have
completed all acts of an incorporator and all authority is transferred to
the board of directors.

Executed this [Date].

_________________________________
[Incorporator Printed Name]   Signature
```

### 4) Quality gate before final output
- No bracketed placeholders remain.
- Director count aligns with charter/state requirements.
- No internal conflicts: name, state, filing date, incorporator identity consistent.
- Professional corporate format: numbered resolutions, clear headings, consistent spacing, execution-ready text.

## Guidelines

- Use a separate subsection when there are multiple incorporators to avoid ambiguity on consent authority.
- Keep language statutory-neutral unless a specific state rule is provided.
- Include [VERIFY] tags for any jurisdictional rule not confirmed by source documents.
- Default references may track MBCA-style defaults, but verify against governing state law when the state is known and any required formalities differ.
- Never imply attorney-client legal advice; draft only the requested governance instrument.
- Notarization is usually not required for written consent, but note jurisdictional or office-specific requirements before finalizing.
