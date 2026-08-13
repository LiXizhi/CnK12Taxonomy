# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "ty", "体育与健康"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_PE = [
    t('hs_track_event_refine', 'P', '高中运动技能', 10, 12, '田径专项提高', 'Track and field specialization', 'moe-ty-2017:MS', '能在短跑、跳跃或投掷中选定一项提高技术细节，并用成绩与动作质量检验进步。', '完成一次专项技术分解练习', '对照个人最好成绩记录改进点'),
    t('hs_ball_tactics_apply', 'P', '高中运动技能', 10, 12, '球类战术运用', 'Ball-game tactics in play', 'moe-ty-2017:MS', '能在篮球、足球或排球等项目中运用传切、掩护或防守轮转，并在对抗中完成既定配合。', '比赛中完成一次成功的战术配合', '赛后标出本队站位与职责分工'),
    t('hs_gym_aerobics_combo', 'P', '高中运动技能', 10, 12, '体操或健美操组合', 'Gymnastics or aerobics combo', 'moe-ty-2017:MS', '能把滚翻、平衡、跳跃或健美操步伐编成连贯组合，动作与节拍一致并注意保护。', '独立完成一套不少于八拍的组合', '保护同伴完成有难度的衔接动作'),
    t('hs_wushu_routine_refine', 'P', '高中运动技能', 10, 12, '武术套路提高', 'Wushu routine refinement', 'moe-ty-2017:MS', '能较完整演练一套拳术或器械套路，做到步型准确、劲力顺达并体现攻防含义。', '完整演练套路并自检步型', '指出两个动作的攻防意图'),
    t('hs_swim_snow_cognition', 'C', '高中运动技能', 10, 12, '游泳或冰雪可选认知', 'Swim or snow-sport cognition', 'moe-ty-2017:MS', '能说明一种泳姿或冰雪项目的安全要点、基本动作要领及场地条件限制。', '复述入水或上冰前的安全检查', '描述一种项目的基本滑行或划水要领'),
    t('hs_emerging_sports', 'P', '高中运动技能', 10, 12, '新兴运动项目', 'Emerging sports', 'moe-ty-2017:MS', '能体验定向、飞盘、攀岩或街舞健身等新兴项目的基本技能，并遵守该项目安全规则。', '完成一次新兴项目的入门任务', '列出该项目两条必须遵守的安全规则'),
    t('hs_strength_endurance', 'P', '高中体能', 10, 12, '力量耐力训练', 'Strength-endurance training', 'moe-ty-2017:PF', '能按正确姿势完成多组自重或轻负荷力量练习，控制组间休息并记录负荷变化。', '完成一组标准深蹲或俯卧撑', '在训练日志中记下组数与主观疲劳'),
    t('hs_speed_agility_drill', 'P', '高中体能', 10, 12, '速度灵敏训练', 'Speed and agility training', 'moe-ty-2017:PF', '能完成加速跑、变向与反应启动等练习，在折返或绳梯中保持低重心与步频控制。', '完成计时折返并比较前后成绩', '根据口令完成启动与急停'),
    t('hs_fitness_test_read', 'C', '高中体能', 10, 12, '体能测评解读', 'Fitness test interpretation', 'moe-ty-2017:PF', '能读懂肺活量、耐力跑、力量等测评结果的含义，指出个人短板并联系可训练因素。', '解释本人两项测评数据的含义', '根据短板选出对应的练习手段'),
    t('hs_personal_exercise_plan', 'M', '高中体能', 10, 12, '个性化锻炼计划', 'Personalized exercise plan', 'moe-ty-2017:PF', '能按目标、频率、强度与恢复安排两周锻炼计划，并根据疲劳与成绩做一次调整。', '提交含热身与放松的两周计划', '根据一次测评结果修改训练量'),
    t('hs_cpr_practice_cognition', 'P', '高中健康教育', 10, 12, '心肺复苏实操认知', 'CPR practice cognition', 'moe-ty-2017:HE', '能在模型上按呼叫求助、胸外按压与人工呼吸的顺序完成模拟操作，并说明AED的使用时机。', '在模型上完成一轮按压节奏练习', '指出校园AED位置及启用步骤'),
    t('hs_sport_injury_care', 'P', '高中健康教育', 10, 12, '运动损伤处理', 'Sports injury care', 'moe-ty-2017:HE', '能识别扭伤、拉伤等常见损伤的早期表现，正确实施停止活动、冷敷、加压与抬高，并判断何时就医。', '演示踝关节扭伤的现场处理', '说明何种情况必须停止自行处理'),
    t('hs_nutrition_weight_mgmt', 'C', '高中健康教育', 10, 12, '营养与体重管理', 'Nutrition and weight management', 'moe-ty-2017:HE', '能根据能量收支说明健康体重管理，避免极端节食，并为训练日搭配合理餐食。', '比较训练日与休息日的能量需求', '指出一种不健康减重做法的风险'),
    t('hs_mental_health_sport', 'M', '高中健康教育', 10, 12, '心理健康与运动', 'Mental health and exercise', 'moe-ty-2017:HE', '能识别学业压力与情绪波动，选择跑步、球类或拉伸等运动调节，并知道何时求助。', '记录运动前后情绪变化', '说出两条可求助的校园支持途径'),
    t('hs_avoid_addictive_behavior', 'C', '高中健康教育', 10, 12, '远离成瘾行为', 'Avoiding addictive behaviors', 'moe-ty-2017:HE', '能说明烟草、酒精、毒品及过度游戏对身心的危害，并在同伴压力情境中拒绝参与。', '列举三类成瘾行为的健康风险', '角色扮演中明确拒绝劝诱'),
    t('hs_rules_fair_play', 'L', '高中体育品德', 10, 12, '竞赛规则与公平', 'Rules and fair play', 'moe-ty-2017:CH', '能准确使用本专项主要判罚术语，自觉遵守规则并尊重裁判，抵制隐瞒犯规与辱骂。', '用规则术语解释一次判罚', '主动报告自己的出界或犯规'),
    t('hs_team_role_lead', 'M', '高中体育品德', 10, 12, '团队角色与领导', 'Team roles and leadership', 'moe-ty-2017:CH', '能在比赛或练习中承担队长、组织者或裁判等角色，协调分工并带动同伴完成任务。', '组织一次小组热身并清点人数', '赛后评价本队角色分工是否合理'),
    t('hs_spirit_career_link', 'C', '高中体育品德', 10, 12, '体育精神与生涯', 'Sportsmanship and career', 'moe-ty-2017:CH', '能把尊重、坚持与公平迁移到学业与职业规划，说明体育习惯如何服务终身健康。', '写一段体育精神与个人目标的联系', '列出毕业后可坚持的两项运动习惯'),
]
