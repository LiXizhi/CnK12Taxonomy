#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emit src/topics/*.json from Python catalogs."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from topiclib import dump
from gen_topics import MATH
from catalog_math_rest import MATH_REST
from catalog_chinese import CHINESE
from catalog_english import ENGLISH
from catalog_science import SCIENCE
from catalog_it import IT
from catalog_morality import MORALITY
from catalog_history import HISTORY
from catalog_geography import GEOGRAPHY
from catalog_pe import PE
from catalog_arts import ARTS
from catalog_labor import LABOR


def main() -> None:
    dump("math.json", MATH + MATH_REST)
    dump("chinese.json", CHINESE)
    dump("english.json", ENGLISH)
    dump("science.json", SCIENCE)
    dump("it.json", IT)
    dump("morality.json", MORALITY)
    dump("history.json", HISTORY)
    dump("geography.json", GEOGRAPHY)
    dump("pe.json", PE)
    dump("arts.json", ARTS)
    dump("labor.json", LABOR)
    n = (
        len(MATH) + len(MATH_REST) + len(CHINESE) + len(ENGLISH) + len(SCIENCE) + len(IT)
        + len(MORALITY) + len(HISTORY) + len(GEOGRAPHY) + len(PE) + len(ARTS) + len(LABOR)
    )
    print(f"total topics: {n}")


if __name__ == "__main__":
    main()
