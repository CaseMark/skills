# CaseMark Agent Skills

Open-source agent skills for legal AI workflows and the [case.dev](https://case.dev) platform.

This repository contains two categories of skills:

| Directory | Audience | Description |
|-----------|----------|-------------|
| `skills/legal/` | Legal professionals & legal AI builders | Skills for legal tasks (deposition summarization, motion drafting, etc.). Embedded into a vector DB on merge to power the [agentskills.legal](https://agentskills.legal) website and Legal Agent Skills API. |
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

See [skills/legal/](skills/legal/) for legal practice skills. These are also searchable via the [agentskills.legal](https://agentskills.legal) website and the Legal Agent Skills MCP.

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
                /           \
skills/legal/**          skills/casedev/**
      ↓                        ↓
legal-embed.yml          Nothing extra.
(embed → pgvector)       Files are the product.
      ↓
Powers:
- agentskills.legal website
- Legal Agent Skills MCP
- case.dev Legal Skills API
```

## Links

- [case.dev](https://case.dev)
- [agentskills.legal](https://agentskills.legal)
- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Skills Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

## License

Apache 2.0 — see [LICENSE](LICENSE).
