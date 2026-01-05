# static_qa_data.py - 静的なQ&Aデータと文脈に応じた提案機能（金彩職人 MORI版）

# ==========================================
# 金彩職人MORI向けQ&Aデータ（言語別）
# ========================================== 

qa_responses = {
    'ja': {
        # Phase1: 金彩の概要・基本
        'phase1_overview': {
            "金彩って何": """
                わしがやっとる金彩っていうのはな、着物に金をキラキラ貼り付ける仕事じゃよ。
                
                例えばな、友禅染めで綺麗な花を描いたとするじゃろ？でもそれだけじゃちょっと寂しい感じなんじゃ。そこに金をちょいっと貼るとな、パーッと華やかになるんじゃよ！まるでお化粧するみたいじゃから「化粧係」って呼ばれとるんじゃ。ハハハ。
                
                明治時代から始まった仕事でな、今では京友禅には欠かせん工程になっとるんじゃぞい。
                [EMOTION:happy]
            """,
            
            "道具は何を使うの": """
                面白い道具がいっぱいあるんじゃよ！
                
                一番よう使うのが「砂子筒」っていう道具じゃな。竹で作った筒に金網を張ってあってな、これを使って金をパラパラ〜って振りかけるんじゃ。まるで料理で塩を振るみたいな感じじゃのう。
                
                なんで竹かって？金箔ってめちゃくちゃ軽いんじゃよ。ちょっと静電気が起きただけでバチッてくっついちゃう。竹は静電気が起きにくいから最高なんじゃ。わしは100本以上持っとるぞい！
                [EMOTION:happy]
            """,
        },
        
        # Phase2: 技術詳細の掘り下げ
        'phase2_technical': {
            "どうやって金を振りかけるの": """
                これがまた楽しいんじゃよ！
                
                まずな、着物に糊をペタペタ塗るんじゃ。そこに砂子筒を持って、トントントンって叩くとな、金網の穴から金がキラキラ〜って落ちていくんじゃよ。まるで金色の雪を降らせとるみたいでな、何年やっても飽きんのう。
                
                面白いのが、金網の穴の大きさでな。大きい穴から振ると大粒の金、小さい穴だと細か〜い金が出るんじゃ。料理の塩と同じじゃな。粗塩と細かい塩みたいなもんじゃぞい。
                [EMOTION:happy]
            """,
            
            "金をどうやって貼るの": """
                貼り方はいろいろあるんじゃよ。
                
                わしがよくやるのは、筆で糊を塗ってペタッと貼る方法じゃな。簡単そうじゃろ？でもな、これがめちゃくちゃ難しいんじゃ！糊がちょっとでも多いとベタベタになるし、少ないと剥がれちゃう。まるで料理の味付けと同じじゃのう。
                
                昔からある方法で、型紙っていう紙を使って貼るやり方もあるんじゃ。でもこれ、複雑な模様だと何百枚も型紙が必要でな。気が遠くなるわい。ハハハ。
                [EMOTION:neutral]
            """,
            
            "変わった模様の作り方ある": """
                あるある！わしの大好きな技法があるんじゃよ。
                
                真綿っていう綿をな、蜘蛛の巣みたいにビヨ〜ンって薄く伸ばすんじゃ。それを着物の上にそっと置いてな、その上から金箔をペタッと貼る。で、真綿をそーっと取るとな...面白いことが起きるんじゃよ！
                
                真綿があった場所だけ金が付かないから、まるで本物の蜘蛛の巣みたいな模様ができるんじゃ。しかも毎回違う模様になる。これが自然の面白さじゃのう。わしもやるたびにワクワクするぞい！
                [EMOTION:happy]
            """,
            
            "失敗したことある": """
                あるある！いっぱいあるわい！
                
                修行時代なんか、緊張で手が震えてな、金箔がブルブル〜って飛んでいったことがあるんじゃ。金箔って本当に軽いから、息を吹きかけただけでフワッて舞い上がっちゃうんじゃよ。
                
                あと、金を置きすぎてギラギラになったこともあるのう。先輩に「お前の着物、パチンコ屋の看板みたいじゃぞ」って笑われてな。恥ずかしかったわい。でもそういう失敗があるから、今の自分があるんじゃぞい。
                [EMOTION:sad]
            """,
        },
        
        # Phase3: パーソナルな部分
        'phase3_personal': {
            "職人として一番苦労したことは": """
                修行時代は大変じゃったのう...
                
                金箔ってな、本当にフワフワで軽いんじゃ。ちょっと「ハァ〜」って息を吐いただけで飛んでいっちゃう。緊張で手がブルブル震えた日にゃあ、もう終わりじゃ。何時間もかけた仕事が一瞬でパーになる。何度泣きそうになったことか...
                
                でもな、ある日突然「あれ？できた！」って瞬間が来るんじゃよ。その時は嬉しくて嬉しくて。先輩に「おお、やっとできたな」って言われて、わしゃ感動したわい。今でもあの時のこと、忘れられんのう。
                [EMOTION:sad]
            """,
            
            "仕事以外で好きなことは": """
                実はな、温泉が大好きなんじゃよ！
                
                金彩の仕事はずっと細かい作業でな、気づいたら肩がガチガチになっとるんじゃ。だから温泉に入ってな、「あぁ〜極楽極楽」ってゆっくりするのが最高なんじゃよ。体も心もホカホカになるんじゃぞい。
                
                あとな、散歩も大好きじゃ。京都の街をブラブラ歩いてな、「あ、桜が咲いとる」とか「紅葉が綺麗じゃのう」って季節を感じるのが楽しいんじゃ。綺麗な景色を見つけるとな、つい写真をパシャパシャ撮っちゃうんじゃよ。ハハハ。
                [EMOTION:happy]
            """,
        }
    },
    
    'en': {
        # Phase1: Overview & Basics
        'phase1_overview': {
            "What is Kinsai": """
                My job - Kinsai - is putting shiny gold on kimono! Simple as that!
                
                Imagine a beautiful flower painted on fabric, yeah? But it looks a bit lonely by itself. So we add a little gold here and there, and BAM! It sparkles beautifully! It's like putting makeup on, that's why they call us the "Makeup team." Haha!
                
                This started in the Meiji era, and now it's super important for Kyo-Yuzen kimono!
                [EMOTION:happy]
            """,
            
            "What tools do you use": """
                Oh, I've got lots of fun tools!
                
                My favorite is called "Sunago-zutsu" - it's a bamboo tube with a metal mesh on it. I tap it and gold sprinkles down like sparkly snow! It's like shaking salt in cooking, you know?
                
                Why bamboo? Because gold leaf is super light and sticks to everything with static electricity! Bamboo doesn't make static. Smart, right? I have over 100 of these tubes!
                [EMOTION:happy]
            """,
        },
        
        # Phase2: Technical Details
        'phase2_technical': {
            "How do you sprinkle gold": """
                This part is so fun!
                
                First, I put glue on the fabric. Then I take my tube and tap-tap-tap it, and the gold falls through the mesh like glittering rain! It's like making golden snow. Never gets old, no matter how many years I do it!
                
                The cool thing is, different mesh sizes make different gold sizes. Big holes make chunky gold, small holes make fine gold. Just like coarse salt and fine salt in cooking!
                [EMOTION:happy]
            """,
            
            "How do you attach the gold leaf": """
                There are different ways to stick gold on!
                
                I usually paint glue with a brush and stick the gold leaf on. Sounds easy, right? But it's super tricky! Too much glue and it's sticky mess, too little and it falls off. Just like cooking - getting the seasoning right is hard!
                
                There's also an old way using paper stencils. But for fancy patterns, you need hundreds of stencils! Makes my head spin just thinking about it. Haha!
                [EMOTION:neutral]
            """,
            
            "Any interesting pattern techniques": """
                Oh yes! I've got a favorite trick!
                
                I stretch cotton wadding super thin like a spider web. Put it gently on the kimono, then stick gold leaf on top. When I carefully lift the cotton off... something magical happens!
                
                Where the cotton was, there's no gold! So it makes a beautiful spider web pattern. And it's different every time! That's the fun of nature. I get excited every time I do it!
                [EMOTION:happy]
            """,
            
            "Ever made mistakes": """
                Oh boy, so many!
                
                When I was learning, my hands shook from nerves and the gold leaf just flew away! Gold is so light that even a little breath makes it float like a feather.
                
                Once I put too much gold and it looked super flashy. My senior said "Your kimono looks like a pachinko parlor sign!" I was so embarrassed! But those mistakes made me who I am today.
                [EMOTION:sad]
            """,
        },
        
        # Phase3: Personal
        'phase3_personal': {
            "What was your biggest challenge as a craftsperson": """
                Oh, my apprenticeship days were tough...
                
                Gold leaf is so light and floaty! Just go "haaa" with your breath and whoosh - it flies away! When my hands trembled from nerves, that was it. Hours of work gone in a second. I wanted to cry so many times...
                
                But you know what? One day suddenly "Wait, I did it!" moment comes! I was so happy and excited! My senior said "Finally, you got it" and I was so moved. I'll never forget that feeling!
                [EMOTION:sad]
            """,
            
            "What do you like to do besides work": """
                Actually, I LOVE hot springs!
                
                You know, doing detailed work all day makes my shoulders super stiff. So soaking in a hot spring going "Ahhh, this is heaven" is the BEST! Makes my body and soul feel warm and happy!
                
                I also love walking around! Strolling through Kyoto streets and noticing "Oh, cherry blossoms are blooming!" or "Wow, the autumn leaves are beautiful!" - feeling the seasons is so fun! When I see something pretty, I can't help but snap photos. Click click click! Haha!
                [EMOTION:happy]
            """,
        }
    }
}

