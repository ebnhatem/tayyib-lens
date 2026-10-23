# Awra-aware MODIFY prompt template

## awra-aware-modify

Turn a human-subject request into a model-executable generation prompt whose
wardrobe facts match the applied profile's published line — per Dar al-Ifta
Fatwa 1214, the egypt-dar-alifta profile renders face and hands visible with
hair, neck, and body covered; per the maintainer's Phase-4 D1 decision, an
uncovered-face request under hanafi-conservative routes to REVIEW and the
MODIFY output offers the face-covering variant below.

Transformation rule: instantiate every slot in the template; compile the
profile-conditional wardrobe clause at routing time; keep the prompt itself to
visual vocabulary only (garments, coverage, fit, framing) — per the
prompt-builder reference, every coverage constraint maps to a wardrobe fact.

```
SUBJECT: <scene description; only male and/or female figures>
WARDROBE — MALE figures: loose opaque garments; navel-to-knee fully covered;
  full-length trousers; no form-revealing fit; no bare torso.
WARDROBE — FEMALE figures: hair and neck fully covered by a headscarf; loose
  opaque garments from neck to ankle; no form-revealing fit.
  PROFILE CLAUSE (compile one at routing time):
  - egypt-dar-alifta: face and hands visible; headscarf frames the face without
    covering it.
  - hanafi-conservative: face covering leaving only the eyes visible
    (niqab-style head covering); the uncovered-face request itself routes to
    REVIEW and this covered variant is the MODIFY offer.
POSE & FRAMING: respectful distance between unrelated figures; no physical
  contact; half-length or wider framing; no close-up beauty portraits and no
  glamour styling of female figures (such framings route to REVIEW under both
  profiles).
STYLE & MEDIUM: <photorealistic / illustration / watercolor / flat vector;
  stated purpose, e.g. wedding album page>.
NEGATIVE BLOCK: no figures other than male or female; no revealing or
  tight-fitting clothing; no swimwear or lingerie contexts; no isolated body
  regions in frame; no beauty-glamour close-ups of female figures; no text
  unless the request specifies it.
```

Worked example (before → after), egypt-dar-alifta profile:

- Before: "Wedding album page: bride in an elegant gown and groom in a suit
  at a courtyard nikkah, warm documentary style."
- After: "SUBJECT: bride and groom seated at a courtyard wedding ceremony,
  female guests and male guests in separate groups. WARDROBE — MALE figures:
  loose opaque suits with full-length trousers. WARDROBE — FEMALE figures:
  hair and neck fully covered by headscarves; loose opaque gowns from neck to
  ankle; face and hands visible. POSE & FRAMING: respectful distance between
  unrelated figures; half-length framing. STYLE & MEDIUM: warm documentary
  wedding photograph. NEGATIVE BLOCK: no tight-fitting clothing; no close-up
  beauty portraits; no text."
