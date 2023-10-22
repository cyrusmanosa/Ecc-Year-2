# pandasライブラリを読み込む
import pandas as pd
# matplotlibライブラリをインポートする
import matplotlib.pyplot as plt
# 関数のインポート
from sklearn.model_selection import train_test_split
# Support Vector Machine (SVM)のインポート
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error


# csvの読み込み
df = pd.read_csv('./cinema-dataset.csv')


# ----散布図の確認   ----

# 散布図を描画する
# DataFrameのplotメソッドを使用し、SNS1列をx軸、sales列をy軸として散布図を描画する
df.plot(kind='scatter', x='SNS1', y='sales')
df.plot(kind='scatter', x='SNS2', y='sales')
df.plot(kind='scatter', x='actor', y='sales')
df.plot(kind='scatter', x='original', y='sales')

# 描画したグラフを表示する
# plt.show()


# ----散布図の確認END----



# 特微量の取り出し
x = df.loc[:, "SNS1":"original"]


# 正解ラベルの取り出し
y = df["sales"]


# 訓練データとテストデータに分割する
# データの分割
x_train, x_test, y_train, y_test = train_test_split(x , y , test_size = 0.2)


# モデルの準備
# kernel="linear"で線形カーネルを使用する
model = SVR(kernel="linear")


# SVMで学習を行う
model.fit(x_train, y_train)


# 予測
# 新しいデータ（SNS1、SNS2、actor、original）を渡して予測を行う
new_data = [[150,700,300,1]]
pred = model.predict(x_test) # 予測
print(f"予測値：{pred}")


# モデルの評価
# テストデータで学習モデルを評価し、スコアを計算する
print(f"score：{model.score(x_test,y_test)}")


# テストデータを使って学習済みモデルの予測結果と正解ラベルとの平均絶対誤差を計算する
mae = mean_absolute_error(y_true=y_test, y_pred=pred) #正解ラベルと予測結果の誤差平均を求める
print(f"平均絶対誤差: {mae}")


# モデルの係数を表示する
print(f"計算式の係数:{model.coef_}")


# 計算式の切片を表示する
print(f"計算式の切片:{model.intercept_}")

# データフレーム作成
# モデルの係数を利用してDataFrameを作成する
tmp = pd.DataFrame(model.coef_)

# 列名を元のデータの列名に設定する
tmp.columns = x_train.columns

# DataFrameを出力する
print(tmp)