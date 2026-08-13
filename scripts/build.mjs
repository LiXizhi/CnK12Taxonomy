#!/usr/bin/env node
/**
 * build.mjs — expand src/ catalogs into data/*.json and write SHA-256 manifest.
 *
 * node scripts/build.mjs
 */
import { createHash } from 'node:crypto';
import { mkdirSync, readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const SRC = join(ROOT, 'src');
const DATA = join(ROOT, 'data');
const VERSION = '0.2.0';

const loadJson = (path) => JSON.parse(readFileSync(path, 'utf8'));
const listJson = (dir) =>
  readdirSync(dir)
    .filter((f) => f.endsWith('.json'))
    .sort()
    .map((f) => join(dir, f));

const xueduanOf = (grade) => {
  if (grade <= 2) return 1;
  if (grade <= 4) return 2;
  if (grade <= 6) return 3;
  return 4;
};

const expandTopic = (raw) => {
  const gradeStart = raw.gradeStart;
  const gradeEnd = raw.gradeEnd ?? raw.gradeStart;
  const xueduan = raw.xueduan ?? xueduanOf(gradeStart);
  const evidence = raw.evidence.filter(Boolean);
  const name = raw.name;
  const assessmentPrompt =
    raw.assessmentPrompt ??
    `请{{name}}示范「${name}」：能否${evidence[0] ?? '独立完成'}？再请 ta 用自己的话讲讲为什么可以这样做。`;
  return {
    id: raw.id,
    type: raw.type,
    subject: raw.subject,
    domain: raw.domain ?? null,
    name,
    nameEn: raw.nameEn ?? null,
    description: raw.description,
    gradeStart,
    gradeEnd,
    xueduan,
    ageRangeStart: raw.ageRangeStart ?? gradeStart + 5,
    ageRangeEnd: raw.ageRangeEnd ?? gradeEnd + 6,
    centrality: raw.centrality ?? null,
    evidence,
    assessmentPrompt,
    standards: raw.standards ?? [],
  };
};

const topicFiles = listJson(join(SRC, 'topics'));
const topics = topicFiles.flatMap((p) => loadJson(p)).map(expandTopic);

const byId = new Map();
for (const t of topics) {
  if (byId.has(t.id)) throw new Error(`duplicate topic id: ${t.id}`);
  byId.set(t.id, t);
}

const extraDeps = listJson(join(SRC, 'dependencies')).flatMap((p) => loadJson(p));

const autoDeps = [];
const groups = new Map();
for (const t of topics) {
  const key = `${t.subject}::${t.domain ?? ''}`;
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key).push(t);
}
for (const arr of groups.values()) {
  arr.sort((a, b) => a.gradeStart - b.gradeStart || a.gradeEnd - b.gradeEnd || a.id.localeCompare(b.id));
  for (let i = 1; i < arr.length; i++) {
    const cur = arr[i];
    const add = (prev, strength, reason) => {
      autoDeps.push({
        topicId: cur.id,
        prerequisiteId: prev.id,
        strength,
        reason,
      });
    };
    const prev = arr[i - 1];
    if (cur.gradeStart >= prev.gradeStart) {
      add(
        prev,
        cur.gradeStart > prev.gradeEnd ? 'hard' : 'soft',
        cur.gradeStart > prev.gradeEnd
          ? `同领域递进：先掌握「${prev.name}」，再学习「${cur.name}」。`
          : `同领域相邻微主题：「${prev.name}」为「${cur.name}」提供准备。`,
      );
    }
    if (i >= 2) {
      const skip = arr[i - 2];
      add(skip, 'soft', `同领域隔项准备：「${skip.name}」支撑「${cur.name}」。`);
    }
  }
}

const seen = new Set();
const dependencies = [];
for (const d of [...extraDeps, ...autoDeps]) {
  const k = `${d.topicId}|${d.prerequisiteId}`;
  const reverse = `${d.prerequisiteId}|${d.topicId}`;
  if (seen.has(k) || seen.has(reverse)) continue;
  if (d.topicId === d.prerequisiteId) continue;
  if (!byId.has(d.topicId) || !byId.has(d.prerequisiteId)) {
    throw new Error(`unknown endpoint in dependency ${k}`);
  }
  seen.add(k);
  dependencies.push({
    topicId: d.topicId,
    prerequisiteId: d.prerequisiteId,
    strength: d.strength,
    reason: d.reason ?? null,
  });
}

