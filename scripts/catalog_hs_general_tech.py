# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "tyjs", "通用技术"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_GENERAL_TECH = [
    t('tech_nature_scope', 'C', '技术与设计', 10, 12, '技术及其性质', 'Nature of technology', 'moe-tyjs-2017:TD1', '能用具体产品说明技术如何满足人的需要，并区分发明、改进与简单仿制。', '举两件日常用品说明其技术目的', '比较改进型产品与全新发明的差异'),
    t('design_general_process', 'P', '技术与设计', 10, 12, '设计的一般过程', 'General design process', 'moe-tyjs-2017:TD1', '能按发现问题、构思方案、制作模型、测试改进的顺序完成一件小型设计任务。', '提交一份带阶段记录的设计档案', '说明测试后修改了哪一处方案'),
    t('find_clarify_problem', 'M', '技术与设计', 10, 12, '发现与明确问题', 'Find and define problems', 'moe-tyjs-2017:TD1', '能把模糊需求写成可检验的设计问题，列出约束条件、使用对象与成功标准。', '把校园痛点改写成一条设计问题', '列出至少三条可测量的成功标准'),
    t('scheme_ideation', 'P', '技术与设计', 10, 12, '方案构思', 'Scheme ideation', 'moe-tyjs-2017:TD1', '能用草图或文字提出不少于两种可行方案，并依据约束比较后选定一种。', '画出两种结构不同的方案草图', '用对比表说明选定理由'),
    t('model_making', 'P', '技术与设计', 10, 12, '模型制作', 'Model making', 'moe-tyjs-2017:TD1', '能选用纸板、木条或数字工具制作能体现主要功能的模型，并记录关键尺寸。', '完成一件可演示功能的模型', '标注模型与实物设想的比例'),
    t('design_drawings', 'R', '技术与设计', 10, 12, '设计图样', 'Design drawings', 'moe-tyjs-2017:TD1', '能识读并绘制简单三视图或爆炸图，用尺寸、材料与装配关系表达设计意图。', '为作品补全带尺寸的三视图', '根据图样指出两个装配关系'),
    t('material_process', 'C', '技术与设计', 10, 12, '材料与工艺', 'Materials and processes', 'moe-tyjs-2017:TD1', '能根据强度、加工难度与成本选择材料，并说明切割、连接、表面处理等工艺要点。', '为同一功能比较两种材料取舍', '列出制作时必须遵守的工艺顺序'),
    t('design_evaluation', 'M', '技术与设计', 10, 12, '设计评价', 'Design evaluation', 'moe-tyjs-2017:TD1', '能从功能、安全、美观、成本与环保等方面评价作品，并提出可操作的改进建议。', '用评价表给同伴作品打分并说明', '写出两条针对测试结果的改进'),
    t('structure_design', 'C', '技术与设计深化', 10, 12, '结构及其设计', 'Structure and its design', 'moe-tyjs-2017:TD2', '能识别梁、桁架、壳体等常见结构形式，并说明受力路径与稳定措施。', '指出教具模型中的承力构件', '提出一种提高稳定性的结构改法'),
    t('process_flow_design', 'P', '技术与设计深化', 10, 12, '流程及其设计', 'Process flow design', 'moe-tyjs-2017:TD2', '能把一项制作或服务拆成有序工序，标出并行、检验与返工节点并优化瓶颈。', '绘制含判断的工序流程图', '指出一处可缩短等待的改动'),
    t('system_design', 'C', '技术与设计深化', 10, 12, '系统及其设计', 'System and its design', 'moe-tyjs-2017:TD2', '能用输入、处理、输出与反馈描述简单技术系统，并分析子系统之间的依赖。', '画出自动浇水装置的系统框图', '说明缺少反馈时系统会如何失控'),
    t('control_design', 'C', '技术与设计深化', 10, 12, '控制及其设计', 'Control and its design', 'moe-tyjs-2017:TD2', '能区分开环与闭环控制，说明传感器、控制器与执行器如何把实际量拉向目标。', '对照温控实例标出三个控制环节', '解释开环无法自动纠正偏差的原因'),
    t('electronic_control_intro', 'P', '技术与设计深化', 10, 12, '电子控制入门', 'Electronic control intro', 'moe-tyjs-2017:TD2', '能用开关、传感器与简单电路实现一种控制功能，并排除断路或接反等常见故障。', '搭出光控或温控小电路并演示', '根据现象判断一处接线错误'),
    t('robot_project', 'P', '技术与设计深化', 10, 12, '机器人专题', 'Robotics project', 'moe-tyjs-2017:TD2', '能组装或编程完成循迹、避障或抓取等一项机器人任务，并记录参数调整过程。', '完成指定场地的一项机器人任务', '说明一次参数修改如何改善表现'),
    t('architecture_design', 'C', '工程专题', 10, 12, '建筑及其设计', 'Architecture and design', 'moe-tyjs-2017:EL', '能结合功能分区、承重、采光与疏散说明小型建筑方案的基本考虑，并识读简易平面图。', '为校园小型展廊画出功能分区', '在平面图上标出出入口与承重墙'),
    t('car_drive_maintain', 'P', '工程专题', 10, 12, '汽车驾驶与保养入门', 'Driving and car care intro', 'moe-tyjs-2017:EL', '能说明起步前检查、视野盲区与日常保养项目，并在模拟或认知层面完成安全操作要点。', '列出出车前五项检查内容', '说明轮胎气压异常时的处理办法'),
    t('clothing_design', 'P', '工程专题', 10, 12, '服装及其设计', 'Clothing and design', 'moe-tyjs-2017:EL', '能按使用场合确定款式与面料，完成纸样或效果图，并说明缝制或裁剪的关键步骤。', '提交一件主题服装的效果图', '为面料选择写出两条功能理由'),
    t('tech_testing', 'P', '工程专题', 10, 12, '技术试验', 'Technical testing', 'moe-tyjs-2017:EL', '能针对强度、稳定性或控制效果设计对比试验，记录数据并据此改进作品。', '写出含变量控制的试验方案', '用试验数据说明一次改进是否有效'),
]