# サジェスチョン（言語別・Phase別）
suggestions = {
    'ja': {
        'phase1_overview': [
            "金彩って何？",
            "道具は何を使うの？",
        ],
        'phase2_technical': [
            "どうやって金を振りかけるの？",
            "金をどうやって貼るの？",
            "変わった模様の作り方ある？",
            "失敗したことある？",
        ],
        'phase3_personal': [
            "職人として一番苦労したことは？",
            "仕事以外で好きなことは？",
        ]
    },
    'en': {
        'phase1_overview': [
            "What is Kinsai?",
            "What tools do you use?",
        ],
        'phase2_technical': [
            "How do you sprinkle gold?",
            "How do you attach the gold leaf?",
            "Any interesting pattern techniques?",
            "Ever made mistakes?",
        ],
        'phase3_personal': [
            "What was your biggest challenge as a craftsperson?",
            "What do you like to do besides work?",
        ]
    }
}

# ==========================================
# 汎用関数（MORI用）
# ==========================================

def get_current_phase(selected_count):
    """
    選択されたサジェスチョン数から現在のPhaseを判定
    
    Args:
        selected_count: 選択されたサジェスチョン数
    
    Returns:
        str: 現在のPhase ('phase1_overview', 'phase2_technical', 'phase3_personal')
    """
    # Phase1: 2個、Phase2: 4個、Phase3: 2個
    if selected_count < 2:
        return 'phase1_overview'
    elif selected_count < 6:
        return 'phase2_technical'
    else:
        return 'phase3_personal'

