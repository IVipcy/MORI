# static_qa_data.py - 静的なQ&Aデータと文脈に応じた提案機能（挿し友禅職人 MORI版）

# ==========================================
# 挿し友禅職人MORI向けQ&Aデータ（言語別）
# ==========================================

# ====================================================================
# 🎯 メディアデータ（画像・動画・リンク）- CERA版に準拠
# ====================================================================
# 注意: 疑問符（？）はget_qa_media関数で自動正規化されるため不要

qa_media_data = {
    # 日本語版
    "挿し友禅って何": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/suggestion1.png",
                "caption": "挿し友禅で色を挿した着物じゃよ",
                "alt": "京友禅の美しい着物"
            }
        ]
    },
    
    "どんな道具を使うの": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/suggestion2.jpg",
                "caption": "挿し友禅で使う筆や刷毛じゃ",
                "alt": "挿し友禅の道具"
            }
        ]
    },
    
    "ぼかしってどうやるの": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/suggstion3.png",
                "caption": "ぼかしの技法で仕上げた模様じゃよ",
                "alt": "ぼかし技法"
            }
        ]
    },
    
    # 英語版
    "What is Sashi-Yuzen": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/suggestion1.png",
                "caption": "Kimono with Sashi-Yuzen coloring!",
                "alt": "Beautiful Kyo-Yuzen kimono"
            }
        ]
    },
    
    "What tools do you use": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/suggestion2.jpg",
                "caption": "Brushes used in Sashi-Yuzen",
                "alt": "Sashi-Yuzen tools"
            }
        ]
    },
    
    "How do you do bokashi": {
        "images": [
            {
                "url": "/static/media/kyoyuzen/suggstion3.png",
                "caption": "Pattern finished with bokashi technique!",
                "alt": "Bokashi technique"
            }
        ]
    },
} 

