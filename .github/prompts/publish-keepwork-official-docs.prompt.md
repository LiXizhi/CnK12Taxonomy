---
name: "Publish Keepwork Official Docs"
description: "Publish this repository's explore/ and data/ directories to the Keepwork CDN, the official/docs Keepwork raw site, or both."
agent: "agent"
---

Publish this repository's `explore/` and `data/` directories under `official/docs/CnK12Taxonomy/`.

Requirements:

- Before doing anything else, ask the user to select exactly one deployment target with these options:
  - `CDN` - publish to `https://cdn.keepwork.com/official/docs/CnK12Taxonomy/`
  - `Keepwork raw` - publish to `https://keepwork.com/api/raw/official/docs/CnK12Taxonomy/`
  - `Both` - publish to both destinations
- Use a fixed-choice question when the question tool is available. Do not ask for a project name or remote path.
- Work from this repository root. Confirm `explore/` and `data/` exist before uploading.
- Do not run a taxonomy build and do not modify either directory. Upload the current files exactly as they exist.
- Execute only the selected workflow. For `Both`, complete and verify both workflows independently.

## CDN workflow

- Use the `upload-deploy-cdn-files` skill from `C:/lxzsrc/keepworkSDK/.github/skills/upload-deploy-cdn-files/SKILL.md` and follow its credential, dependency, upload, and cache-refresh workflow.
- Upload both directories in one command with remote prefix `official/docs/CnK12Taxonomy/`, preserving these object paths:
  - `official/docs/CnK12Taxonomy/explore/...`
  - `official/docs/CnK12Taxonomy/data/...`
- Prefer the skill's Python uploader. On Windows PowerShell, run:

  `python C:/lxzsrc/keepworkSDK/.github/skills/upload-deploy-cdn-files/qiniu_upload_local_files.py --prefix "official/docs/CnK12Taxonomy/" explore data`

- If the Python environment is unavailable, use the Node fallback documented by the skill from the keepworkSDK repository, without building either repository.
- Read the complete uploader output and fail the task if any file fails, either local directory is skipped, credentials are missing, or cache refresh fails.
- Verify that `https://cdn.keepwork.com/official/docs/CnK12Taxonomy/explore/index.html` is reachable after upload.

## Keepwork raw workflow

- Use the `keepwork-copilot` skill from `C:/lxzsrc/keepworkSDK/.github/skills/keepwork-copilot/SKILL.md` and follow its authentication, dry-run, exact-URL approval, publishing, and failure-handling rules.
- Treat `official/docs` as the Keepwork site. Publish the directories separately with these mappings:
  - local `explore/` to remote `CnK12Taxonomy/explore/`
  - local `data/` to remote `CnK12Taxonomy/data/`
- Use the skill CLI at `C:/lxzsrc/keepworkSDK/.github/skills/keepwork-copilot/scripts/keepwork-copilot.mjs`.
- Run both publishes with `--dry-run` first. Show the exact final URLs and obtain the approval required by the skill before rerunning with matching `--confirm-url` values.
- Do not use `--auto-create-site`; `official/docs` is an existing official site.
- After both publishes succeed, verify these raw URLs are reachable and return the expected file content:
  - `https://keepwork.com/api/raw/official/docs/CnK12Taxonomy/explore/index.html`
  - `https://keepwork.com/api/raw/official/docs/CnK12Taxonomy/data/manifest.json`

Report which target or targets were selected, whether each verification succeeded, and any failed or skipped files. Do not expose passwords, access keys, secret keys, or tokens.