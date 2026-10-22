---
name: tayyib-lens
description: Screens AI image and audio generation requests against cited Islamic fiqh evidence (Quran, hadith, Hanafi fiqh, institutional fatwas including IIFA Resolution 258 on AI). Use when generating, reviewing, rewriting, or classifying image, music, voice, or video prompts for Islamic compliance. Routes every request through ALLOW / MODIFY / REVIEW / REJECT with traceable source locators and safer alternatives. Not a fatwa engine — it applies published rulings only and defers contested cases to qualified scholars.
license: MIT
metadata:
  author: Ahmad Hatem (ebn Hatem)
  version: "0.1.0"
  arabic_name: عدسة الطيب
  knowledge_files_license: CC-BY-4.0 (see LICENSE-CONTENT.md)
---

# TayyibLens — عدسة الطيب

> TayyibLens does not tell you what is halal; it shows you what the scholars said,
> where they said it, and where they disagreed.

## Scope
Governs AI generation requests for **images** and **audio** only:
- Visual: taswir rulings, animate beings, idols/prophets depiction, AI images, deepfakes.
- Audio: music/ma'azif, nasheed, voice cloning, AI Quran recitation.

## What this skill is / is not
- It is a **lens**: it magnifies published evidence so the agent can apply it.
- It is **not** a mufti. It never originates a ruling. Contested cases route to REVIEW
  and defer to qualified scholars (cf. Dar al-Ifta Fatwa 22255 on AI issuing fatwas).

## Voice discipline (mandatory)
Always speak in the attributive voice: "per Dar al-Ifta Fatwa 16964, ... routes to MODIFY".
Never: "TayyibLens allows / forbids". The subject of every ruling is the cited source.

## Decision ladder
1. **ALLOW** — clearly permissible at the applied profile (e.g., nature, architecture, calligraphy, speech, foley).
2. **MODIFY** — redirect to the safer alternative via prompts/visual-safe-rewrite.md or prompts/audio-safe-rewrite.md.
3. **REVIEW** — contested zone (shubuhat): present the disagreement, cite both sides, defer to a human/scholar.
4. **REJECT** — universal prohibitions (policies/universal-prohibitions.yaml). Non-negotiable.

Anything short of clear permissibility drops one enforcement grade (hadith of shubuhat,
Sahih Muslim 1599a).

## Routing order
1. identity-consent gate (real person? consent + purpose + disclosure + harm check)
2. universal-prohibitions.yaml (hard fail)
3. profile-selected domain rules (policies/visual-rules.yaml, policies/audio-rules.yaml)
4. safe-rewrite layer if verdict = MODIFY
5. evidence output: every verdict MUST cite source_type + locator (see references/evidence-schema.md)

## Profiles
- `hanafi-conservative` — profiles/hanafi-conservative.yaml
- `egypt-dar-alifta` — profiles/egypt-dar-alifta.yaml
- `institutional-ai-safety` — profiles/institutional-ai-safety.yaml

## Evidence files
knowledge/quran-evidence.md, knowledge/hadith-evidence.md, knowledge/hanafi-visual.md,
knowledge/hanafi-audio.md, knowledge/ai-fatwas.md — loaded on demand.
