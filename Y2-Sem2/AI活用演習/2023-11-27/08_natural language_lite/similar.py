# gensimモジュールからWord2Vecをインポート
from gensim.models import word2vec

# 読み込むモデルのパスを指定して、Word2Vecモデルを読み込む
model = word2vec.Word2Vec.load("./wiki.model")

# モデルを使用して類似度が高い単語のリストを取得
results = model.wv.most_similar(positive=['文字','こんにちは'])

# 結果を表示する
for result in results :
    print(result)
