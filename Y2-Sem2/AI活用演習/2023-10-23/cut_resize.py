# OpenCVをインポート
import cv2
# Matplotlibをインポート
import matplotlib.pyplot as plt

# 画像ファイルを読み込む
img = cv2.imread("./04_opencv_face/man.jpg")

# 画像の一部を切り出し、サイズを変更し、ファイルに保存する
im2 = img[200:500, 900:1200]
im2 = cv2.resize(im2, (400, 400))
cv2.imwrite("./04_opencv_face/cut_resize.png", im2)

# 変更した画像を表示する
plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()