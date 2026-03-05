# CaseMark Agent Skills

Open-source agent skills for legal, medical, finance, and capital markets AI workflows and the [case.dev](https://case.dev) platform.

This repository contains five categories of skills:

| Directory | Audience | Description |
|-----------|----------|-------------|
| `skills/legal/` | Legal professionals & legal AI builders | 874 skills for legal tasks (deposition summarization, motion drafting, etc.). Embedded into a vector DB on merge to power the [agentskills.legal](https://agentskills.legal) website and Legal Agent Skills API. |
| `skills/med/` | Healthcare professionals & health AI builders | 400 skills across 20 medical subgroups (emergency medicine, cardiology, oncology, surgery, etc.). Structured agentic workflows for processing and synthesizing healthcare information. |
| `skills/finance/` | Financial professionals & fintech builders | 400 skills across 20 finance subgroups (accounting, tax, insurance, banking, wealth management, FP&A, etc.). Consumer and corporate finance workflows. |
| `skills/capital/` | Institutional investors & capital markets builders | 400 skills across 20 capital subgroups (M&A, VC, PE, fund formation, structured finance, capital markets, etc.). Institutional capital deployment and deal-making workflows. |
| `skills/casedev/` | case.dev developers | Skills for building on the case.dev platform (vaults, OCR, transcription, search). File-based, consumed directly by Claude Code or any agent. |

## Quick Start

### Claude Code

```bash
# Clone the repo
git clone https://github.com/CaseMark/skills.git

# Copy specific skills to your Claude Code skills directory
cp -r skills/casedev/setup ~/.claude/skills/setup
cp -r skills/casedev/vaults ~/.claude/skills/vaults
```

### Claude.ai

1. Download or clone this repo
2. Zip individual skill folders (e.g., `skills/casedev/vaults/`)
3. Upload via **Settings > Capabilities > Skills**

### Claude API

Use the `/v1/skills` endpoint or the `container.skills` parameter in Messages API requests.

## Available Skills

### case.dev Platform Skills

| Skill | Description |
|-------|-------------|
| [setup](skills/casedev/setup/) | Install CLI, authenticate, diagnostics, focus targets, job tracker, API routes |
| [vaults](skills/casedev/vaults/) | Encrypted document vaults: create, upload, download, semantic search |
| [ocr](skills/casedev/ocr/) | Document OCR: process PDFs/images, word-level positional data |
| [transcription](skills/casedev/transcription/) | Audio/video transcription with speaker diarization |
| [search](skills/casedev/search/) | Web, legal, case law, patent, vault, and skills KB search |

### Legal Skills

See [skills/legal/](skills/legal/) for 874 legal practice skills. These are also searchable via the [agentskills.legal](https://agentskills.legal) website and the Legal Agent Skills MCP.

### Medical Skills (400 skills)

See [skills/med/](skills/med/) for 400 healthcare and medical skills organized across 20 subgroups:

| Subgroup | Skills | Examples |
|----------|--------|----------|
| Emergency Medicine | 20 | ED triage, trauma assessment, stroke pathways, sepsis bundles |
| Hospital Medicine | 20 | Admission orders, discharge summaries, daily rounds, handoffs |
| Primary Care | 20 | Wellness visits, chronic disease management, preventive screening |
| Surgery | 20 | Operative reports, pre-op planning, post-op orders, wound care |
| Radiology | 20 | Chest X-ray, CT/MRI interpretation, tumor response, RADS classification |
| Pathology | 20 | Surgical pathology, cytology, molecular testing, flow cytometry |
| Pharmacy | 20 | Drug interactions, anticoagulation, antimicrobial stewardship, PK dosing |
| Oncology | 20 | Cancer staging, chemo toxicity, tumor boards, survivorship care |
| Psychiatry | 20 | Psychiatric evaluation, suicide risk, psychotropics, capacity assessment |
| Cardiology | 20 | ECG interpretation, echocardiography, heart failure, atrial fibrillation |
| Obstetrics & Gynecology | 20 | Prenatal care, fetal monitoring, labor management, gynecologic screening |
| Pediatrics | 20 | Newborn assessment, developmental milestones, immunizations, pediatric fever |
| Medical Coding & Billing | 20 | ICD-10/CPT coding, E/M coding, DRG optimization, compliance audits |
| Clinical Research | 20 | Trial design, IRB submissions, meta-analysis, regulatory submissions |
| Nursing | 20 | Nursing assessments, care plans, medication administration, wound care |
| Healthcare Compliance | 20 | HIPAA auditing, Stark Law, Anti-Kickback, EMTALA, accreditation |
| Health Informatics | 20 | Clinical terminology mapping, EHR implementation, CDS design, NLP |
| Public Health | 20 | Disease surveillance, outbreak investigation, vaccination campaigns |
| Dental Medicine | 20 | Dental exams, treatment planning, periodontal assessment, oral surgery |
| Rehabilitation Medicine | 20 | Functional assessment, gait analysis, neuro rehab, PT/OT/speech |

### Finance Skills (400 skills)

See [skills/finance/](skills/finance/) for 400 consumer and corporate finance skills organized across 20 subgroups:

| Subgroup | Skills | Examples |
|----------|--------|----------|
| Equity Research | 20 | Earnings call analysis, financial ratios, valuation models, investment theses |
| Fixed Income | 20 | Bond structures, credit analysis, yield curves, structured products |
| Investment Banking | 20 | Pitch books, M&A analysis, LBO models, fairness opinions |
| Private Equity | 20 | Deal evaluation, IC memos, portfolio monitoring, exit strategies |
| Asset Management | 20 | Portfolio construction, performance attribution, factor analysis, rebalancing |
| Risk Management | 20 | VaR calculation, stress testing, counterparty risk, operational risk |
| Financial Compliance | 20 | AML screening, KYC review, trade surveillance, regulatory examinations |
| Corporate Finance | 20 | Financial projections, capital structure, cash flow forecasting, hedging |
| Accounting | 20 | Revenue recognition, month-end close, SOX compliance, SEC reporting |
| Real Estate Finance | 20 | Property valuation, REIT analysis, loan underwriting, cap rate analysis |
| Insurance | 20 | Underwriting analysis, loss reserves, catastrophe risk, reinsurance |
| Quantitative Finance | 20 | Option pricing, volatility surfaces, derivatives risk, Monte Carlo |
| Financial Technology | 20 | Payment flows, fintech evaluation, digital lending, blockchain analysis |
| Tax | 20 | Corporate tax structures, transfer pricing, international tax, M&A tax |
| Wealth Management | 20 | Financial planning, estate planning, retirement income, charitable giving |
| Fund Operations | 20 | NAV calculation, fund accounting, investor reporting, trade operations |
| FP&A | 20 | Annual operating plans, variance analysis, rolling forecasts, dashboards |
| Commercial Banking | 20 | Loan underwriting, credit approval, trade finance, SBA lending |
| Sustainable Finance | 20 | ESG scoring, carbon footprints, green bonds, climate scenarios |
| Economic Analysis | 20 | Economic indicators, monetary policy, inflation dynamics, country risk |

### Capital Skills (400 skills)

See [skills/capital/](skills/capital/) for 400 institutional capital deployment skills organized across 20 subgroups:

| Subgroup | Skills | Examples |
|----------|--------|----------|
| Mergers and Acquisitions | 20 | Target screening, CIMs, synergy analysis, PMI planning |
| Venture Capital | 20 | Deal flow screening, term sheets, cap tables, portfolio support |
| Private Equity | 20 | LBO modeling, value creation plans, add-on analysis, exit timing |
| Growth Equity | 20 | SaaS metrics, pre-IPO readiness, minority protections, PLG analysis |
| Equity Capital Markets | 20 | IPO execution, book building, roadshows, direct listings |
| Debt Capital Markets | 20 | Bond offerings, loan syndication, covenant analysis, leveraged finance |
| Structured Finance | 20 | ABS/MBS/CLO structuring, waterfall modeling, collateral analysis |
| Distressed and Restructuring | 20 | Chapter 11 recovery, DIP financing, liquidity analysis, 363 sales |
| Secondaries and GP-Led | 20 | LP interest pricing, continuation vehicles, tender offers |
| Fund Formation and Structuring | 20 | LPA terms, carry mechanics, fund vehicles, tax structuring |
| Investor Relations and LP Reporting | 20 | Capital calls, distributions, performance reporting, AGMs |
| Infrastructure and Project Finance | 20 | PPP, concessions, project modeling, construction risk |
| Real Assets and Natural Resources | 20 | Mining, energy, commodities, royalty streams |
| Credit and Institutional Lending | 20 | Direct lending, leveraged loans, credit fund operations |
| Public Markets and Trading | 20 | Market microstructure, execution algorithms, TCA |
| Derivatives and Structured Products | 20 | Options, swaps, hedging programs, XVA |
| Cross-Border Capital | 20 | Sovereign risk, FX, international deal structuring |
| Capital Allocation and Corporate Strategy | 20 | ROIC frameworks, strategic alternatives, buybacks |
| Activist and Event-Driven Investing | 20 | Activist campaigns, merger arb, special situations |
| Quantitative Capital Strategies | 20 | Factor models, stat arb, systematic investing |

## Prerequisites

The case.dev skills require the `casedev` CLI:

```bash
# macOS
brew install casemark/casedev/casedev

# macOS + Linux
curl -fsSL https://raw.githubusercontent.com/CaseMark/homebrew-casedev/main/install.sh | sh
```

Authenticate:

```bash
export CASE_API_KEY=sk_case_YOUR_KEY           # env var (best for agents)
casedev auth set-key --api-key sk_case_YOUR_KEY # stored in config
```

Verify: `casedev doctor --json`

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose new skills or improve existing ones.

## Skill Format

Every skill is a directory with a `SKILL.md` file following the [Agent Skills specification](https://agentskills.io/specification). See [spec/SKILL-SPEC.md](spec/SKILL-SPEC.md) for our authoring standard and [template/SKILL.md](template/SKILL.md) for a starter template.

## How It Works

```
PR opened → skill-qa.yml validates format + quality
                    ↓
            PR merged to main
           /        |          \
skills/legal/**  skills/med/**   skills/casedev/**
skills/finance/** skills/capital/**
      ↓                              ↓
legal-embed.yml                Nothing extra.
(embed → pgvector)             Files are the product.
      ↓
Powers:
- agentskills.legal website
- Legal Agent Skills MCP
- case.dev Legal Skills API
```

## Links

- [case.dev](https://case.dev)
- [agentskills.legal](https://agentskills.legal)
- [agentskills.med](https://agentskills.med) (coming soon)
- [agentskills.finance](https://agentskills.finance) (coming soon)
- [agentskills.capital](https://agentskills.capital) (coming soon)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## License

Apache 2.0 — see [LICENSE](LICENSE).
