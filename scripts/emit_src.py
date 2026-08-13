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
from catalog_hs_math import HS_MATH
from catalog_hs_chinese import HS_CHINESE
from catalog_hs_english import HS_ENGLISH
from catalog_hs_politics import HS_POLITICS
from catalog_hs_history import HS_HISTORY
from catalog_hs_geography import HS_GEOGRAPHY
from catalog_hs_physics import HS_PHYSICS
from catalog_hs_chemistry import HS_CHEMISTRY
from catalog_hs_biology import HS_BIOLOGY
from catalog_jh_physics import JH_PHYSICS
from catalog_jh_chemistry import JH_CHEMISTRY
from catalog_hs_pe import HS_PE
from catalog_hs_arts import HS_ARTS
from catalog_hs_labor import HS_LABOR


def main() -> None:
    dump("math.json", MATH + MATH_REST + HS_MATH)
    dump("chinese.json", CHINESE + HS_CHINESE)
    dump("english.json", ENGLISH + HS_ENGLISH)
    dump("science.json", SCIENCE)
    dump("it.json", IT)
    dump("morality.json", MORALITY)
    dump("history.json", HISTORY + HS_HISTORY)
    dump("geography.json", GEOGRAPHY + HS_GEOGRAPHY)
    dump("pe.json", PE + HS_PE)
    dump("arts.json", ARTS + HS_ARTS)
    dump("labor.json", LABOR + HS_LABOR)
    dump("politics.json", HS_POLITICS)
    dump("physics.json", JH_PHYSICS + HS_PHYSICS)
    dump("chemistry.json", JH_CHEMISTRY + HS_CHEMISTRY)
    dump("biology.json", HS_BIOLOGY)
    n = (
        len(MATH) + len(MATH_REST) + len(CHINESE) + len(ENGLISH) + len(SCIENCE) + len(IT)
        + len(MORALITY) + len(HISTORY) + len(GEOGRAPHY) + len(PE) + len(ARTS) + len(LABOR)
        + len(HS_MATH) + len(HS_CHINESE) + len(HS_ENGLISH) + len(HS_POLITICS)
        + len(HS_HISTORY) + len(HS_GEOGRAPHY) + len(HS_PHYSICS) + len(HS_CHEMISTRY)
        + len(HS_BIOLOGY) + len(JH_PHYSICS) + len(JH_CHEMISTRY) + len(HS_PE)
        + len(HS_ARTS) + len(HS_LABOR)
    )
    print(f"total topics: {n}")


if __name__ == "__main__":
    main()
