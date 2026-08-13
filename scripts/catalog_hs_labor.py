# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "ld", "劳动"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_LABOR = [
    t('hs_independent_living', 'P', '高中日常生活劳动', 10, 12, '独立生活管理', 'Independent living management', 'moe-ld-2020:DL', '能自主安排洗衣、清洁、作息与物品收纳，维持寝室或家庭责任区在一周内有序运转。', '连续一周完成个人内务并自检', '制定并执行一份日常家务轮值表'),
    t('hs_home_bookkeeping', 'P', '高中日常生活劳动', 10, 12, '家庭财务记账', 'Household bookkeeping', 'moe-ld-2020:DL', '能分类记录收入与支出，区分必要消费与可选消费，并做月末小结与下月预算。', '完成一个月的分类记账表', '根据超支项提出一条调整建议'),
    t('hs_healthy_meal_plan', 'P', '高中日常生活劳动', 10, 12, '健康饮食规划', 'Healthy meal planning', 'moe-ld-2020:DL', '能按营养均衡与预算规划三日餐单，完成采购清单并在监护下实施一餐制作。', '提交含蔬果与蛋白质的三日餐单', '按清单采购并完成一餐后清理'),
    t('hs_campus_grow_raise', 'P', '高中生产劳动', 10, 12, '校园种植或养殖项目', 'Campus growing or raising project', 'moe-ld-2020:PL', '能承担一项种植或小动物照料的周期任务，记录环境、生长与问题处理，并估算产出。', '完成四周养护日志', '收获或称重后说明影响产量的因素'),
    t('hs_traditional_craft_make', 'P', '高中生产劳动', 10, 12, '传统工艺制作', 'Traditional craft production', 'moe-ld-2020:PL', '能按传统工序完成一件可用手工艺品，说明材料来源、工具安全与质量检验标准。', '完成一件符合尺寸要求的工艺品', '列出三步关键工序与检验点'),
    t('hs_modern_agri_cognition', 'C', '高中生产劳动', 10, 12, '现代农业认知', 'Modern agriculture cognition', 'moe-ld-2020:PL', '能说明温室、滴灌、机械化或溯源等现代农业生产方式如何提高效率并带来新的劳动要求。', '对比传统与设施农业的两项差异', '指出一种现代农技对劳动者技能的新要求'),
    t('hs_community_volunteer', 'P', '高中服务性劳动', 10, 12, '社区志愿服务', 'Community volunteering', 'moe-ld-2020:SL', '能在社区或公益机构完成有岗位职责的志愿服务，遵守约定时间并填写服务记录。', '完成一次不少于两小时的岗位服务', '提交含反馈的志愿服务记录'),
    t('hs_career_internship', 'P', '高中服务性劳动', 10, 12, '职业体验见习', 'Career internship shadowing', 'moe-ld-2020:SL', '能在见习岗位观察真实劳动流程，完成允许范围内的辅助任务，并整理岗位技能清单。', '记录见习日的主要工序与安全注意', '列出该岗位所需的三项核心技能'),
    t('hs_public_project_org', 'M', '高中服务性劳动', 10, 12, '公益项目组织', 'Organizing a public-benefit project', 'moe-ld-2020:SL', '能与同伴策划一项小型公益活动，明确目标、分工、物资与风险，并在结束后做效果反思。', '提交含分工表的活动方案', '用参与人数或反馈总结改进点'),
    t('hs_innovation_make', 'P', '创造性劳动', 10, 12, '创新制作项目', 'Innovative making project', 'moe-ld-2020:CL', '能针对生活不便提出改进方案，用废旧或低成本材料制作可用原型并展示使用效果。', '完成一件可演示的改进原型', '说明创新点与仍未解决的问题'),
    t('hs_labor_career_plan', 'M', '创造性劳动', 10, 12, '劳动与职业规划', 'Labor and career planning', 'moe-ld-2020:CL', '能把劳动体验与兴趣、能力对照，形成高中阶段可执行的职业探索计划。', '对照三次劳动体验写出能力清单', '制定含两项实践任务的学期探索计划'),
    t('hs_labor_safety_law', 'L', '创造性劳动', 10, 12, '劳动安全与法规', 'Labor safety and regulations', 'moe-ld-2020:CL', '能使用未成年人保护、工时与防护等常用术语，说明实习或兼职中不可接受的风险安排。', '指出一份兼职广告中的两处违规风险', '列出上岗前必须确认的防护与保险事项'),
]
