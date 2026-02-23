#!/usr/bin/env python3
"""Migrate SKILL.md files from metadata.{practice_areas,document_types,skill_modes} to flat tags array."""

import os
import re
import sys
import yaml
from pathlib import Path
from collections import Counter

LEGAL_DIR = Path(__file__).resolve().parent.parent / "skills" / "legal"

# === Canonical tags (18 total) ===
VALID_TAGS = {
    # Practice area (4)
    "litigation", "corporate", "transactional", "regulatory",
    # Document type (10)
    "agreement", "pleading", "motion", "brief", "memo",
    "letter", "summary", "analysis", "checklist", "policy",
    # Skill mode (4)
    "drafting", "summarization", "analysis", "research",
}

# === Mapping tables ===

# practice_areas -> canonical practice area tag(s)
PRACTICE_AREA_MAP = {
    "litigation": ["litigation"],
    "transactional": ["transactional"],
    "regulatory": ["regulatory"],
    "corporate": ["corporate"],
    "family law": ["litigation"],
    "family-law": ["litigation"],
    "real estate": ["transactional"],
    "estate planning": ["transactional"],
    "securities": ["regulatory", "corporate"],
    "bankruptcy": ["litigation"],
    "technology": ["transactional"],
    "commercial": ["transactional"],
    "nonprofit": ["corporate"],
    "regulatory compliance": ["regulatory"],
    "general": [],
    "personal injury": ["litigation"],
    "intellectual property": ["transactional", "litigation"],
    "insurance": ["litigation"],
    "environmental": ["regulatory"],
    "elder law": ["litigation"],
    "appellate": ["litigation"],
    "appeals": ["litigation"],
    "unspecified": [],
    "animal law": ["litigation"],
    "criminal": ["litigation"],
    "employment": ["litigation"],
    "health law": ["regulatory"],
    "risk management": ["regulatory"],
    "construction": ["litigation", "transactional"],
    "property law": ["transactional"],
    "mental health": ["regulatory"],
    "health care": ["regulatory"],
    "general practice": [],
    "civil procedure": ["litigation"],
}

# document_types -> canonical document type tag(s)
DOCUMENT_TYPE_MAP = {
    "agreement": ["agreement"],
    "summary": ["summary"],
    "pleading": ["pleading"],
    "memo": ["memo"],
    "letter": ["letter"],
    "analysis": ["analysis"],
    "checklist": ["checklist"],
    "motion": ["motion"],
    "brief": ["brief"],
    "contract": ["agreement"],
    "reference": [],
    "outline": ["checklist"],
    "notice": ["letter"],
    "policy": ["policy"],
    "form": [],
    "compliance guide": ["policy"],
    "certificate": [],
    "table": [],
    "filing": [],
    "resolution": [],
    "memorandum": ["memo"],
    "subpoena": ["pleading"],
    "application": [],
    "worksheet": ["checklist"],
    "report": ["summary"],
    "disclosure": [],
    "tax return": [],
    # Common singletons
    "case brief": ["brief"],
    "exhibit": [],
    "prospectus": [],
    "errata sheet": [],
    "research memo": ["memo"],
    "legal memorandum": ["memo"],
    "settlement agreement analysis": ["analysis"],
    "deposition transcript": ["summary"],
    "deposition summary": ["summary"],
    "client handout": ["summary"],
    "table of contents": ["checklist"],
    "table of authorities": ["checklist"],
    "formation document": ["agreement"],
    "background check report": ["summary"],
    "questionnaire": ["checklist"],
    "verification": [],
    "privilege log": ["checklist"],
    "case summary": ["summary"],
    "case evaluation": ["analysis"],
    "case summary report": ["summary"],
    "compliance matrix": ["checklist"],
    "regulatory filing": [],
    "settlement statement": ["summary"],
    "compliance report": ["summary"],
    "insurance certificate": [],
    "damages calculation": ["analysis"],
    "demand package": ["letter"],
    "deposition": ["summary"],
    "impeachment sequence": ["checklist"],
    "deposition outline": ["checklist"],
    "tracker": ["checklist"],
    "chart": ["summary"],
    "separate statement": ["pleading"],
    "discovery summary": ["summary"],
    "audit memorandum": ["memo"],
    "compliance audit": ["analysis"],
    "contract review": ["analysis"],
    "instruction letter": ["letter"],
    "compliance review": ["analysis"],
    "discovery": ["pleading"],
    "fact sheet": ["summary"],
    "advance directive": ["agreement"],
    "settlement summary": ["summary"],
    "registration statement": [],
    "correspondence": ["letter"],
    "deposition notice": ["pleading"],
    "discovery package": ["pleading"],
    "certificate review": ["analysis"],
    "compliance memo": ["memo"],
    "petition": ["pleading"],
    "complaint": ["pleading"],
    "order": [],
    "declaration": ["pleading"],
    "affidavit": ["pleading"],
    "stipulation": ["agreement"],
    "interrogatories": ["pleading"],
    "demand": ["letter"],
    "response": ["pleading"],
    "objection": ["motion"],
    "plan": ["checklist"],
    "audit": ["analysis"],
    "opinion": ["memo"],
    "opinion letter": ["memo", "letter"],
    "manual": ["policy"],
    "program": ["policy"],
    "assessment": ["analysis"],
    "charter": ["policy"],
    "consent": ["agreement"],
    "deed": ["agreement"],
    "trust": ["agreement"],
    "will": ["agreement"],
    "license": ["agreement"],
    "lease": ["agreement"],
    "note": ["agreement"],
    "guarantee": ["agreement"],
    "guaranty": ["agreement"],
    "indemnity": ["agreement"],
    "waiver": ["agreement"],
    "release": ["agreement"],
    "amendment": ["agreement"],
    "addendum": ["agreement"],
    "rider": ["agreement"],
    "supplement": [],
    "schedule": ["checklist"],
    "exhibit list": ["checklist"],
    "jury instructions": ["brief"],
    "verdict form": [],
    "statement": ["brief"],
    "claim": ["pleading"],
    "proof of claim": ["pleading"],
}

