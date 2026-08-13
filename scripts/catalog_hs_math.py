# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "math", "数学"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_MATH = [
    # 预备知识
    t('set_notation', 'C', '预备知识', 10, 10, '集合的表示', 'Set notation', 'moe-sx-2017:PRE', '能用列举法或描述法表示集合，判断给定对象是否属于该集合。', '用列举法写出小于5的正整数集', '判断3是否属于{x|x>4}并说明理由'),
    t('set_operations', 'P', '预备知识', 10, 10, '集合的交并补', 'Set operations', 'moe-sx-2017:PRE', '会求两个集合的交集、并集和补集，并能用韦恩图表示运算结果。', '求{1,2,3}与{2,3,4}的交与并', '在韦恩图上标出补集对应区域'),
    t('logic_connectives', 'L', '预备知识', 10, 10, '常用逻辑用语', 'Logical connectives', 'moe-sx-2017:PRE', '能正确使用且、或、非以及全称、存在量词表述简单数学命题。', '把“x>0且x<2”改写成集合语言', '指出“存在x使x²=-1在实数中”的真假'),
    t('inequality_properties', 'C', '预备知识', 10, 10, '不等式的性质', 'Inequality properties', 'moe-sx-2017:PRE', '能运用不等式的基本性质比较大小，并解简单一元一次不等式。', '比较a>b时a+c与b+c的大小', '解不等式2x-1>5并在数轴上表示'),
    # 函数
    t('function_concept_graph', 'R', '函数', 10, 10, '函数概念与图像', 'Function concept and graph', 'moe-sx-2017:FN', '能用对应关系理解函数，根据解析式列表描点画出函数图像并读关键点。', '判断一组对应是否构成函数', '根据图像读出指定自变量的函数值'),
    t('power_function', 'C', '函数', 10, 10, '幂函数', 'Power functions', 'moe-sx-2017:FN', '认识幂函数y=x^α的几种常见情形，能比较它们在第一象限的增减与过点。', '画出y=x、y=x²、y=√x的草图', '指出哪个幂函数过点(4,2)'),
    t('exponential_function', 'C', '函数', 10, 10, '指数函数', 'Exponential functions', 'moe-sx-2017:FN', '理解指数函数y=a^x(a>0,a≠1)的定义，能根据底数判断增减并画出草图。', '比较y=2^x与y=(1/2)^x的单调性', '求2^x=8时x的值'),
    t('logarithmic_function', 'C', '函数', 10, 10, '对数函数', 'Logarithmic functions', 'moe-sx-2017:FN', '理解对数函数与指数函数的互逆关系，能求简单对数值并画出y=log_a x草图。', '把2^3=8改写成对数形式', '指出y=log_2 x的定义域和过点'),
    t('function_monotonicity', 'C', '函数', 10, 10, '函数的单调性', 'Monotonicity of functions', 'moe-sx-2017:FN', '能用定义判断函数在区间上的增减，并结合图像说明单调区间。', '用定义证明f(x)=x+1在R上递增', '根据图像写出函数的单调区间'),
    t('function_parity', 'C', '函数', 10, 10, '函数的奇偶性', 'Even and odd functions', 'moe-sx-2017:FN', '能根据f(-x)与f(x)的关系判断奇偶性，并说明图像关于原点或y轴对称。', '判断f(x)=x³是奇函数还是偶函数', '由奇偶性补全图像的另一半'),
    t('function_zeros', 'P', '函数', 10, 11, '函数的零点', 'Zeros of functions', 'moe-sx-2017:FN', '理解函数零点与方程根、图像横轴交点的对应，能用二分法求近似零点。', '指出二次函数图像与x轴交点对应的零点', '对连续变号区间做一次二分并说明理由'),
    t('trig_definition', 'C', '函数', 11, 11, '三角函数定义', 'Trigonometric definitions', 'moe-sx-2017:FN', '能在单位圆上用有向角定义正弦、余弦、正切，并求特殊角的三角函数值。', '在单位圆上标出2π/3对应的点', '求sin(5π/6)和cos(π)的值'),
    t('trig_reduction_formulas', 'P', '函数', 11, 11, '诱导公式', 'Reduction formulas', 'moe-sx-2017:FN', '能用诱导公式把任意角的三角函数化为锐角三角函数并求值。', '用诱导公式求cos(13π/6)', '把sin(π-α)化成sin α并说明依据'),
    t('sine_cosine_graphs', 'R', '函数', 11, 11, '正余弦图像', 'Sine and cosine graphs', 'moe-sx-2017:FN', '能画出y=sin x、y=cos x的图像，读出周期、最值和五点对应关系。', '用五点法画出y=sin x在一个周期内的图像', '从图像读出y=cos x的最大值与周期'),
    t('trig_identities', 'P', '函数', 11, 11, '三角恒等变换', 'Trigonometric identities', 'moe-sx-2017:FN', '能运用同角关系、和差角与倍角公式化简三角式并求值。', '化简sin²α+cos²α+2sinαcosα', '用倍角公式求cos(π/8)的值'),
    t('solving_triangles', 'P', '函数', 11, 11, '解三角形', 'Solving triangles', 'moe-sx-2017:FN', '能用正弦定理、余弦定理解斜三角形，并根据已知元素判断解的情况。', '已知两边夹角求第三边', '用正弦定理解SSA情形并说明是否两解'),
    t('sequence_concept', 'C', '函数', 11, 11, '数列的概念', 'Sequences', 'moe-sx-2017:FN', '理解数列是定义在正整数集上的函数，能写出通项并求指定项。', '根据前几项写出一个可能的通项', '由通项a_n=2n-1求第10项'),
    t('arithmetic_sequence', 'P', '函数', 11, 11, '等差数列', 'Arithmetic sequences', 'moe-sx-2017:FN', '掌握等差数列的通项与前n项和公式，能求公差、项数与指定和。', '已知首项和公差写通项', '求1到100中所有奇数之和'),
    t('geometric_sequence', 'P', '函数', 11, 11, '等比数列', 'Geometric sequences', 'moe-sx-2017:FN', '掌握等比数列的通项与前n项和公式，能处理公比为1与不为1的情形。', '已知首项和公比求第6项', '求等比数列前n项和并讨论q=1'),
    t('derivative_intuition', 'C', '函数', 11, 12, '导数的直观', 'Derivative intuition', 'moe-sx-2017:FN', '能把导数理解为瞬时变化率，并用切线斜率解释函数在一点附近的变化。', '说明位移对时间的导数表示瞬时速度', '根据切线倾斜程度比较两点导数大小'),
    t('derivative_rules', 'P', '函数', 11, 12, '导数的运算', 'Derivative rules', 'moe-sx-2017:FN', '会求多项式、指数、对数及简单复合函数的导数。', '求f(x)=x³-2x的导函数', '求y=e^{2x}在x=0处的导数'),
    t('derivative_extrema', 'P', '函数', 11, 12, '导数与极值', 'Derivatives and extrema', 'moe-sx-2017:FN', '能用导数判断单调性，求函数的极值和给定区间上的最值。', '根据f′(x)的符号写出单调区间', '求二次函数在闭区间上的最大值'),
    # 几何与代数
    t('solid_geometry_views', 'R', '几何与代数', 10, 10, '立体几何直观', 'Solid geometry intuition', 'moe-sx-2017:GA', '能识别棱柱、棱锥、圆柱、圆锥、球的结构特征，并画出简单直观图。', '画出正方体的斜二测直观图', '指出三视图对应的几何体'),
    t('space_incidence', 'C', '几何与代数', 10, 10, '空间点线面位置', 'Points lines and planes in space', 'moe-sx-2017:GA', '能判断空间中点、直线、平面的位置关系，并用符号正确表述。', '判断正方体中两条面对角线是否共面', '用符号表示直线在平面内或与平面相交'),
    t('line_plane_parallel', 'C', '几何与代数', 10, 11, '线面平行', 'Line-plane parallelism', 'moe-sx-2017:GA', '能用线面平行的判定与性质说明直线与平面、平面与平面平行。', '在正方体中找出与给定棱平行的面', '用判定定理证明一条棱与对面平行'),
    t('line_plane_perpendicular', 'C', '几何与代数', 10, 11, '线面垂直', 'Line-plane perpendicularity', 'moe-sx-2017:GA', '能用线面垂直的判定与性质说明直线与平面、平面与平面垂直。', '说明桌腿与桌面垂直的判定条件', '在正方体中指出互相垂直的两个面'),
    t('space_vectors', 'C', '几何与代数', 11, 11, '空间向量', 'Space vectors', 'moe-sx-2017:GA', '能在空间直角坐标系中表示向量，进行加减与数乘，并求模长。', '写出点A(1,2,3)对应的位置向量', '计算向量(1,0,2)与(0,3,-1)的和与模'),
    t('planar_dot_product', 'C', '几何与代数', 11, 11, '平面向量数量积', 'Planar dot product', 'moe-sx-2017:GA', '理解平面向量数量积的几何意义，能用它求夹角和判断垂直。', '计算两个已知坐标向量的数量积', '由数量积为0判断两向量垂直'),
    t('complex_numbers', 'C', '几何与代数', 11, 11, '复数', 'Complex numbers', 'moe-sx-2017:GA', '理解复数的代数形式与复平面表示，能进行加减乘除并指出实部虚部。', '计算(2+3i)+(1-i)并标在复平面', '求(1+i)(1-i)并指出结果是实数'),
    t('line_equations', 'P', '几何与代数', 11, 11, '直线的方程', 'Equations of lines', 'moe-sx-2017:GA', '能根据点斜、斜截、两点等条件写出直线方程，并求两直线交点与夹角。', '过点(1,2)斜率为3写点斜式方程', '求y=2x+1与x+y=4的交点'),
    t('circle_equations', 'P', '几何与代数', 11, 11, '圆的方程', 'Equations of circles', 'moe-sx-2017:GA', '能写出圆的标准方程和一般方程，判断点与圆、直线与圆的位置关系。', '写出圆心(0,0)半径2的圆方程', '判断直线y=x与x²+y²=2相交切或离'),
    t('ellipse', 'C', '几何与代数', 12, 12, '椭圆', 'Ellipse', 'moe-sx-2017:GA', '理解椭圆的定义与标准方程，能求a、b、c、离心率并画出草图。', '由焦点和长轴写出椭圆方程', '指出椭圆x²/9+y²/4=1的顶点'),
    t('hyperbola', 'C', '几何与代数', 12, 12, '双曲线', 'Hyperbola', 'moe-sx-2017:GA', '理解双曲线的定义与标准方程，能求渐近线并区分焦点在哪条轴上。', '写出x²/16-y²/9=1的渐近线', '比较椭圆与双曲线离心率的范围'),
    t('parabola', 'C', '几何与代数', 12, 12, '抛物线', 'Parabola', 'moe-sx-2017:GA', '理解抛物线的定义与标准方程，能由焦点或准线写出方程并画草图。', '由焦点(1,0)写出开口向右的抛物线方程', '指出y²=4x的准线方程'),
    # 概率与统计
    t('sampling_methods', 'P', '概率与统计', 12, 12, '随机抽样深化', 'Sampling methods', 'moe-sx-2017:PS', '能根据总体特点选择简单随机、分层或系统抽样，并说明样本代表性。', '为全校分层抽样设计各层人数', '比较方便抽样与随机抽样的差异'),
    t('sample_estimate_population', 'P', '概率与统计', 12, 12, '用样本估计总体', 'Estimating population from samples', 'moe-sx-2017:PS', '能用样本频率分布、均值和方差估计总体相应特征，并讨论估计波动。', '根据频率分布直方图估计总体均值', '比较两组样本方差说明哪组更分散'),
    t('conditional_probability', 'C', '概率与统计', 12, 12, '条件概率', 'Conditional probability', 'moe-sx-2017:PS', '理解条件概率的含义，能用公式或树状图计算简单条件概率。', '已知抽到红球后再抽到白球的概率', '用树状图表示两步试验的条件概率'),
    t('discrete_random_variable', 'C', '概率与统计', 12, 12, '离散随机变量', 'Discrete random variables', 'moe-sx-2017:PS', '能列出简单离散随机变量的分布列，并求期望与方差。', '写出掷一枚硬币一次的分布列', '根据分布列计算期望值'),
    t('normal_curve_intuition', 'R', '概率与统计', 12, 12, '正态分布直观', 'Normal distribution intuition', 'moe-sx-2017:PS', '认识正态曲线的钟形对称特征，能用均值和标准差描述数据的大致分布。', '指出正态曲线最高点对应的均值', '说明标准差变大时曲线如何变扁'),
    t('linear_regression', 'P', '概率与统计', 12, 12, '线性回归', 'Linear regression', 'moe-sx-2017:PS', '能根据散点图判断线性相关，求回归直线并用于粗略预测。', '根据散点图判断是否大致线性相关', '用回归直线预测一个新的自变量对应值'),
    # 数学建模
    t('function_modeling_task', 'M', '数学建模', 12, 12, '函数建模活动', 'Function modeling activity', 'moe-sx-2017:MD', '能针对实际变化问题选择函数类型建模、求解并检验模型是否合理。', '为气温随时间变化选择合适函数类型', '用实际数据检验模型预测误差'),
    t('stats_modeling_task', 'M', '数学建模', 12, 12, '统计建模活动', 'Statistics modeling activity', 'moe-sx-2017:MD', '能提出统计问题、采集或整理数据、建立统计模型并报告结论与局限。', '设计一项校园调查并说明抽样方法', '根据模型结论提出一条可检验的建议'),
]
