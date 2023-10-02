# pandasライブラリをインポート
import pandas as pd

# Support Vector Machine (SVM)のインポート
from sklearn.svm import SVC # モジュールのインポート

# iris-dataset.csvファイルを読み込み、データフレームに変換する
df = pd.read_csv("iris-dataset.csv")

# 特微量を抽出して変数xに代入
x = df[["がく片長さ","がく片幅","花弁長さ","花弁幅"]]

# 正解データを抽出して変数tに代入
t = df["種類"]

# Support Vector Machine (SVM)のモデルを生成する
model = SVC()

# SVMで学習を行う
model.fit(x,t)

# 予想
pre = model.predict([x.iloc[0]])  # 学習済みのモデルを用いて予測を行う
print(f"予想は{pre}")  # 予測結果を表示する

# 正解率の計算
score = model.score(x,t)
print(f"正解率は{score}")


''' データセットを学習用とテスト用に分割し、再度学習を行う '''
# 関数のインポート
from sklearn.model_selection import train_test_split

# データの分割
x_train, x_test, y_train, y_test = train_test_split(x , t , test_size=0.3 )

# Support Vector Machine (SVM)のモデルを生成する
model = SVC()

# SVMで再度学習を行う
model.fit(x_train,y_train)

# テストデータに対する正解率を算出
test_score = model.score(x_test,y_test)


# 正解率を出力
print(f"Test_正解率は{test_score}")


import pickle

# iris_model.pklファイルをバイトモードで開き、保存する。
with open('iris_model.pkl', 'wb') as f:
    # モデル情報の保存
    pickle.dump(model, f)