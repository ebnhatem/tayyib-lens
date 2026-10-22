# scripts/ — validation tooling

## Rules
- validate.py is the gatekeeper: SKILL.md frontmatter, rule schema, verdict values,
  voice discipline. Extend it; do not weaken checks to make content pass.
- Changes here are `chore(scripts)` and need a demonstration of the new check
  failing then passing, in the PR description.
- Keep dependencies stdlib-first (yaml is the only optional import; degrade
  gracefully when missing — the CI installs it).

## Committing
`chore(scripts): <change>` — include before/after behavior in the body.
