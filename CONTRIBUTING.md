# Contributing to TayyibLens

Thank you for improving this evidence-first project.

## Ground rules
1. **Attributive voice only.** Never write "TayyibLens allows/forbids X". Write
   "per [source + locator], X routes to [verdict] under [profile]".
2. **No rule without evidence.** Every rule needs source_type, exact locator,
   illah, disagreement note, profile verdicts, and a safe alternative
   (references/evidence-schema.md).
3. **Four-layer separation.** Keep these distinct and labeled in every evidence file:
   text → tafsir → madhhab position → contemporary fatwa → policy extrapolation.
4. **No full-text republication.** Quote short excerpts with locators; link originals.
   Full sources stay out of this repository.
5. **Disagreement is data.** Contested zones stay profile-bound REVIEW — never flatten
   khilaf into one verdict.

## Contribution types
- **Evidence correction** (highest priority): an error in citation, takhrij, or
  attribution → open an "Evidence error" issue.
- **New source**: a published institutional fatwa or classical passage in scope →
  "New source proposal" issue with locator.
- **New profile**: a coherent line (e.g., Shafi'i, Maliki) with its evidence set.
- **Tests**: regression cases for existing rules (tests/).
- **Code**: scripts/ improvements.

## Pull request checklist
- [ ] Every new rule has full evidence fields
- [ ] Tests updated (tests/*.yaml) and `python scripts/validate.py` passes
- [ ] Voice discipline respected (no unsourced verdicts anywhere)
- [ ] Short quotes only, with locators
