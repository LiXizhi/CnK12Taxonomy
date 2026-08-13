# AGENTS.md

## Scope

These instructions apply to the entire repository.

## Repository purpose

This repository contains an original Chinese K12 (grades 1-12) micro-topic taxonomy: compulsory education plus ordinary high school. It includes topic nodes, prerequisite edges, curriculum-standard code mappings, parent-facing clusters, JSON schemas, and a small 3D explorer.

The taxonomy is inspired structurally by Marble's `os-taxonomy`, but its Chinese K12 content is independently authored. Do not copy or translate Marble's topic text.

## Source of truth

- Author taxonomy content in `src/`.
- Treat `data/` as generated output. Do not hand-edit files in `data/` when the corresponding source or build logic can be changed instead.
- Keep schemas in `schema/` synchronized with intentional changes to the generated JSON shape.
- `scripts/build.mjs` expands source catalogs, generates automatic same-domain dependencies and clusters, calculates centrality, and writes `data/manifest.json` checksums.
- `scripts/validate.mjs` validates the built files, including counts, topic fields, references, DAG integrity, standards policy, and checksums.

## Taxonomy authoring rules

- Keep JSON UTF-8 and valid JSON. Preserve the surrounding formatting style and avoid unrelated reformatting.
- Topic IDs must be unique, stable, and start with `mt_`. Follow the existing subject and stage naming pattern.
- Supported topic types are `CONCEPTUAL`, `PROCEDURAL`, `REPRESENTATIONAL`, `LANGUAGE`, and `META`.
- Supported subjects are `语文`, `数学`, `英语`, `科学`, `信息科技`, `道德与法治`, `历史`, `地理`, `体育与健康`, `艺术`, `劳动`, `物理`, `化学`, and `生物学`. 高中思想政治 topics use subject `道德与法治`. 日语/俄语、高中信息技术/通用技术 remain out of scope unless the task explicitly expands validation.
- Write concise, teachable micro-topics rather than broad units. Descriptions and evidence should make mastery observable.
- Give each topic at least two non-empty evidence items and at least one valid standards key.
- Use grades 1-12. Keep `gradeEnd >= gradeStart`; stage (`xueduan`) follows grades 1-2, 3-4, 5-6, 7-9, and 10-12 (高中 = 5).
- Put intentional cross-domain or non-sequential prerequisite edges in `src/dependencies/extra.json`. Every endpoint must exist, self-edges are invalid, and the complete graph must remain acyclic.
- Use `hard` when the prerequisite is required and `soft` when it is useful preparation. Give each explicit edge a short, specific Chinese reason.

## Curriculum and content policy

- Curriculum-standard files contain codes and publicly known domain/theme titles only. Do not add verbatim Ministry of Education curriculum text.
- A standards key has the form `<curriculum-slug>:<code>` and must match an entry in `src/standards/`.
- Preserve source URLs, attribution, provenance, and the `textIncluded`/codes-only policy.
- Do not introduce student records, names, assessment results, or other personal data.
- Preserve the repository's licensing split: database structure and links are ODbL 1.0; authored text is CC BY-SA 4.0; curriculum-standard material is governed by its source and is not relicensed here.

## Working conventions

- Make focused changes and preserve stable public IDs unless a migration is explicitly required.
- Do not overwrite unrelated working-tree changes or generated files created by the user.
- When changing a JSON contract, update source data, build logic, schemas, validation, README examples, and explorer consumers as applicable.
- Keep the explorer dependency-light and consistent with the existing vanilla HTML/CSS/JavaScript implementation.
- Do not add runtime dependencies for tasks that can be handled by the Node.js standard library or existing code.

## Commands

- `npm run validate` validates the current built dataset without regenerating it.
- `npm run build` regenerates `data/` from `src/`.
- `npm run prepare` builds and then validates.
- `npm run explore` serves the repository at `http://localhost:4173/explore/`.

After source-data or build changes, regenerate and validate when the task requires generated artifacts to be updated. For documentation-only or explorer-only changes, use the narrowest relevant check and do not regenerate the taxonomy unnecessarily.

## Review checklist

- Changes were made in the owning source files rather than only in generated output.
- IDs and standards references resolve, and prerequisite direction is `topicId` depends on `prerequisiteId`.
- The dependency graph remains acyclic.
- No verbatim curriculum text or personal data was added.
- Generated files and manifest hashes are updated when required.
- Relevant validation passes, and unrelated files remain untouched.
