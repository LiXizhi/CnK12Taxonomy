#!/usr/bin/env node
/**
 * validate.mjs — dependency-free integrity check for the built dataset.
 *
 * node scripts/validate.mjs
 */
import { createHash } from 'node:crypto';
import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const DATA = resolve(dirname(fileURLToPath(import.meta.url)), '..', 'data');
const load = (name) => JSON.parse(readFileSync(resolve(DATA, name), 'utf8'));
const bytesOf = (name) => readFileSync(resolve(DATA, name));

const errors = [];
const check = (cond, msg) => {
  if (!cond) errors.push(msg);
};

const topics = load('topics.json');
const deps = load('dependencies.json');
const standards = load('curriculum-standards.json');
const clusters = load('clusters.json');
const manifest = load('manifest.json');

check(topics.topicCount === topics.topics.length, `topics: topicCount ${topics.topicCount} != ${topics.topics.length}`);
check(deps.edgeCount === deps.dependencies.length, `dependencies: edgeCount ${deps.edgeCount} != ${deps.dependencies.length}`);
check(standards.curriculumCount === standards.curricula.length, `curricula: curriculumCount != length`);
check(clusters.clusterCount === clusters.clusters.length, `clusters: clusterCount != length`);
check(topics.topics.length >= 1400, `v0.3 target is ≥1400 topics, got ${topics.topics.length}`);
check(deps.dependencies.length >= 2500, `v0.3 target is ≥2500 edges, got ${deps.dependencies.length}`);

const TYPES = new Set(['CONCEPTUAL', 'PROCEDURAL', 'REPRESENTATIONAL', 'LANGUAGE', 'META']);
const SUBJECTS = new Set([
  '语文', '数学', '英语', '科学', '信息科技',
  '道德与法治', '历史', '地理', '体育与健康', '艺术', '劳动',
  '物理', '化学', '生物学',
]);
const topicIds = new Set();
for (const t of topics.topics) {
  check(typeof t.id === 'string' && t.id.startsWith('mt_'), `topic id malformed: ${t.id}`);
  check(TYPES.has(t.type), `topic ${t.id}: bad type ${t.type}`);
  check(SUBJECTS.has(t.subject), `topic ${t.id}: unexpected subject ${t.subject}`);
  check(typeof t.description === 'string' && t.description.length > 12, `topic ${t.id}: empty/short description`);
  check(Array.isArray(t.evidence) && t.evidence.length >= 2, `topic ${t.id}: need ≥2 evidence`);
  check(typeof t.gradeStart === 'number' && t.gradeStart >= 1 && t.gradeStart <= 12, `topic ${t.id}: bad gradeStart`);
  check(t.gradeEnd >= t.gradeStart && t.gradeEnd <= 12, `topic ${t.id}: bad gradeEnd`);
  check(t.xueduan >= 1 && t.xueduan <= 5, `topic ${t.id}: bad xueduan`);
  if (topicIds.has(t.id)) errors.push(`duplicate topic id: ${t.id}`);
  topicIds.add(t.id);
}

const standardKeys = new Set();
const codesOnly = new Set(standards.codesOnlySources ?? []);
for (const c of standards.curricula) {
  const expectFullText = !codesOnly.has(c.slug);
  check(c.textIncluded === expectFullText, `curriculum ${c.slug}: textIncluded ${c.textIncluded} disagrees with codesOnlySources`);
  check(c.topicCount === c.topics.length, `curriculum ${c.slug}: topicCount != length`);
  for (const s of c.topics) {
    check(s.key === `${c.slug}:${s.code}`, `standard key mismatch: ${s.key}`);
    if (standardKeys.has(s.key)) errors.push(`duplicate standard key: ${s.key}`);
    standardKeys.add(s.key);
    if (!expectFullText) check(!('data' in s), `codes-only source ${c.slug} leaks verbatim text at ${s.key}`);
  }
}

for (const d of deps.dependencies) {
  check(topicIds.has(d.topicId), `dependency references unknown topicId ${d.topicId}`);
  check(topicIds.has(d.prerequisiteId), `dependency references unknown prerequisiteId ${d.prerequisiteId}`);
  check(d.topicId !== d.prerequisiteId, `self-dependency on ${d.topicId}`);
  check(d.strength === 'hard' || d.strength === 'soft', `bad strength ${d.strength}`);
}

const adj = new Map();
for (const id of topicIds) adj.set(id, []);
for (const d of deps.dependencies) adj.get(d.prerequisiteId).push(d.topicId);
const visiting = new Set();
const visited = new Set();
const dfs = (n) => {
  if (visiting.has(n)) {
    errors.push(`cycle involving ${n}`);
    return;
  }
  if (visited.has(n)) return;
  visiting.add(n);
  for (const m of adj.get(n) ?? []) dfs(m);
  visiting.delete(n);
  visited.add(n);
};
for (const id of topicIds) dfs(id);

let danglingRefs = 0;
for (const t of topics.topics) {
  check(t.standards.length >= 1, `topic ${t.id}: missing standards`);
  for (const key of t.standards) {
    if (!standardKeys.has(key)) {
      danglingRefs++;
      if (danglingRefs <= 8) errors.push(`topic ${t.id} references unknown standard ${key}`);
    }
  }
}
if (danglingRefs > 8) errors.push(`…and ${danglingRefs - 8} more unknown standard references`);

for (const [name, meta] of Object.entries(manifest.files ?? {})) {
  const actual = createHash('sha256').update(bytesOf(name)).digest('hex');
  check(actual === meta.sha256, `checksum mismatch for ${name}`);
}

if (errors.length) {
  console.error(`✗ ${errors.length} problem(s):`);
  for (const e of errors) console.error(` - ${e}`);
  process.exit(1);
}
console.log(
  `✓ valid — ${topics.topics.length} topics, ${deps.dependencies.length} dependencies, ` +
    `${standardKeys.size} standards, ${clusters.clusters.length} clusters. ` +
    `Referential integrity + DAG + checksums OK.`,
);
