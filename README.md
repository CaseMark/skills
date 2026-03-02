# CaseMark Agent Skills

Open-source agent skills for legal, medical, and financial AI workflows and the [case.dev](https://case.dev) platform.

This repository contains four categories of skills:

| Directory | Audience | Description |
|-----------|----------|-------------|
| `skills/legal/` | Legal professionals & legal AI builders | 874 skills for legal tasks (deposition summarization, motion drafting, etc.). Embedded into a vector DB on merge to power the [agentskills.legal](https://agentskills.legal) website and Legal Agent Skills API. |
| `skills/med/` | Healthcare professionals & health AI builders | 30 skills for medical workflows (clinical documentation, lab analysis, medication reconciliation, etc.). Structured agentic workflows for processing and synthesizing healthcare information. |
| `skills/finance/` | Financial professionals & fintech builders | 30 skills for financial workflows (earnings analysis, credit assessment, AML compliance, etc.). Structured agentic workflows for processing and synthesizing financial information. |
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

### Medical Skills (30 skills)

See [skills/med/](skills/med/) for healthcare and medical skills organized across six categories:

| Category | Skills | Examples |
|----------|--------|----------|
| Summarization & Synthesis | 6 | Discharge notes, clinical trials, radiology reports, pathology reports |
| Analysis & Assessment | 6 | Drug interactions, lab results, clinical risk scoring, symptom triage |
| Document Generation | 6 | Clinical notes (SOAP/H&P), referral letters, prior authorizations, care plans |
| Compliance & Regulatory | 4 | HIPAA auditing, ICD-10/CPT coding, IRB review, CDI validation |
| Research & Discovery | 4 | PICO literature review, epidemiology, diagnostic accuracy, endpoint extraction |
| Operational Workflows | 4 | Insurance claims, transitions of care, adverse events, medication reconciliation |

### Finance Skills (30 skills)

See [skills/finance/](skills/finance/) for financial services skills organized across six categories:

| Category | Skills | Examples |
|----------|--------|----------|
| Summarization & Synthesis | 6 | Earnings calls, 10-K/10-Q analysis, credit reports, loan documents |
| Analysis & Assessment | 6 | Financial ratios, credit risk, investment thesis, portfolio benchmarking |
| Document Generation | 6 | Investment memos, client reports, pitch books, offering memoranda |
| Compliance & Regulatory | 4 | AML transaction auditing, KYC review, regulatory exposure, SOX controls |
| Research & Discovery | 4 | Market sector research, comparable transactions, investment screening |
| Operational Workflows | 4 | Trade settlements, account reconciliation, covenant compliance, month-end close |

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
           /        |         \
skills/legal/**  skills/med/**   skills/casedev/**
skills/finance/**
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
- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## License

Apache 2.0 — see [LICENSE](LICENSE).
