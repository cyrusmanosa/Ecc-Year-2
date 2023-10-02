import pandas as pd
from sklearn.svm import SVC # モジュールのインポート

# データの読み込み
df = pd.read_csv("./wine_dataset.csv")

# 特微量を抽出して変数xに代入
x = df[["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol"]]

# 正解データを抽出して変数tに代入
t = df["quality"]


# 訓練用データとテスト用に分割
## テストデータの割合を30%
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x , t , test_size=0.5 )

# モデルの準備
model = SVC()

# モデルの学習
model.fit(x_train,y_train)


# モデルを評価
score = model.score(x_test,y_test)
print(f"正解率は{score}")