# TayyibLens — عدسة الطيب

**Pure by design.** Cited fiqh evidence for AI-generated images and audio.

> TayyibLens does not tell you what is halal; it shows you what the scholars said,
> where they said it, and where they disagreed.

An open **Agent Skill** (agentskills.io open standard) that screens image and audio
generation requests against a citation-backed corpus of Islamic legal evidence —
Quran, authenticated hadith, Hanafi fiqh, and institutional fatwas (Dar al-Ifta,
IslamWeb, IIFA Resolution 258/3-26).

## What it is / What it is not
<!-- TODO: paste the is/is-not matrix from the PRD -->

## Install
<!-- TODO: install instructions per platform (Claude Code, Codex CLI, Gemini CLI, etc.) -->

## Profiles
| Profile | Line | Notes |
|---|---|---|
| `hanafi-conservative` | Hanafi | cautious defaults, prefers leaving what is contested |
| `egypt-dar-alifta` | Egyptian institutions | wider in photography/controlled music, strict on deepfakes |
| `institutional-ai-safety` | IIFA 258 | purpose, rights, transparency conditions |

## Evidence discipline
Every rule carries: source_type, locator (URL + volume/page), illah, disagreement,
profile verdicts, and a safe alternative. See references/evidence-schema.md.

## Contributing
See CONTRIBUTING.md. Scholarly corrections are explicitly welcomed —
open an "Evidence error" issue with the corrected source and locator.

## Important disclaimers
- TayyibLens is **not** a fatwa engine and issues no rulings of its own.
- Contested questions route to REVIEW and defer to qualified scholars.
- This project does not claim to represent any madhhab or institution.

## License
- Code (scripts/): MIT — see LICENSE
- Knowledge & policy files: CC BY 4.0 — see LICENSE-CONTENT.md
