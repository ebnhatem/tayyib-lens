#!/usr/bin/env python3
"""Validate SKILL.md frontmatter and rule YAML schema. Exit 1 on any failure."""
import re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_RULE_FIELDS = ["rule_id", "category", "trigger", "verdict", "profiles",
                        "evidence", "illah", "disagreement", "safe_alternative"]
VALID_VERDICTS = {"ALLOW", "MODIFY", "REVIEW", "REJECT"}
errors = []

# 1. SKILL.md frontmatter
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not fm:
    errors.append("SKILL.md: missing frontmatter block")
else:
    name = re.search(r"^name:\s*(.+)$", fm.group(1), re.M)
    desc = re.search(r"^description:\s*(.+)$", fm.group(1), re.M)
    if not name or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name.group(1).strip()):
        errors.append(f"SKILL.md: invalid name field: {name and name.group(1)}")
    else:
        expected_dir = ROOT.name
        if name.group(1).strip() != expected_dir:
            errors.append(f"SKILL.md: name '{name.group(1)}' != directory '{expected_dir}'")
    if not desc:
        errors.append("SKILL.md: missing description")
    elif not (1 <= len(desc.group(1)) <= 1024):
        errors.append("SKILL.md: description must be 1-1024 chars")

def try_yaml(path):
    try:
        import yaml
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except ImportError:
        # minimal fallback: cannot parse; skip content checks
        return None
    except Exception as e:
        errors.append(f"{path.relative_to(ROOT)}: YAML parse error: {e}")
        return None

# 2. rule files in policies/
for p in sorted((ROOT / "policies").glob("*.yaml")):
    data = try_yaml(p)
    if not isinstance(data, list):
        continue
    for i, rule in enumerate(data):
        for field in REQUIRED_RULE_FIELDS:
            if field not in rule:
                errors.append(f"{p.name}[{i}]: missing field '{field}' (rule {rule.get('rule_id','?')})")
        v = rule.get("verdict")
        if v and v not in VALID_VERDICTS:
            errors.append(f"{p.name}[{i}]: invalid verdict '{v}'")

# 3. voice discipline scan: unsourced ruling claims
banned = re.compile(r"(tayyiblens|this skill)\s+(allows|forbids|permits|rules|judges)", re.I)
for p in ROOT.rglob("*.md"):
    if ".git" in p.parts: continue
    m = banned.search(p.read_text(encoding="utf-8", errors="ignore"))
    if m:
        errors.append(f"{p.relative_to(ROOT)}: voice discipline violation: '{m.group(0)}'")

if errors:
    print("VALIDATION FAILED:")
    for e in errors: print(" -", e)
    sys.exit(1)
print("All checks passed.")