qa_responses = {
    'ja': {
        # Phase1: 挿し友禅の概要・基本
        'phase1_overview': {
            "挿し友禅って何": """
                挿し友禅っていうのはな、着物の模様に筆や刷毛で手作業で色を挿していく工程のことじゃよ。「色挿し」とも呼ばれておるんじゃ。
                
                友禅染の中で最も絵画的で華やかな部分を担当しておってな、この工程があるから京友禅は美しい色彩を持つようになるんじゃ。
                
                わしは先祖代々この仕事をやっておるんじゃが、色を「挿す」から「差す」...つまり「刺す」じゃなくて良かったのう！痛くないからな。ハハハ！
                [EMOTION:happy]
            """,
            
            "どんな道具を使うの": """
                主に使うのは筆と刷毛じゃな。あとは染料を調合するための器や、乾燥を早めるための電熱器も使うんじゃ。
                
                筆の種類もいろいろあってな、細かい部分には小さい筆、広い面には大きい刷毛を使い分けるんじゃよ。
                
                道具は大切にしておるから、毎日手入れするんじゃ。筆は洗ってから乾かして、形を整えておくんじゃよ。筆を大事にせんと「フデ」がいのう、なんちゃって！ハハハ！
                [EMOTION:happy]
            """,
            
            "京友禅の特徴は": """
                京友禅は日本の伝統的な染色技法で、華やかで多彩な色使いが特徴じゃよ。
                
                江戸時代から続く技術でな、一枚の着物を作るのに何人もの職人が関わるんじゃ。わしは色を挿す担当じゃな。
                
                他の染色技法と比べて、繊細な色の表現ができるのが京友禅の魅力じゃと思うんじゃ。「友禅」と「有線」...どっちも繋がりが大事じゃのう！ハハハ！
                [EMOTION:neutral]
            """
        },
        
        # Phase2: 技術詳細の掘り下げ
        'phase2_technical': {
            "ぼかしってどうやるの": """
                ぼかしはな、模様の外側から内側にかけて徐々に色を薄くしていく技法じゃよ。
                
                水を含ませた筆で染料の境界を優しくなぞっていくとな、自然なグラデーションになるんじゃ。力加減が難しくて、最初は失敗したこともあったのう。
                
                ぼかしがうまくいくと、立体感が出て模様が生き生きするから、一番気を使う部分じゃな。ぼかしの技術は「ボカ」っとしとったらダメじゃぞ！集中が大事じゃ！ハハハ！
                [EMOTION:happy]
            """,
            
            "色が混ざらないのはなぜ": """
                それは「糸目糊」っていう技法のおかげじゃよ。模様の輪郭に糊で細い線を引いておくとな、隣り合う色が混ざらないんじゃ。
                
                糸目糊はわしがやる前の工程で、別の職人さんがやってくれるんじゃよ。まるで線画みたいに見えてな、その中にわしが色を塗っていく感じじゃ。
                
                この糸目糊があるから、京友禅は鮮やかな色分けができるんじゃな。糸目糊様様じゃ！「糊」だけに、この技術は「ノリ」に乗っておるのう！ハハハ！
                [EMOTION:happy]
            """,
            
            "染料の調合で工夫していることは": """
                染料の調合はレシピみたいなものがあるんじゃが、同じ分量でも微妙に違う色になることがあるんじゃよ。
                
                じゃから毎回、小さい布で試し染めをして色を確認するんじゃ。補色を少し混ぜて深みを出したり、「サビ」をつけることもあるんじゃよ。
                
                淡い色には「具入り」という技法で、量感を与えることもあるんじゃ。色の世界は奥が深いのう。染料を「染めりょう」と読むのは...やめとくかのう。ハハハ！
                [EMOTION:happy]
            """,
            
            "乾燥の工夫について教えて": """
                染料を挿した後はな、できるだけ早く乾燥させないと色がにじんじゃうんじゃよ。
                
                じゃから友禅机の下に電熱器を置いて、布を熱で炙りながら作業することが多いんじゃ。特に湿度が高い日は気をつけるんじゃよ。
                
                乾燥のタイミングを見極めるのも、経験が必要じゃな。焦りすぎると色が変わっちゃうこともあるんじゃ。乾燥は「カン」が大事じゃ！「乾燥」だけに！なんちゃって！ハハハ！
                [EMOTION:happy]
            """,
        },
        
        # Phase3: パーソナルな部分
        'phase3_personal': {
            "職人として一番苦労したことは": """
                最初の頃は、色の濃淡を均一に保つのが本当に難しかったんじゃよ。同じ色を何度も作ろうとしても、微妙に違う色になっちゃうんじゃ。
                
                先輩に何度も教えてもらって、手の動かし方や力加減を覚えたんじゃ。今でも難しい模様に出会うと緊張するが、それが楽しくもあるんじゃよ。
                
                一枚の着物を完成させるのに何ヶ月もかかるから、根気が必要な仕事じゃな。でも出来上がった時の達成感は最高じゃ。苦労の「クロウ」は「黒う」...いや、色んな色を使う仕事じゃから苦労も「色々」じゃのう！ハハハ！
                [EMOTION:happy]
            """,
            
            "仕事以外で好きなことは": """
                実はな、日曜日にテニスをするのが楽しみなんじゃよ！
                
                挿し友禅の仕事はずっと細かい作業でな、気づいたら肩がガチガチになっとるんじゃ。テニスで体を動かすと、体も心もスッキリするんじゃよ。
                
                あと毎朝6時半に起きてコーヒーを淹れるのが日課じゃな。8時には小学校の交通安全の旗振りもやっとるんじゃ。地域の子どもたちの安全を守るのも大事な仕事じゃからのう。テニスは「点に酢」...いや、それは意味不明じゃな。ハハハ！
                [EMOTION:happy]
            """,
            
            "京友禅の魅力を一言で言うと": """
                「手仕事の温かさ」じゃな。機械では出せない、人の手が生み出す柔らかさや個性があるんじゃよ。
                
                一つ一つの着物が唯一無二で、作り手の想いが込められておるのが京友禅の魅力じゃと思うんじゃ。
                
                わしの座右の銘は「着る人の気持ちになって作る」ことと「自分の仕事に満足せずいつまでも勉強」じゃな。あと10年は健康で頑張りたいもんじゃ。伝統を守りながら、若い感性も取り入れていきたいのう。「魅力」の「ミリョク」で「見りょく」...見てくれる人がおるから頑張れるんじゃ！ハハハ！
                [EMOTION:happy]
            """,
            
            "嬉しかったことは": """
                いろいろあるんじゃが、やっぱり自分の作品が雑誌に載った時は嬉しかったのう！
                
                あとな、着物を買ってくれた人が「こんな素敵な着物をありがとう」って写真を送ってくれることがあるんじゃよ。それを見ると、この仕事をやっててよかったなぁと思うんじゃ。
                
                発表会で賞を受賞した時も嬉しかったのう。でも一番は、お客さんが喜んでくれることじゃな。「嬉しい」が「う・れ・し・い」...4文字じゃな。職人歴40年以上のわしには10倍嬉しいってことじゃ！ハハハ！
                [EMOTION:happy]
            """,
        }
    },
    
    'en': {
        # Phase1: Overview & Basics
        'phase1_overview': {
            "What is Sashi-Yuzen": """
                Sashi-Yuzen is the process of applying colors to kimono patterns by hand using brushes and spatulas. It's also called "color insertion."
                
                This is the most artistic and vibrant part of Yuzen dyeing, and this process is what gives Kyo-Yuzen its beautiful colors.
                
                My family has been doing this work for generations. The characters for "sashi" mean "insert" - good thing it's not "stab"! Hahaha!
                [EMOTION:happy]
            """,
            
            "What tools do you use": """
                Mainly brushes and spatulas. I also use containers for mixing dyes and electric heaters to speed up drying.
                
                There are many types of brushes - small brushes for detailed areas and large spatulas for wide surfaces.
                
                I take good care of my tools, cleaning them every day. Brushes are washed, dried, and reshaped. A craftsman without good tools is like a joke without a punchline - it just doesn't work! Hahaha!
                [EMOTION:happy]
            """,
            
            "What are the characteristics of Kyo-Yuzen": """
                Kyo-Yuzen is a traditional Japanese dyeing technique characterized by gorgeous and colorful designs.
                
                This technique has been passed down since the Edo period, and many craftspeople work together to create a single kimono. I'm in charge of color insertion.
                
                Compared to other dyeing techniques, the delicate color expression is what makes Kyo-Yuzen attractive. You could say it's "dye-namite"! Hahaha!
                [EMOTION:neutral]
            """
        },
        
        # Phase2: Technical Details
        'phase2_technical': {
            "How do you do bokashi": """
                Bokashi is a technique that gradually lightens the color from the outside to the inside of a pattern.
                
                Gently tracing the dye boundary with a water-soaked brush creates a natural gradation. The pressure control is difficult, and I failed at first too.
                
                When bokashi works well, it creates depth and makes the pattern come alive, so it's the part I'm most careful about. You can't be "blurry" about bokashi! Hahaha!
                [EMOTION:happy]
            """,
            
            "Why don't the colors mix": """
                That's thanks to a technique called "itome-nori" (rice paste resist lines). Drawing thin lines with paste on the pattern outlines prevents adjacent colors from mixing.
                
                Itome-nori is done by another craftsperson before my work. It looks like a line drawing, and I color inside it.
                
                This itome-nori is what allows Kyo-Yuzen to have such vivid color separation. The paste really "sticks" to its job! Hahaha!
                [EMOTION:happy]
            """,
            
            "What do you focus on when mixing dyes": """
                Dye mixing has recipes, but even with the same amounts, the color can turn out slightly different.
                
                So every time, I test dye on a small piece of fabric to check the color. I sometimes add a bit of complementary color for depth, or add "sabi" (aging effect).
                
                For light colors, I use a technique called "gu-iri" to give them more body. The world of color is deep. You could say I'm "dyeing" to learn more every day! Hahaha!
                [EMOTION:happy]
            """,
            
            "Tell me about drying techniques": """
                After applying the dye, I need to dry it as quickly as possible or the color will bleed.
                
                So I often place an electric heater under the yuzen table and work while heating the fabric. I'm especially careful on humid days.
                
                Judging the right timing for drying also requires experience. If I rush too much, the color can change. Good drying is all about "timing" - you can't just "air" your grievances about it! Hahaha!
                [EMOTION:happy]
            """,
        },
        
        # Phase3: Personal
        'phase3_personal': {
            "What was your biggest challenge as a craftsperson": """
                At first, keeping the color intensity uniform was really difficult. Even when trying to make the same color multiple times, it would turn out slightly different.
                
                With repeated teaching from my seniors, I learned how to move my hands and control pressure. Even now, I get nervous when I encounter difficult patterns, but that's also fun.
                
                It takes months to complete a single kimono, so it's work that requires patience. But the sense of accomplishment when it's finished is the best. Hard work is "colorful" in many ways! Hahaha!
                [EMOTION:happy]
            """,
            
            "What do you like to do besides work": """
                Actually, I play tennis on Sundays! That's my fun time!
                
                You know, doing detailed work all day makes my shoulders super stiff. Tennis helps me feel refreshed in body and mind!
                
                I also wake up at 6:30 every morning to make coffee. At 8, I do traffic safety patrol for the elementary school kids. Protecting local children is important work too. Tennis is a "racket" I'm happy to be involved in! Hahaha!
                [EMOTION:happy]
            """,
            
            "What's the charm of Kyo-Yuzen in one word": """
                "The warmth of handmade work." There's a softness and individuality created by human hands that machines can't produce.
                
                Each kimono is unique, and the maker's feelings are put into it - that's the charm of Kyo-Yuzen I think.
                
                My motto is "Make it with the wearer in mind" and "Never be satisfied, always keep learning." I want to keep working healthily for at least 10 more years. "Charm" and "arm" sound similar - the arm that makes kimono creates the charm! Hahaha!
                [EMOTION:happy]
            """,
            
            "What made you happiest": """
                There are many things, but seeing my work featured in magazines was really wonderful!
                
                Also, sometimes customers who bought my kimono send photos saying "Thank you for this beautiful kimono." When I see those, I feel glad I do this work.
                
                Winning awards at exhibitions was also great. But the happiest thing is seeing customers smile. "Happy" has two P's - double the positivity! Hahaha!
                [EMOTION:happy]
            """,
        }
    }
}

