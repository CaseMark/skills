#!/usr/bin/env python3
"""
Generate SKILL.md files for medical and capital verticals.

Reads taxonomy definitions and produces well-structured SKILL.md files
following Claude Agent Skills best practices:
- Gerund naming (lowercase-hyphenated)
- Third-person descriptions (max 1024 chars)
- YAML frontmatter with name, description, tags, metadata
- Concise body (<500 lines) with workflow, output template, and guidelines
- Flat directory structure: skills/{vertical}/{skill-name}/SKILL.md

Usage:
    python scripts/generate_skills.py [--vertical med|capital|both] [--dry-run]
"""

import argparse
import os
import sys
import textwrap
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, os.path.dirname(__file__))
from taxonomy_med import MEDICAL_TAXONOMY
from taxonomy_capital import CAPITAL_TAXONOMY


def slugify_subgroup(name: str) -> str:
    """Convert subgroup name to a tag-friendly slug."""
    return (
        name.lower()
        .replace(" & ", "-")
        .replace("/ ", "-")
        .replace(" / ", "-")
        .replace(" ", "-")
    )


def select_tags(skill_name: str, subgroup_name: str, description: str) -> list[str]:
    """Select 2-4 relevant tags based on skill characteristics."""
    tags = []

    # Workflow-type tags (inferred from name/description patterns)
    workflow_keywords = {
        "summarizing": "summarization",
        "synthesizing": "synthesis",
        "analyzing": "analysis",
        "interpreting": "analysis",
        "evaluating": "analysis",
        "assessing": "assessment",
        "scoring": "assessment",
        "calculating": "analysis",
        "drafting": "drafting",
        "writing": "drafting",
        "creating": "drafting",
        "documenting": "documentation",
        "reporting": "reporting",
        "managing": "management",
        "coordinating": "coordination",
        "conducting": "process",
        "tracking": "monitoring",
        "reviewing": "review",
        "auditing": "audit",
        "coding": "coding",
        "building": "modeling",
        "modeling": "modeling",
        "pricing": "valuation",
        "screening": "screening",
        "reconciling": "reconciliation",
        "monitoring": "monitoring",
        "planning": "planning",
        "preparing": "preparation",
        "designing": "design",
        "performing": "process",
        "validating": "validation",
        "mapping": "analysis",
        "investigating": "investigation",
        "counseling": "counseling",
        "forecasting": "forecasting",
    }

    # Get primary workflow tag from skill name's gerund
    first_word = skill_name.split("-")[0]
    if first_word in workflow_keywords:
        tags.append(workflow_keywords[first_word])

    # Add subgroup as a tag
    tags.append(slugify_subgroup(subgroup_name))

    # Add domain-specific tags from description keywords
    domain_tags = {
        "compliance": "compliance",
        "regulatory": "regulatory",
        "risk": "risk",
        "clinical": "clinical",
        "patient": "patient-care",
        "surgical": "surgical",
        "diagnostic": "diagnostic",
        "treatment": "treatment",
        "pharmacol": "pharmacology",
        "investment": "investment",
        "portfolio": "portfolio",
        "credit": "credit",
        "trading": "trading",
        "valuation": "valuation",
        "accounting": "accounting",
        "audit": "audit",
        "tax": "tax",
        "insurance": "insurance",
        "banking": "banking",
        "esg": "esg",
        "research": "research",
    }

    desc_lower = description.lower()
    for keyword, tag in domain_tags.items():
        if keyword in desc_lower and tag not in tags:
            tags.append(tag)
            if len(tags) >= 4:
                break

    return tags[:4]


