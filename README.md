# Chinese K12 Taxonomy

义务教育 1–9 与普通高中 10–12 的开放微主题知识图谱：把「孩子在学什么」拆成可教的微主题，连成先修图，并对齐 2022 / 2017–2020 课程标准（**只含标准代码，不含课标原文**）。

数据形态对齐 [Marble Skill Taxonomy / os-taxonomy](https://github.com/withmarbleapp/os-taxonomy)，内容为另行撰写的中文义务教育图谱，不是 Marble 英美内容的翻译。

> **Version:** `v0.3.2` · **Topics:** 1,522 · **Prerequisite edges:** 2,777 · **Clusters:** 242 · **Standard codes:** 338 · **Band:** grades 1–12

本项目**不隶属、不代表**教育部；课标对齐是我们的映射，不是官方产品。

## What this is

- **Micro-topics** — 一个可教的观念或技能（例如「20以内加减」「数据分类」「闭环控制」），含口语化说明、掌握证据、题型（conceptual / procedural / representational / language / meta）、学科+领域、年级与学段。
- **Prerequisite graph** — 有向无环图：`topicId` 依赖于 `prerequisiteId`，边标 `hard`/`soft` 并附一行理由。
- **Curriculum alignment** — 每个微主题链接到 2022 课标模块/领域/任务群的**代码**（见 [PROVENANCE.md](PROVENANCE.md)）。
- **Domain clusters** — 按（学科, 领域, 学段）给家长看的一段话。

v0.3 是**连通骨架**：义务教育 + 普通高中国家课程学科都有微主题，粒度粗于 Marble 的小学密度。后续版本会加密（尤其是语文、数学）。

### Subjects in v0.3

| Subject | 学段 | Notes |
|---|---|---|
| 语文 | 1–12 | 义务六任务群 + 识字写字；高中十二学习任务群 |
| 数学 | 1–12 | 义务四领域；高中预备/函数/几何与代数/概率统计/建模 |
| 英语 | 3–12 | 一级–三级 + 高中语言技能/知识/文化/策略；1–2 不单列 |
| 科学 | 1–9 | 综合科学；7–9 仍保留，并与分科物理/化学互链 |
| 信息科技 | 1–9 | 2022 课标学科（不再使用已过时的「信息技术/通用技术」） |
| 道德与法治 | 1–12 | 义务四主题 + 高中思想政治模块（中国特色社会主义、经济与社会、政治与法治、哲学与文化等）；图谱中与思政合并为一科 |
| 历史 | 7–12 | 初中通史骨架；高中中外历史纲要 + 选必专题 |
| 地理 | 7–12 | 初中区域地理；高中自然/人文 + 区域发展与安全 |
| 体育与健康 | 1–12 | 基本运动 · 体能 · 专项 · 健康 · 体育品德 |
| 艺术 | 1–12 | 音乐 · 美术 · 综合 · 欣赏（2022 综合艺术课 + 2017 高中艺术） |
| 劳动 | 1–2 / 3–4 / 5–6 / 7–9 / 10–12 | 日常生活 · 生产 · 服务性劳动；高中另有创造性劳动（2020 指导纲要） |
| 物理 | 8–12 | 与科学「物质科学」同一纵列先修；初中运动和力/声光/电磁/能量，高中力学电磁等 |
| 化学 | 9–12 | 与科学「物质科学」、物理同一纵列先修；初中物质构成/溶液/酸碱盐，高中反应原理等 |
| 生物学 | 10–12 | 分子与细胞 · 遗传与进化 · 稳态 · 环境 · 生物技术 |

Planned, not authored: 日语/俄语, 初中生物学独立成科。

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
npm run explore   # then open http://localhost:4173/explore/
```

Interactive 3D map (Marble-style): drag to spin, scroll to zoom, tap a dot to walk prerequisites. Subject pills toggle layers. Height is grade; color is subject.

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

> Chinese K12 Taxonomy (v0.3.1) · 义务教育与普通高中微主题知识图谱 · https://github.com/LiXizhi/CnK12Taxonomy · schema inspired by https://github.com/withmarbleapp/os-taxonomy · licensed under ODbL 1.0 (database) and CC BY-SA 4.0 (content).

## What's not here

Semantic embeddings, per-child data, verbatim 课标 text, and 日语/俄语. A local 3D explorer lives in `explore/`.
