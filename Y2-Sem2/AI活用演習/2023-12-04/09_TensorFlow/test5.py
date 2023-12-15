# OpenCVという画像処理ライブラリを読み込みます。これを使って画像の前処理を行います。
import cv2

# matplotlibのpyplotを使って、画像を表示するための準備をします。
from matplotlib import pyplot as plt

# 前処理
# まず、予測したい画像を読み込みます。
target_image = cv2.imread("./22AAD440-8A8A-4A38-9C4B-84E27FFBD325_1_105_c.jpeg")

# 読み込んだ画像をグレースケール（白黒）に変換します。色は必要ないため、計算を簡単にするために変換します。
target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2GRAY)

# 画像を28x28ピクセルにリサイズします。これはモデルが28x28ピクセルの画像を想定しているからです。
target_image = cv2.resize(target_image, (28, 28))

# 色の範囲を0から1に変換します（通常、色は0から255の範囲です）。
target_image = target_image / 255.0

# モデルの予測
# 前処理した画像をモデルに入力して、何の数字であるかを予測します。
prediction = model.predict(target_image.reshape(1, 28, 28, 1))

# 前処理した画像を表示します。
plt.imshow(target_image, cmap='gray')
plt.show()

# 予測結果を表示します。np.argmaxは一番高い確率のものを選びます。これがモデルが予測した数字です。
print(f"Model prediction: {np.argmax(prediction[0])}")