def determine_skill_modes(skill_name: str) -> list[str]:
    """Determine skill_modes based on the skill's primary activity."""
    mode_map = {
        "summarizing": ["Summarization"],
        "synthesizing": ["Synthesis"],
        "analyzing": ["Analysis"],
        "interpreting": ["Analysis", "Interpretation"],
        "evaluating": ["Analysis", "Assessment"],
        "assessing": ["Assessment"],
        "scoring": ["Assessment", "Calculation"],
        "calculating": ["Calculation"],
        "drafting": ["Drafting"],
        "writing": ["Drafting"],
        "creating": ["Drafting", "Planning"],
        "documenting": ["Documentation"],
        "reporting": ["Reporting"],
        "managing": ["Management", "Coordination"],
        "coordinating": ["Coordination"],
        "conducting": ["Process Management"],
        "tracking": ["Monitoring"],
        "reviewing": ["Review", "Analysis"],
        "auditing": ["Audit", "Compliance"],
        "coding": ["Coding", "Classification"],
        "building": ["Modeling"],
        "modeling": ["Modeling", "Forecasting"],
        "pricing": ["Valuation", "Calculation"],
        "screening": ["Screening", "Filtering"],
        "reconciling": ["Reconciliation"],
        "monitoring": ["Monitoring"],
        "planning": ["Planning"],
        "preparing": ["Preparation"],
        "designing": ["Design"],
        "performing": ["Execution"],
        "validating": ["Validation"],
        "mapping": ["Analysis", "Mapping"],
        "investigating": ["Investigation"],
        "counseling": ["Counseling"],
        "forecasting": ["Forecasting"],
    }
    first_word = skill_name.split("-")[0]
    return mode_map.get(first_word, ["Analysis"])


def humanize_skill_name(skill_name: str) -> str:
    """Convert skill slug to human-readable title."""
    # Handle common abbreviations
    replacements = {
        "ecgs": "ECGs",
        "ecg": "ECG",
        "ekg": "EKG",
        "ct": "CT",
        "mri": "MRI",
        "ehr": "EHR",
        "hipaa": "HIPAA",
        "emtala": "EMTALA",
        "aml": "AML",
        "kyc": "KYC",
        "sox": "SOX",
        "esg": "ESG",
        "ipo": "IPO",
        "lbo": "LBO",
        "reit": "REIT",
        "nav": "NAV",
        "fpa": "FP&A",
        "fpna": "FP&A",
        "irb": "IRB",
        "nicu": "NICU",
        "adhd": "ADHD",
        "ptsd": "PTSD",
        "cds": "CDS",
        "fx": "FX",
        "var": "VaR",
        "xva": "XVA",
        "tmj": "TMJ",
        "iv": "IV",
        "vte": "VTE",
        "drg": "DRG",
        "cdi": "CDI",
        "icd": "ICD",
        "cpt": "CPT",
        "ofac": "OFAC",
        "sar": "SAR",
        "ctr": "CTR",
        "sba": "SBA",
        "cre": "CRE",
        "dei": "DEI",
        "ai": "AI",
        "nlp": "NLP",
        "cmbs": "CMBS",
        "api": "API",
        "pca": "PCA",
    }
    words = skill_name.split("-")
    titled = []
    for w in words:
        if w.lower() in replacements:
            titled.append(replacements[w.lower()])
        else:
            titled.append(w.capitalize())
    return " ".join(titled)


