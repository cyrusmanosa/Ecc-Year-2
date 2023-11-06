# Scikit-learnからデータセットをインポート
import sklearn.datasets
# 手書き数字のデータセットを読み込み
digits = sklearn.datasets.load_digits()

# データの個数を表示
print(f"データの個数={len(digits.images)}")

# 最初の画像データを表示
print(f"画像データ=\n{digits.images[0]}")

# 最初の画像データに対応する数字を表示
print(f"何のデータか={digits.target[0]}")