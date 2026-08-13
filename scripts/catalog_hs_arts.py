# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T

Pfx, Sub = "ys", "艺术"
def t(slug, typ, domain, g0, g1, name, en, std, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, std, desc, *ev)

HS_ARTS = [
    t('hs_music_work_analysis', 'C', '高中音乐', 10, 12, '音乐作品分析', 'Musical work analysis', 'moe-ys-2017:MU', '能从主题、曲式、织体与情绪发展分析一首完整作品，并用术语说明高潮如何形成。', '标出作品的主题再现位置', '用两句话说明力度与速度如何推动情绪'),
    t('hs_multipart_singing', 'P', '高中音乐', 10, 12, '多声部演唱', 'Multipart singing', 'moe-ys-2017:MU', '能在三声部或四声部合唱中稳定本声部音准，控制音量平衡并按指挥进出。', '分声部唱完指定乐段不跟错声部', '弱起进入时与指挥拍点对齐'),
    t('hs_keyboard_guitar_basic', 'P', '高中音乐', 10, 12, '键盘或吉他基础', 'Keyboard or guitar basics', 'moe-ys-2017:MU', '能在键盘或吉他上弹出常用和弦与简单伴奏音型，为熟悉旋律提供和声支持。', '弹奏三种常用和弦转换', '为四句旋律配上简单伴奏'),
    t('hs_short_composition', 'P', '高中音乐', 10, 12, '作曲小品', 'Short composition', 'moe-ys-2017:MU', '能依据给定动机或歌词写出八至十六小节小品，标明调性、节奏并试唱或试奏。', '完成一首可演唱的小品谱面', '说明动机如何发展成乐句'),
    t('hs_chinese_trad_music_deep', 'C', '高中音乐', 10, 12, '中国传统音乐深化', 'Chinese traditional music in depth', 'moe-ys-2017:MU', '能结合一件传统乐器或一种戏曲、民歌体裁，说明其音阶、润腔或演奏特点及文化语境。', '介绍一件民族乐器的音色与技法', '对比两地民歌在旋法上的差异'),
    t('hs_sketch_form_deep', 'P', '高中美术', 10, 12, '素描造型深化', 'Advanced sketch modeling', 'moe-ys-2017:FA', '能用结构线与明暗层次表现静物或石膏的体积、比例与空间关系，并修正透视错误。', '完成一幅有明暗层次的石膏素描', '指出画面中一处透视并改正'),
    t('hs_color_expression', 'P', '高中美术', 10, 12, '色彩表现', 'Color expression', 'moe-ys-2017:FA', '能运用色调、冷暖与补色对比组织画面，表达特定时间或情绪而不只是平涂固有色。', '用限定色调完成一幅色彩写生', '说明主色与点缀色如何服务情绪'),
    t('hs_design_thinking_art', 'M', '高中美术', 10, 12, '设计思维', 'Design thinking in art', 'moe-ys-2017:FA', '能围绕真实使用需求完成调研、构思、原型与反馈迭代，用视觉方案解决一项校园问题。', '提交含用户需求的设计说明', '根据同伴反馈修改一版原型'),
    t('hs_chinese_shuhua_deep', 'P', '高中美术', 10, 12, '中国书画深化', 'Chinese painting and calligraphy in depth', 'moe-ys-2017:FA', '能在毛笔书法或水墨画中控制用笔、墨色与章法，完成一件有题款或印章安排的作品。', '完成一幅有浓淡变化的水墨习作', '说明题款位置如何平衡画面'),
    t('hs_digital_media_paint', 'P', '高中美术', 10, 12, '数字媒体绘画', 'Digital media painting', 'moe-ys-2017:FA', '能用图层、笔刷与色彩调整完成数字插画或海报，并导出适合屏幕与印刷的版本。', '完成一幅分层数字插画', '按用途导出两种分辨率文件'),
    t('hs_drama_rehearsal', 'P', '高中综合艺术', 10, 12, '戏剧排练', 'Drama rehearsal', 'moe-ys-2017:INT', '能在排练中稳定台词、走位与角色关系，根据导演或同伴意见调整表演强度。', '完整演出一场短剧不漏词', '根据一次排练笔记改走位'),
    t('hs_dance_choreo_advance', 'P', '高中综合艺术', 10, 12, '舞蹈编创提高', 'Advanced dance choreography', 'moe-ys-2017:INT', '能围绕主题编创含空间层次与队形变化的短舞，动作动机可重复发展并与音乐结构对应。', '编创一段不少于三十二拍的作品', '画出队形变化并与音乐段落对应'),
    t('hs_short_film_make', 'P', '高中综合艺术', 10, 12, '影视短片制作', 'Short film production', 'moe-ys-2017:INT', '能完成分镜、拍摄与剪辑的微型短片，运用景别、轴线与声音配合叙事。', '提交含分镜的一至三分钟短片', '说明两处剪辑如何服务情节'),
    t('hs_cross_media_exhibit', 'P', '高中综合艺术', 10, 12, '跨媒介展览', 'Cross-media exhibition', 'moe-ys-2017:INT', '能把图像、声音、文本或装置组合成小型展览，撰写说明并规划观众动线。', '布置一组跨媒介展位', '为展品写不超过百字的说明牌'),
    t('hs_art_history_topic', 'C', '高中欣赏与批评', 10, 12, '中外美术史专题', 'Art history topic study', 'moe-ys-2017:AP', '能围绕一个时期或主题比较中外视觉艺术的材料、图像与社会功能，避免简单优劣判断。', '制作一条含五件作品的专题时间轴', '比较两件作品在功能上的差异'),
    t('hs_music_style_contrast', 'C', '高中欣赏与批评', 10, 12, '音乐风格比较', 'Music style comparison', 'moe-ys-2017:AP', '能从节奏、音色、曲式与文化背景比较两种音乐风格，并指出影响其形成的历史条件。', '对照两首作品列出风格特征表', '说明一种风格与其时代语境的联系'),
    t('hs_art_critique_writing', 'L', '高中欣赏与批评', 10, 12, '艺术评论写作', 'Art critique writing', 'moe-ys-2017:AP', '能区分描述、分析、解释与评价，写出结构清楚的短评，论据来自作品本身而非空泛形容词。', '完成一篇不少于三百字的作品短评', '把主观喜好与形式分析分成两段'),
    t('hs_heritage_protection', 'M', '高中欣赏与批评', 10, 12, '文化遗产保护', 'Cultural heritage protection', 'moe-ys-2017:AP', '能说明物质与非物质文化遗产面临的风险，提出尊重原真性的记录、传播或参与保护行动。', '调查一项本地遗产的保存现状', '设计一条不破坏原物的传播方案'),
]
