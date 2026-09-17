#!/usr/bin/env python3
"""Check this suite's entrypoints and portable runtime reference integrity."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
errors = []
entries = sorted(SKILLS.glob("*/SKILL.md"))
if len(entries) != 16:
    errors.append(f"Expected 16 skills, found {len(entries)}")
for entry in entries:
    text = entry.read_text()
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        errors.append(f"{entry.relative_to(ROOT)}: missing frontmatter")
        continue
    name = re.search(r"^name: (.+)$", parts[1], re.M)
    description = re.search(r"^description: (.+)$", parts[1], re.M)
    if not name or name.group(1).strip() != entry.parent.name:
        errors.append(f"{entry.relative_to(ROOT)}: name differs from folder")
    if not description or not description.group(1).strip():
        errors.append(f"{entry.relative_to(ROOT)}: missing description")
references = 0
for file in SKILLS.rglob("*.md"):
    text = file.read_text()
    if "/Users/" in text or re.search(r"/home/[^ /]+/", text):
        errors.append(f"{file.relative_to(ROOT)}: machine-specific home path")
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if "://" in link or link.startswith("#"):
            continue
        target = (file.parent / link.split("#", 1)[0]).resolve()
        references += 1
        if not target.is_relative_to(SKILLS.resolve()) or not target.exists():
            errors.append(f"{file.relative_to(ROOT)}: invalid local reference {link}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: {len(entries)} skills; {references} portable local references")
