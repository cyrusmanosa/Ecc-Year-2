# Matplotlibとscikit-learnから必要なモジュールをインポートする
import matplotlib.pyplot as plt
from sklearn import datasets

# scikit-learnに搭載された数字画像データセットを読み込む
digits = datasets.load_digits()

# 15個の数字画像を描画するループを回す
for i in range(50):
    
    # 3x5のグリッドのi+1番目の場所にプロットする
    # plt.subplot(3,5,i+1)
    
    # 5x10のグリッドのi+1番目の場所にプロットする
    plt.subplot(5,10,i+1)
    # 軸を非表示にする
    plt.axis("off")
    # タイトルにi番目の画像のラベル（答え）を表示する
    plt.title(str(digits.target[i]))
    # i番目の画像をグレースケールで表示する
    plt.imshow(digits.images[i] , cmap="gray")

# 描画する
plt.show()