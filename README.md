# Chinese K12 Taxonomy

义务教育 1–9 的开放微主题知识图谱：把「孩子在学什么」拆成可教的微主题，连成先修图，并对齐 2022 课程标准（**只含标准代码，不含课标原文**）。

数据形态对齐 [Marble Skill Taxonomy / os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)，内容为另行撰写的中文义务教育图谱，不是 Marble 英美内容的翻译。

> **Version:** `v0.1.0` · **Topics:** 661 · **Prerequisite edges:** 1,275 · **Clusters:** 93 · **Standard codes:** 182 · **Band:** grades 1–9

本项目**不隶属、不代表**教育部；课标对齐是我们的映射，不是官方产品。

## What this is

- **Micro-topics** — 一个可教的观念或技能（例如「20以内加减」「数据分类」「闭环控制」），含口语化说明、掌握证据、题型（conceptual / procedural / representational / language / meta）、学科+领域、年级与学段。
- **Prerequisite graph** — 有向无环图：`topicId` 依赖于 `prerequisiteId`，边标 `hard`/`soft` 并附一行理由。
- **Curriculum alignment** — 每个微主题链接到 2022 课标模块/领域/任务群的**代码**（见 [PROVENANCE.md](PROVENANCE.md)）。
- **Domain clusters** — 按（学科, 领域, 学段）给家长看的一段话。

v0.1 是**连通骨架**：每个（学科 × 学段 × 领域）都有微主题，粒度粗于 Marble 的小学密度。后续版本会加密（尤其是语文、数学）。

### Subjects in v0.1

| Subject | 学段 | Notes |
|---|---|---|
| 语文 | 1–2 / 3–4 / 5–6 / 7–9 | 六个学习任务群 + 识字写字 |
| 数学 | 1–2 / 3–4 / 5–6 / 7–9 | 数与代数 · 图形与几何 · 统计与概率 · 综合与实践 |
| 英语 | 3–4 / 5–6 / 7–9 | 一级–三级；1–2 年级不单列 |
| 科学 | 1–2 / 3–4 / 5–6 / 7–9 | 四领域；7–9 暂不拆成物理/化学/生物学独立学科 |
| 信息科技 | 1–2 / 3–4 / 5–6 / 7–9 | 九模块；课程方案中独立开设多为 3–8 年级 |

Planned, not authored: 道德与法治, 历史, 地理, 体育与健康, 艺术, 劳动, 普通高中 2017/2020.

## Files

Author in `src/`, build to `data/` (UTF-8 JSON). Schemas in `schema/`. Checksums in `data/manifest.json`.

| File | What it holds |
|---|---|
| `data/topics.json` | Micro-topics (graph **nodes**) |
| `data/dependencies.json` | Prerequisite **edges** |
| `data/curriculum-standards.json` | 2022 课标 codes, grouped by subject |
| `data/clusters.json` | Parent-facing domain summaries |
| `data/manifest.json` | Counts + SHA-256 |

### A topic

```json
{
  "id": "mt_math_s1_count_within_20",
  "type": "CONCEPTUAL",
  "subject": "数学",
  "domain": "数与代数",
  "name": "20以内数的认识",
  "nameEn": "Numbers within 20",
  "description": "能点数、认读并写出20以内的数，知道每个数表示多少个物体。",
  "gradeStart": 1,
  "gradeEnd": 1,
  "xueduan": 1,
  "ageRangeStart": 6,
  "ageRangeEnd": 7,
  "evidence": ["点数不超过20的实物并说出总数", "认读并书写数字0到20"],
  "assessmentPrompt": "请{{name}}示范「20以内数的认识」：能否点数不超过20的实物并说出总数？",
  "standards": ["moe-sx-2022:NA.S1.数与运算"]
}
```

`{{name}}` in `assessmentPrompt` is the child’s name — substitute or strip before display.

### A dependency

```json
{
  "topicId": "mt_math_s1_add_sub_within_20",
  "prerequisiteId": "mt_math_s1_count_within_20",
  "strength": "hard",
  "reason": "同领域递进：先认识20以内的数，再做加减。"
}
```

## Using it

Pure data after build. No runtime dependencies.

```bash
npm run build
npm run validate
```

```js
import topics from './data/topics.json' with { type: 'json' };
import deps from './data/dependencies.json' with { type: 'json' };

const byId = new Map(topics.topics.map((t) => [t.id, t]));
```

## License

| Layer | License |
|---|---|
| **The database** — collection, structure, IDs, topic↔topic and topic↔standard links | [ODbL 1.0](LICENSE) |
| **Authored text** — `description` / `name` / `evidence` / `assessmentPrompt` / edge `reason` / cluster `summary` | [CC BY-SA 4.0](LICENSE-CONTENT) |
| **`curriculum-standards.json`** | **Not ours to relicense.** Codes-only; see [PROVENANCE.md](PROVENANCE.md). |

Produced works (an app, tutor, or model that *uses* the graph) stay yours. Derivative *databases* (extending this taxonomy) must remain open under ODbL.

### Attribution

> Chinese K12 Taxonomy (v0.1) · 义务教育微主题知识图谱 · https://github.com/withmarbleapp/os-taxonomy (schema inspiration) · licensed under ODbL 1.0 (database) and CC BY-SA 4.0 (content).

## What's not here

Semantic embeddings, a visualization app, per-child data, verbatim 课标 text, and high-school 2017/2020 standards.
