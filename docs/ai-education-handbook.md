# 13 K12 微主题图谱：课程组织与接入

本文由 AI 根据第二大脑资料与 Git 源码整理。核对日期：2026-09-17。代码基线：`CnK12Taxonomy` / `master` / `93a40daff42e`。这是源码快照说明；未据此宣称生产环境已完成全部验收。

## 用途

把课程目标分成可教微主题，以先修关系组织学习路径，服务课程规划与 AI 教师材料检索。[在线图谱](https://keepwork.com/api/raw/official/docs/CnK12Taxonomy/explore/index.html)。它是自建的课标映射数据，不是教育部官方产品，也不替代学生实际掌握证据。

## 使用方法

1. 选择显示到的年级与学科，搜索知识点。
2. 点击主题查看内容与先修关系；沿“必须先会什么”回查前置知识。
3. 用主题目标、掌握证据和关联标准代码设计活动与练习。
4. 学习评估来自实际答题/作品，不能从图谱节点存在直接推断学生掌握。

## 数据合同

当前 manifest v0.3.2：1,522 个主题、2,777 条先修边、242 个簇、338 个标准代码。截图默认过滤到初三，显示的是子集计数，不能与完整 manifest 直接比较。

`topics.json` 是节点，`dependencies.json` 是边，`clusters.json` 是概括，`curriculum-standards.json` 是标准代码映射。边的方向为 topicId 依赖 prerequisiteId，区分 hard/soft。

## 构建与维护

```text
src/ 作者内容 + dependencies/extra.json
 → scripts/build.mjs → data/ + manifest 校验和
 → scripts/validate.mjs（字段、引用、DAG、数量、标准代码）
 → explore/ 展示与下游课程工具
```

修改源内容而非直接改生成 data。新主题使用稳定 ID，保持依赖无环；课标只保留允许的代码与标题，不加入整篇原文。数据、原创文字和标准来源各有许可边界，复用时保留 PROVENANCE 与 LICENSE。

本轮读取 manifest 与构建/验证入口，没有重新生成数据。图谱页面已实际加载；未把图谱覆盖度等同于课程完整度。

## 源码与维护入口

- [`data/manifest.json`](https://github.com/LiXizhi/CnK12Taxonomy/blob/93a40daff42e6e05c2da65a92ef6775b8dcf04c0/data/manifest.json)
- [`schema/topics.schema.json`](https://github.com/LiXizhi/CnK12Taxonomy/blob/93a40daff42e6e05c2da65a92ef6775b8dcf04c0/schema/topics.schema.json)
- [`scripts/build.mjs`](https://github.com/LiXizhi/CnK12Taxonomy/blob/93a40daff42e6e05c2da65a92ef6775b8dcf04c0/scripts/build.mjs)
- [`scripts/validate.mjs`](https://github.com/LiXizhi/CnK12Taxonomy/blob/93a40daff42e6e05c2da65a92ef6775b8dcf04c0/scripts/validate.mjs)
- [`README.md`](https://github.com/LiXizhi/CnK12Taxonomy/blob/93a40daff42e6e05c2da65a92ef6775b8dcf04c0/README.md)

## 实际界面截图

附图为 2026-09-17 浏览器实际页面；只证明所示界面状态。

## 钉钉发布版本

[国基知识库中的本篇手册](https://alidocs.dingtalk.com/i/nodes/ndMj49yWj2jpxr2gHbXb4weDW3pmz5aA)（2026-09-17）。截图保存在钉钉原文中；后续更新本文件后同步原文档。
