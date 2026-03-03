---
name: change-in-control-agreement
description: Drafts U.S. executive Change in Control Agreements with double-trigger severance, equity acceleration, and 280G/409A compliance. Use when drafting or negotiating CIC agreements, change in control protections, executive severance in M&A, or golden parachute provisions.
---

# Change in Control Agreement

Drafts a tax-compliant U.S. executive CIC agreement with double-trigger structure, precise statutory definitions, severance benefits, and parachute payment protections.

## Quick Start

Gather before drafting:

1. **Executive** — name, title, base salary, target bonus, outstanding equity (type, vesting, performance metrics)
2. **Company** — legal name, state of incorporation, entity type, public/private status
3. **Existing agreements** — employment agreement, equity plan docs, prior CIC/severance agreements
4. **Deal terms** — severance multiple, protection period, 280G treatment, benefits continuation period
5. **Benchmarking** (if available) — peer agreements, proxy disclosures, comp committee guidelines

## Core Workflow

```
- [ ] Collect executive profile, company info, and existing agreements
- [ ] Define key terms (Change in Control, Cause, Good Reason, Qualifying Termination)
- [ ] Set severance benefits (cash, equity acceleration, COBRA, pro-rated bonus)
- [ ] Configure 280G approach (No Gross-Up / Best Net / Full Gross-Up)
- [ ] Add 409A compliance provisions (separation from service, specified employee delay)
- [ ] Draft release conditions (OWBPA-compliant consideration + revocation periods)
- [ ] Include general provisions (governing law, dispute resolution, successor assignment)
- [ ] Verify all placeholders resolved and cross-references consistent
```

See `references/ARTICLES.md` for detailed article-by-article output specifications and standard formulations.

## Key Placeholders

| Placeholder | Market Range |
|---|---|
| `[SEVERANCE MULTIPLE]` | CEO: 2x–3x; C-suite/SVP: 1.5x–2x; other senior: 1x–1.5x |
| `[PROTECTION PERIOD]` | 12–24 months post-CIC |
| `[PRE-CIC TAIL]` | 3–6 months (if included) |
| `[BENEFITS CONTINUATION]` | 12–24 months |
| `[280G APPROACH]` | No Gross-Up / Best Net / Full Gross-Up |
| `[PERFORMANCE VEST LEVEL]` | Target / Maximum / Actual through CIC date |
| `[EXERCISE EXTENSION]` | 12–24 months post-termination |
| `[RELOCATION THRESHOLD]` | 35–50 miles |
| `[GOOD REASON NOTICE]` | 60–90 days; cure 30 days; election 30–60 days |

## Pitfalls

- **Single trigger** — avoid for public companies; ISS/Glass Lewis routinely vote against single-trigger equity acceleration
- **280G modeling** — run parachute calculations before selecting approach; full gross-up is rarely defensible in new agreements
- **409A** — treat each payment as separate; do not rely on short-term deferral exemption for CIC-contingent amounts; use Day-60 payment with two-tax-year rule; apply specified-employee 6-month delay for public company executives
- **OWBPA** — strictly observe 21-day (under 40) or 45/60-day (40+) consideration periods plus 7-day revocation; non-compliance invalidates ADEA release
- **Equity plan override** — confirm acceleration and extended exercise provisions expressly supersede conflicting plan/award terms; some plans require separate committee action
- **Pre-CIC tail** — limit to terminations "at the request of" or "in connection with" the contemplated transaction; avoid overbroad language
- **State law** — CA, NY, and others restrict non-competes; review local WARN, mini-COBRA, and wage payment requirements separately

---

**What changed and why:**

- **Description** — trimmed from ~900 chars to ~280 chars; removed enumeration of every provision, kept trigger keywords
- **Removed `tags`** — not part of the standard Agent Skills frontmatter spec
- **Added Quick Start** — prerequisites condensed into a numbered gather-list
- **Added Core Workflow** — checklist format replacing the implicit flow buried in article headings
- **Moved detailed article specs to reference** — the six full article tables (definitions, severance, conditions, 280G, 409A, general provisions) belong in `references/ARTICLES.md` for progressive disclosure; the main file now points there
- **Placeholders** — converted from code block to table for scannability; merged Good Reason sub-placeholders into one row
- **Guidelines → Pitfalls** — renamed and tightened; removed the "public companies" point (duplicated by single-trigger bullet) and folded 409A payment-timing details into the 409A bullet
- **Line count** — reduced from 122 to ~58 lines (~53% reduction)

If you grant write permissions I can write both the SKILL.md and the companion `references/ARTICLES.md` (containing the detailed article-by-article output tables from the original) directly to disk.
