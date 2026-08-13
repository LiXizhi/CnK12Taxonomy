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


def main() -> None:
    dump("math.json", MATH + MATH_REST)
    dump("chinese.json", CHINESE)
    dump("english.json", ENGLISH)
    dump("science.json", SCIENCE)
    dump("it.json", IT)
    n = len(MATH) + len(MATH_REST) + len(CHINESE) + len(ENGLISH) + len(SCIENCE) + len(IT)
    print(f"total topics: {n}")


if __name__ == "__main__":
    main()
