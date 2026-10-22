# policies/ — executable rules

## Rules
- Follow the schema in references/evidence-schema.md exactly; required fields:
  rule_id, category, trigger, verdict, profiles, evidence, illah, disagreement,
  safe_alternative. Verdicts: ALLOW, MODIFY, REVIEW, REJECT.
- Every rule needs evidence from the knowledge/ layer that supports it —
  never invent evidence inline; reference the card.
- Contested issues keep per-profile verdicts (e.g. REJECT for one profile, MODIFY
  for another) and stay REVIEW where the corpus disagrees.
- `universal-prohibitions.yaml` is REJECT-only, agreed across surveyed lines,
  and requires maintainer + (when possible) advisory review to change.
- Any rule you add or change requires a matching test case in tests/.

## Committing
- `feat(policies): add rule <rule_id> (<primary source id>)`
- `fix(policies): correct <field> for <rule_id>` — include the corrected locator.
Definition of done: validate.py passes, test case added, CITATION.md updated.
