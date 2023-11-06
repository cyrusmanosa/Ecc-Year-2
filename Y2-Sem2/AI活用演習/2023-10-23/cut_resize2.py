# OpenCVをインポート
import cv2
# Matplotlibをインポート
import matplotlib.pyplot as plt

# 画像ファイルを読み込む
img = cv2.imread("./04_opencv_face/woman.png")

# 画像の一部を切り出し、サイズを変更し、ファイルに保存する
# y1,y2 x1,x2
im2 = img[250:650, 800:1150]
im2 = cv2.resize(im2, (400, 500))
cv2.imwrite("./04_opencv_face/cut_resizeWoman.png", im2)

# 変更した画像を表示する
plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()