# サジェスチョン（言語別・Phase別）
suggestions = {
    'ja': {
        'phase1_overview': [
            "挿し友禅って何？",
            "どんな道具を使うの？",
            "京友禅の特徴は？"
        ],
        'phase2_technical': [
            "ぼかしってどうやるの？",
            "色が混ざらないのはなぜ？",
            "染料の調合で工夫していることは？",
            "乾燥の工夫について教えて",
        ],
        'phase3_personal': [
            "職人として一番苦労したことは？",
            "仕事以外で好きなことは？",
            "京友禅の魅力を一言で言うと？",
            "嬉しかったことは？"
        ]
    },
    'en': {
        'phase1_overview': [
            "What is Sashi-Yuzen?",
            "What tools do you use?",
            "What are the characteristics of Kyo-Yuzen?"
        ],
        'phase2_technical': [
            "How do you do bokashi?",
            "Why don't the colors mix?",
            "What do you focus on when mixing dyes?",
            "Tell me about drying techniques",
        ],
        'phase3_personal': [
            "What was your biggest challenge as a craftsperson?",
            "What do you like to do besides work?",
            "What's the charm of Kyo-Yuzen in one word?",
            "What made you happiest?"
        ]
    }
}

# ==========================================
# 汎用関数（MORI用）
# ==========================================

