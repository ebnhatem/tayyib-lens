# prompts/ — safe-rewrite patterns

## Rules
- Each pattern: heading anchor, one-line purpose, the transformation rule,
  a worked example (before → after).
- Rewrites must land strictly in the permissible zone of the referenced profile —
  when in doubt, the rewrite itself routes to REVIEW.
- Keep patterns template-like and generator-agnostic (no platform-specific syntax).

## Committing
`feat(prompts): add <anchor> pattern for <category>` — body cites the rule it serves.
