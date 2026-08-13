# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "wl", "物理"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

JH_PHYSICS = [
    t('jh_measurement_error', 'P', '运动和力', 8, 8, '测量与误差', 'Measurement and error', 'moe-kx-2022:C03.S4', '能正确使用刻度尺、秒表等工具测量长度和时间，并估计读数误差。', '用刻度尺多次测量课桌长度取平均', '说明估读到最小刻度下一位的理由'),
    t('jh_mechanical_motion', 'C', '运动和力', 8, 8, '机械运动与参照物', 'Mechanical motion', 'moe-kx-2022:C03.S4', '能选择参照物判断物体是否运动，并区分运动和静止的相对性。', '举例说明坐车时人相对地面在运动', '判断同一物体相对不同参照物的状态'),
    t('jh_speed_and_v_t', 'P', '运动和力', 8, 8, '速度与v-t图像', 'Speed and v-t graphs', 'moe-kx-2022:C03.S4', '能用v=s/t计算平均速度，并读简单v-t图像比较快慢。', '由路程和时间求平均速度', '从v-t图比较两车谁先到达'),
    t('jh_mass_and_density', 'P', '运动和力', 8, 8, '质量与密度', 'Mass and density', 'moe-kx-2022:C01.S4', '能测量质量和体积并计算密度，用密度鉴别常见物质。', '用天平和量筒测金属块密度', '根据密度判断物体是铝还是铁'),
    t('jh_force_and_diagram', 'R', '运动和力', 8, 8, '力与受力示意图', 'Force diagrams', 'moe-kx-2022:C03.S4', '认识力的三要素，能画常见情境的受力示意图。', '画出桌面上书本的受力图', '标明拉力的作用点方向和示意大小'),
    t('jh_gravity_and_weight', 'C', '运动和力', 8, 8, '重力与重量', 'Gravity and weight', 'moe-kx-2022:C03.S4', '知道重力方向竖直向下，能用G=mg做简单计算并指出重心。', '计算质量50kg物体的重力', '说明重心位置对稳定的影响'),
    t('jh_elastic_friction', 'C', '运动和力', 8, 8, '弹力与摩擦力', 'Elastic force and friction', 'moe-kx-2022:C03.S4', '能判断弹力和滑动摩擦力的方向，并说明增大或减小摩擦的方法。', '指出弹簧测力计读数对应的力', '设计减小抽屉摩擦的两种办法'),
    t('jh_newton_first_inertia', 'C', '运动和力', 8, 9, '牛顿第一定律与惯性', 'Newton I and inertia', 'moe-kx-2022:C03.S4', '理解物体保持原有运动状态的性质叫惯性，能解释刹车前倾等现象。', '用小车实验说明不受力时的运动趋势', '解释为什么汽车要系安全带'),
    t('jh_two_force_balance', 'P', '运动和力', 8, 9, '二力平衡', 'Two-force balance', 'moe-kx-2022:C03.S4', '能判断一对力是否平衡，并用平衡条件求未知力。', '判断桌面上杯子是否受力平衡', '由平衡条件求绳子拉力'),
    t('jh_pressure_solids', 'C', '运动和力', 8, 9, '固体压强', 'Solid pressure', 'moe-kx-2022:C03.S4', '理解压强等于压力与受力面积之比，能解释刀刃锋利、履带车等实例。', '计算同一压力下面积减半后的压强', '说明骆驼蹄宽有利于在沙地行走'),
    t('jh_liquid_pressure', 'C', '运动和力', 8, 9, '液体压强', 'Liquid pressure', 'moe-kx-2022:C03.S4', '知道液体压强随深度增大，能用p=ρgh做简单计算。', '比较同一液体不同深度的压强', '解释拦河坝下部比上部厚'),
    t('jh_atmospheric_pressure', 'C', '运动和力', 8, 9, '大气压强', 'Atmospheric pressure', 'moe-kx-2022:C03.S4', '能用实验证明大气压存在，并说明吸管、吸盘等应用。', '描述马德堡半球实验说明什么', '解释高原上水的沸点为何降低'),
    t('jh_buoyancy', 'C', '运动和力', 8, 9, '浮力', 'Buoyancy', 'moe-kx-2022:C03.S4', '理解浮力等于排开液体的重力，能判断物体沉浮条件。', '用弹簧测力计测出物体在水中的浮力', '解释轮船由钢铁制成为何能浮在水面'),
    t('jh_sound_production', 'C', '声和光', 8, 8, '声音的产生与传播', 'Sound production', 'moe-kx-2022:C04.S4', '知道声音由振动产生、需要介质传播，能比较空气、固体传声。', '用尺子振动发声并使其停止', '解释月球上两人为何不能直接对话'),
    t('jh_pitch_loudness', 'C', '声和光', 8, 8, '音调响度与音色', 'Pitch loudness timbre', 'moe-kx-2022:C04.S4', '能区分音调、响度和音色，并联系频率、振幅说明。', '比较粗细橡皮筋发声音调', '听辨两种乐器的音色差异'),
    t('jh_noise_control', 'C', '声和光', 8, 8, '噪声及其控制', 'Noise control', 'moe-kx-2022:C04.S4', '能从声源、传播途径和人耳三方面提出控制噪声的办法。', '为教室设计两项降噪措施', '判断哪些声音属于噪声'),
    t('jh_light_rectilinear', 'C', '声和光', 8, 8, '光的直线传播', 'Rectilinear propagation', 'moe-kx-2022:C04.S4', '知道光在同种均匀介质中沿直线传播，能解释影和小孔成像。', '用手电筒演示影的形成', '画出小孔成像光路示意'),
    t('jh_reflection_plane', 'R', '声和光', 8, 8, '光的反射与平面镜', 'Reflection and plane mirror', 'moe-kx-2022:C04.S4', '能陈述反射定律，画出平面镜成像光路并说明像的特点。', '测量入射角与反射角是否相等', '用对称法画出物体在平面镜中的像'),
    t('jh_refraction_lens', 'C', '声和光', 8, 8, '光的折射与透镜', 'Refraction and lenses', 'moe-kx-2022:C04.S4', '知道光从空气进入水或玻璃会偏折，能区分凸透镜会聚与凹透镜发散。', '观察筷子在水中“折断”', '用凸透镜会聚阳光点燃纸片'),
    t('jh_convex_lens_image', 'P', '声和光', 8, 8, '凸透镜成像', 'Convex-lens images', 'moe-kx-2022:C04.S4', '能根据物距与焦距关系判断像的虚实、倒正和大小，并联系照相机、放大镜。', '在光具座上得到倒立实像', '说明放大镜成正立虚像的条件'),
    t('jh_temp_and_heat', 'C', '声和光', 8, 8, '温度与物态变化', 'Temperature and state change', 'moe-kx-2022:C02.S4', '能正确使用温度计，描述熔化和沸腾过程中的温度变化特点。', '读取体温计示数', '画出冰熔化时温度随时间变化的大致图像'),
    t('jh_charge_and_current', 'C', '电和磁', 9, 9, '电荷与电流', 'Charge and current', 'moe-kx-2022:C04.S4', '知道电荷有正负、同种相斥异种相吸，理解电流是电荷的定向移动。', '用气球摩擦演示静电吸引', '在电路中标出电流方向约定'),
    t('jh_circuit_connection', 'P', '电和磁', 9, 9, '电路连接', 'Circuit connection', 'moe-kx-2022:C04.S4', '能识别串联与并联，按电路图连接简单电路并排除断路。', '连接两灯串联和并联各一次', '根据小灯不亮判断可能断路位置'),
    t('jh_voltage_resistance', 'C', '电和磁', 9, 9, '电压与电阻', 'Voltage and resistance', 'moe-kx-2022:C04.S4', '理解电压是形成电流的原因，电阻与材料、长度、横截面积有关。', '用电压表测干电池电压', '比较长短不同镍铬丝的电阻大小'),
    t('jh_ohm_law', 'P', '电和磁', 9, 9, '欧姆定律', 'Ohm law', 'moe-kx-2022:C04.S4', '能用I=U/R进行简单计算，并设计实验探究电流与电压电阻关系。', '已知电压电阻求电流', '根据实验数据说明电流与电压成正比'),
    t('jh_series_parallel_calc', 'P', '电和磁', 9, 9, '串并联电路计算', 'Series-parallel calculation', 'moe-kx-2022:C04.S4', '能计算简单串、并联电路中的总电阻、电流和电压分配。', '求两个电阻串联后的总电阻', '说明并联时各支路电压相等'),
    t('jh_electric_power', 'C', '电和磁', 9, 9, '电功与电功率', 'Electric work and power', 'moe-kx-2022:C04.S4', '能读铭牌上的额定电压和额定功率，并计算简单用电量。', '由P=UI求小灯泡实际功率', '估算家用电器一天消耗的电能'),
    t('jh_magnetic_field', 'C', '电和磁', 9, 9, '磁场与电流磁效应', 'Magnetic field', 'moe-kx-2022:C04.S4', '能用磁感线描述磁场方向，知道通电导线周围存在磁场。', '用小磁针判断磁体周围磁场方向', '观察通电螺线管吸引铁钉'),
    t('jh_electromagnetic_induction_jh', 'C', '电和磁', 9, 9, '电磁感应入门', 'Induction intro', 'moe-kx-2022:C04.S4', '知道闭合电路一部分导体切割磁感线会产生感应电流，了解发电机原理。', '演示导体切割磁感线使电流计偏转', '说明水力发电如何把机械能转化为电能'),
    t('jh_work_and_power', 'P', '能量', 9, 9, '功和功率', 'Work and power', 'moe-kx-2022:C04.S4', '能判断力是否做功，并用W=Fs、P=W/t做简单计算。', '计算水平拉箱子做的功', '比较两人做功快慢'),
    t('jh_kinetic_potential', 'C', '能量', 9, 9, '动能与势能', 'Kinetic and potential energy', 'moe-kx-2022:C04.S4', '能说明影响动能、重力势能和弹性势能大小的因素，并分析转化。', '比较质量和速度对动能的影响', '分析滚摆上升下降时的能量转化'),
    t('jh_energy_transfer', 'C', '能量', 9, 9, '能量转化与守恒', 'Energy conservation', 'moe-kx-2022:C04.S4', '能在简单装置中指出能量如何转化，知道能量守恒但不能全部被利用。', '画出自行车下坡的能量转化链', '解释永动机不可能的原因'),
    t('jh_heat_engines_energy', 'C', '能量', 9, 9, '内能与热机', 'Internal energy and heat engines', 'moe-kx-2022:C04.S4', '知道做功和热传递可以改变物体内能，了解热机把内能转化为机械能。', '说明摩擦生热改变了什么能量', '指出四冲程汽油机的做功冲程'),
]
