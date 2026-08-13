# Changelog

## 0.3.2 — 2026-08-13

- Merge 高中思想政治 into subject `道德与法治` (one civic track, grades 1–12).
- Bridge 科学·物质科学 → 物理/化学 and 科学·生命科学 → 生物学 at stage seams (not a total-order chain).
- Explorer selection expands all prior knowledge (ancestor subgraph) plus direct follow-ups.

## 0.3.1 — 2026-08-13

- Drop outdated high-school 信息技术 / 通用技术 catalogs.
- Add junior-high 物理 (grades 8–9) and 化学 (grade 9) as first-class subjects, aligned to 科学 2022 codes; extras now run 科学 → 初中分科 → 高中。

## 0.3.0 — 2026-08-13

Add ordinary high school (grades 10–12) as 学段 5, aligned to 2017/2020 课标 (codes only).

- Continuing subjects at 高中: 语文, 数学, 英语, 历史, 地理, 体育与健康, 艺术, 劳动.
- New first-class subjects: 思想政治, 物理, 化学, 生物学, 信息技术, 通用技术.
- Junior-high 科学 remains; 物化生 start as separate subjects in 高中, with extras from 科学 7–9.
- 日语/俄语 still out of scope.

## 0.2.0 — 2026-08-13

Add the remaining 2022 义务教育 subjects (codes-only).

- New catalogs: 道德与法治, 历史, 地理, 体育与健康, 艺术, 劳动.
- History and geography are grades 7–9 only (as in the 课程方案).
- Cross-subject extras: 道法↔信息科技/历史/劳动/艺术, 地理↔科学/数学, 体育↔道法, 劳动↔科学.
- Explorer subject pills and colors for all eleven subjects.

## 0.1.0 — 2026-08-13

First public-shape release (local git).

- Schema aligned with Marble os-taxonomy, plus `gradeStart`/`gradeEnd`/`xueduan`/`nameEn`.
- Codes-only alignment to 义务教育课程标准（2022年版） for 语文, 数学, 英语, 科学, 信息科技.
- Connected skeleton of micro-topics and prerequisite edges for grades 1–9.
- No verbatim 课标 text, no embeddings, no per-child data.
