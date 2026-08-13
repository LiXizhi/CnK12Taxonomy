# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "wl", "物理"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_PHYSICS = [
    t('particle_and_frame', 'L', '力学', 10, 10, '质点与参考系', 'Particle and frame', 'moe-wl-2017:MECH', '能把实际物体抽象为质点，并按研究需要选择参考系来描述位置变化。', '判断高铁过弯时能否视为质点', '用站台和车厢两种参考系描述同一落体'),
    t('uniform_accel_motion', 'P', '力学', 10, 10, '匀变速直线运动', 'Uniform acceleration', 'moe-wl-2017:MECH', '能用位移、速度、加速度关系分析匀变速直线运动，并读v-t图像。', '由v-t图求出一段时间内的位移', '计算刹车距离是否足够停下'),
    t('free_fall', 'C', '力学', 10, 10, '自由落体', 'Free fall', 'moe-wl-2017:MECH', '知道自由落体是初速度为零的匀加速运动，能用g估算下落时间。', '用打点纸带检验落体是否匀加速', '估算石子从楼顶落到地面的时间'),
    t('force_composition', 'R', '力学', 10, 10, '力的合成与分解', 'Force composition', 'moe-wl-2017:MECH', '能用力的平行四边形定则合成或分解共点力，并画出规范受力图。', '作图求出两个互成角度力的合力', '把斜面上重力分解为沿斜面分力'),
    t('newton_laws_apply', 'P', '力学', 10, 10, '牛顿定律应用', 'Newton laws apply', 'moe-wl-2017:MECH', '能结合牛顿第二定律列方程，分析物体在多个力作用下的加速度。', '求解木块在拉力与摩擦下的加速度', '解释同一力对不同质量物体效果不同'),
    t('overweight_weightless', 'C', '力学', 10, 10, '超重与失重', 'Overweight and weightless', 'moe-wl-2017:MECH', '能用牛顿定律解释升降机加速时视重变化，区分超重与失重。', '分析电梯启动时体重计示数变化', '说明完全失重时对地板压力为零'),
    t('curvilinear_motion', 'C', '力学', 10, 10, '曲线运动', 'Curvilinear motion', 'moe-wl-2017:MECH', '知道曲线运动速度沿切线，加速度指向速度变化的方向，能判断受力。', '画出弯道上速度与加速度方向', '说明匀速圆周也属于变速运动'),
    t('projectile_motion', 'P', '力学', 10, 10, '平抛运动', 'Projectile motion', 'moe-wl-2017:MECH', '能把平抛分解为水平匀速与竖直自由落体，并计算落点位置。', '由抛出高度求落地时间', '计算水平射程并与实验比较'),
    t('uniform_circular', 'C', '力学', 10, 11, '匀速圆周运动', 'Uniform circular motion', 'moe-wl-2017:MECH', '能用向心力公式分析匀速圆周运动，说明半径、速率与周期关系。', '计算过山车最低点所需向心力', '解释绳断后小球沿切线飞出'),
    t('gravity_law', 'C', '力学', 10, 11, '万有引力定律', 'Law of gravitation', 'moe-wl-2017:MECH', '能陈述万有引力定律，并用它估算天体表面的重力加速度。', '比较地球与月球表面g差异的原因', '由轨道数据估算中心天体质量'),
    t('satellite_motion', 'C', '力学', 10, 11, '卫星运动', 'Satellite motion', 'moe-wl-2017:MECH', '能区分卫星的圆周轨道与椭圆轨道，说明周期、半径与速度关系。', '解释同步卫星为何定点在赤道上空', '比较近地卫星与同步卫星的周期'),
    t('work_and_power', 'P', '力学', 11, 11, '功和功率', 'Work and power', 'moe-wl-2017:MECH', '能计算恒力做功和平均功率，并区分瞬时功率与平均功率。', '计算斜面拉力对木箱做的功', '由F与v求某一时刻的瞬时功率'),
    t('kinetic_energy_theorem', 'P', '力学', 11, 11, '动能定理', 'Work-energy theorem', 'moe-wl-2017:MECH', '能用动能定理把合外力做功与动能变化联系起来求解问题。', '由刹车过程求摩擦力做的功', '比较牛顿定律与动能定理的简繁'),
    t('mech_energy_conserv', 'C', '力学', 11, 11, '机械能守恒', 'Mechanical energy', 'moe-wl-2017:MECH', '能判断机械能是否守恒，并在只有重力或弹力做功时列出守恒式。', '分析摆球最高点与最低点的机械能', '说明有摩擦时机械能不守恒的去向'),
    t('charge_coulomb', 'C', '电磁学', 11, 11, '电荷与库仑定律', 'Coulomb law', 'moe-wl-2017:EM', '知道电荷守恒，能用库仑定律计算真空中点电荷之间的作用力。', '比较距离加倍后库仑力如何变化', '判断两电荷是相互吸引还是排斥'),
    t('electric_field_strength', 'R', '电磁学', 11, 11, '电场强度', 'Electric field', 'moe-wl-2017:EM', '能用电场强度描述电场，画出点电荷与匀强电场的电场线分布。', '由F=qE求试探电荷所受电场力', '根据电场线疏密比较场强大小'),
    t('potential_and_voltage', 'C', '电磁学', 11, 11, '电势与电势差', 'Potential and voltage', 'moe-wl-2017:EM', '能区分电势与电势差，并用W=qU计算电荷在电场中的能量变化。', '比较正电荷沿电场线移动时电势能', '由等势面判断电场强度的方向'),
    t('capacitor', 'C', '电磁学', 11, 11, '电容器', 'Capacitor', 'moe-wl-2017:EM', '知道电容器能储存电荷，能用C=Q/U分析电容与电压、电荷关系。', '说明插入电介质后电容如何变化', '计算平行板电容与面积间距关系'),
    t('steady_current', 'C', '电磁学', 11, 11, '恒定电流', 'Steady current', 'moe-wl-2017:EM', '能用I=Q/t和欧姆定律分析恒定电流电路中的电流与电压。', '由一段时间内通过的电荷求电流', '解释电源电动势与内阻各自的作用'),
    t('resistance_law', 'P', '电磁学', 11, 11, '电阻定律', 'Resistance law', 'moe-wl-2017:EM', '能用电阻定律计算导体电阻，说明材料、长度、横截面积的影响。', '比较同种材料粗细导线的电阻', '解释远距离输电为何用较粗导线'),
    t('series_parallel', 'P', '电磁学', 11, 11, '串并联电路', 'Series and parallel', 'moe-wl-2017:EM', '能计算串联、并联电路的总电阻，并分析分压与分流关系。', '设计两种接法比较小灯泡亮度', '画出串并联等效电路并求解电流'),
    t('magnetic_field', 'C', '电磁学', 11, 11, '磁场', 'Magnetic field', 'moe-wl-2017:EM', '能用磁感线描述磁场方向，知道电流周围存在磁场并能判断方向。', '用右手螺旋定则判断直导线磁场', '画出通电螺线管内外的磁感线'),
    t('ampere_force', 'P', '电磁学', 11, 11, '安培力', 'Ampere force', 'moe-wl-2017:EM', '能用安培力公式判断通电导线在磁场中的受力方向与大小。', '用左手定则判断导线受力方向', '计算匀强磁场中一段导线的安培力'),
    t('lorentz_force', 'C', '电磁学', 11, 11, '洛伦兹力', 'Lorentz force', 'moe-wl-2017:EM', '能判断洛伦兹力方向，解释带电粒子在匀强磁场中做圆周运动。', '画出正离子垂直进入磁场的轨迹', '说明洛伦兹力对粒子不做功的原因'),
    t('electromagnetic_induction', 'C', '电磁学', 11, 11, '电磁感应', 'Electromagnetic induction', 'moe-wl-2017:EM', '能用磁通量变化说明感应电动势的产生条件，并陈述楞次定律。', '判断线圈磁通量增加时感应电流方向', '比较切割磁感线与磁通量变化两种说法'),
    t('alternating_current', 'C', '电磁学', 11, 11, '交变电流', 'Alternating current', 'moe-wl-2017:EM', '知道交变电流大小和方向随时间变化，能读正弦交流的峰值与有效值。', '由u=Umsinωt读出电压峰值', '说明家用电器铭牌电压指有效值'),
    t('kinetic_molecular', 'C', '热学', 12, 12, '分子动理论', 'Kinetic molecular theory', 'moe-wl-2017:TH', '能用分子热运动和相互作用解释扩散、布朗运动和物态差异。', '解释墨水在热水中扩散更快', '说明温度是分子平均动能的标志'),
    t('ideal_gas_state', 'P', '热学', 12, 12, '理想气体状态', 'Ideal gas law', 'moe-wl-2017:TH', '能用理想气体状态方程分析一定质量气体的压强、体积与温度关系。', '等温压缩时判断压强如何变化', '由两组状态量求出未知的热力学温度'),
    t('thermo_first_law', 'C', '热学', 12, 12, '内能与热力学第一定律', 'First law of thermodynamics', 'moe-wl-2017:TH', '能用热力学第一定律分析做功、热传递引起的物体内能变化。', '说明气体被压缩时内能如何变化', '区分热量、功与内能三个概念'),
    t('thermo_second_intro', 'C', '热学', 12, 12, '热力学第二定律入门', 'Second law intro', 'moe-wl-2017:TH', '知道热量不能自发从低温物体传到高温物体，理解热机效率存在上限。', '解释冰箱为何必须消耗电能', '说明第二类永动机不可能制成'),
    t('simple_harmonic', 'C', '振动与波', 12, 12, '简谐运动', 'Simple harmonic motion', 'moe-wl-2017:WAV', '能写出简谐运动的位移表达式，说明回复力与位移成正比且反向。', '由x=Asinωt读出振幅与周期', '指出弹簧振子在平衡位置加速度为零'),
    t('simple_pendulum', 'P', '振动与波', 12, 12, '单摆', 'Simple pendulum', 'moe-wl-2017:WAV', '能用单摆周期公式测量重力加速度，并说明小角度近似的条件。', '用秒表测三十次全振动求周期', '解释摆长加倍后面周期如何变化'),
    t('mechanical_wave', 'R', '振动与波', 12, 12, '机械波', 'Mechanical waves', 'moe-wl-2017:WAV', '能区分横波与纵波，由波形图读出波长、振幅并判断质点振动方向。', '在给定波形图上标出波长', '由波的传播方向判断某质点下一时刻位移'),
    t('wave_interfere_diffract', 'C', '振动与波', 12, 12, '波的干涉衍射', 'Interference and diffraction', 'moe-wl-2017:WAV', '能陈述波的叠加条件，说明干涉加强减弱和衍射发生的大致条件。', '指出两列波干涉的路程差条件', '解释声波比可见光更容易发生衍射'),
    t('light_refraction', 'P', '振动与波', 12, 12, '光的折射', 'Refraction of light', 'moe-wl-2017:WAV', '能用折射定律计算入射角与折射角，并说明折射率的含义。', '由实验数据验证n等于正弦比', '解释插入水中的筷子看起来弯折'),
    t('light_interference', 'C', '振动与波', 12, 12, '光的干涉', 'Light interference', 'moe-wl-2017:WAV', '能用双缝干涉条纹间距公式分析波长、缝距与屏距对条纹的影响。', '说明红光条纹为何比紫光更疏', '由条纹间距估算光的波长'),
    t('photoelectric_effect', 'C', '近代物理', 12, 12, '光电效应', 'Photoelectric effect', 'moe-wl-2017:MOD', '能用光电效应说明光具有粒子性，解释截止频率与遏止电压的含义。', '说明增大光强为何不一定产生光电子', '由截止频率比较不同金属的逸出功'),
    t('wave_particle_duality', 'C', '近代物理', 12, 12, '波粒二象性', 'Wave-particle duality', 'moe-wl-2017:MOD', '能用德布罗意关系把实物粒子与物质波联系起来，举例说明二象性。', '估算电子德布罗意波长的数量级', '说明电子衍射实验支持物质波'),
    t('atomic_models', 'C', '近代物理', 12, 12, '原子结构模型', 'Atomic models', 'moe-wl-2017:MOD', '能按历史顺序比较汤姆孙、卢瑟福、玻尔原子模型的要点与局限。', '说明α散射如何否定枣糕模型', '指出玻尔模型难以处理多电子原子'),
    t('hydrogen_spectrum', 'R', '近代物理', 12, 12, '氢原子光谱', 'Hydrogen spectrum', 'moe-wl-2017:MOD', '能把氢原子光谱线系与能级跃迁对应起来，并计算相应光子能量。', '指出巴尔末线系对应的能级跃迁', '由能级图计算某条谱线的波长'),
    t('nuclear_decay', 'C', '近代物理', 12, 12, '原子核与衰变', 'Nuclear decay', 'moe-wl-2017:MOD', '能区分α、β、γ衰变，并用质量数和电荷数守恒写出衰变方程。', '写出铀核发生α衰变的方程', '说明半衰期描述的是统计规律'),
    t('mass_energy_intro', 'C', '近代物理', 12, 12, '质能方程入门', 'Mass-energy intro', 'moe-wl-2017:MOD', '能用质能关系说明质量亏损与核能释放的联系，并估算数量级。', '解释裂变释放能量的来源', '比较化学能与核能的数量级差异'),
]