# ==========================================
# CERA版互換関数（application.pyとの互換性確保）
# ==========================================

def get_qa_by_user_type(user_type='business'):
    """
    ユーザータイプに応じたQ&Aデータを返す（CERA版互換）
    MORI版では言語別のみなので、日本語版を返す
    
    Args:
        user_type: 'business' または 'student'（MORI版では未使用）
    
    Returns:
        dict: Q&Aデータ
    """
    # MORI版は言語別のみなので、日本語版を返す
    return qa_responses.get('ja', {})

def get_suggestions_by_user_type(user_type='business'):
    """
    ユーザータイプに応じたサジェスチョンデータを返す（CERA版互換）
    MORI版では言語別のみなので、日本語版を返す
    
    Args:
        user_type: 'business' または 'student'（MORI版では未使用）
    
    Returns:
        dict: サジェスチョンデータ
    """
    # MORI版は言語別のみなので、日本語版を返す
    return suggestions.get('ja', {})

def get_current_phase(selected_count):
    """
    選択されたサジェスチョン数から現在のPhaseを判定（CERA版準拠）
    
    Args:
        selected_count: 選択されたサジェスチョン数
    
    Returns:
        str: 現在のPhase ('phase1_overview', 'phase2_technical', 'phase3_personal')
    """
    # Phase1: 3個、Phase2: 4個、Phase3: それ以降
    if selected_count < 3:  # 0, 1, 2 → Phase1
        return 'phase1_overview'
    elif selected_count < 7:  # 3, 4, 5, 6 → Phase2
        return 'phase2_technical'
    else:  # 7以上 → Phase3
        return 'phase3_personal'

