# ライブラリをインポート
import MeCab

# オブジェクト生成
tagger = MeCab.Tagger()

# 形態素解析
result = tagger.parse("「鬼滅の刃」もいいけど、「鋼の錬金術師」も良い。")

# 解析結果を表示
print(type(result)) # 形態素解析の結果の型を確認
print(result)       # 形態素解析の結果を確認
