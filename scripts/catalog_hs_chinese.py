# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "chinese", "语文"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_CHINESE = [
    # 整本书阅读与研讨
    t('whole_book_annotation', 'P', '整本书阅读与研讨', 10, 10, '整本书批注阅读', 'Whole-book annotation', 'moe-yw-2017:TG1', '能按章节为一部长篇作品做批注，标出人物关系、情节转折和疑问。', '为指定章节写下不少于五处批注', '用人物关系图梳理主要角色'),
    t('whole_book_seminar', 'L', '整本书阅读与研讨', 10, 11, '整本书研讨发言', 'Whole-book seminar talk', 'moe-yw-2017:TG1', '能在研讨中依据文本细节陈述观点，并回应同学的不同解读。', '发言时引用两处原文', '针对同学观点提出一个追问'),
    t('whole_book_review', 'P', '整本书阅读与研讨', 11, 12, '整本书读后评论', 'Whole-book review essay', 'moe-yw-2017:TG1', '能就整本书的主题或人物写出有理据的短评，避免只讲情节梗概。', '完成八百字左右的读后评论', '用具体情节支撑对人物的判断'),
    # 当代文化参与
    t('local_culture_fieldwork', 'P', '当代文化参与', 10, 11, '社区文化调查', 'Local culture fieldwork', 'moe-yw-2017:TG2', '能围绕身边文化现象拟定调查问题，记录见闻并整理成简要报告。', '完成一次访谈或观察记录', '在报告中区分事实描述与个人看法'),
    t('culture_phenomenon_comment', 'P', '当代文化参与', 11, 12, '当代文化评说', 'Commenting on contemporary culture', 'moe-yw-2017:TG2', '能就校园或社会文化现象写出有立场的短评，并说明依据与限度。', '选定一个文化现象写出三百字评说', '口头向小组陈述评说要点'),
    # 跨媒介阅读与交流
    t('cross_media_comparison', 'M', '跨媒介阅读与交流', 10, 11, '跨媒介信息比较', 'Cross-media comparison', 'moe-yw-2017:TG3', '能比较同一事件在文字、图像或音视频中的呈现差异，指出信息侧重。', '列出两种媒介各自强调的信息', '说明一处因媒介形式造成的理解差异'),
    t('multimodal_presentation', 'P', '跨媒介阅读与交流', 11, 12, '多媒介表达交流', 'Multimodal presentation', 'moe-yw-2017:TG3', '能综合文字、图片或短视频完成一次主题交流，并说明媒介选择理由。', '完成一份含图文的展示稿', '口头说明为何选用某种媒介'),
    # 语言积累梳理与探究
    t('classical_particle_sorting', 'L', '语言积累梳理与探究', 10, 10, '文言虚词梳理', 'Classical particle sorting', 'moe-yw-2017:TG4', '能整理常见文言虚词在课文中的用法，并用自己的话说明差异。', '为“之”“其”各整理两种用法', '用课文例句给虚词做分类卡片'),
    t('register_and_diction', 'C', '语言积累梳理与探究', 10, 11, '词语语体探究', 'Register and diction', 'moe-yw-2017:TG4', '能辨析书面语与口语、庄重与通俗的词语差异，并在表达中选用得体。', '把一段口语改写成书面表达', '指出一处用词不得体并改正'),
    t('language_phenomenon_inquiry', 'M', '语言积累梳理与探究', 11, 12, '语言现象专题', 'Language phenomenon inquiry', 'moe-yw-2017:TG4', '能就网络用语、成语活用等一种语言现象搜集例子并作简要探究。', '收集不少于五个相关用例', '写出该现象适用场合与误用风险'),
    # 文学阅读与写作
    t('fiction_close_reading', 'R', '文学阅读与写作', 10, 10, '小说细读人物', 'Fiction close reading', 'moe-yw-2017:TG5', '能通过对话、细节和叙述角度分析小说人物，并说明性格如何显现。', '圈出三处塑造人物的细节', '写一段人物短评并引用原文'),
    t('poetry_imagery_imitation', 'P', '文学阅读与写作', 10, 11, '诗歌意象仿写', 'Poetry imagery imitation', 'moe-yw-2017:TG5', '能识别诗中核心意象及其情感指向，并据此完成一首仿写或扩写。', '标出诗中两个关键意象', '完成一首保留原意象的仿写'),
    t('prose_craft_analysis', 'R', '文学阅读与写作', 11, 11, '散文笔法赏析', 'Prose craft analysis', 'moe-yw-2017:TG5', '能指出散文中的线索、修辞或句式安排，并说明它们如何形成韵味。', '找出全文线索并画出结构提纲', '赏析一处修辞并说明表达效果'),
    t('literary_piece_writing', 'P', '文学阅读与写作', 11, 12, '文学性片段写作', 'Literary piece writing', 'moe-yw-2017:TG5', '能运用描写、抒情或叙述写出有画面感的文学片段，并自行修改用语。', '完成四百字左右的文学片段', '根据同伴意见修改一处表达'),
    # 思辨性阅读与表达
    t('claim_evidence_mapping', 'C', '思辨性阅读与表达', 10, 11, '论点论据梳理', 'Claim-evidence mapping', 'moe-yw-2017:TG6', '能从议论性文本中抽出中心论点和支撑论据，并判断论据是否对题。', '用提纲标出论点与三条论据', '指出一处论据与论点不匹配'),
    t('reasoning_gap_spotting', 'M', '思辨性阅读与表达', 11, 11, '论证漏洞识别', 'Spotting reasoning gaps', 'moe-yw-2017:TG6', '能识别以偏概全、偷换概念等常见推理问题，并说明原文何处失当。', '在短文中标出一处推理漏洞', '用自己的话解释该漏洞为何不成立'),
    t('reasoned_oral_argument', 'L', '思辨性阅读与表达', 11, 12, '思辨性口头表达', 'Reasoned oral argument', 'moe-yw-2017:TG6', '能就争议话题作有层次的口头陈述，先亮明立场再回应反方要点。', '作两分钟有立场的发言', '回应同学反驳时引用一条理由'),
    # 实用性阅读与交流
    t('practical_text_extraction', 'P', '实用性阅读与交流', 10, 10, '实用文本提取', 'Practical text extraction', 'moe-yw-2017:TG7', '能从通知、说明书或报道中提取关键信息，并按任务转述给他人。', '从一则通知中列出时间地点要求', '把说明书步骤转述成口头说明'),
    t('speech_script_writing', 'P', '实用性阅读与交流', 10, 11, '演讲稿撰写', 'Speech script writing', 'moe-yw-2017:TG7', '能按开场、主体、收束撰写面向听众的演讲稿，语言适合口头表达。', '完成一篇八百字左右演讲稿', '朗读时标出停顿与重音'),
    t('interview_and_report', 'P', '实用性阅读与交流', 11, 12, '访谈与书面报告', 'Interview and written report', 'moe-yw-2017:TG7', '能拟定访谈提纲、记录回答，并整理成结构清楚的书面报告。', '设计不少于五个访谈问题', '把访谈记录改写成分段报告'),
    # 中华传统文化经典研习
    t('preqin_prose_study', 'R', '中华传统文化经典研习', 10, 11, '先秦散文研读', 'Pre-Qin prose study', 'moe-yw-2017:TG8', '能疏通一篇先秦散文的关键语句，概括其说理层次并记下疑难。', '用现代汉语翻译指定段落', '画出说理层次并标注关键词'),
    t('tang_song_poetry_study', 'R', '中华传统文化经典研习', 11, 11, '唐宋诗词研习', 'Tang-Song poetry study', 'moe-yw-2017:TG8', '能结合注释理解一首唐宋诗词的意象与情感，并作简要札记。', '为诗中两处典故写出注释大意', '用札记说明诗人情感如何层层推进'),
    t('classic_commentary_notes', 'P', '中华传统文化经典研习', 11, 12, '经典札记写作', 'Classic commentary notes', 'moe-yw-2017:TG8', '能就一篇经典选段写下读书札记，记录字词、章法或思想要点。', '完成一则三百字札记', '在札记中区分字词解释与个人体会'),
    # 中国革命传统作品研习
    t('revolutionary_narrative', 'R', '中国革命传统作品研习', 11, 11, '革命叙事研读', 'Revolutionary narrative reading', 'moe-yw-2017:TG9', '能梳理革命传统作品中的事件与人物选择，说明叙述如何体现信念。', '列出主要事件时间线', '引用一处细节说明人物抉择'),
    t('revolutionary_theme_writing', 'P', '中国革命传统作品研习', 11, 12, '革命传统主题写作', 'Revolutionary theme writing', 'moe-yw-2017:TG9', '能结合作品写一篇有感而发的短文，把历史情境与今日思考联系起来。', '完成一篇读后感并引用原文', '在小组中朗读并说明写作意图'),
    # 中国现当代作家作品研习
    t('modern_fiction_author', 'R', '中国现当代作家作品研习', 10, 11, '现代小说作家研读', 'Modern fiction author study', 'moe-yw-2017:TG10', '能就一位现代小说家的选篇分析叙事方式和人物处境，并做读书卡片。', '为选篇列出叙事视角与时间安排', '制作一张作家作品卡片含代表作'),
    t('contemporary_prose_study', 'R', '中国现当代作家作品研习', 11, 12, '当代散文研习', 'Contemporary prose study', 'moe-yw-2017:TG10', '能抓住当代散文的思想线索与语言个性，写出有针对性的评点。', '标出全文思想转折处', '写一段评点说明语言个性'),
    t('author_style_compare', 'M', '中国现当代作家作品研习', 12, 12, '作家风格比较', 'Author style comparison', 'moe-yw-2017:TG10', '能比较两位现当代作家在题材或笔法上的差异，并举作品实例说明。', '列出两位作家各两条风格特征', '用对照表呈现具体例句'),
    # 外国作家作品研习
    t('foreign_novel_excerpt', 'R', '外国作家作品研习', 11, 12, '外国小说选篇研读', 'Foreign novel excerpt study', 'moe-yw-2017:TG11', '能阅读外国小说选篇，梳理文化背景中的人物冲突，并做讨论发言。', '概括选篇中的主要冲突', '讨论时说明一处需要背景知识才能理解的细节'),
    t('foreign_poetry_drama', 'R', '外国作家作品研习', 12, 12, '外国诗歌戏剧研习', 'Foreign poetry and drama study', 'moe-yw-2017:TG11', '能借助注释阅读外国诗歌或戏剧片段，抓住台词或意象表达的情感。', '朗读一段台词并说明语气', '为诗中一个意象写出理解札记'),
    # 科学与文化论著研习
    t('science_essay_reading', 'C', '科学与文化论著研习', 11, 12, '科学论著节选阅读', 'Science essay reading', 'moe-yw-2017:TG12', '能抓住科学论著节选的核心命题和论证步骤，用自己的话转述大意。', '列出文中的核心命题', '把一段论证改写成三条要点'),
    t('cultural_treatise_notes', 'P', '科学与文化论著研习', 12, 12, '文化论著读书笔记', 'Cultural treatise notes', 'moe-yw-2017:TG12', '能就文化论著节选做分层笔记，区分作者观点、例证和自己的疑问。', '用三栏笔记记录观点例证疑问', '就一个疑问写出准备继续查证的方向'),
]
