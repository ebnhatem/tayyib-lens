<div align="center">

# TayyibLens

## عدسة الطيّب — TayyibLens

**Pure by design.** Cited fiqh evidence for AI-generated images and audio.

**نقيٌّ بالتصميم** — أدلة شرعية موثَّقة للصور والأصوات المولَّدة بالذكاء الاصطناعي

[English](#english) · [العربية](#العربية)

![CI](https://github.com/ebnhatem/tayyib-lens/actions/workflows/validate.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/code-MIT-blue)
![License: CC BY 4.0](https://img.shields.io/badge/knowledge-CC%20BY%204.0-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

</div>

---

<a name="english"></a>

## English

> **TayyibLens does not tell you what is halal; it shows you what the scholars said,
> where they said it, and where they disagreed.**

### What it is

TayyibLens is an open-source **Agent Skill** ([agentskills.io](https://agentskills.io) open standard)
that screens AI **image and audio generation requests** against a citation-backed corpus of
Islamic legal evidence: the Quran, authenticated hadith, Hanafi fiqh chapters, and
institutional fatwas (Egypt's Dar al-Ifta, IslamWeb, and IIFA Resolution 258 on AI).

Install it in any compliant agent, and every generation request passes through a
documented decision ladder — with a traceable source behind every verdict and a
safer alternative proposed wherever possible.

### What it is — and what it is not

| TayyibLens **is**                                                                        | TayyibLens **is not**                                                         |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| A **lens** — it magnifies published evidence so the agent can apply it                   | A mufti — it never originates a ruling of its own                             |
| An application layer for rulings already issued by qualified scholars                    | An ifta engine (AI-issued fatwas are impermissible — Dar al-Ifta Fatwa 22255) |
| Profile-aware: Hanafi and Egyptian institutional lines coexist, attributed               | A flattener that erases scholarly disagreement into one answer                |
| A redirection engine proposing the safer alternative (silhouette, ambience, calligraphy) | A censor of legitimate khilaf — contested cases route to human review         |
| Fully public: corpus, evidence, tests, and dissent all inspectable                       | A representative of any madhhab or institution                                |

### The decision ladder

Every request exits through one of four verdicts, grounded in the hadith of
doubtful matters (*shubuhat*, Sahih Muslim 1599a): anything short of clear
permissibility drops one enforcement grade.

| Verdict    | Meaning                                              | Example                                                 |
| ---------- | ---------------------------------------------------- | ------------------------------------------------------- |
| **ALLOW**  | Clearly permissible at the applied profile           | nature, architecture, calligraphy, speech, foley        |
| **MODIFY** | Redirected to the safer alternative                  | full figure → faceless silhouette; music → ambience     |
| **REVIEW** | Contested zone — evidence shown, deferred to a human | duff in nasheed contexts; new AI-era questions          |
| **REJECT** | Universal prohibition, non-negotiable                | divine or prophet depiction; deepfake deception; nudity |

### Profiles

| Profile                   | Line                       | Notes                                                          |
| ------------------------- | -------------------------- | -------------------------------------------------------------- |
| `hanafi-conservative`     | Hanafi fiqh                | cautious defaults; prefers leaving what is contested (*wara'*) |
| `egypt-dar-alifta`        | Egyptian institutions      | wider on photography and controlled music; strict on deepfakes |
| `institutional-ai-safety` | IIFA Resolution 258 (3/26) | purpose, benefit, rights, transparency conditions              |

### Evidence discipline

Every rule in `policies/` carries: `source_type`, an exact **locator** (URL + volume/page),
the **illah** (ratio legis), the **disagreement** note, per-profile verdicts, and a
**safe alternative**. No verdict may rest on a single source, a single interpretive layer,
or an extrapolation alone. See [references/evidence-schema.md](references/evidence-schema.md)
and the public source register [CITATION.md](CITATION.md).

```yaml
- rule_id: audio.instrumental_music
  trigger: "request for melodic instrumental accompaniment"
  verdict: MODIFY
  profiles: {hanafi-conservative: REJECT, egypt-dar-alifta: MODIFY}
  evidence:
    - source_type: fatwa
      source_name: "Dar al-Ifta, Fatwa 16964"
      locator: "https://www.dar-alifta.org/ar/fatwa/details/16964"
  safe_alternative: "prompts/audio-safe-rewrite.md#ambience"
```

### Install

<!-- TODO: per-platform install instructions (Claude Code, Codex CLI, Gemini CLI, etc.) -->

```bash
git clone https://github.com/ebnhatem/tayyib-lens.git
```

### Repository structure

```
tayyib-lens/
├── SKILL.md          # skill definition (open Agent Skills standard)
├── profiles/         # fiqh lines: hanafi-conservative, egypt-dar-alifta, ...
├── knowledge/        # evidence cards: quran, hadith, hanafi fiqh, AI-era fatwas
├── policies/         # executable rules (YAML) + universal prohibitions
├── prompts/          # safe-rewrite patterns (image & audio)
├── tests/            # regression cases for every rule
├── references/       # evidence schema, glossary, methodology
└── scripts/          # validation tooling (runs in CI)
```

### Contributing

Scholarly corrections are explicitly welcomed and treated as high-priority correctness
issues. Open an issue:

- **Evidence error** — a citation, takhrij, or attribution is wrong
- **New source proposal** — a published fatwa or classical passage in scope
- **Bug report** — the skill misbehaves at runtime

See [CONTRIBUTING.md](CONTRIBUTING.md). Agents working in this repo read [AGENTS.md](AGENTS.md).

### Disclaimers

- TayyibLens **is not a fatwa engine** and issues no rulings of its own; it applies
  rulings already published by qualified scholars and institutions.
- Contested questions route to **REVIEW** and defer to qualified scholars.
- This project claims no representation of any madhhab or institution.

### License

- Code (`scripts/`): **MIT**
- Knowledge, policies, and prompt files: **CC BY 4.0**

### Acknowledgments

Evidence is drawn from published sources, including
[Dar al-Ifta Egypt](https://www.dar-alifta.org),
[IslamWeb](https://www.islamweb.net),
[IIFA](https://iifa-aifi.org),
[Sunnah.com](https://sunnah.com), and
[Shamela](https://shamela.ws) — may Allah reward its people.

---

<a name="العربية"></a>

## العربية

> **عدسةُ الطيّب لا تُخبرك ما هو الحلال؛ بل تُريك ما قاله العلماء، وأين قالوه، وأين اختلفوا.**

### ما هي عدسة الطيّب؟

عدسة الطيّب مهارةٌ مفتوحة المصدر (**Agent Skill**) وفق المعيار المفتوح
[agentskills.io](https://agentskills.io)، تَفحص طلبات توليد **الصور والأصوات**
بالذكاء الاصطناعي في ضوء أدلةٍ شرعية موثَّقة: القرآن الكريم، والأحاديث الصحيحة
وأبواب الفقه الحنفي، وفتاوى مؤسسية معاصرة (دار الإفتاء المصرية، وإسلام ويب،
وقرار مجمع الفقه الإسلامي الدولي رقم ٢٥٨ بشأن الذكاء الاصطناعي).

تُثبَّت المهارة داخل أي وكيل ذكاء اصطناعي متوافق، فيمرّ كل طلب توليدٍ
بسلَّم قرارٍ موثَّق — خلف كل حُكمٍ فيه مصدرٌ يمكن الرجوع إليه، ومع كل التباسٍ
بديلٌ أسلم يُقترح إن أمكن.

### ما هي — وما ليست

| عدسة الطيّب **هي**                                          | عدسة الطيّب **ليست**                                                    |
| ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| **عدسة** تُكبِّر الأدلة المنشورة ليطبّقها الوكيل            | مُفتيًا يُصدر أحكامًا من عنده                                           |
| طبقةُ تطبيقٍ لفتاوى صدرت عن علماء مؤهَّلين                  | آلةَ إفتاء — فالفتوى بالذكاء الاصطناعي لا تجوز (فتوى دار الإفتاء ٢٢٢٥٥) |
| حافظةٌ للخلاف الفقهي منسوبًا إلى أصحابه                     | مُسطِّحةً تذيب الخلاف في جوابٍ واحد                                     |
| موجِّهةٌ إلى البديل الأسلم عند الالتباس                     | رقيبًا يحكم بين المسلمين                                                |
| علنيةٌ بالكامل: الأدلة والاختبارات والخلاف كلها قابلة للفحص | ممثلةً لأي مذهبٍ أو مؤسسة                                               |

### سلَّم القرار

يخرج كل طلبٍ بإحدى أربع درجات، أساسها حديث الشُّبُهات (صحيح مسلم ١٥٩٩):
ما لم يتّضح إباحتُه يهبط درجةً في التنفيذ.

| الدرجة     | المعنى                                     | مثال                                                          |
| ---------- | ------------------------------------------ | ------------------------------------------------------------- |
| **سماح**   | مباح بوضوح وفق الإطار المختار              | الطبيعة، العمارة، الخط، الكلام، المؤثرات الوظيفية             |
| **تعديل**  | إعادة توجيه إلى البديل الأسلم              | شخص كامل ← ظلّ بلا ملامح؛ موسيقى ← أجواء طبيعية               |
| **مراجعة** | منطقة خلاف — تُعرض الأدلة ويُحال إلى إنسان | الدفّ في بعض سياقات الإنشاد، ونوازل الذكاء الاصطناعي المستجدة |
| **رفض**    | ممنوعٌ لا يُتفاوض عليه                     | تجسيد الذات الإلهية أو الأنبياء، التزييف العميق، العري        |

*(بالمصري وببساطة: العدسة مبتفتيش ومش بتحكم؛ هي بس بتركّزلك الصورة على الدليل —
والقرار في المسائل الملتبسة يرجع لعالمٍ تثق فيه.)*

### الأُطُر الفقهية (Profiles)

| الإطار                    | الخط                | ملاحظات                                                    |
| ------------------------- | ------------------- | ---------------------------------------------------------- |
| `hanafi-conservative`     | الفقه الحنفي        | احتياطي: يُفضَّل ترك المتنازع فيه (الوَرَع)                |
| `egypt-dar-alifta`        | المؤسسات المصرية    | أوسع في التصوير والموسيقى المنضبطة، أشدّ في التزييف العميق |
| `institutional-ai-safety` | قرار مجمع الفقه ٢٥٨ | اشتراط المقصد والمصلحة والحقوق والشفافية                   |

### انضباط التوثيق

كل قاعدةٍ في `policies/` تحمل: نوع المصدر، والموضع الدقيق (رابط + جزء/صفحة)،
والعلّة الشرعية، وموضع الخلاف إن وُجد، والحكم في كل إطار، والبديل الأسلم.
لا يُبنى حكمٌ على مصدرٍ واحد، ولا على طبقة تفسيرية واحدة، ولا على استنباطٍ
مجرد وحده. راجع [references/evidence-schema.md](references/evidence-schema.md)
وسجلّ المصادر العام [CITATION.md](CITATION.md).

### التثبيت

<!-- TODO: تعليمات التثبيت لكل منصة -->

```bash
git clone https://github.com/ebnhatem/tayyib-lens.git
```

### المساهمة

نرحّب بالتصحيحات العلمية ونتعامل معها كأخطاء صحيحة عالية الأولوية.
افتح Issue من نوع: **تصحيح دليل** (خطأ في مصدر أو تخريج)، أو **اقتراح مصدر جديد**،
أو **بلاغ خلل**. التفاصيل في [CONTRIBUTING.md](CONTRIBUTING.md).

### تنبيهات مهمة

- عدسة الطيّب **ليست آلة إفتاء** ولا تُصدر حكمًا من عندها؛ إنها تطبّق فتاوى منشورة
  عن علماء ومؤسسات مؤهَّلة.
- المسائل الخلافية تُحوَّل إلى **مراجعة** وتُعرض على أهل العلم.
- المشروع لا يدّعي تمثيل أي مذهبٍ أو مؤسسة.

### الترخيص

- الكود (`scripts/`): **MIT**
- ملفات المعرفة والقواعد والمطالبات: **CC BY 4.0**

### شكرٌ وتقدير

الأدلة منقولةٌ من مصادر منشورة، منها:
[دار الإفتاء المصرية](https://www.dar-alifta.org)،
[إسلام ويب](https://www.islamweb.net)،
[مجمع الفقه الإسلامي الدولي](https://iifa-aifi.org)،
[Sunnah.com](https://sunnah.com)،
و[المكتبة الشاملة](https://shamela.ws) — جزى الله أهلها خير الجزاء.
