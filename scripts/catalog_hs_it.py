# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "xxjs", "信息技术"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_IT = [
    t('hs_data_encoding', 'C', '数据与计算', 10, 12, '数据编码', 'Data encoding', 'moe-xxjs-2017:DC', '能说明文字、图像、声音如何被编码为二进制，并比较常见编码与压缩方案的取舍。', '对照一段汉字说明编码单位差异', '比较无损与有损压缩的适用场景'),
    t('hs_algo_describe', 'R', '数据与计算', 10, 12, '算法描述', 'Algorithm description', 'moe-xxjs-2017:DC', '能用自然语言、流程图或伪代码把同一算法表达清楚，并检查输入边界与终止条件。', '为成绩分档画出含判断的流程图', '把流程图改写成可执行伪代码'),
    t('hs_prog_fundamentals', 'P', '数据与计算', 10, 12, '程序设计基础', 'Programming fundamentals', 'moe-xxjs-2017:DC', '能用一种文本语言编写含变量、分支、循环和函数的小程序，完成数据输入与结果输出。', '编写程序统计一组数的均值', '用函数封装重复计算步骤'),
    t('hs_prog_debug', 'P', '数据与计算', 10, 12, '程序调试', 'Program debugging', 'moe-xxjs-2017:DC', '能根据报错与异常输出定位语法或逻辑错误，用断点或打印追踪变量变化并修正程序。', '修复一份含越界错误的程序', '用日志说明错误被定位的过程'),
    t('hs_ct_project', 'P', '数据与计算', 10, 12, '计算思维项目', 'Computational thinking project', 'moe-xxjs-2017:DC', '能把身边问题分解为可计算任务，完成数据采集、算法实现与结果展示的小型项目。', '提交问题分解与算法方案', '演示可运行原型并说明改进点'),
    t('hs_oss_license', 'L', '数据与计算', 10, 12, '开源与许可', 'Open source and licenses', 'moe-xxjs-2017:DC', '能读懂常见开源许可对修改、分发与署名的条款，并在作品说明中正确引用第三方代码。', '查出所用库的许可类型与限制', '在作品说明里写清引用与署名'),
    t('hs_is_components', 'C', '信息系统与社会', 10, 12, '信息系统组成', 'Information system components', 'moe-xxjs-2017:IS', '能从硬件、软件、数据、人员与规程说明信息系统如何协同完成一项业务目标。', '画出校园选课系统组成示意', '指出缺少人员规程时会出现的问题'),
    t('hs_digital_society', 'C', '信息系统与社会', 10, 12, '数字化社会', 'Digital society', 'moe-xxjs-2017:IS', '能举例说明数字化对生产、治理与日常生活的改变，并讨论便利与风险如何并存。', '分析一项本地数字化公共服务', '列出该服务的两项社会风险'),
    t('hs_info_sec_ethics', 'M', '信息系统与社会', 10, 12, '信息安全与伦理', 'Info security and ethics', 'moe-xxjs-2017:IS', '能判断越权访问、泄露数据、传播不实信息等行为的伦理问题，并提出负责任的应对办法。', '分析一个数据泄露案例的责任点', '提出两条校园信息系统使用守则'),
    t('hs_pip_law', 'C', '信息系统与社会', 10, 12, '个人信息保护法规', 'Personal data protection rules', 'moe-xxjs-2017:IS', '能结合收集、存储、使用、删除等环节说明个人信息处理应满足合法、正当、必要等要求。', '指出某应用过度索权的两项问题', '说明用户可行使的查询与删除权利'),
    t('hs_linear_struct', 'C', '数据与结构', 10, 12, '线性结构', 'Linear structures', 'moe-xxjs-2017:DS', '能说明数组、链表、栈、队列的组织方式与典型操作，并选择合适结构解决简单问题。', '用栈解释撤销操作的实现思路', '比较数组与链表插入的代价差异'),
    t('hs_tree_graph_view', 'R', '数据与结构', 10, 12, '树与图直观', 'Trees and graphs intuitively', 'moe-xxjs-2017:DS', '能用树表示层级关系、用图表示网络关系，并读懂遍历顺序与可达路径的直观含义。', '把班级组织画成树并标出根节点', '在交通图上指出一条可达路径'),
    t('hs_search_sort_impl', 'P', '数据与结构', 10, 12, '查找与排序实现', 'Search and sort implementation', 'moe-xxjs-2017:DS', '能实现顺序查找、二分查找及一种常见排序，并用比较次数说明效率差异。', '对有序表实现二分查找函数', '统计两种排序的比较次数差异'),
    t('hs_db_query_basics', 'P', '数据与结构', 10, 12, '数据库基础', 'Database query basics', 'moe-xxjs-2017:DS', '能设计简单二维表并完成增删改查，说明主键与字段约束如何保证数据一致。', '建立图书借阅表并完成条件查询', '解释主键重复为何会被拒绝'),
    t('hs_net_architecture', 'C', '网络基础', 10, 12, '网络体系结构', 'Network architecture', 'moe-xxjs-2017:NET', '能用分层观点说明主机、交换机、路由器如何协作完成端到端通信。', '画出一次网页访问经过的主要设备', '说明各层大致负责的通信任务'),
    t('hs_proto_address', 'L', '网络基础', 10, 12, '协议与地址', 'Protocols and addresses', 'moe-xxjs-2017:NET', '能准确使用IP地址、MAC地址、域名等术语，并说明常见协议如何约定数据格式。', '查看本机地址并说明公私网区别', '对照说明请求与响应的基本字段名'),
    t('hs_web_api_client', 'P', '网络基础', 10, 12, '网页与API', 'Web pages and APIs', 'moe-xxjs-2017:NET', '能制作简单网页并调用公开接口获取数据，理解请求参数、返回格式与密钥保护。', '用页面展示一次接口返回结果', '说明令牌不应写入公开代码仓库'),
    t('hs_iot_entry', 'P', '网络基础', 10, 12, '物联网入门', 'IoT introduction', 'moe-xxjs-2017:NET', '能说明感知、传输、处理环节如何组成物联网，并完成数据采集上报的入门实验。', '描述智能门锁的数据流向', '完成一次传感器数据上传演示'),
    t('hs_ml_intuition', 'C', '人工智能初步', 10, 12, '机器学习直观', 'Machine learning intuition', 'moe-xxjs-2017:AI', '能用从样例中归纳规律说明机器学习与传统规则程序的差别，并识别分类、回归等任务类型。', '把垃圾邮件过滤说成分类任务', '指出规则写死与模型学习的差异'),
    t('hs_train_test_sets', 'P', '人工智能初步', 10, 12, '训练与测试集', 'Train and test sets', 'moe-xxjs-2017:AI', '能划分训练集与测试集，解释为何不能用训练样本评价泛化，并观察过拟合的直观现象。', '按比例划分一份标注数据', '比较训练集准确率与测试集差异'),
    t('hs_ai_app_cases', 'C', '人工智能初步', 10, 12, '智能应用', 'Intelligent applications', 'moe-xxjs-2017:AI', '能分析语音识别、推荐、辅助驾驶等应用的输入输出与局限，并提出合理使用边界。', '拆解一项校园智能应用的模块', '说明该应用在何种条件下会失效'),
    t('hs_ai_ethics_norm', 'M', '人工智能初步', 10, 12, '人工智能伦理', 'AI ethics', 'moe-xxjs-2017:AI', '能讨论算法偏见、隐私、深度伪造与责任归属，提出使用生成式工具时应遵守的课堂规范。', '分析一个偏见或伪造案例', '起草三条课堂智能工具使用约定'),
]
