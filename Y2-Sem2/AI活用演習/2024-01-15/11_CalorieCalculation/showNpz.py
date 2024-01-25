import matplotlib.pyplot as plt  # グラフを描画するためのモジュール
import numpy as np               # 数学的な操作や配列を扱うためのモジュール

# npzファイルから画像データを読み込む
photos = np.load('image/photos.npz')

x = photos['x']# 画像データをxに代入
# ラベルデータをyに代入
y = photos['y']

# 画像を表示するための領域を設定
plt.figure(figsize=(10, 10))

# 25枚の画像を表示する
for i in range(25):
    # 5x5のグリッドの中に画像を表示するための領域を指定
    plt.subplot(5, 5, i + 1)
    # 画像の上にラベルを表示
    plt.title(y[i])
    # 画像を表示
    plt.imshow(x[i])

# グラフを画面に表示
plt.show()