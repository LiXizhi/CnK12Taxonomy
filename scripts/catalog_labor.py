# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T


Pfx = "ld"
Sub = "劳动"

def st(g):
    if g <= 2:
        return 1
    if g <= 4:
        return 2
    if g <= 6:
        return 3
    return 4

def ld(code, g):
    return f'moe-ld-2022:{code}.S{st(g)}'

def l(slug, typ, domain, code, g0, g1, name, en, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, ld(code, g0), desc, *ev)

LABOR = [
    l('pack_schoolbag', 'P', '日常生活劳动', 'DL', 1, 2, '整理书包', 'Pack schoolbag', '能按课表整理书本文具，保持书包整洁。', '独立整理书包', '检查是否带齐次日用品'),
    l('tidy_desk_corner', 'P', '日常生活劳动', 'DL', 1, 2, '整理课桌与区域', 'Tidy desk', '能清理课桌、图书角并保持物品归位。', '课桌整洁无杂物', '图书按编号放回'),
    l('wash_hands_face', 'P', '日常生活劳动', 'DL', 1, 2, '洗手洗脸', 'Wash hands face', '掌握正确洗手洗脸步骤，养成卫生习惯。', '演示七步洗手法', '饭前便后主动洗手'),
    l('fold_clothes_basic', 'P', '日常生活劳动', 'DL', 3, 4, '折叠衣物', 'Fold clothes', '能折叠上衣、裤子等常见衣物并摆放整齐。', '折叠T恤四角对齐', '将衣物放入指定位置'),
    l('simple_laundry', 'P', '日常生活劳动', 'DL', 3, 4, '简单洗涤', 'Simple laundry', '在指导下手洗小件衣物并晾晒。', '手洗袜子并拧干', '正确晾晒衣物'),
    l('table_setting_cleanup', 'P', '日常生活劳动', 'DL', 3, 4, '摆餐具与收拾', 'Table setting', '能摆放碗筷、饭后收拾桌面并擦桌。', '为家人摆好餐具', '饭后清理桌面残渣'),
    l('cooking_simple_meal', 'P', '日常生活劳动', 'DL', 5, 6, '简易烹饪', 'Simple cooking', '在成人监护下完成煮面、蒸蛋等简单餐食。', '煮一碗面条', '烹饪后关闭火源'),
    l('kitchen_safety', 'C', '日常生活劳动', 'DL', 5, 6, '厨房安全', 'Kitchen safety', '知道刀具、火源使用规范，避免烫伤切伤。', '列出厨房三条安全规则', '发现隐患及时提醒'),
    l('home_cleaning_plan', 'P', '日常生活劳动', 'DL', 5, 6, '家庭清洁', 'Home cleaning', '能扫地、拖地、擦窗等并完成小块区域清洁。', '完成卧室地面清扫', '清洁工具用后归位'),
    l('garbage_sort_home', 'P', '日常生活劳动', 'DL', 5, 6, '家庭垃圾分类', 'Home garbage sort', '能按当地标准进行垃圾分类投放。', '正确分类四类垃圾', '说明有害垃圾例子'),
    l('clothing_care_label', 'C', '日常生活劳动', 'DL', 7, 9, '衣物护理', 'Clothing care', '能读懂洗涤标签并进行基本熨烫或整理。', '解读洗涤符号含义', '熨烫一条围巾'),
    l('budget_shopping_list', 'M', '日常生活劳动', 'DL', 7, 9, '采购与预算', 'Shopping list', '能根据需求列清单并合理选购日用品。', '制定一周食材清单', '比较价格做出选择'),
    l('seed_germination', 'P', '生产劳动', 'PL', 1, 2, '种子萌发观察', 'Seed germination', '能浸泡、播种并观察种子发芽过程。', '记录豆苗三天变化', '说明发芽需要水与温度'),
    l('water_plants', 'P', '生产劳动', 'PL', 1, 2, '给植物浇水', 'Water plants', '能按需要给班级或家庭盆栽适量浇水。', '判断土壤干湿再浇水', '浇水不泼洒到外'),
    l('plant_vegetables_box', 'P', '生产劳动', 'PL', 3, 4, '箱式蔬菜种植', 'Box gardening', '能在花箱中松土、播种、间苗并观察生长。', '完成一次蔬菜播种', '记录生长高度'),
    l('compost_waste', 'C', '生产劳动', 'PL', 3, 4, '厨余堆肥', 'Compost waste', '了解厨余堆肥原理并参与班级堆肥箱管理。', '区分可堆肥与不可堆肥', '翻动堆肥保持通气'),
    l('observe_pets', 'P', '生产劳动', 'PL', 3, 4, '小动物照料', 'Pet care', '能在指导下喂食、清洁并观察小动物习性。', '记录宠物一日作息', '清理笼舍保持卫生'),
    l('paper_craft_make', 'P', '生产劳动', 'PL', 3, 4, '纸工制作', 'Paper craft', '能用折、剪、粘方法完成实用纸工作品。', '制作一个收纳盒', '工具使用安全'),
    l('simple_sewing', 'P', '生产劳动', 'PL', 5, 6, '简易缝补', 'Simple sewing', '能穿针打结并缝纽扣或简单裂缝。', '缝好一颗脱落纽扣', '针脚整齐不扎手'),
    l('woodwork_measure_cut', 'P', '生产劳动', 'PL', 5, 6, '木工测量切割', 'Woodwork basics', '在指导下测量、锯切并打磨简单木件。', '锯切指定长度木条', '佩戴护具操作'),
    l('assemble_simple_kit', 'P', '生产劳动', 'PL', 5, 6, '简易组装', 'Simple assembly', '能按说明组装模型或小型家具部件。', '完成模型组装', '检查螺丝是否拧紧'),
    l('traditional_craft_try', 'P', '生产劳动', 'PL', 5, 6, '传统手工艺', 'Traditional craft', '体验编织、陶艺等传统生产性手工基本步骤。', '完成一件陶艺或编织', '说明工艺与材料'),
    l('garden_harvest', 'P', '生产劳动', 'PL', 7, 9, '种植与收获', 'Garden harvest', '能参与整地、施肥、收获并估算产量。', '收获班级菜园蔬菜', '记录产量与用时'),
    l('tool_maintenance', 'P', '生产劳动', 'PL', 7, 9, '工具保养', 'Tool maintenance', '知道清洁、上油、存放工具的方法并执行。', '清洁并归位一套工具', '说明生锈预防方法'),
    l('small_batch_product', 'P', '生产劳动', 'PL', 7, 9, '小批量制作', 'Small batch product', '能按流程小批量制作手工作品并控制质量。', '制作五份一致书签', '检查次品并改进'),
    l('campus_duty_clean', 'P', '服务性劳动', 'SL', 1, 2, '校园值日清扫', 'Campus cleaning', '能完成分配的包干区清扫与垃圾分类。', '清扫走廊无纸屑', '工具用后放回原处'),
    l('classroom_service', 'P', '服务性劳动', 'SL', 1, 2, '班级服务', 'Classroom service', '主动承担发作业、整理讲台等班级服务。', '一周完成三次服务', '服务时不影响他人'),
    l('library_helper', 'P', '服务性劳动', 'SL', 3, 4, '图书小助手', 'Library helper', '能整理图书、引导同学安静阅读。', '按编号上架十本书', '提醒同学轻拿轻放'),
    l('green_campus_care', 'P', '服务性劳动', 'SL', 3, 4, '校园绿化养护', 'Green campus', '参与浇树、除草、补植等校园绿化劳动。', '给指定树坑浇水', '识别常见杂草'),
    l('elder_visit_help', 'P', '服务性劳动', 'SL', 3, 4, '关爱老人服务', 'Elder visit', '能在成人组织下探望老人并提供简单帮助。', '为老人读一段书', '陪老人散步聊天'),
    l('community_cleanup', 'P', '服务性劳动', 'SL', 5, 6, '社区清洁', 'Community cleanup', '参与社区或公园清洁、宣传等公益劳动。', '参加一次社区捡垃圾', '向居民宣传环保'),
    l('event_volunteer', 'P', '服务性劳动', 'SL', 5, 6, '活动志愿', 'Event volunteer', '能在校运会等活动担任引导、后勤等志愿岗位。', '完成志愿岗位任务', '提前到岗并穿戴标识'),
    l('care_kindergarten_peer', 'P', '服务性劳动', 'SL', 5, 6, '帮扶低年级', 'Peer mentoring', '能指导低年级同学完成简单劳动任务。', '教一年级整理书包', '耐心示范三遍'),
    l('career_shadow_visit', 'C', '服务性劳动', 'SL', 7, 9, '职业体验参观', 'Career shadow', '通过参观或短期体验了解不同职业劳动内容。', '记录一种职业一天工作', '说明所需技能'),
    l('career_interview', 'M', '服务性劳动', 'SL', 7, 9, '职业访谈', 'Career interview', '能采访从业者并整理劳动特点与要求。', '完成一份访谈提纲', '写出三条职业体会'),
    l('public_service_design', 'P', '服务性劳动', 'SL', 7, 9, '公益项目设计', 'Public service design', '能小组设计并实施小型校园或社区服务项目。', '策划一次旧物捐赠', '总结服务效果'),
    l('labor_safety_tools', 'C', '日常生活劳动', 'DL', 3, 4, '劳动工具安全', 'Tool safety', '知道剪刀、锤子等工具的正确握持与传递方式。', '演示剪刀传递方法', '发现损坏工具报告老师'),
    l('labor_safety_ppe', 'C', '生产劳动', 'PL', 5, 6, '劳动防护用品', 'Labor PPE', '了解手套、护目镜等防护用品的使用场景。', '匹配任务与防护用品', '操作前检查防护'),
    l('labor_meaning_reflection', 'M', '服务性劳动', 'SL', 5, 6, '劳动意义', 'Labor meaning', '能结合实例说明劳动对个人与社会的价值。', '写一段劳动体会', '举例劳动创造美好生活'),
    l('labor_habits_daily', 'M', '日常生活劳动', 'DL', 1, 2, '日常劳动习惯', 'Daily labor habits', '养成自己的事自己做、每日小劳动的习惯。', '连续一周自己系鞋带', '主动收拾玩具'),
    l('food_prep_safe', 'P', '日常生活劳动', 'DL', 7, 9, '安全备餐', 'Safe food prep', '能在监护下完成切配、烹饪并注意生熟分开。', '切配蔬菜并清台面', '生熟砧板分开使用'),
    l('repair_simple_fix', 'P', '生产劳动', 'PL', 7, 9, '简单维修', 'Simple repair', '能拧紧松螺丝、更换笔芯等简单维修劳动。', '修复松动的椅脚', '说明何时需专业维修'),
    l('recycle_upcycle', 'P', '生产劳动', 'PL', 3, 4, '废旧改造', 'Recycle upcycle', '能将废旧材料改造成可用物品。', '用瓶罐做花盆', '说明再利用减少浪费'),
    l('labor_contract_team', 'M', '服务性劳动', 'SL', 7, 9, '小组劳动契约', 'Team labor pact', '能与同伴制定劳动分工契约并互相监督。', '小组签署劳动分工表', '按契约完成各自任务'),
    l('seasonal_labor_festival', 'C', '服务性劳动', 'SL', 3, 4, '节日劳动服务', 'Festival service', '结合端午、中秋等节日参与包粽子、做月饼等服务劳动。', '参与一次节日劳动', '说明节日劳动的文化意义'),
    l('weather_adapt_labor', 'C', '生产劳动', 'PL', 1, 2, '天气与户外劳动', 'Weather and labor', '知道高温、雷雨等天气下调整或暂停户外劳动。', '说出雨天不宜浇花原因', '炎热时选择室内劳动'),
    l('labor_time_management', 'M', '日常生活劳动', 'DL', 5, 6, '劳动时间管理', 'Labor time mgmt', '能合理安排每日劳动时间，不与学习冲突。', '制定每日劳动时间表', '按时完成计划任务'),
    l('serve_cafeteria_line', 'P', '服务性劳动', 'SL', 3, 4, '食堂秩序服务', 'Cafeteria service', '能在午餐时协助维持排队秩序与桌面清洁。', '引导同学有序打餐', '提醒光盘行动'),
    l('labor_story_share', 'M', '日常生活劳动', 'DL', 3, 4, '劳动故事分享', 'Labor stories', '能分享家人或劳动者的故事，理解劳动尊严。', '介绍一位劳动者', '说出劳动中的困难与成就'),
    l('plant_identification_field', 'C', '生产劳动', 'PL', 7, 9, '田间识别', 'Field plant ID', '能在田间识别常见作物与杂草并记录。', '辨认三种作物', '说明除草时机'),
    l('digital_labor_tools', 'C', '生产劳动', 'PL', 7, 9, '数字劳动工具', 'Digital labor tools', '了解表格、清单等数字工具在劳动组织中的作用。', '用表格记录劳动分工', '在线共享任务进度'),
    l('labor_reflection_portfolio', 'M', '服务性劳动', 'SL', 7, 9, '劳动档案', 'Labor portfolio', '能整理劳动照片、记录与反思形成个人劳动档案。', '完成学期劳动档案', '设定下一学期劳动目标'),
    l('shoe_care_clean', 'P', '日常生活劳动', 'DL', 3, 4, '鞋袜清洁', 'Shoe care', '能刷洗鞋面、晾晒鞋袜并保持足部卫生。', '刷洗运动鞋并晾晒', '雨天后及时擦干鞋子'),
    l('neighborhood_survey_service', 'P', '服务性劳动', 'SL', 7, 9, '社区调查服务', 'Neighborhood survey', '能调查社区需求并提出可行服务建议。', '完成社区需求问卷', '提交一份服务建议'),
]