// degree centrality in [0,1]
const degree = new Map(topics.map((t) => [t.id, 0]));
for (const d of dependencies) {
  degree.set(d.topicId, degree.get(d.topicId) + 1);
  degree.set(d.prerequisiteId, degree.get(d.prerequisiteId) + 1);
}
const maxDeg = Math.max(1, ...degree.values());
for (const t of topics) t.centrality = Math.round((degree.get(t.id) / maxDeg) * 1000) / 1000;

const standardFiles = listJson(join(SRC, 'standards'));
const curricula = standardFiles.map((p) => {
  const c = loadJson(p);
  return { ...c, topicCount: c.topics.length };
});

const XUEDUAN_LABEL = { 1: '一二年级', 2: '三四年级', 3: '五六年级', 4: '七至九年级' };
const clusterMap = new Map();
for (const t of topics) {
  const key = `${t.subject}::${t.domain}::${t.xueduan}`;
  if (!clusterMap.has(key)) {
    clusterMap.set(key, {
      subject: t.subject,
      domain: t.domain,
      xueduan: t.xueduan,
      gradeStart: t.gradeStart,
      gradeEnd: t.gradeEnd,
      ageRangeStart: t.ageRangeStart,
      ageRangeEnd: t.ageRangeEnd,
      names: [],
    });
  }
  const c = clusterMap.get(key);
  c.gradeStart = Math.min(c.gradeStart, t.gradeStart);
  c.gradeEnd = Math.max(c.gradeEnd, t.gradeEnd);
  c.ageRangeStart = Math.min(c.ageRangeStart, t.ageRangeStart);
  c.ageRangeEnd = Math.max(c.ageRangeEnd, t.ageRangeEnd);
  c.names.push(t.name);
}
const clusters = [...clusterMap.values()].map((c) => {
  const sample = c.names.slice(0, 6).join('、');
  const extra = c.names.length > 6 ? `等共 ${c.names.length} 个微主题` : `（${c.names.length} 个微主题）`;
  return {
    subject: c.subject,
    domain: c.domain,
    xueduan: c.xueduan,
    gradeStart: c.gradeStart,
    gradeEnd: c.gradeEnd,
    ageRangeStart: c.ageRangeStart,
    ageRangeEnd: c.ageRangeEnd,
    summary: `${c.subject}·${c.domain}在${XUEDUAN_LABEL[c.xueduan] ?? '本学段'}（${c.gradeStart}–${c.gradeEnd} 年级）覆盖：${sample}${extra}。这是义务教育 2022 课标对应领域的可教微主题，便于家长看懂孩子正在学什么、下一步学什么。`,
  };
});

mkdirSync(DATA, { recursive: true });

const out = {
  'topics.json': {
    version: VERSION,
    topicCount: topics.length,
    topics,
  },
  'dependencies.json': {
    version: VERSION,
    note: 'topicId depends on prerequisiteId. Auto-wired within (subject, domain) by grade, plus src/dependencies extras.',
    edgeCount: dependencies.length,
    dependencies,
  },
  'curriculum-standards.json': {
    note: 'Codes and publicly known module titles only. Verbatim 课标 text is not included.',
    codesOnlySources: curricula.map((c) => c.slug),
    curriculumCount: curricula.length,
    curricula,
  },
  'clusters.json': {
    version: VERSION,
    clusterCount: clusters.length,
    clusters,
  },
};

const files = {};
for (const [name, obj] of Object.entries(out)) {
  const json = `${JSON.stringify(obj, null, 2)}\n`;
  writeFileSync(join(DATA, name), json);
  files[name] = {
    bytes: Buffer.byteLength(json),
    sha256: createHash('sha256').update(json).digest('hex'),
  };
}

const subjectCounts = {};
for (const t of topics) subjectCounts[t.subject] = (subjectCounts[t.subject] ?? 0) + 1;

const manifest = {
  version: VERSION,
  generated: '2026-08-13',
  topicCount: topics.length,
  edgeCount: dependencies.length,
  clusterCount: clusters.length,
  standardCount: curricula.reduce((n, c) => n + c.topics.length, 0),
  subjects: subjectCounts,
  files,
};
writeFileSync(join(DATA, 'manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`);

console.log(
  `built v${VERSION}: ${topics.length} topics, ${dependencies.length} edges, ${clusters.length} clusters, ${manifest.standardCount} standard codes.`,
);