def get_suggestions_for_phase(phase, selected_suggestions=None, user_type='default', language='ja'):
    """
    Phaseに応じたサジェスチョンを取得（CERA版完全互換 + 自動Phase遷移）
    
    Args:
        phase: 現在のPhase
        selected_suggestions: 既に選択されたサジェスチョンのリスト（デフォルト: []）
        user_type: ユーザータイプ（CERA版: 'business'/'student', MORI版: 'default'）
        language: 言語 ('ja' or 'en', MORI版で使用）
    
    Returns:
        list: サジェスチョンのリスト（最大3個、CERA版準拠）
        
    Note:
        現在のPhaseでサジェスチョンが空の場合、自動的に次のPhaseから取得を試みます
    """
    import random
    
    # selected_suggestionsがNoneの場合は空リストに
    if selected_suggestions is None:
        selected_suggestions = []
    
    # Phase順序（フォールバック用）
    phase_order = ['phase1_overview', 'phase2_technical', 'phase3_personal']
    
    # 現在のPhaseのインデックスを取得
    try:
        current_phase_index = phase_order.index(phase)
    except ValueError:
        current_phase_index = 0
        phase = phase_order[0]
    
    # 重複排除用
    selected_lower = {s.lower().strip() for s in selected_suggestions}
    
    # 現在のPhaseから順に試行
    for try_phase in phase_order[current_phase_index:]:
        # サジェスチョンデータを取得
        if user_type in ['business', 'student']:
            suggestions_data = get_suggestions_by_user_type(user_type)
            phase_suggestions = suggestions_data.get(try_phase, [])
        else:
            # MORI版: 言語別サジェスチョン
            lang_suggestions = suggestions.get(language, suggestions['ja'])
            phase_suggestions = lang_suggestions.get(try_phase, [])
        
        # 選択済みを除外
        available = [s for s in phase_suggestions if s.lower().strip() not in selected_lower]
        
        # サジェスチョンがあれば返す
        if available:
            if try_phase != phase:
                print(f"📋 Phase自動遷移: {phase} → {try_phase} (前のPhaseが空のため)")
            
            # 3個以下の場合はそのまま返す
            if len(available) <= 3:
                return available
            
            # ランダムに3個選択（CERA版互換）
            return random.sample(available, 3)
    
    # 全Phaseで空の場合は空リストを返す
    print(f"⚠️ 全Phaseでサジェスチョンが空です")
    return []

def get_suggestions_for_stage(stage, selected_suggestions=None, language='ja'):
    """
    Stageに応じたサジェスチョンを取得（get_suggestions_for_phaseのエイリアス）
    application.pyの一部で"stage"という名称が使われているため互換性確保
    
    Args:
        stage: 現在のStage（Phaseと同義）
        selected_suggestions: 既に選択されたサジェスチョンのリスト（デフォルト: []）
        language: 言語 ('ja' or 'en')
    
    Returns:
        list: サジェスチョンのリスト
    """
    # get_suggestions_for_phaseを呼び出す
    return get_suggestions_for_phase(stage, selected_suggestions, language=language)

