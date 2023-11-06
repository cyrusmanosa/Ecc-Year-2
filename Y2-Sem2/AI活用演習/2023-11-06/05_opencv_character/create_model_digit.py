# 必要なモジュールのインポート
from sklearn.model_selection import train_test_split   # データをトレーニング用とテスト用に分割するための関数
from sklearn import datasets  # 機械学習に必要なモジュールのインポート
from sklearn.svm import SVC #機械学習モデル

# 手書き数字のデータセットをロードする
digits = datasets.load_digits()

# 手書き数字の画像データと正解ラベルを変数に格納する
x = digits.images
y = digits.target

# 手書き数字の画像データを1次元配列に変換する
x = x.reshape((-1,64))

# データセットをトレーニング用とテスト用に分割する
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2)

# 機械学習モデルを作成し、トレーニングデータを使って学習する
model = SVC()
model.fit(x_train, y_train)

# テストデータを使って、作成した機械学習モデルの予測精度を評価する
print(model.score(x_test,y_test))

# 学習した機械学習モデルを保存する
import pickle
with open("create_model_digit.pkl","wb") as fp:
    pickle.dump(model,fp)