import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error

# csvの読み込み
df = pd.read_csv('./wether_dataset2.csv')

# 根據條件進行資料處理
df.loc[(df['月'] == 3) | (df['月'] == 4) | (df['月'] == 5), '季節'] = 2
df.loc[(df['月'] == 7) | (df['月'] == 6) | (df['月'] == 8), '季節'] = 1
df.loc[(df['月'] == 9) | (df['月'] == 10) | (df['月'] == 11), '季節'] = 3
df.loc[(df['月'] == 2) | (df['月'] == 1) | (df['月'] == 12), '季節'] = 4

# 寫入CSV文件
df.to_csv('wether_dataset2.csv', index=False)

# 特微量の取り出し
x = df[["年","月","日","季節"]]

# 正解ラベルの取り出し
y = df["平均気温(℃)"]

# 訓練データとテストデータに分割
x_train, x_test, y_train, y_test = train_test_split(x , y , test_size = 0.2)

# モデルの準備
# kernel="linear"で線形カーネルを使用する
model = SVR(kernel="linear")

# SVMで学習を行う
model.fit(x_train, y_train)

# 予測
new_data = [[2023,12,31,4]]
pred = model.predict(x_test) 
# pred = model.predict(new_data) 

print(f"明日の平均気温の予測値：{pred}")

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