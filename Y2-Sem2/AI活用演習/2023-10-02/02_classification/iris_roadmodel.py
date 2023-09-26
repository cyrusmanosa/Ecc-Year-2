

""" 修正してください """
# 学習済みモデルの準備
model = None


# 確認用データの準備
# 正解は「Iris-virginica」
new_ayame = [[7.4,2.8,6.1,1.9]]

# 予想
pre = model.predict(new_ayame)  # 学習済みのモデルを用いて予測を行う
print(f"予想は{pre}")  # 予測結果を表示する




