import pandas as pd
import matplotlib.pyplot as plt
# 関数のインポート
from sklearn.model_selection import train_test_split
# Support Vector Machine (SVM)のインポート
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error



# csvの読み込み
df = pd.read_csv('./wether_dataset.csv')

# 特微量の取り出し
x = df.loc[:, "年":"日"]

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
new_data = [[2024,1,1]]
pred = model.predict(new_data) 
print(f"明日の平均気温の予測値：{pred}")