# pandasライブラリをインポート
import pandas as pd

# Ki_vs_Ta.csvファイルを読み込み、データフレームに変換する
df = pd.read_csv("Ki_vs_Ta.csv")

# 上位3件の表示
print(df.head(3))

# 特微量を抽出して変数xに代入
x = df[["身長","体重","年代"]]

# 正解データを抽出して変数tに代入
t = df["派閥"]

# モデルの準備
from sklearn.svm import SVC # モジュールのインポート
model = SVC()

# モデルの学習
model.fit(x,t)

# 新データ(2次元リスト)：身長170cm , 体重70kg , 年代20代
taro = [[170,70,20]]

# taroはどちらに分類されるか予想
pre = model.predict(taro)
print(f"予想は{pre}")

# 正解率の計算
score = model.score(x,t)
print(f"正解率は{score}")