def generate_skill_body(
    skill_name: str, description: str, subgroup_name: str, practice_areas: list[str]
) -> str:
    """Generate the markdown body for a SKILL.md file.

    Follows the pattern from existing skills:
    - Title (H1)
    - One-line summary
    - Workflow section with numbered steps
    - Key Rules section
    - Guidelines/Common Pitfalls
    """
    title = humanize_skill_name(skill_name)

    # Extract the core action from description (first sentence before "Use when")
    core_desc = description.split(". Use when")[0].strip()

    # Build workflow steps from the description
    # We'll create a concise but structured workflow
    body = f"# {title}\n\n{core_desc}.\n\n"
    body += "## Workflow\n\n"

    # Generate contextually appropriate workflow steps
    first_word = skill_name.split("-")[0]

    if first_word in (
        "summarizing",
        "synthesizing",
        "condensing",
        "abstracting",
        "distilling",
    ):
        body += "1. **Collect** source documents and verify completeness\n"
        body += "2. **Extract** key data points, findings, and structured elements\n"
        body += "3. **Normalize** terminology and format for consistency\n"
        body += "4. **Structure** output using the template below\n"
        body += "5. **Validate** completeness against source material — flag gaps explicitly\n"
    elif first_word in (
        "analyzing",
        "evaluating",
        "assessing",
        "scoring",
        "interpreting",
    ):
        body += "1. **Gather** input data and confirm scope of analysis\n"
        body += "2. **Apply** relevant frameworks, criteria, or scoring methodology\n"
        body += "3. **Identify** key findings, patterns, and outliers\n"
        body += "4. **Assess** significance and implications of findings\n"
        body += "5. **Document** analysis with supporting evidence and limitations\n"
    elif first_word in ("drafting", "writing", "creating", "preparing"):
        body += "1. **Gather** required inputs and confirm deliverable requirements\n"
        body += "2. **Outline** structure using the appropriate template\n"
        body += "3. **Draft** content with domain-appropriate language and format\n"
        body += "4. **Review** against quality checklist and compliance requirements\n"
        body += "5. **Finalize** with proper formatting, citations, and required disclosures\n"
    elif first_word in ("managing", "coordinating", "tracking", "monitoring"):
        body += "1. **Identify** scope, stakeholders, and requirements\n"
        body += "2. **Assess** current state against standards or benchmarks\n"
        body += "3. **Execute** required actions with proper documentation\n"
        body += "4. **Monitor** progress against milestones and escalation criteria\n"
        body += "5. **Report** status, exceptions, and next steps\n"
    elif first_word in ("conducting", "performing", "investigating"):
        body += "1. **Plan** scope, methodology, and required resources\n"
        body += "2. **Execute** systematic evaluation following established protocols\n"
        body += "3. **Document** findings with evidence and methodology notes\n"
        body += "4. **Analyze** results against criteria or expected outcomes\n"
        body += "5. **Report** conclusions with recommendations and limitations\n"
    elif first_word in ("building", "modeling", "constructing", "designing"):
        body += "1. **Define** model scope, inputs, and assumptions\n"
        body += "2. **Structure** framework with appropriate methodology\n"
        body += "3. **Build** model with documented assumptions and sources\n"
        body += "4. **Validate** outputs with sensitivity analysis and reasonableness checks\n"
        body += "5. **Document** methodology, limitations, and key assumptions\n"
    elif first_word in ("reconciling",):
        body += "1. **Collect** data sources to be reconciled\n"
        body += "2. **Standardize** formats and reference identifiers\n"
        body += "3. **Match** corresponding items across sources\n"
        body += "4. **Identify** discrepancies with categorization and aging\n"
        body += "5. **Resolve** or escalate breaks with documentation\n"
    elif first_word in ("pricing", "calculating"):
        body += "1. **Gather** required inputs and market data\n"
        body += "2. **Select** appropriate methodology and models\n"
        body += "3. **Calculate** values with documented assumptions\n"
        body += "4. **Validate** results with cross-checks and reasonableness tests\n"
        body += "5. **Document** methodology, inputs, and output with sensitivity\n"
    elif first_word in ("reviewing", "auditing", "validating"):
        body += "1. **Define** review scope and applicable standards\n"
        body += "2. **Examine** subject matter against requirements systematically\n"
        body += "3. **Identify** findings with severity classification\n"
        body += "4. **Document** evidence supporting each finding\n"
        body += "5. **Recommend** corrective actions with priority and timeline\n"
    elif first_word in ("screening", "filtering"):
        body += "1. **Define** screening criteria and data sources\n"
        body += "2. **Apply** quantitative and qualitative filters\n"
        body += "3. **Rank** results by relevance and priority\n"
        body += "4. **Review** top candidates for false positives and edge cases\n"
        body += "5. **Document** methodology, results, and rationale for selections\n"
    elif first_word in ("forecasting",):
        body += "1. **Gather** historical data and current market conditions\n"
        body += "2. **Select** forecasting methodology and key assumptions\n"
        body += "3. **Build** projections with scenario analysis\n"
        body += "4. **Validate** against external benchmarks and consensus\n"
        body += "5. **Document** assumptions, methodology, and confidence ranges\n"
    else:
        body += "1. **Gather** required inputs and define scope\n"
        body += "2. **Process** information using appropriate methodology\n"
        body += "3. **Analyze** results against standards or criteria\n"
        body += "4. **Document** findings with supporting evidence\n"
        body += "5. **Deliver** structured output with quality verification\n"

    body += "\n## Key Rules\n\n"
    body += "- Always verify source data completeness before beginning\n"
    body += "- Flag assumptions explicitly — never present inferred data as confirmed\n"
    body += "- Use consistent terminology throughout the output\n"
    body += "- Note limitations and scope boundaries in the final output\n"
    body += (
        "- When in doubt about a data point, mark with [VERIFY] rather than guessing\n"
    )

    body += "\n## Guidelines\n\n"
    body += f"- This skill operates within the **{subgroup_name}** domain\n"
    body += f"- Relevant practice areas: {', '.join(practice_areas)}\n"
    body += "- Output should be actionable for domain professionals\n"
    body += "- Include appropriate disclaimers for compliance-sensitive outputs\n"
    body += "- Escalate to human review when confidence is low or stakes are high\n"

    return body


