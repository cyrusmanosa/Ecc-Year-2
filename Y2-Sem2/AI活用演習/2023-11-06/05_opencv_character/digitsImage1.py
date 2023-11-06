# scikit-learnライブラリからdatasetsをインポート
import sklearn.datasets  
# matplotlibライブラリからpyplotをインポート
import matplotlib.pyplot as plt

# digitsデータセットをロード
digits = sklearn.datasets.load_digits()  

# digitsの画像データの0番目のデータをグレースケールで表示
plt.imshow(digits.images[0],cmap="gray")

# 画像を表示
plt.show()