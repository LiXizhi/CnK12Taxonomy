# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "english", "英语"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_ENGLISH = [
    # 语言技能
    t('listening_inference', 'P', '语言技能', 10, 10, '听力推断', 'Listening inference', 'moe-yy-2017:SK', '能根据语调、措辞和上下文推断说话人态度或未直接说出的信息。', '听对话判断说话人是建议还是抱怨', '说明推断所依据的关键词或语气'),
    t('speech_presentation', 'P', '语言技能', 10, 11, '演讲陈述', 'Speech presentation', 'moe-yy-2017:SK', '能就熟悉话题做两到三分钟英文陈述，含开场、要点和收束。', '完成有提纲的口头陈述', '回答听众提出的一个问题'),
    t('discussion_negotiation', 'P', '语言技能', 10, 11, '讨论协商', 'Discussion and negotiation', 'moe-yy-2017:SK', '能在小组讨论中提出方案、征求意见并达成简单共识。', '用Shall we…提出一项建议', '在协商中转述同伴观点后再回应'),
    t('argumentative_reading', 'P', '语言技能', 10, 11, '阅读议论文', 'Reading argumentative texts', 'moe-yy-2017:SK', '能找出英文议论文的立场、理由和例证，并判断论证是否充分。', '标出作者立场句', '列出两条支撑理由并评价其力度'),
    t('abridged_literature_reading', 'P', '语言技能', 11, 11, '阅读文学简写', 'Reading abridged literature', 'moe-yy-2017:SK', '能读懂简写文学篇章中的人物与情节，并用英文简述冲突。', '用五句话概述故事主线', '描述一位人物的性格并引用原句'),
    t('summary_writing_senior', 'P', '语言技能', 11, 11, '概要写作', 'Summary writing', 'moe-yy-2017:SK', '能用自己的话压缩短文要点，保留关键信息且不加入个人评论。', '把一段短文压缩为约60词概要', '检查概要是否漏掉主题句信息'),
    t('practical_writing_senior', 'P', '语言技能', 11, 12, '应用文写作', 'Practical writing', 'moe-yy-2017:SK', '能按场合撰写通知、申请或回复邮件，格式完整、语气得体。', '写一封活动申请邮件', '根据对象调整称呼和结尾用语'),
    t('continuation_writing', 'P', '语言技能', 11, 12, '读后续写', 'Continuation writing', 'moe-yy-2017:SK', '能依据给定短文续写情节，保持人称、时态和人物逻辑一致。', '续写两段并衔接原文结尾', '检查续写中人物动机是否合理'),
    t('audiovisual_integration', 'P', '语言技能', 12, 12, '视听信息整合', 'Audiovisual integration', 'moe-yy-2017:SK', '能结合视频画面与语音提取要点，用英文整合为一则简短转述。', '边看边记下三个关键信息', '用五句话转述视听材料大意'),
    t('justifying_opinions', 'P', '语言技能', 12, 12, '观点阐释发言', 'Justifying opinions', 'moe-yy-2017:SK', '能用because、for example等组织理由，清楚阐释并捍卫自己的观点。', '就校园话题给出观点和两条理由', '用I see your point但坚持己见作回应'),
    # 语言知识
    t('attributive_clause_review', 'C', '语言知识', 10, 10, '定语从句巩固', 'Attributive clause review', 'moe-yy-2017:LK', '能正确选用关系代词和关系副词，区分限制性与非限制性定语从句。', '合并两句为含who或which的定语从句', '给非限制性从句补上逗号并说明理由'),
    t('nominal_clauses', 'C', '语言知识', 10, 11, '名词性从句', 'Nominal clauses', 'moe-yy-2017:LK', '能识别并运用主语、宾语、表语和同位语从句，注意that与whether的选用。', '用that从句改写一个宾语从句', '判断一句中的从句充当何种句子成分'),
    t('adverbial_clauses_senior', 'C', '语言知识', 10, 11, '状语从句', 'Adverbial clauses', 'moe-yy-2017:LK', '能运用时间、原因、条件、让步等状语从句，并注意时态呼应。', '用although改写两个简单句', '检查条件句中主将从现是否正确'),
    t('nonfinite_verbs', 'C', '语言知识', 11, 11, '非谓语动词', 'Non-finite verbs', 'moe-yy-2017:LK', '能根据句意选用不定式、动名词或分词，避免逻辑主语错误。', '用分词短语改写时间状语从句', '改正Seeing from the hill, the city is beautiful一类错误'),
    t('subjunctive_mood_intro', 'C', '语言知识', 11, 12, '虚拟语气入门', 'Subjunctive mood intro', 'moe-yy-2017:LK', '能在与现在或过去事实相反的条件句中使用基本虚拟结构。', '用If I were…造一句与现在相反的句子', '把真实条件句改为与过去相反的虚拟句'),
    t('word_formation_senior', 'L', '语言知识', 11, 11, '词汇构词', 'Word formation', 'moe-yy-2017:LK', '能借助常见前缀后缀和词根推测词义，并识别词性变化。', '由happy推出unhappy和happiness', '根据后缀判断单词词性'),
    t('cohesion_devices', 'R', '语言知识', 11, 12, '语篇衔接', 'Textual cohesion', 'moe-yy-2017:LK', '能识别指代、连接词和词汇复现等衔接手段，并在写作中选用。', '找出段落中的指代词及其所指', '用however或therefore衔接两句'),
    # 文化知识
    t('festival_custom_compare', 'C', '文化知识', 10, 10, '中外节日习俗比较', 'Comparing festival customs', 'moe-yy-2017:CK', '能用英语比较中外节日在时间、活动和寓意上的异同，避免刻板印象。', '用英语介绍春节与圣诞节各一项习俗', '指出一处表面相似但含义不同的习俗'),
    t('english_speaking_societies', 'C', '文化知识', 11, 11, '英语国家社会文化', 'English-speaking societies', 'moe-yy-2017:CK', '能简述英语国家学校、社区或公共礼仪的常见做法，并举例说明。', '用英语介绍一种英语国家校园礼仪', '说明拜访家庭时可能需要注意的礼貌'),
    t('chinese_culture_in_english', 'P', '文化知识', 11, 12, '中国文化英语表达', 'Expressing Chinese culture in English', 'moe-yy-2017:CK', '能用得体英语介绍一项中国文化元素，让不熟悉该文化的听者听懂。', '用英语介绍端午节或书法', '为文化专有名词准备一句解释'),
    t('intercultural_conflict', 'C', '文化知识', 12, 12, '跨文化冲突化解', 'Resolving intercultural conflict', 'moe-yy-2017:CK', '能识别因文化差异引起的误解，并用英语提出礼貌的澄清或折中办法。', '分析一则因送礼差异引起的误解', '角色扮演中用英语提出折中方案'),
    t('culture_loaded_words', 'L', '文化知识', 12, 12, '文化负载词理解', 'Culture-loaded words', 'moe-yy-2017:CK', '能识别dragon、red等词在中英文化中的不同联想，并在表达中谨慎选用。', '比较一个词在两种文化中的联想', '改写一句可能引起误解的表达'),
    # 学习策略
    t('vocab_memory_strategies', 'M', '学习策略', 10, 11, '词汇记忆策略', 'Vocabulary memory strategies', 'moe-yy-2017:ST', '能选用词根联想、语境例句或间隔复习等方法记忆新词，并检查效果。', '为十个新词各写一个语境例句', '一周后自测并记录仍会的比例'),
    t('listening_speaking_plan', 'M', '学习策略', 11, 11, '听说训练计划', 'Listening and speaking plan', 'moe-yy-2017:ST', '能根据弱项制定一周听说训练计划，并记录完成情况和调整。', '列出本周三次听力练习的材料与时长', '根据记录把一项任务改得更可执行'),
    t('project_based_english', 'M', '学习策略', 12, 12, '项目式英语学习', 'Project-based English learning', 'moe-yy-2017:ST', '能与同伴分工完成一项英语微型项目，并反思过程中的语言收获。', '提交项目分工表和成果', '写一段说明自己负责部分的语言难点'),
    t('metacognitive_monitoring', 'M', '学习策略', 12, 12, '元认知监控', 'Metacognitive monitoring', 'moe-yy-2017:ST', '能在完成任务前后设定目标、检查理解并调整策略，记下有效做法。', '读前写下两个预测问题并在读后核对', '说明一次策略调整为什么更有效'),
    t('reading_strategy_choice', 'M', '学习策略', 11, 12, '阅读策略选择', 'Choosing reading strategies', 'moe-yy-2017:ST', '能根据阅读目的在略读、寻读和细读之间选择，并说明选择理由。', '限时略读后说出主旨', '为细节题改用寻读并标出定位句'),
    t('writing_process_reflection', 'M', '学习策略', 12, 12, '写作过程反思', 'Writing process reflection', 'moe-yy-2017:ST', '能在构思、起草、修改各环节做简短反思，针对一类错误制定改进措施。', '保存一稿和修改稿并标出三处改动', '针对时态错误列出一条检查步骤'),
]