def generate_skill_md(
    skill_name: str,
    description: str,
    subgroup_name: str,
    practice_areas: list[str],
    vertical: str,  # "med" or "capital"
) -> str:
    """Generate complete SKILL.md content."""
    tags = select_tags(skill_name, subgroup_name, description)
    skill_modes = determine_skill_modes(skill_name)

    # Build YAML frontmatter
    lines = ["---"]
    lines.append(f"name: {skill_name}")

    # Description must be <= 1024 chars
    desc = description[:1024]
    lines.append(f"description: {desc}")

    lines.append("tags:")
    for tag in tags:
        lines.append(f"  - {tag}")

    lines.append("metadata:")
    lines.append("  author: casemark")
    lines.append("  practice_areas:")
    for pa in practice_areas:
        lines.append(f"    - {pa}")

    # Document types based on skill activity
    doc_types = determine_document_types(skill_name, subgroup_name)
    lines.append("  document_types:")
    for dt in doc_types:
        lines.append(f"    - {dt}")

    lines.append("  skill_modes:")
    for sm in skill_modes:
        lines.append(f"    - {sm}")

    lines.append("---")
    lines.append("")

    # Body
    body = generate_skill_body(skill_name, description, subgroup_name, practice_areas)
    lines.append(body)

    return "\n".join(lines)


def determine_document_types(skill_name: str, subgroup_name: str) -> list[str]:
    """Determine document_types based on skill and subgroup."""
    first_word = skill_name.split("-")[0]

    type_map = {
        "summarizing": ["Summary Report"],
        "synthesizing": ["Synthesis Report"],
        "analyzing": ["Analysis Report"],
        "interpreting": ["Interpretation Report"],
        "evaluating": ["Evaluation Report"],
        "assessing": ["Assessment Report"],
        "scoring": ["Score Card"],
        "calculating": ["Calculation Worksheet"],
        "drafting": ["Draft Document"],
        "writing": ["Written Document"],
        "creating": ["New Document"],
        "documenting": ["Clinical Documentation"],
        "reporting": ["Report"],
        "managing": ["Management Report"],
        "coordinating": ["Coordination Plan"],
        "conducting": ["Process Documentation"],
        "tracking": ["Tracking Report"],
        "reviewing": ["Review Report"],
        "auditing": ["Audit Report"],
        "coding": ["Coded Record"],
        "building": ["Model"],
        "modeling": ["Financial Model"],
        "pricing": ["Valuation Report"],
        "screening": ["Screening Report"],
        "reconciling": ["Reconciliation Report"],
        "monitoring": ["Monitoring Report"],
        "planning": ["Plan Document"],
        "preparing": ["Preparation Document"],
        "designing": ["Design Document"],
        "performing": ["Procedure Note"],
        "validating": ["Validation Report"],
        "mapping": ["Mapping Document"],
        "investigating": ["Investigation Report"],
        "counseling": ["Counseling Note"],
        "forecasting": ["Forecast Report"],
    }

    return type_map.get(first_word, ["Report"])