# skill_modes -> canonical skill mode tag(s)
SKILL_MODE_MAP = {
    "drafting": ["drafting"],
    "analysis": ["analysis"],
    "summarization": ["summarization"],
    "research": ["research"],
    "review": ["analysis"],
    "compliance review": ["analysis"],
    "compliance": ["analysis"],
    "reference": ["research"],
    "extraction": ["summarization"],
    "calculation": ["analysis"],
    "negotiation": ["drafting"],
    "project management": ["drafting"],
    "workflow": ["drafting"],
    "formatting": ["drafting"],
    "valuation": ["analysis"],
    "planning": ["drafting"],
    "reconciliation": ["analysis"],
}


def parse_skill(filepath):
    """Parse a SKILL.md file, returning (frontmatter_dict, body_str, raw_content).

    Uses regex extraction for name/description to handle unquoted colons,
    then falls back to yaml.safe_load for the metadata block.
    """
    content = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        return None, None, content

    fm_raw = match.group(1)
    body = match.group(2)

    # Try yaml.safe_load first
    try:
        fm = yaml.safe_load(fm_raw)
        if isinstance(fm, dict) and "name" in fm:
            return fm, body, content
    except yaml.YAMLError:
        pass

    # Fallback: manually parse name, description, and metadata
    fm = {}

    # Extract name
    name_match = re.search(r"^name:\s*(.+)$", fm_raw, re.MULTILINE)
    if name_match:
        fm["name"] = name_match.group(1).strip()

    # Extract description - may span multiple lines before metadata/tags
    desc_match = re.search(r"^description:\s*(.+?)(?=\n(?:metadata:|tags:)|\Z)", fm_raw, re.MULTILINE | re.DOTALL)
    if desc_match:
        desc = desc_match.group(1).strip()
        # Clean up multiline descriptions
        desc = re.sub(r"\s*\n\s*", " ", desc)
        fm["description"] = desc

    # Extract metadata block if present
    meta_match = re.search(r"^metadata:\s*\n((?:[ \t]+.+\n?)*)", fm_raw, re.MULTILINE)
    if meta_match:
        meta_block = "metadata:\n" + meta_match.group(1)
        try:
            meta_parsed = yaml.safe_load(meta_block)
            if isinstance(meta_parsed, dict):
                fm["metadata"] = meta_parsed.get("metadata", {})
        except yaml.YAMLError:
            # Last resort: regex extract arrays
            fm["metadata"] = {}
            for field in ["practice_areas", "document_types", "skill_modes"]:
                items = re.findall(rf"^\s+-\s+(.+)$",
                    re.search(rf"{field}:\s*\n((?:\s+-\s+.+\n?)*)", meta_block, re.MULTILINE).group(1) if re.search(rf"{field}:\s*\n", meta_block) else "",
                    re.MULTILINE)
                if items:
                    fm["metadata"][field] = [i.strip() for i in items]

    # Extract tags block if present (for already-migrated files)
    tags_match = re.search(r"^tags:\s*\n((?:\s+-\s+.+\n?)*)", fm_raw, re.MULTILINE)
    if tags_match:
        fm["tags"] = [t.strip() for t in re.findall(r"^\s+-\s+(.+)$", tags_match.group(1), re.MULTILINE)]

    return fm, body, content


