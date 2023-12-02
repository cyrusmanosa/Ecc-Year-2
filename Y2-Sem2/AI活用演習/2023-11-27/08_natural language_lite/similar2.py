# gensimモジュールからWord2Vecをインポート
from gensim.models import word2vec

# MeCabのインポート
import MeCab

# 読み込むモデルのパスを指定して、Word2Vecモデルを読み込む
model = word2vec.Word2Vec.load("./wiki.model")

# MeCabのTaggerを作成し、NEologd辞書を使用するように設定
tagger = MeCab.Tagger("./NEologd.20200910-u.dic")

# 文字列を受け取って処理する関数を定義
def print_emargency(text):
    print(f"メッセージ内容：{text}")

    # MeCabを使って形態素解析を行い、単語ごとに処理
    node = tagger.parseToNode(text)
    
    while node is not None:
        # 単語の情報を取得
        fields = node.feature.split(",")
        # 名詞・動詞・形容詞の場合にのみ類似度を計算して表示
        if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞':
            print(f"「{node.surface}」の至急との関連度は")
            #   2つの類似度を計算して表示
            print(model.wv.similarity(node.surface,'至急'))

        # 次の単語に進む
        node = node.next

# 例文を入力してprint_emargency関数を呼び出す
print_emargency("PCが起動しなくなりました、急いでいます")
print_emargency("使い方がよくわかりません")