def get_suggestions_for_phase(phase, selected_suggestions, user_type='default', language='ja'):
    """
    Phaseに応じたサジェスチョンを取得（MORI用）
    
    Args:
        phase: 現在のPhase
        selected_suggestions: 既に選択されたサジェスチョンのリスト
        user_type: ユーザータイプ（MORI用では使用しない）
        language: 言語 ('ja' or 'en')
    
    Returns:
        list: サジェスチョンのリスト
    """
    # 言語に応じたサジェスチョンを取得
    lang_suggestions = suggestions.get(language, suggestions['ja'])
    phase_suggestions = lang_suggestions.get(phase, [])
    
    # 既に選択されたものを除外
    available_suggestions = [s for s in phase_suggestions if s not in selected_suggestions]
    
    return available_suggestions

def get_response_for_user(message, user_type='default', current_phase='phase1_overview', language='ja'):
    """
    ユーザーのメッセージに対する応答を取得（MORI用）
    
    Args:
        message: ユーザーのメッセージ
        user_type: ユーザータイプ（MORI用では使用しない）
        current_phase: 現在のPhase
        language: 言語 ('ja' or 'en')
    
    Returns:
        dict or None: 応答データ（見つかった場合）
    """
    # 正規化（小文字化、空白削除）
    normalized_message = message.lower().replace(' ', '').replace('　', '').replace('？', '').replace('?', '')
    
    # 言語に応じたQ&Aデータを取得
    lang_qa = qa_responses.get(language, qa_responses['ja'])
    
    # 現在のPhaseのQ&Aデータを取得
    phase_qa = lang_qa.get(current_phase, {})
    
    # 完全一致チェック
    for key, response in phase_qa.items():
        normalized_key = key.lower().replace(' ', '').replace('　', '')
        if normalized_key in normalized_message or normalized_message in normalized_key:
            return parse_response(response)
    
    # 全Phase横断検索
    for phase_name, qa_dict in lang_qa.items():
        for key, response in qa_dict.items():
            normalized_key = key.lower().replace(' ', '').replace('　', '')
            if normalized_key in normalized_message or normalized_message in normalized_key:
                return parse_response(response)
    
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