def map_tags(metadata):
    """Convert metadata dict to flat list of canonical tags."""
    tags = set()

    # Map practice_areas
    for pa in metadata.get("practice_areas", []):
        key = pa.strip().lower()
        if key in PRACTICE_AREA_MAP:
            tags.update(PRACTICE_AREA_MAP[key])

    # Map document_types
    for dt in metadata.get("document_types", []):
        key = dt.strip().lower()
        if key in DOCUMENT_TYPE_MAP:
            tags.update(DOCUMENT_TYPE_MAP[key])

    # Map skill_modes
    for sm in metadata.get("skill_modes", []):
        key = sm.strip().lower()
        if key in SKILL_MODE_MAP:
            tags.update(SKILL_MODE_MAP[key])

    return sorted(tags)


def build_new_frontmatter(fm, tags):
    """Build new frontmatter dict with tags, without metadata."""
    new_fm = {}
    new_fm["name"] = fm["name"]
    new_fm["description"] = fm["description"]
    if tags:
        new_fm["tags"] = tags
    return new_fm


def serialize_frontmatter(fm):
    """Serialize frontmatter to YAML string, preserving key order."""
    lines = []
    lines.append(f"name: {fm['name']}")

    # Description might be multiline or contain special chars
    desc = fm["description"]
    if "\n" in desc or ": " in desc or desc.startswith(("{", "[", "'", '"', "&", "*", "!", "|", ">")):
        # Use YAML block scalar for complex descriptions
        lines.append("description: >-")
        # Wrap at ~78 chars
        words = desc.split()
        current_line = "  "
        for word in words:
            if len(current_line) + len(word) + 1 > 78:
                lines.append(current_line)
                current_line = "  " + word
            else:
                if current_line == "  ":
                    current_line += word
                else:
                    current_line += " " + word
        if current_line.strip():
            lines.append(current_line)
    else:
        lines.append(f"description: {desc}")

    if fm.get("tags"):
        lines.append("tags:")
        for tag in fm["tags"]:
            lines.append(f"  - {tag}")

    return "\n".join(lines)


def migrate_file(filepath, dry_run=False):
    """Migrate a single SKILL.md file. Returns (slug, old_tags_count, new_tags, unmapped)."""
    fm, body, raw = parse_skill(filepath)
    if fm is None:
        return None, 0, [], []

    slug = fm.get("name", filepath.parent.name)
    metadata = fm.get("metadata", {})

    # Track unmapped values
    unmapped = []
    for pa in metadata.get("practice_areas", []):
        if pa.strip().lower() not in PRACTICE_AREA_MAP:
            unmapped.append(f"practice_area:{pa}")
    for dt in metadata.get("document_types", []):
        if dt.strip().lower() not in DOCUMENT_TYPE_MAP:
            unmapped.append(f"document_type:{dt}")
    for sm in metadata.get("skill_modes", []):
        if sm.strip().lower() not in SKILL_MODE_MAP:
            unmapped.append(f"skill_mode:{sm}")

    tags = map_tags(metadata)
    old_count = (
        len(metadata.get("practice_areas", []))
        + len(metadata.get("document_types", []))
        + len(metadata.get("skill_modes", []))
    )

    if not dry_run:
        new_fm = build_new_frontmatter(fm, tags)
        new_yaml = serialize_frontmatter(new_fm)
        new_content = f"---\n{new_yaml}\n---\n{body}"
        filepath.write_text(new_content, encoding="utf-8")

    return slug, old_count, tags, unmapped


def main():
    dry_run = "--dry-run" in sys.argv
    verbose = "--verbose" in sys.argv

    if dry_run:
        print("=== DRY RUN — no files will be modified ===\n")

    skill_dirs = sorted(
        d for d in LEGAL_DIR.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    )

    print(f"Found {len(skill_dirs)} skill directories\n")

    all_unmapped = []
    tag_counts = Counter()
    no_tags = []
    migrated = 0
    errors = []

    for d in skill_dirs:
        filepath = d / "SKILL.md"
        try:
            slug, old_count, tags, unmapped = migrate_file(filepath, dry_run)
            if slug is None:
                errors.append(f"{d.name}: failed to parse frontmatter")
                continue

            migrated += 1
            for t in tags:
                tag_counts[t] += 1
            if not tags:
                no_tags.append(slug)
            all_unmapped.extend(unmapped)

            if verbose:
                print(f"  {slug}: {old_count} metadata values -> {tags}")

        except Exception as e:
            errors.append(f"{d.name}: {e}")

    # Report
    print(f"\n{'Would migrate' if dry_run else 'Migrated'}: {migrated} skills")
    print(f"Errors: {len(errors)}")
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")

    print(f"\nSkills with NO tags: {len(no_tags)}")
    if no_tags:
        for s in no_tags:
            print(f"  - {s}")

    print(f"\nUnmapped metadata values: {len(all_unmapped)}")
    unmapped_counts = Counter(all_unmapped)
    for val, count in unmapped_counts.most_common():
        print(f"  {val} ({count})")

    print(f"\nTag distribution:")
    for tag, count in tag_counts.most_common():
        print(f"  {tag}: {count}")


if __name__ == "__main__":
    main()
