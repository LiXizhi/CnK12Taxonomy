# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "hx", "化学"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

JH_CHEMISTRY = [
    t('jh_chem_lab_safety', 'M', '化学实验', 9, 9, '化学实验安全', 'Lab safety', 'moe-kx-2022:C02.S4', '能识别常见危险化学品标志，遵守加热、闻气味和废弃物处理的基本规范。', '指出酒精灯加热的正确步骤', '说明闻气体气味时为何要扇闻'),
    t('jh_air_composition', 'C', '常见物质', 9, 9, '空气的组成', 'Air composition', 'moe-kx-2022:C01.S4', '知道空气主要成分及氧气、氮气的用途，能设计测定氧气含量的思路。', '说出空气中氧气的体积分数约多少', '解释红磷燃烧测氧实验的原理'),
    t('jh_oxygen_properties', 'C', '常见物质', 9, 9, '氧气的性质与制取', 'Oxygen properties', 'moe-kx-2022:C02.S4', '能描述氧气支持燃烧的性质，并说明实验室制氧的药品和收集方法。', '比较木炭、铁丝在氧气中的燃烧现象', '选择排水法或向上排空气法并说明理由'),
    t('jh_carbon_dioxide', 'C', '常见物质', 9, 9, '二氧化碳', 'Carbon dioxide', 'moe-kx-2022:C02.S4', '能说明二氧化碳与澄清石灰水、燃烧的关系，并完成实验室制取思路。', '解释蜡烛在二氧化碳中熄灭', '写出二氧化碳使石灰水变浑浊的文字表达式'),
    t('jh_water_purification', 'P', '常见物质', 9, 9, '水的净化', 'Water purification', 'moe-kx-2022:C01.S4', '能区分沉淀、过滤、吸附、蒸馏等净化方法及其能除去的杂质。', '画出过滤操作示意图并指出错误', '说明蒸馏水与硬水软化的差别'),
    t('jh_molecule_atom', 'C', '物质构成', 9, 9, '分子与原子', 'Molecules and atoms', 'moe-kx-2022:C01.S4', '能用分子、原子观点解释扩散、物态变化和化学变化中微粒是否改变。', '解释香水味扩散的微粒原因', '说明水电解时分子变原子再重新组合'),
    t('jh_element_and_symbol', 'L', '物质构成', 9, 9, '元素与化学符号', 'Elements and symbols', 'moe-kx-2022:C01.S4', '能读写常见元素符号，区分元素、原子和单质的含义。', '正确书写氧、铁、钠的元素符号', '判断O、O2、H2O中哪些表示元素'),
    t('jh_valence_formula', 'P', '物质构成', 9, 9, '化合价与化学式', 'Valence and formulas', 'moe-kx-2022:C01.S4', '能根据化合价写出简单化合物的化学式，并计算相对分子质量。', '写出氧化铝和水的化学式', '计算二氧化碳的相对分子质量'),
    t('jh_conservation_mass', 'C', '物质构成', 9, 9, '质量守恒定律', 'Mass conservation', 'moe-kx-2022:C02.S4', '理解化学反应前后原子种类、数目和质量不变，能解释表面“质量变化”的原因。', '用微粒观点说明质量守恒', '解释镁条燃烧后固体变重的原因'),
    t('jh_chemical_equation_jh', 'P', '物质构成', 9, 9, '化学方程式书写', 'Writing equations', 'moe-kx-2022:C02.S4', '能书写并配平常见反应的化学方程式，标明反应条件和气体沉淀符号。', '配平氢气还原氧化铜的方程式', '指出未配平方程式错在何处'),
    t('jh_equation_calc', 'P', '物质构成', 9, 9, '化学方程式计算', 'Equation calculations', 'moe-kx-2022:C02.S4', '能根据化学方程式由一种物质质量求另一种物质质量。', '已知碳酸钙质量求生成二氧化碳质量', '检查计算是否先配平再列比例'),
    t('jh_mixture_separation', 'P', '溶液', 9, 9, '混合物的分离', 'Separating mixtures', 'moe-kx-2022:C01.S4', '能根据溶解性、沸点等选择过滤、蒸发、蒸馏等分离方法。', '设计分离沙子和食盐的步骤', '说明蒸发结晶与降温结晶的选用'),
    t('jh_solution_solubility', 'C', '溶液', 9, 9, '溶液与溶解度', 'Solution and solubility', 'moe-kx-2022:C01.S4', '理解饱和溶液与溶解度含义，能读溶解度曲线比较物质溶解能力。', '判断某温度下溶液是否饱和', '从曲线读出某温度的溶解度'),
    t('jh_solute_fraction', 'P', '溶液', 9, 9, '溶质质量分数', 'Mass fraction', 'moe-kx-2022:C01.S4', '能计算溶质质量分数，并完成简单稀释或配制思路。', '计算20g盐溶于80g水的质量分数', '说明加水后质量分数如何变化'),
    t('jh_metal_activity', 'C', '常见物质', 9, 9, '金属活动性', 'Metal activity', 'moe-kx-2022:C02.S4', '能用金属与酸、盐溶液的反应比较活动性强弱，并解释铁的锈蚀防护。', '根据实验排出锌、铁、铜的活动性', '提出防止铁生锈的两种方法'),
    t('jh_acid_alkali_salt', 'C', '酸碱盐', 9, 9, '酸和碱的性质', 'Acids and alkalis', 'moe-kx-2022:C02.S4', '能用酸碱指示剂和pH判断酸碱性，并写出酸与碱、金属氧化物的典型反应。', '用pH试纸测定肥皂水的大致酸碱性', '解释氢氧化钙能改良酸性土壤'),
    t('jh_neutralization', 'P', '酸碱盐', 9, 9, '中和反应', 'Neutralization', 'moe-kx-2022:C02.S4', '理解酸与碱反应生成盐和水，能举出生活中的中和应用。', '写出盐酸与氢氧化钠反应的方程式', '说明服用含氢氧化铝药物缓解胃酸的原理'),
    t('jh_salt_and_fertilizer', 'C', '酸碱盐', 9, 9, '盐与化学肥料', 'Salts and fertilizers', 'moe-kx-2022:C02.S4', '认识常见盐和氮磷钾肥的作用，能判断标签并注意合理施用。', '识别碳酸钠、氯化钠的主要用途', '根据含氮量比较两种氮肥'),
    t('jh_carbon_and_fuels', 'C', '常见物质', 9, 9, '碳和燃料', 'Carbon and fuels', 'moe-kx-2022:C02.S4', '了解碳的单质、一氧化碳还原性和化石燃料燃烧，能讨论完全燃烧与环保。', '比较石墨和金刚石的性质差异', '说明一氧化碳中毒与通风的关系'),
    t('jh_organic_intro', 'C', '常见物质', 9, 9, '有机物入门', 'Organic intro', 'moe-kx-2022:C01.S4', '知道甲烷、乙醇、乙酸等常见有机物的主要用途，能与无机物简单区分。', '写出甲烷燃烧的文字表达式', '举例说明塑料属于有机高分子'),
    t('jh_chem_and_life', 'M', '化学实验', 9, 9, '化学与生活环境', 'Chemistry and life', 'moe-kx-2022:C02.S4', '能从化学视角分析食品添加剂、水质和空气污染，并提出可行的防护建议。', '读食品标签找出一种添加剂并说明作用', '提出减少汽车尾气影响的一项做法'),
    t('jh_inquiry_lab', 'P', '化学实验', 9, 9, '化学探究实验', 'Inquiry lab', 'moe-kx-2022:C02.S4', '能提出假设、控制变量并完成一组对比实验，用现象支持结论。', '设计实验比较两种金属与酸反应快慢', '用表格记录现象并得出结论'),
]
