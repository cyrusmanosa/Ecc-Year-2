import cv2
import matplotlib.pyplot as plt  # matplotlibライブラリからpyplotをインポート

# 画像ファイル名を指定し、cv2.imread()関数を使用して画像を読み込む
filename = "./2.png"
target_image = cv2.imread(filename)

# 画像を白黒反転させるために15から画像の値を引いて16で割る
target_image = 15 - target_image // 16

# 読み込んだ画像をグレースケールに変換する
target_image = cv2.cvtColor(target_image,cv2.COLOR_BGR2GRAY)

# cv2.resize()関数を使って画像サイズを8x8にリサイズする
target_image = cv2.resize(target_image,(8,8))

# pyplot.imshow()関数を使用して画像を表示する
plt.imshow(target_image,cmap="gray")  

# リサイズされた画像を出力する
print(target_image)

# 画像を表示する
plt.show()