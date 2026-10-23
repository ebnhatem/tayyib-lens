# Prompt builder — MODIFY to model-executable prompt

How a MODIFY safe_alternative maps to a model-executable generation prompt.
Per the Phase-4 template rules, the fiqh terms live in the RULE while the
PROMPT carries only visual vocabulary: every coverage constraint maps to a
wardrobe fact, never a fiqh word.

## Template skeleton

MODIFY prompts instantiate these slots in order:

```
SUBJECT: <scene description, only male and/or female figures>
WARDROBE — MALE figures: loose opaque garments; navel-to-knee fully covered;
  full-length trousers; no form-revealing fit; no bare torso.
WARDROBE — FEMALE figures: hair and neck fully covered by a headscarf; loose
  opaque garments from neck to ankle; no form-revealing fit;
  <profile-conditional clause, compiled at routing time>.
POSE & FRAMING: <respectful distance between unrelated figures; no physical
  contact; camera distance per framing conditions>.
STYLE & MEDIUM: <photorealistic / illustration / watercolor / flat vector;
  stated purpose>.
NEGATIVE BLOCK: no figures other than male or female; no revealing or
  tight-fitting clothing; no swimwear or lingerie contexts; no isolated body
  regions in frame; no beauty-glamour close-ups of female figures; no text
  unless the request specifies it.
```

## Slot mapping

- SUBJECT — the scene from the request, restated with figure genders made
  explicit; figures are male and/or female only.
- WARDROBE (male / female) — the coverage line rendered as garment facts:
  which parts cloth covers, looseness, opacity, length. Per run-1 evidence,
  bare coverage phrases are not model-executable instructions, so each
  constraint names a garment behavior.
- PROFILE-conditional clause — compiled at routing time, never shipped with
  both variants: per Dar al-Ifta Fatwa 1214, the egypt-dar-alifta clause
  renders face and hands visible; per the maintainer's Phase-4 D1 decision,
  the hanafi-conservative clause renders a face covering leaving only the
  eyes visible, and an uncovered-face request routes to REVIEW with this
  covered variant as the MODIFY offer. Close-up beauty framings and glamour
  styling route to REVIEW under both profiles.
- POSE & FRAMING — distance between unrelated figures, contact, and camera
  distance; beauty-glamour close-ups of female figures stay in the negative
  block.
- STYLE & MEDIUM — medium plus the request's stated purpose.
- NEGATIVE BLOCK — the fixed exclusions above, appended verbatim; prompts stay
  generator-agnostic plain descriptive sentences with no platform-specific
  syntax.

See prompts/awra-aware-modify.md for the instantiated template and a worked
before → after example.
