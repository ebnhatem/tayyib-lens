# TayyibLens — Agent Guide (public repo)

TayyibLens is an Agent Skill that screens AI image/audio generation requests against
cited Islamic fiqh evidence. It is a lens that magnifies published rulings — it is
NOT a mufti and never originates a verdict.

## Commands

- Validate everything (run before every commit): `python scripts/validate.py`
- One-time hook setup: `git config core.hooksPath .githooks` (then `chmod +x .githooks/pre-commit`)

## Voice discipline (mandatory, enforced by CI)

Always write in the attributive voice: "per Dar al-Ifta Fatwa 16964, X routes to MODIFY".
NEVER write "TayyibLens allows/forbids/rules/judges X". The subject of every ruling is
the cited source, never this project.

## Hard boundaries — never do

- Never commit full source texts (books, fatwa pages). Short quoted excerpts with
  locators only. Full texts live outside this repo, in `private/` (which you must
  never reference by path in any repo file).
- Never change the `name:` field in SKILL.md (must equal the directory name).
- Never flatten a khilaf (scholarly disagreement) into a single verdict; contested
  zones stay profile-bound `REVIEW`.
- Never use governor/judge/creator/criterion role words for this project
  (rejected-words taxonomy in references/glossary.md).
- Never commit with `--no-verify`; never force-push `main`.
- Never create tags, releases, or version bumps unless the task explicitly asks for one.
  Versioning follows GOVERNANCE.md: MAJOR = verdict changes, MINOR = new rules/sources,
  PATCH = corrections. Versions never encode dates.

## Commit convention (Conventional Commits)

Format: `type(scope): imperative subject, max 72 chars`

| type | use for | scope |
|---|---|---|
| `feat` | new rules, sources, profiles, rewrite patterns | policies, knowledge, profiles, prompts |
| `fix` | corrections to locators, citations, verdicts | policies, knowledge, citations |
| `docs` | README, references, methodology | readme, references |
| `test` | regression cases | tests |
| `chore` | CI, hooks, tooling | ci, scripts |

Examples:
- `feat(policies): add rule visual.full_body_animate (Bukhari 5954)`
- `fix(knowledge): correct takhrij note for ma'azif hadith`

When a commit adds or changes a rule, the body must include the source locator.

## Branches and PRs

- Branches: `scope/short-description` (e.g. `policies/audio-rules`, `knowledge/hadith-takhrij`)
- Open a PR into `main` even for your own work; merge only when CI (validate.yml) is green.
- Squash before merge; the squash commit follows the convention above.

## Definition of done (a change is complete only when)

1. `python scripts/validate.py` passes
2. New rules have full schema fields + a CITATION.md row
3. tests/*.yaml updated if a verdict or trigger changed
4. Voice discipline holds everywhere, including comments

## Directory map (nearest AGENTS.md wins)

- `knowledge/` — evidence cards and their extraction rules
- `policies/` — executable rules, schema, universal prohibitions
- `profiles/` — fiqh line definitions
- `prompts/` — safe-rewrite patterns
- `tests/` — regression cases
- `references/` — schema, glossary, methodology
- `scripts/` — validation tooling
