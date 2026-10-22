# tests/ — regression cases

## Rules
- One case per behavior: case_id, request, expect (verdict), profile where relevant,
  reason/note citing the rule.
- Cases must cover: universal prohibitions (expect REJECT), clearly permissible
  content (expect ALLOW), MODIFY rewrites, and REVIEW/identity-gate deferrals.
- Verdict or trigger changes in policies/ REQUIRE updating the corresponding case.
- Never weaken a test to make a rule pass — fix the rule or escalate to the maintainer.

## Committing
`test(tests): <what is covered>` — body references the rule ids covered.