def get_response_for_user(message=None, user_type='default', current_phase='phase1_overview', language='ja', query=None, phase=None):
    """
    ユーザーのメッセージに対する応答を取得（MORI用 + CERA版完全互換）
    
    Args:
        message: ユーザーのメッセージ（MORI版）
        user_type: ユーザータイプ（CERA版では'business'/'student'、MORI版では'default'）
        current_phase: 現在のPhase（MORI版）
        language: 言語 ('ja' or 'en')
        query: ユーザーの質問（CERA版互換用）
        phase: Phaseキー（CERA版互換用）
    
    Returns:
        str or None: 応答テキスト（CERA版と同じく文字列を返す）
                     感情タグは[EMOTION:xxx]形式で含まれている
    """
    # CERA版互換: queryパラメータをサポート
    if query is not None:
        message = query
    
    # CERA版互換: phaseパラメータをサポート
    if phase is not None:
        current_phase = phase
    
    # メッセージがない場合はNoneを返す
    if not message:
        return None
    
    # 正規化（小文字化、空白削除、疑問符削除）
    normalized_message = message.lower().replace(' ', '').replace('　', '').replace('？', '').replace('?', '')
    
    # MORI版: 言語別のQ&Aデータ
    # CERA版: ユーザータイプ別のQ&Aデータ
    if user_type in ['business', 'student']:
        # CERA版との互換性: ユーザータイプ別Q&A（日本語版のみ対応）
        qa_data = get_qa_by_user_type(user_type)
    else:
        # MORI版: 言語別Q&A
        lang_qa = qa_responses.get(language, qa_responses['ja'])
        qa_data = lang_qa
    
    # 現在のPhaseのQ&Aデータを取得
    phase_qa = qa_data.get(current_phase, {}) if current_phase else {}
    
    # 指定Phase内で検索
    if phase_qa:
        for key, response in phase_qa.items():
            # キーも同様に正規化（疑問符を削除）
            normalized_key = key.lower().replace(' ', '').replace('　', '').replace('？', '').replace('?', '')
            if normalized_key in normalized_message or normalized_message in normalized_key:
                # CERA版互換: 文字列を直接返す（感情タグは[EMOTION:xxx]形式で含まれる）
                return response
    
    # 全Phase横断検索
    for phase_name, qa_dict in qa_data.items():
        for key, response in qa_dict.items():
            # キーも同様に正規化（疑問符を削除）
            normalized_key = key.lower().replace(' ', '').replace('　', '').replace('？', '').replace('?', '')
            if normalized_key in normalized_message or normalized_message in normalized_key:
                # CERA版互換: 文字列を直接返す（感情タグは[EMOTION:xxx]形式で含まれる）
                return response
    
    return None

def parse_response(response_text):
    """
    応答テキストから感情タグを抽出
    
    Args:
        response_text: 応答テキスト
    
    Returns:
        dict: {'text': str, 'emotion': str}
    """
    import re
    
    # [EMOTION:xxx] タグを検索
    emotion_match = re.search(r'\[EMOTION:(\w+)\]', response_text)
    emotion = emotion_match.group(1) if emotion_match else 'neutral'
    
    # テキストから感情タグを削除
    clean_text = re.sub(r'\[EMOTION:\w+\]', '', response_text).strip()
    
    return {
        'text': clean_text,
        'emotion': emotion
    }

def get_qa_media(question):
    """
    質問に紐付くメディアデータを取得（CERA版準拠）
    
    Args:
        question (str): 質問テキスト
        
    Returns:
        dict or None: メディアデータ、存在しない場合はNone
    """
    if not question or not qa_media_data:
        return None
    
    # 完全一致チェック（最も高速）
    if question in qa_media_data:
        print(f"📷 メディアヒット（完全一致）: {question}")
        return qa_media_data[question]
    
    # 正規化して完全一致チェック
    question_normalized = question.replace('?', '').replace('？', '').strip()
    
    for key in qa_media_data.keys():
        key_normalized = key.replace('?', '').replace('？', '').strip()
        if question_normalized == key_normalized:
            print(f"📷 メディアヒット（正規化一致）: {key}")
            return qa_media_data[key]
    
    # 部分一致チェック（フォールバック）
    question_lower = question_normalized.lower().replace(' ', '').replace('　', '')
    
    for key, media_data in qa_media_data.items():
        key_lower = key.replace('?', '').replace('？', '').strip().lower().replace(' ', '').replace('　', '')
        
        # キーワードマッチング
        if key_lower in question_lower or question_lower in key_lower:
            # メディアがある場合のみ返す
            if media_data.get('images') or media_data.get('videos') or media_data.get('link'):
                print(f"📷 メディアヒット（部分一致）: {key}")
                return media_data
    
    return None
