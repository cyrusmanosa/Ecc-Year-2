# gensimモジュールからword2vecをインポートする
from gensim.models import word2vec

# テキストコーパスを指定して、分かち書き済みの文書を読み込む
sentences = word2vec.Text8Corpus('./topic_wakati.txt')

# 分かち書き済みの文書からWord2Vecモデルを学習したものを作成
model = word2vec.Word2Vec(sentences, sg=0, vector_size=100, window=5, min_count=5)

# モデルを保存する
model.save("./text.model")