# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T


Pfx = "ty"
Sub = "体育与健康"

def st(g):
    if g <= 2:
        return 1
    if g <= 4:
        return 2
    if g <= 6:
        return 3
    return 4

def ty(code, g):
    return f'moe-ty-2022:{code}.S{st(g)}'

def p(slug, typ, domain, code, g0, g1, name, en, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, ty(code, g0), desc, *ev)

PE = [
    p('natural_walking', 'P', '基本运动技能', 'MS', 1, 2, '自然走', 'Natural walk', '能在不同地面上保持平衡自然行走。', '沿直线走十米不偏离', '在窄道上平稳通过'),
    p('running_basics', 'P', '基本运动技能', 'MS', 1, 2, '跑的基本动作', 'Running basics', '掌握摆臂、抬腿协调的慢跑动作。', '完成二十米慢跑', '起跑时不抢跑'),
    p('two_foot_jump', 'P', '基本运动技能', 'MS', 1, 2, '双脚跳', 'Two-foot jump', '能双脚同时起跳落地，跳过小障碍。', '跳过十厘米高障碍', '落地时屈膝缓冲'),
    p('throw_softball', 'P', '基本运动技能', 'MS', 1, 2, '投软球', 'Softball throw', '能用单手肩上投或下手投将软球投出。', '投中两米外目标', '投掷前观察周围安全'),
    p('catch_large_ball', 'P', '基本运动技能', 'MS', 1, 2, '接大球', 'Catch large ball', '能张开双臂接住滚来或抛来的大球。', '连续接住五次滚球', '接球时目视来球'),
    p('balance_on_line', 'P', '基本运动技能', 'MS', 1, 2, '走平衡', 'Balance walk', '能在地面线或低平衡木上保持身体稳定。', '走完全程不落地', '双臂张开辅助平衡'),
    p('formation_drill', 'P', '基本运动技能', 'MS', 1, 2, '队列与队形', 'Formation drill', '能听口令完成立正、稍息、齐步走等队列动作。', '与同伴保持整齐队形', '快速准确变换两列队形'),
    p('rhythmic_movement', 'P', '基本运动技能', 'MS', 1, 2, '节奏性动作', 'Rhythmic movement', '能随音乐或口令做简单节奏性体操动作。', '跟随节拍做八拍动作', '与同伴动作同步'),
    p('direction_change_run', 'P', '基本运动技能', 'MS', 3, 4, '变向跑', 'Direction change run', '能在跑动中改变方向并保持速度控制。', '绕桩跑不碰桩', '急停后稳定站立'),
    p('single_foot_hop', 'P', '基本运动技能', 'MS', 3, 4, '单脚跳', 'Single-foot hop', '能单脚连续跳跃一定距离并保持节奏。', '单脚跳过五米', '左右脚交替练习'),
    p('overhand_throw', 'P', '基本运动技能', 'MS', 3, 4, '肩上投掷', 'Overhand throw', '掌握转体、鞭打动作的肩上投掷。', '投沙包达到规定距离', '投掷方向避开人群'),
    p('kick_stationary_ball', 'P', '基本运动技能', 'MS', 3, 4, '踢球入门', 'Kick ball', '能用脚内侧或正脚背踢静止球。', '踢中三米外标志', '支撑脚位置正确'),
    p('dribble_handball', 'P', '基本运动技能', 'MS', 3, 4, '手运球', 'Hand dribble', '能连续用手运球并保持对球的控制。', '运球绕障碍十米', '抬头观察路线'),
    p('relay_handoff', 'P', '基本运动技能', 'MS', 3, 4, '接力传接', 'Relay handoff', '能在接力中稳定传接棒或标志物。', '完成四人接力不掉棒', '在标记区内交接'),
    p('long_jump_takeoff', 'P', '基本运动技能', 'MS', 5, 6, '立定跳远', 'Standing long jump', '掌握预摆、蹬伸、落地的立定跳远动作。', '跳出个人最好成绩', '落地时双脚前伸'),
    p('sprint_start', 'P', '基本运动技能', 'MS', 5, 6, '短跑起跑', 'Sprint start', '能采用合理起跑姿势快速启动。', '听口令起跑反应及时', '起跑后加速跑十米'),
    p('volleyball_pass', 'P', '基本运动技能', 'MS', 5, 6, '排球垫球', 'Volleyball pass', '能用前臂垫击排球并完成连续对垫。', '与同伴对垫五次', '移动到位再垫球'),
    p('basketball_dribble', 'P', '基本运动技能', 'MS', 5, 6, '篮球运球', 'Basketball dribble', '能低运球、变向运球通过简单路线。', '运球绕桩不丢球', '非运球手保护球'),
    p('rope_skipping_basic', 'P', '基本运动技能', 'MS', 5, 6, '跳绳基础', 'Rope skipping', '能连续跳绳并尝试不同节奏。', '连续跳三十次', '调整绳长适合身高'),
    p('gymnastics_roll', 'P', '基本运动技能', 'MS', 5, 6, '滚翻动作', 'Gymnastics roll', '能完成前滚翻或侧滚翻等基本体操动作。', '独立完成前滚翻', '滚翻后平稳站起'),
    p('throw_catch_progression', 'P', '基本运动技能', 'MS', 5, 6, '传接进阶', 'Throw catch', '能在移动中传接球并保持成功率。', '移动中完成十次传球', '接球后快速传回'),
    p('multi_skill_combo', 'P', '基本运动技能', 'MS', 7, 9, '组合动作', 'Skill combination', '能将跑、跳、投组合运用于游戏或测试。', '完成综合体能闯关', '动作衔接流畅'),
    p('flexibility_stretch', 'P', '体能', 'PF', 1, 2, '柔韧拉伸', 'Flexibility stretch', '能完成基本静态拉伸，增大关节活动范围。', '坐位体前屈有进步', '拉伸时避免弹震'),
    p('core_stability_play', 'P', '体能', 'PF', 1, 2, '核心稳定游戏', 'Core stability', '通过游戏体会腹部与背部协同稳定身体。', '平板支撑坚持十五秒', '爬行时躯干不塌腰'),
    p('endurance_jogging', 'P', '体能', 'PF', 3, 4, '耐力慢跑', 'Endurance jog', '能按节奏慢跑并完成规定圈数。', '慢跑一圈不停步', '跑后做放松拉伸'),
    p('strength_push_pull', 'P', '体能', 'PF', 3, 4, '推拉力量', 'Push and pull', '能完成俯卧撑、引体辅助等基础力量练习。', '完成标准跪姿俯卧撑', '悬垂坚持十秒'),
    p('agility_ladder', 'P', '体能', 'PF', 3, 4, '灵敏梯练习', 'Agility ladder', '能快速准确完成脚步穿越格线练习。', '完成绳梯往返', '脚步轻快节奏稳'),
    p('coordination_ball', 'P', '体能', 'PF', 3, 4, '球类协调', 'Ball coordination', '在抛接、拍球中提高手眼协调。', '对抛网球二十次', '拍球走直线五米'),
    p('speed_reaction', 'P', '体能', 'PF', 5, 6, '速度反应', 'Speed reaction', '能对信号快速做出跑、停、变向反应。', '听口令快速起跑', '反应游戏得分提高'),
    p('muscular_endurance', 'P', '体能', 'PF', 5, 6, '肌肉耐力', 'Muscular endurance', '能完成多组仰卧起坐、深蹲等练习。', '一分钟仰卧起坐达标', '深蹲动作规范'),
    p('cardio_fitness_test', 'P', '体能', 'PF', 5, 6, '心肺耐力', 'Cardio fitness', '了解心率与运动强度关系，完成耐力测试。', '完成八百或一千米跑', '跑后测量脉搏恢复'),
    p('shuttle_run', 'P', '体能', 'PF', 5, 6, '折返跑', 'Shuttle run', '能在折返跑中控制速度并快速转身。', '完成十米折返五次', '转身时降低重心'),
    p('power_jump', 'P', '体能', 'PF', 7, 9, '爆发力跳跃', 'Power jump', '通过纵跳、摸高等练习发展下肢爆发力。', '摸高成绩有提升', '起跳前充分摆臂'),
    p('strength_training_safe', 'P', '体能', 'PF', 7, 9, '力量训练安全', 'Strength training', '掌握自重力量练习的正确姿势与负荷控制。', '完成标准俯卧撑', '力量练习后充分拉伸'),
    p('fitness_self_monitor', 'M', '体能', 'PF', 7, 9, '体能自我监测', 'Fitness monitor', '能记录运动心率、成绩并制定改进计划。', '填写一周运动日志', '根据数据调整训练量'),
    p('football_rules_basics', 'C', '专项运动', 'SP', 3, 4, '足球规则初识', 'Football rules', '知道越位、犯规等基本规则及场上位置。', '说出守门员职责', '识别手球犯规'),
    p('football_pass_shoot', 'P', '专项运动', 'SP', 3, 4, '足球传射', 'Football pass shoot', '能与同伴短传配合并尝试射门。', '与同伴完成三次传球', '射门脚法基本正确'),
    p('football_safety', 'C', '专项运动', 'SP', 3, 4, '足球安全', 'Football safety', '了解护腿板、热身及对抗中的自我保护。', '赛前完成动态热身', '不做危险铲球动作'),
    p('warmup_cooldown', 'P', '专项运动', 'SP', 3, 4, '热身与放松', 'Warmup cooldown', '养成运动前热身、运动后拉伸的习惯。', '完成五分钟动态热身', '跑后慢走并拉伸'),
    p('outdoor_activity_safety', 'C', '专项运动', 'SP', 1, 2, '户外活动安全', 'Outdoor safety', '在跑步、游戏时注意场地、天气和同伴安全。', '检查活动场地无隐患', '炎热天气减少暴晒'),
    p('basketball_shoot_pass', 'P', '专项运动', 'SP', 5, 6, '篮球传投', 'Basketball skills', '能胸前传球、上篮或近距离投篮。', '连续上篮三次', '传球到位不过高'),
    p('basketball_defense', 'P', '专项运动', 'SP', 5, 6, '篮球防守', 'Basketball defense', '掌握滑步、盯人防守基本站位。', '防守时保持低重心', '不拉拽对手'),
    p('table_tennis_stroke', 'P', '专项运动', 'SP', 5, 6, '乒乓球击球', 'Table tennis', '能正手攻球或推挡往返击球。', '对打十个回合', '握拍姿势正确'),
    p('table_tennis_serve', 'P', '专项运动', 'SP', 5, 6, '乒乓球发球', 'Table tennis serve', '能发出合法的平击或下旋球。', '发球过网落台', '发球不抛过高'),
    p('badminton_clear', 'P', '专项运动', 'SP', 5, 6, '羽毛球高远球', 'Badminton clear', '能发高远球并完成简单对打。', '高远球过对方底线', '握拍放松转紧'),
    p('swimming_water_safety', 'C', '专项运动', 'SP', 5, 6, '游泳与水上安全', 'Swimming safety', '知道不在无监护水域游泳及抽筋自救要点。', '复述防溺水六不准', '演示漂浮求助姿势'),
    p('martial_arts_basic', 'P', '专项运动', 'SP', 5, 6, '武术基本功', 'Martial arts', '能练习基本步型、手型及一套简化动作。', '完成五步拳套路', '冲拳发声有力'),
    p('broadcast_gymnastics', 'P', '专项运动', 'SP', 3, 6, '广播体操', 'Broadcast exercises', '能跟上节奏完成规定广播体操。', '整套动作连贯', '节拍与动作一致'),
    p('traditional_sports_games', 'P', '专项运动', 'SP', 3, 6, '传统体育游戏', 'Traditional games', '体验踢毽子、跳绳、滚铁环等传统项目。', '连续踢毽子五次', '与同伴合作完成游戏'),
    p('swimming_basics', 'P', '专项运动', 'SP', 7, 9, '游泳基础', 'Swimming basics', '能在水中换气、漂浮并尝试一种泳姿。', '水中连续换气五次', '蹬壁出发流线型'),
    p('track_sprint_hurdle', 'P', '专项运动', 'SP', 7, 9, '田径短跑跨栏', 'Track sprint', '掌握短跑、跨栏或接力技术要点。', '百米跑成绩进步', '跨栏节奏稳定'),
    p('track_field_events', 'P', '专项运动', 'SP', 7, 9, '田赛项目', 'Field events', '能完成跳远、投掷等田赛基本技术。', '实心球出手角度合理', '跳远助跑节奏正确'),
    p('gymnastics_apparatus', 'P', '专项运动', 'SP', 7, 9, '体操器械', 'Gymnastics apparatus', '能在保护与帮助下完成简单器械动作。', '完成跳箱支撑越', '双杠支撑摆动'),
    p('volleyball_serve', 'P', '专项运动', 'SP', 7, 9, '排球发球', 'Volleyball serve', '能用下手或上手动作发球过网。', '发球成功率提高', '发球前观察站位'),
    p('team_tactics_intro', 'C', '专项运动', 'SP', 7, 9, '团队战术初识', 'Team tactics', '理解传切、掩护等基本配合概念。', '在比赛中完成一次配合', '说明站位分工'),
    p('balanced_diet', 'C', '健康教育', 'HE', 1, 2, '均衡饮食', 'Balanced diet', '知道每天摄入谷薯、蔬果、肉蛋奶等多样食物。', '画出一天均衡餐盘', '说出三种健康零食'),
    p('breakfast_importance', 'C', '健康教育', 'HE', 1, 2, '早餐重要性', 'Breakfast', '了解规律吃早餐对学习和生长的作用。', '记录一周早餐情况', '设计一份健康早餐'),
    p('posture_spine_care', 'C', '健康教育', 'HE', 1, 2, '姿势与脊柱', 'Posture care', '保持正确站坐姿势，避免长时间弯腰驼背。', '自检读写姿势', '书包双肩背'),
    p('sleep_hygiene', 'C', '健康教育', 'HE', 3, 4, '睡眠卫生', 'Sleep hygiene', '知道充足睡眠有助于恢复和专注，养成固定作息。', '记录就寝与起床时间', '睡前减少屏幕使用'),
    p('eye_care_habits', 'C', '健康教育', 'HE', 3, 4, '用眼卫生', 'Eye care', '保持读写距离、光线充足并定时休息眼睛。', '演示正确读写姿势', '完成眼保健操'),
    p('health_goal_setting', 'M', '健康教育', 'HE', 3, 4, '健康目标设定', 'Health goals', '能设定可测量的运动或饮食小目标并跟踪。', '设定每周运动三次', '记录目标完成情况'),
    p('nutrition_labels', 'C', '健康教育', 'HE', 5, 6, '营养标签', 'Nutrition labels', '能读懂包装上的能量、糖、盐等信息并做选择。', '比较两种饮料含糖量', '选择低糖健康食品'),
    p('hydration_exercise', 'C', '健康教育', 'HE', 5, 6, '运动补水', 'Hydration', '知道运动前后适量补水，避免脱水。', '说明运动中何时喝水', '识别脱水早期信号'),
    p('first_aid_basics', 'P', '健康教育', 'HE', 5, 6, '急救基础', 'First aid basics', '掌握擦伤处理、止血包扎及求助流程。', '演示清洁伤口步骤', '拨打120说明情况'),
    p('cpr_aed_awareness', 'C', '健康教育', 'HE', 7, 9, '心肺复苏认知', 'CPR awareness', '了解心肺复苏与AED使用的基本流程与意义。', '复述CPR步骤', '找出校园AED位置'),
    p('injury_prevention', 'C', '健康教育', 'HE', 7, 9, '运动损伤预防', 'Injury prevention', '知道热身、放松、循序渐进原则以预防损伤。', '制定赛前热身计划', '识别过度训练信号'),
    p('mental_health_stress', 'C', '健康教育', 'HE', 7, 9, '压力与情绪', 'Mental health', '能识别考试等压力并采用运动、呼吸等方法调节。', '说出两种减压方法', '运动后记录心情变化'),
    p('substance_avoidance', 'C', '健康教育', 'HE', 7, 9, '拒绝烟酒毒品', 'Substance avoidance', '了解烟酒毒品对健康的危害并坚定拒绝。', '列举吸烟三种危害', '角色扮演拒绝递烟'),
    p('follow_rules', 'M', '体育品德', 'CH', 1, 2, '遵守规则', 'Follow rules', '在游戏中自觉遵守规则，服从裁判或教师口令。', '犯规后主动承认', '提醒同伴遵守规则'),
    p('respect_opponents', 'M', '体育品德', 'CH', 1, 2, '尊重对手', 'Respect opponents', '比赛前后与对手握手，不嘲笑失误。', '赛后向对手致谢', '对手得分时不打扰'),
    p('teamwork_cooperation', 'M', '体育品德', 'CH', 3, 4, '团队合作', 'Teamwork', '在集体项目中主动配合、鼓励同伴。', '传球给位置更佳队友', '落后时为同伴加油'),
    p('fair_play', 'M', '体育品德', 'CH', 3, 4, '公平竞赛', 'Fair play', '拒绝作弊，尊重判罚，体现体育精神。', '主动报告出界球', '不因判罚与裁判争执'),
    p('sport_event_etiquette', 'M', '体育品德', 'CH', 3, 4, '观赛礼仪', 'Event etiquette', '观看比赛时文明加油，不辱骂运动员或裁判。', '为双方精彩表现鼓掌', '保持看台整洁'),
    p('perseverance_effort', 'M', '体育品德', 'CH', 5, 6, '坚持与努力', 'Perseverance', '面对困难项目坚持练习，不轻言放弃。', '耐力跑坚持到终点', '记录个人进步'),
    p('resilience_setback', 'M', '体育品德', 'CH', 5, 6, '抗挫能力', 'Resilience', '比赛失利后能调整情绪，总结经验再尝试。', '失利后与队友总结', '下次训练改进一点'),
    p('leadership_rotation', 'M', '体育品德', 'CH', 7, 9, '轮换担当', 'Leadership rotation', '轮流担任队长、裁判等角色并负责任。', '担任裁判公正判罚', '组织小组热身'),
    p('sportsmanship_reflection', 'M', '体育品德', 'CH', 7, 9, '体育精神反思', 'Sportsmanship', '能结合实例说明尊重、公平、友谊的体育品德。', '撰写体育品德短文', '举例中外运动员风范'),
    p('side_step_shuffle', 'P', '基本运动技能', 'MS', 3, 4, '侧向滑步', 'Side shuffle', '能侧向快速移动并保持重心稳定。', '侧向滑步五米不交叉', '防守站位时使用滑步'),
    p('handstand_wall', 'P', '专项运动', 'SP', 7, 9, '靠墙倒立', 'Wall handstand', '能在保护下完成靠墙倒立体会支撑平衡。', '靠墙倒立坚持五秒', '落地时屈膝缓冲'),
    p('physical_activity_guidelines', 'C', '健康教育', 'HE', 5, 6, '活动量指南', 'Activity guidelines', '知道每日中高强度活动建议时间并尝试达成。', '记录一天运动时长', '说明久坐危害'),
]
