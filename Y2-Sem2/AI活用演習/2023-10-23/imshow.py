# matplotlibとOpenCVをインポート
import matplotlib.pyplot as plt
import cv2

# 画像ファイルを読み込む
img = cv2.imread("./04_opencv_face/woman.png")

# BGRからRGBに変換して、画像を表示する
# plt.axis("off")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# 画像を表示する
plt.show()