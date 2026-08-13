# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from topiclib import T


Pfx = "ys"
Sub = "艺术"

def st(g):
    if g <= 2:
        return 1
    if g <= 4:
        return 2
    if g <= 6:
        return 3
    return 4

def ys(code, g):
    return f'moe-ys-2022:{code}.S{st(g)}'

def a(slug, typ, domain, code, g0, g1, name, en, desc, *ev):
    return T(Pfx, Sub, slug, typ, domain, g0, g1, name, en, ys(code, g0), desc, *ev)

ARTS = [
    a('singing_breath', 'P', '音乐', 'MU', 1, 2, '歌唱呼吸', 'Singing breath', '能用自然呼吸支持短句歌唱，声音放松。', '跟唱四句不喊嗓', '体会深吸气慢呼气'),
    a('steady_beat_clap', 'P', '音乐', 'MU', 1, 2, '稳定拍击', 'Steady beat', '能用手或脚稳定击拍，保持匀速。', '随歌曲击拍不出错', '区分快慢两种拍速'),
    a('high_low_pitch', 'C', '音乐', 'MU', 1, 2, '音高辨别', 'High and low pitch', '能听辨并模仿高音与低音，感知旋律走向。', '指出旋律上行下行', '用嗓音模仿高低音'),
    a('rhythm_echo', 'P', '音乐', 'MU', 1, 2, '节奏模仿', 'Rhythm echo', '能模仿教师敲击的简单节奏型。', '复现四拍节奏型', '与同伴对敲节奏'),
    a('nursery_song_sing', 'P', '音乐', 'MU', 1, 2, '儿歌演唱', 'Nursery songs', '能完整演唱学过的儿歌并吐字清楚。', '独立唱完一首儿歌', '加入简单动作表演'),
    a('instrument_sound_perceive', 'C', '音乐', 'MU', 1, 2, '乐器音色感知', 'Instrument sounds', '能分辨鼓、铃、弦乐等不同音色。', '闭眼辨三种乐器', '描述音色特点'),
    a('listening_concentration', 'M', '音乐', 'MU', 1, 2, '专注聆听', 'Listening focus', '能在音乐活动中保持安静专注聆听。', '聆听后回答两个问题', '不打断他人表演'),
    a('classroom_instruments', 'P', '音乐', 'MU', 3, 4, '课堂乐器', 'Classroom instruments', '能使用打击乐或竖笛等演奏简单片段。', '用打击乐合奏四小节', '竖笛吹奏三个音'),
    a('two_part_singing', 'P', '音乐', 'MU', 3, 4, '简单合唱', 'Two-part singing', '能在合唱中保持自己的声部不跑调。', '分声部唱完一段', '倾听其他声部'),
    a('note_duration', 'C', '音乐', 'MU', 3, 4, '音符时值', 'Note duration', '知道全音符、二分、四分音符的相对长短。', '用手势表示时值', '读简单节奏谱'),
    a('melody_line_shape', 'C', '音乐', 'MU', 3, 4, '旋律线条', 'Melody shape', '能描述旋律的起伏并用手势画出线条。', '画出熟悉旋律线', '说明高潮音位置'),
    a('tempo_dynamics', 'C', '音乐', 'MU', 3, 4, '速度与力度', 'Tempo and dynamics', '理解快板慢板、强弱的表达作用。', '用不同力度唱同一句', '说明慢板适合什么情绪'),
    a('rhythm_instrument_make', 'P', '音乐', 'MU', 3, 4, '自制节奏乐器', 'DIY rhythm', '用日常材料制作简单打击乐器并演奏。', '制作沙锤并演奏', '说明发声原理'),
    a('music_notation_intro', 'R', '音乐', 'MU', 5, 6, '简谱识读', 'Notation reading', '能识读简谱中的音高、节奏并试唱。', '视唱四句简谱', '找出最高音'),
    a('choral_blend', 'P', '音乐', 'MU', 5, 6, '合唱融合', 'Choral blend', '在合唱中控制音量、音色与同伴协调。', '合唱时音色统一', '弱声演唱不丢音准'),
    a('composer_work_intro', 'C', '音乐', 'MU', 5, 6, '作曲家与作品', 'Composer works', '了解一位中国或外国作曲家及其代表片段。', '介绍聂耳与义勇军进行曲', '描述作品情绪'),
    a('ensemble_cooperation', 'P', '音乐', 'MU', 5, 6, '小合奏配合', 'Ensemble', '在合奏中看指挥、对准节奏并控制音量。', '小乐队完成一段', '进拍与同伴一致'),
    a('music_improvisation', 'P', '音乐', 'MU', 5, 6, '即兴表现', 'Improvisation', '能根据给定动机即兴敲击或演唱短句。', '即兴四小节节奏', '即兴哼唱动机'),
    a('vocal_health', 'M', '音乐', 'MU', 7, 9, '嗓音保健', 'Vocal health', '知道不大声喊叫、充足饮水等护嗓方法。', '列出三条护嗓习惯', '演唱后不做伤嗓行为'),
    a('harmony_basics', 'C', '音乐', 'MU', 7, 9, '和声基础', 'Harmony basics', '能听辨主和弦与简单和声色彩。', '分辨协和与不协和', '为旋律配简单和声'),
    a('music_style_compare', 'C', '音乐', 'MU', 7, 9, '音乐风格比较', 'Music styles', '能比较民歌、艺术歌曲、流行等风格差异。', '举例两种音乐风格', '说明乐器编配差异'),
    a('creative_melody', 'P', '音乐', 'MU', 7, 9, '旋律创编', 'Melody creation', '能为给定歌词或节奏创编短旋律。', '创编四小节旋律', '演唱并记录简谱'),
    a('line_drawing_shape', 'P', '美术', 'FA', 1, 2, '线条与形状', 'Line and shape', '能用线条画出圆形、方形等基本形状组合。', '画一件文具的轮廓', '线条连贯闭合'),
    a('color_primary_mix', 'C', '美术', 'FA', 1, 2, '原色与混合', 'Primary colors', '知道红、黄、蓝原色及简单混色结果。', '调出橙色与绿色', '指出三原色'),
    a('warm_cool_colors', 'C', '美术', 'FA', 1, 2, '冷暖色感受', 'Warm cool colors', '能区分冷暖色并表达不同感觉。', '用冷色画夜晚', '用暖色画太阳'),
    a('collage_paper', 'P', '美术', 'FA', 1, 2, '纸材拼贴', 'Paper collage', '能撕剪彩纸拼贴出简单形象。', '完成一幅拼贴画', '画面有主次'),
    a('composition_center', 'C', '美术', 'FA', 3, 4, '画面构图', 'Composition', '理解主体居中或三分法等基本构图。', '调整主体位置更均衡', '说明留白作用'),
    a('shading_light', 'C', '美术', 'FA', 3, 4, '明暗与体积', 'Light and shade', '能用简单明暗表现物体体积感。', '画球体加阴影', '说明光源方向'),
    a('watercolor_wash', 'P', '美术', 'FA', 3, 4, '水彩晕染', 'Watercolor wash', '能控制水分完成由深到浅的渐变晕染。', '完成天空渐变', '避免纸面搓毛'),
    a('printmaking_basic', 'P', '美术', 'FA', 3, 4, '版画初体验', 'Printmaking', '能完成简单刻印或拓印作品。', '拓印清晰图案', '注意安全用刀'),
    a('pattern_design', 'P', '美术', 'FA', 3, 4, '纹样设计', 'Pattern design', '能设计重复纹样并用于装饰。', '设计二方连续纹样', '用于边框装饰'),
    a('craft_material_explore', 'P', '美术', 'FA', 3, 4, '材料探索', 'Material explore', '尝试黏土、纤维等不同材料造型。', '用黏土做小动物', '说明材料特性'),
    a('art_safety_tools', 'M', '美术', 'FA', 3, 4, '美术工具安全', 'Art tool safety', '正确使用剪刀、颜料并保持整洁。', '演示剪刀传递方法', '活动后清理桌面'),
    a('sketch_observation', 'P', '美术', 'FA', 5, 6, '素描观察', 'Sketch observation', '能观察物体比例并用线条写生。', '素描静物有比例', '区分近大远小'),
    a('color_mixed_gray', 'C', '美术', 'FA', 5, 6, '色彩混合', 'Color mixing', '能调出生灰与复色并用于表现。', '调出三种复色', '说明互补色关系'),
    a('chinese_painting_basics', 'P', '美术', 'FA', 5, 6, '中国画入门', 'Chinese painting', '体验毛笔、水墨画简单花鸟或山水元素。', '画竹叶或山石', '控制墨浓淡'),
    a('calligraphy_strokes', 'P', '美术', 'FA', 5, 6, '书法基本笔画', 'Calligraphy strokes', '能练习横、竖、撇、捺等基本笔画。', '书写八个基本笔画', '坐姿执笔正确'),
    a('design_poster', 'P', '美术', 'FA', 5, 6, '海报设计', 'Poster design', '能结合主题设计图文并茂的海报。', '完成活动海报', '标题醒目易读'),
    a('sculpture_form', 'P', '美术', 'FA', 5, 6, '立体造型', 'Sculpture form', '能用纸、线等材料创建立体作品。', '完成立体纸雕塑', '作品多角度有看点'),
    a('seal_carving_intro', 'P', '美术', 'FA', 7, 9, '篆刻初识', 'Seal carving intro', '了解篆刻工具与朱文白文，完成简单练习。', '刻制姓名印', '说明印面布局'),
    a('digital_drawing', 'P', '美术', 'FA', 7, 9, '数字绘画', 'Digital drawing', '能用简单软件完成分层绘画或涂色。', '完成数字插画', '保存并导出作品'),
    a('perspective_one_point', 'C', '美术', 'FA', 7, 9, '一点透视', 'One-point perspective', '理解消失点概念并画简单空间。', '画走廊透视图', '标注消失点'),
    a('landscape_sketch_outdoor', 'P', '美术', 'FA', 7, 9, '户外写生', 'Outdoor sketch', '能在户外观察并完成风景速写。', '完成校园风景速写', '概括远近景'),
    a('dance_basic_steps', 'P', '综合艺术', 'INT', 1, 2, '舞蹈基本步', 'Dance steps', '能跟随节奏完成简单舞蹈步伐。', '学跳八拍舞蹈', '动作与节拍一致'),
    a('body_expression', 'P', '综合艺术', 'INT', 1, 2, '身体表达', 'Body expression', '用动作表现高兴、安静等情绪。', '用动作表现三种情绪', '与同伴镜像模仿'),
    a('drama_role_play', 'P', '综合艺术', 'INT', 3, 4, '戏剧角色扮演', 'Drama role play', '能在短剧中扮演角色并清晰台词。', '完成一分钟角色表演', '使用简单道具'),
    a('story_tableau', 'P', '综合艺术', 'INT', 3, 4, '故事定格', 'Story tableau', '用静态造型表现故事中的关键瞬间。', '小组定格三个场景', '观众猜出情节'),
    a('creative_costume', 'P', '综合艺术', 'INT', 3, 4, '简易服饰设计', 'Creative costume', '用材料设计表演用简易服饰或头饰。', '制作角色头饰', '服饰符合角色'),
    a('dance_choreography', 'P', '综合艺术', 'INT', 5, 6, '舞蹈编创', 'Dance choreography', '能为短音乐编创简单队形与动作。', '编创十六拍舞蹈', '队形变换整齐'),
    a('shadow_puppet_intro', 'P', '综合艺术', 'INT', 5, 6, '皮影初体验', 'Shadow puppet', '了解皮影原理并操作简单影人。', '操作皮影讲故事', '制作简易影人'),
    a('video_storyboard', 'P', '综合艺术', 'INT', 5, 6, '分镜绘制', 'Storyboard', '能为短故事绘制简单分镜脚本。', '绘制四格分镜', '标注镜头说明'),
    a('film_shot_basics', 'C', '综合艺术', 'INT', 7, 9, '镜头语言初识', 'Film shots', '知道远景、近景、特写等镜头作用。', '识别三种镜头', '用平板拍不同景别'),
    a('multimedia_artwork', 'P', '综合艺术', 'INT', 7, 9, '多媒体作品', 'Multimedia art', '能结合图像、声音完成小型综合展示。', '制作图文音短片', '说明创意来源'),
    a('stage_light_sound', 'C', '综合艺术', 'INT', 7, 9, '舞台声光', 'Stage light sound', '了解舞台灯光、音响对氛围的影响。', '描述两种灯光效果', '说明音效与情节关系'),
    a('cross_art_project', 'P', '综合艺术', 'INT', 7, 9, '跨学科艺术项目', 'Cross-art project', '能合作完成含音乐、美术、表演的综合项目。', '完成班级艺术展演', '分工明确协作'),
    a('listen_describe_music', 'M', '欣赏与文化', 'AP', 1, 2, '听音乐描述', 'Listen and describe', '能听后说出快慢、强弱等感受。', '描述一首摇篮曲特点', '说出喜欢的理由'),
    a('artwork_appreciation', 'M', '欣赏与文化', 'AP', 1, 2, '画作欣赏', 'Art appreciation', '能观察画作颜色、主体并表达感受。', '描述一幅儿童画', '说出最吸引的细节'),
    a('festival_spring_art', 'C', '欣赏与文化', 'AP', 1, 2, '春节艺术', 'Spring Festival art', '了解春联、剪纸、年画等春节艺术形式。', '识别春联上下联', '完成简单剪纸'),
    a('lantern_festival_art', 'C', '欣赏与文化', 'AP', 1, 2, '元宵艺术', 'Lantern Festival', '了解灯笼、汤圆等与元宵相关的艺术元素。', '制作简易灯笼', '说出元宵习俗'),
    a('folk_song_intro', 'C', '欣赏与文化', 'AP', 3, 4, '民歌欣赏', 'Folk songs', '能欣赏本地或民族民歌并了解背景。', '学唱一句民歌', '说明民歌与生活关系'),
    a('masterwork_visual', 'C', '欣赏与文化', 'AP', 3, 4, '名画欣赏', 'Masterwork visual', '欣赏中外经典绘画并描述构图色彩。', '描述清明上河图局部', '说出作品时代'),
    a('opera_mask_intro', 'C', '欣赏与文化', 'AP', 3, 4, '戏曲脸谱', 'Opera masks', '了解脸谱颜色象征并欣赏片段。', '匹配脸谱颜色含义', '观看戏曲片段'),
    a('mid_autumn_art', 'C', '欣赏与文化', 'AP', 3, 4, '中秋艺术', 'Mid-Autumn art', '了解与中秋相关的诗词、音乐和视觉艺术。', '朗诵中秋诗词', '画月亮相关主题'),
    a('national_anthem_etiquette', 'M', '欣赏与文化', 'AP', 3, 6, '国歌礼仪', 'Anthem etiquette', '奏国歌时立正肃立，理解其庄严意义。', '演示奏国歌礼仪', '说明国歌历史背景'),
    a('world_music_listen', 'C', '欣赏与文化', 'AP', 5, 6, '世界音乐', 'World music', '能欣赏非洲鼓、西方古典等不同文化音乐。', '比较两种世界音乐', '说明使用乐器'),
    a('architecture_appreciate', 'C', '欣赏与文化', 'AP', 5, 6, '建筑欣赏', 'Architecture', '欣赏中外典型建筑的形式与功能。', '描述故宫或金字塔特点', '说明建筑与地域关系'),
    a('intangible_heritage', 'C', '欣赏与文化', 'AP', 5, 6, '非遗艺术', 'Intangible heritage', '了解一项本地或国家级非遗艺术形式。', '介绍一项非遗项目', '说明传承意义'),
    a('heritage_craft_try', 'P', '欣赏与文化', 'AP', 5, 6, '非遗技艺体验', 'Heritage craft', '在指导下体验一项传统手工艺基本步骤。', '体验剪纸或编织', '说明工艺难点'),
    a('museum_etiquette', 'M', '欣赏与文化', 'AP', 5, 6, '美术馆礼仪', 'Museum etiquette', '参观时保持安静、不触摸展品并尊重作品。', '列出参观三条守则', '向同伴介绍一件展品'),
    a('aesthetic_criteria', 'M', '欣赏与文化', 'AP', 7, 9, '审美标准', 'Aesthetic criteria', '能从主题、形式、技法等角度简评艺术作品。', '写五十字作品短评', '区分个人喜好与评价'),
    a('cultural_identity_art', 'C', '欣赏与文化', 'AP', 7, 9, '艺术与文化认同', 'Cultural identity', '理解艺术在表达民族文化与身份中的作用。', '举例艺术表达文化', '讨论传统与创新'),
    a('comparative_art_history', 'C', '欣赏与文化', 'AP', 7, 9, '中外艺术比较', 'Art history compare', '能比较不同时期中外艺术风格特点。', '比较明清绘画与文艺复兴', '制作简易时间轴'),
    a('art_reflection_journal', 'M', '欣赏与文化', 'AP', 7, 9, '艺术学习反思', 'Art reflection', '能记录学习过程并设定改进目标。', '写艺术学习周记', '展示前后作品对比'),
    a('art_exhibition_curate', 'M', '欣赏与文化', 'AP', 7, 9, '班级艺术展', 'Class exhibition', '能策划布置班级艺术展示并撰写说明。', '布置一面作品墙', '为作品写标题说明'),
    a('drumming_patterns', 'P', '音乐', 'MU', 3, 4, '鼓点型练习', 'Drumming patterns', '能模仿并演奏简单二拍、四拍鼓点型。', '合奏四小节鼓点', '保持节奏稳定'),
    a('color_wheel_theory', 'C', '美术', 'FA', 5, 6, '色环关系', 'Color wheel', '理解邻近色、对比色关系并用于配色。', '制作简易色环', '用对比色完成小画'),
    a('drama_improv', 'P', '综合艺术', 'INT', 5, 6, '即兴戏剧', 'Drama improv', '能根据提示即兴表演短场景。', '完成一分钟即兴', '与同伴自然接台词'),
    a('folk_dance_intro', 'P', '综合艺术', 'INT', 3, 4, '民族舞蹈体验', 'Folk dance', '能学习简单民族舞蹈动作并了解背景。', '学跳八拍民族舞', '说出舞蹈所属民族'),
    a('clay_sculpture', 'P', '美术', 'FA', 5, 6, '泥塑造型', 'Clay sculpture', '能用泥材捏塑人物或动物基本形。', '完成一件泥塑作品', '控制湿度防止开裂'),
    a('dragon_boat_festival_art', 'C', '欣赏与文化', 'AP', 3, 4, '端午艺术', 'Dragon Boat art', '了解龙舟、粽子等与端午相关的艺术形式。', '绘制龙舟简图', '听端午相关音乐'),
]
