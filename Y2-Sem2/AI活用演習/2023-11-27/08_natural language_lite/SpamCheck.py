from gensim.models import word2vec
import MeCab

# Word2Vecモデルの読み込み
model = word2vec.Word2Vec.load("./wiki.model")
# MeCabの設定
tagger = MeCab.Tagger("./NEologd.20200910-u.dic")

# スパム判定を行う関数の定義
def print_emargency(text):
    print(f"メッセージ内容：{text}")
    # テキストを形態素解析して単語ごとに処理
    node = tagger.parseToNode(text)
    while node is not None:
        # 単語の情報を取得
        fields = node.feature.split(",")
        # 名詞・動詞・形容詞に対してにのみスパム判定を行う
        if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞':
            # print(f"{node.surface}")
            #   2つの類似度を計算して表示
            similarity = model.wv.similarity(node.surface, '遊び')
            if similarity >= 0.9:
                break
        # 次の単語へ
        node = node.next
    # スパム判定結果の表示
    if similarity <= 0.9:
        print("スパムを検知しました")

print("--------------------")
# メッセージのスパム判定を行う
print_emargency("このゲームもうやめろ、二度と来るな")
print("--------------------")
print_emargency("バカ、ゴミ")
print("--------------------")
print_emargency("楽しかったです、また一緒にゲームで遊びましょう")
print("--------------------")
print_emargency("死ね")
print("--------------------")