def generate_vertical(
    taxonomy: dict,
    vertical_name: str,  # "med" or "capital"
    output_dir: Path,
    dry_run: bool = False,
) -> tuple[int, int]:
    """Generate all skills for a vertical. Returns (created, skipped)."""
    created = 0
    skipped = 0

    for subgroup_name, subgroup_data in taxonomy.items():
        practice_areas = subgroup_data["practice_areas"]

        for skill_name, description in subgroup_data["skills"]:
            skill_dir = output_dir / skill_name
            skill_file = skill_dir / "SKILL.md"

            if dry_run:
                print(f"  [DRY RUN] Would create: {skill_file}")
                created += 1
                continue

            skill_dir.mkdir(parents=True, exist_ok=True)

            content = generate_skill_md(
                skill_name=skill_name,
                description=description,
                subgroup_name=subgroup_name,
                practice_areas=practice_areas,
                vertical=vertical_name,
            )

            skill_file.write_text(content)
            created += 1

    return created, skipped


def check_name_collisions(taxonomy: dict) -> list[str]:
    """Check for duplicate skill names within a taxonomy."""
    seen = {}
    collisions = []
    for subgroup_name, subgroup_data in taxonomy.items():
        for skill_name, _ in subgroup_data["skills"]:
            if skill_name in seen:
                collisions.append(
                    f"  COLLISION: '{skill_name}' in both '{seen[skill_name]}' and '{subgroup_name}'"
                )
            seen[skill_name] = subgroup_name
    return collisions


def main():
    parser = argparse.ArgumentParser(
        description="Generate SKILL.md files for med/capital verticals"
    )
    parser.add_argument(
        "--vertical",
        choices=["med", "capital", "both"],
        default="both",
        help="Which vertical to generate (default: both)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("skills"),
        help="Base output directory (default: skills/)",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("AgentSkills Generator — Medical & Capital Verticals")
    print("=" * 60)

    # Check for name collisions first
    if args.vertical in ("med", "both"):
        collisions = check_name_collisions(MEDICAL_TAXONOMY)
        if collisions:
            print("\n⚠ Medical taxonomy name collisions:")
            for c in collisions:
                print(c)
            sys.exit(1)

    if args.vertical in ("capital", "both"):
        collisions = check_name_collisions(CAPITAL_TAXONOMY)
        if collisions:
            print("\n⚠ Capital taxonomy name collisions:")
            for c in collisions:
                print(c)
            sys.exit(1)

    # Check for cross-vertical collisions
    if args.vertical == "both":
        med_names = set()
        for data in MEDICAL_TAXONOMY.values():
            for name, _ in data["skills"]:
                med_names.add(name)
        cap_names = set()
        for data in CAPITAL_TAXONOMY.values():
            for name, _ in data["skills"]:
                cap_names.add(name)
        cross = med_names & cap_names
        if cross:
            print(f"\n⚠ Cross-vertical collisions: {cross}")
            # These go to separate directories, so warn but don't block
            print("  (These are in separate directories, so proceeding)")

    total_created = 0
    total_skipped = 0

    if args.vertical in ("med", "both"):
        print(f"\nGenerating Medical skills → {args.output_dir}/med/")
        med_dir = args.output_dir / "med"
        created, skipped = generate_vertical(
            MEDICAL_TAXONOMY, "med", med_dir, args.dry_run
        )
        total_created += created
        total_skipped += skipped
        print(f"  Medical: {created} created, {skipped} skipped")

    if args.vertical in ("capital", "both"):
        print(f"\nGenerating Capital skills → {args.output_dir}/capital/")
        cap_dir = args.output_dir / "capital"
        created, skipped = generate_vertical(
            CAPITAL_TAXONOMY, "capital", cap_dir, args.dry_run
        )
        total_created += created
        total_skipped += skipped
        print(f"  Capital: {created} created, {skipped} skipped")

    print(f"\nTotal: {total_created} created, {total_skipped} skipped")
    print("Done.")


if __name__ == "__main__":
    main()
