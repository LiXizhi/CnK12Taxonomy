# Provenance & third-party licensing

The micro-topics, the prerequisite graph, and all authored text in this repository
are original work, released under ODbL 1.0 + CC BY-SA 4.0 (see [README](README.md#license)).

**`data/curriculum-standards.json` is different.** Those records are *identifiers*
for modules / domains / 学段 in the 2022 compulsory and 2017/2020 high-school
national curricula. This project does **not** own and **cannot** relicense the
official 课标 text.

## The "codes-only" distinction

We ship only a **standard code** (e.g. `NA.S1.数与运算`) and its key
(`moe-sx-2022:NA.S1.数与运算`) — a short factual identifier — and we **omit**
verbatim 内容要求 / 学业要求 / 教学提示 text. Topic→standard *links* in
`topics.json` are unaffected. Every source is marked `textIncluded: false`.

## Per-source terms

### 🔴 义务教育 2022 `moe-*-2022`

### 🔴 普通高中 2017/2020 `moe-*-2017` and `moe-ld-2020`

- **Publisher / rights:** 中华人民共和国教育部. Official notices: 教材〔2017〕7号; 教材〔2020〕3号 (2017年版2020年修订); 劳动教育指导纲要 教材〔2020〕4号.
- **Source URL:** https://www.moe.gov.cn/srcsite/A26/s8001/202006/t20200603_462199.html
- **劳动纲要:** https://www.moe.gov.cn/srcsite/A26/jcj_kcjcgh/202007/t20200715_472808.html
- **What we ship:** codes + publicly known module / 任务群 / theme *titles* only.

### 🔴 `moe-yw-2022` `moe-sx-2022` `moe-yy-2022` `moe-kx-2022` `moe-xxkj-2022`

- **Publisher / rights:** 中华人民共和国教育部. Official notice: 教材〔2022〕2号.
- **Source URL:** https://www.moe.gov.cn/srcsite/A26/s8001/202204/t20220420_619921.html
- **What we ship:** codes + publicly known module / domain / 任务群 *titles* only.
  Not affiliated with, endorsed by, or a substitute for the official 课程标准.
- **To include full 课标 text:** obtain permission from the rights holder first;
  then regenerate with `textIncluded: true` and a `data` object per standard.

## Schema inspiration

File layout and field names follow [Marble Skill Taxonomy (os-taxonomy)](https://github.com/withmarbleapp/os-taxonomy)
(ODbL 1.0 / CC BY-SA 4.0). This dataset is **not** a fork of Marble's US/UK
content; it is a separately authored Chinese K12 (grades 1–12) graph.
