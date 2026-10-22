# Evidence & rule schema
Every rule in policies/*.yaml requires:
- rule_id, category (visual|audio), trigger
- verdict: ALLOW | MODIFY | REVIEW | REJECT
- profiles: per-profile verdict map
- evidence: list of {source_type, source_name, locator, note}
- illah (the ratio legis), disagreement, safe_alternative
Every evidence card in knowledge/*.md must label its layer:
[TEXT] [TAFSIR] [MADHHAB] [FATWA] [EXTRAPOLATION]
No verdict may be asserted from a single source, a single layer, or an extrapolation alone.
