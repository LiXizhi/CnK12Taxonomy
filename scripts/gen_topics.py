#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expand compact topic tuples into src/topics/*.json."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPE = {
    "C": "CONCEPTUAL",
    "P": "PROCEDURAL",
    "R": "REPRESENTATIONAL",
    "L": "LANGUAGE",
    "M": "META",
}


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
                raise SystemExit(f"duplicate id {i}")
            seen.add(i)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{filename}: {len(rows)}")


# ---------------------------------------------------------------------------
# 数学
# ---------------------------------------------------------------------------
M = "数学"
Pfx = "math"


def m(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, M, slug, typ, domain, g0, g1, name, en, std, desc, *ev)


MATH = [
    # 数与代数 学段1
    m("count_to_10", "C", "数与代数", 1, 1, "10以内数的认识", "Numbers to 10", "moe-sx-2022:NA.S1.数与运算",
      "能把不超过10个物体与数一一对应，理解每个数表示多少，会认读0到10。",
      "点数一堆不超过10的实物并说出总数", "认读数字0到10", "用圆片或手指表示一个10以内的数"),
    m("count_within_20", "C", "数与代数", 1, 1, "20以内数的认识", "Numbers within 20", "moe-sx-2022:NA.S1.数与运算",
      "在10的基础上认识11到20，知道十几是10和几个一，能点数、认读和书写。",
      "把12个物体分成10和2来数", "认读并书写11到20", "在数轴或计数器上指出一个20以内的数"),
    m("compare_within_20", "C", "数与代数", 1, 1, "20以内数的比较", "Comparing numbers within 20", "moe-sx-2022:NA.S1.数与运算",
      "会用多、少、同样多比较20以内两个数，能用大于小于符号记录比较结果。",
      "说出两个20以内数谁更大", "用> < = 连接两个数", "用一一对应说明为什么一个数比另一个多"),
    m("number_bonds_10", "C", "数与代数", 1, 1, "10的组成与分解", "Number bonds to 10", "moe-sx-2022:NA.S1.数与运算",
      "熟练说出10可以分成哪两个数，为凑十法加减做准备。",
      "快速说出和为10的数对", "把10个圆片分成两堆并记录", "根据一部分说出另一部分"),
    m("add_within_10", "P", "数与代数", 1, 1, "10以内加法", "Addition within 10", "moe-sx-2022:NA.S1.数与运算",
      "理解加法是把两部分合起来，能正确计算10以内加法并解释想法。",
      "口算10以内加法", "用实物或图解释一道加法", "看图列出加法算式"),
    m("sub_within_10", "P", "数与代数", 1, 1, "10以内减法", "Subtraction within 10", "moe-sx-2022:NA.S1.数与运算",
      "理解减法是从整体里去掉一部分或求相差，能正确计算10以内减法。",
      "口算10以内减法", "用拿走或比较解释一道减法", "根据情境选择用加法还是减法"),
    m("add_sub_within_20", "P", "数与代数", 1, 1, "20以内进位加法与退位减法", "Add and subtract within 20", "moe-sx-2022:NA.S1.数与运算",
      "会用凑十、破十等方法计算20以内进位加法和退位减法，追求熟练。",
      "正确计算如9+7、15-8", "说出自己用的凑十或破十步骤", "在一分钟内完成一组20以内加减"),
    m("add_sub_stories", "P", "数与代数", 1, 1, "用加减解决简单实际问题", "Add/subtract story problems", "moe-sx-2022:NA.S1.数量关系",
      "能从把两部分合并、去掉、比较等生活情境中列出加减算式并求解。",
      "听故事列出加减算式", "说明算式中每个数表示什么", "检验得数是否符合情境"),
    m("count_within_100", "C", "数与代数", 1, 2, "100以内数的认识", "Numbers within 100", "moe-sx-2022:NA.S1.数与运算",
      "认识100以内各数，能读、写、数，知道几个十和几个一。",
      "读出并写出一个两位数", "从任意数接着数到100", "用小棒表示34是3捆加4根"),
    m("place_value_tens_ones", "R", "数与代数", 1, 2, "十位与个位", "Tens and ones", "moe-sx-2022:NA.S1.数与运算",
      "理解两位数中数字所在数位决定它表示几个十或几个一。",
      "说出52里的5表示5个十", "交换52的两个数字并比较大小", "在计数器上拨出一个两位数"),
    m("skip_count_2_5_10", "P", "数与代数", 2, 2, "按2、5、10跳着数", "Skip counting by 2, 5, 10", "moe-sx-2022:NA.S1.数与运算",
      "能按2、5、10的间隔往下数，为乘法和钱币计数做准备。",
      "从0开始按5数到50", "按2数一排鞋子或手套", "用10元一张数出80元"),
    m("even_odd", "C", "数与代数", 2, 2, "奇数与偶数", "Odd and even numbers", "moe-sx-2022:NA.S1.数与运算",
      "能把数分成一对对，理解偶数能两两配对、奇数会剩一个。",
      "判断20以内一个数是奇是偶", "用配对图说明为什么7是奇数", "说出一个偶数后面的奇数"),
    m("add_within_100", "P", "数与代数", 2, 2, "100以内加法", "Addition within 100", "moe-sx-2022:NA.S1.数与运算",
      "会口算和笔算100以内加法，包括进位，能解释满十进一。",
      "计算36+27并说明进位", "口算整十数加两位数", "检查得数是否合理"),
    m("sub_within_100", "P", "数与代数", 2, 2, "100以内减法", "Subtraction within 100", "moe-sx-2022:NA.S1.数与运算",
      "会口算和笔算100以内减法，包括退位，能解释退一作十。",
      "计算52-18并说明退位", "口算整十数减两位数", "用加法验算减法"),
    m("compare_within_100", "C", "数与代数", 2, 2, "100以内数的大小比较", "Compare numbers within 100", "moe-sx-2022:NA.S1.数与运算",
      "先看十位再看个位比较两个两位数，能在数线上标出它们的位置。",
      "比较47和74并说明理由", "把五个两位数从小到大排列", "在百数表里找出相邻的数"),
    m("length_compare_add", "P", "数与代数", 2, 2, "与长度有关的加减", "Add/subtract lengths", "moe-sx-2022:NA.S1.数量关系",
      "能把线段或物体长度的和差写成加减算式，体会数量关系在测量中的用处。",
      "求两根绳子接起来有多长", "已知全长和一段求另一段", "选用合适单位记录得数"),
    m("repeated_add_preview", "C", "数与代数", 2, 2, "相同加数连加", "Repeated addition", "moe-sx-2022:NA.S1.数量关系",
      "把几个相同的数连加，体会乘法的雏形，能用图画表示。",
      "把3+3+3+3写成连加并求值", "画4个盘子每盘2个苹果并列式", "说出连加表示几个几"),
    m("estimate_within_100", "M", "数与代数", 2, 2, "100以内估算", "Estimating within 100", "moe-sx-2022:NA.S1.数与运算",
      "能把数看成接近的整十数来估计和差，判断计算结果是否合理。",
      "估计38+21大约是几十", "发现明显算错的得数", "说明自己估的是估多了还是估少了"),
    # 图形与几何 学段1
    m("shape_names_2d", "C", "图形与几何", 1, 1, "常见平面图形的辨认", "Recognizing 2D shapes", "moe-sx-2022:GG.S1.图形的认识与测量",
      "能从物体表面辨认长方形、正方形、三角形、圆，说出它们的名字。",
      "给平面图形正确命名", "从实物表面指出一种图形", "在一组图形中找出指定形状"),
    m("shape_names_3d", "C", "图形与几何", 1, 2, "长方体、正方体、圆柱、球", "Common 3D shapes", "moe-sx-2022:GG.S1.图形的认识与测量",
      "能辨认长方体、正方体、圆柱和球，描述它们能不能滚动、有没有平的面。",
      "给立体图形正确命名", "说出球和立方体在滚动上的不同", "按形状给学具分类"),
    m("compare_length", "P", "图形与几何", 1, 1, "比长短", "Comparing lengths", "moe-sx-2022:GG.S1.图形的认识与测量",
      "会把物体一端对齐再比较长短，知道比较要有共同起点。",
      "判断两支笔谁更长", "用一端对齐的方法比较", "发现起点不齐时比较会出错"),
    m("nonstandard_length", "P", "图形与几何", 1, 2, "用非标准单位量长度", "Non-standard length units", "moe-sx-2022:GG.S1.图形的认识与测量",
      "用回形针、手掌等同样长的单位去量物体，体会单位要统一。",
      "用回形针量课桌边大约几枚", "解释为什么单位不同结果不同", "首尾相接摆放单位、不留缝"),
    m("centimetre", "C", "图形与几何", 2, 2, "认识厘米", "The centimetre", "moe-sx-2022:GG.S1.图形的认识与测量",
      "认识厘米是常用长度单位，会用直尺量整厘米长度。",
      "在直尺上指出1厘米", "量出一支铅笔大约几厘米", "估计橡皮长度并用尺验证"),
    m("metre", "C", "图形与几何", 2, 2, "认识米", "The metre", "moe-sx-2022:GG.S1.图形的认识与测量",
      "知道1米=100厘米，能判断什么场合用米、什么场合用厘米。",
      "说出1米等于100厘米", "选择量教室长度该用米还是厘米", "用米尺量一步大约多长"),
    m("clock_hour_half", "R", "图形与几何", 1, 2, "整时与半时", "Hours and half hours", "moe-sx-2022:GG.S1.图形的认识与测量",
      "会看钟面的整时和半时，把时刻与日常作息对应起来。",
      "读出钟面上的8时、8时半", "拨出指定的整时或半时", "说出自己上学大概是几点"),
    m("position_above_beside", "C", "图形与几何", 1, 1, "上下前后左右", "Above, in front, left and right", "moe-sx-2022:GG.S1.图形的认识与测量",
      "能用上、下、前、后、左、右描述物体位置，分清自己的左和右。",
      "按指令把物品放在盒子左边", "描述同桌在自己的哪一侧", "在简单地图上指出上下"),
    m("compose_shapes", "P", "图形与几何", 2, 2, "用简单图形拼组", "Composing shapes", "moe-sx-2022:GG.S1.图形的认识与测量",
      "能用几个三角形或长方形拼出新图形，体会图形可以组合与分解。",
      "用两个三角形拼成一个长方形", "说出一个图形是由哪些小图形组成的", "把一个图形沿线剪开再拼回"),
    m("pattern_shape_color", "R", "图形与几何", 1, 2, "图形与颜色的简单规律", "Shape and color patterns", "moe-sx-2022:GG.S1.图形的认识与测量",
      "能发现并续编按形状或颜色重复出现的规律。",
      "说出下一个该是什么图形", "自己设计一种红蓝交替规律", "找出打乱规律的那一项"),
    # 统计与概率 学段1
    m("sort_by_attribute", "P", "统计与概率", 1, 1, "按一个标准分类", "Sorting by one attribute", "moe-sx-2022:SP.S1.数据分类",
      "能按颜色、形状或大小把一组物品分成几类，并说明分类标准。",
      "按颜色把积木分开", "说出自己用的分类标准", "发现同组物品还可以按别的标准再分"),
    m("tally_count", "P", "统计与概率", 1, 2, "用正字或点子计数", "Tally marks", "moe-sx-2022:SP.S1.数据分类",
      "会用正字或点子记录每一类有多少，避免漏数和重数。",
      "用正字记录小组里喜欢苹果的人数", "把正字换成数字", "检查记录是否与实物一致"),
    m("pictograph_read", "R", "统计与概率", 2, 2, "读简单象形统计图", "Reading pictographs", "moe-sx-2022:SP.S1.数据分类",
      "能从一符一物的象形图中读出各类数量，并进行简单比较。",
      "从图中读出最多的一类", "说出两类相差几个", "根据图回答谁最少"),
    m("ask_and_record", "P", "统计与概率", 2, 2, "问一问并记录结果", "Ask and record", "moe-sx-2022:SP.S1.数据分类",
      "会向同学问一个简单问题并把答案记下来，形成一小份分类数据。",
      "调查同桌最喜欢的季节并记录", "把记录整理成各类数量", "用一句话描述调查结果"),
    m("same_different_groups", "C", "统计与概率", 1, 2, "同样多与不一样多", "Equal and unequal groups", "moe-sx-2022:SP.S1.数据分类",
      "能判断两类物品是不是同样多，体会分类后比较数量。",
      "判断两组圆片是否同样多", "用一一对应说明差几个", "把多的一类拿掉一些变成同样多"),
    # 综合与实践 学段1
    m("math_in_classroom", "M", "综合与实践", 1, 1, "教室里的数学", "Math in the classroom", "moe-sx-2022:PA.S1.综合与实践",
      "能在教室里找出可以数、可以比长短的事物，用刚学的数和比较去描述。",
      "数出一组课桌有几张", "比较两支铅笔长短", "用一句话说教室里的一个数量"),
    m("make_a_20_book", "P", "综合与实践", 1, 1, "做一本20以内的数书", "Make a numbers-to-20 book", "moe-sx-2022:PA.S1.综合与实践",
      "为每一个20以内的数收集图画或实物照片，展示数与数量的对应。",
      "为某个数找到对应数量的图", "按顺序排列自己的数页", "向同伴介绍其中一页"),
    m("measure_our_things", "P", "综合与实践", 2, 2, "量一量我们的物品", "Measure our things", "moe-sx-2022:PA.S1.综合与实践",
      "选几件学习用品用厘米量一量，做一张简单的长度记录表。",
      "正确用尺量一件物品", "把结果记在表里", "比较哪件物品最长"),
    m("survey_favorite", "P", "综合与实践", 2, 2, "最喜欢的…小调查", "Favorite-item mini survey", "moe-sx-2022:PA.S1.综合与实践",
      "在小组里调查一个喜好问题，分类计数并用象形图展示。",
      "提出一个能分类的问题", "记录每个人的选择", "画出简单象形图并介绍"),
]
