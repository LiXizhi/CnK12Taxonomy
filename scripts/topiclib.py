# -*- coding: utf-8 -*-
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
TYPE = {"C": "CONCEPTUAL", "P": "PROCEDURAL", "R": "REPRESENTATIONAL", "L": "LANGUAGE", "M": "META"}


def xd(g: int) -> int:
    if g <= 2:
        return 1
    if g <= 4:
        return 2
    if g <= 6:
        return 3
    return 4


def T(prefix, subject, slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    stds = std if isinstance(std, list) else [std]
    evidence = [e for e in ev if e]
    if len(evidence) < 2:
        raise SystemExit(f"{slug}: need ≥2 evidence")
    return {
        "id": f"mt_{prefix}_s{xd(g0)}_{slug}",
        "type": TYPE[typ],
        "subject": subject,
        "domain": domain,
        "gradeStart": g0,
        "gradeEnd": g1,
        "name": name,
        "nameEn": en,
        "standards": stds,
        "description": desc,
        "evidence": evidence,
    }


def dump(filename: str, rows: list) -> None:
    path = ROOT / "src" / "topics" / filename
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        seen = set()
        for i in ids:
            if i in seen:
                raise SystemExit(f"duplicate id {i} in {filename}")
            seen.add(i)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{filename}: {len(rows)}")
